# 安装 Monitor ERP 服务器
本指导概述了MONITOR MQ 的首次安装 Monitor ERP。在安装过程中， Monitor ERP 将安装服务器（程序服务器）和MONITOR安装管理器。

## 准备工作
> 如果你无法自行安装， MONITOR支持中心将为您提供安装帮助 Monitor ERP，以固定价格。然后周三将创建一个远程控制会话并执行安装。远程控制会话的程序可以从我们的网址下载 [https://www.monitorerp.com/mos](https://www.monitor.se/mos/)。
1. 生效日期 Monitor ERP 版本2.44（含），Microsoft . 净值 Framework 4.8 或更新版本必须安装在计算机上。安装程序将在安装之前安装/更新到此版本 Monitor ERP 开始。自 24.3版本释放以来， Monitor ERP 将否工作于搭载 32 位 Windows 操作系统的计算机（客户端）。这意味着你要么将系统升级到Windows 64位，要么变更为具有Windows 64位系统的计算机。
2. 如果 Monitor ERP 对于 Microsoft SQL 服务器应安装，服务器必须已经安装，无论是在本地服务器还是在网络上的服务器上。你需要有权访问有关服务器的信息，以及安装期间要使用的科目 Monitor ERP 服务器。该科目必须具有 SQL 服务器中的服务器角色“sysadmin”。
3. 保存附加的 ZIP文件– MONITOR.zip – 以及许可证 MONITOR认证- [您的系统名称].rsa，Email已收到你在 Monitor ERP 系统有限公司，位于要安装程序服务器（MONITOR服务器）的服务器计算机上的文件夹中。许可证文件对于您的 Monitor ERP 系统。它可以在未来新建安装的服务器和客户端中再次使用。
4. 解压缩 ZIP文件。在该文件中，你查询安装文件 MONITOR服务器准备- 欧盟.exe 和 MONITOR服务器准备- CN.exe （对于服务器）和 MONITOR客户端准备.exe （对于客户而言）。名称中带有“ 欧盟 ”的文件适用于中国境外的安装。名称中带有“CN”的文件适用于在中国安装。
5. 然后，在MONITOR服务器上共享该文件夹，仓储费用可以从要安装客户端的计算机访问该文件夹。或者，你可以复制客户端的许可证文件和安装文件 MONITOR客户端准备.exe 到网络上的共享文件夹。
6. 你安装之前，开始关闭全部其它程序。
7. 继续读取​ 安装描述。
> 将许可证文件保存为备份，以供未来的新建安装（如果有）使用。 你不需要保存服务器和客户端的安装文件。当你将服务器已更新到较新的版本（通过与服务器一起安装的安装管理器）后，这些内容将在一段时间之后日期下班。 如果你稍后需要服务器的新建安装文件，你可以从MONITOR支持中心订单当前版本的文件。客户端的安装文件位于你版本的当前夹中，名为 MONITORERP系统AB\ MONITOR服务器 在路径中 Monitor ERP 已安装。

## 安装描述：
1. 使用名为的文件开始服务器安装 MONITOR服务器准备- 欧盟.exe。如果服务器位于中国，你使用文件 MONITOR服务器准备- CN.exe。
2. 如果窗口 用户科目控制 然后会显示你应该允许安装在计算机上进行变更。点击 是的 在那个窗口中。
3. 在窗口 MONITOR服务器安装 显示的，点击 下一个 开始安装。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall1.png)
4. 安装程序将首先检查计算机上是否安装了 Microsoft . 净值 Framework，如果需要，则安装/更新到版本 4.8 （下载并安装. 净值 Framework 需要分钟）。安装已完成安装 Monitor ERP 服务器继续。
5. 下一个，你应该点击按钮 ... 并选择许可证文件 MONITOR认证- [您的系统名称].rsa。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall2.png)
6. 然后点击 下一个 你许可证文件之后。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall3.png)
7.    
在此步骤中，你可以选择是否应已创建新建的环境/设置或者是否应安装现有的环境。点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall4.png)
> 如果这是你第一个时间安装 Monitor ERP 你选择的服务器 创建新建环境。例如，如果你要将现有的服务器安装移动/重新定位到新建的服务器计算机，你选择 安装现有的环境 选项。
8.    
如果你已选择创建一个新建环境，你在这里选择 生产环境 （实际的公司环境）或 测试环境 应该被已创建。如果你选择安装现有的环境，你仅选择您的 生产 环境。点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall5.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerMove2.png)
> 提示！你仅创建一次生产环境。可以创建多个测试环境。
9. 在下一个中，你安装路径 Monitor ERP 服务器。建议安装在默认路径下。点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall6.png)
10. 在下一个中，你安装数据库的路径。建议安装在默认路径下。点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall6-1.png)
11. 在下一个中，你选择要使用的数据库引擎。你可以选择 SQL无处不在 或者 微软 SQL服务器。如果你选择 SQL无处不在 作为数据库引擎，单击 下一个 并跳过低于的第 14事项。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall6-2.png)
12.      
如果你选择 微软 SQL服务器 你可以配置一个 数据源。输入格式为 [db 服务器]\[instance 名称] 或 [db 服务器],[端口]。
你可以输入 登录 和 密码 在 SQL 服务器中选择一个具有服务器角色“sysadmin”的科目（请参见低于图片阅读更多）。
你还可以选择 使用集成登录 如果你使用服务器上的 Windows科目登录。在这种案件下，你不输入登录和密码。你选择之后，点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall6-3.png)
> 请注意！SQL 服务器中的科目必须已激活服务器角色“sysadmin”，订单在 Monitor ERP 在 SQL 服务器中。该科目仅在安装期间使用 Monitor ERP。
13.    
连接到 SQL 服务器 ，并在以下步骤中输入数据库的登录细节（名称和密码），并使用标准名称和密码进行输入 控制器， 行政， 程序， 和 扩展。数据库名称 系统 和 出价 也以标准名称输入。点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall6-4.png)
> 请注意！如果此 SQL 服务器已在运行或者将要运行其它MONITOR系统，你必须更改SYS 和 BID 的标准登录名称和标准数据库名称。例如，你可以为此MONITOR系统添加前缀。
14.    
在这里你Windows 中应该运行的科目 Monitor ERP 服务器（服务器作为服务安装）。默认的是电脑上登录的科目。你还需要输入账户的密码并确认。自动开始服务也是默认的。你科目密码后，点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall7.png)
> 请注意！输入对你目录具有“完全控制”许可的域管理员科目 Monitor ERP并完全控制文件服务器上的共享目录。
15. 现在你需要确认安装。如果你后悔现在做出的选择，可以后退 后退 按钮。但如果一切OK你应该点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall8.png)
16. 现在将开始安装，此步骤所需的时间可能会有所不同，具体取决于您的互联网宽度。当安装中不同的包装下载完成后，进度堆可以处于停滞状态。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall9.png)
17. 最后，你完成安装 完成。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerInstall10.png)
> 如果安装之后出现你重启计算机的消息，你重启计算机。

