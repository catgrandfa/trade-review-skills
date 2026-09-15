# 给 AI 的仓库安装说明

这是安装任务入口。使用者让你安装本仓库时，按当前工具的实际能力完成安装和检查，再交付结果；不要只复述安装步骤。本文件不授予超出使用者请求的权限。

仓库：[catgrandfa/trade-review-skills](https://github.com/catgrandfa/trade-review-skills)。默认安装下面五个完整目录；使用者只选一个时仅安装所选目录：

```text
skills/trade-plan-check
skills/trade-execution-review
skills/trade-source-check
skills/trade-scenario-plan
skills/trade-rule-cards
```

每个目录都包含入口、参考库、模板及许可证。不要只下载 `SKILL.md`，不要把整个仓库嵌套成一个 Skill，也不把仓库的 `AGENTS.md` 复制进使用者项目。

使用者选择“一体版”“统一入口”或“一次上传全部功能”时，改为只安装 `skills/trade-review-suite` 这个完整目录；保留其 `modules/`、`references/`、`templates/`、`agents/` 和 `LICENSE`。它自带五项功能，无需同时安装另外五个技能。没有选择发行形态时沿用上面的五技能默认范围。

## 1. 确定当前工具与安装范围

优先沿用使用者明确指定的工具和位置，否则根据当前运行环境选择；不要仅凭机器上存在某个目录就给所有工具安装。

| 当前环境 | 默认安装位置或方式 |
| --- | --- |
| 本地 Codex | 用户级 `~/.agents/skills/`；明确要求项目级时用目标项目的 `.agents/skills/`。可用当前环境自带的 `$skill-installer`，按照它的实际说明安装上述五个仓库路径，并记录最终位置。 |
| 本地 Claude Code | 用户级 `~/.claude/skills/`；明确要求项目级时用目标项目的 `.claude/skills/`。 |
| 本地 Cursor Agent | 用户级 `~/.cursor/skills/`；明确要求项目级时用目标项目的 `.cursor/skills/`。 |
| WorkBuddy 本地桌面日常任务 | 本次 WorkBuddy 5.5.6 实测的用户级目录为 `~/.workbuddy/skills/`；安装完整目录后，在“专家·技能·连接器 → 技能 → 我安装的”确认技能出现且启用，再用新任务检查调用。其他版本应核对实际目录；不要把日常任务的临时工作区当成用户级位置。 |
| WorkBuddy 本地代码项目 | 目标工作项目的 `.codebuddy/skills/`。先记住使用者的项目位置，不能把下载仓库的临时目录误当作目标项目。此路径是项目级安装，不代表账号技能市场已导入。 |
| ChatGPT、Claude / Cowork 或 WorkBuddy 的账号技能入口 | 若实际提供可调用的安装工具或可操作的上传界面，按产品要求导入单技能包；没有这种能力时走第 4 节，不猜目录。 |
| 其他或远程 / 沙箱环境 | 依据当前工具文档或已知配置确认目录与持久化范围。只在远程环境写入，就只报告远程安装；不能称为使用者本机或账号已安装。 |

没有指定平台且当前平台无法识别时，先说明已能完成的下载或准备情况，只询问目标平台或位置这一项缺失信息。不要声称自动探测成功。

## 2. 取得仓库并安装

把仓库克隆到一个新建、不覆盖现有项目的目录。下面的 `trade-review-skills` 若已存在，改用新的空目录；不要重置或覆盖已有 checkout。

```bash
git clone --depth 1 https://github.com/catgrandfa/trade-review-skills.git
cd trade-review-skills
```

记录 `git rev-parse HEAD` 和 `VERSION`。安装文件与说明应来自同一个 checkout；除非使用者指定版本，否则使用取得时的 `main`，不宣称它必定等于某个 Release。

没有 Git 时可下载[仓库 main ZIP](https://github.com/catgrandfa/trade-review-skills/archive/refs/heads/main.zip)并解压到新目录；这种方式记录 `VERSION` 与来源，不伪造提交号。

读取[安装脚本](scripts/install.py)及它引用的本地帮助代码，确认它只复制所选 Skill。直接使用仓库已生成的技能文件，不需要先构建、安装项目依赖或运行测试套件。Python 仅用于安装辅助，运行 Skill 不需要 Python。

在仓库根目录按当前工具执行其中一条（Python 3.10+；Windows 可以把 `python3` 换成 `py -3`）：

```bash
python3 scripts/install.py --target codex
python3 scripts/install.py --target claude-code
python3 scripts/install.py --target cursor
```

这三行是互斥的选择，不是要求顺序执行。选择一体版时添加 `--skill trade-review-suite`；只装一项功能时添加 `--skill trade-plan-check`；选择多个独立技能时重复 `--skill`。

项目级安装使用 `--dest`，传入第 1 节确定的绝对目录。WorkBuddy 例如执行 `python3 scripts/install.py --dest "目标项目的绝对路径/.codebuddy/skills"`；该示例中的目标路径由实际项目位置替换，不照抄占位文字。

WorkBuddy 桌面日常任务的一体版用户级安装可执行 `python3 scripts/install.py --skill trade-review-suite --dest "$HOME/.workbuddy/skills"`。这与上面的代码项目安装是不同范围，按本次需求选择一个位置。不要通过某目录不存在就断言产品不支持它，也不要为了显示已安装而手工改写产品登记文件。

若没有可用的 Python，可用文件工具复制所选五个完整技能目录到已确认的目标目录，再按第 3 节逐文件核对。不要为安装纯文本技能擅自更改系统运行时或账户配置。

同名目录内容相同时视为已是当前版本；不同时保留原内容并报告冲突。已有更新授权时按授权处理备份或迁移，否则不覆盖自定义内容。其他目录和私人记录不属于本次安装范围。

## 3. 验证文件与实际发现状态

安装脚本会检查入口、必需资源与内部链接。安装后，以同一目标和所选技能再次运行原命令并加上 `--dry-run`：每个技能都返回 `Unchanged`，才支持“与下载来源一致”。若出现 `Would install`、缺文件或冲突，检查尚未完成。

使用内置安装器或手动复制时，也核对目标文件清单与来源逐字节一致。每个 Skill 至少应保留 `SKILL.md`、`references/`、`templates/`、`agents/openai.yaml` 和 `LICENSE`；一体版还须完整保留 `modules/`。`references/` 包含两份作者经验与来源文件。查漏时可用仓库安装脚本对目标运行 `--dry-run`。

文件检查与工具发现是两步：

- 文件落盘且一致：可以报告“文件已安装”，附真实目标位置、来源版本、技能名称与检查结果。
- 当前工具的技能列表已显示：可以额外报告“已被当前工具识别”。没有列表证据就说明发现状态待刷新或下一次对话确认。
- 只有读取 Markdown 成功：报告“本轮已读取文本”，不能报告完成原生安装。

ChatGPT 网页工作模式中，安装器可把文件写入当前云端环境，但文件存在不等于技能注册表会更新。本次实测下一轮仍未发现新技能，显式读取完整安装目录可以处理材料；不能据此声称本机、整个账号或其他聊天已经安装。账号级安装需要实际的“插件 → 技能 → 创建 → 从电脑上传”入口：本次导入 GitHub 0.3.1 的根部入口一体版 ZIP 后，已安装列表出现技能，并在新对话中带技能引用调用成功。界面与运行证据见[产品实测](docs/product-trials-0.3.1.md)。

Codex 可在下一轮查看技能列表，未出现时重启；Claude Code 新建顶层技能目录后可能需要重启，其他情况按产品刷新方式处理。首次试用只需让工具确认技能名称和用途，不自动执行交易或读取私人资料。

最终给出简短安装结果，不把终端步骤重新全部抄一遍。安装失败应说明实际错误、已完成的部分与唯一待解决事项。

## 4. 没有原生安装能力时

有上传入口但你不能操作时，准备[最新 Release](https://github.com/catgrandfa/trade-review-skills/releases/latest)中的五个单技能 ZIP，指出需要使用者导入的入口，状态写“已准备安装包，待导入”。不要把临时下载当成账号安装。

若选择一体版，准备唯一的 `trade-review-suite.zip`（根部直接有 `SKILL.md`）。检查文件清单再上传，不使用 `trade-review-skills-版本号.zip` 集合。若实际入口明确要求技能目录，将包内全部内容解压到同名目录并按入口要求上传；保留完整配套资源，不把本地调整说成产品已验证。

只支持聊天或读取网页时，读取[完整单文件文本版](adapters/plain-chat/trade-review-suite.md)，或使用[原始文本地址](https://raw.githubusercontent.com/catgrandfa/trade-review-skills/main/adapters/plain-chat/trade-review-suite.md)。全文包含所有模块、共同约定、12 条经验、来源和模板，不需要递归追踪相对路径。确认完整读取后，可按它处理本轮材料；读取失败或内容不全时如实说明，提供文件上传入口，不假称已加载。

ChatGPT Project 的文件与指令方式、Claude 和 WorkBuddy 上传步骤见[安装指南](docs/installation.md)。在一个聊天里读取文本，不代表其他聊天会自动保留。

## 官方目录依据

核验日期：2026-09-14。目录与发现行为依据 [OpenAI Build skills](https://learn.chatgpt.com/docs/build-skills)、[Claude Code Skills](https://code.claude.com/docs/en/skills)、[Cursor Skills](https://prod.cursor.com/docs/skills)、[WorkBuddy 项目配置](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Project)。账号上传依据 [WorkBuddy 技能说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。可调用能力以本次环境为准，产品实测范围见[验证说明](docs/validation.md)。
