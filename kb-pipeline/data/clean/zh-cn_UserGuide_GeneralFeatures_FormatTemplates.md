### 格式模板（在导入程序中）
在下面 格式模板 在程序的后台，你可以创建自己的格式模板，以便导入从另一个 ERP系统已导出的文本文件的数据从。在您自己的格式模板中，你可以定义要使用的列以及位数限制。
针对不同数据，可用使用定制/自己的格式模板的导入模板，具体程序如下： 供应商导入， 客户导入， 组件导入， 价格导入， 导入会计科目， 凭证导入， 预算导入， 和 固定资产导入。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/FormatTemplates.png)](../../../Resources/Images/UserGuide/FormatTemplates.png)
还有一个导入功能，其中包含用于库存余额的固定格式模板 库存余额导入 程序。
> 提示！ 也可以使用 CSV格式的 Excel文件作为来源，该文件以逗号分隔并且以期间作为位数限制。 例如，如果数据应该从内部获取 Monitor ERP （例如物料列表或工序列表）：通过剪贴板将列表导出到 Windows。粘贴到 Excel 中。将 Excel文件保存作为文本文件(.txt)，以制表符分隔。然后这个文件就可以直接作为导入的来源了。
导入类型
在里面 组件导入 程序你开始，选择一个 导入类型 你希望为其创建格式模板。可用的导入类型包括 组件， 物料清单， 和 工序。术语“导入类型”在 供应商导入 和 客户导入 程序。
格式模板
在里面 格式模板 默认表格，你会看到 标准 系统被用于的模板。你可以在此处添加自己的格式模板，方法是使用按钮 在末端增加新行 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add_row.png) 或通过 拆分行 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_copy_row.png) 并选择要使用的格式模板 默认 在导入中。
你还可以在这里选择 保存 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_save.png) 你已创建的格式模板。
列
这里你查询表格 可选列 以及一张表格 已选列。使用表格在中间的按钮你添加 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_next.png) 或删除 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_previous.png) 格式模板中的列。你还可以更改列的订单：向上 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_up.png) 或向下 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_down.png) 在格式模板中。这意味着你可以按照文本文件中的订单列到右边或到左边移动。你还可以通过使用鼠标指针拖放列来添加、删除或移动列。
必要时，你可以 预留 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_delete.png) 您已选列。然后你已选择添加的全部列都将被删除。使用按钮 重置到最近已保存的 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_cancel.png) 格式模板已保存之后，你可以撤销你的更改。
有些列还包含子列。到左边的小箭头表示此内容，用于展开主要的列并显示子列。你可以选择添加包括全部子列在内的整个主要的列，也可以时间选择一子列添加到格式模板中的主要的列。你还可以在格式模板中上下更改列的订单。主要的列在格式模板中仅作为分组列。子列是文本文件中可能存在的列。
> 请注意！表格中列的订单称为 已选列 必须与文本文件的列相对应。这意味着第一行的列将从文本文件的第一个列导入数据等。你应该使用列 跳过 如果你不在导入包括文本文件中的一列。例如，如果文本文件中的第五列不已导入，然后你 跳过 表格中第五行的列。
在列下，你配置 列限制器 文本文件：如果它应该是一个 逗号， 分号， 或者 标签页。
你还选择了 位数限制 对于文本文件中的值：如果 逗号 或者 小数点 应该使用。
你还可以决定是否应该导入 跳过初始行 在文本文件中。例如，如果文本文件中的 forts行是行标题，然后你在此设置中输入一(1)。默认下它显示零 (0)，也就是说，不会跳过否行。
