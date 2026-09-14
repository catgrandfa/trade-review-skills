# Trade Review Skills · 交易决策复核

**把自己认可的交易规则，落实到每一次决策，并留下可以复盘的证据。**

提供五个可独立安装的 AI Skill，以及一次安装即可使用五项功能的统一入口版，帮助个人交易者理清想法、核对计划、检查观点、记录执行。使用者提供自己的规则和材料即可开始；无需行情接口、券商账户或 API Key。

[让 AI 安装](#直接让-ai-从仓库安装) · [下载安装包](https://github.com/catgrandfa/trade-review-skills/releases/latest) · [安装指南](docs/installation.md) · [完整演示](examples/walkthrough.md) · [验证与限制](docs/validation.md) · [English](README.en.md)

## 一次安装全部功能

选择 [trade-review-suite 一体版](skills/trade-review-suite/SKILL.md)，按任务调用计划核对、执行复盘、观点检查、预案整理与规则卡；使用者在平台中只安装一个技能。模块和参考材料都包含在包内。

| 文件 | 用途 |
| --- | --- |
| [trade-review-suite.zip](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.0/trade-review-suite.zip) | 一体版，ZIP 根部直接是 `SKILL.md`；用于要求根部入口的上传器，也用于排查 SkillHub 的缺少入口提示 |
| [trade-review-suite-folder.zip](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.0/trade-review-suite-folder.zip) | 相同内容，外包一层 `trade-review-suite/` 目录；用于要求单技能文件夹的上传入口 |
| `trade-plan-check.zip` 等五个包 | 按需分别安装独立技能 |
| `trade-review-skills-版本号.zip` | 仓库分发集合，解压后选择技能；不能直接当作一个技能上传 |

本地安装一体版可执行 `python3 scripts/install.py --target codex --skill trade-review-suite`；其他工具见[安装指南](docs/installation.md)。五个独立版仍可使用，一体版无需同时安装它们。两种 ZIP 均已做本地结构校验，SkillHub 账号上传及审核仍待实际验证。

## 直接让 AI 从仓库安装

把下面整段复制给你正在使用的 AI：

```text
请帮我从 https://github.com/catgrandfa/trade-review-skills 安装全部 5 个 Skill。
先读取仓库根目录 INSTALL.md，按当前工具的实际能力完成安装，不要只给我教程。
只安装到当前工具适用的位置，保留已有同名自定义内容。
完成后列出技能名称、实际位置和验证结果；如果只有聊天或临时沙箱能力，请明确说明，按文档提供可用方式，不要把读取文本说成已安装。
```

要一次安装全部功能，把“全部 5 个 Skill”改成“统一入口版 trade-review-suite”；只想试一项功能可改成“trade-plan-check”。[INSTALL.md](INSTALL.md) 是 AI 的安装入口，包含仓库获取、目标目录、完整资源复制、重复安装检查和聊天环境的替代方式。Codex 内置安装器专用指令及 WorkBuddy 项目安装指令见[安装指南](docs/installation.md#复制给-ai-的指令)。

## 先试一次

对 AI 说：

> 帮我做开单前计划核对。我的计划是等回调，但现在一直涨，我怕错过，想先买一点，止损还没想好。这些是我的自述，尚未提供行情数据。

它应指出：回调条件及当前是否满足仍待核对，不能直接断定已经改变计划；失效条件、仓位和风险安排缺失；“怕错过”是本人自述。没有提供个人纪律，就不能宣判违反纪律，也不会给出“可以买”的批准。

你可以只安装第一个 Skill。普通聊天工具也能直接使用[单文件文本版](adapters/plain-chat/trade-plan-check.md)：把全文贴入对话，随后提供你的材料。

## 五个 Skill

| Skill | 适合什么时候用 | 交付内容 |
| --- | --- | --- |
| [trade-plan-check](skills/trade-plan-check/SKILL.md) · 开单前计划核对 | 想开仓、加仓或临时改计划 | 完整性、前后差异、规则对照及缺项 |
| [trade-execution-review](skills/trade-execution-review/SKILL.md) · 交易行为复盘 | 操作结束或阶段复盘 | 事前计划、实际执行、结果分开评价 |
| [trade-source-check](skills/trade-source-check/SKILL.md) · 观点完整性检查 | 想把视频、文章的一句话用于自己的交易 | 补全语境、限制、来源版本与遗漏 |
| [trade-scenario-plan](skills/trade-scenario-plan/SKILL.md) · 交易预案整理 | 已有判断，需要整理条件分支 | 条件出现、未出现、失效时的预案草案 |
| [trade-rule-cards](skills/trade-rule-cards/SKILL.md) · 心法转规则卡 | 想把经验变成临场可核对的提醒 | 场景、边界、来源及采用状态明确的规则卡 |

这五项功能可分别安装，也可通过一体版的统一入口选用；都不自动运行 Agent。需要衔接时保留[上下文交接卡](shared/context-template.md)中的证据、时间和采用状态：经验与观点 → 规则 → 计划 → 操作记录 → 复盘。

## 作者经验参考库

五个 Skill 均附带[12 条作者经验](shared/author-experience.md)及[来源说明](shared/author-sources.md)：条件预案、仓位与逻辑止损、风险收益、计划更新、交易身份、加仓训练、回补落空、执行评价、方法取舍、连亏暂停、回撤训练、定期自查。

作者经验参考库会持续更新和优化。欢迎通过 [Issues](https://github.com/catgrandfa/trade-review-skills/issues) 提出意见、分享使用反馈或建议补充的场景。

每条都有适用场景、AI 核对问题和边界。它们可以帮助提出具体问题；使用者明确采用后，才作为个人纪律对照。3:1、连亏 2–3 次、练习 200 次、约两个月自查及底仓比例分别保存为可选参考，不自动生效。

可以这样开始：

> 用 TE07 帮我检查预案里有没有“卖出后接不回来”的遗漏，先作经验参考。

> 我从今天采用 TE01 的条件预案原则，不选择其他数字参数。帮我整理规则卡。

这些参考已包含在单技能 ZIP、ChatGPT 知识文件和普通聊天文本版中，无需额外下载或访问来源网站。

## 在哪些工具里使用

| 工具 | 使用方式 |
| --- | --- |
| ChatGPT | 有 Skills 上传入口时导入单技能包；其他账号用文本版，或 Project 指令 + 知识文件 |
| Claude / Cowork | 在自定义 Skills 入口逐个上传单技能 ZIP |
| WorkBuddy | 技能 → 添加技能 → 上传技能，导入单技能包 |
| Codex / Claude Code / Cursor | 安装到工具识别的技能目录，可用本仓库的本地安装脚本 |
| 其他聊天 Agent | 复制单文件文本版，或明确让 Agent 阅读本地 SKILL.md 及配套资源 |

各平台入口、账号限制和验证范围见[兼容说明](docs/compatibility.md)。采用通用 Agent Skills 格式不代表已在所有产品上完成真实账号安装测试。

## 使用边界

复核以使用者自己的规则、事前计划和实际记录为依据。AI 推断与本人事实分开；信息不足时指出缺项，不补造价位或成交。计划完整性不能证明行情判断正确，也不构成下单许可。

所有案例示例均为虚构示例；内置参考来源统一注明“根据作者经验”，没有默认生效的交易策略、仓位比例或纪律阈值。Skill 运行时不含脚本或联网依赖；所选 AI 平台仍会处理你提供的内容，分享前请自行去除不必要的私人信息。

## 开发与发布

运行时只需能读文本的 AI。以下命令仅供维护者打包，要求 Python 3.10+，无第三方依赖：

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

`shared/` 是共同约定的唯一维护源。一体版只单独维护任务选择入口，具体模块、模板和示例从五个独立技能生成；构建同时生成 `adapters/` 文本适配及 `dist/` 发布包。详见[贡献指南](CONTRIBUTING.md)。

推荐到技能目录时，可使用[收录资料](docs/catalog-listing.md)：包含中英文简介、适用场景、依赖、授权、固定版本下载链接及验证证据。SkillsMP 自动索引与 SkillCast 编辑审核的结果分别核对，未将准备完成写成已经收录。

## 开源与来源

根据作者经验，将“规则—计划—执行—复盘”整理为通用流程。公开内容包括经验说明、AI 核对问题与虚构示例，不关联个人身份或本地项目。

代码、技能说明及示例以 [MIT License](LICENSE) 发布。项目不隶属于 OpenAI、Anthropic、腾讯或其他平台。
