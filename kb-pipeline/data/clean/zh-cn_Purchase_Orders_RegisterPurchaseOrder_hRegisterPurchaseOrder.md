### 页眉行

#### 订单号
在此字段中，您可以输入新的订单号或使用查找功能加载现有的订单号。订单号为字母数字，最多可包含15个字符。
如果您没有输入订单号，则系统将在保存订单时从编号序列中分配一个新的订单号。如果您手动输入订单编号，系统将检查输入的编号是否已经存在，在这种情况下，它将加载现有订单。
新记录通过该字段中显示的绿点![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/green_dot.png)进行突出显示。首次保存记录后，该点将消失。
如果订单号与案件相关联，则按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridConnectImage.png) 字段下一个的将可用。通过使用此按钮，你可以在 登记案件 程序。

#### 订单类型
你可以在此字段中看到采购订单的类型。你在您的用户科目中设置的默认订单类型将在此默认已建议。如果你不在此处已配置默认订单类型，然后系统将已建议你在最近的订单中使用的订单类型。当需要时，可以选择其他订单类型。
系统已交货时附带订单类型 采购物料。你需要的其它订单类型必须第一个在 订单类型 程序。此处输入的订单类型决定了过账组、汇率类型、优先级，以及该订单是否应被用于在采购统计中。使用按钮 变更订单类型 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_change_record.png) 你还可以更改现有的订单的订单类型。当你更改订单类型时，也可以更新前缀。你仅更新状态低于 2 且不有时间高于该状态的订单的前缀。
还有一种订单类型叫做 外协 随系统已交货的分包采购订单，但外协采购订单仅由系统基于已登记的工单自动已创建。
如果采购订单是退回订单，你将在此处看到订单类型 退回订单。如果仓储费用，则无法在字段中不可改变订单类型。你创建在 登记退回订单 程序。

#### 状态
你可以在这里看到以符号表示的采购订单状态。工具提示以文本形式显示状态。

#### 供应商
在这里你从供应商登记中选择一个供应商。采购订单强制的指定供应商。第一个时间你该程序打开，此字段为空。下一个你时间程序时间，你将看到最后你的供应商号。当你已选择了供应商号后，供应商名称将显示在到右边。使用按钮 变更供应商 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_change_record.png)，你还可以变更供应商现有的订单的供应商。
如果供应商已被冻结登记，则会出现一条消息，你可以通过使用按钮查看原因 显示冻结原因 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/RedPadlock.png)。在这种案件下，不为供应商创建订单。如果你为供应商已选择了通知（冻结 / 通知），你将通过按钮看到消息/通知 显示消息 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_comment.png)。在这种案件下，仍然可以为供应商创建订单。

#### 供应商的订单号
你可以在此字段中输入供应商的订单号。如果订单状态为 1 (已登记的) 或 2 (已打印）当你在此字段中输入供应商的订单号时， 已确认的 复选框被自动选中。此复选框与订单状态链接至，显示供应商已已确认采购订单。

#### 询价单号
如果订单是创建自询价创建的，你可以在这里看到询价单号。

#### 电子数据交换
点击 电子数据交换 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 你可以看到有问题的EDI 信息。
在里面 EDI 已连接 它说的字段 是的 如果订单上的供应商已连接到 EDI，否则它将阅读 否。默认值从供应商处加载。当供应商连接到 EDI 时，可以使用 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 字段下一个的按钮可查看应用于该供应商的EDI 事务类型和方向。
如果供应商连接到EDI，则可以通过EDI发送订单。这是通过使用 通过 EDI 发送 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_send_edi.png) 该命令然后可在程序工具栏上可用。默认打印发送在​ 打印采购订单 程序。当订单被已发送时，它是根据与供应商已链接的EDI 行为进行的。这可以在程序 管理 EDI 事务。
如果供应商已连接到 EDI，你可以使用 排除自 EDI 设置决定是否应将相关订单排除在 EDI 流之外。这意味着订单无法通过 EDI已发送，不从这里发送，与非能从 打印采购订单 程序。这 通过 EDI 发送 按钮然后将被未激活。
你还可以看到 EDI 导出状态 显示订单的导出日期和时间。
