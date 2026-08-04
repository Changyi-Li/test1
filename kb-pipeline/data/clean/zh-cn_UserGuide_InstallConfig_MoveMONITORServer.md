# 重新定位 Monitor ERP 服务器
该指导描述了 Monitor ERP 将带有 SQL Anywhere 的服务器迁移到新建的服务器计算机。

## 准备工作
> 如果你无法自行完成迁移， MONITOR支持中心将为您提供安装帮助 Monitor ERP，持续收费。白天、晚上或周末的价格有所不同。然后周三将创建一个远程控制会话并执行重新定位。远程控制会话的程序可以从我们的网址下载 [https://www.monitorerp.com/mos](https://www.monitor.se/mos/)。
1. 订单服务器迁移包装 Monitor ERP 来自MONITOR支持中心的服务器。此包装包含服务器和客户端的安装文件、认证文件以及指导（例如本指导）。
2. 你包装后，你可以执行安装 Monitor ERP 新建服务器计算机上的服务器，见低于。
3. 首先，确保全部用户都已关闭 Monitor ERP 客户。
4. 然后你应该打开 服务 在旧的服务器计算机上的 Windows 中并关闭该服务 SQL Anywhere — [服务器名称] （用于数据库引擎）。还可以停用该服务，使其无法重启，例如，如果服务器计算机重新启动。要停用，更改 启动类型 的服务来自 自动的 到 未激活。

## 在新建服务器计算机上安装：
1. 根据以下指导开始安装 安装 Monitor ERP 服务器 包含在安装文件中，然后按照初始的项目中的步骤进行操作。
2. 当你到达安装中的第 7事项时，你选择 安装现有的环境。然后点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerMove1.png)
3. 在下一个现有的，你选择 生产 并点击 下一个。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerMove2.png)
4. 应根据以下指导进行步骤 安装 Monitor ERP 服务器。

## 从旧的服务器计算机复制文件：
1. 创建备份​ MonitorCompanyConfiguration.json 在里面 MONITORERP系统AB 新建服务器计算机上的文件夹。你你在安装路径中查询此文件 Monitor ERP 服务器。将备份复制保存在不同的文件夹中。
2. 然后你应该将相同的 json 文件从旧的服务器计算机复制到新建服务器计算机。选择覆盖新建服务器计算机上的现有的文件。
3. 使用文本编辑器在新建服务器计算机上打开该文件并更改 “SqlAnywhere” 服务器名称 “连接字符串” 以及文件路径 “数据库目录” 和 “备份数据库目录”，使它们与新建服务器计算机的服务器名称和路径相对应。请参见低于图片中黄色的高亮部分。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MONServerMove3.png)
4. 关闭服务 SQL Anywhere — [服务器名称] （用于数据库引擎）在新建的服务器计算机上。
5. 复制​ 数据库 文件夹和 数据库备份 文件夹从旧的服务器计算机复制到新建服务器计算机。选择覆盖现有的 数据库 新建服务器计算机上的文件夹。你可以通过在旧的服务器计算机和新建服务器计算机上安装数据库的路径查询这些文件夹。
6. 在新建服务器计算机上开始数据库引擎的服务。
7. 在里面 MONITOR安装管理器 在新建服务器计算机的 Windows 中，你现在应该创建和日程表测试公司的备份任务和复制任务，使这些任务与旧的服务器计算机上的已配置方式相对应。确保你在新建服务器计算机上创建的备份任务中数据库备份文件夹的路径正确。
8. 如果旧的服务器计算机上你包含已链接文件的文件夹，你将这些文件复制到新建服务器计算机。
9. 更新文件路径 路径 程序 Monitor ERP 在新建的服务器计算机上。如果路径指向旧的服务器计算机上的文件夹，则应进行已变更，仓储费用路径转到新建服务器计算机上的相应文件夹。

## 重新安装 Monitor ERP 客户
1. 卸载 Monitor ERP 客户端在用户的计算机上 .
2. 安装 Monitor ERP 文件客户端安装计算机 MONITOR客户端准备.exe。按照指导进行操作 安装 Monitor ERP Windows客户端 在服务器迁移包装中可用。
3. 开始 Monitor ERP客户并确保一切正常。
