# 抽取流水线规格（草案 · prototype）

> **PROTOTYPE — 评审用草稿**：本文件位于 throwaway 分支 `prototype/pipeline-spec`，不入 main。
> 对应 wayfinder 票「抽取流水线规格与仓库布局原型」。评审通过后按评审结论定稿入库。
> 所有已定决策均来自地图「Monitor ERP help → RAG-ready 数据集：抽取流水线地图」的已关闭票；结论索引见 §8。

## 1. 目的地与范围

把 Monitor ERP G5 全站 help 变成**平台无关的 RAG-ready 数据集**：可重复运行的抽取流水线（抓取、清洗、元数据、分块），并已用 Getting Started 试点跑通「抽取 → 清洗 → 分块 → 评审」。

- 中文是问答主语言，英文是准确真源；数据集含两层：英文保真层（canonical）+ 现有中文参考层（reference）。
- 输出为每主题 Markdown + JSONL 元数据清单 + 分块派生产物；不依赖任何 RAG 平台。
- **不在范围内**：RAG 问答系统选型与落地、中文精修阶段、中文检索实测、修改 help 站点内容、help 之外的其他资料源、全站推广的实际执行、CI/监控/产物保留的具体接入（见 §9）。

## 2. 仓库布局（kb-pipeline/ 目标结构）

```
kb-pipeline/
├── README.md                    # 运行说明：安装、常用命令、限速与合规口径
├── config/
│   └── sync.json                # 节奏/限速/错峰时段/UA；未来 CI 同源读取
├── scripts/
│   ├── run_sync.py              # 同步 CLI（草案 §5.7）
│   ├── run_pilot.py             # 试点一键（现状，保留）
│   └── pipeline.py              # 共享库：fetch / clean / metadata / chunk / check
├── state/                       # gitignore；sync-state.jsonl（运行时缓存，不入库）
├── data/
│   ├── raw/                     # 原始 HTML + 响应头（生产 gitignore，评审点 R1）
│   ├── clean/                   # 每主题清洗后 Markdown（入库）
│   ├── metadata.jsonl           # 每主题 13 字段（入库）
│   ├── chunks.jsonl             # 每块 14 字段（入库）
│   ├── exceptions.jsonl         # 例外表（入库，草案 §4.3）
│   └── selfcheck-results.txt    # 最近一次自检输出（入库）
└── docs/
    ├── pipeline-spec.md         # 本规格（评审通过后定稿）
    ├── pilot-sample.md          # 双语样张（试点产物）
    ├── acceptance-report.md     # 试点验收报告（试点产物）
    └── questions-fixture.md     # 15 题中文问题夹具（试点产物）
```

评审点 R1：试点把 `data/raw/`（5 页 HTML）提交进了分支；全站推广后原始 HTML 约 7000+ 页，建议生产环境 gitignore `data/raw/`，只提交清洗后产物与例外表（原始内容可用 `run_sync.py` 重取）。

## 3. 模块划分

| 模块 | 职责 | 主要决策来源 |
| --- | --- | --- |
| M1 清单与同步 | sitemap 重生成/修复/过滤、HEAD 全清单、ETag 增量判定、zh 镜像扫描、图片 URL 验证、删除墓碑、状态文件、失败恢复 | 「增量同步与全量对账设计决策」 |
| M2 抓取 | 对变化页 GET 全文；可识别 UA；限速/退避；原始 HTML + 响应头落盘 | 「增量同步与抓取合规可行性」 |
| M3 清洗 | BS4 `#contentBody` 提取；噪音剔除；note→blockquote；链接/图片绝对化；alt 原样保留 | 「Flare HTML → 干净正文/Markdown 转换方案」+ 试点补充 |
| M4 元数据 | 13 字段清单；content_hash；同路径配对 + 重命名映射表；例外表 | 「RAG-ready 数据集的元数据与分块规格」+「知识库图片处理决策」 |
| M5 分块 | h2 子树切块；~600/~1200 token；原子保留；14 字段 JSONL；中文块单向映射 | 「RAG-ready 数据集的元数据与分块规格」 |
| M6 质量门 | 五条验收的机器自检（M/C）+ 转换质量 7 项逐页/抽查模板 | 「Getting Started 试点验收标准」 |

## 4. 数据 schema

### 4.1 主题元数据清单（metadata.jsonl，每主题一行，13 字段）

