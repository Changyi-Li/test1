# 增量同步与抓取合规可行性 — 调查结论

对应 wayfinder 研究票「增量同步与抓取合规可行性」（issue #8）。调查日期：2026-08-02。所有结论基于对 help.monitorerp.cn 的实际 HTTP 探测；每个证据附来源 URL 与响应头。

## 结论速览

1. **增量同步可行**：站点为 Microsoft IIS/10.0 直接提供静态文件（无 CDN），主题页同时返回 ETag 与 Last-Modified；条件请求 If-None-Match / If-Modified-Since 均实测返回 **304 Not Modified**。用「本地记录 ETag/Last-Modified → 定时 HEAD 全清单 → 只 GET 变化页」即可实现可靠增量同步。
2. **版本指纹**：HTTP 层用 ETag（IIS 格式 `"hex:0"`，随文件变更号/时间变化）+ Last-Modified；内容层页脚含 Flare 变量 `Online help for version 25.8`（Year 2026），可作为数据集版本标注。全站文件发布时间为 2026-05-21 08:16–08:22 GMT（同一次发布）。
3. **全量对账成本低**：实测 12 次顺序 HEAD 平均 44ms/请求（首请求 155ms，后续 ~32–38ms）。按英文 3926 + 中文约 3926（1:1 估算，待 site-inventory 票确认）≈ 7852 个主题 URL：1 req/s 礼貌节奏约 2.2 小时，5 req/s 约 27 分钟。每月一次全量对账完全可行。
4. **无 robots.txt**：根路径返回 302（→ `/CN-MONITOR_G5/Default.htm`），`/robots.txt` 返回 HTML 跳转页，`/CN-MONITOR_G5/robots.txt`、`/en-us/robots.txt`、`/zh-cn/robots.txt` 均 404。按 RFC 9309 默认允许抓取，但应自约束。
5. **未观察到限流**：无 429/503、无 Retry-After、无 X-RateLimit 头；连续 12 个请求无减速。仍建议保守速率与退避策略。

## 证据明细

### 1. HTTP 响应头（HEAD，2026-08-02 04:30 GMT）

英文主题页：
`https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm`

```
HTTP/1.1 200 OK
Accept-Ranges: bytes
ETag: "c18ad76fae8dc1:0"
Server: Microsoft-IIS/10.0
X-Powered-By: ASP.NET
Date: Sun, 02 Aug 2026 04:30:23 GMT
Content-Length: 25986
Content-Type: text/html
Last-Modified: Thu, 21 May 2026 08:18:54 GMT
```

中文主题页：
`https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm`

```
HTTP/1.1 200 OK
ETag: "475ef9f9fae8dc1:0"
Last-Modified: Thu, 21 May 2026 08:22:34 GMT
Content-Length: 24797
Content-Type: text/html
Server: Microsoft-IIS/10.0
```

sitemap（en-us）：
`https://help.monitorerp.cn/CN-MONITOR_G5/en-us/sitemap.xml`

```
HTTP/1.1 200 OK
ETag: "b3914e1efae8dc1:0"
Last-Modified: Thu, 21 May 2026 08:16:26 GMT
Content-Length: 877532
Content-Type: text/xml
```

要点：
- 无 `Cache-Control` / `Expires` 头（IIS 静态默认）。
- 无 `Content-Encoding`（未启用 gzip 压缩）。
- 无 CDN 特征头（无 Age / X-Cache / CF-*），判定为 IIS 直连源站。

### 2. 条件请求实测（304 行为）

URL：英文 GettingStarted 页。

首次 GET 得到：
```
ETag="0eb6376fae8dc1:0"
Last-Modified=Thu, 21 May 2026 08:18:54 GMT
```

携带 `If-None-Match: "0eb6376fae8dc1:0"` → **HTTP 304 Not Modified**。

携带 `If-Modified-Since: Thu, 21 May 2026 08:18:54 GMT` → **HTTP 304 Not Modified**。

（注：PowerShell 的 Invoke-WebRequest 把 304 当作异常抛出，需在 catch 中读取状态码；HTTP 语义正确。）

结论：**ETag 与 Last-Modified 双通道都支持条件请求**，增量同步可以选择任一（建议 ETag 优先，避免 1 秒粒度的 Last-Modified 在同秒内多次发布时漏检）。

### 3. 版本指纹

