### 利息开票
以下主题描述了利息开票的工作原理 Monitor ERP 以及在公司开始应用利息开票之前你配置哪些设置。

#### 设置
你需要复核编号与利息开票相关的不同系统设置。你查询在 Interest invoice 标题下 销售 标签页卡中的 系统设置 程序。一些设置有默认值。请阅读该程序的在线帮助功能中这些系统设置的描述。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InterestInvoicingSystemSettings.png)
> 该章节中的最后系统设置称为 利息发票的服务组件。它要求你第一个创建以下内容来控制过账和VAT： 创建一个利息产品组（例如，调用“利息”），然后为全部客户组选择罚息销售科目8313（在瑞典）。这是根据 产品组 和 销售科目 标签页卡中的 过账矩阵 程序。为全部客户组的产品组选择VAT 代码4（免征 VAT）。这是根据 每产品组例外 标签页卡中的 VAT设置 程序。创建组件 服务 类型（例如，调用为“利息”）并选择 未指定 作为 服务类型。将你之前已创建的产品组分配给该组件。这是在 组件登记 程序。最后，在上面提到的系统设置中选择此服务组件。

#### 客户登记
对于上面提到的一些系统设置，可以每客户做出例外。你查询在Exceptions 框下 设置 标签页卡中的 客户登记 程序。如果此处的设置为空（否已选择任何选项），则表示应用系统设置。但是如果你输入/选择一个设置，则在向该客户开具利息开票时，这将覆盖相应的系统设置。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InterestInvoicingCustomerSettings.png)

#### 文档设置
对于利息发票，有一个文档模板 利息发票 在里面 文档设置 程序。你需要复核此文档模板的设置。有关这些设置的阅读更多 Settings 话题。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InterestInvoicingDocumentSettings.png)](../../../../Resources/Images/TrainingMaterial/InterestInvoicingDocumentSettings.png)

#### 收款的利息费用
你可以自动接收系统的建议 收款 程序，向客户收取利息应使用 利息发票 或应在 后续常规发票因付款太迟导致。为此，需要为相关客户已选择这两种利息费用方法中的一。
系统检查应收账款记录是否已选择了任何一种利息费用方法（从客户设置中加载）。然后系统设置 利息宽限期， 免息天数， 和 每张发票利息费用最小金额 将确定是否应根据两种方法中的任一种已建议利息费用。否则 不收取 将被已建议。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InterestInvoicingIncomingPayments.png)](../../../../Resources/Images/TrainingMaterial/InterestInvoicingIncomingPayments.png)
> 使用侧面板 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_sidebar.png) 你可以快速轻松地转到订单积压和发票底单，订单查看是否有未来的发票正在处理中。

#### 利息费用底单
在此程序中有一个列表，你可以在其中查看哪些发票的付款记录已已付款太迟并且正在待产利息费用。你可以使用本程序来创建利息费用的基础或取消选择你不创建利息发票的发票。在列表中，还可以选择如何费用利息（与 收款 程序）。
请注意！该列表每付款记录显示。也就是说，如果你有一张部分付款的发票，然后发票上的每个付款记录都会在列表中显示为单独的行。
在此程序中，你使用按钮通过利息发票释放利息费用的付款记录 释放利息发票 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 在工具栏上。这付款记录 包括 复选框已标记，并且 利息发票 已选择方式 利息费用 在列表中。只有当付款记录两者满足这两个条件时，释放按钮仅激活。已选择在 利息费用 列表中的列将发生以下情况：
- 利息发票 – 这意味着利息是在传统的利息发票上收取的。当你使用列表中的释放按钮时，发票底单类型 利息发票 将被已创建（每客户/货币一基础）。出现一个控制问题，询问你是否要释放发票未开票。如果你点击 OK 在控制问题中，程序 复审 / 批准发票 将打开。你可以在那里复核并批准利息发票。时间这些付款记录也会从列表上消失。如果你点击 取消，释放将会已停止，并且你将被返回到列表。
- 后续常规发票 – 这意味着利息费用将被已添加到下一份向客户的后续常规发票中。当你通过利息发票释放利息费用列表中的其它付款记录时，这些付款记录时间发生没有。它们将一直保留在列表中，直到下次向相关客户开具后续常规发票时间。当向客户已批准常规的发票然后， 复审 / 批准发票 程序,你可以 将利息添加到发票底单中 .
- 不收取 – 这意味着不收取应计利息。如果你已选择此选项作为客户默认使用由或为付款你此已选择，然后付款记录将不被用于在列表中。但是，如果你在设置待包含费用在程序中的选项，那么你也可以显示该付款 不收取。例如，你可能已变更主意，现在想费用利息。
使用设置 订单类型, 利息发票 你可以在程序中决定已创建利息发票时应使用哪种订单类型。
设置名为 下一个发票等待时间, 警告后： （天数）在程序中，你可以配置你在输入的天数之后在列表中看到警告。这样做是订单查询等待下一个一张发票很时间的利息费用。已超出天数的付款记录将显示付款日期 红色的 列表中的文本。这指示器这些发票可能会已变更使用利息发票来收费。
在里面 哦 列表中的列，如果有储备订单或未为相关客户未开票发票底单，则选中该复选框。这很帮助了解是否有未来的发票，并且这些信息可以帮助你决定或不应对这些发票收取利息。

