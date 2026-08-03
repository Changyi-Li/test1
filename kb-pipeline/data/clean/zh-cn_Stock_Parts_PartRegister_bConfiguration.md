### 配置
在此框中，您搜索连接到的设置 产品配置器 选项中 Monitor ERP。

#### 配置组
你可以在这里选择应用于该组件的配置组。已选择配置组的名称显示在字段的到右边。对于已配置的组件，应用不同的条款，如下低于：
- 该组件应该有一个基本BOM 与工艺路线，你创建在 BOM 与工艺路线 程序，如果它是生产件类型。
- 组件应具有可追溯性 批次 层级或 序列号 层级。如果该组件的可追溯性不已激活，则会显示警告。
- 该组件应该有批量规则 需求直连 在全部仓库。如果该组件的可追溯性不已激活，则会显示警告。

#### 自动打开
通过此设置，登记你你组件订单自动打开配置窗口。

#### 默认配置 / 模板
你可以在此处选择一个模板，将你作为登记该组件订单时的默认配置应用。可以在配置窗口中已创建与注册组件订单连接的模板。也模板已创建在 配置模板 程序。
> 如果你的 Monitor ERP 系统由MONITOR G4 转换而来，已经为该组件已选择了模板。此模板称为 标准 并在其配置中已选择相同的部件，即之前所说的 默认 用于前道生成MONITOR中的选项列表的选择替代方案。
其它的
在下面 其它的 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 按钮可以输入更多信息配置信息，低于所示。当已保存的信息已经存在时，按钮上的符号将会不同 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info_have_data.png)。这些设置用于配置中的选项组件，即被用于在选项列表中的组件，不已配置的主组件。

#### 价格公式
点击 价格公式 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add_formula.png) 按钮，你可以使用第一个选择的你配置组中的变量输入组件的价格公式。价格公式的功能是将常规的价格值与公式的结果乘以。当组件已已保存价格公式时，按钮上的符号将会不同 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_formula_info.png)。
价格公式通常用于计算不同配置被用于的为组件的价格。价格公式使得所包含组件的价格可以根据包含该组件的配置中的变量值而变化。价格公式主要用于具有批量规则需求直连的采购件，其中设计和价格有所不同。
当需要时，还可以使用价格公式对主组件（正在已配置的组件）用于灵活价格。在配置零件的常规的价格时，将乘以主组件的价格公式公式的结果。
当组件有价格公式时，已计算的价格将用于按标准计算和订单。在按标准计算中，选择中的备选价格是使用价格公式已计算的。如果通过工单创建自了组件的已链接采购订单，则将使用价格公式已计算供应商价格和零件的标准成本，并将其已保存在订单行中。在采购订单行中，单价已计算的价格将默认被锁定由。如果工单被用于的物料有价格公式，则已计算的价格将用作计划价格和已报告价格。该计算是基于备选价格（根据设置）的，并将根据价格公式已重新计算。

#### 备选名称
你可以在此处输入备选名称，当在配置中使用该零件时，该名称将取代组件的常规的名称。使用按钮 翻译 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_translate.png)s 你可以将文本翻译为系统中已登记的不同激活语言。阅读更多内容 [语言管理](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) 用于可翻译文本。

#### 扩展描述
你可以在此处输入该组件的扩展描述文本。对于包含该组件的配置，此描述显示在订单文档上的组件名称或备选名称低于。在文本编辑器中，你可以编写和格式文本、插入图像、签名和超链接等。通过单击插入短语按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add_phrase.png)，可以插入在短语程序中登记的不同短语。 使用按钮 翻译 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_translate.png)s 你可以将文本翻译为系统中已登记的不同激活语言。阅读更多内容 [语言管理](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) 用于可翻译文本。
然而， 附加的名字 你在配置中选择的组件将不显示在订单文档上。
