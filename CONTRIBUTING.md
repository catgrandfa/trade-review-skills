# 贡献指南

作者经验参考库会持续更新和优化，欢迎通过 [Issues](https://github.com/catgrandfa/trade-review-skills/issues) 提出意见。反馈时可以说明使用场景、遇到的问题，以及希望补充或改进的内容。

提交改动时请说明具体用户场景、原行为、预期行为及验证证据。示例只用虚构数据，不提交真实交易日志、持仓、截图或第三方原始材料全文。

## 维护位置

- 五个独立技能的 `SKILL.md`、专用模板及 `references/examples.md`：维护各模块的实际行为。
- `skills/trade-review-suite/SKILL.md`：只维护统一入口的任务选择和衔接；其 `modules/`、模板、示例及示例索引全部由构建生成，不手改。
- `shared/`：共同约定与交接卡的唯一来源。技能目录中的同名文件由构建复制。
- `adapters/chatgpt/instructions.md`：简短 Project 指令；其余聊天适配正文自动生成。
- `scripts/`：离线打包、结构校验和本地安装。保持标准库实现。
- `docs/compatibility.md`：官方来源、日期、验证层次。新平台需先核对官方文档。
- `docs/catalog-listing.md`：可供目录收录使用的事实与证据。发布后核对公开下载链接；GitHub 发现标签需在仓库元数据中配置，不能用文档文字代替。收录状态只按实际结果更新。

## 检查

```bash
python3 scripts/build.py
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
git diff --check
```

改变决策行为时，用没有看过预期答案的独立 Agent，在临时目录运行有关虚构案例，再人工核对输出与原始证据。把模型试用与真实平台安装分开报告；结构通过不代表推理表现通过。

## 发布

更新 `VERSION` 与 `CHANGELOG.md`，生成并校验发布资产。检查暂存文件只含本项目公开内容，提交后推送。以 `v` 加版本号创建 GitHub Release，上传 `dist/SHA256SUMS` 列出的资产及该校验文件。

五个独立技能包各包含一个顶层目录。一体版只生成 `trade-review-suite.zip`，根部直接含 `SKILL.md`；构建会清除本地遗留的 `trade-review-suite-folder.zip`，不再把它列入校验和或发布资产。集合包供解压使用，不用于某个平台的单技能上传入口。未完成平台账号试跑时，兼容矩阵保留“未实测”。
