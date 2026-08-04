### Email
请注意！用户必须在正确已配置全部Email 设置之前使用在 Monitor的活动日历集成。

#### Email 方式
确定用户应应用的Email通信类型。
- 基于客户端, 通过 Microsoft Outlook – 如果用户安装了 Outlook，你可以选择此选项。
- 基于服务器, 通过 Microsoft Exchange – 如果要将在 Monitor的内置Email客户端用于 Exchange，你选择此选项。
- 基于服务器, 通过 SMTP – 如果使用 Exchange 以外的其它Email服务器，选择此选项。
- 基于服务器, 通过 Microsoft Exchange Online – 如果要使用在 Monitor的内置Email客户端端来访问 Exchange Online，选择此选项。在这种案件下，必须在 Microsoft Entra 标识 （以前称为 Azure 激活 目录 ）中已登记Oauth 2.0 的客户端程序。请参见 [本指南](../../BasicSettings/SystemSettings/GuideOAuth2.0.htm)。

#### Email 地址
用户的电子邮件地址。

#### 用户名 (Exchange)
如果你在 Email 方式 设置上面已选择了一Exchange选项后，你必须在这里输入用户在 Exchange 中的科目的用户名。

#### 密码 (Exchange)
如果你在 Email 方式 设置上面已选择了一Exchange选项后，你必须在这里输入用户在 Exchange 中的科目的密码。第一个，你需要点击挂锁按钮来解锁该字段 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/Padlock.png)。

#### 将副本发送至自己的 Email 地址
你可以在这里选择是否你从MONITOR ERP你的Email 消息副本。可用的选项包括 不复制， 复制 （抄送），以及 密件抄送。
仅当你在字段中已选择了基于服务器的替代方案时，仅支持此功能 Email 方式 或者在系统设置中调用 Email 发送方式。
