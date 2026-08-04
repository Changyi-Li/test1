# 配置ODBC链接
你必须输入SQL Anywhere 数据库用户的密码 只读用户。在帮助主题中阅读有关如何输入新密码或如何更改ReadOnlyUser密码的更多信息 [更改ReadOnlyUser密码](bChangePasswordReadOnlyUser.htm)。
除了到科目信息附加，你还需要配置以下设置：
- 数据库名称 – 公司编号（例如“001”）
- 服务器名称 – SQL服务的名称。在 Monitor ERP（MONITOR G5）中，它通常被称为“monitorG5_servername”（在数据库服务器上的“服务”下列出）。
- 主机 –MONITOR服务器的IP 地址或其 DNS名称。
- 端口 – 2638（如果MONITORG4 和MONITORERP（MONITORG5）在同一台服务器上运行，则端口可能会有所不同，在这种案件下，检查SQL服务使用由了哪个端口）。
