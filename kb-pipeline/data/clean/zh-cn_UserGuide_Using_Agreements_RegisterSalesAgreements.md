### 登记客户协议
在里面 登记客户协议 程序,你登记新建 的协议并修改现有的协议.例如，与客户订单不同，协议从不结果库存事务。协议的目的是用来发票，例如，按照固定的开票间隔开具服务。
当你登记协议并且该协议获得状态 3（激活），基于已配置的设置和协议上的行已创建协议底单。
要创建发票底单，你必须释放协议底单。
> 已已释放的协议底单将被已冻结从对协议进行全部变更。也就是说，如果你对协议进行变更，这仅影响/更新不已释放的协议底单。时间你点击时，这些协议底单都会已更新 保存。
标签页页眉

#### 通用的
在通用章节，你配置应用于协议的期间和日期数。例如，协议有效在中间日期数，协议签署的时间，以及通知期有多长等等。
你还可以在此处查看协议的状态。仅当协议达到状态 3（激活） 将基于此标签页下的设置以及协议上已登记的行基于已创建协议底单。
如果你激活 自动更新状态 设置，协议的状态将从状态已更新 2 (签名 / 生效) 到状态 3（激活） 当。。。的时候 有效自 日期发生。协议将以同样的方式变更为状态 6 (已关闭) 当日期进入 有效至 已经过去了。
如果你已已暂停在协议预付开票期间已激活VAT，则重要
开票时，使用已暂停VAT的VAT账号，以及预估计提科目的标准科目。
付款时，已暂停的VAT已传输销销项 VAT科目，并将净额根据协议已传输计提科目。
如果 VAT 报告底单载入自 系统设置已设置为 总账事务 VAT 代码，适用以下规定：支付预付发票时，在已付款预付款的过账行中输入VAT 代码。VAT编码是从正在已付款的发票中加载的。当VAT会计通过总账事务中的VAT 代码加载VAT 报告的基础连接，这结果正确的营业额会计。
如果系统设置设为载入 会计科目表 VAT 代码，当你不考虑事务的VAT 代码时，将根据科目的设置使用VAT 代码。订单不创建VAT会计差异，已付款预付款科目与应缴纳VAT的营业额的VAT行链接至。

