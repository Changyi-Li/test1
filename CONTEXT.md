# CONTEXT

## 术语表

- **Help 主题页（Topic）**：Monitor ERP G5 在线帮助站中的一个 HTML 页面，知识库的最小文档单元，路径形如 `Content/Topics/UserGuide/GettingStarted/GettingStarted.htm`。
- **知识库数据源（KB source）**：从 help 站点抽取、清洗后供 RAG 系统检索使用的数据集。
- **RAG-ready 数据集**：平台无关的中间产物——干净正文（Markdown）+ 元数据（语言、主题路径、URL、时间戳）+ 分块。
- **元数据清单（metadata manifest）**：RAG-ready 数据集的每主题元数据记录（JSONL 一行一条），含稳定主题 id、标题、URL、来源站点、文档版本、语言、主题路径、质量标记、Last-Modified、ETag、内容 hash、图片清单与双语配对 id。
- **图片引用（Image reference）**：正文图片在 RAG-ready 数据集中以绝对 URL 记录（Markdown 引用 + 元数据图片清单），图片文件本身不入库；失效情况记入例外日志。
- **分块（Chunk）**：从清洗后的 Markdown 主题页按标题层级切出的检索单元；块内保留标题路径，并继承主题元数据上下文。
- **双语同构块（bilingual isomorphic chunk）**：同一主题对下标题位置路径相同的中文块与英文块；中文块以 paired_chunk_id 指向英文块，用于交叉验证。
- **双语数据源**：中文是问答主语言（硬性要求），英文是准确真源；两种语言的 Help 主题页都入库，中文内容带质量标记。
- **保真层（Canonical tier）**：英文主题页——准确真源，用于交叉验证与兜底。
- **参考层（Reference tier）**：现有中文主题页——问答主语言的主要检索语料，带“参考/低质量”质量标记。
- **中文精修（CN refinement）**：用英文真源生成高质量中文以替换粗糙中文翻译的候选流水线阶段；本次抽取流水线地图已决定不启用、划为 out of scope，由未来 RAG 工作另行评估。
- **试点（Pilot）**：用 Getting Started 部分跑通“抽取 → 清洗 → 分块 → 评审”的端到端验证，作为全站推广的样板。
- **预推广试跑（Pre-rollout trial）**：全站推广执行前，对一个模块（如 Stock）跑模块级全量对账作为验收门；通过判据为机器门禁 ALL PASS + 抽查模板审阅 + 结构例外审阅定案，通过后才推广全站。
- **全站推广执行（Full-site rollout）**：对全站所有 en 主题（当前 3923 个）跑全量对账、修复暴露的 bug 并交付全库 RAG-ready 数据集的阶段；紧接在预推广试跑通过之后。



- **抽取流水线（Extraction pipeline）**：把 Help 主题页从站点抓取、清洗、元数据化、分块并同步为 RAG-ready 数据集的可重复运行流程；代码与产物位于本仓库 kb-pipeline/。
- **增量同步（Incremental sync）**：基于 HTTP 条件请求或变更信号，只抓取变化的主题页，避免全量重复下载。
- **全量对账（Full reconciliation）**：定期用完整页面清单重扫站点，纠正增量同步的漏抓、失效与删除。
- **同步状态（Sync state）**：增量同步与对账的运行时记录（每 URL 的 ETag/Last-Modified/内容 hash/状态/时间戳），存于仓库内 gitignore 的 JSONL 文件，不进入数据集产物。
- **例外表（Exception log）**：对账发现的结构性例外清单（未翻译/缺失页、已知重命名映射、失效图片 URL、删除事件），与数据集产物一起入库，供审计与下游使用。
- **墓碑（Tombstone）**：已从站点删除的 URL 在同步状态中的留存记录（删除时间与最后已知指纹）；数据集构建不包含墓碑页。
- **RAGFlow 数据集（RAGFlow dataset）**：RAGFlow 中的知识库容器，检索实测时把 RAG-ready 数据集灌入的**具体实例**（`monitorerp-help`）；区别于平台无关的 RAG-ready 数据集中间产物。单数据集双语混合、文档级元数据标注语言与质量层。
- **导入工具（import tool）**：把 RAG-ready 数据集导入 RAGFlow 的 CLI（`kb-pipeline/scripts/import_ragflow.py`）；按文档 `content_hash` 做全量对账（跳过未变/重建变更/清除消失），导入状态存 `state/ragflow-import.jsonl`。
- **检索实测（retrieval test）**：RAG 系统落地后，用中文问题清单夹具（questions-fixture）对 RAGFlow 数据集跑检索的验收环节；命中判定按主题全路径比对。
