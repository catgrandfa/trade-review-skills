# ClawHub 发布与目录收录调查

核验日期：2026-09-14。仓库版本：0.2.3。本文记录平台规则、只读预检及建议，不代表已经发布、投稿、被收录或完成产品安装测试。

后续实现：0.3.0 已新增 [trade-review-suite](../skills/trade-review-suite/SKILL.md) 统一入口及根部入口、文件夹入口两种 ZIP，见[安装指南](installation.md)。以下“尚未新增一体版”等表述是 0.2.3 调查时的历史状态；平台许可及未做账号实测的边界仍保留。

收录准备的当前说明已移至[收录资料](catalog-listing.md)，包括发现标签、公开入口、固定版本资产和可直接使用的推荐介绍。以下“缺少标签”“尚未修改”等表述保留为首次调查时的记录，不作为当前仓库元数据状态。

## 结论

- **ClawHub**：已复现把仓库根目录作为单个技能发布时的 `SKILL.md required` 错误；选择 `skills/trade-plan-check` 后，同一 CLI 的预检通过。另有本项目 MIT 与平台 MIT-0 的许可差异需要在实际发布前明确处理。尚未取得原始失败操作和报错，不能认定用户遇到的一定是这两项。
- **SkillsMP**：现行官方 FAQ 指向 GitHub 自动索引；本仓库缺少它建议的发现 topic。没有核实到当前必须达到 2 stars 的硬门槛。
- **SkillCast**：当前使用 `skillcast.cn` 的仓库推荐、编辑审核流程。旧版 Agent 投稿教程不能直接套用。

## ClawHub：已验证的卡点与边界

### 1. 发布目录必须是一个技能

本仓库根目录没有 `SKILL.md`，五个入口位于 `skills/<name>/SKILL.md`。每个技能包含 9 个文件，总计约 24–25 KB；五个单技能 ZIP 各有一层技能目录，集合 ZIP 则包含五个技能和仓库说明。见[构建脚本](../scripts/build.py)、[技能入口](../skills/trade-plan-check/SKILL.md)。

