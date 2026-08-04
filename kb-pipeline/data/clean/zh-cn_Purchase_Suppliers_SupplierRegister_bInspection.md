### 质检
在此框中决定是否应对供应商采购订单上的组件应用收货质检。

#### 收货质检
使用此复选框，您可以确定是否应用收货质检。可使用以下选项：
- 否 - 不应用收货检验。
- 是 - 应用收货检验。
-    
间隔 - 将应用可变收货检验。可通过字段旁边的质检设定按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png)（见下文）进行配置。
“质检设定”按钮
如果接收质检设置为间隔，则此按钮可用。可在此处配置有关变量接收质检的设置。这是通过选择质检模板来完成的。质检模板必须首先在基本数据表 - SRM程序中登记。
质检模板用于在不同情况下触发接收质检，例如：采购订单上的组件已进行新的修改，已登记一个案件，或以前的接收质检导致拒收。
在对话窗口中可看到质检模板的所有设置。层级显示质检模板当前的质检级别。可通过![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add.png)和![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_reject.png)按钮提高/降低质检模板中的当前级别。可在质检模板中看到每个级别的设置。可查看供应商对组件执行的质检次数。通过按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_refresh.png)可将执行的质检次数重置为 0。如选择了检查模板，频率值将从模板的第一行加载。这无法更新。当达到模板中的下一个级别时，将从质检模板加载该值。
> 在基本数据表 - 组件或基本数据表 - SRM中对质检模板所做的更改不会影响已经分配了相关质检模板的组件或供应商。

#### 自
如接收检验设置为是或间隔，则此字段可用并建议今天的日期。可在此处选择应为供应商申请接收检验的日期。

#### 至
如接收质检设置为是或间隔，则此按钮可用。可在此选择一个日期，到何时应对供应商报告的到货组件应用接收质检。

#### 指导
如接收质检设置为是或间隔，则此按钮可用。可在此处输入有关接收质检的指导。您在此处输入的文本将显示给执行质检的人员。如果您取消了收货质检，然后再次将其激活，则说明仍然存在。
单击此按钮，你访问文本编辑器，你可以在其中编写和格式文本、插入图像和签名以及超链接等。当有评论/文本时，按钮上的符号将从空的气泡更改 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_no_comment.png) 到已填满的对话泡泡 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_comment.png)。

#### 文件
如接收质检设置为是或间隔，则此按钮可用。
通过单击文件按钮![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_file_link.png)，可以链接与相关记录的评论或指导相关的不同文件。当设置自动打印输出激活时，您可选择自动打印链接文件。阅读有关如何链接文件、自动打印输出以及可以在何处自动打印链接文件的[通用功能](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles)主题以获得更多信息。若有链接文件，您将在按钮上看到此符号![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_file_linked.png)
您在此处链接的文件可以是与接受质检有关的检查清单或测量记录，并可向执行质检的人显示。如在链接文件时选中自动打印框，则在保存到货报告时将自动打印该文件。这样，可以在下一步（即接收质检）中使用打印输出。如果您禁用收货质检然后再次将其激活，则链接的文件仍然可用。
支持直接查看 PDF 文件。使用扩展文件阅读器可选功能，您可以查看/显示更多的文件类型，例如不同的图纸格式和Office格式。通过单击此链接，您可以访问[支持文件格式](https://www.rasterex.com/file-formats?hsCtaTracking=f7142bf7-4cfa-4c3b-8be8-cde24df7f2b4%7Cdae7ecbb-26b0-43cd-b9d0-3579248ec31b)的完整列表。
