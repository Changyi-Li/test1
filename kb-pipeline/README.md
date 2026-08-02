# kb-pipeline — Monitor ERP help 抽取流水线

> 状态：Getting Started 试点已评审通过（「Getting Started 双语试点数据集」，2026-08-02）；规格定稿见 `docs/pipeline-spec.md`（「抽取流水线规格与仓库布局原型」评审通过，2026-08-02）。
> 生产同步 CLI（`run_sync.py`）按规格待实现；当前提供试点一键脚本。

## 一键运行（试点）

    py scripts/run_pilot.py               # 全流程：fetch → clean → metadata → chunk → check
    py scripts/run_pilot.py --stage fetch # 只跑某个阶段

依赖：Python 3.10+；`pip install beautifulsoup4 lxml`。

抓取自约束：help.monitorerp.cn 无 robots.txt，请求间隔 1 秒（日常 1–2 req/s 口径）。

## 布局

- `scripts/pipeline.py` — 共享库：抓取、清洗（`#contentBody` BS4 管线）、分块、token 估算
- `scripts/run_pilot.py` — 试点编排 + 验收自检；生产同步入口 `run_sync.py` 见规格 §5.7（待实现）
- `config/sync.json` — 同步节奏/限速/退避参数（规格 §5，未来 CI 同源读取）
- `state/` — gitignore；`sync-state.jsonl` 运行时缓存（生产实现后产生，不入库）
- `data/raw/` — gitignore；原始 HTML 与响应头（不入库，评审结论 R1）
- `data/clean/<topic_id 的 / 换成 _>.md` — 清洗后 Markdown（入库）
- `data/metadata.jsonl` — 每主题 13 字段元数据清单（入库）
- `data/chunks.jsonl` — 每块 14 字段分块 JSONL（入库）
- `data/exceptions.jsonl` — 例外表（untranslated / renamed / deleted / broken_image，入库）
- `data/selfcheck-results.txt` — 最近一次自检输出（入库）
- `docs/` — 规格、双语样张、验收报告、中文问题清单夹具

## 清洗规则（试点实测）

- 提取根 `#contentBody`（兜底 `.body-container`）
- 删除 `script/style/nav/header/footer/aside`、面包屑与侧栏容器（class 含 `breadcrumbs`/`nocontent`）、页脚版本行
- 保留标题层级（原样，不重排）；`note/warning/tip/important` → blockquote
- 图片相对路径解析为绝对 URL；展开/收起图标（`MCDropDown_Image_Icon`、`MCHelpControl_Image_Icon`）视为 UI 不入库；alt 原样保留不合成
- 链接保留（`#` 与 `javascript:` 开头的 UI 锚点除外）
- 表格/代码块按原子块保留（当前语料未出现）

## 分块规则（按「RAG-ready 数据集的元数据与分块规格」）

- 按 h2 子树切块；无 h2 时整页一块；h3 及更小标题跟随父 h2 并保留在块内容与标题路径中
- 目标 ~600 token、硬上限 ~1200；超限先按 h3、再按段落/列表边界二次切，列表/提示框/代码不切断
- 中文块按标题**位置路径**（层级内出现序号）单向映射英文同构块（`paired_chunk_id`）
- token 估算：CJK 每字 ~1 token，其余 ~4 字符/token（cl100k_base 近似，仅监控）