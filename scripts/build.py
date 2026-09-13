"""Generate standalone references, chat adapters and deterministic release ZIPs."""

from __future__ import annotations

import argparse
import hashlib
import zipfile
from pathlib import Path

from project import CATALOG, LINK, ROOT, frontmatter, skill_files


def inline_links(text: str) -> str:
    return LINK.sub(lambda m: m.group(0) if m.group(2).startswith(("http://", "https://", "#"))
                    else f"{m.group(1)}（内容已附在本文件中）", text)


def generated_files(root: Path) -> dict[Path, bytes]:
    output = {}
    common = [root / "shared" / name for name in (
        "review-contract.md", "context-template.md", "author-experience.md", "author-sources.md")]
    intro = ("# 交易决策复核 · 聊天适配版\n\n"
             "请按本文件处理我随后提供的任务和材料。按任务选择对应模块；"
             "示例全部为虚构，不作为我的规则、持仓或操作。没有外部文件读取、行情或下单依赖。\n\n")
    common_text = "\n\n".join(inline_links(p.read_text(encoding="utf-8").strip()) for p in common)
    sections = []
    for name, (title, description) in CATALOG.items():
        folder = root / "skills" / name
        for source in common:
            output[folder / "references" / source.name] = source.read_bytes()
        output[folder / "LICENSE"] = (root / "LICENSE").read_bytes()
        metadata = (f'interface:\n  display_name: "{title}"\n'
                    f'  short_description: "{description}"\n'
                    f'  default_prompt: "请用 ${name} 根据我提供的材料完成{title}。"\n')
        output[folder / "agents" / "openai.yaml"] = metadata.encode("utf-8")
        _, body = frontmatter(folder / "SKILL.md")
        extras = [folder / "references" / "examples.md", *sorted((folder / "templates").glob("*.md"))]
        section = inline_links(body) + "\n\n" + "\n\n".join(
            inline_links(p.read_text(encoding="utf-8").strip()) for p in extras)
        sections.append(section)
        output[root / "adapters" / "plain-chat" / f"{name}.md"] = (
            intro + common_text + "\n\n" + section + "\n").encode("utf-8")
    routing = "## 选择模块\n\n" + "\n".join(f"- {name}：{v[0]}。" for name, v in CATALOG.items())
    suite = intro + routing + "\n\n" + common_text + "\n\n" + "\n\n".join(sections) + "\n"
    output[root / "adapters" / "plain-chat" / "trade-review-suite.md"] = suite.encode("utf-8")
    output[root / "adapters" / "chatgpt" / "knowledge.md"] = suite.encode("utf-8")
    return output


def zip_bytes(files: dict[str, bytes]) -> bytes:
    from io import BytesIO
    buffer = BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    return buffer.getvalue()


def release_files(root: Path) -> dict[Path, bytes]:
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    output = {}
    bundle = {}
    for name in CATALOG:
        folder = root / "skills" / name
        files = {f"{name}/{p.relative_to(folder).as_posix()}": p.read_bytes() for p in skill_files(folder)}
        output[root / "dist" / f"{name}.zip"] = zip_bytes(files)
        bundle.update({f"trade-review-skills/skills/{path}": data for path, data in files.items()})
    # The collection ZIP is for extraction, never a single-skill upload.
    for rel in ("README.md", "README.en.md", "INSTALL.md", "LICENSE", "VERSION", "docs/installation.md",
                "docs/compatibility.md", "docs/validation.md", "examples/walkthrough.md"):
        bundle[f"trade-review-skills/{rel}"] = (root / rel).read_bytes()
    for path in sorted((root / "adapters").rglob("*.md")):
        bundle[f"trade-review-skills/{path.relative_to(root).as_posix()}"] = path.read_bytes()
    for path in sorted((root / "shared").glob("*.md")):
        bundle[f"trade-review-skills/{path.relative_to(root).as_posix()}"] = path.read_bytes()
    # Include the maintenance helpers linked by the source README in the extracted collection.
    for rel in ("CONTRIBUTING.md", "CHANGELOG.md", "AGENTS.md"):
        bundle[f"trade-review-skills/{rel}"] = (root / rel).read_bytes()
    for dirname in ("scripts", "tests"):
        for path in sorted((root / dirname).glob("*.py")):
            bundle[f"trade-review-skills/{path.relative_to(root).as_posix()}"] = path.read_bytes()
    for path in sorted((root / "evals").rglob("*")):
        if path.is_file() and not path.is_symlink() and path.suffix in {".md", ".json"}:
            bundle[f"trade-review-skills/{path.relative_to(root).as_posix()}"] = path.read_bytes()
    output[root / "dist" / f"trade-review-skills-{version}.zip"] = zip_bytes(bundle)
    output[root / "dist" / "chatgpt-instructions.md"] = (root / "adapters/chatgpt/instructions.md").read_bytes()
    output[root / "dist" / "chatgpt-knowledge.md"] = (root / "adapters/chatgpt/knowledge.md").read_bytes()
    output[root / "dist" / "trade-review-suite.md"] = (root / "adapters/plain-chat/trade-review-suite.md").read_bytes()
    hashes = "".join(f"{hashlib.sha256(data).hexdigest()}  {path.name}\n" for path, data in sorted(output.items()))
    output[root / "dist" / "SHA256SUMS"] = hashes.encode()
    return output


def write_files(files: dict[Path, bytes], check: bool = False) -> None:
    for path, data in files.items():
        if path.is_symlink() or any(parent.is_symlink() for parent in path.parents):
            raise ValueError(f"Refusing generated output through symlink: {path}")
        if check:
            if not path.is_file() or path.read_bytes() != data:
                raise ValueError(f"Generated file is missing or stale: {path}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)


def build(root: Path = ROOT, check: bool = False) -> None:
    write_files(generated_files(root), check)
    write_files(release_files(root), check)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated files without changing them")
    args = parser.parse_args()
    build(check=args.check)
    print("Generated files and release assets are current." if args.check else "Built 5 standalone skills, text adapters and release assets in dist/.")


if __name__ == "__main__":
    main()
