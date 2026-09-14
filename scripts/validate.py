"""Check package structure, references, generated parity and release contents."""

from __future__ import annotations

import re
import zipfile
from pathlib import Path

from build import build
from project import CATALOG, DISTRIBUTIONS, ROOT, SUITE_NAME, check_local_links, frontmatter, skill_files


def validate_skill(folder: Path) -> None:
    metadata, body = frontmatter(folder / "SKILL.md")
    name = metadata.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64 or name != folder.name:
        raise ValueError(f"Invalid skill name: {folder}")
    description = metadata.get("description", "")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        raise ValueError(f"Invalid description: {folder}")
    if metadata.get("license") != "MIT" or not body or len(body.splitlines()) >= 500:
        raise ValueError(f"Invalid skill body/license: {folder}")
    required = {"SKILL.md", "LICENSE", "references/review-contract.md", "references/context-template.md",
                "references/author-experience.md", "references/author-sources.md",
                "references/examples.md", "agents/openai.yaml"}
    files = skill_files(folder)
    if name == SUITE_NAME:
        required.update(f"modules/{module}.md" for module in CATALOG)
    if not required.issubset({p.relative_to(folder).as_posix() for p in files}):
        raise ValueError(f"Missing standalone resources: {folder}")
    for path in files:
        if path.suffix == ".md":
            check_local_links(path, folder)


def validate(root: Path = ROOT) -> None:
    if {p.name for p in (root / "skills").iterdir()} != set(DISTRIBUTIONS):
        raise ValueError("Expected five independent skills and one unified suite")
    for name in DISTRIBUTIONS:
        validate_skill(root / "skills" / name)
    build(root, check=True)
    for dirname in ("docs", "examples", "shared", "adapters", "evals"):
        for path in (root / dirname).rglob("*.md"):
            check_local_links(path, root)
    for path in root.glob("*.md"):
        check_local_links(path, root)
    for name in CATALOG:
        with zipfile.ZipFile(root / "dist" / f"{name}.zip") as archive:
            expected = {f"{name}/{p.relative_to(root / 'skills' / name).as_posix()}"
                        for p in skill_files(root / "skills" / name)}
            if set(archive.namelist()) != expected or archive.testzip() is not None:
                raise ValueError(f"Incorrect standalone ZIP: {name}")
    folder = root / "skills" / SUITE_NAME
    for filename, prefix in ((f"{SUITE_NAME}.zip", ""), (f"{SUITE_NAME}-folder.zip", f"{SUITE_NAME}/")):
        with zipfile.ZipFile(root / "dist" / filename) as archive:
            expected = {prefix + p.relative_to(folder).as_posix() for p in skill_files(folder)}
            if set(archive.namelist()) != expected or archive.testzip() is not None:
                raise ValueError(f"Incorrect suite ZIP: {filename}")


if __name__ == "__main__":
    validate()
    print("PASS: 5 standalone skills, 1 unified suite, both suite ZIP layouts, local references, generated adapters and checksums.")
