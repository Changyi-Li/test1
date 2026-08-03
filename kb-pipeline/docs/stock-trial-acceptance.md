# Stock 模块预推广试跑验收报告

- 日期：2026-08-03；分支：`main`（地图「全站推广执行」#22，T1 子票 #23）
- 触发命令：
  1. `py kb-pipeline/scripts/run_sync.py --mode reconcile --topic-path Stock`（第 6 轮，全修复后）→ **EXIT 0**
  2. `py kb-pipeline/scripts/run_sync.py --mode reconcile --topic-path UserGuide/GettingStarted`（恢复 Getting Started raw）→ **EXIT 0**
  3. `py kb-pipeline/scripts/run_sync.py --mode check` → **ALL PASS**（转换质量抽样 54/972 页）
- 依据：`docs/pipeline-spec.md`（§4–§6）+ 地图 D1–D7；自检输出见 `data/selfcheck-results.txt`

## 1. 结论：预推广试跑通过 → 可推广全站（T2）

- 合并数据集（Getting Started 双语 + Stock 双语两层）**全部质量门 ALL PASS**：
  **6825 PASS / 0 FAIL / RESULT: ALL PASS**；独立抽查模板 ALL PASS。
- 结构化例外（49 条：48 untranslated + 1 renamed）已审阅定案，非阻塞。
- 试跑期间暴露的 **11 个 bug（#25–#35）已全部修复**（TDD，134 单元测试 + mypy 通过），
  修复经真实数据重跑验证。

## 2. 覆盖口径

| 范围 | en 主题 | zh 镜像 | 备注 |
| --- | --- | --- | --- |
| Stock 模块（`--topic-path Stock`） | 507 | 460 命中 / 47 未翻译 / 0 重命名 | en HEAD 507/507 可达 |
| Getting Started（试点留存） | 3 | 2 | 重跑恢复 raw |
| **合并数据集** | **~510** | **~462** | **972 主题、1085 分块** |

zh 镜像命中率 460/507 ≈ 90.7%；47 个未翻译页记 `untranslated` 例外（zh 同路径 404，不补译）。

## 3. 质量门结果

- 机器检查 M1–M10 / C1–C10：**全部 PASS**（含 M2 id 格式、C8 token 上限、C9 分块配对）。
- 转换质量 Q1–Q7 逐页全检（合并数据集）：**全部 PASS**。
- 图片验证（票 #20 AC1）：去重后 **206 个 URL，0 失效**，无 `broken_image` 例外。
- 例外表 49 条 = 48 `untranslated` + 1 `renamed`（MobileClient↔WebClient，试点既有）。
- 错误报告：`completed`，failed=0。

## 4. 试跑暴露并修复的 bug（#25–#35）

| 票 | 类别 | 根因 | 修复 |
| --- | --- | --- | --- |
| #25 | 阻塞 | 表格内图片未绝对化（`table_md` base_url 丢空） | 透传 base_url |
| #26 | 阻塞 | `data/raw` 按页名平铺同名互覆 → Q 检查 174 页误报 | 改按 topic_id 编码文件名 |
| #27 | 阻塞 | M2 id 正则不允许括号（`tWarnings(intotal)`） | id_re 允许 `()` |
| #28 | 阻塞 | C8 token 硬上限：est_tokens 传 list + oversize 仅 path≥2 | 两处修（含 split_oversize_unit 返回字符串回归） |
| #29 | 非阻塞 | Q2 上标空白误报（`m 3 ` vs `m3`） | 标题比较去空白归一 |
| #30 | 阻塞 | Q7 `md_stats` 表格按行计数（一张 6 行表 → 6） | 改数分隔行 |
| #31 | 阻塞 | `<a>` 包裹图片（缩略图）整体丢失 | 保留为可点击图片 |
| #32 | 门禁决策 | C9 非同构 zh 块（zh 翻译缺 h4）配对不上 | 允许 None（按规格 §4.2），完全缺失仍 FAIL |
| #33 | 阻塞 | `inline_md` 不递归，li/div 内图片/表格/提示框扁平化 | 递归 + 块级列表项 |
| #34 | 阻塞 | 标签间换行文本节点切断表格单元格 | 折叠为单空格 |
| #35 | 阻塞 | `md_stats` 相邻表合并 | 分隔行计数 |

## 5. 门禁决策（D6/D7，用户拍板）

- **D6 C8 原子块例外**：超上限且无空行切分点的原子块（表格/列表/提示框，规格 §4.2
  「原子保留」）放行并在自检标注；有切分点仍超上限才判 FAIL。
- **D7 C9 非同构允许 None**：zh 翻译缺子标题导致位置路径对不上的 zh 块允许
  `paired_chunk_id=None`（不做模糊匹配）；悬空引用、主题不一致、某主题完全未配对仍 FAIL。

## 6. 测试与合规

- 单元测试 **134 全部通过**、**mypy clean**（新增 11 个回归测试）。
- 合规：Stock 试跑 ~2500 请求 @5 req/s 白天一次性；`MonitorERP-KB-Bot/1.0` UA；无 robots.txt；
  429/5xx 指数退避；全站跑（T2）排夜间错峰。

## 7. 已知限制（推广前审阅）

- 47 个 zh `untranslated` 页 + 1 个 `renamed` 例外为结构事实，不补译（与试点一致）。
- `data/raw` 仍 gitignore（R1），重取可用 `run_sync.py`；Getting Started raw 需重跑恢复。
- 分块 token 估算为近似（cl100k_base 4 字符/token + CJK 每字 1）。

## 8. 验收结论（T1 子票 #23 验收标准）

- [x] reconcile 门禁 ALL PASS（EXIT 0，M/C/Q 全过）
- [x] `--mode check` 抽查模板 ALL PASS（54/972 页抽样）
- [x] 结构例外审阅定案（49 条：untranslated/renamed）
- [x] 冒出的 11 个 bug 全部按 D3 开票修复并验证
- [x] 本验收报告 + 地图 Decisions-so-far 追加，给出「可以推广全站」结论

**推广结论：T1 通过，解除对 T2（#24）的阻塞。**
