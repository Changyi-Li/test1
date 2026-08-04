### 现金收据和内部发票

#### 现金收据
你在销售时使用现金收据，你你和打印发票连接收到现金付款（实际的现金或通过信用卡支付），例如在商店销售时。当你登记客户订单时也可以已选择现金收据。
现金收据一经已批准将自动已付款至应收账款。现金收据的过过账在客户开票日记账已记录中。对于这种发票类型，否已打印收款日记账（即使它自动设置为已付款）。
在现金收据类型的发票上，否显示付款条款。
现金收据有单独的文档模板，也可以有单独的编号序列（可选）。

#### 内部发票
内部的发票供内部的使用，用于处理内部的客户订单的销售，例如在贸易展览会提取货物时等。然后，你希望登记库存领用并获取领用的交货单，但发票仅已记录为内部的销售，与非已发送给客户。这里你经常在订单上使用内部的客户号（指自己的公司或者有时是公司内的部门）。你可能还会在处理组在中间的内部的开票时使用它。
内部发票的过账在客户开票日记账中。
内部发票有单独的文档模板，也可以有单独的发票号序列（可选）。

#### 确定订单和发票上的发票类型
订单类型
根据客户订单的订单类型和付款条款，你可以确定 发票类型 应用于订单和发票。对于订单类型你可以选择 根据客户付款条款， 内部的 （发票），或 现金收据。对于新订单类型，默认将根据客户的付款条款，但可以更改。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/CashReceiptInternalInvoiceOrderTypes.png)](../../../../Resources/Images/TrainingMaterial/CashReceiptInternalInvoiceOrderTypes.png)
付款条款
如果你选择 内部的 或者 现金收据 对于订单类型，你还必须选择 付款期限。付款期限决定了订单应如何已开票，即该期限的发票类型。全部你输入多个一贷项的天数付款条款将总是获得发票类型 发票 且无法已变更。对于没有贷项时间的付款条款，即将贷项天数编号设置零 (0) ，也可以选择现金收据或内部发票作为发票类型。新建的付款条件将默认被赋予发票类型“发票”。
你需要根据你的意愿配置现金收据和内部发票的付款条款。这是在 条款 程序。对于这些付款条款，你输入零 (0)作为贷项天数编号。在列中 发票类型 你选择 现金收据 或者 内部的。
当开票现金收据和内部发票时，这些将自动设置为已付款。对于现金收据，付款方式会影响发票已记录在哪个现金科目中。这就是为什么程序中针对该付款期限有一个默认付款方式。对于内部发票，付款方式不重要，因为过账是从标准科目与非付款方式科目加载的。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/CashReceiptInternalInvoicePaymentTerms.png)](../../../../Resources/Images/TrainingMaterial/CashReceiptInternalInvoicePaymentTerms.png)

#### 登记客户订单
在此程序中，你查询字段 发票类型 在里面 开票 盒子。根据上面，订单类型或付款条件决定了订单上使用的发票类型。只要订单不已开票，也可以在此程序中人工的更改变更订单类型、付款条件或订单的发票类型。当订单已开票时，它将获得你已选择的发票类型。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/CashReceiptInternalInvoiceOrderTypeOnOrder.png)](../../../../Resources/Images/TrainingMaterial/CashReceiptInternalInvoiceOrderTypeOnOrder.png)
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/CashReceiptInternalInvoicePaymentTermInvoiceTypeOnOrder.png)](../../../../Resources/Images/TrainingMaterial/CashReceiptInternalInvoicePaymentTermInvoiceTypeOnOrder.png)

#### 直接登记发票
关于订单类型、付款条款和发票类型，此程序的工作方式与 登记客户订单 程序。但在这里你也可以将发票类型更改为利息发票。在此程序中，也可以贷项现金收据和内部发票。
