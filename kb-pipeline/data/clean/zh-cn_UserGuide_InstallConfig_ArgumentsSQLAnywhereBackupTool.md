### MONITOR.SqlAnywhere.BackupTool.exe 的参数
1. 标记低于示例一中的全部文本，然后使用 Ctrl + 当前日程表图表复制它。
2. 使用 Ctrl + V 将其粘贴到文本编辑器中，例如 记事本。
3. 编辑标有 黄色​ 在例如中，使其与您的环境相对应。
4. 在文本编辑器中标记全部文本，然后使用 Ctrl + 当前日程表图表再次复制。
5. 使用 Ctrl + V 将文本粘贴到安装指导中步骤9 中描述的参数字段中 [在单独的数据库服务器上本地备份/测试公司](BackupTestDatabaseLocalDatabaseServer.htm)。

#### 例如1：公司数据库备份
-d 当前日程表图表:\数据库 -s SQLANYs_MonitorG5_Server1 --dbn 001,002,003 -o 当前日程表图表:\数据库备份 -n 当前日程表图表:\DatabaseBackup\{yyyy-MM-dd} 日志 提醒 ——ms 你的.smtp服务器 --主组件 二十五 --md 发件人名称 --mn BackupSender@yourcompany.com - 亩 Smtp用户名 --兆瓦 当前日程表图表:\某处\pwd.txt - 先生 BackupRecipient1@yourcompany.com,BackupRecipient2@yourcompany.com --mb 邮件主题 --mt 0

#### 例如2：复制到测试公司
-d “当前日程表图表:\ProgramData\MONITORERP系统G5\Databases“-s” 数据库服务器名称 --dbn 001 -t 001_1 -o”当前日程表图表:\ProgramData\MONITORERP系统G5\Databases“ -n ”当前日程表图表:\ProgramData\MONITORERP系统G5\Databases\001_1\{yyyy-MM-dd} 日志“提醒 --ms 你的.smtp服务器 --主组件 二十五 --md 发件人名称 --mn BackupSender@yourcompany.com - 亩 Smtp用户名 --兆瓦 当前日程表图表:\某处\pwd.txt - 先生 收件人1@yourcompany.com,收件人2@yourcompany.com --mb 邮件主题 --mt 0
> 请注意！在参数中，如果值包含空格，则你使用“”将其括起来。

#### 全部论点的解释（英语）
| 选项 | 必选/可选 | 描述 | 例如 |
|---|---|---|---|
| -d “数据库路径” | 必需的 | 提供要备份的文件或数据库的根路径。 | -d 当前日程表图表:\数据库 |
| -s “服务器名称” | 必需的 | SQL Anywhere 数据库服务器的服务名称。 | -s SQLANYs_MonitorG5_Server1 |
| --dbn “数据库名称” | 必需的 | 以逗号分隔的数据库名称列表。 | --dbn 001,002,003 |
| -o“输出路径” | 必需的 | 放置备份的文件夹根路径。 | -o “当前日程表图表:\数据库备份” |
| -n “logPath{日期时间格式}” | 可选的 | 备份错误日志。 如果无指定，然后使用可执行文件的库位。 提供文件或目录路径。 如果不指定文件名，然后默认名称为：yyyy-MM.[databaseNames] 日志 可以在文件名中指定日期时间模式。 | -n 当前日程表图表:\日志 -n 当前日程表图表:\ 日志\{yyyy-MM-dd} 日志 |
| -v | 可选的 | 如果指定，然后备份已完成一次进行校验。 | -v |
| -匹配行 | 可选的 | 如果指定然后仅后退日志文件。 | -匹配行 |
| 提醒 | 可选的 | 如果指定，然后截断日志文件。 | 提醒 |
| - Tm值 | 可选的 | 如果指定，然后仅测试已供应的邮件设置。用于设置备份作业以确保邮件正常工作。 当使用此选项时，否运行其它备份参数，即使你已包含备份选项。 | - Tm值 |
| -u | 可选的 | 如果指定，然后每个备份都将在名为 yyyyMMddHHmmss 的新建文件夹中已创建 | -u |
| -t “测试公司” | 必需的 | 将数据库复制到名为测试公司。提供测试公司的数据库名称。 与--dbn“数据库名称”一起使用，从中待复制数据库。 | -t 001_1 |
| --ms “邮件服务器” | 必需的 | 指定Email服务器名称。 | --ms 你的.smtpserver.com |
| 主组件 “端口编号” | 必需的 | 指定Email服务器的端口编号。 | --主组件25 |
| --md “显示名称” | 必需的 | 指定Email显示名称。 | --md 发件人姓名 |
| --mn “发件人电子邮件地址” | 必需的 | 指定发件人的Email 地址。 | --mn BackupSender@yourcompany.com |
| --mu “用户名” | 必需的 | 指定登录Email服务器的用户名。 | --mu 堆 --mu Smtp用户名 |
| --mw “密码文件路径” | 必需的 | 指定包含将发送 Email报告的发件人Email 地址的实际的密码的文本文件的路径。应限制此文件的许可，仓储费用仅运行已排程任务的Windows账户才具有对此文件的独占访问。 | --mw 当前日程表图表:\某处\pwd.txt |
| --mr“邮件接收者” | 必需的 | 以逗号分隔的接收者列表。 | --Recipient1@yourcompany.com 先生，Recipient2@yourcompany.com 先生 |
| --mb “主题” | 必需的 | 指定邮件主题。 | --mb 邮件主题 |
| --mt“邮件触发器” | 必需的 | 指定已发送电子邮件的触发器。默认总是。 0 =总是 1 =错误 | --mt 0 |
| --毫升 | 可选的 | 如果指定，然后使用 SSL。 | --毫升 |
