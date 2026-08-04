# 从 SQL Anywhere 迁移到 SQL 服务器
该指导描述了 Monitor ERP数据库服务器从 SAP SQL Anywhere 到 Microsoft SQL 服务器。

## 要求
Monitor ERP 支持Microsoft SQL 服务器 2017、2019标准版、企业版。
Microsoft SQL 服务器安装由在单独的服务器计算机上，除非你已经现有的服务器可以运行 Monitor ERP 数据库。
您的 SQL 服务器必须具有设置 SQL 服务器和 Windows验证模式 在服务器属性的安全页上已激活。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLServerRequirement.png)
周三建议你在 SQL 服务器中配置与数据库相同的字符集（排序规则）。 Monitor ERP。要选择的国家 / 地区包装取决于您的 Monitor ERP，低于所示 ：
| 国家 / 地区包装 | 排序规则 |
|---|---|
| 瑞典/芬兰 | 芬兰语_瑞典语_100_CI_AS |
| 丹麦 | 丹麦语_格陵兰语_100_CI_AS |
| 挪威 | 挪威语_100_CI_AS |
| 德语 | 德国电话簿_CI_AI |
| 波兰 | 波兰语_100_CI_AS |
| 爱沙尼亚 | 爱沙尼亚语_100_CI_AS |
| 拉脱维亚 | 拉脱维亚语_100_CI_AS |
| 立陶宛 | 立陶宛语_100_CI_AS |
| 俄罗斯 | 西里尔文_通用_CI_AS |
| 其它 | Latin1_General_100_CI_AS |
> 如果你用于的国家/国家 / 地区包装 Monitor ERP 不在上面列出，联系人MONITOR支持中心。

## 选项和定制包 Monitor ERP
> 请注意！如果你有选项或定制包你的 Monitor ERP 系统，这些必须在从 SQL Anywhere 迁移到 SQL 服务器 的过程中单独处理。 例如，选项包括设备集成、网上商店和垂直仓储升降机集成。如果你有选项，联系人MONITOR支持中心： 支持 例如，定制包包括报告、仪表盘和暗箱。你定制包，联系人Monitor 的Adaptation部门Adaptation，并包括您的公司和联系人细节。该部门将后退你报价，并估计完成工作所需的时间。修改现有的定制包以确保其与 SQL 服务器工作产生的成本不定制包更新协议的涵盖范围内。 还环境你在 Monitor ERP 你移动到SQL 服务器 ，然后你测试和核实全部的选项，定制包和日常工作 Monitor ERP。

## 准备工作
你必须第一个修改文件 MonitorCompanyConfiguration.json 在里面 MONITORERP系统AB 文件夹。这通常位于文件路径下的文件夹中 当前日程表图表:\程序文件（x86）\。
在较旧的安装中，文件中的“ConnectionString”属性中仅一个 SQL Anywhere连接。然后必须将连接移动到新建的“ConnectStrings”属性。对于前道的“ConnectString”属性，将值至“null”。请参阅低于例如：
“连接字符串”：空，
“连接字符串”：{
“SqlAnywhere”：“ASTART=否；ENG=MonitorG5_MyServerName”，
},
你必须在 SQL 服务器的“ConnectStrings”下添加行。请参阅低于例如：
“连接字符串”：{
“SqlAnywhere”：“ASTART=否；ENG=MonitorG5_mlse1393”，
"MicrosoftSqlServer": "集成安全=SSPI；数据源=DbServerName,1443"
},
“数据源”的值是您的 SQL 服务器的名称。你可以以 [DbServerName]:[ 端口 ] 或 [DbServerNname]\\[SQLServerInstanceName] 的形式输入名称。在上面的例如中，SQL 服务器监听对端口1443 的连接。

