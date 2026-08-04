### 付款

#### 付款建议
如果你在供应商发票上使用现金折扣，你选择列表类型的现金折扣格式 付款建议 在里面 付款 程序。一个技巧是将此格式设为默认一。这是通过后台的默认值完成的。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/PresentatonCashDiscount.png)](../../../../Resources/Images/TrainingMaterial/PresentatonCashDiscount.png)
当你使用现金折扣时，激活设置非常重要 考虑现金折扣日期。你还应该为该设置配置一个默认值。当设置被已激活时，列表会已调整，使付款日期和已付金额考虑到现金折扣。
当你载入付款建议时，共同的会选择到期日在特定日期之前的发票，低于图片所示。当设置 考虑现金折扣日期 已激活后，现金折扣日期之前到期日的发票也将包含。这样做的目的是能够在现金折扣日期支付发票，即在常规的到期日之前。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/SettingsPaymentsIn.png)](../../../../Resources/Images/TrainingMaterial/SettingsPaymentsIn.png)
在现金折扣格式中，你可以看到与现金折扣有关的多个列。发票上的付款日期将根据发票的常规的到期日或现金折扣根据限制1或 3 进行已建议。如果已激活了折扣，你将以粗体字体看到现金折扣日期和现金折扣百分比。待支付金额将考虑每个发票可能出现的折扣，即减少现金折扣金额。折扣金额显示在到右边的单独一列。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/PaymentsOutList.png)](../../../../Resources/Images/TrainingMaterial/PaymentsOutList.png)

#### 手动支付
在手动付款期间，系统将考虑现金折扣（如果有），方式与登记收款时相同。阅读更多内容 [手工登记收款](PaymentsIn.htm)。

#### 支付由文件(订单)
当你通过文件订单付款时，现金折扣将以与付款建议相同的方式考虑。也就是说，系统基于可以获得的现金折扣建议付款日期和待支付金额。然而，如果使用现金折扣为时太迟，然后系统将建议在常规的到期日全额支付剩余金额。

#### 确认
当确认付款时，系统将认为发票付款已发送并扣减现金折扣。确认后，系统建议销账代码“现金折扣”。折扣和VAT的过账与收款时的方式相同。当使用现金折扣对发票进行部分付款时，现金折扣将在最终付款已确认时已编码。