| 字段 | 取值/语义 |
| --- | --- |
| `id` | 稳定主题 id：语言 + 修复后相对路径，如 `en-us/UserGuide/GettingStarted/GettingStarted` |
| `title` | 页面标题（首个标题或 `<title>`） |
| `url` | 规范抓取 URL（`help.monitorerp.cn/CN-MONITOR_G5/<lang>/Content/Topics/...`） |
| `source` | `help.monitorerp.cn` |
| `version` | 页脚 Flare 版本号（当前 25.8） |
| `language` | `en-us` \| `zh-cn` |
| `topic_path` | 模块路径 |
| `quality` | `canonical` \| `reference`（`refined` 预留） |
| `lastmod` | HTTP Last-Modified，ISO 8601 UTC |
| `etag` | HTTP ETag |
| `content_hash` | 清洗后 Markdown 的 SHA-256 |
| `images` | 正文内图片绝对 URL 数组，无图为 `[]` |
| `paired_topic_id` | 同路径另一语言主题 id，缺失为 `null` |

### 4.2 分块派生产物（chunks.jsonl，每块一行，14 字段）

| 字段 | 取值/语义 |
| --- | --- |
| `chunk_id` | `{topic_id}::{order}` |
| `topic_id` | 所属主题 id（join 元数据清单） |
| `order` | 主题内顺序号（0 起） |
| `title` | 主题标题 |
| `heading_path` | 标题路径数组 |
| `content` | 块内 Markdown 原文（含标题行） |
| `language` | `en-us` \| `zh-cn` |
| `quality` | `canonical` \| `reference`（`refined` 预留） |
| `url` | 源页 URL |
| `topic_path` | 模块路径 |
| `images` | 块内图片绝对 URL 数组 |
| `paired_chunk_id` | 中文块的英文同构块 id；无配对或英文块为 `null` |
| `char_count` | 块字符数（监控） |
| `token_estimate` | cl100k_base 近似 token 数（仅估算/监控） |

分块规则：按 h2 子树切块，无 h2 整页一块；目标 ~600 token、硬上限 ~1200；超限先按 h3、再按段落/列表边界二次切（重叠仅限二次切，~64 token）；提示框/表格/代码/图片原子保留；中文块按标题位置路径单向映射英文同构块，匹配不上为 `null` 不做模糊匹配。

### 4.3 例外表（exceptions.jsonl，草案新增）

对账/抓取发现的结构性例外，一行一条，入库供审计与下游使用：

```json
{"id": "<topic id 或图片 URL>", "type": "untranslated|renamed|deleted|broken_image", "detail": "...", "discovered_at": "2026-08-02T00:00:00Z", "resolved": false}
```

- `untranslated`：zh 同路径 404，`paired_topic_id=null`（例：MonitorBI zh）。
- `renamed`：已知重命名映射（例：`MobileClient ↔ WebClient`），`detail` 记映射对。
- `deleted`：曾 200 后变 404 或从 sitemap 消失；数据集构建不含该页，状态文件留墓碑。
- `broken_image`：全量对账验证图片 URL 时 404（detail 记所属主题）。

### 4.4 同步状态（state/sync-state.jsonl，gitignore，不入库）

每行一条：`url / language / etag / lastmod / content_hash / status(ok|deleted|error) / last_ok_at / deleted_at`。新环境首跑无状态文件时自动退化为一轮全量 HEAD 重建。

## 5. 同步策略

### 5.1 权威清单

- 每轮全量对账重新下载 `en-us/sitemap.xml` → 修复规则（`help.monitorerp.com → help.monitorerp.cn`、去 `Content/Content/` 双写层）→ 过滤 `/Topics/*.htm` → 规范化 URL 去重 → HEAD 可达性校验。
- sitemap 404 或大量 URL 失配（如 >10% 404）→ 停止本轮并告警，不用旧清单静默继续。

### 5.2 中文清单

- 同轮对每个 en 主题的 zh 同路径全量 HEAD，生成 zh 清单 + 例外表（`untranslated` / `renamed` 两类）。
- zh-only 页不做主动发现（已知限制：.cn 无 TOC/Manifest 可爬）。

### 5.3 增量判定

ETag 优先 → Last-Modified 兜底（If-Modified-Since）→ GET 后重算 `content_hash` 复核。HEAD 全清单后只 GET 变化页。

### 5.4 节奏与合规

