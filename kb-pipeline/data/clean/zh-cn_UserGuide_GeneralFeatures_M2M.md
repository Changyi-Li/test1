### Monitor - to - Monitor
Monitor - to - Monitor （M2M）旨在促进客户和供应商在中间的通信，使用 Monitor ERP或MONITORG4。今天在 Monitor -to-Monitor 支持的不同业务措施根据图表所示：
| 客户行动 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_email.png) | 供应商的行动 |
|---|---|---|
| 发送采购订单 发送交货日程表 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/arrow_right.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/arrow_right.png) | 客户订单已创建 已已创建销售预测 |
| 采购订单已已确认 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/arrow_left.png) | 发送订单确认单 |
| 采购订单已已报告发货通知 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/arrow_left.png) | 发送货运通知 |
| 供应商发票已已创建 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/arrow_left.png) | 发送客户发票 |
| 发送案件/供应商不合格品 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/arrow_right.png) | 已创建案件/客户不合格品 |
| 已创建案件/供应商不合格品 | ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/arrow_left.png) | 发送案件/客户不合格品 |
例如，如果客户通过MONITOR通过Email发送采购订单，消息订单两者PDF 和 XML 格式附加在Email中。在Email中，有信息表明该Email是Monitor - to - Monitor的消息，以及附件 – 在本案件中消息采购订单。然后，创建供应商使用客户订单Email在其 Monitor ERP 系统。它是用于创建客户订单的附加 XML文件。然后，供应商通过Email发送订单确认单，客户使用该Email确认采购订单。供应商交付客户订单，然后五月发送一封带有货运通知的Email。然后，客户使用该Email报告采购订单的报告发货通知。然后，供应商通过Email将客户发票发送给客户。然后，客户使用该Email创建供应商发票 Monitor ERP。
如果客户需要对已已发送的采购订单进行变更，则可以通过Email再次已发送该订单作为已修改采购订单。然后，供应商使用该Email来更新其现有的订单或创建新客户订单。如果供应商选择更新客户订单，则在导入XML文件时会进行不同的检查。第一个检查以确保客户订单的状态不高于 4（正在拣货）。如果客户订单已经已部分交货或已经最终交货，然后不基于已变更的采购订单更新客户订单。然后供应商必须创建新客户订单。下一个检查的是客户订单行。这将检查任何订单行是否有已链接工单或采购订单。如果某一行有已链接订单，然后就不更新该行。然后供应商可以选择仅更新没有订单链接的更新订单行，或者选择创建新客户订单。
如果创建自协议创建了客户发票，则 XML文件被用于协议编号的相关信息。
Email 设置
Monitor ERP 如果已在电子邮件管理控制台中已添加了公司Email服务器和Email 账户的设置，则可以MONITOR用户的Email 收取 Email 设置 程序。对于接收Monitor - to - MonitorEmail的Email 账户，设置 Monitor - to - Monitor 必须检查 类型。点击 可用的 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 你可以确定这些Email 账户对哪些用户、组和角色可用。默认下，这是针对全部用户的设置。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/settings_incoming_email_m2m.png)](../../../Resources/Images/UserGuide/settings_incoming_email_m2m.png)
在里面 用户 程序，你可以看到Email 账户 Monitor - to - Monitor 已已激活 类型 在上面程序中，并将其已配置为可用于用户使用。默认下，每个Email科目的Email均已已激活以进行显示（在桌面部件中 收件箱 Monitor - to - Monitor）。对于每个Email科目，你可以决定 类型 系统应该为用户MONITOR的Monitor - to - Monitor的Email。目前全部可用的类型均已默认激活由。这些是：客户订单、发票、采购订单、案件和销售预测。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/user_settings_m2m.png)](../../../Resources/Images/UserGuide/user_settings_m2m.png)
当任何这些Email 账户收到由任何类型的Monitor - to - MonitorEmail时，该Email将自动已导入并显示在桌面部件中 收件箱 Monitor - to - Monitor。用户两者查看EmailEmail科目的Email已激活并类型在 用户 程序，就能在桌面部件中看到该Email。
如果同一供应商/客户有多个订单/发票，消息你配置为在每消息Email中附加一订单/发票，或将所有订单/发票附加在一封Email中。这是由系统系统设置通用的 在同一个 Email 中发送多个订单 （采购）和 在同一个 Email 中发送多个订单 / 发票 （销售）。这些设置可以设置为 是的 或者 否。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/system_setting_p_m2m.png)](../../../Resources/Images/UserGuide/system_setting_p_m2m.png)
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/system_setting_s_m2m.png)
还可以针对供应商（作为采购订单的接收者的）和客户（作为订单确认单和/或发票的接收者的）的每Email 地址进行专门已配置。在这种案件下，这些设置将覆盖上面提到的通用系统设置。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/email_settings_supplier_m2m.png)](../../../Resources/Images/UserGuide/email_settings_supplier_m2m.png)
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/email_settings_customer_m2m.png)](../../../Resources/Images/UserGuide/email_settings_customer_m2m.png)
收件箱 Monitor - to - Monitor
该桌面部件是一个收件箱，你可以在其中查看有关已到达的Monitor - to - MonitorEmail的信息。在 这里 ,你可以 看到消息的类型,状态,消息已收到时间,发件人名称,公司,消息主题以及来源.如果Email是通过 Monitor 的监控到达的，你将看到发件人的Email 地址作为来源。用户还可以通过将Email直接从其Email程序拖放到收件箱来人工的载入Email。然后 手工的 将显示为来源。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/inbox_m2m.png)](../../../Resources/Images/UserGuide/inbox_m2m.png)
收件箱中有一个功能菜单，其中有一个按钮，你可以使用该按钮将附加的 XML文件从收件箱导入到相关程序中，处理中和登记。例如，如果Email包含采购订单的 XML文件，则 登记客户订单 程序将会打开，同时会打开一个用于导入客户订单的导入窗口，其中会显示有关 XML文件组成哪些类型的数据以及新客户订单将包含哪些内容的信息。也可以双击Email消息来开始导入。
例如，如果已收到的Email包含多个采购订单（客户已已配置为可以在消息Email中发送多于一采购订单），然后该Email将显示在收件箱中的多个行行（每订单一）。然后，你可以分别导入这些订单处理中并登记为客户订单。
功能菜单上还有按钮你用于更新收件箱、从收件箱中删除Email 消息以及显示Email的目录。
> 当用户将附加的 XML文件导入相关程序时，这意味着Email将被已锁定在收件箱中，并且挂锁 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Padlock.png) 显示为状态。此锁定可防止其它用户意外负荷相同的Email消息并从而在登记程序中创建复制。 如果 EIM 工作流 已安装并且 XML文件是供应商发票，则用于导入XML文件的按钮不可用。也不双击Email来导入发票。EIM 工作流将自动导入供应商发票 登记供应商发票 程序。
导入窗口
例如，如果客户不匹配，用户可以在导入窗口中视图和修改信息。可以已选择订单号、订单类型和客户。可以在客户登记中更新我们的供应商号 Monitor ERP 使用导入文件中的我方供应商号。你还可以选择订单的交货地址是否应根据 Monitor ERP，或者根据导入文件。
用户还可以客户信息 Monitor ERP 导入文件中包含客户信息。
用户可以选择应包含哪些订单行（或从交货日程表导入销售预测时的预测行）。还可以选择或不为订单行/预测行中的组件已更新/已创建客户链接。默认下，它被标记为在全部行上更新/创建客户链接，但这可以通过系统设置来决定 导入客户订单 (XML) 时更新 / 创建客户链接。
导入采购订单（订单确认单）时，案件组件供应商链接不存在，你可以创建供应商链接。导入采购订单（订单确认单）时，默认也会已导入文本行，但是你可以选择不已导入。案件已经已导入的采购订单需要重新进口的（订单确认单已发生变更），仅已添加或已修改订单行才会被标记为已导入。
用户可以查看订单行的信息，例如可以在已创建订单之前对某些信息进行调整。例如，在中间 Monitor ERP 和导入文件，这些差异将显示为警告 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/warning.png) 并在导入窗口中以文本显示原因。即使在订单已创建之后，这些警告仍然存在，然后显示在订单的校验窗口中，仓储费用也可以在那里进行更正。如果数据不存在或数据错误的，例如，在导入文件中不组件号 Monitor ERP，这将显示为错误 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/error.png)。然后，用户可以人工的选择订单行的正确组件，或者选择不包括该订单行。
如果你在导入文件中导入的订单是已修改采购订单，并且用户选择更新其现有的客户订单，然后订单页眉将会已更新，并且全部没有订单链接的订单行将被已导入订单中的行替换。有关此信息也将显示在导入窗口中。第一个还会检查是否有多于一客户订单具有相同的“客户的订单号”。在这种案件下，用户可以在导入窗口中选择要更新哪个客户订单。
在导入窗口中还有一个PDF阅读器，使用户可以视图导入文件中订单的图片（在低于的例如中，这是采购订单）。这是用于的附加 PDF文件。Email中附加的任何其它PDF文件（如果有）也可以显示，例如图纸。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/import_window_m2m.png)](../../../Resources/Images/UserGuide/import_window_m2m.png)
> 通过使用系统设置 在采购订单确认 (M2M) 的文本行上预选“包括” 你可以决定在导入期间是否默认包含文本行。你可以在中间 是的， 否， 和 仅新行。
创建时间用户在导入窗口已关闭之后按照程序保存时，订单就被创建了。然后Email被记录并显示在 活动 订单上的标签页。从那里，用户还可以打开Email并查看全部目录。
通过 Monitor-till-Monitor导入包含合金成本行的客户订单

