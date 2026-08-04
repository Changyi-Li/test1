# Preparing to install the Monitor BI Server
> These steps need to be carried out by your IT department or IT supplier. If you have questions you can contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com
You must have Monitor ERP version 24.5 or later installed.
The Monitor BI Server can either be installed on the application server (the Monitor server) or on a separate computer. Installation on the Monitor server is the recommended method if only BI clients will be used locally in the network. If the Monitor BI Server is not going to be installed on the application server but on a separate computer in the DMZ network, it is recommend to install the server on a separate computer in the DMZ network. For this installation you also need an SSL certificate for the computer, please see below.
However you choose to install the BI server, you are required to have an account in Windows with local administrator rights on the computer that the server will be installed on. During the installation of the BI server, you get to select which account will run the services installed in connection with the installation. You should then select that account. You can use the same account that runs the service for the application server (the Monitor server).
To run Monitor BI, the computer must have Microsoft Windows Desktop Runtime 8 (x64) and Microsoft ASP.NET Core 8.0.3 (x64) – Shared Framework is installed. Both are required and need to be the same version. We recommend that you install the latest version of Microsoft Windows Desktop Runtime 8 (x64) and Microsoft ASP.NET Core 8 (x64) – Shared Framework.

## SSL certificate
1. Purchase an SSL certificate for the server that will function as the BI server. The certificate should be issued by a certificate authority such as Verisign, Go Daddy, or Comodo. Certificates are either issued for the computer's DNS name (e.g., "monitor.yourcompany.com") or for an entire domain (as a so-called wildcard certificate "*.yourcompany.com").
2. When you receive the certificate file, install it on the server that will function as the BI server. The certificate file must be installed with the private key linked to your certificate, so we can then connect this certificate during installation.
> If Monitor BI is used only within the internal network, you do not need to use certificates. However, if Monitor BI is to be accessed externally, certificates must be used.

## Firewall configuration
The tables below describe how firewalls should be configured for the Monitor BI Server.
> When the application server (the Monitor server) was installed, firewalls were configured for communication between Windows clients, the application server, and the distribution server. This means you can skip those parts in the tables below.
> The distribution servers provide updates for Monitor ERP, options, and licenses. These servers are maintained by Monitor ERP System AB and are available for the Europe and China regions. The DNS names are cdn-eur-01.monitorerp.com and cdn-chn-01.monitorerp.cn. At present there is one server node per region (node number 01). A server node number 02 will shortly be added (DNS name cdn-eur-02.monitorerp.com and cdn-chn-02.monitorerp.cn respectively).
> Please note! Remember to check whether the standard port 443 and 80 is available and that it is not already being used by another service. If the standard port is already being used, choose another port that isn’t being used.

### Network's firewall
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | DMZ → LAN | Used for updating the BI server. |
| TCP | 8001 | DMZ → LAN | Used by the BI server server for communication with the application server (the Monitor server). |
| TCP | 8007 | LAN → DMZ | Used for updating the BI server. Port 8007 is set as default but when installing the BI server you can choose another port. |
| TCP | 443/80 | Internet → DMZ | Used for communication between BI clients and the BI server. Port 443 is used by SSL; port 80 is used otherwise. |
| TCP | 2638 | DMZ → LAN | Used by the BI server for communication with the application server database. Port 2638 is set as default for the database engine SQL Anywhere. Another port can also be chosen. |
| TCP | 1433 | DMZ → LAN | Used by the BI server for communication with the application server database. Port 1433 is set as default for the database motor Microsoft SQL Server. Another port can also be chosen. |
| TCP | 5432 | DMZ → LAN | Used by the BI server for communication with the application server database. Port 5432 is set as default for the database engine PostgreSQL. Another port can also be chosen. |

### Windows firewall in the application server (the Monitor server)
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | Inbound, Outbound | Used for updating Windows clients. |
| TCP | 8001 | Inbound, Outbound | Used by the BI server for communication with the application server. |
| UDP | 8002 | Inbound, Outbound | Used by Windows clients to automatically find the application server. |
| TCP | 2638 | Inbound, Outbound | Used by the BI server for communication with the application server database. Port 2638 is set as default for the database engine SQL Anywhere. Another port can also be chosen. |
| TCP | 1433 | Inbound, Outbound | Used by the BI server for communication with the application server database. Port 1433 is set as default for the database motor Microsoft SQL Server. Another port can also be chosen. |
| TCP | 5432 | Inbound, Outbound | Used by the BI server for communication with the application server database. Port 5432 is set as default for the database engine PostgreSQL. Another port can also be chosen. |

### Windows firewall in the BI server
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | Outbound | Used for updating the BI server. |
| TCP | 8001 | Outbound | Used by the BI server server for communication with the application server (the Monitor server). |
| TCP | 2638 | Inbound | Used by the BI server server for communication with the application server database (the Monitor database). Port 2638 is set as default for the database engine SQL Anywhere. Another port can also be chosen. |
| TCP | 1433 | Inbound | Used by the BI server for communication with the application server database. Port 1433 is set as default for the database motor Microsoft SQL Server. Another port can also be chosen. |
| TCP | 5432 | Inbound | Used by the BI server for communication with the application server database. Port 5432 is set as default for the database engine PostgreSQL. Another port can also be chosen. |
| TCP | 443/80 | Inbound | Used for communication between BI clients and the BI server. Port 443 is used by SSL; port 80 is used otherwise. |
| TCP | 8007 | Inbound | Used by the application server (the Monitor server) to communicate updates to the BI server. |

### Illustration of network and firewall configuration
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/FlowChart_BI.jpg)
