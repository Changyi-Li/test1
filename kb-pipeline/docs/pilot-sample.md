# 双语样张：Getting Started 主页面（en ↔ zh）

选点：英文 `GettingStarted.htm` 与中文同路径页，展示“原始 HTML → 清洗 Markdown → 元数据行 → 分块 JSONL”四段对照。

## 段 1：原始 HTML（节选）

`#contentBody` 实际包含大量 UI 噪音（语言/打印工具栏、侧栏菜单、面包屑），清洗时全部剔除：

```html
<div id="contentBody">
<div class="row collapse">
<div class="sideContent">
<div class="clearfix">
<div class="buttons popup-container clearfix topicToolbarProxy ... nocontent" ...>
<button class="button needs-pie select-language-button" title="Change language">...</button>
<button class="button needs-pie print-button" title="Print">...</button>
...
<div aria-label="Breadcrumbs" class="MCBreadcrumbsBox_0 breadcrumbs">...</div>
...
<h1>Getting started</h1>
<p data-mc-conditions="Web.Exclude content">Welcome to <span class="mc-variable Variables.ProductName variable">Monitor ERP</span>! ...</p>
<p>The program is also available as a mobile client, Monitor Mobile, ... <a href="../Interface/Interface.htm">user interface</a> ...</p>
```

完整原文：`data/raw/en-us/GettingStarted.htm`、`data/raw/zh-cn/GettingStarted.htm`。

## 段 2：清洗后 Markdown（全文）

**en-us/UserGuide/GettingStarted/GettingStarted.md**

```markdown
# Getting started
Welcome to Monitor ERP! This section of the online help is intended for those of you that are new users of the ERP system. Monitor ERP is primarily used as a program installed in Windows.
The program is also available as a mobile client, Monitor Mobile, which you can run in a browser or in an app for Android and IOS. Monitor Mobile is ideal for use in warehouses. Here you can read about the [user interface](../Interface/Interface.htm) and different [functions](../GeneralFeatures/GeneralFeatures.htm) in the program and about [Monitor Mobile](MobileClient.htm). If you are a system administrator you can read about how to [configure](../InstallConfig/Configuration.htm) Monitor ERP.
Before you start your training in the ERP system and before going live, there are different default settings which need to be controlled and possibly changed. Different basic data should also be registered. If the company is converting from Monitor G4, all data will be included, except for certain basic data which needs to be registered again. If the company changes from another ERP system to Monitor ERP you can import parts, customers, and suppliers from your old ERP system. The work regarding basic data needs to be performed before you can create inquiries, quotes, different orders, etc.
Read more about the basic data you normally should register in the [Basic data and settings](../Using/RegisterBasicData/BasicDataSettings.htm) topic.
In the online help function you can read more about [order flows](../Using/Flows/OrderFlows.htm), [how to use MONITOR](../Using/UsingMONITOR.htm), and [options](../Options/Options.htm). There are different order flows you need to have knowledge of to understand how uou work with inquiries, quotes, and different orders in Monitor ERP. These Monitor ERP options are purchased separately.
> The system administrator must register users and also needs to configure different parts of the system before you can start using Monitor ERP. When you register new users, the Force password setting is activated. This settings requires you to enter a password of a certain length and complexity for the user. You can read more about how the password policy and multifactor authentication (MFA) work in the [Security settings](../../GeneralRegisters/BasicSettings/SecuritySettings/wSecuritySettings.htm) section.
```

**zh-cn/UserGuide/GettingStarted/GettingStarted.md**

