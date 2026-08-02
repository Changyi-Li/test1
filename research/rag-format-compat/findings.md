# 主流 RAG 平台摄入格式兼容性调查 — 调查结论

对应 wayfinder 研究票「主流 RAG 平台摄入格式兼容性调查」（issue #9）。调查日期：2026-08-02。只使用官方文档（primary source）；每条结论附来源 URL。

## 结论速览

1. **Markdown 是所有被调查平台/框架的一等摄入格式**：Dify、FastGPT、OpenAI File Search（Assistants）、Azure AI Search、LangChain、LlamaIndex 都直接支持 `.md`/文本摄入。本项目“每主题一个 Markdown”的设计**可直接消费，无需额外导出格式**。
2. **标题层级是最重要的结构约定**：Azure AI Search 的 Markdown 解析模式把标题解析为 `sections.h1..h6` 元数据（可配置最深到 h6）；LangChain 的 `MarkdownHeaderTextSplitter` 与 LlamaIndex 的 Markdown 节点解析器都把标题层级写进分块元数据。**清洗管线必须保留正确的标题层级**（本仓库「Flare HTML → 干净正文/Markdown 转换方案」已按此要求保留 h1–h6）。
3. **表格/代码块/提示框**：Azure 把非标题元素（列表、代码、表格）作为纯文本放进 `content` 字段；LangChain/LlamaIndex 保留 Markdown 原文；Dify 会把 Markdown 图片引用（`![alt](url)`）提取为附件。当前 Monitor ERP 语料中表格与代码块基本不存在，重点是保留提示框（blockquote/callout）与图片引用。
4. **元数据没有统一 schema，但字段名惯例可映射**：各平台用自己的机制（Dify 自定义字段 + 内置 `document_name/uploader/upload_date`；Azure 的 `metadata_storage_name`、HTML/文本的 `metadata_language` 等；LangChain/LlamaIndex 任意 metadata 字典）。JSONL 元数据建议采用 `title/source/url/language/lastmod` 这类通用字段名，摄入时逐平台映射。
5. **分块“平台生成 vs 预生成”两者都兼容**：OpenAI File Search 只能整文件摄入、由平台自动分块（用户不可控）——按主题页单文件恰好合适；Dify/FastGPT/Azure 可在摄入时自动按配置分块，也支持 API 直传分块（Dify Knowledge API 可手工创建 chunk，FastGPT 数据集 API 可控制 chunkSize/indexSize）；LangChain/LlamaIndex 直接消费预分块文件。**预生成分块是“低成本适配层”，不是必需层**。
6. **无需为被调查平台额外导出 PDF/txt/JSONL 作为唯一格式**；JSONL 仅在走 Dify/FastGPT 的 API 批量导入或 OpenAI 结构化检索（csv/jsonl）时有额外价值，可作为可选导出。

## 各平台明细

### Dify（docs.dify.ai）

- 知识库导入支持本地文件与文本/在线数据；上传上限每批 5 个文件、单文件 15 MB（专业版/团队版可批量 50 个）。来源：https://docs.dify.ai/en/cloud/use-dify/knowledge/create-knowledge/import-text-data/readme
- 文档提取器（Document Extractor 节点）支持 TXT、Markdown、HTML、DOCX、PDF 等文本类文档。来源：https://docs.dify.ai/en/cloud/use-dify/nodes/doc-extractor
- 分段/分块模式：通用分段、父子分段（Parent-Child）、Q&A、LLM 生成 Q&A；“转换为 Markdown”流水线面向 DOCX/XLSX/PPTX（官方不推荐 PDF）。来源：https://docs.dify.ai/en/cloud/use-dify/knowledge/knowledge-pipeline/create-knowledge-pipeline
- 图片：Markdown 语法引用的可访问图片 URL 会被自动提取为附件（每块最多 10 张），multimodal 嵌入可选；URL 保留在 chunk 文本中。来源：同上（Upload Local Files）。
- 元数据：Knowledge API 支持自定义元数据字段（string/number/time）、内置字段（`document_name`、`uploader`、`upload_date`）、标签（tags）；可手工创建/更新 chunk（content + keywords）。来源：https://docs.dify.ai/en/api-reference/guides/knowledge

