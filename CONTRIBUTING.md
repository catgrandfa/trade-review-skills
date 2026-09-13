# 贡献指南

提交改动时请说明具体用户场景、原行为、预期行为及验证证据。示例只用虚构数据，不提交真实交易日志、持仓、截图或第三方原始材料全文。

## 维护位置

- `skills/*/SKILL.md`、专用模板及 `references/examples.md`：维护各技能的实际行为。
- `shared/`：共同约定与交接卡的唯一来源。技能目录中的同名文件由构建复制。
- `adapters/chatgpt/instructions.md`：简短 Project 指令；其余聊天适配正文自动生成。
- `scripts/`：离线打包、结构校验和本地安装。保持标准库实现。
- `docs/compatibility.md`：官方来源、日期、验证层次。新平台需先核对官方文档。

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

每个单技能包只包含一个顶层目录。集合包供解压使用，不用于某个平台的单技能上传入口。未完成平台账号试跑时，兼容矩阵保留“未实测”。
