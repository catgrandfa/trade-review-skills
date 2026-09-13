# 平台兼容与证据

文档核验日期：2026-09-14。平台入口可能随版本、账号和管理员设置变化。

## 支持范围

| 平台 | 本项目提供 | 官方依据 | 本次验证边界 |
| --- | --- | --- | --- |
| ChatGPT | 原生上传材料；Project 指令 + 知识文件；完整单文件文本 | [Skills 帮助](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)、[Projects 帮助](https://help.openai.com/en/articles/10169521-using-projects-in-chatgpt) | 已核对入口及生成文件；未在用户 ChatGPT 账号导入或试跑 |
| Claude / Cowork | 五个单技能 ZIP，每包一个顶层目录 | [自定义技能](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)、[使用技能](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | 已验证 ZIP 与引用自包含；未在 Claude 账号导入或试跑 |
| WorkBuddy | 单技能 ZIP、本地项目 `.codebuddy/skills/` 安装、显式读取和文本适配 | [官方技能说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)、[项目配置](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project) | 已核对上传入口与项目目录；未在 WorkBuddy 客户端导入或试跑 |
| Codex | `~/.agents/skills` 目录安装、OpenAI UI 元数据 | [Build skills](https://learn.chatgpt.com/docs/build-skills) | 安装器临时目录检查；当前版本未在客户端执行 |
| Claude Code | `~/.claude/skills` 目录安装 | [Skills 文档](https://code.claude.com/docs/en/skills) | 临时目录结构检查；未在 Claude Code 执行 |
| Cursor | `~/.cursor/skills` 目录安装 | [Skills 文档](https://cursor.com/docs/skills) | 临时目录结构检查；未在 Cursor 执行 |
| 其他 Agent | 标准技能文件夹或自包含纯文本 | [Agent Skills 规范](https://agentskills.io/specification) | 需要目标工具能够读取文本；不承诺自动发现 |

“兼容”指提供符合已核对入口要求的材料与替代使用方式。结构校验、模型行为试用、真实平台安装是不同层次；没有做过的层次不标为通过。

可复制给 AI 的仓库安装指令见[安装指南](installation.md#复制给-ai-的指令)，执行入口为 [INSTALL.md](../INSTALL.md)。安装到当前远程环境、文件落盘、工具已经发现、账号已导入是不同状态，须按实际结果报告。WorkBuddy 的本地项目安装不自动代表账号技能市场已安装。

## ChatGPT 入口差异

截至核验日，OpenAI 帮助页列出的原生 Skills 面向符合条件的 Business、Enterprise、Healthcare、Edu 账号，并受工作区设置和产品可用性影响。不要假定所有个人 ChatGPT 账号都有同一入口；没有入口时仍可使用文本或 Project 适配。

该帮助页确认上传功能，但没有列出 ZIP 的精确格式契约。本项目的 ZIP 按 Agent Skills/Claude 单目录规范打包；ChatGPT 如不接受该文件类型，使用编辑器添加内容或文本适配，不称 ZIP 已通过 ChatGPT 官方导入验证。

## 可移植性设计

- 每个技能包自带共同约定、交接模板、专用模板、示例和许可证，不读取兄弟技能目录。
- 技能正文不依赖某个平台的工具名称、环境变量、MCP 或脚本。
- 元数据只使用通用的 `name`、`description`、`license`；`agents/openai.yaml` 是可忽略的界面元数据。
- 文本适配由相同来源生成，相关文件内容已经内联，纯聊天用户不需要打开相对路径。
- 五个技能只共享使用者主动交接的材料，不假设不同平台的记忆、文件或安装状态同步。

验证方法与目前结果见[验证说明](validation.md)。
