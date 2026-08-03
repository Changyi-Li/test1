### 列表标签页
该标签页分为三个不同的部分。到左边有一个章节包含 [设置](bSettings.htm) 可以为列表进行已配置。在到右边你将看到一个列表，其中包含根据所做的设置制定的负荷计划的全部信息。窗口底部有一个“合计”章节。
该列表总是按工作中心分组，并显示在“创建”已选择工作中心标签页或 设置 到左边章节中的标题。该列表可以按照负荷类型进行分段。
使用功能按钮 转到程序 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_link.png)，你可以转到多个相关程序，例如，你可以变更产能并变更优先计划。
你可以使用按钮展开每个负荷类型 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_expand_row.png) 行首。然后显示实际订单、建议等。你可以看到他们创建负荷的小时编号和时间期间。对于实际订单，你将看到订单号、组件号和工序。还有一个名为 更多信息 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 在该行上，你可以用来查看有关该工序的信息。
如果你已已激活 可更新 模式 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_edit_list.png) 在过程的工具栏上，你可以使用功能按钮 重新计划 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_clock.png) 更改工序的开始时间和完成时间。当进行任何变更时，你会询问你是否还希望重新计划整个工单。在程序保存的时候会进行重新计划。
随着 更改工作中心 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_copy_to.png) 你一个对话窗口，你可以在打开更改已选择工序的更改工作中心。如果复选框 建议最近的工作中心 在对话框窗口中被已激活，这意味着当你想要更改更改工作中心时，最近已选择的工作中心将成为默认。如果该工序有备选工作中心，你可以默认变更为为该工作中心。这 显示所有工作中心 在这种案件下，对话框中的复选框不标记。如果某一工序不备选工作中心，则会标记该复选框，然后可以在全部工作中心（外协工作中心除外）中进行选择。还可以通过“拖放”将标记的工序移动到不同的工作中心。
和 变更产能 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_calendar.png) 你可以更改已选择工作中心和周的产能 按工作中心汇总 已设置为产能。对于具有“日计划”的工作中心，可以编辑每个的基础时间和设备 / 员工数量。对于具有“小时计划”或“通过日程表产能”的工作中心，可以通过改变日程表和设备 / 员工数量来更改产能。

#### 导航按钮
您可在图表/列表下找到以下可用于导航的按钮：
- 最早负荷期间 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_first.png) - 此按钮将您及时带回到图表/列表中存在负荷的第一个周期。
- 推迟10个周期 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_backward.png) - 此按钮可让您从当天时间周期退回10个时间周期。然后，您可再次使用该按钮以退回另外10个时间段。
- 上一周期 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_previous.png) – 此按钮一次将焦点移回一个周期。
- 今天 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_today.png) - 单击此按钮以返回在时间轴上标记今天日期的红线。
- 下一周期 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_next.png)此按钮一次将焦点向前移动一个周期。
- 提前10个周期 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_forward_10.png) - 此按钮可让您从当天时间周期退回10个时间周期。然后，您可再次使用该按钮及时提前10个周期。
- 最后负荷期间 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_last.png) - 此按钮将您及时带回到图表/列表中存在负荷的第一个周期。
在导航按钮行下还有一个分隔符，可用于通过光标更改程序窗口中各部分的大小。

#### 合计的
在图表/列表下的表格中，你将看到每个日/周/月的总负荷信息，具体取决于您的已配置设置。合计遵循图表/列表中上面显示的期间。
无论其它设置如何，总是显示的值是 产能 （%）， 总负荷 （小时）， 每期间差异 （小时）， 载入 （％） 和 累计差异 （小时）。
在下面 产能，你可以看到针对你选择章节的每个数据类型对应的一。例如，如果你选择按负荷类型进行章节，则会显示行实际订单和行建议等。其它，如果你选择了每工作中心划分章节，则会显示你已选择的每工作中心的行。你仅看到负荷图表/列表中显示的合计信息行。例如，如果你已选择不显示CDT或不工作中心X 的负荷，否不会显示它们的行。
这张表格的正上面你可以看到 延误合计 （过去的负荷）和 范围合计 （在灵活的未来中负荷）。此处显示的合计还包括时间期间（11 个期间）之外的负荷，因此，它们不在图表中显示为单独的列。
