# Manufacturing 模块全量对账与交付验收报告

- 日期：2026-08-03；分支：`main`（地图「Manufacturing 模块抽取执行与交付地图」#36，T1 子票 #37）
- 触发命令：
  1. `py kb-pipeline/scripts/run_sync.py --mode reconcile --topic-path Manufacturing` → **EXIT 0**
  2. `py kb-pipeline/scripts/run_sync.py --mode check` → **ALL PASS**（转换质量抽样 98/1837 页）
- 依据：`docs/pipeline-spec.md`（§4–§6）+ 地图 D1–D7；自检输出见 `data/selfcheck-results.txt`

## 1. 结论：Manufacturing 模块全量对账通过 → 交付

- 合并数据集（Getting Started 双语 + Stock 双语 + Manufacturing 双语两层）**全部质量门 ALL PASS**：
  **12880 PASS / 0 FAIL / RESULT: ALL PASS**；独立抽查模板 ALL PASS（98/1837 页）。
- 结构化例外（75 条：71 `untranslated` + 1 `renamed` + 3 `broken_image`）已审阅定案，非阻塞。
- 本轮**未暴露新代码 bug**（门禁零失败），无需 TDD 修复；**无新增 renames**（`config/sync.json` 不变）。

## 2. 覆盖口径

| 范围 | en 主题 | zh 镜像 | 备注 |
| --- | --- | --- | --- |
| Manufacturing 模块（`--topic-path Manufacturing`） | 444 | 421 命中 / 23 未翻译 / 0 重命名 | en HEAD 444/444 可达 |
| Stock（既有，试跑交付留存） | 507 | 460 | 48 未翻译 |
| Getting Started（既有，试点交付留存） | 3 | 2 | 1 未翻译 + 1 重命名 |
| **合并数据集** | **954** | **883** | **1837 主题、2086 分块** |

Manufacturing zh 镜像命中率 421/444 ≈ **94.8%**（高于 Stock 的 90.7%）；23 个未翻译页记
`untranslated` 例外（zh 同路径 404，不补译）。

## 3. 质量门结果

- 机器检查 M1–M10 / C1–C10：**全部 PASS**（含 M2 id 格式、C8 token 上限、C9 分块配对）。
- 转换质量 Q1–Q7 逐页全检（合并数据集）：**全部 PASS**。
- 图片验证：去重后 **357 个 URL，3 个失效**（`broken_image` 例外，见 §4）。
- 例外表 75 条 = 71 `untranslated` + 1 `renamed`（MobileClient↔WebClient，试点既有）+ 3 `broken_image`。
- 错误报告：`completed`，failed=0（本轮 ~1689 请求）。

## 4. broken_image 例外（3 条，非阻塞，已定案）

源站内容缺陷：外协单据发货页 `SubcontractDocumentShipped/bResult` 与可持续发展导入页
`SustainabilityImport/bImportFile` 的按钮图标引用了 `../../../../../../G5_Sales_SV|G5_Stock_SV/...`
（6 级相对路径，比正确层级多爬 2 级，指向不存在的版本子树）；三张图在正确路径
`CN-MONITOR_G5/en-us/Content/Resources/Images/` 下均存在（HEAD 200）。流水线解析忠实
（数据集按源页原文解析为绝对 URL），3 个引用按例外表保留；均为行内小按钮图标（Go to procedure /
Create shipment / Browse），正文完整，属外观性问题，不阻塞交付。

| 例外 id（URL 尾段） | 引用页 | 源路径缺陷 |
| --- | --- | --- |
| `.../G5_Sales_SV/.../button_link.png` | `en-us/Manufacturing/Subcontract/SubcontractDocumentShipped/bResult` | `G5_Sales_SV/` 子树不存在 |
| `.../G5_Sales_SV/.../button_add_shipping.png` | 同上 | `G5_Sales_SV/` 子树不存在 |
| `.../G5_Stock_SV/.../button_browse.png` | `en-us/Manufacturing/Sustainability/SustainabilityImport/bImportFile` | `G5_Stock_SV/` 子树不存在 |

## 5. 门禁决策沿用（D6/D7，地图 #22 定案）

- **D6 C8 原子块例外**、**D7 C9 非同构允许 None**：本模块对账沿用，自检全部 PASS。

## 6. 测试与合规

- 本轮**无代码改动**；测试套件保持 **134 全部通过**、**mypy clean**（7 源文件，既有交付基线复核）。
- 合规：Manufacturing 对账 ~1689 请求 @5 req/s 白天一次性；`MonitorERP-KB-Bot/1.0` UA；无 robots.txt；
  429/5xx 指数退避；错误报告 `completed`、failed=0。

## 7. 已知限制

- 23 个 Manufacturing zh `untranslated` 页 + 3 个源站 `broken_image` 为结构事实，不补译/不修源站（范围外）。
- `data/raw` 仍 gitignore（R1）；重取可用 `run_sync.py`。
- 分块 token 估算为近似（cl100k_base 4 字符/token + CJK 每字 1）。

## 8. 验收结论（T1 子票 #37 验收标准）

- [x] reconcile 门禁 ALL PASS（EXIT 0，M/C/Q 全过）
- [x] `--mode check` 抽查模板 ALL PASS（98/1837 页抽样；人工复杂页抽查按用户决定跳过）
- [x] 结构例外审阅定案（75 条：untranslated/renamed/broken_image，全部非阻塞）
- [x] 本轮无新代码 bug；无新增 renames（`config/sync.json` 不变）
- [x] 合并数据集产物 + 本验收报告入库，地图 Decisions-so-far 追加

**交付结论：Manufacturing 模块全量对账通过，合并数据集（Getting Started + Stock + Manufacturing，
1837 主题、2086 分块）交付。**
