# Flare HTML → 干净正文/Markdown 转换方案 — 调查结论

对应 wayfinder 研究票「Flare HTML → 干净正文/Markdown 转换方案」（issue #3）。调查日期：2026-08-02。所有结论基于对 help.monitorerp.cn 实际页面的实测；样例输入、脚本与输出见本目录 `samples/` 与 `scripts/compare.py`。

## 页面结构事实（决定清洗策略）

对 20+ 个随机/代表性主题页（含 Getting Started、Warehouse Basics、Bank Integration、Security Settings、Sales Orders 等）的实测：

- 正文容器稳定：`<div class="body-container">` 内嵌 `<div class="content">` 与 `<div id="contentBody">`；转换时以 `#contentBody` 为提取根即可排除页眉、页脚、顶部导航、面包屑与工具栏。
- 标题层级不统一：主题标题有的是 `<h1>`（如 Getting Started），有的是 `<h3>`（如 Depreciation settings，其子节为 `<h4>`）；转换必须保留相对层级而不是假设“标题= h1”。
- **当前语料中没有 `<table>`、`<pre>`、`<code>`**：20 个采样页全部为 0（10 个随机页 + 5 个代表页 + Getting Started 双语页）。正文结构主要是：标题 + 段落 + 无序列表（10 页共 60 个 `<ul>`，`<ol>` 为 0）+ 截图 + 提示框。
- 提示框标记为 `<p class="note">` 等（实测 `Please note!` 在 `<p class="note">` 内）；另有 `warning/tip/important` 类。应转成 Markdown blockquote 或自定义 callout 标记。
- 截图以 `<img src="../../../Resources/Images/...">` 相对路径引用（在正文段落中），页眉 logo/社交图标也在 HTML 里但位于正文容器之外，天然被剔除。
- 相对链接指向同主题树内页面（`../Interface/Interface.htm`、`WebClient.htm`），可保留相对路径或解析为绝对 URL。
- 页脚版本信息（`Online help for version 25.8`）、`Powered by MadCap`、导航/搜索框均在正文容器外；基于 `#contentBody` 的提取不含这些噪音（已实测校验）。

## 四种方案实测对比

测试工具：trafilatura 2.2.0、readability-lxml 0.8.4.1、pandoc（pypandoc-binary 1.17，HTML→Markdown）、自研 BeautifulSoup/lxml 管线。样本 5 页（Getting Started en/zh、Warehouse Basics、Bank Integration、Sales Orders）。完整数字见 `samples/summary.md`，输出样例在 `samples/out-*.md`。

| 方案 | 标题层级 | 链接 | 图片引用 | 导航/页脚噪音 | 主要问题 |
| --- | --- | --- | --- | --- | --- |
| **trafilatura** | 保留 h1–h3 | 少量保留 | **全部丢失** | 无 | 图片全丢；链接页提取失败（Sales Orders 只出 126 字符） |
| **readability-lxml + pandoc** | 保留 | 多处丢失 | 部分保留 | 无 | 链接丢失不稳定；提取结果受正文结构影响 |
| **pandoc（裸跑）** | 保留 | 保留 | 保留 | **噪音大** | 把页眉/页脚/导航/脚本全部转出，需预处理 |
| **自定义 BS4 管线（#contentBody + 元素遍历）** | 保留（原样） | 保留 | 保留（正文内） | 无 | 需维护；表格/代码处理逻辑已内置但当前语料未触发 |

关键实测数据（示例）：

- Getting Started en：pandoc_raw 2916 字符（含导航噪音）vs custom_bs4 2352 字符；trafilatura 丢失图片引用，custom 保留正文图片。
- Bank Integration（14 张图）：trafilatura 0 图，readability+pandoc 与 custom 均 10 图（其余 4 张为页眉图标，正确地被剔除）。
- Warehouse Basics：三套工具标题数一致（9），但 custom 对 `<p class="note">` 正确转 blockquote，trafilatura 输出为普通段落。
- Sales Orders（链接密集型）：trafilatura 提取失败（126 字符），custom/readability 正常。

## 推荐方案

**采用自研 BeautifulSoup/lxml 清洗管线**（`scripts/compare.py` 中的 `custom_convert` 为可运行原型）：

1. 以 `#contentBody`（兜底 `.body-container`）为提取根，丢弃 `script/style/nav/header/footer/aside` 与根外一切内容。
2. 保留标题层级（h1–h6 原样转 `#`），不重排层级。
3. 段落、无序/有序列表、链接（`[text](href)`）、图片（`![alt](src)`）、`<p class="note|warning|tip|important">` → blockquote。
4. 表格/`<pre>`/`<code>` 转 Markdown 表格与代码块（当前语料未出现，逻辑保留备用）。
5. 相对链接原样保留（后续规格可决定解析为绝对 URL）。

**pandoc 作为可选后备**：对清洗后的片段（`#contentBody` 内 HTML）跑 pandoc 输出 Markdown，可减少手写转换器的维护面；但需注意 pandoc 对 Flare 特有 class 不做 callout 语义化。若团队更愿意少维护自定义代码，可组合“BS4 提取正文片段 + pandoc 转 Markdown”，放弃对 callout 的语义化。

**不建议**：trafilatura（图片/链接丢失，链接页失败）、readability-lxml（链接不稳定）、裸 pandoc（噪音）。

## 清洗规则清单

- 删除：`script`、`style`、`nav`、`header`、`footer`、`aside`、导航/搜索/工具栏容器、面包屑、页脚版本行、`Powered by MadCap`、社交图标、logo。
- 保留：标题层级、段落、列表、链接、正文内图片引用、提示框（语义化为 blockquote/callout）。
- 归一：实体解码（`&amp;` 等）、多余空白折叠、中文标点不做改动。
- 双语一致性：en/zh 页面结构相同（同一 Flare 输出），同一管线可直接复用；页面标题用首个标题或 `<title>`。

## 可复现性

- 依赖：`beautifulsoup4`、`lxml`（可选 `pypandoc-binary`）。测试环境为 Python 3.14 临时虚拟环境，安装命令见 `samples/summary.md` 生成过程；脚本 `scripts/compare.py` 无外部服务依赖，输入 HTML 在 `samples/input/`。
- 输出样例：`samples/out-custom_bs4-*.md`（推荐方案）、`out-trafilatura-*.md`、`out-readability_pandoc-*.md`、`out-pandoc_raw-*.md`。
