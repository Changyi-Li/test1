### 配置组
在此程序中，你创建并更新配置组。配置组描述的是产品的组合。
你可以在页眉行输入评论并将链接文件到配置组。该评论在订单登记期间显示在指南中，然后可以提供帮助。在主行中，你还可以看到哪些组件链接至现有的配置组-
结构 / 指南标签页
在下面 结构 / 指南 标签页让你创建和编辑在注册产品订单时你的指南。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsStructurGuide.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsStructurGuide.png)
在这里，你可以将章节、选项列表和变量放在一个结构中，仓储费用它们按逻辑订单出现。每个章节都有一个名称，其中包含翻译和设置确定其在指南和文档中的显示方式。一个章节表格登记订单时使用的指南的一。在订单文档中，章节功能作为具有标题和页脚的分组。
可以添加现有的选项列表和变量，两者可以直接在相关章节中新建的选项列表和变量。使用功能菜单上的按钮或使用“拖放”功能，你可以在选项列表和变量之间以及不同部分在中间移动和组织选项列表和变量。你还可以将一个选项列表移动到另一个选项列表中，使其成为结构中选项列表的基层。
要编辑更多属性和新建选项中的不同选项，你可以使用指向该程序的链接 选项列表 你可以在功能菜单上查询它。还有一个指向该程序的链接 变量 你可以在其中编辑它们的属性。
选项列表标签页
在下面 选项列表 标签页中你可以概览配置组中使用的选项列表。你可以在此处添加和删除选项列表。还可以通过输入新建选项列表代码来新建的选项列表。在这种案件下，你需要在结构中添加新建选项列表 结构 / 指南 标签页，之前你才能在程序中保存。
你决定选项列表如何与 选项最小数量 （最小选项）和 选项最大数量 （最大选项）设置，以及它是否应该是 自动选项 或不。如果最大选项值是大于分钟 选项时，你还可以输入 最小数量 和一个 最大数量。
在标签页的章节，你可以看到选项列表包含哪些选项，但无法在此处不可改变该目录。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsSelectionsGroupsTab.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsSelectionsGroupsTab.png)
如果你在此标签页下添加或新建的添加选项列表选项列表，然后你先在 结构 / 指南 标签页，之前你才能在程序中保存。
变量标签页
在下面 变量 标签页中你可以看到配置组被用于的全部变量。可以添加和删除变量。某些变量设置也可以在这里已更新。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsVariablesTab.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsVariablesTab.png)
如果你在此标签页下添加变量，然后必须在以下部分下使用你 结构 / 指南 标签页，之前你才能在程序中保存。
给变量值有三种方式：
- 用户在登记订单时输入值。
- 值是使用公式已计算的。
- 通过确定选项列表中的选择来已添加值（见低于）。
如果变量应由一或多个选项列表确定，即它应通过确定选项列表中已选择组件来获取其值，然后你可以在此处的字段中输入默认值 值 直接针对确定选项列表中的选项（组件）。这是在标签页的底部完成的。
另外，你可以通过设置配置从组件登记中组件的某些字段加载值 链接到字段 在变量上。当变量按选项列表决定时，你还可以选择一个 聚合方式。这意味着应如何将来自多个选项或组件字段的值用作变量的值。
> 一个有用的技巧可能是使用 附加字段 对于组件登记中的为组件，是否应该从组件登记中的组件加载值。
规则标签页
在下面 规则 标签页你创建并更新应在配置组中应用的规则。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsRulesTab.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsRulesTab.png)
每个规则都有一个规则号，你可以输入描述以帮助以后理解该规则。当需要时，可以重新编号规则编号。你可以按此标签页中的全部列进行排序和筛选。这使得你可以分析影响某个选项的全部规则，或者查询某个选项或变量产生影响的全部规则。
在列中 逻辑公式， 按规则排除， 和 按规则自动已选择，选项列表代码，组件号和变量代码，用于描述规则。你可以决定是否显示最后两列。这是通过设置完成的 显示"已排除"与"自动选择由"的列 在标签页顶部。
随着 规则定义 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/gridFolderImage.png) 你一个窗口，你可以在其中编辑规则（见低于）。
规则定义
规则可以排除选项列表中的一或多个选项，也可以排除整个选项列表或变量。规则还可以配置自动生成一或多个选项。规则可以包含你创建的选项、变量值以及逻辑和数学功能的复杂条款。例如，你可以创建规则，基于产品的不同“包装”自动添加或排除某些设备。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsRuleDefinition.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorConfigurationGroupsRuleDefinition.png)
> 规则提示： 使用带有设置的选项列表 自动选项–是, 第一个。在选项列表中按逻辑订单添加选项（组件），并创建排除无效的选项的规则。然后第一个有效选项将自动被已选择，但用户可以在配置期间人工的选择其它选项。这通常在涉及某种尺寸时使用，其中将自动已选择“足够”或“足够好”的第一个选项，但你可以人工的选择其他选项（例如更多强大的驱动电机）。 使用功能 拒绝 在规则定义中。如果你需要在定义中添加多行，则考虑使用拒绝来“逆转逻辑”以创建更多简单的规则可能会很有用。 区分大选项列表分成多个较小的列表，并创建排除整个选项列表的规则，而不必单独排除每个选项。 在窗口 规则定义 你可以使用拖放功能。这意味着你使用鼠标指针将部件从构造图拖放到定义盒子、按规则排除和按规则选择。 如果你创建许多类似的规则，你开始创建一规则作为模板。然后，使用“规则”标签页下的功能菜单上的按钮你规则复制到新建规则。
