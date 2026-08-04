### EIM 设置
这里周三描述了在你现金折扣之前你配置的不同设置 Monitor ERP。
用户
在此程序中，你为使用 EIM 的用户配置有关不同用户权限的设置。

#### 角色 / 用户权限标签页
系统被用于不同角色的 EIM 有预定义的用户权限，例如角色 财务经理 和 买家。在盒子里 生成的用户权限 你角色已添加到用户之后，你将看到该角色被用于的全部用户权限。大多数案件下，EIM用户可用的角色就足够了，但在某些案件下，你还需要为这些用户配置唯一的用户权限。对于 EIM，你在以下部分中配置设置： 扫描供应商发票， 英美烟草公司， 和 EIM 文档 在盒子里 特定用户权限。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMUsersRolesRights.png)](../../../../Resources/Images/TrainingMaterial/EIMUsersRolesRights.png)
在上面的例如中，具有以下角色的用户 财务助理 还被授予更改已审核行的许可，然后显示在框中 生成的用户权限。
系统设置
你设置仅激活系统 在过账行上使用扩展审核 如果你希望能够输入谁应该在费用发票的过账行层级上复核/审核发票。此设置还确定费用发票和物料发票（订单发票）的两者首席审核人。通过科目和维度的设置，你可以确定谁应该根据过账审核每个过账行。这应用至具有 EIM 和EIM 工作流的系统。
通过系统设置 激活EFH 工作流程 你可以激活EFH工作流选项。当你采购EFH Workflow 时，系统设置默认处于激活由。
审核设置 - EIM
在此程序中，你可以设置供应商发票的审核进行设置。

#### 审核人选项标签页
添加应审核供应商发票的用户。补充设置 审核限制， 发票审核的缺勤， 提醒， 转发审核， 和 查看发票文档的用户权限。最终设置也可以在 英美烟草公司 按钮 用户 程序。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMSigners.png)](../../../../Resources/Images/TrainingMaterial/EIMSigners.png)

#### 审核人组标签页
如果需要，创建审核人组。在审核人组中，只要一包含审核人审核发票，然后即可继续流通。这与审核列表不同，授权列表要求列表中的全部审核人都审核发票。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMSignerGroups.png)](../../../../Resources/Images/TrainingMaterial/EIMSignerGroups.png)

#### 审核列表标签页
如果需要，创建审核组。审核列表是一份审核人的列表，发票必须经过列表上全部审核人的审核由之前已最终记录。与审核人组不同的是，当发票被已发送到审核列表时，它需要按照列表的订单得到全部审核人的审核由。
审核列表可以有 会签。如果你激活此设置，发票将时间发送给全部审核人送至审核，也就是说，发票不按照特定的订单进行已审核。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMAuthorizationLists.png)](../../../../Resources/Images/TrainingMaterial/EIMAuthorizationLists.png)

#### 审核限制例外标签页
如果需要，可从审核限制中创建例外。这些例外可能基于供应商分类、供应商组或供应商。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMAuthorizationLimitExceptions.png)](../../../../Resources/Images/TrainingMaterial/EIMAuthorizationLimitExceptions.png)

#### 维度标签页
如果你行层级应用审核（通过系统设置已激活，称为 在过账行上使用扩展审核，此标签页将可用。你在此处每维度代码配置审核人 / 批准者和首席审核人。对于项目，你可以从项目登记中选择项目经理或我方联系人作为审核人 / 批准者和首席审核人。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMPostingDimensions.png)

#### 行审核的优先级标签页
如果你行层级应用审核（通过系统设置已激活，称为 在过账行上使用扩展审核，此标签页将可用。在这里，你输入有关优先级的核心规则，如果多个员工负责人同一过账行，那么该规则将确定谁应该是该行的审核人/首席审核人。例如，科目的审核人比成本中心的审核人更多重量。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMPriorityRowAuthorization.png)

#### 标签页查看发票的用户权限
创建用于查看发票的创建用户权限组，并为每组配置应显示与非显示哪些发票的条款。如果需要的然后，审核人可以链接至用户权限组。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMUserRightViewInvoices.png)](../../../../Resources/Images/TrainingMaterial/EIMUserRightViewInvoices.png)

