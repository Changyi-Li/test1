### CDT 的结果
点击按钮 中部夏令时间 在报价行,客户订单行和工单上 ,你可以 在 单独 的窗口中 看到 CDT 的结果.此按钮上的符号表示订单/订单行如何根据低于列表已供应。按钮上的工具提示也会以文本表格告知你这一点。
-   
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StockBalance.png)–此行由余额供应。
-   
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusRegistered.png)– 该行供应由现有的订单提供。
-   
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypeManufacturing.png)– 需要生产来供应该行。
-   
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/PartTypePurchase.png)– 需要采购才能供应该行。
如果有备选工作中心/供应商，并且你使用备选工作中心/供应商重新计划订单，则按钮上你还会看到星号（*），这会结果更早的交货日期/完成日期。
在结果窗口中有一个标签页，你可以在该选项卡下看到 CDT 的规划窗口。根据订单的已供应方式，你还可以在附加选项卡下查看采购建议、工单建议、订单信息或以图表形式显示的负荷。
在结果窗口的采购建议和工单建议选项卡下的功能菜单上，你可以使用不同的按钮：
-   
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_delivery_time_check_again.png)– 再次运行 CDT。如果你选择/添加备选工作中心/供应商，你可以使用此按钮再次运行CDT。
-   
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_critical_op.png)– 转到临界工序 / 物料。使用此按钮，你可以在表格中导航到关键的第一个工序或首要物料。
-   
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/button_filter.png)– 也显示不包括在CDT的工序。通过单击此按钮，你还可以显示订单结构中工作中心中不包含在 CDT 中的工序。
> 帮助结果窗口，你可以调查哪里存在关键工序和物料，即哪些供应商和工作中心的计划交货日期/完成日期和实际交货日期/完成日期在中间差异最大。差异体现在工作日编号上。这帮助重新计划订单以便更快地交货就绪。
汇总
在里面 汇总 在结果窗口组件的表格中，你仅看到是否需要生产或采购的信息。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ResultFromCDT_Summary.png)](../../../../Resources/Images/UserGuide/ResultFromCDT_Summary.png)
在第一行，你可以看到输入的订单的交货日期/完成日期。在下下一行中，你可以看到如果使用标准工作中心的话最早交货日期是多少，以及订单的边际贡献和边际贡献率是多少。在第三行中，你可以看到如果使用 CDT已选择的备选供应商和工作中心，最早交货日期/完成日期是什么。在这种案件下，你还将看到订单的边际贡献和贡献比率。
如果 CDT已选择了备选供应商或工作中心，然后你可以检查 应用 如果你希望使用该替代方案，请在第三行中选中框，或者你可以保持默认设置以使用标准工作中心。
使用按钮 确认![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) 你确认应该使用哪一行。结果窗口然后关闭，并且该行的交货日期/完成日期将会输入到订单中。
采购订单储备
这 采购建议 如果在采购件的组件上运行CDT，并且检查交货时间功能已经已创建了采购建议，则标签页已激活，也就是说，你需要进行采购来供应订单/订单行。
你然后在表格中看到有关采购建议的信息，其中包括供应商、数量、需求日期、交货日期和物料行的差异（实体的差异）。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ResultFromCDT_POS.png)](../../../../Resources/Images/UserGuide/ResultFromCDT_POS.png)
你按钮后，会显示组件的供应商链接 备选供应商 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info_have_data.png) 然后就可用了。在这里，你可以看到备选供应商及其交期是否会影响能否提前交货关键物料。在下面 更多信息 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 你将看到默认供应商的交期为标准。
工单建议
这 工单建议 如果你对生产件运行分析，并且 CDT功能已已创建工单建议，即你需要制造以供应订单/订单行，则标签页已激活。
你然后在表格中看到有关工单建议的信息，其中包括订单的主组件、工序和物料。在下下一个节点（层级），你可以看到包含的组件和物料。如果你已已选择CDT 还应检查包含的库存驱动组件（通过系统设置），那么在不可用余额的案件下，你还将看到有关这些组件的工序和物料的信息。对于每个工序和物料，你将看到工作中心和已链接的默认供应商、数量、开始日期、需求日期、个体差异*和天数的整体差异*以及交货日期。最关键的工序和物料红色浅色显示。使用按钮 转到临界工序 / 物料 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_critical_op.png) 你标记 了第一个关键工序/物料.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/resultFromCDT_MOS.png)](../../../../Resources/Images/UserGuide/resultFromCDT_MOS.png)
点击按钮 备选工作中心 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 可以改变关键工序的更改工作中心以获得更早的完成日期数。你按钮后，会显示物料上的供应商链接 备选供应商 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info_have_data.png) 然后就可用了。在这里，你可以看到备选供应商及其交期是否会影响是否可以更早交货关键物料或是否可以以较低的成本采购物料。
> * CDT两者计算行差异，也计算整体差异。哪些结果应该继承到订单行的结果字段由系统设置决定，称为 差异。这 个体 此设置中的选项意味着 CDT 将仅使用包含/合并的工序和物料的最大差异。这 整体 此设置中的选项意味着 CDT 将尝试将全部包含/合并的工序和物料放入负荷计划中，就像订单上的那样（然后CDT 将订单用作整体中的件，并尝试将其放入）。如果不，则该行的整体差异将显示为 999。
CDT计划窗口
标签页 CDT计划窗口 总是处于激活。在这里你可以看到工单建议标签页下焦点组件的计划窗口。
计划窗口与 组件登记 和 需求计算 程序。来自 CDT功能的客户订单、工单、建议和物料需求以 (美国中部夏令时间) 在里面 类型 列。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ResultFromCDT_PlanningWindow.png)](../../../../Resources/Images/UserGuide/ResultFromCDT_PlanningWindow.png)
订单信息
这 订单信息 如果存在可以供应订单/订单行的现有工单，则标签页已激活。在这里你可以看到与 工单信息 程序。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ResultFromCDT_OrderInfo.png)](../../../../Resources/Images/UserGuide/ResultFromCDT_OrderInfo.png)
负荷
这 负荷 如果 CDT功能已经已创建了工单建议来供应订单/订单行，则标签页已激活。在此标签页下，你可以看到包含关键工序/物料的组件节点的工序上全部受影响工作中心的负荷图表。该组件显示在第一行。在低于的行中，你可以看到工序如何作为不同的冻结每个定位。
每个操作的冻结都有一个颜色代码或图案，根据：蓝色表示工作中心的现有负荷，颜色表示根据CDT 的操作负荷，绿色网格表示来自另一个工序的 CDT的负荷。
关键工序在左边以红色点标记，关键工序的冻结红色浅色。当你打开标签页时，负荷图表也会定位在时间轴上的关键工序上。
你可以使用标签页底部的按钮沿时间轴导航，也可以选择直接转到关键工序。你还可以使用一个控制杆来放大和下班时间轴。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ResultFromCDT_Loading.png)](../../../../Resources/Images/UserGuide/ResultFromCDT_Loading.png)