### FastGPT（doc.fastgpt.io）

- 知识库支持导入 Word、PDF、TXT、Excel、Markdown 等文件；参数设置含解析方式、分块存储/索引方式、分块条件（token 数）、索引增强（含图片相关增强）；可预览分块效果。来源：https://doc.fastgpt.io/zh-CN/guide/getting-started/quick-start
- 数据集 API 支持分块拆分模式（`size` 按长度 / `char` 按字符）、`chunkSize`（默认 1500）、`indexSize`（默认 512，须小于索引模型最大 token）、自定义分隔符。来源：https://doc.fastgpt.io/docs/development/openapi/dataset/
- 官方介绍称知识库系统会把 PDF 等复杂结构处理为 Markdown（保留图片、表格、LaTeX），支持图片自动标注与索引。来源：https://doc.fastgpt.io/docs/workflow/modules/ai_chat

### OpenAI File Search / Assistants（platform.openai.com 文档；开发者文档 403 时以官方镜像页佐证）

- File Search 支持多种文件格式，包括 `.md`（text/markdown）、`.txt`、`.json`、`.csv`、`.pdf`、`.docx`、`.pptx` 等；支持 csv/jsonl 等结构化文件检索。来源：https://developers.openai.com/api/docs/assistants/tools/file-search （另见官方镜像 https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/file-search?tabs=rest）
- 上限：每个 assistant 最多 10000 个文件，单文件最大 512 MB、每文件不超过 500 万 token；**OpenAI 自动解析与分块**（用户不控制 chunk 大小），同时做向量与关键词检索。来源：https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/file-search?tabs=rest
- 含义：按主题页生成的小型 Markdown 文件是最佳粒度；预分块对 File Search 无意义，但 JSONL/元数据可用于其他平台。

### Azure AI Search（learn.microsoft.com/azure/search）

- Blob/File/OneLake 索引器原生支持 `parsingMode: markdown`，两种模式：
  - `oneToMany`（默认）：按标题把 Markdown 拆成多个搜索文档，输出 `content` + `sections.h1..h6`（标题层级元数据）+ `ordinal_position`（文档内顺序）；可用 `markdownHeaderDepth` 控制最深标题（默认 h6）。
  - `oneToOne`：整文件一个文档，输出 `document_content` + 嵌套 `sections`（header_level/header_name/content/ordinal_position）。
  - 列表、代码块、表格按纯文本进 `content` 字段。来源：https://learn.microsoft.com/en-us/azure/search/search-how-to-index-azure-blob-markdown
- 分块与向量化：可用 Document Layout 技能产出 Markdown 结构（标题/内容），Text Split 技能按 Markdown 段落约束块大小，再嵌入索引。来源：https://learn.microsoft.com/en-us/azure/search/search-how-to-semantic-chunking
- 元数据惯例：blob 索引器暴露 `metadata_storage_name`、`metadata_language`、`metadata_title`、`metadata_description`、`metadata_keywords` 等（HTML/纯文本/PDF 各有不同集合）。来源：https://learn.microsoft.com/zh-cn/azure/search/search-blob-metadata-properties

### LangChain（docs.langchain.com）

- `MarkdownHeaderTextSplitter`：按指定标题层级分块，把标题层级写进每个 chunk 的 metadata（如 `Header 1/Header 2/Header 3`）；`strip_headers` 可保留/去除标题行；再叠加 `RecursiveCharacterTextSplitter` 控制块大小与重叠（重叠不跨标题边界）。来源：https://docs.langchain.com/oss/python/integrations/splitters/markdown_header_metadata_splitter
- Markdown loader/爬虫（如 Firecrawl、Docling）默认输出 Markdown + 元数据，可直接进 LangChain 文档管线。来源：https://docs.langchain.com/oss/python/integrations/document_loaders/azure_document_intelligence

