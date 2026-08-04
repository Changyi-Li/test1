# Preparation for installation of Monitor ERP TimeCard
> These steps need to be carried out by your IT department or your IT supplier. The actions require knowledge in Windows Server administration. If you have questions you can contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com
You install Monitor ERP TimeCard on a separate server in DMZ which have Internet Information Server (IIS) installed. If the customer already has the Monitor ERP Web server installed on a server, then it is good to install the TimeCard on the same server. Certain parts of TimeCard should also be installed on the application server (the Monitor server) on the customer's internal network (LAN).
Monitor's tech support will perform the installation for the customer on the two servers. This in performed by remote access via a program named Splashtop. The TimeCard is installed so the web sever responds on the address http://localhost:80, that is, standard TCP port 80 for HTTP. It is recommended, prior to actual startup, to change so the web server responds on the address https://localhost:443, that is, TCP port 443 for HTTPS. The customer's IT department or IT supplier is responsible for ensuring this is done. An SSL certificate should also be installed for this on the the server for TimeCard, if it has not already been installed. See the below description of the SSL certificate.

## System recommendations
In our system recommendations for Monitor ERP you also find the system recommendations for Monitor ERP TimeCard. These can be found here:
[https://www.monitorerp.com/support/system-recommendations/](https://www.monitorerp.com/sv/support/systemrekommendationer/)
If you have questions regarding hardware for the TimeCard, please contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com.

## SSL certificate
1. Purchase an SSL certificate for the server where the TimeCard will be installed. The certificate should be issued by a certificate authority such as Verisign, Go Daddy, or Comodo. Certificates are either issued for the server's DNS name (e.g. "timecard.yourcompany.com") or for an entire domain (as a so-called wildcard certificate "*.yourcompany.com").
2. When you have received the certificate file you should copy it to the server for the TimeCard.

## Administrator account and user rights
An account with local administrator rights is required on the server where the installation is made. You can use the same account that runs the service for the application server (the Monitor server).
In Windows on the TimeCard's server, the user right Write will be configured for the account group IIS_IUSRS on the folder TimeCard. This should be configured in connection with the installation. Example of path (which may vary from installation to installation):
C:\inetpub\Timecard (Contains system files for the TimeCard).

## Configuration of Internet Information Server (IIS)
On the server for the TimeCard you should configure IIS with multiple roles and functions. In the Windows Server Manager you add this in the map structure according to the table below.
| Structure map | Add |
|---|---|
| Server Roles > Web Server (IIS) > Web Server > Common HTTP Features | Default Document, Directory Browsing, HTTP Errors, Static Content |
| Server Roles > Web Server (IIS) > Web Server > Health and Diagnostics | HTTP Logging, Request Monitor, Tracing |
| Server Roles > Web Server (IIS) > Web Server > Performance | Static Content Compression, Dynamic Content Compression |
| Server Roles > Web Server (IIS) > Web Server > Security | Request Filtering |
| Server Roles > Web Server (IIS) > Management Tools | Management Console |
| Features | IIS Hostable Web Core |

## TimeCard's URL/domain name and port
Domain name, URL, and TCP port (443 or 80) for the TimeCard's web server are decided by the customer's IT department.

## Firewall configuration

### Network's firewall
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 9922 | LAN → DMZ | Used for communication from the application server (Monitor server) to the server for TimeCard. |
| TCP | 9922 | DMZ → LAN | Used for communication from the server for TimeCard to the application server. |
| TCP | 443 | Internet → DMZ | Is used for encrypted communication (HTTPS) between end users and the TimeCard's web server. Used for communication with Adaptation Updater and Monitor's package manager. |
| TCP | 80 | Internet → DMZ | Alternatives. Can be used for unencrypted communication (HTTP) between end users and the TimeCard's web server. However, it is not recommended to use unencrypted communication over the Internet. |

### Windows firewall in the application server (the Monitor server)
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 9922 | Inbound | Used for communication from the server for TimeCard to the application server. |
| TCP | 9922 | Outgoing | Used for communication from the application server to the server for TimeCard. |
| TCP | 443 | Inbound, Outbound | Used for communication with Adaptation Updater and Monitor's package manager. |

### Windows firewall in the TimeCard's server
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 9922 | Inbound | Used for communication from the application server to the server for TimeCard. |
| TCP | 9922 | Outbound | Used for communication from the server for TimeCard to the application server. |
| TCP | 443 | Inbound | Is used for encrypted communication (HTTPS) between end users and the TimeCard's web server. Used for communication with Adaptation Updater and Monitor's package manager. |
| TCP | 80 | Inbound | Alternatives. Can be used for unencrypted communication (HTTP) between end users and the TimeCard's web server. However, it is not recommended to use unencrypted communication over the Internet. |

### Illustration of network and firewall configuration
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/TimeCardChart.png)
