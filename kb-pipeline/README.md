# kb-pipeline — Getting Started 双语试点（原型）

> 原型（prototype）：评审产物，位于 throwaway 分支 `prototype/gs-pilot-dataset`，不进入 main。
> 对应 wayfinder 票「Getting Started 双语试点数据集」。

## 一键运行

    py scripts/run_pilot.py               # 全流程：fetch → clean → metadata → chunk → check
    py scripts/run_pilot.py --stage fetch # 只跑某个阶段

依赖：Python 3.10+；`pip install beautifulsoup4 lxml`。

抓取自约束：help.monitorerp.cn 无 robots.txt，请求间隔 1 秒（日常 1–2 req/s 口径）；本试点共 7 个探测请求。

## 布局

- `scripts/pipeline.py` — 共享库：抓取、清洗（复用 `research/html-conversion` 的 BS4 `#contentBody` 管线）、分块、token 估算
- `scripts/run_pilot.py` — 阶段编排 + 验收自检
- `data/raw/<lang>/<page>.htm` — 原始 HTML；`data/raw/headers.json` 记录 status/lastmod/etag
- `data/clean/<topic_id 的 / 换成 _>.md` — 清洗后 Markdown
- `data/metadata.jsonl` — 每主题 13 字段元数据清单
- `data/chunks.jsonl` — 每块 14 字段分块 JSONL
- `data/selfcheck-results.txt` — 最近一次自检输出
- `docs/` — 双语样张、验收报告、中文问题清单夹具

## 清洗规则（试点实测补充）

- 提取根 `#contentBody`（兜底 `.body-container`）
- 删除 `script/style/nav/header/footer/aside`、面包屑与侧栏容器（class 含 `breadcrumbs`/`nocontent`）、页脚版本行
- 保留标题层级（原样，不重排）；`note/warning/tip/important` → blockquote
- 图片相对路径解析为绝对 URL；展开/收起图标（`MCDropDown_Image_Icon`、`MCHelpControl_Image_Icon`）视为 UI 不入库
- 链接保留（`#` 与 `javascript:` 开头的 UI 锚点除外）
- 表格/代码块按原子块保留（当前语料未出现）

## 分块规则（按「RAG-ready 数据集的元数据与分块规格」）

- 按 h2 子树切块；无 h2 时整页一块；h3 及更小标题跟随父 h2 并保留在块内容与标题路径中
- 目标 ~600 token、硬上限 ~1200；超限先按 h3、再按段落/列表边界二次切，列表/提示框/代码不切断
- 中文块按标题**位置路径**（层级内出现序号）单向映射英文同构块（`paired_chunk_id`）
- token 估算：CJK 每字 ~1 token，其余 ~4 字符/token（cl100k_base 近似，仅监控）