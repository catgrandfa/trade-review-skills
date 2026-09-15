"""Shared build helpers; runtime skills contain no Python dependency."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = {
    "trade-plan-check": ("开单前计划核对", "核对开单前的判断依据、触发条件、风险安排与原计划的一致性"),
    "trade-execution-review": ("交易行为复盘", "对照事前计划与实际操作，分别复盘判断依据、执行过程和盈亏结果"),
    "trade-source-check": ("观点完整性检查", "核对交易观点的原文、适用前提和限制，发现引用遗漏与理解偏差"),
    "trade-scenario-plan": ("交易预案整理", "把已有判断整理成条件分支，保留原始依据、待定义项和草案状态"),
    "trade-rule-cards": ("心法转规则卡", "把经验整理成有场景、来源和采用状态的规则卡，供决策时核对"),
}
SUITE_NAME = "trade-review-suite"
DISTRIBUTIONS = {
    **CATALOG,
    SUITE_NAME: ("交易决策复核一体版", "按任务调用计划核对、执行复盘、观点检查、预案整理与规则卡五个模块"),
}
DEFAULT_PROMPTS = {
    "trade-plan-check": "核对我准备做的这一步与原计划是否一致，先说关键差异和缺项",
    "trade-execution-review": "复盘我已经做过的操作，分清执行情况和盈亏结果",
    "trade-source-check": "对照我提供的原文，看看我的理解有没有遗漏条件",
    "trade-scenario-plan": "把我给的条件和打算整理成预案，没决定的地方留待定",
    "trade-rule-cards": "把我提供的经验做成提醒卡，保留来源和是否采用的状态",
    SUITE_NAME: "根据我描述的事情选择需要的功能，先说能确定的结论和关键缺项",
}
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def frontmatter(path: Path) -> tuple[dict[str, str], str]:
    """Validate the flat YAML subset authored by this project, not arbitrary YAML."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"Missing frontmatter: {path}")
    header, body = text[4:].split("\n---\n", 1)
    values = {}
    for line in header.splitlines():
        key, sep, value = line.partition(":")
        if not sep or key in values or key not in {"name", "description", "license"}:
            raise ValueError(f"Unsupported or duplicate frontmatter field: {path}: {line}")
        value = value.strip()
        values[key] = json.loads(value) if value.startswith('"') else value
    return values, body.strip()


def skill_files(skill: Path) -> list[Path]:
    """Only declared runtime assets may enter distribution archives."""
    if skill.is_symlink() or not skill.is_dir():
        raise ValueError(f"Not an ordinary skill directory: {skill}")
    result = []
    resource_dirs = {"references", "templates"}
    if skill.name == SUITE_NAME:
        resource_dirs.add("modules")
    for path in sorted(skill.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink not allowed in skill: {path}")
        if path.is_dir():
            if path.relative_to(skill).as_posix() not in resource_dirs | {"agents"}:
                raise ValueError(f"Unexpected runtime directory: {path}")
            continue
        relative = path.relative_to(skill).as_posix()
        allowed = relative in {"SKILL.md", "LICENSE", "agents/openai.yaml"} or (
            path.parent.name in resource_dirs and path.suffix == ".md"
            and len(path.relative_to(skill).parts) == 2
        )
        if not allowed:
            raise ValueError(f"Unexpected runtime file: {path}")
        result.append(path)
    return result


def check_local_links(path: Path, boundary: Path | None = None) -> None:
    for _, target in LINK.findall(path.read_text(encoding="utf-8")):
        if target.startswith(("https://", "http://", "#", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        resolved = (path.parent / target).resolve()
        if boundary is not None and not resolved.is_relative_to(boundary.resolve()):
            raise ValueError(f"Link escapes standalone package: {path}: {target}")
        if not resolved.is_file():
            raise ValueError(f"Missing linked file: {path}: {target}")
