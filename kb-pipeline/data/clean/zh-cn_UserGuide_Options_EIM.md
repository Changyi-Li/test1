![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Options/EIM.png)

# 电子发票管理 (EIM)
电子发票管理 (EIM) 使你能够以电子方式管理从供应商已收到的发票，并将供应商发票链接到 Monitor ERP。EIM还提供对电子审核的支持。这使审核人能够收到有关审核和最终记录的提醒和消息。

#### EIM 如何工作？
供应商发票可以放在 Monitor ERP 以不同的方式：
- 扫描为PDF文件并放置在特定目录（收件箱）中的发票（纸质）。
- 通过Email已发送的发票（PDF）可以直接从Email客户端拖放到发票查看窗口。
- Monitor - to - Monitor电子发票（XML + PDF）将显示在特定目录（收件箱）中。
- 扫描、解释并然后已导入的发票（纸质）。
- 电子发票自动已导入。
- 通过Email已收到的发票（PDF），会自动解释并进行验证 Monitor ERP 在已登记之前。
当供应商发票已登记在 Monitor ERP，发票从指定的收件箱已导入。或者，可以使用光标从Email客户端人工的拖动发票文件并放入发票查看窗口。
PDF文件用于提供纸质发票的图片。该 XML文件用于从供应商发票导入数据以供登记。XML文件中的数据在导入窗口中与正确的采购订单和发票底单进行已匹配 Monitor ERP。
发票也可以暂估记录，而不必进行已登记。你还可以在登记和暂估输入后直接最终记录发票，前提是审核人拥有仓储费用做的用户权限。另一种方法是在发票被一或更多审核人审核由之后进行最终记录。
EIM 还提供为审核列表和审核人组的支持。

#### 捕获/解释
你可以激活解释和导入发票的功能。此功能通过 API链接至CrossState (OptoSweden) Monitor ERP。CrossState 是一种用于扫描和捕获/解释供应商发票的云解决方案。
数据捕获/解释功能有助于发票的登记，因为否手工登记发票上的信息。
与EIM 工作流选项结合使用特别有效，EIM发票捕获可自动执行整个发票流程 Monitor ERP从解释和导入供应商发票到审核和最终记录。阅读更多内容 [捕获/解释](EIMInvoiceCapture.htm)。

#### 电子发票
你可以激活在 EIM 中导入电子发票的功能。这样您的供应商就可以向你发送电子发票，这些发票将自动已导入 Monitor ERP。
你还可以激活导出电子发票的功能。利用此功能你可以向能够接收电子发票的客户发送电子发票。阅读更多内容 [电子发票](EInvoice.htm)。

#### EIM 工作流
EIM 工作流是一个选项，可以自动处理发票流程 Monitor ERP从登记、链接采购订单、审核到最终的发票最终记录。
通过使用 EIM 和EIM 工作流选项，你可以实现完全数字化和自动化的发票流程 Monitor ERP。这在行业内是独一无二的。阅读更多内容 [EIM 工作流](EIMWorkflow.htm)。
功能概览
| 功能 | 英美烟草公司 | 捕获/解释 | 电子发票 | EIM 工作流** |
|---|---|---|---|---|
| 手工发票登记 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |
| 手工导入Monitor - to - Monitor* | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished_15x15.png) |   |   |   |
| 自动导入Monitor - to - Monitor* |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |
| 自动导入已捕获的发票 |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |
| 自动导入电子发票 |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |
| 发送电子发票 |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |
| 电子审核流转 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |
| 通过应用程序/网络审核 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |
| 审核限制 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |
| 提醒管理 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |
| 手工最终记录 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   |   |
| 自动最终记录 |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |
| 自动采购订单匹配 |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |
| 行层级的审核/审核控制 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) |
*Monitor - to - Monitor
**EIM 的附加选项
有兴趣下班更多？请联系人我们的销售部门 [表格](https://www.monitorerp.com/contact-us/)。