#### 日程计划标签页
激活两个服务 转发审核 和 通过 Email 提醒 日程表在​ 设置 框，这将决定服务何时运行。使用 运行 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 你也可以人工的运行服务。还可以在框中进行设置 通过 Email 提醒设置 对于服务 通过 Email 提醒。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMScheduling.png)](../../../../Resources/Images/TrainingMaterial/EIMScheduling.png)
收取 Email 设置
在此程序中，你可以添加与 Exchange 或 IMAPEmail服务器绑定的Email科目，并选择类型 Monitor - to - Monitor 对于相关科目。目的是将传入的Monitor - to - MonitorEmail发票直接放入 EIM工作流程中。使用按钮 校验选择的地址 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 你可以测试科目设置是否正确。如果正确，最左边的列中会显示一个绿色检查标记。如果信息输入不正确，则会出现黄色警告符号 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/warning.png) 将会显示。收到的Monitor - to - MonitorEmail发票然后自动放置在收件箱 收件箱 Monitor - to - Monitor 在里面 登记供应商发票 程序。此收件箱也可作为桌面部件（见下文）。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMSettingsIncomingEmail.png)](../../../../Resources/Images/TrainingMaterial/EIMSettingsIncomingEmail.png)
扫描供应商发票
在此程序中，你可以进行有关供应商发票扫描的设置。这些设置位于 Monitor ERP 在安装扫描仪的计算机上已配置。你还可以使用该程序扫描新建的纸质发票。
> 在高级选项扫描仪上，有一个显示屏，你可以在其中选择如何/在何处保存文件。如果你有这样的扫描仪，你可以在扫描仪上选择将文件保存在你已配置为收件箱的文件夹中，如下低于。然后你不使用该程序 扫描供应商发票 扫描时。

#### 扫描标签页
配置扫描仪的设置，并在收件箱中选择路径 设置 box必须输入路径 PDF收件箱 在下下一个标签页下。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMScannerSettings.png)](../../../../Resources/Images/TrainingMaterial/EIMScannerSettings.png)

#### 收件箱路径的标签页路径
在名为 PDF收件箱 在此标签页下，你至少登记一文件夹的路径，该文件夹将成为扫描纸质发票的PDF 收件箱。这是扫描时PDF文件已保存的位置。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMInbox.png)](../../../../Resources/Images/TrainingMaterial/EIMInbox.png)
> 如果 EIM 的其它用户需要访问收件箱中的扫描发票，则在登记程序中 登记供应商发票，然后该路径应指向网络中计算机上的共享文件夹。其它用户必须有许可 修改 在 Windows 中查找该文件夹。

#### 附件类型标签页
登记你需要的附件类型，附加 发票 被用于在系统中。附件类型是可已添加到扫描发票的其它类型文档的标签，例如交货单、采购订单、差旅费投诉等。使用按钮将此类文档已增加到发票时 添加文档 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add.png) 在发票查看窗口中，然后你选择此处已创建的附件类型一。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMAttachmentTypes.png)](../../../../Resources/Images/TrainingMaterial/EIMAttachmentTypes.png)
供应商登记

#### 设置标签页
选择默认 审核人代码 每供应商。你可以选择的审核人代码是程序中已登记的审核人和审核列表 审核设置 - EIM。已选择的审核人或审核列表然后默认到审核相关供应商的发票。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMSignerCodeSupplierRegister.png)](../../../../Resources/Images/TrainingMaterial/EIMSignerCodeSupplierRegister.png)
会计科目表
如果你层级行应用过账（通过系统设置已激活，称为 在过账行上使用扩展审核，你五月必须输入审核人 / 批准者和科目首席审核人。
后台

#### 桌面
全部审核人用户都可以添加部件 任务 - EIM 和 收件箱 Monitor - to - Monitor， 和 电子发票 / XML收件箱 在他们的桌面配置中。另一种方法是管理员将这些部件添加到桌面模板中，然后审核人可以使用它。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMDesktopBackstage.png)](../../../../Resources/Images/TrainingMaterial/EIMDesktopBackstage.png)
在您的桌面上安装这三个部件将使您更容易MONITOR与供应商发票相关的活动，并且你还可以轻松地登记/预估记录发票。
你可以双击桌面上的某个任务，这将带你进入 任务 你就能 完成已分配给你 的任务了 .
你可以双击收件箱中的发票，这将带你到 登记供应商发票 加载发票后，登记/预估记录发票。
部件名为 电子发票 / XML收件箱 显示已已收到的电子发票/XML文件。该部件扫描在收件箱路径下已登记的XML收件箱，查找 扫描供应商发票 程序。如果你已已收到发票，你开始导入 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_import.png) 或双击该行。你可以通过点击人工的从运营商服务器开始下载 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_refresh.png)。点击 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_preview.png) 订单预览PDF发票。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/EIMDesktop.png)](../../../../Resources/Images/TrainingMaterial/EIMDesktop.png)
