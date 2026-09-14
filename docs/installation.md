# 安装与开始使用

从 [GitHub Releases](https://github.com/catgrandfa/trade-review-skills/releases/latest) 选择对应版本的 ZIP，或克隆仓库。想一次安装全部功能选 `trade-review-suite`；想只试一项功能选 `trade-plan-check`。

## 选择一体版或独立版

一体版在平台中是一个技能，包含五个按任务读取的模块，不需要同时安装独立版。

| 资产 | 解压结构 | 用法 |
| --- | --- | --- |
| `trade-review-suite.zip` | 根部直接为 `SKILL.md`、`modules/` 等，0.3.1 共 22 个文件 | 供要求 ZIP 根部入口的上传器使用；无独立 `LICENSE` 文件 |
| `trade-review-suite-folder.zip` | `trade-review-suite/SKILL.md` 及配套资源 | 要求单层技能目录的上传入口，例如 Claude 的文件夹式技能包 |
| `trade-plan-check.zip` 等 | 每包一个独立技能目录 | 分别安装所需功能 |
| `trade-review-skills-版本号.zip` | 仓库与多个技能目录 | 解压后分发，不作为单技能上传包 |

两份一体版 ZIP 的文件内容相同，区别仅在外层目录。对应发行版从 0.3.0 开始提供；Release 尚未发布时使用本地 `dist/` 构建产物，不把旧版集合重命名为一体版。

从 0.3.1 起，五个独立技能 ZIP 和两种一体版 ZIP 均不包含独立 `LICENSE` 文件，`license: MIT` 元数据保留。仓库、源码集合及本地目录安装仍保留许可证；源码集合不用于平台上传。

腾讯 SkillHub 地址为 [skillhub.cn/dashboard](https://skillhub.cn/dashboard)。2026-09-14 已在 Edge 的真实发布页验证 0.3.0 根部入口包的文件识别，0.3.1 尚未重测；未由此次测试提交审核或验证安装运行。ClawHub 是另一个平台，其 MIT-0 发布规则不能套用到腾讯 SkillHub，见[分发调查](distribution-research.md)。

### SkillHub 上传

1. 下载 v0.3.1 的 [trade-review-suite.zip](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.1/trade-review-suite.zip)，确认文件名；无需重新压缩。
2. 在“发布 Skill”中选择普通发布，进入“本地上传”，点击“选择 zip 文件”，选择这份 ZIP。
3. 等待页面解析并核对文件列表：0.3.1 应有 22 个文件，包含 `SKILL.md（必需）`，没有 `LICENSE`。出现从入口提取的描述建议才说明页面读到了入口。旧版 0.3.0 的实测是 23 个文件，其中包括此次移除的 `LICENSE`。
4. 之后再填写 Slug、显示名称、描述、版本号等发布信息。文件识别、提交审核、审核通过和安装运行分别确认。

旧版[实测记录](skillhub-upload-check.md)包含当时的 SHA-256；新版以对应 Release 的 `SHA256SUMS` 为准。若仍报缺少 `SKILL.md`，先核对确切版本、文件名和校验和；旧版成功不能直接解释此前未留存的失败上传。不要上传仓库集合 ZIP；也不要仅上传入口 `SKILL.md`，因为它还引用包内模块、参考和模板。

本地安装一体版：

```bash
python3 scripts/install.py --target codex --skill trade-review-suite
```

将 `codex` 换成 `claude-code` 或 `cursor`，或按实际目标使用 `--dest`。不指定 `--skill` 的原命令仍安装五个独立技能。

## 复制给 AI 的指令

**通用版：**适用于有仓库读取、终端或文件操作能力的 Agent。全文复制发送即可；具体执行说明在[仓库安装入口](../INSTALL.md)。

```text
请帮我从 https://github.com/catgrandfa/trade-review-skills 安装全部 5 个 Skill。
先读取仓库根目录 INSTALL.md，按当前工具的实际能力完成安装，不要只给我教程。
只安装到当前工具适用的位置，保留已有同名自定义内容。
完成后列出技能名称、实际位置和验证结果；如果只有聊天或临时沙箱能力，请明确说明，按文档提供可用方式，不要把读取文本说成已安装。
```

**Codex 内置安装器版：**在有 `$skill-installer` 的 Codex 环境中直接发送：

```text
请使用 $skill-installer，从 https://github.com/catgrandfa/trade-review-skills 安装以下五个完整技能目录：
skills/trade-plan-check
skills/trade-execution-review
skills/trade-source-check
skills/trade-scenario-plan
skills/trade-rule-cards
安装前读取仓库 INSTALL.md，保留 references、templates、agents 和 LICENSE；同名自定义内容不覆盖。
完成后检查目标文件，告诉我实际安装位置及下一轮如何调用；尚未被工具发现时请明确标注。
```

OpenAI 官方支持让安装器从其他仓库下载技能，见 [Build skills](https://learn.chatgpt.com/docs/build-skills)。内置安装器的版本可能使用自己的默认目录，采用它的实际说明并记录路径；本仓库独立脚本默认使用 `~/.agents/skills`，不要在两个位置重复安装同名技能。

**WorkBuddy 当前项目版：**在已经打开本地工作项目的任务里发送：

```text
请从 https://github.com/catgrandfa/trade-review-skills 安装全部 5 个 Skill 到当前工作项目。
先记住当前工作项目位置，再读取仓库 INSTALL.md；把五个完整目录安装到该项目的 .codebuddy/skills/，不要安装到下载仓库的临时目录。
保留已有同名自定义内容，完成后核对文件并报告实际位置与发现状态。
如果当前不是可写的本地项目，请准备上传包并明确下一步，不声称已完成账号安装。
```

此路径来自 [WorkBuddy 官方项目配置](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project)，属于项目级能力。账号技能入口仍可使用后面的 ZIP 导入方式。

**只有聊天能力时：**这条用于当前会话读取，不是原生安装：

```text
请读取 https://raw.githubusercontent.com/catgrandfa/trade-review-skills/main/adapters/plain-chat/trade-review-suite.md 的完整内容，按其中五个模块处理我随后提供的材料。
先说明是否完整读取成功，并列出模块名称。如果不能读取或内容不全，请告诉我需要上传该文件；不要声称已安装或会跨会话记住。
```

## ChatGPT

**有原生 Skills 入口的账号**：进入 Plugins → Skills → Create → Upload from your computer，按界面支持的文件类型上传单技能包。若界面只接受单文件，使用对应技能目录中的 `SKILL.md`，并按编辑器要求一并添加其 `references/`、`templates/` 资源；也可直接使用下面的文本适配方式。官方说明确认上传入口，但未在该帮助页规定 ZIP 的具体目录约束，因此不能承诺所有 ChatGPT 界面都接受与 Claude 相同的 ZIP。

**没有 Skills 入口，或希望直接用普通聊天**：打开 [trade-review-suite.md](../adapters/plain-chat/trade-review-suite.md)，把全文作为初始说明贴入聊天，再提供材料。也可只使用[开单前核对文本](../adapters/plain-chat/trade-plan-check.md)。无需解压或执行代码。

**使用 ChatGPT Project**：新建一个用于复核的 Project，将 [instructions.md](../adapters/chatgpt/instructions.md) 全文放入项目指令，将 [knowledge.md](../adapters/chatgpt/knowledge.md) 上传为项目文件。第一条消息要求它读取知识文件并复述任务范围，随后贴入虚构试用材料。Release 中对应文件名为 `chatgpt-instructions.md` 与 `chatgpt-knowledge.md`。项目指令 + 文件是一种文本适配方式，不等同于原生技能安装。

不要把整个开源仓库上传作为个人记录。自己的规则、计划和操作另行提供；本项目的示例不作为你的事实。

## Claude / Cowork

1. 一次安装全部功能时下载 `trade-review-suite-folder.zip`；只装一项功能时选 `trade-plan-check.zip` 等独立包。
2. 在 Customize → Skills 中选择创建/上传技能，上传 ZIP 并启用。组织账号需具备相应权限；按产品要求启用代码执行能力，尽管本套技能本身不运行代码。
3. 用下面的虚构材料试用。其余四个包按需分别上传。

这里选择的 ZIP 只有一个顶层技能目录，目录下直接是 `SKILL.md` 与配套资源。一体版导入一次即可；五个独立版才需要分别上传。不要把集合包当作单技能上传。Claude Code 的本地技能目录与 Claude/Cowork 账号技能属于不同安装入口。

## WorkBuddy

1. 下载单技能 ZIP。
2. 打开“技能” → “添加技能” → “上传技能”，选择技能包。
3. 在“已安装”中确认启用，发起任务时选择该技能或描述对应任务。

若当前客户端的上传入口不可用，将集合 ZIP 解压到你选择的工作目录，明确告诉 WorkBuddy：先读取其中 `skills/trade-plan-check/SKILL.md`，再读取它要求的参考文件，按材料完成任务。这是显式读取方式，不声称已完成自动发现安装。也可以使用单文件文本版。

## Codex / Claude Code / Cursor

克隆后，在仓库根目录执行所需的一条命令（Windows 可将 `python3` 换成 `py -3`）：

```bash
git clone https://github.com/catgrandfa/trade-review-skills.git
cd trade-review-skills
python3 scripts/install.py --target codex
```

其他工具分别使用：

```bash
python3 scripts/install.py --target claude-code
python3 scripts/install.py --target cursor
```

安装器仅复制本地文件，无下载、无凭证、无自动覆盖。先预览或只选一个：

```bash
python3 scripts/install.py --target codex --skill trade-plan-check --dry-run
```

默认个人目录分别为 `~/.agents/skills`、`~/.claude/skills`、`~/.cursor/skills`。也可以用 `--dest` 指定项目内相应目录；不需要安装脚本时，直接复制完整技能文件夹即可。

安装后新开会话，确认技能出现在列表中。Codex 可以使用 `$trade-plan-check`，Claude Code 可以使用 `/trade-plan-check`；其他工具根据其技能选择器操作。

## 通用试用

> 这是虚构练习。U1：原计划等回调，但现在一直涨，我怕错过，想先买一点，止损还没想好。我尚未提供自己的正式规则，也未提供行情数据。请做开单前计划核对。

核对它是否保留来源、检查计划一致性并指出缺项、没有编造价位或批准买入，也没有把没有提供的纪律说成你的规则。当前触发状态未知时，不能直接断定已经违反或修改原计划。更多案例见[完整演示](../examples/walkthrough.md)。

## 更新与卸载

在产品界面导入新版时，按产品提示管理旧版。本地安装器遇到不同内容会停止；先把旧技能文件夹移到技能扫描目录以外备份，再安装新版。内容相同会显示 `Unchanged`。卸载只处理本项目命名的技能目录，不删除个人记录或整个工具配置。

来源与核验日期见[兼容说明](compatibility.md)。