- 每周一次增量（错峰）；每月一次全量对账（sitemap 重生成 + zh 扫描 + 图片验证 + 删除检测）。
- 全量 ≤5 req/s、日常 ≤2 req/s；中国时区夜间错峰；可识别 UA（`MonitorERP-KB-Bot/1.0`）；遇 429/5xx 指数退避（1s→2s→4s…上限 60s）。

### 5.5 失败恢复

每条结果即时落盘，断点续跑、重跑幂等；连续 5 次失败或单轮错误率 >10% → 停止、非零退出、写错误报告（告警通道留给未来 CI）。

### 5.6 删除与去重

- 规范化 URL 去重（图片 URL 验证前同样先去重）。
- 200→404 或从 sitemap 消失 = 删除事件：状态留墓碑（`deleted_at` + 最后指纹）、例外表记 `deleted`，数据集只反映当前在线集。

### 5.7 手动触发

```
py kb-pipeline/scripts/run_sync.py --mode incremental|reconcile [--dry-run] [--limit N] [--url <单个URL>] [--rate <req/s>]
```

默认节奏/限速/时段/UA 在 `kb-pipeline/config/sync.json`；试点阶段手动触发，未来 CI 读同一配置。

## 6. 质量门

试点验收五条即为生产质量门：

1. 覆盖口径：en 主题 100% 抓取/清洗/入库；zh 按镜像存在即入库，缺失记例外不补译。
2. 元数据完整率：机器可查 100% 零容差（13/14 字段合法性、id 唯一、hash 重算一致、配对引用真实）。
3. 转换质量：每页 7 项全检 0 失败（无导航残留、标题层级一致、无截断/乱码、链接数一致、图片绝对 URL、提示框转 blockquote、表格/代码原子保留）。
4. 中文检索实测：本地图不含，仅保留问题清单夹具（15 题）。
5. 交付样张：整库产物 + 双语主题对端到端对照 + 验收报告。

全站推广抽查模板（草案）：机器检查 100%；转换质量按模块抽样，每模块 ≥5% 且 ≥10 页，7 项全过。

## 7. 试点结果摘要（Getting Started）

- 3 英文 + 2 中文主题入库；zh `MonitorBI` 404（`untranslated`）、`MobileClient ↔ WebClient` 重命名映射两个例外已确认处理。
- 一键自检 M/C/Q 全部 PASS；中文块配对 2/2；token 最大 1079 ≤ 1200。
- 双语样张、验收报告、15 题问题夹具在分支 `prototype/gs-pilot-dataset`（kb-pipeline/docs/）。
- 图片实测：截图无 alt；3 张样例 23–102KB；已定不入库、只记录 URL，全量对账验证。

## 8. 决策索引（地图 → 本规格）

| 规格章节 | 决策票 |
| --- | --- |
| §3 M1/M2、§5 | 「增量同步与全量对账设计决策」「增量同步与抓取合规可行性」 |
| §3 M3、§4 | 「Flare HTML → 干净正文/Markdown 转换方案」 |
| §3 M4/M5、§4.1–4.2 | 「RAG-ready 数据集的元数据与分块规格」 |
| §4.1 images、§4.3 broken_image | 「知识库图片处理决策」 |
| §6 | 「Getting Started 试点验收标准」 |
| §7 | 「Getting Started 双语试点数据集」 |
| 范围 | 「是否启用中文精修阶段」（Out of scope） |

## 9. 后续执行建议（评审通过后）

1. 本规格定稿为 `kb-pipeline/docs/pipeline-spec.md` 并入 main；试点产物按 §2 布局迁入正式目录（含 exceptions.jsonl 首版：MonitorBI zh、MobileClient↔WebClient）。
2. 按 TDD 实现 `run_sync.py` 与 M1–M6（试点脚本为基线）；先跑 `--mode reconcile --limit` 抽样验证，再手动触发一次完整 Getting Started 对账。
3. 全站推广执行（跑全量、修 bug）是地图终点后的新 effort，不在本地图。
4. CI 接入、产物保留策略、监控/告警通道仍在 Not yet specified，随本规格定形后收口。

## 10. 评审清单（reviewer）

- [ ] 布局（§2）是否符合预期；`data/raw/` 是否 gitignore（R1）。
- [ ] exceptions.jsonl 四类是否够用；字段是否要加（如 `paired_id` 映射字段）。
- [ ] 同步参数默认值（每周增量/每月全量、限速、退避阈值）是否合适。
- [ ] 质量门（§6）与抽查模板是否可执行。
- [ ] CLI 参数（§5.7）是否够用。
- [ ] §9 后续建议是否遗漏关键步骤。