### 选项列表
在此程序中，你创建并更新选项列表。
在程序的页眉行中你选项列表的名称和代码。该名称在订单登记时显示，也可以显示在文档上。代码如规则所示。你可以输入 分类 A 评论，你可以链接 文件 功能作为订单登记时的指导。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/TrainingMaterial/ConfiguratorSelectionGroups.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratorSelectionGroups.png)
在页眉行低于你可以输入可用的选项。也就是说，选项列表应该包含哪些组件。
> 该选项作为工单中的物料行行。大多数字段与BOM 与工艺路线中的物料行相同。
有两种方法可以输入选项（也可以组合使用）。这是为了：
- 将组件添加到列表中。提示！如果组件较多，你可以使用按钮从组件剪贴板粘贴它们 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_import.png)。
- 输入一个 选择 按钮下方的组件 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/modified_image.png) 位于列表顶部行。此选择的定义方式与列表的选择相同。例如，你可以输入应包含组件代码为“钢铁”且状态“正常”的全部组件。如果有很多选项或者经常已添加新建选项，则这种方式特别适合使用。
顶行功能作为其它行字段值的默认，但每字段和每行可以有例外。
可以使用拖放功能或按钮来更改选项的订单 向上移动 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_move_up.png) 和 向下移动 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_move_down.png) 在功能菜单上。你还订单排序更改 排序 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_sort_right.png) 按钮。
使用按钮 添加子行 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add_subrow.png) （Ctrl + 班次 + F5）为组件添加子行。这些是上面行选项中应该总是默认包含的组件。
对于每个选项，还可以在注册订单时显示的行中输入评论。

#### 继承选项的功能
有一项功能，即在订单行/报价行的配置中所做的选择会在下一个下一个的订单行/报价行中已自动选择。你还可以在功能中包括已选择数量。该功能由主行上的两个字段控制，名为 继承选项 和 ID。
该功能还可以在完全不同的已配置组件在中间工作，因为你输入 ID 它决定了其它选项列表将每个继承。
例如，如果你输入“颜色”作为ID，则此选项列表中的选项将被继承到以下订单行/报价行，前提是此配置中有一个以“颜色”作为ID的选项列表。也就是说，下一个订单行/报价行上不是相同的选项列表或相同的主组件。这可能很有用，例如，如果你有一个特定颜色的门，并且在下面的选项列表中，对于门，你希望自动继承相同的颜色。
选项列表的ID将链接不同的选项列表，即使如例如所示，门和门有两个不同的选项列表。
如果你稍后更改了订单行上的选项，你可以选择是否让其它订单行继承这些变更。
