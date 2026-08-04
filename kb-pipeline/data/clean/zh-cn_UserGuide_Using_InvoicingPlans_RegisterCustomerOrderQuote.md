### 登记客户订单 / 报价
这里描述了如何在登记客户订单程序中使用开票计划登记订单/报价。

#### 标签页页眉
你可以在这里输入订单 / 报价是否应根据开票计划已开票。这是在 开票计划 字段。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanTerms.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanTerms.png)
开票计划也可以通过客户设置自动已激活使用。这已配置在 [供应商登记](../../../Sales/Customers/CustomerRegister/wCustomerRegister.htm)或[客户列表](../../../Sales/Customers/CustomerList/wCustomerList.htm)程序。
如果你想通过项目结算跟踪订单，你可以在订单页眉中输入项目号。然后，项目号将自动用于可在项目上已编码的订单行以及在“开票计划”标签页下处理项目过账的分批发票上。请注意！如果你更改订单行上的项目，然后预付和尾款行的过账将不自动已更新。这些必须人工的已变更。

#### 行标签页
你照常在此登记客户订单行/报价行。也就是说，你不需要在此添加任何行和尾款。但是，每个行都有一个重要的复选框。你可以用它来决定哪些行应该被用于在开票计划中。这是通过列完成的 包括在开票计划。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanRows.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanRows.png)
未被用于在开票计划中的行可以照常已交货和已开票，与开票计划分开。例如，如果你已添加了需要已交货的额外产品或运费成本。

#### 开票计划标签页
在此标签页下，你可以看到订单 / 报价的开票计划。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanTab.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanTab.png)
在上方的框中，你可以看到不同的分批发票行，这些行是从在开票计划程序中已登记的开票计划模板中加载的。可以编辑/删除/添加行还可以更改预付发票和尾款发票上的更改名称。对于每个分批发票，你都应该输入已计划开票日期。这被称为“开票期间”。如果你稍后在开票计划列表中想要选择需要已开票的内容，则可以使用此方法。
在下方的框中，你可以看到有关包含在开票计划被用于的订单行的信息。
根据上面图片，你可以在标签页的底部看到不同类型的合计。在这里你还有机会确定如何交货相关订单。这是通过字段完成的 交货时检查未支付的预付款。例如，如果预付发票不已付全款，你可以冻结交货。此冻结既存在于交货计划中，两者存在于报告交货程序中。

#### 文档标签页
打印中订单确认单时，可以显示有关开票计划的信息。此信息显示在订单行低于。在程序中 [文档设置](../../../GeneralRegisters/DocumentManagement/DocumentSettings/wDocumentSettings.htm) 你可以选择或不显示该信息。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanOrderConf.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanOrderConf.png)
