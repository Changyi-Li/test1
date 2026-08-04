### 使用 Microsoft Entra 标识激活OAuth 2.0
在这里，你查询有关在 Microsoft Entra 标识 （以前称为 Azure 激活 目录）和在 Monitor需要执行哪些措施的信息，以便能够使用 OAuth 2.0验证从 Exchange Online 向MONITOR ERP 发送传入Email。

#### 在 Microsoft Entra 标识中登记程序
在 Microsoft Entra 标识中登记用于MONITORERP 的客户端程序。看 [本指南](https://help.monitor.se/英语/Monitor_G5/PDF/setup_azure_oauth.pdf) （用英语）。
> 请注意！解决此问题时，如果需要，你应该联系人您的 IT 顾问，以获取有关 Microsoft Entra 标识中所需措施的帮助！

#### 在 MonitorEmail的设置
从 22.6版本开始，你必须按照相应的程序在低于的在 Monitor配置附加设置。在这里你查询 [设置描述](bEmail.htm)。
系统设置：
- Email 方式 –选择选项 基于服务器, 通过 Microsoft Exchange Online。
- 应用程序 (客户端) ID –值自复制值 应用程序 (客户端) ID 在 Microsoft Entra 标识中的客户端程序中。
- 目录 (租户) ID –值自复制值 目录 (租户) ID 在 Microsoft Entra 标识中的客户端程序中。
- 认证流 –选择用于 Exchange Online 的认证流。你可以在中间 客户端密码 和 用户名 / 密码。
- 客户端密码 – 如果你已选择了 客户端密码 选项作为认证流，你应该复制 值 对于你在 Microsoft Entra 标识中已创建的客户端密码，并将其粘贴这里。
用户：
如果你对用户有特定的Email 设置（会覆盖相应的系统设置），你五月也需要对这些设置进行调整/附加。
如果你给了 网上商店 选项，你还必须设置WEBSHOP用户（用于网上商店）配置以下设置：
- Email 方式 –选择选项 基于服务器, 通过 Microsoft Exchange Online。
- 用户名 (Exchange) /密码 (Exchange) – 如果上面系统设置， 认证流， 被设定为 用户名 / 密码，你必须输入Exchange科目的用户名和密码。
收取 Email 设置：
如果你已已登记用于接收不同类型Email的Email 账户，例如， Monitor - to - Monitor，你必须补充与系统设置相对应的设置，并复制相同的值粘贴到这里。

#### MONITORERP选项中的Email附加设置
在里面 网上商店——管理 你必须补充低于有关Email的设置。在这里你查询 [设置描述](https://help.monitor.se/SV/webshop_G5/latest/Content/Using/e_mail/settings.htm)。
- Email 方式 –配置为 根据用户设置在 Monitor的用户设置。
