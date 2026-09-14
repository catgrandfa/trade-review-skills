# 验证范围

本文件区分包结构检查、模型行为试用与真实产品安装。结构检查通过不证明交易效果或所有平台端到端兼容。

## 自动检查

当前版本执行以下检查：

- 五个独立 Skill 与统一入口版的名称、frontmatter、入口、模板与资源自包含。
- 共同约定、参考库及文本适配与源文件一致。
- 单技能 ZIP 的目录、文件清单、可解压性与字节一致性。
- 发布资产校验和与重复构建的确定性。
- 安装器在临时目录中的安装、重复安装、冲突预检及不覆盖行为。
- 一体版两种 ZIP 各自只有一个技能入口，解压后无需独立技能目录也能解析全部本地引用；原技能修改能同步到一体版模块、模板与示例。

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

当前 16 项自动测试通过。Python 检查器验证本项目使用的扁平 YAML 子集，不是通用 YAML 解析器。临时目录安装不代表真实客户端已发现技能或用户账号已完成导入。

## 行为试用

提供三组虚构输入：[基础场景](../evals/cases.json)、[作者经验场景](../evals/author-experience-cases.json)与[统一入口场景](../evals/suite-cases.json)。评估方法见[试用说明](../evals/README.md)。

0.3.0 对统一入口版完成三个独立虚构案例，覆盖五个模块的任务选择及两组跨模块衔接；本轮复核未发现阻断问题。完整输出、文件摘要、逐案判断与未覆盖项见[独立试用记录](../evals/results/0.3.0-suite.md)。五个独立版和聊天适配未在本轮重新做全量行为试用，不能从三案外推全部场景。

行为试用不能证明长期交易收益、稳定识别心理状态或所有模型表现一致，也不替代真实平台安装测试。

## 产品验证

平台入口的文档依据见[兼容矩阵](compatibility.md)。当前版本没有真实 SkillHub、ClawHub、ChatGPT、Claude、WorkBuddy、Codex、Claude Code 或 Cursor 账号导入与产品内运行的验证结论。普通文本适配不应被报告为原生安装成功。
