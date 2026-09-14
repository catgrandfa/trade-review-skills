# 平台兼容与证据

文档核验日期：2026-09-14。平台入口可能随版本、账号和管理员设置变化。

0.3.0 新增统一入口版：`trade-review-suite.zip` 的根部直接包含 `SKILL.md`，`trade-review-suite-folder.zip` 则包含一层技能目录；两者内容相同。原有五个独立技能继续提供。下表的入口文档不等于新一体版已经在相应产品中通过安装测试。

0.3.2 已补做 WorkBuddy 用户级更新及 ChatGPT 账号替换、工作环境更新和运行时回读，见[本版产品复测](../evals/results/0.3.2-products.md)。安装与发现成功不代表六案回答全部达标；报告保留未解决的模型输出偏差。

0.3.1 按上传要求，从七个技能上传 ZIP 中移除独立 `LICENSE` 文件；技能内容和 MIT 元数据不变。新版通过本地包检查，尚未在 SkillHub 重测。以下 0.3.0 的页面识别结果不外推到新版审核与运行。

## 支持范围

| 平台 | 本项目提供 | 官方依据 | 本次验证边界 |
| --- | --- | --- | --- |
| ChatGPT | 根部入口一体版 ZIP；Project 指令 + 知识文件；完整单文件文本 | [Build skills](https://learn.chatgpt.com/docs/build-skills)、[Projects 帮助](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) | 0.3.1 ZIP 在账号技能页导入成功并从新对话调用；云端目录安装单独记录，见[实测](product-trials-0.3.1.md) |
| Claude / Cowork | 五个单技能 ZIP，每包一个顶层目录 | [自定义技能](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)、[使用技能](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | 已验证 ZIP 与引用自包含；未在 Claude 账号导入或试跑 |
| WorkBuddy | 用户级目录安装、单技能 ZIP、本地代码项目安装和文本适配 | [官方技能说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)、[项目配置](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project) | 5.5.6 在 `~/.workbuddy/skills/` 安装 0.3.1，界面识别并在三个新任务调用；发现一项来源编号缺陷，见[实测](product-trials-0.3.1.md) |
| Codex | `~/.agents/skills` 目录安装、OpenAI UI 元数据 | [Build skills](https://learn.chatgpt.com/docs/build-skills) | 安装器临时目录检查；当前版本未在客户端执行 |
| Claude Code | `~/.claude/skills` 目录安装 | [Skills 文档](https://code.claude.com/docs/en/skills) | 临时目录结构检查；未在 Claude Code 执行 |
| Cursor | `~/.cursor/skills` 目录安装 | [Skills 文档](https://cursor.com/docs/skills) | 临时目录结构检查；未在 Cursor 执行 |
| 其他 Agent | 标准技能文件夹或自包含纯文本 | [Agent Skills 规范](https://agentskills.io/specification) | 需要目标工具能够读取文本；不承诺自动发现 |

腾讯 SkillHub 的[官方仓库](https://github.com/Tencent/skillhub)确认站点为 `skillhub.cn`。2026-09-14 在 Edge 的真实发布页选择 v0.3.0 根部入口一体包后，页面识别了全部 23 个文件、`SKILL.md` 与描述，见[上传实测记录](skillhub-upload-check.md)。未提交审核或验证安装运行，文件夹版 ZIP 也未在此入口实测。此前用户报告的失败上传没有留存具体包和操作路径，不能将其根因直接断定为目录层级或不支持一体版。未将其他腾讯云产品的 ZIP 规范当作 SkillHub 的官方契约；历史调查见[分发调查](distribution-research.md)。

“兼容”指提供符合已核对入口要求的材料与替代使用方式。结构校验、模型行为试用、真实平台安装是不同层次；没有做过的层次不标为通过。

可复制给 AI 的仓库安装指令见[安装指南](installation.md#复制给-ai-的指令)，执行入口为 [INSTALL.md](../INSTALL.md)。安装到当前远程环境、文件落盘、工具已经发现、账号已导入是不同状态，须按实际结果报告。WorkBuddy 的本地项目安装不自动代表账号技能市场已安装。

## ChatGPT 入口差异

截至核验日，本次实际账号已提供原生 Skills 上传入口，并成功导入 0.3.1 一体版。入口受账号、工作区设置和产品可用性影响；不再仅根据旧帮助页的套餐列表推断个人账号一定不可用。没有入口时仍可使用文本或 Project 适配。

本次 ChatGPT 上传页明确接受 ZIP，实际接受了根部直接包含 `SKILL.md` 的一体版。文件夹版及其他格式没有在此入口实测；不要把一个入口的成功扩展成所有客户端的格式契约。

## 可移植性设计

- 每个技能包自带共同约定、交接模板、专用模板和示例，不读取兄弟技能目录。上传 ZIP 不附独立许可证文件；源码目录保留许可证。
- 技能正文不依赖某个平台的工具名称、环境变量、MCP 或脚本。
- 元数据只使用通用的 `name`、`description`、`license`；`agents/openai.yaml` 是可忽略的界面元数据。
- 文本适配由相同来源生成，相关文件内容已经内联，纯聊天用户不需要打开相对路径。
- 五个技能只共享使用者主动交接的材料，不假设不同平台的记忆、文件或安装状态同步。

验证方法与目前结果见[验证说明](validation.md)。
