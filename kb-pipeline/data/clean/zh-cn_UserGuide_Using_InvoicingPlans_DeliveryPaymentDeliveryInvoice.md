### 交货及开票交货发票
如有交货计划，交货将照常进行。

#### 交货计划
如果订单的交货计划已经已激活，然后在预付发票不已付款的情况下就可以将其冻结。在里面 [交货计划](../../../Sales/Delivery/DeliveryPlanning/wDeliveryPlanning.htm) 程序，冻结 冻结交货 已在订单的开票计划上进行了核对，但时间预付不已付款。在这种模式下，不开始拣货订单。然而，任何不包含在开票计划中的订单行OK开始拣货。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanDeliveryPlanning.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanDeliveryPlanning.png)

#### 报告交货
在里面 [报告交货](../../../Sales/Delivery/ReportDelivery/wReportDelivery.htm) 程序, 如果预付发票还不已付款, 就会 显示警告或冻结, 就像 执行交货计划时 一样 .
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanReportDelivery.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanReportDelivery.png)
你报告交货订单，但是在已创建发票底单时（保存时），会插入附加的行（服务）。这些将根据开票计划扣除分批发票。扣减是按照已交货值的比例进行的。
例如：
订单合计值：100,000 欧元
开票计划：
预付30% – 30,000 欧元
交货60% – 60,000 欧元
尾款10% – 10,000 欧元
正在已交货的订单值：50,000 欧元
这结果一张扣减预付和尾款的发票，如下所示：
已交货值：50,000 欧元
扣减预付：-15,000 欧元
扣减尾款： -5,000 欧元
发票合计值：30,000 欧元
另请记住以下几点：
- 仅已标记的订单行进行扣减 包括在开票计划。
- 在交货报告中已添加的行不被视为被用于在开票计划中，因此否对这些行进行扣减。
- 系统从不会扣除多于预付/尾款的值，例如，如果你交付的数量大于供给 (+)的数量。
- 交货报告时删除剩余数量时，将基于已交货值进行扣减。已删除的值将否扣减。
超额交货或已删除剩余交货将导致订单上的已开票合计值与你已计划开具发票的值不同。可以通过以下方式已删除剩余记录 [登记客户订单](../../../Sales/Orders/RegisterCustomerOrder/wRegisterCustomerOrder.htm)。

#### 发票交货
连接交货，已创建交货发票的基础。这些发票通过常规的方式已开票 [复审 / 批准发票](../../../Sales/Invoicing/ReviewApproveInvoice/wReviewApproveInvoice.htm) 程序。
交货发票包含已已报告交货的订单行以及预付发票和尾款发票的扣除额。如果同一客户订单有多个部分交货，也可以创建汇总发票。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanInvoice.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanInvoice.png)
你可以在发票上看到有关开票计划的信息，其方式与预付发票上的信息相同。但在这里还可以看到已已开票的金额，以及剩余待开票金额的金额。
在发票上你还将看到有关预付发票上的发票号的信息。
