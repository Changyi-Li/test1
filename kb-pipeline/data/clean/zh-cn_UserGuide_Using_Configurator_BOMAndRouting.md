### BOM 与工艺路线
如前所述，你可以在BOM 与工艺路线中将组件链接到配置组，选择是否自动打开配置窗口，然后选择模板。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratorBOMAndRouting.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorBOMAndRouting.png)
在BOM 与工艺路线中，你还可以对配置组中的全部组件使用以下功能。也就是说，两者针对主组件，也针对全部包含/合并的订单导向的生产件以及虚拟件，无论它们是通过基本BOM 与工艺路线还是通过选项包含在订单中。
- 对于工序，你可以使用公式来计算单位时间和准备时间，并且你创建配置指导。
- 对于物料行，你可以计算数量和准备数量，也你在这里创建配置指导。
- 配置可以创建唯一的变量代码，使得你可以使用基于变量代码的条款两者进行工序和物料。

#### 配置指导
工序和物料（以及选项列表中的选项）可以有配置指导。在配置指导中，你可以将静态文本和图像与变量值以及在配置指导中你的公式计算值结合。
这 CI 工序和物料行上的按钮打开窗口 配置指导。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguredInstruction.png)](../../../../Resources/Images/TrainingMaterial/ConfiguredInstruction.png)
在里面 指导 在窗口到左边的章节中，你添加指导的变量，并将每个变量链接至一或更多配置组。每个变量都会被赋予一个流水号。第一个变量从 1001开始。
在章节 变量 在底部，你可以看到配置组中可用的变量。
在章节 公式 你可以在右边添加公式，并帮助可用变量你值并计算它们公式名称。
中间章节称为 指导，你写下实际的指导。可以使用拖放功能两者变量和公式已添加到指导中的任何位置。另一种方法是在指导中人工的输入变量和公式，形式为 [v：变量代码] 和 [f：公式名称]。进行校验以确保输入的变量和公式可用。
在图片它们在指导中以绿色突出显示，但这仅为了让它们清楚。当然，你可以根据你在指导中格式两者、变量和公式。
你可以时间使用按钮测试整个指导的结果 预览指导 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_preview.png) 下一个的指导。
你后，你应该保存 OK 按钮。
> 提示！ 程序 模拟工单 是测试配置组的好工具。在该程序中，你可以轻松查看物料与工序是否按照你想要的方式已创建。 如果你想测试文档的设计并查看配置指导是否正确，大多数案件下最好在程序中创建测试订单 登记客户订单 并根据客户订单创建工单。 你可以激活 自工单 在系统设置中 传输信息自需求原因至采购订单。这意味着指导（你可能已经通过配置确定）从工单上的物料行已传输到应供应该行的采购。(支持传输信息自需求原因至采购订单 从客户订单 稍后将会已添加。）
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratorSystemSettings2.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorSystemSettings2.png)
