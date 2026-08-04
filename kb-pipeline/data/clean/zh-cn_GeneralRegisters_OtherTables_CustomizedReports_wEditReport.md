### 编辑报告
点击 编辑报告 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_edit.png) 在功能菜单中，你你打开一个编辑器来创建/构建已定制的报告。此编辑器可用在 列表类型 盒子里 子报表 盒子。该编辑器组成： 布局， 选择行， 设置， 和 SQL。对于子报表， 选择行 标签页不显示..
布局
该标签页有两种变量，具体取决于你是否已选择了 列表 或者 自由格式布局 在下面 类型。
列表
如果你选择 列表 作为 类型，你会在标签页下查询一个编辑器，你可以在其中输入报告中数据列的不同属性。数据列显示为标签页下的行。这些列是从在 SQL 标签页。
对于每个数据列，你可以根据以下内容配置编号属性。你报告订单更改列 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_up.png) 和 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_goto_down.png)，或者使用“拖放”功能。

#### 标题
在这里你报告中输入的标题。使用按钮 翻译 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_translate.png)s 你可以将文本翻译为系统中已登记的不同激活语言。阅读更多内容 [语言管理](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) 用于可翻译文本。

#### 已分组
如果选中此框，则该列将被已分组。

#### 宽度
报告中默认的列宽度（以像素编号）。

#### 排序
确定列是否订单升序、降序订单，或不全部。

#### 显示格式
在这里你可以决定列的显示格式。支持数字格式。

#### 聚合
确定或不应在报告中汇总列中全部行的值。可以已选择的不同类型的聚合有：合计、平均价值、数量、最小（值），最大（值）、第一记录、最近记录、中值和外部的。聚合结果字体粗体在报告中相关列下。

#### 在按图表显示
你可以在这里确定是否应默认在图表中显示相关列。当你选择以图表表格视图报告时，将包含已已配置此设置的列。如果某一列的复选框不可用，则表示该列的数据不能显示在图表中。

#### 更多信息
如果该列应在按钮下方可用，检查此框 更多信息 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 在报告中。

#### 打印
如果你想要在报告的打印中包括该列，检查此框。

#### 隐藏
如果你想在报告中负荷列表时排除该列，检查此框。

#### 剪贴板
你可以在这里配置哪个登记 剪贴板 报告中的数据应该能够被复制。

#### 程序链接
在这里，你可以基于数据记录的类型配置从报告中可以转到哪个程序。
自由格式布局
如果你选择 自由格式布局 作为 类型，你可以在标签页中预览报告的布局两者编辑报告。

#### 编辑
在标签页顶部，你会查询按钮 编辑 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_xtrareport_designer.png)。此按钮打开报告编辑器 DevExpress报告设计器 用于创建你的报告。在编辑器中，你可以访问你已添加到报告下的设置 设置 标签页。你你可以访问在 SQL 标签页。
> 要编辑报告，你还必须了解报告设计工具 DevExpress报告设计器。你还可作为从我们的顾问或MONITOR ERP 系统 AB 的支持中心订单报告编辑服务。
选择行
此标签页可用于以下报告 列表类型 盒子。你可以在此确定你在列表类型的选择中包括哪些选择行。你添加选择行并根据以下内容配置。

#### 名称
该文本显示为选择行的名称。使用按钮 翻译 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_translate.png)s 你可以将文本翻译为系统中已登记的不同激活语言。阅读更多内容 [语言管理](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) 用于可翻译文本。

#### 数据库字段
在这里你数据库中用于选择行的表格和列。你还可以输入在 SQL 查询中你的别名。

#### 分组名称
如果你希望将选择行已分组到某个标题下，例如工单或组件，可以在此处输入。

#### 字段类型
数据库字段的类型。你可以在这里选择 文本， 数值， 日期， 或者 日期 + 时间。

#### 分类类型
如果你使用分类，你可以在此处选择一个分类类型。在开始你分类之前，必须第一个在 分类 程序。

#### 默认值：来自
你可以在此处配置默认值 从 选择行的字段。

#### 默认值：
你可以在此处配置默认值 到 选择行的字段。

#### 排除
在这里你可以选择选择行是否应包含 排除 质检由。

#### 选项类型
字段​ 枚举 字段设置为 无。你可以在这里选择 等于 （等式）， 在中间， 或者 包含。
等于 和 包含 仅激活 从 选择行上的字段。在中间 两者 从 和 到 字段。

#### 枚举
你可以在这里为选择行选择预定义的枚举类型的数据。这 无 选项默认被已选择。这意味着否使用预定义的枚举类型。如果你选择任何其它选项，则前面的 选项类型 字段变为未激活。你将在下下一个中选择一个枚举选项类型 选项类型 字段。

#### 查找
字段​ 枚举 字段设置为 无。然后，你可以在此处为选择行上的字段选择一个查找功能。你可以从数据库中可用的查找功能中进行选择。

#### 剪贴板
可用在​​ 查找 字段。然后你可以在这里配置从哪个登记 剪贴板 应该可以待复制到选择行。
设置
在此标签页下，你可以设置报告或子报表配置可选的编号。这些设置显示在你创建的已定制的报告程序中的“选择标签页的底部。

#### 代码
在这里你输入设置的唯一代码。这是你在 SQL 查询中引用的名称。最多你输入50 个字符。

#### 名称
该文本显示为设置的名称。使用按钮 翻译 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_translate.png)s 你可以将文本翻译为系统中已登记的不同激活语言。阅读更多内容 [语言管理](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) 用于可翻译文本。最多你输入100 个字符。

#### 测试值
子报表设置 你可以在此处输入测试值。

#### 类型
报告设置。可以使用的不同类型的设置：复选框、文本字段、整数、小数、日期不带时间、日期带时间、选项 - 登记者和选项。

#### 登记
报告设置。如果你已选择，则你在这里选择登记 选项 - 登记者 在类型下。

#### 单选列表
报告设置。如果你已经选择 选项 在类型单选列表，你可以添加行 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png)。在每个行中你输入内部的名称和名称。然后用户将在单选列表中看到该名称。使用按钮 翻译 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_translate.png)s 你可以将文本翻译为系统中已登记的不同激活语言。阅读更多内容 [语言管理](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) 用于可翻译文本。

#### 默认值
报告设置。你可以在此处输入或配置默认值，取决于已选类型。

#### 宏
报告设置。如果一备选 日期不带时间 或者 日期带时间 已已选择为类型，你可以在此处输入宏。
SQL
在这里你创建一个 SQL 查询。查询的结果也会显示在这里。然后报告将基于此 SQL 查询。

#### SQL 查询
在这里你类型列表类型的SQL 查询。
> 你必须了解数据库中监视器的表、列和别名的名称。你还必须知道如何编写 SQL 才能编写正确的 SQL问好。
通过使用 测试 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 按钮，你可以测试SQL 查询，结果将显示在 结果 盒子。
通过使用 为仓库ID插入占位符 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_warehouses.png) 你插入仓库标识的代码（光标所在的位置）。代码如下 : 周# 标识。
通过使用 为语言 ID 插入占位符 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_url.png) 你插入语言标识的代码（光标所在的位置）。代码如下 :lng#标识。

#### 结果
在这里你可以看到 SQL 查询返回的结果列和行。
在里面 最大结果（行） 字段输入你查询测试运行可能返回的最大行数。
其中一字段返回了有关 SQL 查询测试运行的消息。
