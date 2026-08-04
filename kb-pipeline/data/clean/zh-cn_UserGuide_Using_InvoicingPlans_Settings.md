### 设置
这里周三描述了在你现金折扣之前你配置的不同设置 Monitor ERP。

#### 系统设置
在里面 系统设置 程序，在销售标签页下，标题下 [开票计划](../../../GeneralRegisters/BasicSettings/SystemSettings/bInvoicingPlan.htm)，你查询以下未开票计划的重要系统设置：
1. 管理报价 / 客户订单的开票计划
2. 支付预付发票期间处理暂扣 VAT
3. 使用单独的科目用于开票和预付款
4. 基于开票计划自动激活客户订单上的远期汇率
设置1 是用于激活系统中与开票计划相关的全部功能的主要的系统设置。
应已激活设置2，订单在已付款预付发票时将VAT从已暂停VAT已记录到销项 VAT。这意味着，只有预付发票已付款后，VAT不被纳入VAT 报告被用于。
> 请注意！还应输入预付组件已暂停的VAT。阅读更多 VAT设置 低于。
应已激活设置3 来处理已付款和未付款预付款的单独科目。这样，就可以获得VAT 报告来显示与发票付款连接的营业额。对于国家 / 地区应缴纳VAT的贸易，应当这样做。如果你已经已激活设置2，那么你应该激活设置3。
通过设置4，你可以决定是否已允许对具有开票计划的货币订单和发票变量汇率。如果对此系统设置选择否，系统将不会为具有开票计划的订单未设置远期汇率。这意味着开票时应用的汇率将用于每个分批发票。请注意！如果预付科目存在汇率差异，则必须在会计中人工的已调整。该系统设置激活由。但是，你可以每订单覆盖此设置。

#### 过账矩阵/服务组件
创建预付款产品组（如果需要，还创建尾款/最终付款产品组）。在下面 销售科目 标签页卡中的 [过账矩阵](../../../GeneralRegisters/FinanceAccounting/PostingMatrix/wPostingMatrix.htm) 在 程序,你然后输入应该 使用 哪个科目用于支付每个客户组的预付和尾款.如果你有单独的未付款和已付款预付款科目，然后你应该在这里输入未付款预付款的科目。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanPostingMatrix.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanPostingMatrix.png)
在里面 [组件登记](../../../Stock/Parts/PartRegister/wPartRegister.htm) 然后你程序创建预付和尾款的服务组件。请记得输入正确的服务组件产品组。

#### 标准科目
如果你对发票和已付款使用单独的科目，你在 [标准科目](../../../GeneralRegisters/FinanceAccounting/StandardAccounts/wStandardAccounts.htm) 程序。此科目应输入行中 自客户预付款。请注意！你可能需要每客户组输入单独的科目。当VAT 报告从会计科目表中加载VAT 代码案件，你可能必须这样做才能实现正确的VAT报告。你可以使用行上的加号每客户分组创建例外。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanStandardAccounts.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanStandardAccounts.png)

#### VAT设置
在里面 [VAT设置](../../../GeneralRegisters/FinanceAccounting/VATSettings/wVATSettings.htm) 你配置系统在已暂停VAT科目上过账预付发票的程序。这是通过对此类发票使用单独的VAT 代码来实现的。这是根据 每产品组例外 标签页。在产品组上 进展，你输入VAT 代码，以便为该国家 / 地区境内的客户已暂停VAT。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlanVatSettings.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanVatSettings.png)

#### 会计科目表
标记 订单号 有关预付款和尾款的结算科目。当这些科目的订单号被已激活时，系统将自动连接订单号进行过过账，并开具开票和付款。按订单号过账的目的是为了能够查询和协调这些结算科目的每客户订单的账面值。在开票计划列表程序中，你可以进行这样的对账。

#### 开票计划
在里面 [开票计划](../../../GeneralRegisters/FinanceAccounting/InvoicingPlans/wInvoicingPlans.htm) 在程序中，你登记不同的“开票计划模板”并设置。然后可以为客户、报价和客户订单已选择这些内容。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InvoicingPlan1.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlan1.png)
在顶部的框中你可以定义应该存在哪些开票计划。对于每个开票计划，你在低于的框中输入哪些分批发票应应用于该开票计划，以及每个发票应占的百分比。
在里面 分批发票类型 字段输入你的类型：
- 预付 – 这是订单已交货之前已发送的发票。对于预付类型的每个分批发票编号，都会已创建一张发票。此处输入的服务将在已开票发票底单时应用已开发票。
- 交货 –订单已交货时随交货已发送的发票。该发票实际上是与订单交货连接的“常规的”发票底单。预付和尾款类型的分批发票将自动从此发票中已扣减。此分批发票类型可能会为同分批发票编号生成多个发票。如果客户订单进行了多个部分交货并且你选择为每个部分交货发送一发票，就会出现这种情况。
- 尾款 - 此发票将在尾款单独已发送，例如当客户批准由交货时。对于每个尾款类型的分批发票编号，都会已创建一张发票。此处输入的服务将在已开票发票底单时应用已开发票。
在下面 预付发票 / 尾款发票的发票文本，你可以输入是否需要在预付/尾款发票上显示任何附加文本信息。

#### 编号序列
对于预付发票，你可以设置单独的发票号序列。你可以在 编号序列 程序。
