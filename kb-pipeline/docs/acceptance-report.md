# Getting Started 试点验收报告（自测）

- 日期：2026-08-02；分支：`prototype/gs-pilot-dataset`
- 自检命令：`py scripts/run_pilot.py` → 全流程成功，自检 **ALL PASS**
- 依据：「Getting Started 试点验收标准」五条；完整自检输出见 `data/selfcheck-results.txt`

## 1. 覆盖口径（3 英文主题 + 中文按镜像存在即入库）

| 主题 | 语言 | 状态 | 配对 |
| --- | --- | --- | --- |
| GettingStarted | en-us | 入库 | `zh-cn/.../GettingStarted` |
| MobileClient | en-us | 入库 | `zh-cn/.../WebClient`（重命名映射） |
| MonitorBI | en-us | 入库 | `null`（zh 404，见例外） |
| GettingStarted | zh-cn | 入库 | `en-us/.../GettingStarted` |
| WebClient | zh-cn | 入库（重命名例外） | `en-us/.../MobileClient` |
| MonitorBI | zh-cn | **未入库** — 404 | — |
| MobileClient | zh-cn | **未入库** — 404（重命名为 WebClient） | — |

结论：英文 3/3 = 100%；中文按镜像存在 2/2 入库；2 个例外已记录（见第 6 节）。

## 2. 元数据完整率（M1–M9，机器可查 100% 零容差）

全部 **PASS**，共 5 行：13 字段集合、id 唯一且格式稳定、url 规范、language/quality 枚举、version/lastmod/etag 非空且 lastmod 为 ISO8601 UTC、images 绝对 URL、content_hash 重算一致、paired_topic_id 引用完整且与镜像映射一致。

## 3. 转换质量抽查（全量逐页，Q1–Q6 + 人工目视）

| 页面 | Q1 无残留 | Q2 标题一致 | Q3 链接 | Q4 图片 | Q5 提示框 | Q6 表格/代码 |
| --- | --- | --- | --- | --- | --- | --- |
| en GettingStarted | PASS | PASS | 9/9 | 0/0 | 1/1 | 0/0 |
| en MobileClient | PASS | PASS | 5/5 | 3/3（绝对 URL） | 2/2 | 0/0 |
| en MonitorBI | PASS | PASS | 2/2 | 0/0 | 1/1 | 0/0 |
| zh GettingStarted | PASS | PASS | 8/8 | 0/0 | 1/1 | 0/0 |
| zh WebClient | PASS | PASS | 2/2 | 3/3（绝对 URL） | 1/1 | 0/0 |

人工目视复核：5 页清洗输出内容完整、无截断/重复/乱码，标题层级与原文一致，提示框均为 blockquote。

## 4. 分块（C1–C10）

全部 **PASS**：5 块（每主题 1 块，页面无 h2 时整页一块）；`order` 连续、`char_count` 一致、上下文字段与主题清单一致；token 估算最大 1079 ≤ 1200 硬上限；中文块配对 2/2 命中真实英文块。

## 5. 中文检索实测

推迟到 RAG 系统落地后（地图 Out of scope）。本试点交付夹具：`docs/questions-fixture.md`（15 题，含预期主题与关键事实点）。

## 6. 例外清单

- `zh-cn/.../MonitorBI.htm` → 404（疑似未翻译）：英文 MonitorBI 的 `paired_topic_id = null`，报告列出即可，不补译。
- `zh-cn/.../MobileClient.htm` → 404：同主题中文页为重命名后的 `WebClient.htm`（已知例外），已按映射入库并配对。
- 清洗规则试点补充：`#contentBody` 内面包屑容器（`breadcrumbs`/`nocontent`）与下拉展开图标（`MCDropDown_Image_Icon`、`MCHelpControl_Image_Icon`）视为 UI 噪音排除；`#`/`javascript:` UI 锚点不计入链接。

## 7. 待人工确认

1. 双语样张（`docs/pilot-sample.md`）与四段对照形式是否合意；
2. 问题清单夹具（`docs/questions-fixture.md`）是否需增删题目；
3. 是否批准本原型（决定「Getting Started 双语试点数据集」关闭与后续入库）。