```markdown
# 已开始
欢迎来到 Monitor ERP！在线帮助功能中的此章节你主要针对 ERP系统的新用户和系统管理员。Monitor ERP 主要用作安装在 Windows 中的程序。该程序还有一个网络客户端。它可以在常规的网络浏览器中运行，也可以作为 Android 和 IOS 的应用程序运行。你可以在这里阅读 [用户界面](../Interface/Interface.htm) 和不同的 [功能](../GeneralFeatures/GeneralFeatures.htm) 在程序中以及关于 [网络客户端](WebClient.htm)。如果你是系统管理员，你可以阅读如何 [配置](../InstallConfig/Configuration.htm) Monitor ERP。
在你开始ERP系统培训和上线之前，有不同的默认设置需要控制并可能已变更。还应已登记不同的基础数据。如果公司从MONITOR G4 转换而来，则会包含全部数据，除了需要重新已登记的某些基础数据。如果公司从其他 ERP系统变更为 Monitor ERP 你可以从旧的ERP系统导入组件、客户和供应商。在你创建询价、报价、不同的订单等之前，需要执行有关基础数据的工作。
阅读更多基础数据你通常登记在 [基础数据和设置](../Using/RegisterBasicData/BasicDataSettings.htm) 话题。
在在线帮助功能中，你可以阅读更多关于 [订单流](../Using/Flows/OrderFlows.htm)， [如何使用MONITOR](../Using/UsingMONITOR.htm)， 和 [选项](../Options/Options.htm)。你需要了解不同的订单流程，以了解如何你询价、报价和不同的订单。 Monitor ERP。这些 Monitor ERP 选项需单独采购件。
> 系统管理员必须登记用户，并且还需要配置系统的不同组件，之前你开始使用 Monitor ERP。
```

## 段 3：元数据行（`data/metadata.jsonl`）

```json
{"id": "en-us/UserGuide/GettingStarted/GettingStarted", "title": "Getting started", "url": "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm", "source": "help.monitorerp.cn", "version": "25.8", "language": "en-us", "topic_path": "UserGuide/GettingStarted", "quality": "canonical", "lastmod": "2026-05-21T08:18:54Z", "etag": "\"c18ad76fae8dc1:0\"", "content_hash": "b2f62b21b6ca8494b28d5241eb276bfdef2d9be24d0e224d9ec173a18531914e", "images": [], "paired_topic_id": "zh-cn/UserGuide/GettingStarted/GettingStarted"}
{"id": "zh-cn/UserGuide/GettingStarted/GettingStarted", "title": "已开始", "url": "https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm", "source": "help.monitorerp.cn", "version": "25.8", "language": "zh-cn", "topic_path": "UserGuide/GettingStarted", "quality": "reference", "lastmod": "2026-05-21T08:22:34Z", "etag": "\"475ef9f9fae8dc1:0\"", "content_hash": "7e59c7a6c5006402d9dbd8846b8870d1e5ea5132e9f50a544c96d56bb8293543", "images": [], "paired_topic_id": "en-us/UserGuide/GettingStarted/GettingStarted"}
```

## 段 4：分块行（`data/chunks.jsonl`，content 省略、完整见文件）

```json
{"chunk_id": "en-us/UserGuide/GettingStarted/GettingStarted::0", "topic_id": "en-us/UserGuide/GettingStarted/GettingStarted", "order": 0, "title": "Getting started", "heading_path": ["Getting started"], "content": "# Getting started\nWelcome to Monitor ERP! ...", "language": "en-us", "quality": "canonical", "url": "https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm", "topic_path": "UserGuide/GettingStarted", "images": [], "paired_chunk_id": null, "char_count": 2353, "token_estimate": 588}
{"chunk_id": "zh-cn/UserGuide/GettingStarted/GettingStarted::0", "topic_id": "zh-cn/UserGuide/GettingStarted/GettingStarted", "order": 0, "title": "已开始", "heading_path": ["已开始"], "content": "# 已开始\n欢迎来到 Monitor ERP！ ...", "language": "zh-cn", "quality": "reference", "url": "https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Topics/UserGuide/GettingStarted/GettingStarted.htm", "topic_path": "UserGuide/GettingStarted", "images": [], "paired_chunk_id": "en-us/UserGuide/GettingStarted/GettingStarted::0", "char_count": 853, "token_estimate": 506}
```

## 双语同构块配对表（试点全量）

| 中文块 | 中文 heading_path | 英文块 | 英文 heading_path |
| --- | --- | --- | --- |
| `zh-cn/.../GettingStarted::0` | 已开始 | `en-us/.../GettingStarted::0` | Getting started |
| `zh-cn/.../WebClient::0` | Web客户端 | `en-us/.../MobileClient::0` | Monitor Mobile |
| —（zh 404，无中文页） | — | `en-us/.../MonitorBI::0` | Monitor BI |

配对按标题**位置路径**（h1#0 ↔ h1#0）命中，2/2 成功。