#### 导入包含合金成本的订单文件，该合金成本来自 Monitor ERP
在创建自的文件中 Monitor ERP，合金成本行具有与作为组件行相同的行类型。这意味着，在Monitor - to - Monitor导入对话框中，合金成本行看起来像一个正常的组件行，并且 包括 复选框将默认质检由。然而，即使已选择导入合金成本行，只要它与订单上现有的合金成本行相匹配，它就从不不会被全部已导入到订单行中。匹配的合金成本行仅已导入到特别表格中，该表用于将匹配订单行与已导入的行进行比较，并通过警告指示差异 登记客户订单。如果订单上有现有的且匹配的合金成本行，则这些将 从不 从导入文件中进行已更新。附加，重要的是要知道客户订单上的盟友成本行 从不 可以创建自导入文件创建，只要它们与订单上现有的合金成本行匹配。仅当已选择了要导入的行并且执行 不 匹配现有的合金成本行，文件中的合金成本行被已导入，并创建订单行。在其它案件下，采购订单上的合金成本行仅在 Monitor ERP。（行在 Monitor ERP 取决于合金成本行设置 客户登记）。
通过 Monitor-till-Monitor导入供应商发票时查询右边的供应商
在某些情况下，由于同一供应商号可以在多于供应商中找到，因此无法自动找到供应商 我方客户号 字段，系统将继续搜索，即使在字段 企业 ID 号， VAT 登记号， 银行转账编号， PlusGiro编号 和 银行账号。
> 用户还可以人工的导入订单、发票或案件，而无需上面已配置Monitor - to - Monitor的Email 设置。在这种案件下，用户仅添加桌面部件 收件箱 Monitor - to - Monitor，然后可以将Email或仅附加的 XML文件拖放到收件箱中。Monitor ERP 分析 XML文件的类型，打开相关程序并加载订单、发票或案件。
