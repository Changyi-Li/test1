# 安装准备 Monitor ERP 网上商店
> 低于描述的措施应由您的 IT部门或 IT供应商执行由。这些措施需要 Windows 服务器管理方面的知识。如果你有任何疑问，你通过电话联系人MONITOR支持中心：+46 650 766 03 或通过Email： 支持
Monitor ERP Webshop 安装在 DMZ 中的单独服务器上，该服务器安装了 Internet信息服务器(IIS)。如果客户已经拥有 Monitor ERP Web服务器安装在服务器上，然后最好在同一台服务器上安装网上商店。MONITOR 门户网站的某些组件也应安装在客户内部的网络 (LAN) 上的程序服务器( MONITOR服务器) 上。
Monitor 的技术支持将在两台服务器上为客户执行安装。这是通过远程访问下班的。安装网上商店仓储费用，网络服务器会响应地址http://localhost:80，即 HTTP 的标准TCP端口80。建议你在实际的启动之前更改，仓储费用网上商店响应地址https://localhost:443，即 HTTPS 的 TCP端口443 客户的 IT部门或 IT供应商负责人确保完成此操作。如果不安装 SSL认证，还应在网上商店的服务器上安装该证书。请参阅低于的SSL认证描述。

## 系统建议
在我们的系统建议中 Monitor ERP 你还查询系统建议 Monitor ERP 网上商店。您可以在这里找到这些内容：
[https://www.monitorerp.com/支持/system-recommendations/](https://www.monitorerp.com/sv/support/systemrekommendationer/)
如果你对网上商店的硬件有疑问，请通过电话：+46 650 766 03 或Email： 支持 @monitorerp. com联系人MONITOR支持中心。

## SSL认证
1. 为将要安装网上商店的服务器采购SSL认证。这应该是发出自的认证。认证可以为服务器的 DNS名称（例如“shop.yourcompany.com”）或整个域（即所谓的通配符认证“*.yourcompany.com”）颁发。
2. 你认证文件已收到，你应该将其复制到网上商店的服务器。

## 管理员科目和用户权限
安装的服务器上需要具有本地管理员权限的科目。你可以使用与运行程序服务器（MONITOR服务器）的服务相同的科目。
在 Windows 网上商店的服务器上，用户权限 写 将针对科目组已配置 iis_iusrs 在文件夹上 网上商店 和 网上商店通用文件。这是连接安装进行的已配置。路径示例（五月因安装而安装）：
当前日程表图表:\inetpub\webshop （包含网上商店的系统文件）。
当前日程表图表:\ MONITOR\ 定制包\WebShopGeneralFiles （包含应在网上商店显示的图像/文件）。

## Internet信息服务器(IIS) 的配置
在 Web服务器上，你应该为 IIS配置多个角色和功能。在里面 Windows服务器管理器 你根据低于表格将其添加到地图结构中。
| 构造图 | 添加 |
|---|---|
| 服务器角色> Web服务器(IIS) > Web服务器>共同的HTTP 功能 | 默认文档、目录浏览、HTTP错误、静态目录、HTTP 重定向 |
| 服务器角色> Web服务器(IIS) > Web服务器> 运行状况和诊断 | HTTP日志、定制日志、日志工具、请求MONITOR、跟踪 |
| 服务器角色> Web服务器(IIS) > Web服务器>性能 | 静态目录压缩、动态目录压缩 |
| 服务器角色> Web服务器(IIS) > Web服务器>安全 | 请求筛选中 |
| 服务器角色> Web服务器(IIS) > Web服务器>程序开发 | 净值扩展性 4.6、 净值 4.6、ISAPI 扩展、ISAPI筛选 |
| 服务器角色> Web服务器(IIS) > 管理工具 | 管理控制台 |
| 功能 > . 净值 Framework 3.5 功能 | 净值框架3.5 |
| 功能 > . 净值 Framework 4.6 功能 | 净值框架4.6 |
| 功能 > . 净值 Framework 4.6 功能 > ASP. 净值 4.6 | WCF服务、HTTP激活、TCP端口共享 |
| 特征 | IIS 可托管 Web 核心 |

## 网店的 URL/名称和端口
网店的名称、URL 和端口由客户的 IT部门决定。

## 防火墙配置

### 网络防火墙
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 8020 | 局域网 → DMZ | 用于从程序服务器（MONITOR服务器）到网上商店的服务器的通信。 |
| TCP | 8020 | DMZ → LAN | 用于从网上商店的服务器到程序服务器的通信。 |
| TCP | 443 | 互联网 → DMZ | 用于结束用户和网上商店在中间的加密通信（HTTPS）。用于与Adaptation Updater 和 Monitor 的包装管理器通信。 |
| TCP | 80 | 互联网 → DMZ | 备选。可用于结束用户和网上商店在中间的非加密通信（HTTP）。但是，不建议在互联网上使用未加密的通信。 |

### 程序服务器（MONITOR服务器）中的 Windows 防火墙
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 8020 | 入站 | 用于从网上商店的服务器到程序服务器的通信。 |
| TCP | 8020 | 出站 | 用于从程序服务器到网上商店的服务器的通信。 |
| TCP | 443 | 入站出站 | 用于与Adaptation Updater 和 Monitor 的包装管理器通信。 |

### 网店服务器中的 Windows 防火墙
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 8020 | 入站 | 用于从程序服务器到网上商店的服务器的通信。 |
| TCP | 8020 | 出站 | 用于从网上商店的服务器到程序服务器的通信。 |
| TCP | 443 | 入站 | 用于结束用户和网上商店在中间的加密通信（HTTPS）。用于与Adaptation Updater 和 Monitor 的包装管理器通信。 |
| TCP | 80 | 入站 | 备选。可用于结束用户和网上商店在中间的非加密通信（HTTP）。但是，不建议在互联网上使用未加密的通信。 |

### 网络和防火墙配置说明
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/WebshopChart.png)

## 网店的设计/布局
被用于标准布局。您可以使用 CSS、JavaScript 和 HTML代码来根据自己的设计和布局调整网上商店，但这不属于 Monitor 的责任区域。然而，表格站点实际的结构的 HTML代码无法已变更。
如果客户聘请一家网页设计公司来为网店创建自己的设计和布局，那可能会很好。公司徽标、产品/组件图像和“网站图标”（在网络浏览器的标签页和书签中显示的图标）全部由客户已创建/已添加。
