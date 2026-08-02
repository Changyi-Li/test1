# kb-pipeline — Monitor ERP help 抽取流水线

> 状态：Getting Started 试点已评审通过（「Getting Started 双语试点数据集」，2026-08-02）；规格定稿见 `docs/pipeline-spec.md`（「抽取流水线规格与仓库布局原型」评审通过，2026-08-02）。
> 生产同步 CLI（`run_sync.py`）已交付（票 #14/#15/#16/#17/#18/#19）：参数解析、配置加载与同步状态原语、`--mode reconcile --url <主题 URL>` 单页端到端全量对账、`--mode reconcile [--limit N]` 清单驱动全量对账（sitemap → en 清单 → HEAD 校验 → zh 镜像扫描 → 完整管道 → 例外表 → 数据集自检）、`--mode incremental` 增量同步（条件请求 + 断点续跑 + dry-run），以及失败恢复与停止条件（429/5xx 指数退避、连续失败/错误率阈值停止、错误报告、中断续跑）。

## 一键运行（试点）

    py scripts/run_pilot.py               # 全流程：fetch → clean → metadata → chunk → check
    py scripts/run_pilot.py --stage fetch # 只跑某个阶段

依赖：Python 3.10+；`pip install beautifulsoup4 lxml pytest`。

抓取自约束：help.monitorerp.cn 无 robots.txt，请求间隔 1 秒（日常 1–2 req/s 口径）。

## 生产同步 CLI

    py scripts/run_sync.py --mode incremental|reconcile [--dry-run] [--limit N] [--url <单个URL>] [--rate <req/s>]

- `--mode` 必填（incremental | reconcile）；`--limit`/`--url` 为范围限定且互斥；`--rate` 覆盖当前模式限速；`--dry-run` 只预览不写产物。
- 非法组合/取值以非零码退出并给出可读错误。
- 限速/UA/退避/停止阈值来自 `config/sync.json`，可被 `--rate` 覆盖。
- `--mode reconcile --url <主题 URL>`（票 #15）对单页完成 抓取→清洗→元数据→分块→自检：原始 HTML 与响应头落盘 `data/raw/`（gitignore，不入库）；清洗 Markdown、13 字段元数据、14 字段分块与自检结果写入 `data/`；同步状态写 `state/sync-state.jsonl` 的 ok 记录（ETag/Last-Modified/content_hash）。重复运行幂等（按 id/topic_id 覆盖更新，保留其他主题既有产物）。
- `--mode reconcile [--limit N]`（票 #16/#19）清单驱动全量对账：下载 en-us sitemap → 修复规则（`help.monitorerp.com → help.monitorerp.cn`、去 `Content/Content/` 双写层）→ 过滤 `/Topics/*.htm` → 规范化去重 → en HEAD 可达性校验 → zh 同路径 HEAD 镜像扫描（含 `config/sync.json` 的 `renames` 已知重命名映射）→ 对样本主题跑完整管道（en 保真层 + zh 参考层）→ 未翻译/重命名/删除例外写 `data/exceptions.jsonl` → 全量数据集自检（M1–M10/C1–C10/Q1–Q6，镜像配对不再 SKIP）。`--limit N` 把本轮范围限定为清单前 N 个 en 主题（含其 zh 镜像）。sitemap 404 或 en 清单失配 >10% 时停止本轮、非零退出并告警，不使用旧清单静默继续。删除检测（票 #18）：曾 ok 的页面 200→404 或从 sitemap 消失时，状态留墓碑（deleted_at + 最后指纹）、例外表记 deleted、数据集清除该页旧产物并解除镜像配对；页面重现时墓碑清除、例外 resolved、重新入库。重跑幂等。
- `--mode incremental [--dry-run] [--limit N] [--url <单个URL>]`（票 #17/#19）日常增量同步：范围默认取同步状态中的已知主题（`--limit N` 限前 N 个，`--url` 只处理单个；已删除墓碑页不重探），对每个主题发起条件请求——状态有 ETag 时带 `If-None-Match`，否则用 Last-Modified 带 `If-Modified-Since`（IMF-fixdate）；返回 304 或指纹一致时不重写任何产物、状态保持，只对变化主题 GET 全文并更新 `data/` 产物与 `content_hash`。每条结果即时落盘，中断后可从 `state/sync-state.jsonl` 断点续跑，不重复抓取已完成项；重跑幂等。`--dry-run` 只做条件 HEAD 探测并输出本轮将抓取的 URL 清单，不发 GET、不写任何产物。曾 ok 页面 404/410 → 墓碑 + deleted 例外 + 产物清除；墓碑页不重探，--url 显式指定时可重新入库（票 #18）。
- 失败恢复与停止条件（票 #19，两种模式通用）：所有 GET/HEAD 遇 429/5xx 按 `config/sync.json` 的 `backoff` 指数退避重试（base×2^n 封顶 max_seconds，默认 1s→60s，读配置；下一跳延迟已达上限时放弃重试并计入失败）。每轮跟踪失败（含 en HEAD 校验与 zh 镜像扫描阶段的失败；404/410 视为删除/未翻译事件不计失败）：连续失败 ≥ `stop_conditions.consecutive_failures`（默认 5）立即停止；单轮错误率 > `stop_conditions.error_rate_percent`（默认 10%）轮末停止——停止均非零退出并把失败 URL 与原因写进 `state/sync-error-report.jsonl`（gitignore，不入库）供恢复排查。批量同步（incremental / reconcile）正常结束也写该报告（失败 0 条时为仅 summary，覆盖上一次报告避免残留误导；自检未通过时 summary 记录该状态）；单 URL 对账只在失败时写报告。每条结果即时落盘，任何中断（网络/手动/阈值停止）后续跑从同步状态恢复，不重复已完成工作。

