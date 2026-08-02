## Destination

一条可重复运行的抽取流水线规格 + Getting Started 双语试点验证：从 help.monitorerp.cn 的全站帮助网页（英文准确真源 + 中文问答主语言）抽取、清洗为平台无关的 RAG-ready 数据集（Markdown + JSONL 元数据 + 分块产物），并在 Getting Started 部分跑通端到端试点与中文检索质量验证。地图走完时：抽取路径上的每个决策都已定，剩余的是执行。

## Notes

- 领域：Monitor ERP G5 在线帮助文档（MadCap Flare 静态站，help.monitorerp.cn，en-us 与 zh-cn 两套语言站）。
- 已对齐的四个范围决策（详见本仓库 CONTEXT.md 与各票）：
  1. 目的地：抽取流水线规格 + Getting Started 试点；RAG 问答系统本身不做。
  2. 语言：三层入库——英文全部入库（保真层），现有中文全部入库（参考层，问答主语言），中文精修是否启用由试点证据决定。
  3. 输出：平台无关中间格式——每主题一个 Markdown + JSONL 元数据 + 派生分块。
  4. 落地：代码与文本产物进本仓库 kb-pipeline/；增量同步 + 定期全量对账；试点阶段手动触发；图片默认不入库（单独决策票）。
- 操作：所有 issue 操作走 gh CLI（见 docs/agents/issue-tracker.md）。
- 会话约定：决策票用 /grilling 与 /domain-modeling；原型票用 /prototype；事实调查用 /research（产物提交到 research/<name> 一次性分支）；一个会话最多手工解决一张决策票（research 票除外）。
- 术语：用 CONTEXT.md 术语表（Help 主题页、保真层、参考层、中文精修、RAG-ready 数据集、试点）。
- 引用票时用名称，不用裸编号。

## Decisions so far

<!-- 每张已关闭票一行：名称 + 链接 + 一句话摘要 -->

## Not yet specified

- 试点“中文检索质量够不够”的评估口径：用什么中文问题集、什么指标、达标线在哪——等试点产物与分块策略票之后才能精确化。
- 主题内特殊结构（表格/代码/提示框/截图）对检索的影响——等清洗规则原型票。
- 数据集版本与打包/发布方式（谁消费、怎么分发）——目的地边缘，试点后决定是否扩大范围。
- 试点通过后的 CI/定时自动化运行细节——目的地是“规格 + 试点”，自动化是执行层。

## Out of scope

- RAG 问答系统本身（向量库选型、嵌入模型、检索 API、UI）——目的地只到 RAG-ready 数据集。
- 全站大规模抓取与 CI/定时自动化的上线执行——目的地是规格 + Getting Started 试点。
- Web help 以外的知识源（PDF、旧版文档、内部知识）。
- help 文档的翻译工作本身（中文精修只做“是否启用”的决策，不在此地图内执行）。
