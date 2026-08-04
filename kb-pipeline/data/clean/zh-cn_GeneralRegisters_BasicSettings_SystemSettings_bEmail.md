### Email
大多数文件打印输出（例如订单）也可以通过Email已发送。不过，必须第一个在文档的页眉中输入收件人的Email 地址。这些文档会自动附加为PDF文件，在某些案件下也会附加为 XML文件。为了能够从MONITOR ERP发送 Email，你必须在此处配置Email服务器的设置。
请注意！这些Email 设置也用于在 Monitor的活动日历集成。

#### Email 方式
在这里你选择在 Monitor ERP 中发送和接收Email的通用方式。有四种方法：
- 基于客户端, 通过 Microsoft Outlook – 如果用户安装了 Outlook，你可以选择此选项。
- 基于服务器, 通过 Microsoft Exchange – 如果要将在 Monitor的内置Email客户端用于 Exchange（本地），选择此选项。
- 基于服务器, 通过 SMTP – 如果使用 Exchange 以外的其它Email服务器，选择此选项。
- 基于服务器, 通过 Microsoft Exchange Online – 如果要使用在 Monitor的内置Email客户端端来访问 Exchange Online，选择此选项。在这种案件下，你需要在 Microsoft Entra 标识 （以前称为 Azure 激活 目录 ）中登记Oauth 2.0 的客户端程序。请参见 [本指南](GuideOAuth2.0.htm)。
相应的设置也可用在用户层级上进行 用户 程序，并且在这种案件下它将覆盖此通用系统设置。

#### 服务器地址 (Exchange / SMTP)
在输入你Email的IP 地址或 DNS名称。
检查 Email 设置
使用按钮 检查 Email 设置 ![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/button_run.png) 你可以通过发送测试消息下一个确保字段Email 设置正确。
在单击按钮时显示的对话框中，你可以在系统设置中选择两种基于服务器的方法一 Email 发送方式。你还可以在此处输入Email 地址 接收者 和 发件人。这些字段中的Email 地址将默认从已登陆用户处加载。如果 Email 发送方式 被设定为 基于服务器, 通过 Microsoft Exchange，你还可以输入 用户名 和 密码 用于 Exchange服务器的验证。
当你点击 测试 按钮，显示“OK” 结果 字段是否设置工作。接收者还应该在其收件箱中收到一封测试Email。如果任何设置错误的，则原因将显示在结果字段中。

#### 端口(Exchange / SMTP)
在此处你Email服务器的IP 地址或 DNS名称的输入端口。默认下它说 0。这意味着将使用 Exchange 或 SMTP 的标准端口。如果系统设置调用 使用 SSL 已已激活，端口通常应设置为 587 （TLS）或 465 （SSL）。

#### 用户名 (SMTP)
在输入你登录SMPTEmail服务器的科目的用户名。根据应使用的 SMTP服务器或 SMTP服务，这可能是科目名称或Email 地址。
用于登录ExchangeEmail服务器的用户名是每用户输入的 用户 程序。

#### 密码 (SMTP)
在输入你登录SMTPEmail服务器的上面用户名的现有的密码。用于登录ExchangeEmail服务器的密码是每用户在 用户 程序。

#### 使用 SSL
如果Email服务器需要通过 TLS 或 SSL 建立单独的网络连接，则应已激活此系统设置。然后你还必须更改上面的系统设置 端口(Exchange / SMTP)。

#### Email 文件的最大规格
此设置将影响以下系统设置： 在同一个 Email 中发送多个订单 和 在同一个 Email 中发送多个订单 / 发票。在这里，你可以决定发送给供应商/客户的包含多个订单的Email附件的最大合计尺寸（以兆字节 (MB) 为单位）。这里的默认值是 10 MB。
如果此类Email中附件的合并尺寸是大于此处输入的值，则该Email将被分成两封或多更多Email。附件然后已分配这些Email中。
如果Email不包含多个订单，但是它包含的附件​​编号加起来超过了此处输入的尺寸，则该Email将不被拆分。
