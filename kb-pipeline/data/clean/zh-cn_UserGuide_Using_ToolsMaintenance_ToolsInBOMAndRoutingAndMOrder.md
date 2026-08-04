### 使用 BOM 和工艺路线以及工单中的工具
工具可以链接至物料清单 (BOM) 和工艺路线中的工序，然后在工单中进行处理。

#### BOM 与工艺路线
在创建为组件的BOM 与工艺路线时，工具可以按照与物料行相同的方式链接至工序。在大多数案件下，该字段 准备数量 用于输入该工序需要多少个工具。在包含可重复使用工具的行中，你查询一个字段，你可以在一输入是否应在除领用操作其它的工序中退回工具。你还会查询两个字段，你可以在其中输入每周期生产件的细节编号以及工具的周期。当已报告工序时，需要这些值订单已更新序列号登记中的工具计数器。序列号登记中的这些计数器的值可以反过来用于触发器工具的不同维护项目。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsInBOM.png)](../../../../Resources/Images/TrainingMaterial/ToolsInBOM.png)
> 提示！在里面 层级列表 程序，你可以看到该工具被包含在哪些BOM和工艺路线中。在里面 物料列表 程序，你可以按照与包含物料相同的方式编辑工具行上的数据。你还可以在包含该工具的 BOM 和工艺路线中将一工具交换为另一个工具。

#### 工单
在工单中，你可以按照与物料相同的方式添加和删除工具。可重复使用的工具按订单在物料列表中显示两行。一行用于领用，一用于退回。领用行上的预订日期是从工序上的开始日期加载的。退回行上的预订日期是从完成日期加载的。工具 每周期数量 和 周期 如果你需要做临时更改，可以在订单上进行已调整。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsInMOrder.png)](../../../../Resources/Images/TrainingMaterial/ToolsInMOrder.png)
> 提示！ 你可能需要配置以下设置 允许自动领用 当工具有序列号时。这将有助于报告提款和退货。这可以在组件模板中已配置 组件模板 程序。 在订单程序的构造图中，你查询一个按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_tools.png) 用于显示或隐藏工具。你还可以在此处查询按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_search.png) 用于在构造图中查找工具。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsInStructure.png)

#### 工单文档
在里面 文档模板 - 工单 程序，你查询确定工具在订单文档上如何显示的设置。你可以通过创建现有的文档的变量来使用单独的工具列表，配置你仅显示工具。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsMOrderDoc.png)](../../../../Resources/Images/TrainingMaterial/ToolsMOrderDoc.png)

#### 优先计划、优先计划列表、池计划
在优先计划的工序行中，你查询包含有关工具信息的新建列。在里面 电视 列，你可以看到该工序是否有工具以及是否已已预留。你还会查询显示组件与该工序链接至的首要工具的零件编号和工具名称的列。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsInPriorityPlanning.png)](../../../../Resources/Images/TrainingMaterial/ToolsInPriorityPlanning.png)
如果你想要筛选工序，以便能够基于工具坐标加工，其方式与物料相同。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsFilterMaterial.png)

#### 管理工具准备
手动操作状态功能可用于创建流程来订单工具的准备，并确认工具是否可用。

#### 工单报告工具
在报告工单上的工具时，可以使用多个可能的设置组合 -例如，在已开始和已报告工序时是否应人工的或自动报告时间工具。有些设置在一起工作会更好，但有些设置结合在一起效果会更差。低于设置会影响工具的报告。
> 请注意！慎重你如何报告工具非常重要。
生产系统设置：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsSettings1.png)](../../../../Resources/Images/TrainingMaterial/ToolsSettings1.png)
时间记录的系统设置：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsSettings2.png)](../../../../Resources/Images/TrainingMaterial/ToolsSettings2.png)
工作中心的设置：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsSettings3.png)](../../../../Resources/Images/TrainingMaterial/ToolsSettings3.png)
组件的设置（也可以通过组件模板进行已配置）：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsSettings4.png)](../../../../Resources/Images/TrainingMaterial/ToolsSettings4.png)
有关如何处理和配置工具报告设置的建议
处理和设置取决于你是否要人工的或自动报告工具。

#### 工具手动报告
如果您的公司有一个负责处理工具领用和退回的工具部门，然后手动报告会很有用：
-   
在系统设置里关自动领用和退回。
-   
在 拣货单 和 报告拣货单 程序。
-   
在 领用列表 程序。

#### 记录时自动报告工具
工序你在 记录终端 程序，在时间记录模块中，想要自动领用和退回：
-   
激活设置 允许自动领用 在你查询方便的地方，在带有序列号的为工具组件登记中。
-   
激活系统设置 当工序被报告完成时退回可重复使用的工具。（这个逻辑就是在退回工序中当剩余数量达到0的时候就会自动退回。该逻辑有一条件 –否员工可以在工序中打卡。）
提款时有两种备选可供选择：
方案一：
-   
激活系统设置 自动报告工具。
-   
配置 在第一次自动报料时建议总准备数量 系统设置 为工具。使用此设置，领用不在打卡时进行，而是在第一个报告工序数量时进行。（这样做是为了避免在工单中部分报告数量时你问题。）
方案 2：
-   
激活设置 工序开始时建议领用工具。操作员在打卡订单时然后看到一个报告窗口。然后他/她可以签字同意工具领用。工单照常已记录。

#### 自动报告工具，无需记录
如果你使用生产模块中的报告程序来报告工序：
-   
激活系统设置 自动报告工具。
-   
激活系统设置 当工序被报告完成时退回可重复使用的工具。（这个逻辑就是在退回工序中，当剩余数量达到0，就会自动退回。该逻辑有一条件 –否员工可以在工序中打卡。）
-   
配置 在第一次自动报料时建议总准备数量 系统设置 为工具。然后领用将在第一个报告工序数量时进行，与非在打卡期间进行。（这样做是为了避免在工单中你部分数量报告时出现问题。）
-   
停用设置 工序开始时建议领用工具。

#### 使用相同工具批次记录订单
同一工具将被取出批次中全部使用该工具的工序。领用将通过第一个部分报告时的自动报告或通过报料窗口进行，具体取决于上面系统设置。请注意！记录批次时，停止工作时工具总是自动返回。如果退回时间工序上有剩余数量，则工具上的剩余数量将被重置，以便在再次已开始订单时可以再次领用。
请注意！添加到批次功能尚无法使用。如果工序需要批次已记录，不支持其它程序中的手工领用和退回。

#### 日志周期和周期
为工具已取出工序的序列号工具， 周期 自动登录序列号。你可以在 序列号 / 批次 程序。当已报告工序数量时，会自动进行日志。周期 如果 在BOM 与工艺路线或订单中输入了周期，也会记录在序列号上。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ToolsLoggingTimeCycles.png)](../../../../Resources/Images/TrainingMaterial/ToolsLoggingTimeCycles.png)