- HTTP 层：ETag（IIS 静态文件 ETag 由文件变更信息生成，内容变化时变化）+ Last-Modified（粒度 1 秒）。同一发布批次（2026-05-21 08:16–08:22 GMT）内文件时间戳一致，可作为“发布批次”信号。
- 内容层：主题页页脚含 Flare 变量：
  `<span class="mc-variable Variables.VersionNumber variable">25.8</span>` 与 `Variables.Year` = 2026，文本为 “Online help for version 25.8”（来源：GettingStarted.htm HTML）。
- sitemap 内**无 `<lastmod>` 元素**（全文件扫描无匹配）。
- 页面 HTML 无 “Last updated” 字段、无 meta generator。

建议：数据集元数据中同时记录 HTTP Last-Modified、ETag 与内容中的文档版本号（25.8）；同步逻辑以 ETag 为主键判断变化。

### 4. 清单来源（影响对账成本）

- `en-us/sitemap.xml`：5128 条 URL（3926 个 .htm 主题页 + 1202 个资源）；全部 URL 指向 `help.monitorerp.com`（而非 .cn）且路径为失效的 `Content/Content/...` 双写路径；无 lastmod。→ 清单需做路径修正与主机替换（详见「help 站点结构与页面清单机制」票）。
- `zh-cn/sitemap.xml`：**404 不存在**。
- 常见 Flare TOC/Manifest 探测：`/en-us/Data/TOC.js`、`/en-us/Data/Manifest.xml`、`/en-us/Toc.xml`、`/en-us/Content/TOC.js` 均 **404**。
- 根路径 `https://help.monitorerp.cn/` 302 → `https://help.monitorerp.cn/CN-MONITOR_G5/Default.htm`；`/zh-cn/Default.htm` 200。

含义：全量对账必须基于“修复后的主题页清单”，不能依赖服务器端清单文件或 sitemap 的 lastmod。

### 5. 延迟与限流实测

对英文 GettingStarted 页连续 12 次 HEAD：

```
1 OK 155ms（首请求/连接建立）
2–12 OK 31–38ms
平均 44ms，总耗时 528ms
```

无 429/503/Retry-After/X-RateLimit 响应头。

### 6. robots.txt 与合规

- `https://help.monitorerp.cn/robots.txt` → HTTP 200，但内容是 JS 跳转页（HTML），非 robots.txt。
- `https://help.monitorerp.cn/CN-MONITOR_G5/robots.txt`、`/en-us/robots.txt`、`/zh-cn/robots.txt` → 均 404。
- 站点无任何 robots 指令 → 按 RFC 9309 默认允许抓取公开内容。

建议的抓取规范（自约束）：
- 使用可识别的 User-Agent（如 `MonitorERP-KB-Bot/1.0 (+内部知识库; contact: ...)`）。
- 速率：日常增量 1–2 req/s；每月全量对账 ≤ 5 req/s，突发不超过 10 req/s。
- 退避：遇 429/5xx 指数退避（1s → 2s → 4s … 上限 60s），连续失败停止并告警。
- 时段：避开中国时区工作日 8:00–22:00 高峰，全量对账安排在夜间/凌晨。
- 范围：只请求主题页 HTML（HEAD 为主），不下载图片/字体/脚本；图片仅记录 URL（见地图的图片决策票）。
- 内容用途：仅作为内部知识库数据源，不做公开再分发。

## 全量对账成本估算

| 项目 | 数值 |
| --- | --- |
| 英文主题页（sitemap .htm） | 3926 |
| 中文主题页（按 1:1 映射估算，待 site-inventory 票确认） | ~3926 |
| 合计 URL（两语言） | ~7852 |
| 实测单请求延迟 | ~44ms（顺序） |
| 1 req/s：总时长 | ~2.2 小时 |
| 5 req/s：总时长 | ~27 分钟 |
| 每月一次对账的月流量 | ~7852 × HEAD（无 body）≈ 可忽略 |

增量运行（每日）：同样 HEAD 全部清单（约 6–27 分钟），仅对 ETag/Last-Modified 变化的页面 GET 全文；正常情况下每日变化页为个位数到几十页，流量极小。

## 风险与依赖

- 站点结构若从 `Content/Topics/...` 变更，sitemap 的失效路径问题会重演 → 全量对账必须同时验证“清单 URL 全部可达”（HEAD 404 即告警），避免静默漏抓。
- 中文清单依赖 en/zh 映射规则（site-inventory 票产出）；若映射不完整，需补充从中文页导航爬取，成本会上升（可在对账时发现：中文清单条数 vs 中文导航计数）。
- 未见版本化 URL（如 ?v= 或 /25.8/ 路径），站点升级会原地覆盖文件 → ETag/Last-Modified 是全站升级后的必然变化信号，数据集应保留历史快照策略（每次全量对账后做内容 hash 对比并记录）。

