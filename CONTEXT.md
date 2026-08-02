# CONTEXT

## 术语表

- **Help 主题页（Topic）**：Monitor ERP G5 在线帮助站中的一个 HTML 页面，知识库的最小文档单元，路径形如 `Content/Topics/UserGuide/GettingStarted/GettingStarted.htm`。
- **知识库数据源（KB source）**：从 help 站点抽取、清洗后供 RAG 系统检索使用的数据集。
- **RAG-ready 数据集**：平台无关的中间产物——干净正文（Markdown）+ 元数据（语言、主题路径、URL、时间戳）+ 分块。
- **元数据清单（metadata manifest）**：RAG-ready 数据集的每主题元数据记录（JSONL 一行一条），含稳定主题 id、标题、URL、来源站点、文档版本、语言、主题路径、质量标记、Last-Modified、ETag、内容 hash、图片清单与双语配对 id。
- **分块（Chunk）**：从清洗后的 Markdown 主题页按标题层级切出的检索单元；块内保留标题路径，并继承主题元数据上下文。
- **双语同构块（bilingual isomorphic chunk）**：同一主题对下标题位置路径相同的中文块与英文块；中文块以 paired_chunk_id 指向英文块，用于交叉验证。
- **双语数据源**：中文是问答主语言（硬性要求），英文是准确真源；两种语言的 Help 主题页都入库，中文内容带质量标记。
- **保真层（Canonical tier）**：英文主题页——准确真源，用于交叉验证与兜底。
- **参考层（Reference tier）**：现有中文主题页——问答主语言的主要检索语料，带“参考/低质量”质量标记。
- **中文精修（CN refinement）**：候选流水线阶段——用英文真源生成高质量中文以替换粗糙翻译；是否启用由试点证据决定。
- **试点（Pilot）**：用 Getting Started 部分跑通“抽取 → 清洗 → 分块 → 评审”的端到端验证，作为全站推广的样板。



- **抽取流水线（Extraction pipeline）**：把 Help 主题页从站点抓取、清洗、元数据化、分块并同步为 RAG-ready 数据集的可重复运行流程；代码与产物位于本仓库 kb-pipeline/。
- **增量同步（Incremental sync）**：基于 HTTP 条件请求或变更信号，只抓取变化的主题页，避免全量重复下载。
- **全量对账（Full reconciliation）**：定期用完整页面清单重扫站点，纠正增量同步的漏抓、失效与删除。