### LlamaIndex（developers.llamaindex.ai）

- Markdown 节点解析器按标题切分并把**标题层级写入 metadata**；`SimpleFileNodeParser` 自动选解析器、`FlatReader` 把文件信息放进元数据；再链 token 级切分器控制长度。来源：https://developers.llamaindex.ai/python/examples/node_postprocessor/filenodeprocessors/
- 官方 Python 文档说明文档加载后切成 Node（chunk），并支持给文档/节点附加元数据。来源：https://developers.llamaindex.ai/python/framework/understanding/rag/loading/

## 兼容性对照表

| 平台/框架 | Markdown 直接摄入 | 标题层级处理 | 表格/代码 | 元数据机制 | 分块方式 | 额外导出需求 |
| --- | --- | --- | --- | --- | --- | --- |
| Dify | 是（md/txt/html/docx/pdf） | 导入时可配置分段模式（通用/父子/Q&A），结构感知 | 文本保留；Markdown 图片 URL 提取为附件 | 自定义字段 + 内置字段 + 标签 | 平台自动，或 API 直传 chunk | 无 |
| FastGPT | 是（md/txt/pdf/docx/xlsx） | 分块参数可配置（size/char、chunkSize、自定义分隔符） | 文本保留（PDF 处理为 Markdown） | 数据集 API（集合/数据） | 平台自动，API 可控 | 无 |
| OpenAI File Search | 是（md/txt/json/csv/pdf/docx…） | 平台自动解析（用户不可控） | 文本保留 | 无自定义元数据入口（按文件） | 平台自动 | 无（整文件为宜） |
| Azure AI Search | 是（parsingMode=markdown） | 按标题拆文档，sections.h1–h6 元数据 | 非标题元素进纯文本 content | blob 元数据 + 索引字段映射 | 索引器/技能自动 | 无 |
| LangChain | 是 | MarkdownHeaderTextSplitter → 标题写进 metadata | Markdown 原文保留 | 任意 metadata 字典 | 库内切分（预生成或运行时） | 无 |
| LlamaIndex | 是 | Markdown 节点解析器 → 标题层级写进 metadata | Markdown 原文保留 | 文档/节点 metadata | 库内切分（预生成或运行时） | 无 |

## 对“Markdown + JSONL 元数据 + 预生成分块”设计的建议

1. **Markdown 文件**：每主题一个，保留真实标题层级（h1–h6），提示框用 blockquote/自定义标记，图片用 `![alt](绝对或相对 URL)`（Dify 可据此提取附件；Azure/OpenAI 当纯文本无害）。
2. **JSONL 元数据字段命名**（与各平台惯例对齐，方便摄入映射）：
   - `id`（稳定主题 id）、`title`、`url`（源页 URL）、`source`（站点/版本，如 `help.monitorerp.cn`）、`language`（`zh-cn`/`en-us`）、`lastmod`（HTTP Last-Modified）、`etag`、`topic_path`（模块路径）、`quality`（`reference` 等）、`images`（图片 URL 清单）。
3. **预生成分块**：作为可选派生产物，直接喂 LangChain/LlamaIndex/Dify API；对 Azure/OpenAI 只影响“少一次运行时切分”，不阻塞摄入。块内保留标题行（strip_headers=False 的等价物），并把标题路径写进块元数据。
4. **无需**为被调查平台维护 txt/PDF 导出；JSONL 本身已是通用批量导入格式。
5. **合规/体积**：Dify 单文件 15 MB 上限与 OpenAI 512 MB/5M token 上限对本项目（每页几十 KB）毫无压力；图片不下载仅记 URL 的做法与 Dify 附件提取兼容。
