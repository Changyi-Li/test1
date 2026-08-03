### 日常管理部件
在本章节中你查询今天日常管理中包含的部件的描述。
信息 / 文本
此部件显示可选的文本、图像和超链接。如果你单击或点击部件中的超链接，它将在您的浏览器中打开。显示部件可用于例如不同的信息或功能公告板。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题。你还可以在此处查询文本编辑器，在其中你和格式要显示的文本、插入图像和超链接。
工作中心
该部件显示视图设置中已添加的工作中心，如果视图中否已添加工作中心，则显示全部工作中心。每视图你有一具有工作中心的部件。
你可以看到每个工作中心的工作中心编号和名称。从左边你可以看到载入的百分比。以下应用至百分比值：
- 它决定了已选择日期的负荷，即每已选择日期的当前负荷除以该日期的当前产能。
- 它不考虑延误（如果有的话）。
- 当选择历史数据并且存在负荷时，无论日延误了编号小时，都会显示 100％。
- 如果该值超过 100 %，则将显示在 红色的。
在载入下一个，你会看到符号和文本，让你知道日工作中心是否存在问题。这些符号和问题可能是以下几种：
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusTimeLate.png)– 迟到了，也就是说，如果工作中心优先计划中任何工序的计划开始日期早于今天。
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusTimePostponed.png)– 将延迟，即，如果工作中心优先计划中任何工序的新的完成日期晚于计划完成日期。
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusMaterialNone.png)– 未预留物料，即如果工作中心的优先计划中任何今日工序在匹配行列中有提醒 （意味着有物料需求）。不一定是短缺，但是必须进行物料预留。
最左边有一个堆，你可以为每个工作中心添加一种颜色，以显示其当前状态。你可以为工作中心的状态创建自己的标准。你可以使用的颜色以及它们想要表示的状态如下：
- 绿色的 -OK。
- 黄色的 –排序干扰。
- 红色的 – 必须解决的问题。
- 蓝色的 –服务或维护。
- 灰色的 – （默认）中立状态。
如果在部件中你一个工作中心，则视图中的其它部件将仅显示标记工作中心的信息。这应用至与上班中心相关的部件，即优先计划、产能、拒收、延误、内部交付可靠性和效率。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题。
优先计划
此部件显示已选择工作中心的优先计划 工作中心 部件。如果该部件中否标记任何工作中心，则优先计划将显示在视图设置中已添加的工作中心中的第一个工作中心。仅每你有一优先计划。
优先计划显示 粉色的 背景是已计划今天完成的工序，但是不完成。如果计划开始日期和计划完成日期早于或等于当前日期，就会发生这种情况。新的完成日期晚于当前日期。
通过点击或点击菜单 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_hamburgermenu.png) 在顶部，你将看到以下选项：
- 更改工作中心 – 将已选择的工序变更为不同的工作中心。
-    
重新计划订单 –根据订单所选的完成日期，重新计划已选择工序的订单*。开始日期被清空，受影响的工序的开始和完成日期将自动已重新计算，以配合已选择的完成日期。
> * 请注意！整个订单将重新计划！这意味着订单的完成日期可能与已选择日期不同。这取决于可用产能。新的完成日期也可能变成不同的日期。该功能需谨慎使用！
- 委派工作 –选择将已选择的工序已授予给哪一员工/哪些员工。
-    
更改优先级 – 使用拖放功能在优先计划中移动工序，然后根据其在优先计划中所在的行对其进行已优先排序*。
> * 请注意！如果使用拖放操作你某个工序，移动工序优先级中的全部前道工序也将根据其在优先计划中所在的行获得优先级。例如，第 4行的工序将获得优先级4 等等。如果你不想优先级考虑其它工序，然后你在之后删除它。 优先计划 程序。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题，选择时间范围，选择考虑模拟因子。在“通用”标签页下，你选择要包括在部件中的列。其它选项卡可用 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_hamburgermenu.png) 部件中的菜单。在这里你可以选择在菜单上不同选项下显示的对话框中包括哪些列。
产能
此部件显示已选择日期的工作中心的产能，该日期标记在 工作中心 部件。如果否标记工作中心，则将显示在视图设置中已添加的工作中心的产能。每视图你有仅具有产能的部件。
符号将说明工作中心类型。它可以是设备 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridMachineImage.png)，手工劳动 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridEmployeeImage.png)、外协 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridSubcontractImage.png)或池 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridManufacturingGroupImage.png)。
在下一个列，你可以看到该工作中心该日期的基本人员配置/今天的人员配置。例如，3.0/1.0 表示基本人员配备（设备 / 员工数量）为 3.0，但日的设备 / 员工数量例外，为 1.0设备/员工。如果工作中心中该日否例外，则会显示3.0/3.0。
在下一个列，你将看到工作中心的产能 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridPartialDeliveredOperation24x24.png) 在日的小时内。如果否例外，然后产能=基本人员 x基础时间。如果工作中心基础时间为8小时，基本人员配置为3人，则意味着产能24小时。如果有例外，则显示例外的产能。如果该日与基础时间有例外（4.0小时），则产能为 3 x 4 = 12小时。如果基本人员配备 1.0 也有例外，那么案件的产能为 1 x 4 = 4小时。
通过单击或点击工作中心，你可以在对话框窗口中通过更改工作中心的小时产能来添加基础时间的例外。
如果 时间记录 安装模块后，你还可以在对话窗口中通过将员工添加到工作中心来更改今天的人员配置。这意味着你将这些员工的能力移动到日的这个工作中心。你标记应已添加的员工。你可以选择已允许在工作中心报告工作的员工。这已配置在 开始工作设置 在程序中的“工作”标签页下 员工记录 - 时间记录。如果有很多员工可供选择，你也可以按字段查找员工。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题。
拒收
此部件显示已报告的工单拒收，这些拒绝情况适用于工作中心在输入的回退天数所标记的 工作中心 部件。如果否标记工作中心，则将显示在视图设置中已添加的工作中心的已报告拒收。你可以看到在工单中已选择使用的单位中已拒收的组件编号。如果你标题最大化部件，则会显示详细列表。该列表显示每工作中心和订单的拒收数量和原因代码。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题并选择部件的可视模式：图表，计量器或数字显示。对于已选择的可视模式，你可以然后单击按钮配置设置 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 字段下一个.对于图表，你可以从不同的图表类型中选择，设置最小值和值，并输入区域间隔。对于仪表，你可以设置最小值和值，输入值间隔- 细和粗，并你配置区域间隔。对于数字显示，你可以配置区域间隔。
在设置中，你还可以输入你包含并显示拒收的回退天数。时间后退到0天数意味着今天的日期。
延误
此部件显示延误（延迟订单）的尺寸，关为已选择日期中标记的工作中心的整小时。 工作中心 部件。如果否标记工作中心，则将显示在视图设置中已添加的工作中心的延误。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题并选择部件的可视模式：图表，计量器或数字显示。对于已选择的可视模式，你可以然后单击按钮配置设置 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 字段下一个.对于图表，你可以从不同的图表类型中选择，设置最小值和值，并输入区域间隔。对于仪表，你可以设置最小值和值，输入值间隔- 细和粗，并你配置区域间隔。对于数字显示，你可以配置区域间隔。
缺勤列表
此部件显示缺勤员工的缺勤列表。仅每你有一缺勤列表。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题并决定是否仅已计划缺勤，否则将显示全部缺勤。
内部交付可靠性
此部件显示工作中心的内部交付可靠性（基于时间）。 工作中心 部件。如果否标记工作中心，则将显示在视图设置中已添加的工作中心的内部交付可靠性。
准时交货意味着工序已被已报告为在已计划完成的同日已完成，或者在部件设置中已选择的容差范围内（之前和之后）。在计算中，将实际完成日期与工作中心在相关时间期间已经报告或应当已报告的工序的计划完成日期进行比较。仅已报告为已完成的工序才会被被用于计算。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题并选择部件的可视模式：图表，计量器或数字显示。对于已选择的可视模式，你可以然后单击按钮配置设置 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 字段下一个.对于图表，你可以从不同的图表类型中选择，设置最小值和值，并输入区域间隔。对于仪表，你可以设置最小值和值，输入值间隔- 细和粗，并你配置区域间隔。对于数字显示，你可以配置区域间隔。
在设置中，你还可以输入你包括的回退天数，并在计算内部交付可靠性时显示已报告为完成时间的显示工序。时间后退到0天数意味着今天的日期。你还可以输入之前和之后的之前的津贴。这是按天数输入的。之后0天数之前的津贴意味着今天的日期。提前一或之后日的之前的津贴意味着，相对于计划完成日期，今天太早一或一日。
效率
此部件显示已选择日期的工作中心的效率因子，该日期标记在 工作中心 部件。如果否标记工作中心，则将显示在视图设置中已添加的工作中心的效率因子。效率因子是根据输入的回退天数已计算的。在此计算中，将已报告时间与已报告数量的计划时间进行比较。它是每时间单位计划数量除以每时间单位实际的已报告数量，以百分比显示。仅已报告为已完成的工序才会被被用于计算。有关计算的更多详细描述，请阅读更多在线帮助功能 [工序跟进](../../StatisticsFollowUp/OperationFollowUp/wOperationFollowUp.htm) 程序。
在日常管理中你可以基于效率因子合计除以天数来获得效率因子的平均。例如：0.47 + 4.18 + 2.98 + 3.95 = 11.58 / 4（天数）= 2.895，关为 2.90。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于部件，你可以更改标题并选择部件的可视模式：图表，计量器或数字显示。对于已选择的可视模式，你可以然后单击按钮配置设置 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 字段下一个.对于图表，你可以从不同的图表类型中选择，设置最小值和值，并输入区域间隔。对于仪表，你可以设置最小值和值，输入值间隔- 细和粗，并你配置区域间隔。对于数字显示，你可以配置区域间隔。
在设置中，你还可以输入计算效率因子时你包括的回退天数。时间后退到0天数意味着今天的日期。
网址
该部件显示一个网址。
在设置中 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 对于该部件，你可以更改标题并输入要显示的网址的 URL。使用按钮 转到网页 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_url.png) 在地址字段下一个，你可以在浏览器中打开网址，例如检查输入的 URL 是否正确。
