"""Install standalone skills locally without network access or overwriting changes."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from project import CATALOG, DISTRIBUTIONS, ROOT, skill_files
from validate import validate_skill

TARGETS = {"codex": ".agents/skills", "claude-code": ".claude/skills", "cursor": ".cursor/skills"}


def install(destination: Path, names: list[str], dry_run: bool = False, root: Path = ROOT) -> list[str]:
    if len(names) != len(set(names)) or not names or any(name not in DISTRIBUTIONS for name in names):
        raise ValueError("Select unique skill names from the catalog")
    destination = destination.expanduser().absolute()
    if any(p.is_symlink() for p in (destination, *destination.parents)):
        raise ValueError("Installation destination must not traverse symbolic links")
    if any(p.exists() and not p.is_dir() for p in (destination, *destination.parents)):
        raise ValueError("Installation destination must be a directory")
    changes = []
    messages = []
    # Preflight every destination before creating anything.
    for name in names:
        source = root / "skills" / name
        validate_skill(source)
        target = destination / name
        if target.is_symlink():
            raise ValueError(f"Refusing symlink destination: {target}")
        if target.exists():
            expected = {p.relative_to(source): p.read_bytes() for p in skill_files(source)}
            actual = {p.relative_to(target): p.read_bytes() for p in skill_files(target)}
            if expected != actual:
                raise ValueError(f"Existing skill differs; move it to a backup location before reinstalling: {target}")
            messages.append(f"Unchanged: {target}")
        else:
            changes.append((source, target))
            messages.append(f"{'Would install' if dry_run else 'Installed'}: {target}")
    if not dry_run:
        for source, target in changes:
            # copytree refuses a destination created concurrently; it never merges into one.
            shutil.copytree(source, target)
    return messages


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--target", choices=TARGETS, help="User-level skill directory")
    destination.add_argument("--dest", type=Path, help="Explicit skills directory, including project-local directories")
    parser.add_argument("--skill", action="append", choices=DISTRIBUTIONS,
                        help="Repeat to select; defaults to five independent skills; select trade-review-suite for one entry")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    path = args.dest if args.dest else Path.home() / TARGETS[args.target]
    try:
        for message in install(path, args.skill or list(CATALOG), args.dry_run):
            print(message)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Install stopped: {exc}\n")


if __name__ == "__main__":
    main()
