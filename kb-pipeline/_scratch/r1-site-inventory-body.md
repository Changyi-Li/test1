## Question

如何可靠地枚举 help.monitorerp.cn 的全部 Help 主题页（英文 + 中文），并验证 en-us ↔ zh-cn 的 URL 映射规则与数量？

背景事实（已初探）：
- 英文站 sitemap 约 5128 条 URL，其中约 3926 个 .htm 主题页。
- 已知 sitemap 内部分路径失效（Content/Content/...），实际页面位于 Content/Topics/...。
- 中文站没有 sitemap，但 URL 结构与英文站同构。
- .com 与 .cn 两个域名英文页时间戳不一致（.com 更新），真正中文内容只在 .cn。

需要调查：
- 除 sitemap 外，MadCap Flare 是否还产出 TOC/CSH 清单（如 Data/ 目录、manifest、搜索索引文件），哪个是可靠的真源；两份清单是否一致。
- 中文主题页清单如何从英文清单推导：抽样验证同构映射是否成立，列出反例（含 .com/.cn 差异）。
- Getting Started 部分（UserGuide/GettingStarted/）EN 与 ZH 各多少页、完整 URL 列表。
- 是否有页面未被 sitemap 收录，或 sitemap 中有失效条目。

输出：facts + 清单文件（research/help-site-inventory/findings.md，含 Getting Started 的 EN/ZH URL 清单）。
