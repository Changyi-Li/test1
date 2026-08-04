### 设置
这里周三描述了在你现金折扣之前你配置的不同设置 Monitor ERP。

#### 系统设置
在里面 系统设置 程序，在采购标签页下 [付款计划](../../../GeneralRegisters/BasicSettings/SystemSettings/bPaymentPlan.htm) 标题，你将查询以下未开票计划的重要系统设置：
1. 处理采购订单的付款计划
2. 支付预付发票期间处理暂扣 VAT
设置1 是用于激活系统中与开票计划相关的全部功能的主要的系统设置。
应已激活设置2，订单在已付款预付发票时将VAT从已暂停VAT已记录到销项 VAT。这意味着，只有预付发票已付款后，VAT不被纳入VAT 报告被用于。
> 请注意！还应输入预付组件已暂停的VAT。阅读更多 VAT设置 低于。

#### 过账矩阵/服务组件
创建预付款产品组（如果需要，还创建尾款/最终付款产品组）。在下面 采购科目 标签页卡中的 [过账矩阵](../../../GeneralRegisters/FinanceAccounting/PostingMatrix/wPostingMatrix.htm) 按照预付程序,你然后输入用于每个供应商组用于和尾款 的科目.
在里面 [组件登记](../../../Stock/Parts/PartRegister/wPartRegister.htm) 然后你程序创建预付和尾款的服务组件。请记得输入正确的服务组件产品组。

#### VAT设置
如需办理已暂停VAT，则适用以下规定。在 [VAT设置](../../../GeneralRegisters/FinanceAccounting/VATSettings/wVATSettings.htm)，你指定付款计划中的预付将具有已暂停VAT的VAT 代码。你可以在 每产品组例外 标签页，通过对这些付款计划行和发票使用单独的VAT 代码。对于产品组 进展，你输入了该国家 / 地区境内供应商已暂停VAT的VAT 代码。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanVatSettings.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanVatSettings.png)

#### 会计科目表
标记 订单号 有关预付款和尾款的结算科目。当这些科目的订单号被已激活时，系统将自动连接订单号进行过过账，并开具开票和付款。按订单号过账的目的是为了能够查询和协调这些结算科目的每采购订单的账面值。在里面 开票计划列表 程序，你就可以做出这样的对账。

#### 开票 / 付款计划
在 [开票 / 付款计划](../../../GeneralRegisters/FinanceAccounting/InvoicingPlans/wInvoicingPlans.htm) 你登记不同的开票计划和付款计划，以及相关设置。然后可以为客户、报价、客户订单和采购订单已选择这些内容。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlan1.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlan1.png)
在上面的框中，你可以定义应该有的开票和付款计划。在低于的框中，对于每个计划，你应用于该计划的分批发票以及分配给每个发票的百分比。
在里面 分批发票类型 字段输入你的类型：
- 预付 - 此发票在订单已交货之前已发送。对于预付类型的每个分批发票编号，都会已创建一个发票底单。当发票底单与供应商发票相链接时，输入的服务将作为已开发票应用。
- 交货 –订单已交货时随交货已发送的发票。该发票实际上是一份“常规的”发票底单，是在订单到货时已创建的。预付和尾款类型的分批发票将自动从此发票中已扣减。此分批发票类型可能会为同分批发票编号生成多个发票。如果采购订单进行了多个部分交货，并且你选择为每个部分交货发送发票，则可能会出现这种情况。
- 尾款 - 该发票将在尾款单独已发送，例如，当交货已在最终质检中获得已批准时。对于欠款类型的每个分批发票编号，将已创建与释放连接的发票底单。已记录发票底单时，输入的服务将应用已开发票。
