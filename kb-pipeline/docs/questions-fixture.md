# 中文问题清单夹具（RAG 落地后的检索实测用）

按「Getting Started 试点验收标准」第 4 条：检索实测推迟到 RAG 系统落地后，本清单为定稿夹具（待人工评审）。
每题标注预期答案主题与 2–3 条关键事实点；命中判定与答案正确性规则见验收标准结论。

| # | 中文问题 | 预期主题（en） | 预期主题（zh，如有） | 关键事实点 |
| --- | --- | --- | --- | --- |
| 1 | 我刚开始接触 Monitor ERP，应该从哪里了解系统？ | UserGuide/GettingStarted/GettingStarted | 同路径 zh | 该章节面向新用户；系统主要用作 Windows 程序；可阅读用户界面、功能与 Monitor Mobile |
| 2 | 公司从 MONITOR G4 升级到 G5，基础数据会全部保留吗？ | UserGuide/GettingStarted/GettingStarted | 同路径 zh | 全部数据包含；某些基础数据需重新登记 |
| 3 | 从其他 ERP 系统迁移到 Monitor ERP，旧系统数据怎么处理？ | UserGuide/GettingStarted/GettingStarted | 同路径 zh | 可导入零件、客户、供应商；基础数据需在创建询价/报价/订单前完成 |
| 4 | 上线前管理员需要做哪些准备？ | UserGuide/GettingStarted/GettingStarted | 同路径 zh | 登记用户并配置系统组件；Force password 激活、密码长度与复杂度要求；可查密码策略与 MFA 的安全设置 |
| 5 | Monitor ERP 的移动客户端叫什么？支持哪些运行方式？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | 叫 Monitor Mobile；可在浏览器或 Android/iOS 应用中运行 |
| 6 | 使用 Monitor Mobile 前需要满足什么条件？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | 必须安装 Monitor ERP Web 服务器；需为使用者配置用户设置 |
| 7 | 管理员如何允许用户登录 Monitor Mobile？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | Users 程序 Security 标签页激活“Allow login to Monitor Mobile”；输入密码或链接 Windows 账户 |
| 8 | 首次打开 Monitor Mobile 应用需要配置什么？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | 设置页输入 Web 服务器 URL；可选择是否显示通知 |
| 9 | Monitor Mobile 在仓库里能做哪些操作？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | 拣货、库存盘点、直接领用、直接到货、移动库存余额、案件登记等 |
| 10 | 移动端的用户权限与 Windows 客户端一样吗？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | 相同用户权限（对应程序和仓库） |
| 11 | Monitor BI 是什么？ | UserGuide/GettingStarted/MonitorBI | —（zh 404） | 把公司数据转为可视化洞察；预装仪表板；可新建/定制仪表板与 KPI |
| 12 | 选择 Monitor BI 的理由有哪些？ | UserGuide/GettingStarted/MonitorBI | — | 数据集中一处、创建仪表板与 KPI、基于 Web、Monitor ERP 标准内置 |
| 13 | Monitor BI 的详细说明在哪里？ | UserGuide/GettingStarted/MonitorBI | — | 有独立在线帮助站点（页面内链接）；入门页介绍要求与建议 |
| 14 | 如何通过浏览器登录 Monitor Mobile？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | 从管理员获取 Web 服务器地址；浏览器输入地址显示登录页；输入用户名与密码（或 Windows 账户密码） |
| 15 | 中文帮助里的“Web客户端”和英文帮助里的“Monitor Mobile”是什么关系？ | UserGuide/GettingStarted/MobileClient | UserGuide/GettingStarted/WebClient | 同一主题的中文参考页；重命名例外 MobileClient ↔ WebClient，配对已验证 |