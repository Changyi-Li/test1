# 检索实测：RAGFlow 作为首个 RAG 运行时，naive 上传 clean md

ADR 0001 把 RAG 运行时选型列为范围外；检索实测（questions-fixture 落地验收）选定
RAGFlow v0.26.4（本机 Docker，嵌入模型 Zhipu embedding-3）作为首个运行时，并把
RAG-ready 数据集的 clean md 以 naive 方式上传（单数据集双语混合、文档级元数据
标注 language/quality/配对），而非注入我们预计算的分块（chunks.jsonl）——首测目标
是对照 RAGFlow 自身解析与检索能力做端到端冒烟、保持工具最小；chunks.jsonl 仅作
元数据与后续对比基准。导入用全量对账式工具（kb-pipeline/scripts/import_ragflow.py）。

考虑过注入预计算分块（manual chunk_method，更忠实地测试自身产物，但逐块请求、
绕过 RAGFlow 解析）；首测舍弃，若 naive 检索质量不达验收，再切换。
