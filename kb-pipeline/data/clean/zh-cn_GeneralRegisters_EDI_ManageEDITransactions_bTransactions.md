### 事务
在上面的表格中 列表 标签页你可以看到全部EDI业务事务。你还可以查看它是否涉及 EDI文件的导入或导出。最新的事务默认置于顶部。
在这里你可以分析 EDI文件的每个事务中的每个步骤。通过状态，你可以查看事务是否 已完成的 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png)， 已更正 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusRegistered.png)，或者如果存在任何错误 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/error.png)。如果事务有错误，则会在符号上的工具提示中显示原因。
通过选中列中的复选框 A 在事务记录（导入）中，你在保存时人工的批准导入。如果你在行为中已配置了应手动批准导入，则会出现该复选框。你还可以检查标题列中的复选框来批准全部事务记录。
对于每个事务记录，你可以使用按钮 日志 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_more_info.png) 查看步骤、事件、细节、时间和层级。
在一些涉及导入的案件下，同一个文件可以包含多于一商业事务。例如，一个导入文件可以包含多于一客户订单。这反映在已导入交易时赋予该事务的两组件号（例如478-1）中。该编号的第一个组件（478）是该文件的事务号，第二组件编号（1）是同一文件内订单的排序编号。如果导入文件包含多于一商业事务（例如多个客户订单），然后每个事务都有单独的排序编号，但文件的事务号相同（例如478-1、478-2 等）。
按钮 开始事务 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 在功能菜单上，重启列表中已选择的事务记录。例如，如果事务正在待产再运行（行为中的导入原则允许组件订单）或者在负荷导入文件时出现问题（然后从发生错误的步骤重新启动事务），这很有用。也可以选择多个事务记录并时间重启。如果事务（导入）已已完成并且你尝试重启它，则会出现一个对话框询问你是否要再次运行该事务。如果要再运行事务（导出），则会出现一个对话框，其中显示以下选项 仅导出 和 再次运行 进行事务。通过使用第一个选项，该文件将仅被再次已导出。通过使用第二种选择，事务将再运行并已导出一个新建文件。
使用按钮 处理错误（描述） ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_edit.png) 你可以处理事务记录中可能发生的任何错误。仅当已选择的事务中存在错误时，此按钮仅处于激活。如果你光标放在按钮上，将出现一个工具提示，告知你错误发生的位置。
使用按钮 转到标签页 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_send_edi.png) 你可以选择在受影响的标签页下视图已选择事务记录的更多详细信息。此按钮应用至导入事务。你也可以双击某个事务以转到受影响的标签页。
使用按钮 删除事务![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_delete.png) （F6）在功能菜单上，你删除已选择的事务记录。也可以时间选择多个事务并删除它们。你也可以选择一事务，右键单击它并选择删除属于同一笔事务的所有记录。阅读更多低于有关删除事务的更多信息。
按钮 复核事务{0} 的文件数据 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_form_viewing.png) （Ctrl+ 班次 +L）显示已选择事务记录中已导入或已导出的EDI文件的目录。这将显示在一个单独的窗口中。
通过使用 保存本地文件 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_export.png) 你可以选择 保存事务文件 订单将属于事务记录的实际的EDI文件保存为 XML文件。你还可以选择 保存日志文件 订单保存属于事务记录的日志记录的 CSV文件。
按钮 通过 Email 发送事务 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_email.png) 创建消息Email，其中附加了 EDI文件和日志文件。这样做的目的是，例如，如果你遇到问题并想将 EDI文件和日志文件发送给您的 EDI 合作伙伴或MONITOR支持中心以进行故障排除。
按钮 查询 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_search.png) （Ctrl + B）在表格上面打开一个搜索字段，你可以在其中对表格中的记录中的信息执行完全符合搜索。该按钮也存在于程序中的其它盒子。
使用按钮 在搜索文件内容 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_validate.png) 你可以在事务文件和日志文件中查找信息。在表格中你可以看到与你搜索的信息匹配的记录。搜索完成之后，该按钮显示为已激活。如果你想更改搜索或重置，请再次单击该按钮。该按钮也存在于程序中的其它盒子。
使用按钮 转到程序 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_link.png) 你可转到已选择的事务记录执行不同的程序。该按钮也存在于其它类型记录程序的其它盒子。
删除事务
当你删除事务时会发生什么？
- 删除你事务，则你删除底层日志记录。如果事务包含文件，不已删除实际的文件。
- 如果你状态为“已完成”的记录（即已已创建的客户订单），删除已创建的订单不受到影响。信息还显示， 在 Monitor的订单不受到影响。
- 只要其它业务事务仍来自同事务，事务记录就不受到影响。
- 若你选择删除最新的或者仅的商业事务，然后该笔事务记录也将被已删除。
