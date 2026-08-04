## 审核供应商发票
程序你已可用 [电子发票管理](../../../UserGuide/Using/EIM/ElectronicInvoiceManagement.htm) （EIM）选项。该程序也可用于用户许可证类型为 外部审核。
在此程序中，你可以复核并审核供应商发票。仅当你拥有到审核的发票时才可使用此程序。在标题你堆看到有多少张发票需要你到审核。为审核最长的发票将被自动加载。在里面 任务 功能 消息中心 在标题，你可以通过作为任务列出的发票堆打开程序。
审核人在中间的消息被输入与发票图像分开的文本日志中。如果发票与采购订单相链接，则会打开“标签顺序”链接选项卡。在该标签页下，你可以检查与相关发票相关的订单行。你还可以在此处创建新订单行链接。如果你是审核人，你可以访问订单链接标签页并将订单行链接到已加载的发票。你还可以在你现在处理的发票上视图供应商前道的发票。
工具栏上的按钮
工具栏上有用于保存、批准、转发、拒收和显示发票图像的按钮。
如果你对发票进行了变更，你保存 保存 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_save.png) （Ctrl + S）。你之后，保存发票保留在程序中。
这 批准 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_approve_document.png) 在此程序中，（Ctrl + 数量 ）至关重要。当你想要批准（审核）供应商发票时使用此方法。在使用此按钮之前你不保存变更。当你使用此按钮时，变更将自动已保存，无需控制问题。发票获得已批准后，将已转发给流程中的下一个一位审核人。如果你是批准/授权发票的最终审核人，你将收到一个问题，询问发票是否应该继续进行最终记录或是否应该仅获得已批准。在你已批准一张发票之后，下一个一张送至审核你授权的发票将自动加载。
你发票转发 转发 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_forward.png) （Ctrl + F）。然后会打开一个对话框，你可以在其中选择要采取的行动：是否你转发或两者批准并转发。在窗口的左边，你可以选择要将发票已转发给哪些审核人/审核人组。当你已转发发票时，即使你未批准/已审核，它也将从您的任务中删除。
例如，如果你希望将发票发送后退财务部门进行进一步调查，只需单击按钮 拒收 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_reject.png)。然后，发票将离开审核环节，并被放置在 已拒收 收件箱箱中的 导航 框中的 登记供应商发票 程序。
EIM 工作流
如果选项 EIM 工作流 安装后，你还会查询按钮 保存并发送至工作流 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_save_and_send_to_workflow.png) 在程序的 工具栏 上 。你使用此按钮保存对发票所做的更新，然后你其发送给 为审核 收件箱。案件发票在流程中停止并且仍保留在前第一个收件箱一中时，五月需要执行此类更新（见低于）。
如果你使用EIM 工作流，则导航面板和 导航 已已添加框。它的功能与导航面板相同 登记供应商发票 程序。导航面板中有收件箱，每个收件箱代表此程序中发票流程中的一个步骤，这些步骤包括：
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusOpPartiallyShipped.png) 查找订单 / 组件注意：如果已开发票不与采购订单行已匹配，则在此收件箱中已导入的物料发票将被卡住。在此收件箱中，你可以检查发票行上不匹配的内容，更正/调整并人工的将订单行链接到每个已开发票，然后在流程中发送发票为审核。
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridDeliveryTimeImage.png)等待到货报告：如果订单行不到货已登记，则在此收件箱中，已导入的物料发票将被卡住。这些发票不人工的处理，因为它们正在由工作流监控，并且会在订单行到货已登记时自动处理。
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_approve_document.png)为审核：仅当出于不同原因的发票需要已审核时，发票才会滞留在此收件箱中。需要审核原因的最共同的原因是当已配置了已允许的差异时 EIM 工作流设置 已经超出。当你授权发票后，它们将被已发送为最终记录。
