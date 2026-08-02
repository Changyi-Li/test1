# Getting Started 完整对账验收报告（自测）

- 日期：2026-08-02；分支：`main`（本地图验收终点，票 #21）
- 触发命令：`py kb-pipeline/scripts/run_sync.py --mode reconcile --topic-path UserGuide/GettingStarted`
  —— 完整 Getting Started 全量对账：en 3 主题 + zh 镜像扫描 + 图片验证 + 例外表 + 数据集自检
- 依据：`docs/pipeline-spec.md`（§4–§6）+ 票 #21 验收标准；自检输出见 `data/selfcheck-results.txt`
- 独立抽查模板：`py kb-pipeline/scripts/run_sync.py --mode check` → **ALL PASS**（5/5 页）
- 重跑幂等：对账重跑 exit 0，`content_hash`/`etag`/`lastmod`/例外 `discovered_at` 逐字节不变

## 1. 覆盖口径（en 3 主题 + 中文按镜像存在即入库）

| 主题 | 语言 | 状态 | 配对 |
| --- | --- | --- | --- |
| GettingStarted | en-us | 入库 | `zh-cn/.../GettingStarted` |
| MobileClient | en-us | 入库 | `zh-cn/.../WebClient`（重命名映射） |
| MonitorBI | en-us | 入库 | `null`（zh 404，见例外） |
| GettingStarted | zh-cn | 入库 | `en-us/.../GettingStarted` |
| WebClient | zh-cn | 入库（重命名例外） | `en-us/.../MobileClient` |
| MonitorBI | zh-cn | **未入库** — 404 | — |
| MobileClient | zh-cn | **未入库** — 404（重命名为 WebClient） | — |

结论：en 3/3 = 100% 抓取/清洗/入库；zh 按镜像存在 2/2 入库；2 个结构性例外已记录（第 6 节）。

> 交付口径：本交付数据集只含 Getting Started 双语两层。此前 #16 `--limit 3` 抽样对账
> 留下的 Accounting 中间产物（3 en + 3 zh）不属于 Getting Started 交付物，已在入库前
> 从 `data/clean/`、`data/metadata.jsonl`、`data/chunks.jsonl` 清除（Accounting 仍在线，
> 同步状态未标删除；将来全量对账会重新覆盖）。

## 2. 元数据完整率（M1–M10，机器可查 100% 零容差）

全部 **PASS**，共 5 行：13 字段集合、id 唯一且格式稳定、url 规范、language/quality 枚举、
version/lastmod/etag 非空且 lastmod 为 ISO8601 UTC、images 绝对 URL、content_hash 重算一致、
paired_topic_id 引用互逆且与镜像扫描一致、缺失镜像的 en 主题有 untranslated 例外。

## 3. 转换质量（Q1–Q7 逐页全检，0 失败）

| 页面 | Q1 无残留 | Q2 标题一致 | Q3 无截断/乱码 | Q4 链接数 | Q5 图片绝对URL | Q6 提示框→blockquote | Q7 表格/代码 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| en GettingStarted | PASS | PASS | PASS | 9/9 | 0/0 | 1/1 | 0/0 |
| en MobileClient | PASS | PASS | PASS | 5/5 | 3/3 | 2/2 | 0/0 |
| en MonitorBI | PASS | PASS | PASS | 2/2 | 0/0 | 1/1 | 0/0 |
| zh GettingStarted | PASS | PASS | PASS | 8/8 | 0/0 | 1/1 | 0/0 |
| zh WebClient | PASS | PASS | PASS | 2/2 | 3/3 | 1/1 | 0/0 |

图片验证（票 #20 AC1）：数据集图片 URL 去重后 6 个全部 HEAD 200，0 失效，无 `broken_image` 例外。

## 4. 分块（C1–C10）

全部 **PASS**：5 行，每主题 1 块（页面无 h2 时整页一块）；`order` 0 起连续、`char_count` 一致、
上下文字段与主题清单一致、token 估算 ≤ 1200 硬上限；中文块 `paired_chunk_id` 2/2 命中真实英文块，
英文块为 `null`。

## 5. 中文检索实测

推迟到 RAG 系统落地后（本地图 Out of scope）。交付夹具：`docs/questions-fixture.md`（15 题，
含预期主题与关键事实点）。双语主题对端到端对照沿用试点样张 `docs/pilot-sample.md`
（本交付内容未变：清洗后 GettingStarted 5 页的 content_hash 与试点逐字节一致）。

## 6. 例外清单（`data/exceptions.jsonl`，2 条，均进行中）

- `zh-cn/.../MonitorBI` — `untranslated`：zh 同路径 404，英文 MonitorBI `paired_topic_id = null`，不补译。
- `zh-cn/.../MobileClient` — `renamed`：zh 侧页面为 `WebClient.htm`（`MobileClient ↔ WebClient` 重命名映射），已按映射入库并配对。

清洗规则试点补充（未变）：`#contentBody` 内面包屑容器（`breadcrumbs`/`nocontent`）与下拉展开图标
（`MCDropDown_Image_Icon`、`MCHelpControl_Image_Icon`）视为 UI 噪音排除；`#`/`javascript:` UI 锚点不计入链接。

## 7. 机器自检输出

完整输出见 `data/selfcheck-results.txt`；55 项 PASS、0 FAIL、0 SKIP，末行 `RESULT: ALL PASS`。
抽查模板输出见 `data/selfcheck-sample-results.txt`（ALL PASS）。

## 8. 验收结论

票 #21 五条验收全部达成：

- [x] 完整 Getting Started 全量对账成功（en 3 主题 + zh 镜像扫描）
- [x] 全部质量门 PASS；机器自检输出 ALL PASS
- [x] 双语配对验证：paired_topic_id/paired_chunk_id 引用真实且与镜像映射一致
- [x] 清洗 Markdown、元数据、分块、例外表与自检结果入库
- [x] README 补充生产同步 CLI 的用法与合规口径（见 `README.md` 生产同步 CLI 一节）

数据集产物为 RAG-ready 的 Getting Started 双语两层：en 保真层（canonical，3 主题）+ zh 参考层
（reference，按镜像存在 2 主题）。
