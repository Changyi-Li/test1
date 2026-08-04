# Preparation for installation of Monitor ERP Server
> The actions described below should be performed by your IT department or your IT supplier. If you have questions about this or about hardware, you can contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com

## Requirements
Read our system recommendations for Monitor ERP here: [https://www.monitorerp.com/support/system-recommendations/](https://www.monitorerp.com/sv/support/systemrekommendationer/)
As of Monitor ERP version 24.6, the server computer must have Microsoft Windows Desktop Runtime 8 (x64) and Microsoft ASP.NET Core 8 (x64) – Shared Framework, before you install Monitor ERP Server. We recommend that you install the latest version of Microsoft Windows Desktop Runtime 8 (x64) and Microsoft ASP.NET Core 8 (x64) – Shared Framework. From version 24.3, Monitor ERP will no longer work on computers (clients) with a 32-bit Windows operating system. This means that computers with a 32-bit operating system need to be updated to a 64-bit operating system or need to be swapped with a computer that has a 64-bit operating system.

## SAP SQL Anywhere
If the Monitor ERP Server is to be installed for SAP SQL Anywhere database server, the program is included on installation of Monitor ERP Server.

## Microsoft SQL Server
If Monitor ERP Server is to be installed for Microsoft SQL Server database server, Monitor ERP supports Microsoft SQL Server 2017, 2019, and 2022 Standard Edition and Enterprise Edition. SQL Server is installed separately by your IT team on a server computer, unless you have an existing SQL Server that will run your Monitor ERP databases.
Monitor ERP Server is also installed on a separate server computer. See the Install Monitor ERP Server instruction.
Your SQL Server must have the setting SQL Server and Windows Authentication mode activated on the Security page under Server Properties in the SQL Server Management Console.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLServerRequirement.png)
> Please note! When installing the Monitor ERP Server, an account in your SQL Server must be selected which has the server roll "sysadmin" activated. This is in order to create the necessary logins for Monitor ERP in SQL Server. The account is only used during installation of Monitor ERP.
We recommend that you configure the same character set (collation) in SQL Server which the databases have in Monitor ERP. The character set to be chosen depends on the country package included in the installation of your Monitor ERP, as shown below:
| Country packages | Collation |
|---|---|
| Sweden/Finland | Finnish_Swedish_100_CI_AS |
| Denmark | Danish_Greenlandic_100_CI_AS |
| Norway | Norwegian_100_CI_AS |
| Germany | German_PhoneBook_CI_AI |
| Poland | Polish_100_CI_AS |
| Estonia | Estonian_100_CI_AS |
| Latvia | Latvian_100_CI_AS |
| Lithuania | Lithuanian_100_CI_AS |
| Russia | Cyrillic_General_CI_AS |
| Other | Latin1_General_100_CI_AS |
If the country package included in your Monitor ERP is not listed above, contact the Monitor Support Center.

## Windows administrator account
To install Monitor ERP Server you need an account in Windows with local administrator rights on the computer where the installation will be made. During the installation, you’ll get to select a Windows account which will run the server service created in connection with the installation. You should then select this account. The server service which is created is called Monitor ERP Application Server.
The Windows account you choose must have full access to shared directories where files/documents are saved that will be used in Monitor ERP.
If a document server is installed later on (done via the Installation manager), the administrator account should also run the server service created during that installation. The server service is called Monitor ERP Document Server. If you do not install the document server logged-on with the administrator account in Windows, you must then select that account on the server service in Services in Windows.

## Firewall configuration
The tables below describe how firewalls should be configured for the Monitor Server. At the end, there is an illustration of the network in a complete environment with both application server (Monitor server), web server*, distribution servers**, Windows clients, and mobile clients. In this illustration you can see which ports are used, and the direction of the traffic.
> * If Monitor Web server should not be installed, you can skip the sections which concern the communication between the web server on DMZ and the application server (the Monitor server) on LAN, as well as between the web server and the mobile clients.
> ** The distribution servers provide updates for Monitor ERP, options, and licenses. These servers are maintained by Monitor ERP System AB and are available for the Europe and China regions. The DNS names are cdn-eur-01.monitorerp.com and cdn-chn-01.monitorerp.cn. At present there is one server node per region (node number 01). A server node number 02 will shortly be added (DNS name cdn-eur-02.monitorerp.com and cdn-chn-02.monitorerp.cn respectively).

### Network's firewall
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | DMZ → LAN | Used for updating the web server. |
| TCP | 8001 (HTTPS) | DMZ → LAN | Used by the web server for communication with the application server (the Monitor server). |
| TCP | 8714 | LAN → DMZ | Used for updating the web server. |
| TCP | 443/80 | Internet → DMZ | Used for all communication between the mobile clients and the web server. Port 443 is used for SSL; port 80 is used otherwise. |
| TCP | 443/80 | LAN → Internet | Used for all communication between the application server and the distribution server. Used for all communication with external services for the application server and clients. Port 443 is used for SSL; port 80 is used otherwise. External services include currency update services and shipping services, for example. |

### Windows firewall in the application server (the Monitor server)
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | Inbound, Outbound | Used for updating Windows clients. |
| TCP | 8001 (HTTPS) | Inbound, Outbound | Used by Windows clients and web server for communication with application server. |
| UDP | 8002 | Inbound, Outbound | Used by Windows clients to automatically find the application server. |

### Windows firewall in the web server (if it should be installed)
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | Outbound | Used for updating the web server. |
| TCP | 8001 (HTTPS) | Outgoing | Used by the web server for communication with the application server (the Monitor server). |
| TCP | 443/80 | Inbound | Used for communication between the mobile clients and the web server. Port 443 is used for SSL; port 80 is used otherwise. |
| TCP | 8714 | Inbound | Used by the application server (the Monitor server) to communicate updates to the web server. |

### Illustration of network and firewall configuration
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/NetworkChart.png)
