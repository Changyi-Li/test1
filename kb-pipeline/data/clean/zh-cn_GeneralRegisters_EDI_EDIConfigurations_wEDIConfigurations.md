## EDI 配置
在此程序中，你创建EDI 配置。一个配置必须至少包含一渠道和至少一已链接行为。配置还可以由多个不同的渠道组成，每个渠道具有一或多个已链接行为。
一个配置不能由多个相同的渠道组成，并且同一个渠道不能链接至多个不同的配置。
在你开始配置之前，你必须在 [EDI 渠道](../EDIChannels/wEDIChannels.htm) 和 [EDI 行为](../EDIBehaviors/wEDIBehaviors.htm) 程序。
使用按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_refresh.png) 在过程的工具栏上，你可以重载数据，而无需关闭并重启程序。目的是更新自你打开程序以来是否已添加了新建的渠道或行为。
检查以确保已添加到配置的渠道在 EDI 渠道 程序。如果在此处你渠道设置为激活频道，然后警告 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/warning.png) 出現。在这种案件下，你无法将配置配置为激活。
这里进行的另一项检查是确保在同一渠道配置中已链接的行为不包含相同的客户或供应商。然后出现警告 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/warning.png) 出现 并且配置无法设置为激活。
还会进行检查以确保客户或供应商未通过另一个EDI 配置未链接至同一事务类型（格式）。如果仓储费用，则会出现警告 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/warning.png)。如果你然后将EDI 配置为激活，则会显示一条错误消息 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/error.png) 显示的是配置以及冲突的配置。
在EDI 配置为激活之前，你无法在 EDI 流中的配置中查看或运行包含的激活渠道 管理 EDI 事务 程序。如果配置中的激活渠道与日程表相链接，则配置为激活后，EDI 流程就会根据日程表自动运行。
