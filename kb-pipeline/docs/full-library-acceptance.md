# 全站逐模块全库对账与交付验收报告

- 日期：2026-08-04；分支：`main`（地图「全站执行与交付地图（逐模块分批全库对账）」#38，T1 子票 #39）
- 触发命令：
  1. 逐模块 `py kb-pipeline/scripts/run_sync.py --mode reconcile --topic-path <模块>`（Sales /
     GeneralRegisters / Accounting / Purchase / UserGuide / TimeRecording / Manufacturing /
     Stock，含已交付模块幂等刷新；**每次门禁 EXIT 0**）
  2. 根级 5 主题 `--url` 单页对账（Glossary / LegalText / Modules / Resources / Search，en+zh）
  3. 全库合并数据集最终自检：**EXIT 0 / RESULT: ALL PASS**（`data/selfcheck-results.txt`）
  4. `py kb-pipeline/scripts/run_sync.py --mode check` → **ALL PASS**
- 依据：`docs/pipeline-spec.md`（§4–§6）+ 地图 D1–D9；门禁 D1/D2/D3（机器门禁 + 抽查 +
  结构例外定案）

## 1. 结论：全库 3923 个 en 主题全部对账通过 → 交付

- 全站 **3923/3923 en 主题**（9 模块 + 根级 5）全部入库；合并数据集 **7070 主题、
  8162 分块**（3923 en 保真层 + 3147 zh 参考层）。
- 全库质量门 **ALL PASS**：M1–M10 / C1–C10 机器检查 100% + Q1–Q7 转换质量逐页全检
  （本次最终自检覆盖全库），`--mode check` 抽查模板独立 ALL PASS。
- 结构例外 **805 条已审阅定案，全部非阻塞**（773 untranslated + 1 renamed +
  29 broken_image + 2 deleted[1 已 resolve]）。
- 本轮对账暴露并修复 **19 个代码 bug**（#40–#58，全部阻塞类按 D3 TDD 修复，
  154 测试全过），**无新增 renames**（`config/sync.json` 不变）。

## 2. 覆盖口径

| 范围 | en 主题 | zh 入库 | 未翻译 | 备注 |
| --- | --- | --- | --- | --- |
| UserGuide | 737 | — | — | 最大模块 |
| Sales | 573 | — | — | 含唯一非 ASCII 路径页 |
| GeneralRegisters | 530 | — | — | — |
| Stock（既有，D8 幂等刷新） | 507 | — | — | — |
| Accounting | 502 | — | — | — |
| Purchase | 469 | — | — | — |
| Manufacturing（既有，D8 幂等刷新） | 444 | — | — | — |
| TimeRecording | 156 | — | — | — |
| ROOT（Glossary/LegalText/Modules/Resources/Search） | 5 | — | — | `--url` 覆盖 |
| **合并数据集** | **3923** | **3147** | **773** | **7070 主题、8162 分块** |

zh 参考层入库 3147 / 3923 ≈ 80.2%；773 个未翻译 zh 页记 `untranslated` 例外（zh 同路径
404，不补译）。

## 3. 质量门结果

- 机器检查 M1–M10 / C1–C10：**全部 PASS**（含 M2 id 唯一稳定格式、M8 hash 重算一致、
  M9 镜像配对互逆、C8 token 上限、C9 分块配对）。
- 转换质量 Q1–Q7：**全库逐页全检 ALL PASS**。
- 图片验证：全库去重后图片引用 10408 个，**29 个失效**（`broken_image` 例外，见 §4）。
- 例外表 805 条 = 773 `untranslated` + 1 `renamed`（MobileClient↔WebClient，试点既有）+
  29 `broken_image` + 2 `deleted`（1 已 resolve：Säljare 页重入；1 源站删除：zh
  RegisterVoucher）。

## 4. broken_image 例外（29 条，非阻塞，已定案）

源站内容缺陷，均为行内小按钮/示意图片引用 404，正文完整，不阻塞交付：

- **9 条**沿用已知缺陷模式：相对路径多爬层级指向不存在的 `G5_<模块>_SV/` 版本子树
  （Accounting 2 / Sales 4 / Stock 2 / UserGuide 1）。
