# help 站点结构与页面清单机制 — 调查结论

对应 wayfinder 研究票「help 站点结构与页面清单机制」（issue #2）。调查日期：2026-08-02。所有结论基于对 help.monitorerp.cn 与 help.monitorerp.com 的实际 HTTP 探测（响应码/响应头/内容比对），每条结论附来源 URL。

## 结论速览

1. **唯一可用的全站清单是 sitemap.xml**：`https://help.monitorerp.cn/CN-MONITOR_G5/en-us/sitemap.xml`（HTTP 200，5128 条 loc，其中 3926 个 .htm）。zh-cn 没有 sitemap（`/CN-MONITOR_G5/zh-cn/sitemap.xml` → 404）。
2. **sitemap 的 URL 需要修复后才能用**：所有 URL 指向 `help.monitorerp.com`，且路径多写了一层 `Content`（`/en-us/Content/Content/...`）。修复规则 = 主机换 `help.monitorerp.cn` + 去掉 `Content/Content/` 中多余的一层。抽样验证：Home、Warehouse、VacationPreparations 等修复后 URL 均 200。
3. **Flare 的 TOC/Manifest 数据文件不存在（.cn）**：`Default.xml`（页面声明的 help system 文件，位于 `/en-us/Default.xml`）→ 404；`Data/TOC.js`、`Data/Menu.js`、`Data/Manifest.xml`、`Data/TOC.xml`、`Data/TOC.json`、`Data/Map.json`、`Data/TocData.js`、`Data/search.js`、`Toc.xml`、`Toc.json`、`Content/Default.htm`、`Content/Default.mcwebhelp` 在 `/en-us/` 与 `/en-us/Content/` 两个 base 下全部 404。页面内的 JS（`MadCapAll.js`）期望从 `Default.xml` 加载 TOC，但 .cn 上该文件缺失，说明 .cn 部署不完整——**不能依赖服务器端清单文件**。
4. **目录树可从主题路径本身重建**：主题页 URL 路径形如 `/en-us/Content/Topics/<Area>/<Module>/.../<Topic>.htm`，模块层级即目录树。修复后的 sitemap 共 3923 个主题页 + 3 个非主题页（`Home.htm`、`Search.htm`、`Default.htm`，前两个 .cn 上 200，`Default.htm` 404）。
5. **en/zh 映射基本是同路径镜像，但不完全**：随机抽样 280 个英文主题，中文同路径 200 的占约 **80%**（223/280）。缺失集中在较新模块（银行集成/保理、UserList 列表页、StockValue 列表页、版本差异 News、MonitorToolbox 等，疑似 26.5 新增英文页未翻译）。另有个别重命名：英文 `MobileClient.htm` 与中文 `WebClient.htm` 对应。**精确 zh 清单需全量 HEAD 镜像扫描**（3923 次，成本见「增量同步与抓取合规可行性」结论：约 6–27 分钟）。
6. **.cn 与 .com 的英文主题页内容基本同源**：对 Getting Started 页逐行比对，268 行中仅页脚版本行不同——.cn 为 **version 25.8**，.com 为 **version 26.5**；Last-Modified 分别为 2026-05-21 与 2026-06-26（.com 更新）。但 .com 的 `Default.xml` 已 302 到 **MadCap Central 登录门户**，站点壳不可匿名使用；静态主题页仍可匿名访问。

## 证据明细

### 1. sitemap 结构（en-us）

- URL：`https://help.monitorerp.cn/CN-MONITOR_G5/en-us/sitemap.xml` → 200，`text/xml`，877532 字节，Last-Modified 2026-05-21 08:16:26 GMT。
- 5128 条 `<loc>`；3926 个 `.htm`；其余为资源（`Resources/Images/*`、`Fonts/*`、CSS、脚本等）。
- 全部 URL 主机为 `help.monitorerp.com`；路径为 `/CN-MONITOR_G5/en-us/Content/Content/...`（双写 `Content`）。
- 无 `<lastmod>` 元素。
- 含两个死链：`/en-us/Content/Default.htm`、`/en-us/Content/Default.mcwebhelp`（.cn 上 404）。

### 2. URL 修复规则（已验证）

对 sitemap 条目做 `help.monitorerp.com → help.monitorerp.cn` 且 `/en-us/Content/Content/ → /en-us/Content/` 后，抽样 HEAD：

- `/en-us/Content/Home.htm` → 200（34278 字节）
- `/en-us/Content/Topics/UserGuide/Using/VacationPreparation/VacationPreparations.htm` → 200
- `/en-us/Content/Topics/UserGuide/Using/Warehouse/Warehouse.htm` → 200
- 对应 zh 路径（`/zh-cn/`）→ 200

修复后清单保存为 `topics-en-fixed.txt`（3923 条主题 URL，仅 `.htm` 且在 `/Topics/` 下）。

### 3. TOC/清单文件探测（.cn）

页面 HTML 声明 `data-mc-help-system-file-name="Default.xml"`、`data-mc-path-to-help-system="../../../../"`（解析为 `/en-us/Default.xml`）→ 探测 404（IIS 自定义 404 页，1245 字节）。

探测过的候选（均为 404，base 分别取 `/CN-MONITOR_G5/en-us/` 与 `/CN-MONITOR_G5/en-us/Content/`）：

`Data/TOC.js`、`Data/Menu.js`、`Data/Manifest.xml`、`Data/TOC.xml`、`Data/TOC.json`、`Data/Map.json`、`Data/TocData.js`、`Data/search.js`、`Toc.xml`、`Toc.json`、`Content/Default.htm`、`Content/Default.mcwebhelp`。

