# 验证范围

本文件区分包结构检查、模型行为试用与真实产品安装。结构检查通过不证明交易效果或所有平台端到端兼容。

## 自动检查

当前版本执行以下检查：

- 五个 Skill 的名称、frontmatter、入口、模板与资源自包含。
- 共同约定、参考库及文本适配与源文件一致。
- 单技能 ZIP 的目录、文件清单、可解压性与字节一致性。
- 发布资产校验和与重复构建的确定性。
- 安装器在临时目录中的安装、重复安装、冲突预检及不覆盖行为。

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

当前 13 项自动测试通过。Python 检查器验证本项目使用的扁平 YAML 子集，不是通用 YAML 解析器。临时目录安装不代表真实客户端已发现技能或用户账号已完成导入。

## 行为试用

提供两组虚构输入：[基础场景](../evals/cases.json)与[作者经验场景](../evals/author-experience-cases.json)。评估方法见[试用说明](../evals/README.md)。

当前版本未附可用于确认其表现的独立模型试用结果，不将示例、结构检查或维护者判断当作行为验证通过。行为试用需要检查真实输出及证据边界，不能证明长期交易收益、稳定识别心理状态或所有模型表现一致。

## 产品验证

平台入口的文档依据见[兼容矩阵](compatibility.md)。当前版本没有真实 ChatGPT、Claude、WorkBuddy、Codex、Claude Code 或 Cursor 账号导入与产品内运行的验证结论。普通文本适配不应被报告为原生安装成功。
