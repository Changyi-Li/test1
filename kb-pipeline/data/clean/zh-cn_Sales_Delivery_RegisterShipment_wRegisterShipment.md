## 登记货运
在此程序中，你可以将有关货运的信息导出给您的货运代理，他们将退回/交付包含正确信息的运输文档供你打印。你还可以使用 EDI 向您的客户导出带有包装结构的拣货单发货通知。
你必须至少选择一 信息来源 之前你才可以编辑程序中的任何信息。
在你第一个导出之前，你必须已配置货运设置 nShift 交付， nShift Web-TA， 或者 日志贸易 在系统中。
nShift 和 Logtrade 的货运设置
1. 输入您的科目信息 nShift 交付， nShift Web-TA 或者 日志贸易 在下面 货运 导出类型 导出 / 导入设置 程序。
2. 在 nShift 或 Logtrade科目中配置全部特定于货代的设置，例如服务和附加服务。你还可以在此查询货运模板，你将其用作基础订单配置默认货运设置并名称它们。你可以使用以下方式访问您的 nShift 或 Logtrade科目 登录[货运服务] 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_url.png) 在此程序中的工具栏上。
3. 在里面 用户 你添加的程序 本地打印机 对于文档 货运 - 标签 和 货运 - 运货单。你还可以选择标签 货运打印格式 - 标签 字段。这需要为将发送EDI通知和打印运输文档的用户进行已配置。
4. 在登记货运服务和模板（可选） 货运服务 程序。在里面 货运模板代码 在该程序中的字段，你应该输入与在 nShift科目中相应模板中你的相同的名称。
5. 将交货方式与货运代理、货运服务和货运模板链接 条款 程序。模板中的设置与订单的交货方式链接至，然后会自动加载以进行货运。在程序中 登记货运 你可以在需要时覆盖特定货运的大多数默认设置。
这是你导出货运的方式
1. 检查货运的全部信息是否正确且完成 页眉 标签页。不要忘记货运中的附加服务（如果有的话）。这可以已添加 附加服务 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png)。
2. 在下面 行 标签页你可以检查和更新包装信息。
3. 需要时，你激活 使用客户信息 并在海关信息标签页下更新信息 海关信息 - 页眉 信息载入​ 加载海关信息 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 在行行。
4. 点击 导出 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_export.png) 或在程序中按Ctrl + 班次 + E来导出货运。然后，货运将被已传输（通过网络请求）至货运服务。货运包含有关发件人、接收者、货运包装数量、已选择的货代、服务以及货运是否合并等信息。
5. nShift 或 Logtrade登记该批货运并以同样的方式发后退货运号和运输文档的打印。这些文档将自动在你已选择的打印机上已打印。货运号和包装号（如果有）将显示在字段中 货代货运号 和 货代包装号 在程序的页眉行上。货运状态也将已更新，并显示在 状态 页眉行上的字段。
运输文档重印
如果你需要重印该批货运的运输文档，请使用 重印货运 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_print.png) 在工具栏上。与nShift 交付集成时，打印按钮将在货运第一个打印之后60分钟内未激活。之后，可以通过 nShift Delivery 的网址打印货物运费文档的新建份数。
发送 Email
点击 发送 Email 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_email.png) 你访问两种选项，通过Email向您的客户发送运单或货运通知。输入的Email 地址 接收者 用来。
货运失败/检查工序状态
如果货运导出失败，屏幕上会出现一条消息，同时 状态 页眉行上的字段。然后你可以使用 登录[货运服务] 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_url.png) 在工具栏上登录货运服务并检查和调整科目设置（如果需要）。如果实际的货运的信息有错误的或信息，建议你首先调整此问题 Monitor ERP 然后再次导出该货运。
你还可以时间检查工序状态 [货运状态] 的工序状态 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_url.png) 在工具栏上。
使用EDI导出具有包装结构的拣货拣货单的发货通知。
为了能够通过EDI导出具有包装结构的拣货单的发货通知，必须为拣货单上的客户已配置EDI 行为 （即，被用于在 EDI 行为 程序）。此外，拣货单不从 EDI 中排除（已配置单击 电子数据交换 按钮 发货包装 程序）。
1. 作为 类型 你应该选择信息来源 带有包装结构的拣货单 在里面 信息来源 盒子。
2. 在里面 信息来源 在表格中的行字段添加你通过 EDI已导出发货通知的拣货单。确保它说 是的 在里面 EDI导出 字段。如果出现以下情况，则不通过EDI导出拣货单的发货通知： 否。如果你希望将这些发货通知包含在同一个EDI导出被用于，你还可以添加更多带有拣货单的行。
3. 点击 EDI导出 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_send_edi.png) 在程序的工具栏上执行导出。然后，导出你在 管理 EDI 事务 程序。
