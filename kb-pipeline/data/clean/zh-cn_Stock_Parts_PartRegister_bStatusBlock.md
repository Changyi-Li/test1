### 状态 / 冻结
在该框中你选择该组件的状态。你还可以冻结该组件或为其输入消息。

#### 状态
在选择你的状态。新的组件将获得默认组件状态1-4，由系统设置决定 新组件的默认状态。
一个组件有七种不同的状态。这些反映了部件的生命周期（以及未激活组件的附加状态），低于表格的状态阶段所示：
| 象征 | 代码 | 名称 |
|---|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeFictitious.png) | 1 | 报价 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypePrototype.png) | 2 | 样品 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/green_dot.png) | 3 | 新组件 |
|   | 4 | 正常的 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeUpgrade.png) | 5 | 新版本 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeDowngrade.png) | 6 | 逐步淘汰 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeDeleted.png) | 9 | 过时的 |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/RedPadlock.png) | 99 | 未激活 |
不同组件状态是固定的。不添加或删除组件状态。例如，在订单行上显示组件的状态。你可以根据不同列表中的组件状态选择。
如果组件状态1（报价），则你无法为其登记客户订单或工单。
如果组件状态为 3（新组件）或 5（新版本），则在调用文档设置时，这将已打印在采购订单和工单的文档上 显示组件状态 已已激活。
如果你为该组件输入状态5（新版本），则输入的版本评论将显示在 版本 当文档设置调用时订单文档上的字段 显示版本组件状态5 的评论 已已激活。你配置在​ 文档设置 程序。
如果你输入状态99（未激活），组件否再修改该组件的任何信息。未激活组件也会在新建报价、客户订单、询价、采购订单、工单、BOM 与工艺路线以及新序列号 / 批次号中被已冻结。你可以使用状态字段下一个的按钮重新激活未激活的组件。

#### 活动
你可以在此字段中为该组件配置一个冻结或通知。
存在以下冻结/通知的备选：
- 无/取消（默认）——不显示任何冻结或通知，或者它已被取消
- 通知 - 您可以在一个单独的窗口中选择将在其中显示通知/消息的事件。必须输入消息文本。如果您已激活此备选，则可以使用该字段旁边的按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_comment.png)打开一个窗口，您可以在该窗口中看到和/或更改通知/消息应该应用时的事件。在该字段下方，您可以查看是谁创建了通知以及何时创建。在程序的主行上，消息的符号也显示在记录的代码/编号字段旁边。
- 冻结 —— 您可以在单独的窗口中选择将应用冻结的事件。必须输入原因文本。如果您已激活此备选，则可以使用该字段旁边的按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/RedPadlock.png)来打开窗口，您可以在该窗口中看到和/或更改应用该冻结的事件。在该字段下方，您可以查看是谁创建了冻结以及何时创建。在程序的主行上，代码/编号的记录字段旁边也会显示冻结符号。记录的代码/编号也以红色粗体显示。
在冻结/通知窗口中，您找到文件按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_file_link.png)。使用此功能，可以将文件链接到冻结或消息/通知。
如果有取消，您可以在字段下方看到有关信息。右侧的按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png)访问包含以前的冻结/通知的事件日志
在具有产品配置选项的系统中，你还可以选择冻结或显示某个组件上的消息，该消息然后在配置中已选择组件时显示。如果已选择了已冻结的组件，则不保存配置。