对比：`.com` 的 `/en-us/Default.xml` → 302（重定向至 MadCap Central `Secure Login` 门户）。

### 4. 目录树（修复后 sitemap 路径分布）

主题路径前缀即模块结构。按 `<Area>/<Module>` 聚合的前 25 名：

| 主题数 | 模块 |
| --- | --- |
| 305 | UserGuide/News |
| 239 | UserGuide/Using |
| 188 | Stock/Parts |
| 124 | Accounting/BankManagement |
| 121 | Purchase/Orders |
| 118 | Purchase/AccountsPayable |
| 113 | GeneralRegisters/BasicSettings |
| 109 | Sales/Orders |
| 108 | Accounting/Projects |
| 100 | GeneralRegisters/UserPersonnel |
| 92 | GeneralRegisters/OtherTables |
| 87 | Sales/Delivery |
| 79 | Sales/AccountsReceivable |
| 73 | Purchase/Suppliers |
| 66 | Sales/Customers |
| 65 | Sales/StatisticsFollowUp |
| 59 | Accounting/FixedAssetsRegister |
| 59 | Manufacturing/Planning |
| 57 | Purchase/Arrivals |
| 53 | Manufacturing/Reporting |
| 53 | Stock/Traceability |
| 53 | Manufacturing/Calculations |
| 52 | Manufacturing/Orders |
| 51 | UserGuide/GeneralFeatures |
| 50 | Manufacturing/Sustainability |

完整分布可由 `topics-en-fixed.txt` 的路径前缀生成；页面标题在抓取阶段从各页 `<title>`/首个标题取得（转换方案见「Flare HTML → 干净正文/Markdown 转换方案」）。

### 5. en/zh 映射与 zh 概况

- 映射规则：同路径替换语言段（`/en-us/` → `/zh-cn/`），已抽样验证 200。
- 覆盖率：280 个随机英文主题 → 223 个中文 200（**79.6%**；单独 200 样本随机抽样为 160/200 = 80%）。缺失页示例（均 404）：
  - `Accounting/BankManagement/ManageBankTransactions/bSettingsFactoring.htm`、`bSettingsManageTransactionsViaBankIntegration.htm`、`tManageTransactionsViaBankIntegration.htm`、`tCashReports.htm` 等（银行集成/保理，疑似 26.5 新增）
  - `GeneralRegisters/UserPersonnel/UserList/tListAbcenseForwarding.htm`、`tListAuthorizationLimits.htm`、`tListMobile.htm`
  - `Stock/Valuation/StockValue/tListDetailedTraceability.htm`、`tListRejectedInReceivingInsp.htm`
  - `UserGuide/News/DifferencesFromPrecedingGeneration/Manufacturing/LoadingPlan.htm`、`ReportPickList.htm`
  - `GeneralRegisters/SystemMaintenance/MonitorToolbox/wMonitorToolbox.htm`
- 重命名例外：`GettingStarted/MobileClient.htm`（en 200 / zh 404）vs `GettingStarted/WebClient.htm`（en 404 / zh 200）。
- zh 页面总数估计：约 3923 × 80% ≈ **3100–3200** 页（不含可能的 zh-only 页面；精确值需全量 HEAD 扫描）。

### 6. .cn vs .com（英文真源）

- Getting Started 英文页（同路径）：.cn 与 .com 均为 200，逐行比对 268 行仅 1 行（页脚版本）不同：
  - .cn：`Online help for version 25.8 of Monitor ERP`
  - .com：`Online help for version 26.5 of Monitor ERP`
- 响应头：.cn `Last-Modified: Thu, 21 May 2026 08:18:54 GMT`、ETag `"c18ad76fae8dc1:0"`（IIS）；.com `Last-Modified: Fri, 26 Jun 2026 15:34:44 GMT`、ETag 为 GUID 格式（非 IIS）。
- .com 站点壳（Default.xml）已迁入 MadCap Central 并需登录，但静态主题页仍匿名可访问。

## 权威清单生成方式建议

1. **基线清单**：用修复后的 sitemap（`topics-en-fixed.txt` 的生成规则）作为英文权威清单；抓取时对每个 URL 做可达性 HEAD 校验，404 即告警（避免 sitemap 再次失效时静默漏抓）。
2. **zh 清单**：镜像英文路径 + 全量 HEAD（约 3923 次），结果落成 zh 清单与“未翻译/重命名例外表”；这同时就是「增量同步与全量对账设计决策」的全量对账动作。
3. **层级与标题**：模块树从路径前缀生成；页面标题/链接在正文抓取阶段补充，不单独爬导航。
4. **不依赖** Flare 的 `Default.xml`/`Data/*` 清单（.cn 缺失，.com 需登录）。
5. **站点口径**：以 **help.monitorerp.cn** 为抓取与双语真源（中文内容只在 .cn；英文内容与 .com 基本同源，.cn 为 25.8 静态公开版）；.com 仅作内容抽样对照，不建议作为主抓取源（壳需登录、版本 26.5 与 zh 25.8 不一致）。

## 风险与依赖

- sitemap 无 lastmod、路径已坏过一次 → 每次发布后需重验修复规则（抽查 10–20 条）。
- zh 覆盖率基于抽样（约 80%），全量扫描前不视为精确数字。
- 若后续启用 .com 的 26.5 英文作为真源，会与 .cn 中文（25.8）出现版本错位，需在元数据规格中显式记录版本；本调查建议当前阶段以 .cn 为准。