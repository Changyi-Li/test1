### 创建测试数据库
Monitor ERP 安装管理器 用于添加公司数据库的份数测试数据库。测试数据库已添加 测试数据库 标签页。它们用于培训目的或不在公司数据库中执行的不同测试。
已增加测试数据库时，配置文件中也会已创建测试数据库的章节 MonitorCompanyConfiguration.json。该文件可以在MONITOR服务器的安装文件夹中找到（通常为当前日程表图表:\ 程序 文件 (x86)\ MONITOR ERP 系统 AB）。
如果有必要，可以用公司数据库替换现有的文本数据库，以获取最近复制到用作测试数据库。
如果数据库位于 SQL Anywhere 上，则可以人工的按钮 复制新建的测试数据库 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_copy_to.png) 在 测试数据库 标签页。还可以通过已排程复制任务定期复制现有的测试数据库。您可以在你测试数据库创建或之后在安装管理器中已配置。
如果数据库位于 SQL 服务器上，则脚本 测试公司复制.sql 用于创建复制任务的已排程运行 微软 SQL服务器管理套件。你应该已经已收到来自 Monitor ERP 系统有限公司。
> 现有用户科目包含在公司数据库中。但是，测试数据库不用户许可，仓储费用你可以自由地在测试数据库中添加其他用户科目。 在测试数据库中，已排程和自动事件将默认激活由，但可以人工的运行。这应用至以下事件：净需求计算、转发审核和通过Email提醒审核（使用 EIM 时）、从Email收件箱负荷（例如在CRM中）、代理任务和监控任务。测试数据库中的搜索索引也将被关。停用和关搜索索引的目的是保存服务器上的系统资源。
添加测试数据库
1. 在安装管理器中，你转到 测试数据库 标签页并点击 新建的测试数据库 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add_row.png)。
2. 在显示的对话框中，选择 公司 在下面 设置 标签页（即你要待复制到测试数据库的公司数据库）。
SQL Anywhere 上的公司数据库：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase1.png)](../../../Resources/Images/UserGuide/TestDatabase1.png)
1. 在选择了 公司，你可以更改 名称 在测试数据库上。默认名称为“测试公司[您的公司名称]”。
2. 决定是否选择 现在复制 应已选择（默认）。这将在已创建公司数据库时将其直接复制到测试数据库。这也可以使用 复制新建的测试数据库 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_copy_to.png) 在下面 测试数据库 标签页。
3. 当。。。的时候 现在复制 设置已已激活，输入 运行任务时使用以下用户科目。默认下，这是在计算机上登录Windows的用户。不过，你可以输入不同的用户 更改用户 按钮。
4. 如果你希望为测试数据库创建已排程复制任务，选择 日程表 标签页并移动低于的第 6 点。
否则，关闭对话框 OK 按钮并已增加测试数据库。现在在配置文件中已创建了测试数据库的章节 MonitorCompanyConfiguration.json。
5. 如果 现在复制 设置已已激活，你现在可以输入 密码 对于被已选择运行该活动的用户（见低于第 12 点）。一个名为“复制新建数据（[测试数据库编号]）”的手工复制任务已已创建并显示在测试数据库下。在 Windows 中 任务调度器 相应的手工任务也被已创建。
6. 在下面 日程表 你激活的标签页 已排程复制 测试数据库。目的是当前获取生产/实际的/实时数据库的副本，然后你将其用作测试数据库。你也可以稍后添加已排程复制任务（请参阅 添加已排程复制任务 低于）。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase2.png)](../../../Resources/Images/UserGuide/TestDatabase2.png)
7. 输入一个 已排程任务名称。
8. 配置 发送有关备份的发送 Email 设置。在这里你可以决定是否已发送Email 总是， 发生错误案件， 或者从不。默认选项是 总是 这意味着复制任务完成后总是已发送Email。如果你选择 发生错误案件 选项，仅当复制任务已失败时才会已发送Email。选择 从不 如果你不无论复制任务是否已执行或是否已失败都已发送Email，请选项。
你配置通用​​​​​ ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 查询你 备份 标签页，这些应用至全部复制任务。
9. 选择 类型。选项包括 周， 月， 和 月末之日。类型 默认设置为 周。
10. 输入一个 时间 和 天数 或者 月 应在其上执行复制任务。如果 类型 已设置为 月，你还可以选择一个 日期 在需要进行复制任务的月。
11. 点击 OK 在对话框中订单数据库。现在在配置文件中已创建了测试数据库的章节 MonitorCompanyConfiguration.json。
12. 最后，你必须输入 密码 为将运行该任务的已选择用户。然后点击 OK 在此对话框中。
然后便会已创建已排程的复制任务，并以你为已排程任务输入的名称显示在测试数据库下。在 Windows 中 任务调度器 相应的已排程任务就已创建好了。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase7.png)
SQL 服务器上的公司数据库：
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabaseMSSQL1.png)](../../../Resources/Images/UserGuide/TestDatabaseMSSQL1.png)
1. 你之后​ 公司，你仅更改 数据库名称 测试数据库应该在 SQL 服务器上具有。默认名称为“MONITOR[företagsdatabasnummer_testdatabasnummer]”。
2. 点击 OK 在对话框中。现在在配置文件中已创建了测试数据库的章节 MonitorCompanyConfiguration.json。
3. 运行脚本 恢复Mssql数据库.sql 在 微软 SQL服务器管理套件 在 SQL 服务器上创建测试数据库。你应该已经已收到来自 Monitor ERP 系统有限公司。
4. 阅读更多 添加已排程复制任务，低于，如果你想要为 SQL 服务器上的测试数据库创建已排程复制任务。
添加已排程复制任务
SQL无处不在
1.    
如果之后你为测试数据库添加已排程复制任务，选择在 测试数据库 标签页并点击 添加已排程复制 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add_subrow.png) （如果你选择测试数据库，此按钮已激活）。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase6.png)](../../../Resources/Images/UserGuide/TestDatabase6.png)
2.    
在相应的选项卡中名称并配置你的复制任务 设置 和 日程表 并点击 OK 按钮。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase3.png)](../../../Resources/Images/UserGuide/TestDatabase3.png)[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase4.png)](../../../Resources/Images/UserGuide/TestDatabase4.png)
SQL服务器
1. 如果你SQL 服务器上的测试数据库添加已排程复制任务，请使用脚本 测试公司复制.sql 并在中创建复制任务的已排程运行 微软 SQL服务器管理套件。你应该已经已收到来自 Monitor ERP 系统有限公司。
添加已排程复制任务
> 如果测试数据库位于 SQL Anywhere 上，则适用此规定。
1.    
复制你更改已排程复制任务，你选择​ 测试数据库 标签页并点击 编辑复制 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_edit.png) （如果你在测试数据库下标记复制任务，则此按钮已激活）。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase5.png)](../../../Resources/Images/UserGuide/TestDatabase5.png)
2.    
在相应的选项卡下进行你想要做的变更 设置、数据库、 日程表， 和 Email，然后点击 OK 按钮。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase3.png)](../../../Resources/Images/UserGuide/TestDatabase3.png) [![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase4.png)](../../../Resources/Images/UserGuide/TestDatabase4.png)
3.   
当你做出已变更时，你还必须将这些变更传输任务 任务调度器 在 Windows 中。这是通过使用 更新已排程任务 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_refresh.png) 在下面 测试数据库 标签页。
> 已登录测试公司的用户将自动下班 Monitor ERP 当复制到测试公司时。了解这一点很有用，特别是当你使用已排程复制时。