#### 复审 / 批准发票
开票利息发票
利息发票你在 利息费用底单 程序然后将打开此程序，你可以在其中复核和批准未开票的利息发票发票，你也可以打印它们。尽管你会自动被已发送该程序进行复核和批准，但你不时间就这么做。可以关闭该程序并在其他场合打开它来执行此操作。利息发票将与其它发票一起保留以供复核和批准。这体现在 发票类型 列中写着 利息 这些发票。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InterestInvoicingApproveInvoice.png)
在下后续常规发票上收取利息
如果客户下后续常规发票需要费用利息，则在程序中会显示按钮 添加利息 可用顶部 结果 盒子。仅当客户下下一个发票的货币与要费用的利息相同时，此按钮才可可用。然后，你可以单击按钮打开一个窗口，你可以在其中为客户的常规的发票底单添加利息。显示客户的合计利息金额。如果特定客户还存在通过利息发票费用的利息，则对话框窗口中会显示警告。这指示器你可能想要取消对话窗口并更改这些利息项目的利息费用方式，仓储费用在常规的发票上收取利息。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/InterestInvoicingAddInterestNextRegularInvoice.png)](../../../../Resources/Images/TrainingMaterial/InterestInvoicingAddInterestNextRegularInvoice.png)
你​​ OK 按钮，这意味着将根据客户的第一个张发票底单（使用你之前已创建的服务组件）使用一或多个组件行已添加利息。组件行下方显示发票号，发票金额，到期日，付款日期和利息天数编号等信息。在下面 预览 如果你重载利息基础，你标签页看到利息行。（这是通过单击另一个基础，然后你标记第一个基础来完成的 结果 盒子）。在那个框里有一个信息符号 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_information.png) 也显示在已开发票的到右边。该符号的工具提示会让你知道已已添加利息，并且该利息属于应在下一张后续常规发票上收取的类型。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/interestInvoicingInterestNextRegularInvoiceAdded.png)](../../../../Resources/Images/TrainingMaterial/interestInvoicingInterestNextRegularInvoiceAdded.png)

#### 贷项利息发票
如果你通过以下程序创建利息发票 直接登记发票 （当从应收账款列表链接时）你已允许贷项利息发票。你可以选择要记入贷项的行。然而，不对涉及利息发票的行进行价格批准。

#### 过账/记录利息发票
集成设置和日记帐也应用至利息发票，其方式与客户发票相同。也就是说，利息发票在客户开票日记账/取消日记账中处理，也可以通过与会计直接集成来已记录。

#### 更新应收账款分类账
如果利息不已开票或未已释放未开票，然后在此程序中更改借项发票的利息费用方式。也就是说，在下后续常规发票上使用利息发票收取利息，或不收取利息。你还可以在此程序中创建利息发票类型的新建应收账款记录。

#### 发票日志
你还可以在发票日志中查看利息发票。

#### 撤销释放利息发票的发放
如果你错误地已释放了利息发票（不已开票），然后你可以使用 撤销交货报告 执行撤销这些操作的程序。然后这些发票将再次成为列表中的基础 利息费用底单 程序。