- **20 条**其他失效引用：图片在站点上确实不存在（curl 复核 404），分布于
  `Resources/Images/{SubProjects,TrainingMaterial,UserGuide}`、`Images_WebClient`、
  `Topics/.../Images/FAQ_Snippet_Images` 等路径，流水线解析忠实（数据集按源页原文
  解析为绝对 URL），按例外表保留。

## 5. 本轮修复的 bug（D3 分流：19 个阻塞类，全部 TDD 修复并回归）

| Issue | 类别 | 内容 |
| --- | --- | --- |
| #40 | 清洗/解析 | 非 ASCII 主题路径：抓取 URL 百分号编码 + id 拉丁转写（Säljare→Saeljare） |
| #41 | 清洗 | ul 内 <li> 间游离 callout 丢失 → walk 重构为 emit 分派 |
| #42 | 清洗 | 顶层 <a> 链接丢失（<a><img></a> 与 <p> 同级） |
| #43 | 检查 | raw_body_stats 嵌套表计数 → 只计顶层表 |
| #44 | 检查 | raw_body_stats 空锚点计数 → 跳过无内容 <a> |
| #45 | 清洗 | inline_md 丢 <a href='#'> 锚点内图片（MCDropDown 热点） |
| #46 | 清洗 | 块级 li 内联头部重复输出 / 缩略图去链 |
| #47 | 清洗 | 表格单元格内 <br/> 打断表格行 |
| #48 | 检查 | md_stats 标题正则跨行（空标题+文本合并） |
| #49 | 清洗 | <hX><p>text</p></hX> 非法嵌套 → 空标题 |
| #50 | 检查 | raw_body_stats 不计 <blockquote> |
| #51 | 检查 | Q1 噪声模式 'Skip to' 误报正文 |
| #52 | 检查 | raw_body_stats 计表格内标题 |
| #53 | 检查 | 标题含图片/链接时 Q2 文本比较失配 |
| #54 | 检查 | raw_body_stats 计 callout 内标题 |
| #55 | 清洗 | _inline_only 丢块级 li 直接子 <img>/<br> |
| #56 | 检查 | md_stats 链接正则跨行误拼链接 |
| #57 | 同步 | normalize_url 不去百分号编码 → 删除检测误清双记录产物 |
| #58 | 解析 | 根级主题（无目录段）URL 不可解析 → 可选主题路径段 |

## 6. 测试与合规

- 测试套件 **154 全部通过**（对账暴露的 19 个 bug 均带新增回归测试）。
- 合规：逐模块白天一次性 @5 req/s（D9 定案），可中断续跑（幂等）；`MonitorERP-KB-Bot/1.0`
  UA；无 robots.txt；429/5xx 指数退避；错误报告 completed、failed=0。

## 7. 已知限制

- 773 个 zh `untranslated` 页 + 29 个源站 `broken_image` + 1 个源站 `deleted`（zh
  RegisterVoucher）为结构事实，不补译/不修源站（范围外）。
- `data/raw` 仍 gitignore（R1）；重取可用 `run_sync.py`。
- 分块 token 估算为近似（cl100k_base 4 字符/token + CJK 每字 1）。
- 根级 5 主题经 `--url` 单页对账入库（无镜像扫描），配对为 None（站点导航/辅助页）。

## 8. 验收结论（T1 子票 #39 验收标准）

- [x] 全库 reconcile 门禁 ALL PASS（逐模块 EXIT 0；最终全库自检 EXIT 0 / RESULT: ALL PASS，
      M/C/Q 全过）
- [x] `--mode check` 抽查模板 ALL PASS
- [x] 结构例外审阅定案（805 条：untranslated/renamed/broken_image/deleted，全部非阻塞）
- [x] 冒出的 19 个 bug 按 D3 分流，阻塞类全部 TDD 修复并回归（154 测试过）；无新增
      renames（`config/sync.json` 不变）
- [x] 合并数据集产物 + 本验收报告入库，地图 Decisions-so-far 追加

**交付结论：全库对账通过，RAG-ready 全库合并数据集（3923 en + 3147 zh，7070 主题、
8162 分块）交付。**
