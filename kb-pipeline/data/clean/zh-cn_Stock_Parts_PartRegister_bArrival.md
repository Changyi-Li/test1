### 到货
在此框中你可以选择是否用于组件使用到货质检，并且你可以视图到货日志和质检报告。

#### 到货质检
在这里你可以确定是否应对该组件应用到货质检。有以下选项可用：
- 否 –不应用到货质检。
- 是的 – 该组件将应用到货质检。
-    
间隔 – 该组件将应用变量到货质检。你通过以下方式配置设置 质检设定 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) （见低于）位于字段下一个。
质检设定按钮
如果 到货质检 被设定为 间隔，此按钮变为可用。你可以在这里配置有关变量到货质检的设置。这是通过选择一个 质检模板。第一个已创建在 基本数据表 - 组件 程序。
质检模板用于在不同情况下触发器到货质检，例如，当组件有了新版本时、当为组件已登记了案件时、或者当前道的接收检验导致拒收时。
在对话窗口中，你可以看到质检模板的全部设置。层级 显示质检模板的当前质检层级。通过使用 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add.png) 和 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_reject.png) 按钮你步骤/步骤质检模板中的当前层级。你可以在质检模板中看到每个层级的设置。你可以查看该组件已执行检查的编号。通过使用此按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_refresh.png) 你可以将已执行的检查编号重置为 0.00。如果已选择了质检模板，值 频率 从模板中的第一行加载。这无法已更新。当达到模板中的下一个层级时，将从质检模板中加载值。
> 对质检模板所做的变更 基本数据表 - 组件 或者 基本数据表 - SRM，不影响已经已分配相关质检模板的组件或供应商。

#### 从
如果 到货质检 被设定为 是的 或者 间隔，此字段将变为可用，并已建议今天的日期。你可以在这里选择该组件的应用到货质检日期自。

#### 到
如果 到货质检 被设定为 是的 或者 间隔，该字段变为可用。你可以在这里选择该组件应用到货质检的日期至。

#### 指导
如果 到货质检 被设定为 是的 或者 间隔，此按钮变为可用。你在此输入有关到货质检的指导。你在此处输入的文本将显示给执行质检的员工。如果你停用到货质检，然后再次激活它，该指导仍然有效。
单击此按钮，你访问文本编辑器，你可以在其中编写和格式文本、插入图像和签名以及超链接等。当有评论/文本时，按钮上的符号将从空的气泡更改 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_no_comment.png) 到已填满的对话泡泡 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_comment.png)。

#### 文件
如果 到货质检 被设定为 是的 或者 间隔，此按钮变为可用。
通过单击文件按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_file_link.png)，可以链接与相关记录的评论或指导相关的不同文件。当设置自动打印输出激活时，您可选择自动打印链接文件。阅读有关如何链接文件、自动打印输出以及可以在何处自动打印链接文件的[通用功能](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles)主题以获得更多信息。若有链接文件，您将在按钮上看到此符号![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_file_linked.png)
如果已激活了到货质检，你可以在此处链接外部文件，例如质检文档。如果你更改到货质检或将其关并稍后重新激活，则已链接文档剩余
支持直接查看 PDF 文件。使用扩展文件阅读器可选功能，您可以查看/显示更多的文件类型，例如不同的图纸格式和Office格式。通过单击此链接，您可以访问[支持文件格式](https://www.rasterex.com/file-formats?hsCtaTracking=f7142bf7-4cfa-4c3b-8be8-cde24df7f2b4%7Cdae7ecbb-26b0-43cd-b9d0-3579248ec31b)的完整列表。

#### 到货日志
通过单击此按钮，你可以查看该组件采购订单的到货已报告。

#### 质检报告
通过单击此按钮，你可以看到有关在到货报告组件采购订单时的到货质检期间所做的质检报告的信息。在你按钮时打开的对话框中，你还可以转到 报告测量数据 - 采购 已加载已选择的质检报告。

#### 测量计划
点击 测量计划 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 你可以为组件创建测量计划订单在接收检验时执行控制测量。在测量计划中，你添加一或多个测量模板。每个测量模板包含一个测量表格。模板和表格应第一个在 测量模板 - 采购 和 测量表格 - 采购 程序。
