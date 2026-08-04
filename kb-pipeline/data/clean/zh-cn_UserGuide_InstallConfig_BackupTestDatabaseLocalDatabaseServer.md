## 备份/测试公司拥有独立的数据库服务器
> 当 SQL Anywhere 数据库服务器安装在单独的服务器计算机上与非程序服务器（MONITOR服务器）上时，建议按照此指导备份公司数据库。该指导还建议创建和日程计划复制公司数据库以在单独的服务器计算机上测试公司。在两者案件下，SQL Anywhere备份工具都用于在数据库服务器上运行备份和复制任务。
复制SQL Anywhere备份工具复制到数据库服务器
首先，你必须复制SQL Anywhere备份工具复制到数据库服务器，以便能够在数据库服务器上本地创建和运行备份任务和复制任务。
如果数据库服务器上已有 SQL Anywhere备份工具，检查该备份工具是否与程序服务器（以下简称“MONITOR服务器”）上的版本相同。如果不，则必须一次复制备份工具。
1. 打开 探索者 在MONITOR服务器上的 Windows 中，转到名为 当前日程表图表:\ 程序 文件 (x86)\ MONITOR ERP 系统 AB\ MONITOR安装管理器。
2. 复制名为 SqlAnywhere备份工具 至网络资源或 USB 存储器。
3. 转到根文件夹 当前日程表图表:\ 程序 文件 (x86)\ MONITOR ERP 系统 AB 用于MONITOR服务器。
4. 同时复制文件 认证.rsa 到 SqlAnywhere备份工具 网络资源或 USB 记忆棒上的文件夹。
5. 打开 探索者 在安装了 SQL Anywhere数据库引擎和公司数据库的数据库服务器上的 Windows 中。
6. 复制名为 SqlAnywhere备份工具 从网络资源或 USB 记忆棒复制到数据库服务器上的当前日程表图表 :\。这将创建路径 当前日程表图表:\SqlAnywhere 备份工具。
使用 Windows 中的任务调度器人工的创建和日程表备份
这是在MONITOR服务器上人工的创建和日程计划备份任务的方式。还有另一种创建和日程计划备份任务的方式 Monitor ERP 安装管理器 在MONITOR服务器上 .见低于。
1. 打开 任务调度器 在 Windows 数据库服务器上。
2.    
创建名为的文件夹 MONITORERP系统AB 在下面 任务调度器库 在左侧章节。右键点击 任务调度器库 并选择 新建文件夹... 并将新建文件夹名称。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup1.png)
3.    
当你标记了 MONITORERP系统AB 文件夹，选择 创建基本任务... 在右边章节中 措施。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup2.png)
4.    
在出现的对话框中输入活动的名称和描述。点击 下一个>。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup3.png)
5.    
选择何时运行活动。日常的 是数据库备份的默认和推荐选项。对于复制到测试公司，你可以选择有关你到测试公司频率的选项一。点击 下一个>。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup4.png)
6.    
在开始 你选择日期活动开始的日期和时间。在里面 重复间隔 字段输入你活动重复的频率。当涉及备份时，建议每天运行该活动。当复制到测试公司时，你可以输入您选择的任何间隔。点击 下一个>。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup5.png)
7.    
选择 开始程序 进行活动。点击 下一个>。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup6.png)
8. 点击 浏览... 按钮并选择 MONITOR.SqlAnywhere.BackupTool.exe 文件夹中的文件名为 SqlAnywhere备份工具。
9. 在里面 添加参数 你需要根据字段添加参数 [以下例如](ArgumentsSQLAnywhereBackupTool.htm)。
10.    
离开 开始于 空的。点击 下一个>。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup7.png)
11.    
激活 单击“完成”时打开此任务的“属性”对话框 复选框。点击 完成。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup8.png)
12.    
点击 更改用户或组... 在打开的对话框中单击按钮，然后输入将运行该活动的Windows账户。它通常与运行MONITOR服务器服务的科目或管理科目相同。同时激活 无论用户或不运行 和 以最高权限运行 设置。点击 设置 标签页。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup9.png)
13.    
激活设置 错过已排程的开始之后尽快运行任务。然后点击 OK。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup10.png)
14.    
最后，将显示此窗口，你必须在其中输入将运行该活动的Windows账户的密码。然后点击 OK。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup11.png)
使用以下方式创建并日程表备份 Monitor ERP 安装管理器
这是使用以下方式创建和日程计划备份任务的方法 Monitor ERP 安装管理器 然后导出 到MONITOR服务器服务器.
1. 按照标题下的指导进行操作 复制SQL Anywhere备份工具复制到数据库服务器，如果不完成此操作。
2. 然后按照本章节中的指导进行操作 [创建并日程表备份](CreateScheduleBackup.htm)。
3. 现在将已导出备份任务订单复制到数据库服务器。打开 任务调度器 在MONITOR服务器的 Windows 中。
4. 选择文件夹 任务调度器 任务已保存的位置，通常 MONITORERP系统AB。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup1.png)
5.    
文件夹中的任务显示在右边的框中。选择需要已导出的任务。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup12.png)
6.    
选择 导出... 然后将备份任务作为 XML文件保存在磁盘上。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup15.png)
7.   
如果还有更多备份任务需要已导出，请对这些任务重复上面步骤5-6。
8. 请注意！然后删除备份任务 任务调度器 在MONITOR服务器上 .这很重要，订单然后否一可以从MONITOR服务器触发器备份运行。
9. 将已导出的XML文件复制到数据库服务器上的任意文件夹。
10. 备份任务现在将被已导入到数据库服务器。打开 任务调度器 在 Windows 数据库服务器上。
11.    
创建名为的文件夹 MONITORERP系统AB 在下面 任务调度器库 在左侧章节。右键点击 任务调度器库 并选择 新建文件夹... 并将新建文件夹名称。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup1.png)
12.    
选择文件夹，然后选择 导入任务... 在最右边的盒子里。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup16.png)
13. 案件在MONITOR服务器上的安装管理器中设置了通过网络运行到数据库服务器的备份任务，你必须将备份任务中的 UNC文件路径替换为本地文件路径。这是在 添加参数 字段（参见上面第 9 点，标题下 使用 Windows 中的任务调度器人工的创建和日程表备份）。
14. 还检查该字段中的其它参数 添加参数 在备份任务中。然后，你可以添加在运行备份任务时是否发送电子邮件以及何时已发送Email的参数。请参阅以下内容 [章节](ArgumentsSQLAnywhereBackupTool.htm) 根据可用的论据。
创建并日程表复制以测试公司 Monitor ERP 安装管理器
公司你任务单独的数据库服务器第一个，公司测试总是复制 Monitor ERP 安装管理器 在MONITOR服务器上，然后已导出到数据库服务器。这是为了确保在系统的配置文件中为每个测试公司已创建一条记录。
1. 按照标题下的指导进行操作 复制SQL Anywhere备份工具复制到数据库服务器，如果不完成此操作。
2. 然后按照本章节中的指导进行操作 [创建测试数据库](CreateTestDatabases.htm)。
3. 然后，按照上面标题下步骤3-4 中的指导进行操作 使用以下方式创建并日程表备份 Monitor ERP 安装管理器）。
使用 Windows 中的任务调度器人工的运行备份或复制任务
如果你已创建了不已排程的备份任务或复制任务，或者你一人工的运行该任务，时间你运行 任务调度器 在数据库服务器上。
1. 使用以下方式将远程桌面连接到数据库服务器 远程桌面连接 在 Windows 中，或用于远程连接的等效程序。
2. 按照标题下步骤1-2 中的指导进行操作 使用 Windows 中的任务调度器更改备份或复制任务。
3.    
然后选择 运行 对于最右边框中已选择的任务。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup18.png)
使用 Windows 中的任务调度器更改备份或复制任务
如果你稍后需要更改备份任务或复制任务，你仓储费用 任务调度器 在数据库服务器上。
1.    
选择文件夹 任务调度器 任务已保存的位置，通常 MONITORERP系统AB。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup1.png)
2.    
文件夹中的任务显示在右边的框中。选择相关任务。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup12.png)
3.    
然后选择 属性 在最右边的框中已选择任务。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup13.png)
4.   
在显示的对话框中对任务进行变更，然后单击 OK 保存。
使用 Windows 中的任务调度器删除备份或复制任务
如果你稍后需要删除备份任务或复制任务，你仓储费用 任务调度器 在数据库服务器上。
1.   
按照标题下步骤1-2 中的指导进行操作 使用 Windows 中的任务调度器更改备份或复制任务。
2.    
然后选择 删除 在最右边的框中已选择任务。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup14.png)
3.    
选择 是的 在显示的对话框中删除该任务。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLAnywhereBackup17.png)
