# 安装准备 Monitor ERP 服务器
> 低于描述的措施应由您的 IT部门或 IT供应商执行由。如果你对此或有关硬件有任何疑问，你可以通过电话：+46 650 766 03 或Email： 支持@monitorerp. com联系人MONITOR支持中心。

## 要求
阅读我们的系统建议 Monitor ERP 这里： [https://www.monitorerp.com/支持/system-recommendations/](https://www.monitorerp.com/sv/support/systemrekommendationer/)
在安装之前，服务器计算机需要安装 Microsoft . 净值 Framework 4.8 或更高版本 Monitor ERP 服务器。
自 24.3版本释放以来， Monitor ERP 将否工作于搭载 32 位 Windows 操作系统的计算机（客户端）。这意味着你要么将系统升级到Windows 64位，要么变更为具有Windows 64位系统的计算机。

## SAP SQL 无处不在
如果 Monitor ERP 服务器将安装 SAP SQL Anywhere 数据库服务器，该程序包含在安装中 Monitor ERP 服务器。

## 微软 SQL服务器
如果 Monitor ERP 服务器将安装 Microsoft SQL 服务器数据库服务器， Monitor ERP 支持Microsoft SQL 服务器 2017、2019标准版和企业版。SQL 服务器由您的 IT 团队在服务器计算机上单独安装，除非你有现有的SQL 服务器可以运行您的 Monitor ERP 数据库。
Monitor ERP 服务器也安装在单独的服务器计算机上。查看 安装 Monitor ERP 服务器 指导。
您的 SQL 服务器必须具有设置 SQL 服务器和 Windows验证模式 在 SQL 服务器管理控制台中的服务器属性下的安全页上已激活。
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/SQLServerRequirement.png)
> 请注意！安装时 Monitor ERP 服务器，必须已选择一个 SQL 服务器中的科目，该帐户已已激活服务器角色“sysadmin”。这是订单创建必要的登录信息 Monitor ERP 在 SQL 服务器中。该科目仅在安装期间使用 Monitor ERP。
周三建议你在 SQL 服务器中配置与数据库相同的字符集（排序规则）。 Monitor ERP。要选择的字符集取决于您的安装被用于的国家 / 地区包装 Monitor ERP，低于所示 ：
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
如果您的包装被用于的国家 / 地区/地区 Monitor ERP 不在上面列出，联系人MONITOR支持中心。

## Windows管理员科目
安装 Monitor ERP 服务器你需要在将要进行安装的计算机上拥有一个本地管理员权限的 Windows科目。在安装中，你将选择一个Windows账户，该帐户将运行与安装连接的已创建的服务器服务。然后你应该选择这个科目。已创建的服务器服务称为 Monitor ERP 程序服务器。
你选择的Windows账户必须具有对已保存文件/文档的共享目录的完全访问，这些文件/文档将在 Monitor ERP。
如果稍后安装了文档服务器（通过安装管理器完成），则管理员科目还应运行在安装期间已创建的服务器服务。服务器服务被称为 Monitor ERP 文档服务器。如果你不在 Windows 中安装使用管理员科目登录的文档服务器，然后你在服务器服务中选择该科目 服务 在 Windows 中。

## 防火墙配置
低于表描述了如何为MONITOR服务器已配置防火墙。结束，说明了完成环境中的网络，两者包括程序服务器（MONITOR服务器）、Web服务器*、分配服务器**、Windows 客户端和 Web 客户端。在此图中，你可以看到使用了哪些端口以及流量的方向。
> * 如果不安装MONITORWeb服务器，你跳过有关 DMZ 上的 Web服务器与 LAN 上的程序服务器（MONITOR服务器）在中间的通信以及 Web服务器与 Web 客户端在中间的通信的部分。
> **分配服务器提供以下更新 Monitor ERP、选项和许可。这些服务器由 Monitor ERP 系统有限公司 并可用于欧洲和中国地区。DNS 名称是 cdn-eur-01.monitorerp.com 和 cdn-chn-01.monitorerp.cn。目前每地区有一服务器节点（节点号01）。很快将已添加服务器节点号02（DNS名称 cdn-eur-02.monitorerp.com 和 cdn-chn-02.monitorerp.cn 分别）。

### 网络防火墙
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 7710 | DMZ → LAN | 用于更新网络服务器。 |
| TCP | 8001（HTTPS） | DMZ → LAN | 由 Web服务器使用由与程序服务器（MONITOR服务器）进行通信。 |
| TCP | 8714 | 局域网 → DMZ | 用于更新网络服务器。 |
| TCP | 443/80 | 互联网 → DMZ | 用于Web 客户端和 Web服务器在中间的全部通信。端口443用于SSL；否则使用端口80。 |
| TCP | 443/80 | 局域网 → 互联网 | 用于程序服务器和分配服务器在中间的全部通信。用于程序服务器和客户端与外部的服务的全部通信。端口443用于SSL；否则使用端口80。例如，外部的服务包括货币更新服务和货运服务。 |

### 程序服务器（MONITOR服务器）中的 Windows 防火墙
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 7710 | 入站出站 | 用于更新Windows 客户端。 |
| TCP | 8001（HTTPS） | 入站出站 | 由 Windows 客户端和 Web服务器使用由与程序服务器通信。 |
| UDP | 8002 | 入站出站 | 使用由自动查询程序服务器。 |

### Web服务器中的 Windows 防火墙（如果应该安装）
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 7710 | 出站 | 用于更新网络服务器。 |
| TCP | 8001（HTTPS） | 出站 | 由 Web服务器使用由与程序服务器（MONITOR服务器）进行通信。 |
| TCP | 443/80 | 入站 | 用于Web客户端和Web服务器在中间的通信。端口443用于SSL；否则使用端口80。 |
| TCP | 8714 | 入站 | 由程序服务器（MONITOR服务器）使用由向 Web服务器传送更新。 |

### 网络和防火墙配置说明
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/NetworkChart.png)