## 创建登录名 Monitor ERP 在 SQL 服务器中
下一个步骤运行该程序 MONITOR.DbConnectionManager.exe 在里面 MONITORERP系统AB\ MONITOR服务器 文件夹，订单创建登录名 Monitor ERP 在 SQL 服务器中。日志该程序时，你必须使用在 SQL 服务器中具有服务器角色“sysadmin”的科目。
开始程序并使用具有此用户权限的科目的用户名和密码登录。
你选择​ 重新生成密码 在顶部，然后 保存。然后，你将生成以下登录所需的密码： Monitor ERP 在 SQL 服务器上。
> 这是一个重要的步骤，因为在创建你 服务器数据库时必须存在这些登录信息。

## 数据库移植
数据库从 SQL Anywhere 移植到 SQL 服务器数据库需要运行以下程序 MONITOR.DatabasePortation.Console.exe 在文件夹中 MONITORERP系统AB\ MONITOR服务器 在程序服务器（MONITOR服务器）上。该程序在控制台窗口中运行。
> 请注意！ 在你数据库之前，端口你确保运行程序MONITOR的数据库和程序服务器（MONITOR服务器）具有相同的版本。这是为了确保数据库中的表和列正确已匹配。 数据库移植期间仅包含数据库中的标准表和列。如果你有选项或定制包你的 Monitor ERP 系统你必须首先联系人MONITOR支持中心或Adaptation部门。参见 选项和定制包 Monitor ERP，细节请参阅上面。 否情况下五月用户或其它程序连接到数据库！如果在数据库移植时已变更或已添加数据，这原因数据库出现问题。
你打开Windows 命令解释器 以管理员身份在上面文件夹中打开 (cmd.exe)，然后根据低于示例输入命令：
端口到 SQL 服务器上名称数据库 001：
MONITOR.DatabasePortation.Console - 当前日程表图表 001
端口到 SQL 服务器上名称Monitor001 的数据库：
MONITOR.DatabasePortation.Console - 当前日程表图表 001 -n Monitor001
将数据库 001端口到 SQL 服务器上名称Monitor001 的数据库，并将临时文件的文件路径设置为 e:\data：
MONITOR.DatabasePortation.Console - 当前日程表图表 001 -n Monitor001 -fe:\data
要查看程序中支持的全部参数，输入命令：
MONITOR.DatabasePortation.Console
你对将要移植到 SQL 服务器 的数据库运行命令。可以运行混合环境，其中某些数据库在 SQL Anywhere 上，某些数据库在 SQL 服务器上。
> 请注意！SYS 数据库也必须以同样的方式移植到 SQL服务器。
在数据库移植期间，来源数据库中的全部标准表都将已导出到临时文件，然后已导入到 SQL 服务器中的目标数据库中。导入之后，所有文件将被自动已删除。因此，数据库移植要求至少有与来源数据库尺寸相同的可用磁盘空间。
在数据库移植期间，全部登录都已链接创建人程序MONITOR创建的目标数据库中。
> 该程序 MONITOR.DatabasePortation.Console.exe 也可以在其它上下文中使用，订单将数据库从 SQL 服务器端口到 SQL Anywhere，或者 [减小尺寸](../../GeneralRegisters/SystemMaintenance/DatabaseAdministration/bChangeBLOBStorageLocation.htm) SQL Anywhere 数据库。

## 连接到 SQL 服务器
现在，你有一个在 SQL 服务器上运行的MONITOR数据库，但是，你需要在文件中进行更改 MonitorCompanyConfiguration.json 订单程序服务器（MONITOR服务器）可以连接到SQL 服务器上的数据库。你必须更改文件中每个已移植到 SQL 服务器 的数据库的“DatabaseName”和“Dialect”。你还必须对 SYS 数据库执行此操作。请参阅低于文件摘录：
"数据库": [
{
“编号”： “SYS”，
...
"数据库名称": "SYSDatabaseNameInSQLServer",
...
“方言”：1，
...
},
{
“编号”：“001”，
...
"数据库名称": "001数据库名称InSQLServer",
...
“方言”：1，
...
现在一切都已完成，你可以开始 Monitor ERP 客户端并测试以确保你可以在移植的数据库中工作 Monitor ERP。
