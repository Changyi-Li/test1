## MONITOR安装管理器
安装时 Monitor ERP 第一个服务器，该程序 Monitor ERP 安装经理 也已安装，并且在计算机桌面上已创建了该程序的捷径。
安装管理器是一个程序，管理员可以通过它下载和安装更新和其它部件 Monitor ERP。该程序还用于激活其他公司数据库。安装管理器还会检查已安装的选项和定制包是否在兼容版本中可用，之前你才能更新 Monitor ERP。如果 Monitor ERP 服务器为SQL Anywhere进行了安装，然后安装管理器还用于创建备份任务和测试公司。
安装管理器自动连接到提供新建更新包装的 Monitor分配服务器。
第一个时间你安装管理器时，会显示一个地区，你需要选择您的 Monitor ERP 服务器已安装。你可以在中间 欧洲 和 中国。这些地区有分配服务器。如果服务器位于中国，则应已选择中国地区选项，订单提高更新时的性能。应已选择欧洲地区来涵盖欧洲和世界剩余地区。随后可以在安装管理器中更改地区。然后应在 设置 标签页。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerChooseRegion.png)
安装管理器是自我更新的。这意味着当安装管理器的新建版本已释放时，程序将在启动时自动更新。你正在运行的程序的版本显示在标题堆的顶部。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerVersion.png)
安装管理器的功能低于所述。
> 安装管理器通过 TCP端口443 与分配服务器通信。该端口必须对防火墙的出站流量打开。否则，你选择地区的对话框中会显示一条错误消息。分配服务器的 DNS 名称是 cdn-eur-01.monitorerp.com 和 cdn-chn-01.monitorerp.cn。
扫描更新
在下面 开始 标签页，将检查系统是否有可用更新。你安装管理器已开始，此检查会人工的进行，但你也可以开始 扫描更新 按钮。此类更新可以是，例如，由以下机构向您的系统已交货的附加许可或新公司： Monitor ERP 系统有限公司。必须在这里已激活一家新公司。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerTab1.png)](../../../Resources/Images/UserGuide/InstallationManagerTab1.png)
> 此更新检查/扫描针对 Monitor 的分配服务器日自动运行一次。通常情况下，管理员不人工的执行此操作。你还可以使用以下方法强制检查/扫描更新 同步 Windows客户端后台的按钮 Monitor ERP。这可以由具有角色的用户完成 ERP 经理。
更新 Monitor ERP 和部件
在标签页下 已安装的版本 你将看到当前安装的版本 Monitor ERP。在这里你更新 Monitor ERP 通过 更改版本 按钮。在此标签页下，你还可以通过按钮安装和更新系统中的其它部件 安装 和 更改版本 在本章节中 其它部件。在每个已安装的部件下一个，你可以看到当前版本。如果不安装部件，则会显示 不安装。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerTab2.png)](../../../Resources/Images/UserGuide/InstallationManagerTab2.png)
你更新 Monitor ERP 或以同样的方式添加部件。阅读更多如何更新 Monitor ERP 在里面 话题[更新 Monitor ERP 服务器](UpdateMONITOR.htm)。
创建并复制测试数据库
> 这适用于 Monitor ERP 已为 SQL Anywhere 安装服务器。
在下面 测试数据库 标签页你可以创建测试数据库和复制任务。当创建测试数据库或创建复制任务时，可以激活实际的数据库到测试数据库的已排程复制。你可以从这里人工的运行复制任务。对于已排程的复制任务，你可以更新日程计划，该计划已保存在 任务调度器 在 Windows 中。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerTab3.png)](../../../Resources/Images/UserGuide/InstallationManagerTab3.png)
阅读更多内容 [创建测试数据库](CreateTestDatabases.htm) 话题。
管理数据库备份
> 这适用于 Monitor ERP 已为 SQL Anywhere 安装服务器。
在下面 备份 标签页你可以为实际的（生产）数据库创建和日程表备份任务。你还可以在此处修改备份任务。当需要时，也可以人工的开始备份。对于已排程的备份任务，你可以更新日程计划，该计划已保存在 任务调度器 在 Windows 中。对于已运行的备份任务，你可以看到每个运行之后已更新的日志。标签页底部还有全部备份任务的通用备份设置。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerTab4.png)](../../../Resources/Images/UserGuide/InstallationManagerTab4.png)
在下面 设置 标签页，你可以配置 备份文件的标准路径。已创建新建的备份任务时，标准路径将用作默认备份文件夹。请注意！对于全部备份任务，都可以更改备份文件夹的路径。这将应用于特定的备份任务。
阅读更多内容 [创建并日程表备份](CreateScheduleBackup.htm) 话题。
设置
在下面 设置 标签页你可以更改安装管理器的地区。点击 更改 你可以选择的按钮 欧洲 或者 中国。
你可以输入 备份文件的标准路径 这里。这适用于 Monitor ERP 已为 SQL Anywhere 安装服务器。默认标准路径为“当前日程表图表:\ProgramData\ MONITOR ERP 系统 G5\DatabaseBackup”。
你还可以输入 备份日志的标准路径。这也应用至SQL Anywhere。默认标准路径为“当前日程表图表:\ 程序 文件 (x86)\ MONITOR ERP 系统 AB\ MONITOR 安装 Manager\SqlAnywhereBackupTool\ 日志”。
你可以同步系统配置与 同步 按钮。Windows客户端后台也可用同样的功能 Monitor ERP。查看 [同步系统](SynchronizeSystem.htm) 话题。
[![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerTab5.png)](../../../Resources/Images/UserGuide/InstallationManagerTab5.png)
登录用户
在下面 登录用户 标签页你可以看到此刻哪些用户已登录系统。这应用至你所在的公司。根据 选择数据库 你选择要查看哪些数据库的登录用户。默认下，全部数据库均被已选择。点击 发送通知 按钮 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_information.png) 你可以向登录用户发送通知，例如，如果你需要重启您的 Monitor ERP 服务器。如果用户在重启之前不退出，他/她将失去与服务器的连接。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/InstallationManagerTab7.png)
