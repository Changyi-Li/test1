### 页眉行

#### 订单号
在此字段中，您可以输入新的订单号或使用查找功能加载现有的订单号。订单号为字母数字，最多可包含15个字符。
如果您没有输入订单号，则系统将在保存订单时从编号序列中分配一个新的订单号。如果您手动输入订单编号，系统将检查输入的编号是否已经存在，在这种情况下，它将加载现有订单。
新记录通过该字段中显示的绿点![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/green_dot.png)进行突出显示。首次保存记录后，该点将消失。
如果订单号与案件相关联，则按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridConnectImage.png) 字段下一个的将可用。通过使用此按钮，你可以在 登记案件 程序。

#### 订单类型
在这里你选择客户订单的类型。你在您的用户科目中设置的默认订单类型将在此默认已建议。如果你不在此处已配置默认订单类型，然后系统将已建议你在最近的订单中使用的订单类型。当需要时，可以选择其他订单类型。通过使用 变更订单类型 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_change_record.png) 你还可以更改现有的订单的订单类型。
订单类型 新建销售 被用于在系统中。你需要的其它订单类型必须第一个在 订单类型 程序。订单类型决定了价格策略，过账组，已链接采购订单的交货地址，是否应用交货计划，是否应用预估拣货单，付款条款，汇率类型，信用期限，发票类型，付款方式，销售统计，预估客户订单和优先级。

#### 状态
在这里你可以看到以符号表示的客户订单状态。工具提示以文本形式显示状态。

#### 客户
在这里你可以从客户登记中选择客户。当你打开该程序时，光标会自动定位在此字段中。客户订单上强制的有客户。第一个时间你该程序打开，此字段为空。下一个你时间程序时间，你将看到最后你的客户号。当你已选择了客户号后，客户名称将显示在到右边。使用按钮 变更客户 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_change_record.png) 你还可以变更客户现有的订单的客户。
如果客户因登记订单客户登记已冻结，则会出现一条消息，你也可以在其中查看冻结的原因。在这种模式下，不为客户创建订单。如果已经为客户已配置了通知，你将看到该消息/通知，但你仍然可以为客户创建订单。你可以使用按钮重新打开该消息 显示消息 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_comment.png)。

#### 客户的订单号
你可以在此字段输入客户的订单号。然后将根据该订单号检查客户的现有的订单。如果客户已登记的另一个订单已输入该信息，则会显示一个对话框 客户的订单号。在该对话框中，你可以选择转到该订单。但是，可以创建包含相同内容的多个客户订单 客户的订单号。
如果客户订单是在从交货日程表传输时已创建的，然后客户的订单号通常已经加载，客户的订单号也会在订单行中看到。使用交货日程表类型的设置，你决定是否将客户的订单号仅已传输到订单行或两者转移到订单行和订单页眉。

#### 报价单号
如果客户订单是创建自报价创建的，则可以在此字段中你报价单号。你可以使用按钮链接/转到报价 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_link.png)。

#### 订单日期
此字段默认输入今天的日期，但可以已变更。默认下，行的日期与页眉中的订单日期相同。

#### 电子数据交换
点击 电子数据交换 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 你可以看到有问题的EDI 信息。
在里面 EDI 已连接 它说的字段 是的 如果订单上的客户已连接到 EDI，否则它将阅读 否。默认值是从客户加载的。当客户连接到 EDI 时，可以使用 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 字段下一个的按钮可查看应用于该客户的EDI 事务类型和方向。
如果客户连接到EDI，则可以通过EDI发送订单确认单。这是通过使用 通过 EDI 发送 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_send_edi.png) 该命令然后可在程序工具栏上可用。默认打印订单确认单在​ 打印客户订单 程序。当已发送订单确认单时，它是根据与客户已链接的EDI 行为来完成的。这可以在程序 管理 EDI 事务。
如果客户已连接到 EDI，你可以使用 排除自 EDI 设置决定是否应将相关订单排除在 EDI 流之外。这意味着订单确认单无法通过 EDI已发送，不从这里发送，与非能从 打印客户订单 程序。这 通过 EDI 发送 按钮然后将被未激活。
你还可以看到 EDI 导出状态 显示订单的导出日期和时间。
