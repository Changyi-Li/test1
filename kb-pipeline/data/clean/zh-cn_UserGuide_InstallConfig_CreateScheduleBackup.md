### 创建并日程表备份
> 当程序服务器（MONITOR服务器）和 SQL Anywhere 数据库服务器在同一台服务器计算机上运行时（标准安装），此指导适用。Monitor ERP 安装经理 用于创建和日程表公司数据库的备份。 如果要在单独的服务器计算机上运行SQL Anywhere 数据库服务器，请按照此处的指导进行操作： [具有单独数据库服务器的备份/测试公司](BackupTestDatabaseLocalDatabaseServer.htm)。 如果要使用 Microsoft SQL 服务器 ，则在 SQL 服务器上的常规的数据库备份工具中运行公司数据库的备份。
创建备份任务
1.    
转到 备份 在安装管理器中单击标签页 新建备份任务 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_add_row.png)。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/BackupSettingsTab.png)
2.          
在下面 设置 标签页输入你 已排程任务名称。
默认 备份目录 对于新建的备份任务，根据 备份文件的标准路径 在里面 设置 标签页。这是已保存备份文件*的地方。你可以为此备份任务选择不同的备份目录。
默认 备份日志目录 对应于 备份日志的标准路径 在里面 设置 标签页。包含每个备份运行日志的文本文件都已保存在这里。
截断日志文件 （默认）表示在运行备份任务之后，数据库的相关日志文件“MONITOR ”中的事务将已预留。建议进行截断订单尽量减少日志文件的尺寸。
验证备份 表示备份任务运行完成之后，备份文件才会生效。此校验在数据库服务器的单独会话中执行，并检查备份文件不损坏。
仅备份日志文件 表示备份被用于仅包含日志文件“MONITOR ” 。激活此设置的原因五月是你需要非常频繁地运行备份任务（例如小时），因为数据库中在时间进行了许多事务。然后你可以选择仅备份日志文件（可以快速运行备份任务）。如果需要重置，可以使用数据库文件和日志文件的最近常规的备份任务以及此备份任务按按时间排序的全部单独的日志文件来重新创建数据库。
> 请注意！应将仅备份日志文件的备份任务已创建为单独的备份任务。对于此备份任务，必须有一个不已激活此设置的常规的备份任务，例如，每24小时运行1时间。
输入 运行任务时使用以下用户科目。默认下，这是登录到服务器上的 Windows的用户。不过，你可以使用 更改用户 按钮在 Windows 中输入不同的用户。然后你可以输入用户的密码。
3.    
在下面 数据库 标签页你要包括在备份任务中的数据库。这将激活 OK 按钮。通过单击该按钮，你将创建手工备份任务。然后你必须输入用户密码（见低于的第 7 点）。你通过按钮运行手工备份 开始 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_copy_to.png) 在下面 备份 安装管理器中的标签页。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/BackupDatabasesTab.png)
4.       
如果你创建已排程备份任务，转到 日程表 标签页，而不是单击 OK 按钮。你可以在那里创建备份任务的日程计划。你随后使用的替代方案 编辑备份任务 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_edit.png) 在下面 备份 标签页。
在下面 日程表 你激活的标签页 已排程任务。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/BackupScheduleTab.png)
选择 类型。选项包括 周， 月， 和 月末之日。
输入一个 时间 和 天数 或者 月 应在其上执行备份任务。如果 类型 已设置为 月，你还可以选择一个 日期 在应该执行备份任务的月。
5.      
在下面 Email 标签页你配置是否以及连接在运行备份任务时已发送Email。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/BackupEmailTab.png)
配置 发送有关备份的发送 Email 设置。在这里你可以决定是否已发送Email 总是， 发生错误案件， 或者从不。默认选项是 发生错误案件。这意味着仅当备份任务已失败时才会已发送Email。如果你选择 总是，这意味着在执行备份任务案件也会已发送Email。选择 从不 如果你不无论备份任务是否已执行或是否已失败已发送Email，请选项。
配置 Email 设置为 标准 或者 手工的。标准 是默认选项，这将使用接收者和主题的通用Email 设置。如果你选择 手工的，你更改在 到 和 主题 相关备份任务的字段。你多于在​​​ 到 字段。
6.   
点击 OK 在对话框中订单备份任务。然后还会在 Windows 中已创建一个已排程任务 任务调度器。
7.    
最后，你必须输入 密码 为将运行该任务的已选择用户。然后点击 OK。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/TestDatabase7.png)
> *备份文件日志当前数据库文件“MONITOR”和当前数据库日志文件“MONITOR ”的份数。这里还会已创建当前日志文件的额外复制，文件名称中包含今天的日期和时间；“monitorYYYY-MM-DD 日志”。这意味着下一个运行备份任务时间日志文件将从不被覆盖。所有文件都已保存在与实际的（实时）数据库文件夹名称的子文件夹中，例如“001”。 请注意！每个运行备份任务时间，备份文件“MONITOR”和“MONITOR ”都会被覆盖！这就是为什么在备份任务运行之后总是备份整个备份文件夹非常重要。将备份份数保存在保护的库位。
更改已排程备份任务
1. 任务你变更现有的备份任务，你选择 备份 标签页并点击 编辑备份任务 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_edit.png) （如果你标记了备份任务，此按钮已激活）。
2. 在相应的选项卡下进行你想要做的变更 设置、数据库、 日程表， 和 Email，然后点击 OK 按钮。
3. 当你做出已变更时，你还必须将这些变更传输任务 任务调度器 在 Windows 中。这是通过使用 更新已排程任务 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_refresh.png) 在下面 备份 标签页。
通用备份设置
通用备份设置涉及运行备份任务时以及为测试公司复制任务时通过Email已发送的通知。你还可以在此处配置与您的Email服务器通信的设置。你仅配置这些设置一次。这些设置然后默认应用你为测试公司创建的所有的默认备份任务和复制任务。
1. 点击 备份设置... 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_settings.png) 在底部 备份 安装管理器中的标签页。
2.    
在下面 通知 标签页，你可以激活通过Email已发送通知给已在字段中输入的至一或多个接收者。你可以在字段中输入多于Email 地址，用分号（;）分隔。随着 测试Email 按钮你可以发送测试Email给接收者来测试该功能。还可以每备份任务输入通知的接收者/接收者的。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/BackupGlobalSettingsNotifications.png)
> 有关备份任务成功和已失败运行的详细信息已保存在每个备份任务的日志文件中 -你通过以下方式访问此类日志 日志 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_log.png) 在下面 备份 标签页。
3. 在标签页 Email 设置 你配置哪个 服务器 （Email服务器）和 端口 用于通过Email发送通知。你还可以输入 用户名 和 密码 对于有许可通过输入的Email服务器发送 Email的 Windows账户。在里面 发件人地址 在字段输入你Email 地址，该地址将功能通知的发件人。激活 使用 SSL 如果Email服务器需要的话。然后你还应该输入 端口 Email服务器使用 SSL。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/BackupGlobalSettingsEmail.png)
4. 点击 OK 你通用备份设置后，单击 按钮。
