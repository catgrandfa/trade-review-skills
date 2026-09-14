# SkillHub ZIP 文件识别实测

核验日期：2026-09-14。测试浏览器：Microsoft Edge。测试页面：[SkillHub 发布页](https://skillhub.cn/dashboard/publish)。

这是 **0.3.0 的历史记录**。0.3.1 按上传要求移除了独立 `LICENSE` 文件，一体版变为 22 个文件，其余内容不变。新版包仅通过本地检查，尚未在此页面重测；以下文件数和 SHA-256 不适用于新版。

## 所选文件

- 版本：[v0.3.0](https://github.com/catgrandfa/trade-review-skills/releases/tag/v0.3.0)。
- 文件：[trade-review-suite.zip](https://github.com/catgrandfa/trade-review-skills/releases/download/v0.3.0/trade-review-suite.zip)，根部直接包含 `SKILL.md`，共 23 个文件。
- 压缩包大小：27,357 字节。
- SHA-256：`64524b6340e17870cc06883e910335c585b46ecad40e52cd6bf0772fd0763579`。
- 包内容未因本次验证修改；选择的是与上述 Release 资产字节一致的本地文件。

## 操作与观察

1. 在已登录的 SkillHub 页面进入“发布 Skill”的普通发布类型，选择“本地上传”。页面注明支持文件夹或 ZIP，最多 200 个文件，总大小不超过 10 MB。
2. 点击“选择 zip 文件”，通过 Edge 的系统文件选择框选定上述文件，确认打开。
3. 等待页面解析后，上传区显示“已选择 23 个文件，总大小 42.1 KB”。
4. 文件列表显示 `agents/` 下 1 个文件、`modules/` 下 5 个文件、`references/` 下 10 个文件、`templates/` 下 5 个文件，以及根部 `LICENSE` 和 `SKILL.md（必需）`。
5. 描述区域出现“检测到 SKILL.md 中的描述：”，内容与一体版入口的中英文 description 一致，并提供“使用此描述”按钮。

观察来自真实页面的可访问性文本。未保存包含账号信息的页面截图，也未将账号信息写入公开记录。

## 结论与边界

本次根部入口 ZIP 已通过 SkillHub 上传页的文件识别，五个模块的资源同时被识别。未点击“提交审核”，没有审核通过、公开上架、下载后安装或模型运行的验证结果。本次也没有在此入口验证文件夹版 ZIP、拖放上传或其他浏览器。

用户此前报告 ZIP 上传提示必须包含 `SKILL.md`，单个入口可以被识别。本次没有取得此前失败文件的确切名称、摘要和操作路径，无法证明它与上述测试文件一致，也不能据此断定失败根因。后续排查应先比对文件名、SHA-256 和上传路径，而不是继续盲目改变压缩格式。

仅上传一体版的 `SKILL.md` 会遗漏其引用的模块和资源。上传时保留对应版本的全部技能资源；0.3.1 的上传包共 22 个文件，无独立 `LICENSE`。不要把仓库集合 ZIP 当作单技能上传包。
