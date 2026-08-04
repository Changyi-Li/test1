# Preparing to install the Monitor Portal
> These steps need to be carried out by your IT department or IT supplier. The actions require knowledge in Windows Server administration. If you have questions you can contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com
Monitor Portal is installed on a separate server in DMZ which has the Internet Information Server (IIS) installed. If the customer already has the Monitor ERP Web server installed on a server, then it preferable to install Monitor Portal on the same server. Certain parts for Monitor Portal should also be installed on the application server (the Monitor server) on the customer's internal network (LAN).
Monitor's tech support will perform the installation for the customer on the two servers. This in performed by remote access via a program named Splashtop. Monitor Portal is installed so the web sever responds on the addresshttp://localhost:80, i.e. standard tcp-port 80 for HTTP. It is recommended, prior to actual startup, to change so the web server responds on the address https://localhost:443, that is, TCP port 443 for HTTPS. The customer's IT department or IT supplier is responsible for ensuring this is done. For this, a local SSL certificate should also be installed on the server for Monitor Portal if not already installed. See the description below of the SSL certificate.

## System recommendations
In our system recommendations for Monitor ERP you’ll also find the system recommendations for Monitor Portal. These can be found here:
[https://www.monitorerp.com/support/system-recommendations/](https://www.monitorerp.com/sv/support/systemrekommendationer/)
If you have questions regarding hardware for Monitor Portal, please contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com.

## SSL certificate
1. Purchase an SSL certificate for the server where Monitor Portal will be installed. The certificate should be issued by a certificate authority such as Verisign, Go Daddy, or Comodo. Certificates are either issued for the server's DNS name (e.g. "monitorportal.yourcompany.com") or for an entire domain (as a so-called wildcard certificate "*.yourcompany.com").
2. When you have received the certificate file you should copy it to the server for Monitor Portal.

## Administrator account and user rights
An account with local administrator rights is required on the server where the installation is made. You can use the same account that runs the service for the application server (the Monitor server).
In Windows on the Monitor Portal's server, the user right Write will be configured for the account group IIS_IUSRS on the folder MonitorPortal. This should be configured in connection with the installation. Example of path (which may vary from installation to installation):
C:\inetpub\MonitorPortal (Contains system files for Monitor Portal).

## Configuration of Internet Information Server (IIS)
On the server for Monitor Portal you should configure IIS with multiple roles and functions. In the Windows Server Manager you add this in the map structure according to the table below.
| Structure map | Add |
|---|---|
| Server Roles > Web Server (IIS) > Web Server > Common HTTP Features | Default Document, Directory Browsing, HTTP Errors, Static Content |
| Server Roles > Web Server (IIS) > Web Server > Health and Diagnostics | HTTP Logging, Request Monitor, Tracing |
| Server Roles > Web Server (IIS) > Web Server > Performance | Static Content Compression, Dynamic Content Compression |
| Server Roles > Web Server (IIS) > Web Server > Security | Request Filtering |
| Server Roles > Web Server (IIS) > Management Tools | Management Console |
| Features | IIS Hostable Web Core |

## Monitor Portal URL/domain name and port
Domain name, URL, and TCP port (443 or 80) for Monitor Portal's web server are decided by the customer's IT department.

## Firewall configuration

### Network's firewall
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 9933 | LAN → DMZ | Used for communication from the application server (Monitor server) to the server for Monitor Portal. |
| TCP | 9933 | DMZ → LAN | Used for communication from the server for Monitor Portal to the application server. |
| TCP | 443 | Internet → DMZ | Is used for encrypted communication (HTTPS) between end users and Monitor Portal's web server. Used for communication with Adaptation Updater and Monitor's package manager. |
| TCP | 80 | Internet → DMZ | Alternatives. Can be used for unencrypted communication (HTTP) between end users and Monitor Portal's web server. However, it is not recommended to use unencrypted communication over the Internet. |

### Windows firewall in the application server (the Monitor server)
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 9933 | Inbound | Used for communication from the server for Monitor Portal to the application server. |
| TCP | 9933 | Outbound | Used for communication from the application server to the server for Monitor Portal. |
| TCP | 443 | Inbound, Outbound | Used for communication with Adaptation Updater and Monitor's package manager. |

### Windows firewall in Monitor Portal server
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 9933 | Inbound | Used for communication from the application server to the server for Monitor Portal. |
| TCP | 9933 | Outbound | Used for communication from the server for Monitor Portal to the application server. |
| TCP | 443 | Inbound | Is used for encrypted communication (HTTPS) between end users and Monitor Portal's web server. Used for communication with Adaptation Updater and Monitor's package manager. |
| TCP | 80 | Inbound | Alternatives. Can be used for unencrypted communication (HTTP) between end users and Monitor Portal's web server. However, it is not recommended to use unencrypted communication over the Internet. |

### Illustration of network and firewall configuration
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/MonitorPortalChart.png)