ClawHub CLI 检查发布目录根部的技能入口，服务端也按根部路径查找；网页支持展开 ZIP，但仅去除一层共同顶层目录。因此整仓 ZIP 去除 `trade-review-skills/` 后，入口仍在 `skills/<name>/SKILL.md`，不满足单技能上传要求。[CLI 源码](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/packages/clawhub/src/cli/commands/publish.ts#L98)、[服务端检查](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/convex/lib/skillPublish.ts#L285)、[ZIP 展开](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/src/lib/uploadFiles.ts#L8)、[网页目录处理](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/src/routes/skills/publish.tsx#L192)。

使用 npm 发布的官方 `clawhub@0.23.3`，本次实际执行了以下**不上传**的预检：

```bash
npm exec --yes --package=clawhub@0.23.3 -- \
  clawhub skill publish . --version 0.2.3 --dry-run --json
# 退出码 1：Error: SKILL.md required

npm exec --yes --package=clawhub@0.23.3 -- \
  clawhub skill publish ./skills/trade-plan-check \
  --version 0.2.3 --dry-run --json
# 退出码 0：ok=true, status=would-publish, fileCount=9
```

正确上传材料是单个目录或对应的 `dist/trade-plan-check.zip`，其余四个技能分别处理。不要为通过单技能上传而在仓库根部增加一个虚假的入口。集合包仍用于解压后选择技能。[现有发布资产](https://github.com/catgrandfa/trade-review-skills/releases/tag/v0.2.3)、[平台技能格式](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/docs/skill-format.md#L10)。

**GitHub 导入有不同逻辑**：它能发现仓库内的多个技能入口，不能把“根部无 SKILL.md”当作 GitHub 导入必然失败的理由。但该入口只接受登录 GitHub 用户自己拥有的公开、非 fork、未归档、未禁用仓库。本仓库公开状态符合这些仓库条件，实际登录身份未知。[导入规则](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/docs/skill-format.md#L24)、[发现候选技能的实现](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/convex/githubImport.ts#L136)、[仓库公开元数据](https://api.github.com/repos/catgrandfa/trade-review-skills)。

### 2. MIT 与 MIT-0 要分清

本项目 [LICENSE](../LICENSE) 和五个技能 frontmatter 均为 MIT。ClawHub 要求发布内容采用 MIT-0，不提供逐技能许可覆盖；网页要求声明拥有按 MIT-0 发布的权利。[平台许可规则](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/docs/skill-format.md#L198)、[网页勾选项](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/src/routes/skills/publish.tsx#L1253)。

需要区分两种情况：

- 没有接受网页条款会阻止提交；GitHub 导入后端也明确拒绝未接受条款的请求。[导入检查](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/convex/githubImport.ts#L270)。
- `license: MIT` 与平台规则不一致，但本次没有证据表明它触发了原始报错。预检通过也不会证明许可问题已解决，因为 CLI 在上传与服务端审核前就返回预检结果。[预检返回点](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/packages/clawhub/src/cli/commands/publish.ts#L150)。

建议：由权利人明确是否愿意提供 MIT-0 发行版，再通过构建流程统一处理许可声明；本次没有更改许可证或生成独立发行版。

### 3. 其他错误须按原文诊断

| 操作或报错 | 已核对的规则 / 下一步 |
| --- | --- |
| `SKILL.md required` | 改选单技能目录；不要直接发布仓库根部或集合 ZIP。 |
| `MIT-0 license terms must be accepted` | 明确发行许可，确认有权接受平台条款。 |
| GitHub 导入提示仓库归属、访问问题 | 检查登录账号是否就是仓库所有者，而非另一个账号或组织身份。 |
| GitHub 账号年龄限制 | 当前源码要求 GitHub 账号至少 14 天；不是仓库至少 14 天。仓库所有者公开账号创建于 2019 年，若登录的是该账号则年龄达标。 |
| 发布后搜索不到 | 查看精确技能页和发布状态，区分待扫描、审核限制与发布失败。 |
| `429` / GitHub API rate limit | 按重试提示等待；不能归咎于技能正文格式。 |

账号门槛依据：[githubAccount.ts](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/convex/lib/githubAccount.ts#L9)、[公开账号元数据](https://api.github.com/users/catgrandfa)。扫描、搜索与限流处理依据：[官方排错说明](https://github.com/openclaw/clawhub/blob/main/docs/troubleshooting.md)。单技能体积远低于当前单文件 10 MB、总量 50 MB 限制。[大小限制实现](https://github.com/openclaw/clawhub/blob/8c2de6c506bb4efabe3f0c2ffb8370b9e23d4650/convex/lib/publishLimits.ts#L12)。

本次未取得原始报错、网页发布记录或账号内扫描报告，不能宣布完整根因已经确定，也不能将 `would-publish` 写成服务端审核通过。

## SkillsMP：GitHub 自动收录

[官方 FAQ](https://skillsmp.com/docs/faq) 的投稿说明是：GitHub 仓库中存在 `SKILL.md`，包含 `name`、`description` frontmatter，添加 `claude-skills` 或 `claude-code-skill` topic，等待每日同步；手动提交系统仍标记为 coming soon。

本仓库已有五个结构完整的技能，当前 topics 包含 `agent-skills`、`claude` 等，但缺少上述两个发现标签。[公开仓库信息](https://api.github.com/repos/catgrandfa/trade-review-skills)、[目录树](https://api.github.com/repos/catgrandfa/trade-review-skills/git/trees/main?recursive=1)。

建议执行的元数据修改，**本次尚未执行**：

```bash
gh repo edit catgrandfa/trade-review-skills \
  --add-topic claude-skills \
  --add-topic claude-code-skill
```

不必拆成五个仓库，或为此增加根部入口。SkillsMP 已存在仓库内部技能目录的收录实例，例如 [marketingskills / copywriting](https://skillsmp.com/creators/coreyhaines31/marketingskills/skills-copywriting)。这是现有条目的证据，不是对本仓库必收录的承诺。

当前 FAQ 未公布“至少 2 stars”的门槛，本次[公开搜索结果](https://skillsmp.com/api/v1/skills/search?q=trade-review&limit=50)中也有 0、1 star 条目。因此不能把获取 2 stars 作为必要前置工作；完整后台筛选条件仍未知。

本次以仓库名、作者名和五个技能名查询，未找到本仓库条目。例如 [trade-plan-check 查询](https://skillsmp.com/api/v1/skills/search?q=trade-plan-check&limit=5)。搜索没有结果不证明后台从未抓取。补充 topic 后，等待后续同步，再检索完整技能名；“每日运行”不等于保证 24 小时内收录。持续无结果时可使用[官方联系入口](https://skillsmp.com/about)询问；本次未发送消息。

## SkillCast：推荐仓库，等待编辑审核

本次核对的平台是 [SkillCast.cn](https://skillcast.cn/)，其[市场页](https://skillcast.cn/skills)底部有“推荐一个 Skill”。登录后填写 GitHub 仓库 URL，点击“推荐收录”进入编辑审核，不会直接公开发布。

[关于页](https://skillcast.cn/about)说明会检查仓库、文档、授权、维护状态和风险，并整理适用场景、依赖与安装案例；低 star 项目也可收录。未查到公开审核时限或交易类技能的特殊准入规则。

建议提交仓库根地址：

```text
https://github.com/catgrandfa/trade-review-skills
```

供投稿说明或后续编辑沟通使用的描述：

> 基于使用者提供的材料，复核交易规则、计划、执行与引用证据。包含五个可独立安装的中文 Markdown 技能，附虚构示例和安装说明。无需行情 API、券商账户或自动交易；作者经验仅作可选参考，不代表使用者已经采用。

现有[视频制作技能库条目](https://skillcast.cn/skill/skill-6a9b91dc54fd8)表明一个多技能集合仓库可以被收录。但本项目最终显示为一条集合还是五条独立条目，未找到公开承诺，取决于编辑处理。

旧教程中的 `https://skillcast.cn/skill.md` 在本次访问时显示“页面未找到”。不要据此继续使用旧 Agent 注册、API Key 或等级解锁流程。应以当前市场页展示的推荐流程为准。

## 建议执行顺序与验证

1. 给 GitHub 仓库补充 SkillsMP 建议的 topic，再通过后续目录搜索验证收录。
2. 登录 SkillCast，推荐仓库 URL，等待编辑审核并核对最终条目。
3. 明确 ClawHub 的发行许可，逐个使用单技能目录或 ZIP 发布；保留原始报错及最终状态。

以上是建议顺序，未执行外部修改、发布或投稿。源码检查、CLI 预检、平台审核、目录收录、真实产品安装是不同状态，应分别记录。

## 补充：腾讯 SkillHub 的 ZIP 报错

用户随后明确平台为 `https://skillhub.cn/dashboard`，并报告上传 ZIP 后提示必须包含 `SKILL.md`。这是用户报告的错误含义，尚未取得确切上传文件名或完整原始错误。本次浏览器访问看到登录入口，未在该账号上传复现。

腾讯 SkillHub 与 ClawHub 是不同平台；不能直接套用 ClawHub 的许可条款或 ZIP 顶层目录处理规则。[腾讯官方仓库](https://github.com/Tencent/skillhub)确认产品站点为 `skillhub.cn`。

根据现有集合 ZIP 的结构，最直接的解释是：上传器未在它要求的位置找到单个技能入口；集合内虽然存在五份 `SKILL.md`，却都嵌套在 `trade-review-skills/skills/<name>/` 下。若上传的是现有单技能 ZIP，则仍需核对 SkillHub 是否接受 `skill-name/SKILL.md` 的外层目录，不能仅凭此报错认定不支持多个技能。

一个 skill 可以包含多个任务模块。若要实现一次上传后使用全部五项能力，可另行设计统一入口发行版：一个 `SKILL.md` 根据任务加载对应模块，并在包内携带全部参考材料。它在平台上是一个技能，内部包含五个模块。现有集合包没有这种统一入口；本次仅提出方案，尚未新增该技能或验证其行为。原有五个独立技能可以继续保留。
