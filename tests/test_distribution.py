from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build import build, generated_files, inline_links, release_files
from install import install
from project import CATALOG, LINK, check_local_links
from validate import validate, validate_skill


class DistributionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()

    def copy_project(self) -> Path:
        root = self.base / "project"
        shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", ".scratch", "dist", "__pycache__"))
        return root

    def test_each_zip_is_independently_usable(self) -> None:
        assets = release_files(ROOT)
        for name in CATALOG:
            from io import BytesIO
            with zipfile.ZipFile(BytesIO(assets[ROOT / "dist" / f"{name}.zip"])) as archive:
                names = archive.namelist()
                self.assertEqual({n.split("/")[0] for n in names}, {name})
                self.assertTrue(all(".." not in Path(n).parts and not Path(n).is_absolute() for n in names))
                archive.extractall(self.base / name)
            folder = self.base / name / name
            validate_skill(folder)
            for source in (ROOT / "shared").glob("*.md"):
                self.assertEqual((folder / "references" / source.name).read_bytes(), source.read_bytes())

    def test_release_checksums_and_reproducibility(self) -> None:
        first, second = release_files(ROOT), release_files(ROOT)
        self.assertEqual(first, second)
        sums = first[ROOT / "dist/SHA256SUMS"].decode().splitlines()
        self.assertEqual(len(sums), len(first) - 1)
        for line in sums:
            digest, name = line.split("  ")
            self.assertEqual(digest, hashlib.sha256(first[ROOT / "dist" / name]).hexdigest())

    def test_collection_links_survive_extraction(self) -> None:
        from io import BytesIO
        assets = release_files(ROOT)
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        with zipfile.ZipFile(BytesIO(assets[ROOT / "dist" / f"trade-review-skills-{version}.zip"])) as archive:
            archive.extractall(self.base)
        root = self.base / "trade-review-skills"
        for path in root.rglob("*.md"):
            check_local_links(path, root)

    def test_shared_edit_requires_regeneration(self) -> None:
        root = self.copy_project()
        build(root)
        shared = root / "shared/review-contract.md"
        shared.write_text(shared.read_text(encoding="utf-8") + "\n新增维护规则。\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "stale"):
            build(root, check=True)
        build(root)
        validate(root)
        self.assertIn("新增维护规则", (root / "adapters/plain-chat/trade-plan-check.md").read_text(encoding="utf-8"))

    def test_author_reference_update_reaches_every_distribution(self) -> None:
        root = self.copy_project()
        build(root)
        source = root / "shared/author-experience.md"
        updated = source.read_text(encoding="utf-8") + "\n虚构维护试验：新增适用范围。\n"
        # Exercise a Windows-style edit on every host: ZIPs preserve source bytes,
        # while self-contained text adapters normalize newlines when reading.
        source.write_bytes(updated.replace("\n", "\r\n").encode("utf-8"))
        with self.assertRaisesRegex(ValueError, "stale"):
            build(root, check=True)
        build(root)
        validate(root)
        for name in CATALOG:
            with zipfile.ZipFile(root / "dist" / f"{name}.zip") as archive:
                self.assertEqual(archive.read(f"{name}/references/author-experience.md"), source.read_bytes())
        for path in (root / "adapters").rglob("*.md"):
            if path.name != "instructions.md":
                self.assertIn(inline_links(updated.strip()), path.read_text(encoding="utf-8"))

    def test_missing_or_escaping_reference_is_rejected(self) -> None:
        root = self.copy_project()
        skill = root / "skills/trade-plan-check"
        path = skill / "SKILL.md"
        body = path.read_text(encoding="utf-8")
        path.write_text(body + "\n[missing](references/missing.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Missing linked"):
            validate_skill(skill)
        path.write_text(body + "\n[outside](../../README.md)\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "escapes"):
            validate_skill(skill)

    def test_private_or_executable_payload_is_rejected(self) -> None:
        root = self.copy_project()
        skill = root / "skills/trade-plan-check"
        for name in (".env", "download.py", "account.csv"):
            path = skill / name
            path.write_text("synthetic fixture", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Unexpected runtime file"):
                validate_skill(skill)
            path.unlink()

    def test_text_adapters_have_no_file_dependency(self) -> None:
        files = generated_files(ROOT)
        for name in CATALOG:
            text = files[ROOT / "adapters/plain-chat" / f"{name}.md"].decode()
            for _, target in LINK.findall(text):
                self.assertTrue(target.startswith(("https://", "http://", "#")), target)
            for source in (ROOT / "shared").glob("*.md"):
                self.assertIn(inline_links(source.read_text(encoding="utf-8").strip()), text)
            self.assertIn("# 虚构示例", text)

    def test_dry_run_creates_nothing(self) -> None:
        dest = self.base / "not-created/skills"
        install(dest, list(CATALOG), dry_run=True)
        self.assertFalse(dest.parent.exists())

    def test_install_is_complete_and_idempotent(self) -> None:
        for layout in (".agents/skills", ".claude/skills", ".cursor/skills"):
            dest = self.base / layout
            messages = install(dest, list(CATALOG))
            self.assertEqual(len(messages), 5)
            for name in CATALOG:
                validate_skill(dest / name)
            snapshots = {p: p.stat().st_mtime_ns for p in dest.rglob("*") if p.is_file()}
            self.assertTrue(all(m.startswith("Unchanged:") for m in install(dest, list(CATALOG))))
            self.assertEqual(snapshots, {p: p.stat().st_mtime_ns for p in snapshots})

    def test_one_conflict_prevents_other_installations(self) -> None:
        dest = self.base / "skills"
        existing = dest / "trade-rule-cards"
        shutil.copytree(ROOT / "skills/trade-rule-cards", existing)
        original = "user customization\n"
        (existing / "SKILL.md").write_text(original, encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "differs"):
            install(dest, list(CATALOG))
        self.assertEqual({p.name for p in dest.iterdir()}, {"trade-rule-cards"})
        self.assertEqual((existing / "SKILL.md").read_text(encoding="utf-8"), original)

    def test_unknown_or_duplicate_skill_is_rejected(self) -> None:
        dest = self.base / "skills"
        for names in (["../escape"], [], ["trade-plan-check", "trade-plan-check"]):
            with self.assertRaises(ValueError):
                install(dest, names)
        self.assertFalse(dest.exists())

    @unittest.skipIf(sys.platform == "win32", "Creating test symlinks may require Windows admin privileges")
    def test_symlinks_are_rejected(self) -> None:
        root = self.copy_project()
        outside = self.base / "outside.md"
        outside.write_text("synthetic private fixture", encoding="utf-8")
        link = root / "skills/trade-plan-check/references/hidden.md"
        link.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            validate_skill(root / "skills/trade-plan-check")
        dest = self.base / "linked-skills"
        actual = self.base / "actual-skills"
        actual.mkdir()
        dest.symlink_to(actual, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symbolic links"):
            install(dest, ["trade-plan-check"])
        self.assertEqual(list(actual.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
