# 目录收录资料

核验日期：2026-09-14。对应版本：0.3.0。本页提供可供目录抓取、编辑核验与推荐投稿使用的材料，不表示已被收录或通过平台审核。

## 项目简介

**名称：** Trade Review Skills · 交易决策复核

**中文介绍：** 根据作者经验，整理交易规则、计划、引用与执行的复核流程。使用者提供自己的材料，AI 区分事实、观点、计划、已报告操作和推断，指出证据缺项与前后变化。提供五个可独立安装的中文技能，以及一个按任务调用五项功能的统一入口；无需行情 API 或券商账户。

**English:** Chinese-first skills for reviewing user-supplied trading reasoning, plans, quotations and execution against the user's own rules. Includes five independent skills and one self-contained entrypoint. No market-data engine, brokerage connection or automatic trading.

**适合人群：** 希望核对自己的决策依据、条件与执行记录的个人交易者；整理交易方法笔记、引用材料或复盘内容的作者。内容是否适合 SkillCast 的创作者定位，由其编辑判断。

**典型场景：** 开单前发现条件缺项；操作后区分执行与盈亏；核对引用遗漏；将已有判断整理为预案；将本人选择的经验写成规则卡。

**使用门槛：** 能读取技能说明和配套 Markdown 的 Agent。技能运行不要求 Python、API Key、网络、付费数据或其他插件；所使用 AI 产品自身的账号、可用功能及费用由该产品决定。Python 3.10+ 只用于可选的本地安装与维护助手。

**授权与维护：** [MIT 许可证](../LICENSE)；作者经验参考库持续更新，见[更新记录](../CHANGELOG.md)。公开示例与试用输入均为虚构材料，内置参考不自动成为使用者规则。

**边界：** 不获取行情、不验证交易信号、不补造价位、持仓或成交、不代下单，不用计划完整性证明收益或批准交易。

## 源码、入口与发行资产

- 仓库：[catgrandfa/trade-review-skills](https://github.com/catgrandfa/trade-review-skills)
- 统一入口：[skills/trade-review-suite/SKILL.md](../skills/trade-review-suite/SKILL.md)
- 独立入口：[计划核对](../skills/trade-plan-check/SKILL.md)、[执行复盘](../skills/trade-execution-review/SKILL.md)、[观点检查](../skills/trade-source-check/SKILL.md)、[预案整理](../skills/trade-scenario-plan/SKILL.md)、[规则卡](../skills/trade-rule-cards/SKILL.md)
- 固定版本：[v0.3.0 Release](https://github.com/catgrandfa/trade-review-skills/releases/tag/v0.3.0)
- 根部入口 ZIP：[trade-review-suite.zip](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.0/trade-review-suite.zip)
- 文件夹入口 ZIP：[trade-review-suite-folder.zip](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.0/trade-review-suite-folder.zip)
- 校验和：[SHA256SUMS](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.0/SHA256SUMS)
- [安装说明](installation.md)、[完整虚构演示](../examples/walkthrough.md)、[验证范围](validation.md)

统一入口 ZIP 根部直接包含一个 `SKILL.md`，五个模块和全部参考材料随包提供；文件夹版外包一层同名目录。独立技能各有自己的 `SKILL.md`、非空 `name` / `description` frontmatter 和完整资源。仓库集合 ZIP 用于解压分发，不用于单技能上传。

## SkillsMP：可发现性要求

[官方 FAQ](https://skillsmp.com/docs/faq) 的投稿说明要求 GitHub 仓库包含 `SKILL.md`、`name` 与 `description`，并添加 `claude-skills` 或 `claude-code-skill` topic；随后等待每日索引。手动提交入口仍标为即将推出。

| 项目 | 本仓库提供 |
| --- | --- |
| 公开 GitHub 来源 | 上述公开仓库；无需登录即可获取源码 |
| 技能入口和元数据 | 六个入口分别代表五个独立技能与一个一体版，均通过本地格式校验 |
| 发现 topic | 仓库配置 `claude-skills`、`claude-code-skill`，保留原有相关标签 |
| 可理解的描述与用途 | 中文优先、含英文检索描述；README 列出场景与选包方式 |
| 可核验内容 | 固定版本、许可证、示例、安装说明、自动检查及有限行为试用结果 |

Topic 是 GitHub 仓库元数据，不是写在 README 中就会生效；可通过[公开仓库 API](https://api.github.com/repos/catgrandfa/trade-review-skills)查看实际值。日同步不代表保证 24 小时内收录；官方当前未公布至少 2 stars 的硬门槛。收录结果应以目录中能找到本仓库对应条目为准，不从标签添加成功推定。

## SkillCast：编辑核验材料与推荐内容

[官方介绍](https://skillcast.cn/about)说明采用编辑精选，检查仓库、说明、授权、维护状态、适用场景、依赖与安装案例。[市场页](https://skillcast.cn/skills)底部可登录后推荐 GitHub 仓库，进入审核，不能直接公开发布。

| 编辑核验项 | 可查材料与限制 |
| --- | --- |
| 解决什么问题、适合谁 | 本页简介、场景与 README 的五项功能说明 |
| 授权、来源与维护状态 | MIT、根据作者经验的来源说明、版本记录、公开提交历史 |
| 安装与依赖 | 两种 ZIP、完整安装步骤、纯文本运行边界 |
| 输入输出与局限 | 虚构演示、三案独立试用完整回答；不冒充真实交易案例 |
| 验证证据 | 16 项分发测试、独立代理试用；真实产品账号安装和审核仍未验证 |

推荐时填写：

```text
https://github.com/catgrandfa/trade-review-skills
```

若需要补充介绍，可使用：

> 中文交易决策复核技能，帮助使用者对照自己的规则，检查计划、引用与执行记录。提供五个独立技能和一个包含全部功能的统一入口，附安装说明、虚构示例与独立试用输出。无需行情接口或券商连接，不做自动交易，也不把内置经验视为使用者已采用的纪律。

准备材料、推荐成功、进入审核与正式收录是不同状态。本次不声明已向 SkillCast 推荐，也不声明编辑已接受。

## 结果核验

SkillsMP 可搜索 `trade-review-suite`、仓库名或各独立技能名，并核对条目来源是否指向本仓库。SkillCast 则在推荐后核对审核结果及最终条目；未公开承诺固定审核时限。没有条目时只报告“本次未找到”，不能据此证明后台从未抓取。

发布与格式调查的历史证据见[分发调查](distribution-research.md)。本页未要求转为 ClawHub 的 MIT-0 许可；ClawHub 与腾讯 SkillHub 的发布规则应分别处理。
