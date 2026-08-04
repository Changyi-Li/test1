# 安装 Monitor ERP Windows客户端
本指导介绍了首次安装Windows客户端 Monitor ERP。

## 准备工作
1. 生效日期 Monitor ERP 版本2.44（含），Microsoft . 净值 Framework 4.8 或更新版本必须安装在计算机上。安装程序将在安装之前安装/更新到此版本 Monitor ERP 开始。自 24.3版本释放以来， Monitor ERP 将否工作于搭载 32 位 Windows 操作系统的计算机（客户端）。这意味着你要么将系统升级到Windows 64位，要么变更为具有Windows 64位系统的计算机。
2. 你安装之前，开始关闭全部其它程序。
3. 打开MONITOR服务器上的共享文件夹，或网络上存放安装文件的文件夹 MONITOR客户端准备.exe 和许可证文件 MONITOR认证- [您的系统名称].rsa 被存储。
4. 将许可证文件复制到将要安装客户端的计算机。在安装中，它必须位于计算机本地。

## 安装描述：
1. 使用该文件开始客户端安装 MONITOR客户端准备.exe。
2. 如果窗口 用户科目控制 然后会显示你应该允许安装在您的计算机上进行变更。点击 是的 在那个窗口中。
3.     
窗口 MONITOR客户端安装 将打开，然后你可以在中间：
- 快递安装 – 这是使用默认设置在用户计算机上安装客户端的默认选项。如果你选择此选项 你第跳过事项 你安装之后。
-    
定制安装 – 使用此选项可以在安装过程中配置的可能性不同的设置。如果你此选项，已开始你你安装之后继续低于。
> 如果客户端安装在 终端服务器 你应该选择选项 定制安装。
点击 下一个 开始安装。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall1.png)
4. 你应该点击这里 ... 并选择许可证文件 MONITOR认证- [您的系统名称].rsa 在已保存它的计算机上的本地文件夹中。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall2.png)
5. 点击 下一个 你许可证文件之后。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall3.png)
6. 在这里你可以选择使用哪个服务器。默认是在网络中自动查找程序服务器（MONITOR服务器），这是推荐的方式（通信通过 UPD端口8002 进行）。如果搜索时你不程序服务器，请选择人工的输入服务器地址的查询。在这种案件下，在字段中输入程序服务器的 DNS名称或IP 地址。然后点击 标签页 键盘上的确认。然后点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall4.png)
7. 在此处选择程序服务器，然后单击 下一个。如果一多于服务器，你选择此 Windows客户端应连接的服务器。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall5.png)
8. 在这里你可以选择安装 Windows客户端的路径。
如果在用户电脑上你，建议你安装在默认路径下。
如果你安装在 终端服务器 建议你将其安装在当前日程表图表 : 下的文件夹中，或者安装在终端服务器上不同单位下的文件夹中，例如当前日程表图表:\ MONITOR。然后你输入 当前日程表图表:\MONITOR 作为路径。然后点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall6.png)
9. 现在你可以确认安装。如果你后悔现在做出的选择，可以后退 后退 按钮。但如果一切OK你应该点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall7.png)
10. 现在将开始安装，这将花费大约一分钟。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall8.png)
11. 最后，完成你安装 完成。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientInstall9.png)
捷径 Monitor ERP 现在在计算机桌面和开始菜单上已创建。此捷径是你开始该程序的方式。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientShortcut.png)

### 默认公司或用户
可选的。可以选择哪个公司或哪个用户应总是为默认 Monitor ERP 通过计算机上上面的捷径已开始。你按照低于的说明在捷径方式的属性中配置。
1. 右键单击捷径方式 Monitor ERP 并选择 属性。
2. 在里面 目标 下的字段 捷径 标签页，你添加 当前日程表图表=[数据库编号] 配置默认公司或 U=用户[名称] 配置默认用户。你可以添加两者公司和默认默认。请参见低于图片中的例如。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/DefaultCompanyUserShortcut.png)

### 终端服务器安装之后的特别措施
- 复制上面捷径 Monitor ERP 到 当前日程表图表:\用户\公开\桌面。
（用户应该通过这个捷径来开始该程序。）
建议用户 Monitor ERP Windows客户端在终端服务器上的程序文件夹（例如当前日程表图表:\ MONITOR ）中被赋予写许可。但是，如果为该程序文件夹中的用户已配置了只读（例如由于 IT 政策），然后你还应该执行以下操作：
1. 右键单击用户的捷径 Monitor ERP 并点击 属性。
2. 在里面 目标 你字段​ .无检查 程序文件的名称“MONITOR ”中的文本，结果名称客户端“ MONITOR ”。
（该程序文件不更新客户端。）
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONClientShortcut2.png)
> 请注意！如果用户运行该程序文件 MONITOR.客户端.NoCheck.exe 并且程序服务器（MONITOR服务器）更新之后MONITOR客户端有更新，管理员必须第一个使用捷径开始客户端 “MONITOR.客户端.exe” （安装中已创建的捷径）。这确保客户端将在终端服务器上进行已更新。每个你程序服务器时间、用户在终端服务器上开始客户端之前更新执行此操作。
> 阅读更多内容 Monitor ERP 在指南中 已开始 Monitor ERP 或在线帮助功能。