#### 开票
在开票时，你可以决定如何以及多久为协议已开票。重要保持的是，开票间隔决定了协议行上使用何种价格类型。例如，如果你已选择了 每年 选项为开票间隔，这表示协议行上的价格将被视为年度价格。
价格定义
如果你已经在组件登记中输入了年度价格，并你每月发票，你使用 价格定义。在输入你协议行上已登记的价格类型。这样就可以区分年度价格并每月发票。例如，如果某组件的年度价格为 12,000 欧元，你可以通过配置 价格定义 到 年度的，以及 开票间隔 到 每月，每月向客户开具 1000 欧元的发票。
当月发票
确定当前月份是否也已开票。
自动释放协议底单
订单避免手工管理释放你已登记的全部协议的协议底单，你可以使用功能 自动释放协议底单。此功能将根据输入的日期释放发票底单 计划开票日期。此设置的默认值由 订单类型 程序。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/Agreement2.png)](../../../../Resources/Images/UserGuide/Agreement2.png)
客户订单
正如前面提到的，库存事务否基于协议。但可以将协议与客户订单链接/连接。这是在 客户订单 盒子。你仅链接与协议具有相同客户的订单。当协议和客户订单已链接/连接时，你可以在分组 / 过账下看到协议编号 登记客户订单 程序。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/Agreement3.png)
行标签页
在“行”标签页下，你可以添加应被用于在协议中的组件（服务）。如果你在协议中使用价格定义，你将看到根据价格的 开票间隔。这体现在 价格/发票间隔 列。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/Agreement4.png)](../../../../Resources/Images/UserGuide/Agreement4.png)
一次性成本
如果你仅对某项成本发票一时间，你在行标记这是一次性成本。这是通过 一次性成本 按钮。输入该行是否应与协议中的其它行一起已开票，或者是否应已创建新协议基础（即，应单独已开票）。如果你选择单独为该行发票，你可以自由输入 计划开票日期。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/Agreement5.png)
与页眉标签页下的通用章节中的方法相同，你可以每行输入一个 有效自 和一个 有效至。例如，如果你希望仅协议期间的某一特定期间开具特定行的发票，这将非常有用。你在此处输入的日期数将决定在哪个协议底单上包含协议行。
向上调整行
案件协议是预付已开票的，并且在已已开票的期间内已变更协议，然后你可以为客户单独开具产生的附加成本发票（或将其放在下一个一张发票上）。这是在所谓的 向上调整。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/Agreement6.png)](../../../../Resources/Images/UserGuide/Agreement6.png)
有两种方法可以触发器 向上调整。或者直接行上修改影响行总数的内容，例如更改数量、价格或折扣。
你还可以触发器 向上调整 通过输入 未来数量， 未来价格和/或 未来折扣，从已已开票的期间开始适用。
在低于的例如中，截至日期 ，价格从年12,000 欧元上涨至年15,000 欧元。由于 2022-05-01 至 2022-05-31期间已已开票，因此已建议将 2022-05-19 至 2022-05-31为此期间的调整的125 欧元/月。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/Agreement7.png)
如果你将光标放在该行的按钮上，你将看到建议上调金额。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/Agreement8.png)](../../../../Resources/Images/UserGuide/Agreement8.png)
要创建向上调整，你单击加号按钮。然后，在协议上会已创建一个新行，其中包含已建议调整的金额，以及一个链接文字行，你可以在其中看到该行所指的期间。已创建的行是 一次性成本，即仅开具一次已开票。其它不已释放的协议底单，将根据变更进行已调整。
你成本隐藏 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusInvoice.png) 功能菜单上的按钮。
协议底单标签页
在“协议底单”标签页下，你查询为相关协议已创建的全部协议底单。当存在协议底单时，此标签页可用。这些是创建人监控服务创建的，该服务每晚在MONITOR服务器上运行，并为已获得状态的协议创建协议底单 3（激活） 并有协议行。协议底单仅针对未来 12 个月生成。这意味着，如果协议跨越 12 个月多于，你最初仅看到未来 12 个月的发票底单。该系统确保未来 12 个月总是有基础。
在此标签页下你可以 释放协议底单 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_release.png)。直到协议底单已释放后，不已创建发票底单。如前所述，已释放的协议底单不协议变更的影响。
如果你错误地已释放了基础，你可以 撤销协议底单的释放 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_undo_release.png)。
已已开票的协议底单不被撤销。在这种案件下，你必须第一个发票贷项贷方。这可以通过 贷项发票 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/addCreditImage.png)。在下面 贷项发票 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/addCreditImage.png) 按钮有两个选项， 贷记后重新开票 和 贷记后开票完成。全部在背景已创建的基础和客户订单信息都已加载。
- 贷记后重新开票 将协议底单的状态回溯 为已登记, 并且贷项之后可以一次已释放该 基础 .这意味着当你根据协议底单记入贷项时，将一次向客户已开票。
- 贷记后开票完成 贷项之后，按协议底单保留已已开票状态。当你应用贷项之后不向客户已开票时使用此方法。
使用 暂停 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusOpPaused.png) 按钮来暂停协议底单，并且否可能释放协议底单。如果你不想协议底单已开票，这将很有用。这意味着，如果你否已释放 自动释放协议底单 设置。当协议底单被已暂停时，将无法人工的已释放。
使用 恢复 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 按钮一次释放被已暂停的协议底单。这 恢复 按钮用于更改协议底单的状态从 已暂停 到 已登记的。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/Agreement9.png)](../../../../Resources/Images/UserGuide/Agreement9.png)
在下面 行信息 你会看到协议底单中存在的全部行，这些行又将包含在发票底单中。