## 测试

    python -m pytest kb-pipeline/tests

单元测试覆盖：同步状态读写（ETag/Last-Modified/content_hash/status/last_ok_at/deleted_at、墓碑与幂等重跑）、配置加载（含 `renames`）与 `--rate` 覆盖、`run_sync` 参数解析与非法组合、共享库按清单参数化与 HEAD 探测、单 URL 对账引擎（UA/限速/幂等/失败状态/自检）、sitemap 清单生成（修复/过滤/去重）与清单驱动对账引擎（en 保真层入库、zh 镜像扫描、未翻译/重命名/删除例外、sitemap 消失墓碑、页面重现恢复、>10% 失配停止、限速、幂等）、增量同步引擎（304 不重写产物、只 GET 变化页、404→墓碑与产物清除、中断续跑、dry-run 零写入、重跑幂等）、失败恢复与停止条件（429/5xx 退避重试与封顶、连续失败/错误率阈值停止、错误报告内容、阈值停止后续跑恢复）与 CLI 委托。

## 布局

- `scripts/pipeline.py` — 共享库：抓取、清洗（`#contentBody` BS4 管线）、分块、token 估算；站点/主题路径/主题清单由 `Manifest` 参数化（`pilot_manifest()` 为试点清单）
- `scripts/run_pilot.py` — 试点编排 + 验收自检
- `scripts/run_sync.py` — 生产同步 CLI（规格 §5.7）：计划预览 + `--mode reconcile --url` 单页对账（票 #15）
- `scripts/sync_engine.py` — 对账引擎：单 URL 全量对账 + 清单驱动全量对账（sitemap → en 清单 → HEAD → zh 镜像 → 完整管道 → 例外表 → 数据集自检 → 同步状态）
- `scripts/sync_manifest.py` — sitemap 修复/过滤/去重、zh 镜像 URL 推导（规格 §5.1/§5.2）
- `scripts/sync_state.py` — 同步状态原语（state/sync-state.jsonl，按 URL 读写）
- `scripts/sync_config.py` — 同步配置加载（config/sync.json + CLI 覆盖）
- `config/sync.json` — 同步节奏/限速/退避参数（规格 §5，未来 CI 同源读取）
- `state/` — gitignore；`sync-state.jsonl` 运行时缓存与 `sync-error-report.jsonl` 失败报告（生产实现后产生，不入库）
- `data/raw/` — gitignore；原始 HTML 与响应头（不入库，评审结论 R1）
- `data/clean/<topic_id 的 / 换成 _>.md` — 清洗后 Markdown（入库）
- `data/metadata.jsonl` — 每主题 13 字段元数据清单（入库）
- `data/chunks.jsonl` — 每块 14 字段分块 JSONL（入库）
- `data/exceptions.jsonl` — 例外表（untranslated / renamed / deleted / broken_image，入库）
- `data/selfcheck-results.txt` — 最近一次自检输出（入库）
- `tests/` — 单元测试（状态、配置、CLI、清单参数化）
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


