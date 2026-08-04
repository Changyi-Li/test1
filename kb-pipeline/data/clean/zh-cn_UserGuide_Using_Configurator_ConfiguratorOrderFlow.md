### 使用配置的订单流程

#### 报价和客户订单
当你登记与配置组链接至的组件的报价或客户订单时，你将看到一个按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Button_Configuration_Done.png) 在里面 配置 行上的列.你进行实际的配置的配置窗口将自动打开，除非你已在组件上未激活此功能。在这种案件下，你应该使用上面提到的按钮来打开窗口。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratingWindowGuide.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratingWindowGuide.png)
如果组件上有默认模板，则意味着选项和变量现在输入到 指南 根据模板进行标签页。在你选择选项并在各部分中输入变量值之前，您可以选择不同的模板或从先前的报价、客户订单或工单中载入设置。总是可以将当前配置保存为模板以供重复使用。
你可以在到左边展开导航树。如果配置很广泛的话这将很有用。在到右边你可以看到为已激活字段已添加的描述。
配置结果显示在 结果 标签页。你可以在那里选择要显示的信息。你还可以为每个选项和变量输入评论并选择在何处显示它们。可以调整价格和折扣。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratingWindowResult.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratingWindowResult.png)
当配置有效时，你可以通过单击按钮运行CDT 和计算 确认, 但不关闭此窗口 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinishedBox.png)。CDT 的结果和标准成本显示在配置窗口后面主要的窗口中的订单行上。
你后，使用按钮你配置 确认 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png)。这将关闭配置窗口并更新订单行上的价格。将自动已创建一个子行，显示有关配置的信息。
在文档中有一个特别的文档章节，你可以在其中根据您的设置查看配置。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfigurationDocumentComponent.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationDocumentComponent.png)
如果你已已配置组件应具有序列号，则其处理方式将与未配置的为组件相同。

#### 工单
你创建制造订单的方式与创建常规的组件的工单的方式相同。为已配置组件创建工单的最共同的方式是直接从客户订单创建。这 净需求计算 和 需求计算 程序负责基于配置创建正确的工单建议。
你创建的工单将作为正常工单功能。正在已配置的订单信息通过按钮显示 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Button_Configuration_Done.png) 在里面 工单信息。你按钮时将显示有关配置的信息。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfigurationMOrderInfo.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationMOrderInfo.png)
根据你在选项列表和变量以及文档设置中所做的设置，配置会显示在订单文档中。还显示配置指导。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfigurationMOrderDocument.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationMOrderDocument.png)

#### 采购
可以根据客户订单已配置采购件。当你为这些行创建采购订单时，信息将被已传输到采购订单并显示在文档上。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfigurationPOrderDocument.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationPOrderDocument.png)

#### 变更
如果你想更改已登记的工单上的配置，则这些变更将从配置的位置进行，在大多数案件下是在客户订单上。当你保存更改时（例如在登记客户订单程序中），将发生以下情况以使修改影响工单：
程序 与“BOM 与工艺路线”同步 会自动打开，你必须在那里检查并确认工单上的变更。通过使用按钮 运行同步检查 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) （Ctrl + 提醒）。

#### 版本管理
为了处理订单系统中已经使用的配置组的变更，系统会自动创建该配置组的新版本，即所谓的快照。
当你在配置组中进行更改时，不创建时间此新版本。它是在更改之后第一个时间在订单系统中你配置组时已创建的。
如果你在进行此类更改之后打开订单的配置，然后你按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_information.png) 低于 警告 配置窗口顶部的按钮。现在，你可以保持旧的配置组的订单，也你使用新版本的配置组更新订单。然后可以使用按钮 与配置组同步 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_refresh.png) 在窗口的顶部。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfigurationGroupChanges1.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationGroupChanges1.png)
> 同步之后，你应该检查订单上的配置是否正确。
对配置组进行重大变更之后，你可能需要新建的配置组并链接到各个组件。对于现有的订单，你然后在配置窗口中看到不同的警告。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfigurationGroupChanges2.png)

#### 售后
在产品登记中（程序 序列号 / 批次)你可以通过序列号输入每个已交货单位的附加信息。可以在登记客户订单连接已创建序列号。产品登记支持质保承诺、投诉、备件供应、维修等的跟踪和处理。
当使用产品配置时以及当执行/设计的变化可能因单位而异时，产品登记特别有用。
