### 更新 Monitor ERP 服务器
Monitor ERP 安装管理器 用于更新软件 Monitor ERP 服务器。服务器桌面上有一个该程序的捷径。
的更新 Monitor ERP 服务器完全自动化。更新所需的时间取决于系统中你多少个数据库以及这些数据库的尺寸。
> 你更新之前请注意以下事项！ 否用户可以登录 Monitor ERP 当你运行更新时！ 如果你安装了 MI、Webshop、WMS 集成或 TimeCard 等选项，你必须根据每个单独选项/产品的指导更新这些选项/产品，连接你 Monitor ERP 服务器。这些选项不通过以下方式已更新 Monitor ERP 安装管理器。 如果 Monitor ERP 服务器安装了 SQL Anywhere，具有单独的数据库服务器，适用以下情况：如果下班部件SQL Anywhere 必须在 Monitor ERP 安装经理，联系人MONITOR支持中心并订单SQL Anywhere 的更新包装。然后你还应该在单独的数据库服务器上更新SQL Anywhere。 如果 Monitor ERP 服务器已安装 Microsoft SQL 服务器，你必须确保在更新你之前你的当前和已更新的备份 Monitor ERP 服务器。 生效日期 Monitor ERP 版本2.44（含），Microsoft . 净值 Framework 4.8 或更高版本必须在您的服务器上安装之前更新 Monitor ERP 可以开始。
安装更新 Monitor ERP 服务器
1.    
开始 Monitor ERP 安装管理器并选择 已安装的版本 标签页。您安装的（当前）版本显示在标签页的顶部。点击按钮 更改版本。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerTab2.png)](../../../Resources/Images/UserGuide/InstallationManagerTab2.png)
2.      
在下一个中，你将查看是否有更新的版本可供下载和安装。如果有多于一的版本需要安装 其它版本，你可以选择最新版本 最新版本。确保该版本与您安装的版本兼容。然后出现绿色检查标记 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/StatusFinished.png) 显示在 兼容性 列。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/UpdateMONITOR.png)](../../../Resources/Images/UserGuide/UpdateMONITOR.png)
如果否更新版本，你将在下方看到当前版本 最新版本 下面为空 其它版本。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/NoUpdateMONITOR.png)](../../../Resources/Images/UserGuide/NoUpdateMONITOR.png)
如果该版本与您安装的版本不兼容，则会显示在 兼容性 带有错误符号的列 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/error.png)。错误符号上的工具提示会让你知道哪些是不兼容的。规则来说，它是你第一个需要更新的部件，例如SQL Anywhere 或文档服务器。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/UpdateMONITORCompabilityIssue.png)](../../../Resources/Images/UserGuide/UpdateMONITORCompabilityIssue.png)
要更新部件，你使用 安装 按钮下方 其它部件。你必须之前完成此操作，然后才能继续更新 Monitor ERP 服务器低于步骤所示，下一个。
3.   
点击 安装 按钮订单安装该版本。你还可以点击按钮 下载 如果你仅下载一个版本。下载之后，会出现一个已填充的复选框，表明该版本已下载。你然后 安装 按钮订单安装该版本。
4.       
当你点击 安装，窗口将显示将要安装的包装。点击 OK 确认并开始安装。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/UpdateMONITORConfirmBackup.png)
从这里开始，更新完全自动化。数据库已迁移至新版本，并制作了备份。点击超链接“[点击这里](DatabaseBackupUpdate.htm)“在对话窗口中，你可以查询迁移和备份是如何下班的。你可以在单独的窗口中看到备份和迁移的过程。
> 请注意，仅数据库位于 SQL Anywhere 上时才可以将数据库复制为备份。如果你有 SQL 服务器上的数据库，则会出现一个对话框通知你必须人工的运行备份。然后，运行数据库备份 微软 SQL服务器管理套件，如果不完成此操作，你在更新之前。然后你在对话框的字段中写入“ 是 ”，订单确认你已进行备份。然后点击 OK 继续更新。
更新已完成后，你将被引导后退标签页 已安装的版本。现在，你可以在标签页的顶部看到你已更新到的版本，即您安装的版本。更新之后，服务器服务开始大约需要 30 到 60秒。
5. 关闭安装管理器。如果你安装了任何选项（可选产品），你单独更新这些选项，请参见低于。
6. 用户可以第一个启动他们的 Monitor ERP 更新已完成之后客户端客户端将在启动时自动更新。
更新选项
如果你安装了MI 、 Webshop、WMS 集成和 TimeCard 等选项，你在更新 Monitor ERP 服务器。
1. 按照有关如何更新每个选项的指导进行操作。
