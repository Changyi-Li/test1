# MONITOR门户网站安装准备
> 低于描述的措施应由您的 IT部门或 IT供应商执行由。这些措施需要 Windows 服务器管理方面的知识。如果你有任何疑问，你通过电话联系人MONITOR支持中心：+46 650 766 03 或通过Email： 支持
你可以在 DMZ 中安装了 Internet信息服务器(IIS) 的单独服务器上安装MONITOR门户网站。如果客户已经拥有 Monitor ERP 在一台服务器上安装好Web服务器然后，最好在同一台服务器上安装MONITOR门户网站。MONITOR 门户网站的某些组件也应安装在客户内部的网络 (LAN) 上的程序服务器( MONITOR服务器) 上。
Monitor 的技术支持将在两台服务器上为客户执行安装。这是通过 Splashtop程序通过远程访问执行由的。MONITOR门户网站已安装，仓储费用Web 服务器响应地址http://localhost:80，即 HTTP 的标准TCP端口80。建议你在实际的启动之前更改，仓储费用网上商店响应地址https://localhost:443，即 HTTPS 的 TCP端口443 客户的 IT部门或 IT供应商负责人确保完成此操作。如果不安装 SSL认证，还应在MONITOR 门户网站服务器上安装该证书。请参阅低于的SSL认证描述。

## 系统建议
在我们的系统建议中 Monitor ERP 你还查询针对MONITOR 门户网站的系统建议。您可以在这里找到这些内容：
[https://www.monitorerp.com/支持/system-recommendations/](https://www.monitorerp.com/sv/support/systemrekommendationer/)
如果你对MONITOR 门户网站硬件有疑问，请通过电话：+46 650 766 03 或Email： 支持@monitorerp. com联系人MONITOR支持中心。

## SSL认证
1. 为将要安装MONITOR门户网站的服务器采购SSL认证。这应该是发出自的认证。认证可以为服务器的 DNS名称颁发（例如“monitorportal.yourcompany.com”），也可以为整个域颁发（即所谓的通配符认证“*.yourcompany.com”）。
2. 你认证文件后，你应该将其复制到MONITOR门户网站的服务器。

## 管理员科目和用户权限
安装的服务器上需要具有本地管理员权限的科目。你可以使用与运行程序服务器（MONITOR服务器）的服务相同的科目。
在MONITOR Portal服务器上的 Windows 中，用户权限 写 将针对科目组已配置 iis_iusrs 在文件夹上 监控门户。这应该与安装连接已配置。路径例如（五月因安装而安装）：
当前日程表图表：\inetpub\MonitorPortal （包含MONITOR门户网站的系统文件）。

## Internet信息服务器(IIS) 的配置
在MONITOR门户网站的服务器上，你应该为 IIS配置多个角色和功能。在里面 Windows服务器管理器 你根据低于表格将其添加到地图结构中。
| 构造图 | 添加 |
|---|---|
| 服务器角色> Web服务器(IIS) > Web服务器>共同的HTTP 功能 | 默认文档、目录、HTTP错误、静态目录 |
| 服务器角色> Web服务器(IIS) > Web服务器> 运行状况和诊断 | HTTP日志、请求MONITOR、跟踪 |
| 服务器角色> Web服务器(IIS) > Web服务器>性能 | 静态目录压缩、动态目录压缩 |
| 服务器角色> Web服务器(IIS) > Web服务器>安全 | 请求筛选中 |
| 服务器角色> Web服务器(IIS) > 管理工具 | 管理控制台 |
| 特征 | IIS 可托管 Web 核心 |

## MONITOR门户的 URL/名称和端口
MONITOR门户 Web服务器的名称、URL 和 TCP端口（443 或 80）由客户的 IT部门决定。

## 防火墙配置

### 网络防火墙
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 9933 | 局域网 → DMZ | 用于从程序服务器（MONITOR服务器）到MONITOR门户网站服务器的通信。 |
| TCP | 9933 | DMZ → LAN | 用于从MONITOR门户网站服务器到程序服务器的通信。 |
| TCP | 443 | 互联网 → DMZ | 用于结束用户和MONITOR门户的网站服务器在中间的加密通信（HTTPS）。用于与Adaptation Updater 和 Monitor 的包装管理器通信。 |
| TCP | 80 | 互联网 → DMZ | 备选。可用于结束用户和MONITOR门户的 Web服务器在中间的非加密通信(HTTP)。但是，不建议在互联网上使用未加密的通信。 |

### 程序服务器（MONITOR服务器）中的 Windows 防火墙
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 9933 | 入站 | 用于从MONITOR门户网站服务器到程序服务器的通信。 |
| TCP | 9933 | 出站 | 用于从程序服务器到MONITOR门户网站服务器的通信。 |
| TCP | 443 | 入站出站 | 用于与Adaptation Updater 和 Monitor 的包装管理器通信。 |

### MONITOR Portal服务器中的 Windows 防火墙
| 协议 | 端口 | 方向 | 功能 |
|---|---|---|---|
| TCP | 9933 | 入站 | 用于从程序服务器到MONITOR门户网站服务器的通信。 |
| TCP | 9933 | 出站 | 用于从MONITOR门户网站服务器到程序服务器的通信。 |
| TCP | 443 | 入站 | 用于结束用户和MONITOR门户的网站服务器在中间的加密通信（HTTPS）。用于与Adaptation Updater 和 Monitor 的包装管理器通信。 |
| TCP | 80 | 入站 | 备选。可用于结束用户和MONITOR门户的 Web服务器在中间的非加密通信(HTTP)。但是，不建议在互联网上使用未加密的通信。 |

### 网络和防火墙配置说明
![](https://help.monitorerp.cn/CN-MONITOR_G5/zh-cn/Content/Resources/Images/UserGuide/MonitorPortalChart.png)
