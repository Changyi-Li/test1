## Question

平台无关的“Markdown + JSONL 元数据 + 预生成分块”设计，能否被主流 RAG 平台/框架直接或低成本消费？

需要调查（只信官方文档/primary source）：
- 常见平台/框架的文档摄入格式与约定：Dify、FastGPT、OpenAI File Search / Assistants、Azure AI Search、LangChain / LlamaIndex 的 loader 与 chunking。
- 对 Markdown 结构（标题层级、表格、代码块、提示框）的保留要求；元数据字段惯例（title、source、language 等）。
- 分块由平台生成 vs 数据集预生成：各自的兼容性结论。
- 是否需要为某平台额外导出格式（如 JSONL 约定、txt/PDF）。

交付：结论与证据写入 research/rag-format-compat/ 下的 Markdown（引用每个来源 URL），在本票评论中给摘要。