### 安装之后激活公司：
安装之后你应该开始该程序 MONITOR安装管理器 并按照低于指导进行操作。该程序的捷径已在服务器计算机的桌面上已创建。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONInstallManagerShortcut.png)
你使用MONITOR安装管理器来激活安装被用于的公司。在激活期间，将为每个公司已创建公司数据库。稍后，当你想安装以下更新时，也你使用安装管理器 Monitor ERP。安装管理器还用于安装和更新其它部件以及激活其他公司。如果你已经安装，你还可以在这里创建测试公司并配置数据库备份 Monitor ERP 用于 SQL Anywhere数据库引擎。
> 你阅读更多在安装 配置 Monitor ERP 或以下 配置 在线帮助功能。
1. 在安装之后你安装管理器已开始 Monitor ERP 服务器，你应该激活其中包含的公司。你在“开始”标签页下执行此操作。确保选中激活复选框，然后单击按钮 激活。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ActivateCompany1.png)
2. 你现在应该选择公司的 国家 / 地区包装 和 公司语言。默认下会为公司已创建一个数据库，但如果你有一个要使用的现有的数据库，你可以取消选中该选项 创建数据库。如果公司数据库适用于 SQL 服务器，你还可以输入 数据库名称 在 SQL 服务器中。如果包含多个公司，你针对每个公司都执行此操作。然后点击 添加。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ActivateCompany2.png)
3. 现在正在已创建公司数据库，这将需要分钟。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ActivateCompany3.png)
4. 已完成后，上面窗口将关闭。确保它看起来如下图片低于，并且显示 已完成的 作为公司行的状态。之后，你可以继续进行安装之后要进行的其它活动，如下低于。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/ActivateCompany4.png)

### 其它活动：
- 安装客户端： 当你想在用户的计算机上安装 Windows文档机时，你应该按照指导 安装 Monitor ERP 客户端。如果你还打算将服务器计算机用作客户端，仅在服务器计算机上安装 Windows客户端。
- 安装网络服务器： 为了 Monitor ERP 有一个网络服务器、一个网络客户端和一个应用程序（适用于 Android 和 IOS）。如果你想使用网页客户端或应用程序， Monitor ERP 还必须第一个安装 Web服务器。然后你应该按照单独文档中的指导进行操作 安装准备 Monitor ERP 网络服务器 和文档 安装 Monitor ERP 网络服务器。使用该应用程序的用户应遵循文档中的指导 安装 Monitor ERP 应用程序。
- 创建备份： 定期运行公司数据库你重要 Monitor ERP。
- 如果你已安装 Monitor ERP 为了 SQL无处不在 数据库引擎：请阅读 配置 Monitor ERP 指南或转到 已开始 - 配置 在在线帮助功能中，阅读如何使用安装管理器创建备份。
- 如果你已安装 Monitor ERP 为了 微软 SQL服务器：公司数据库的备份是在常规的SQL 服务器数据库备份工具中已创建的。
