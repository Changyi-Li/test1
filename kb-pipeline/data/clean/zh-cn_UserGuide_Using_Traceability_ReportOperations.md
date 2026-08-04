### 报告工序

#### 批次层级可追溯性
当你报告一项具有可追溯物料的工序时，可追溯物料在正常案件下不自动从库位余额中已扣减。不过，这已激活通过 允许自动领用 在组件登记中设置.如果可追溯物料不已报告，报告你工序的组件计划数量时将显示警告。该警告提醒人们应尽快已报告可追溯物料。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/BatchReportOperation1.png)](../../../../Resources/Images/TrainingMaterial/BatchReportOperation1.png)
只要可追溯物料有剩余，则已链接有可追溯物料的工序就不能被已报告为已完成。然后就会出现一条错误消息。这是因为必须已报告可追溯物料订单确保可追溯性。必须已报告已消耗的可追溯物料，仓储费用剩余物料的体积零 (0)，之前才能已报告该工序已已完成。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/BatchReportOperation2.png)](../../../../Resources/Images/TrainingMaterial/BatchReportOperation2.png)
当你报告输入数量的最终工序时，就会发生至仓库- 这与到货报告采购订单到货时大致相同。默认下已建议工单号作为批次号。但你可以输入任何你想要的批次号。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/BatchReportOperation3.png)](../../../../Resources/Images/TrainingMaterial/BatchReportOperation3.png)
你可以选择库位，否则它将根据设置自动已创建并命名。因此，当你报告最后工序时，不在至仓库期间打开库位窗口。

#### 序列号层级的序列号的可追溯性
当已报告生产件的可追溯性工序时 序列号 层级，并且还有与工序链接的可追溯物料，将出现一个对话框，你在其中将生产件编号与可追溯物料链接。通过将物料的序列号 / 批次与生产件序列号相链接，你可以实现个体的可追溯性。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/MapSerialNumberTraceableMaterial.png)](../../../../Resources/Images/TrainingMaterial/MapSerialNumberTraceableMaterial.png)
系统设置 即使所有内容都已链接也显示序列号对话框 确定是否显示对话框，订单将生产件的序列号链接到可追溯物料。这适用于已建议生产件的序列号，并且全部物料都有已建议的批次号/序列号的案件。如果生产件仅一(1)剩余序列号，且留下报告的物料数量只有一(1)，这也将应用。
如果物料可追溯至 序列号 (仅领用) 层级，这是你输入物料序列号的地方。
在对话框的左侧章节，你将看到全部序列号及其包含的可追踪项目。在这里你输入已生产件的生产件的序列号以及该特定序列号包含的已消耗的序列号/批次。对话框中会已报告每已报告数量的一序列号。
在右边章节适用相反的情况，对于有批次的物料，你可以更多快速地在这里指定同一批次用于多个序列号。
两者部分中也都显示了费用号。你还将看到领用的序列号 / 批次号的体积，如果你尝试链接大于领用的数量，则会出现警告。
当已报告最终工序并发生至仓库时，你在库位输入生产件序列号。
> 如果某个序列号在生产中序列号被拒绝，则该序列号不能用于任何订单，并且会从库存余额中排除。 当序列号在生产中被已拒收时，系统将更改序列号的状态为 已报废。
对话框中功能菜单上的按钮：
随着 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_form_viewing.png) 按钮你隐藏已经已链接的序列号，仓储费用你仅看到左边上班的内容。
使用此按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_broken_link.png) 你可以断开已已链接的序列号，例如，如果你想预留它们并重新开始。
使用此按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_rename.png) 你可以根据需要重命名序列号，或者稍后在 序列号 / 批次 程序。
