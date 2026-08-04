# Preparation for installation of Monitor ERP Webshop
> These steps need to be carried out by your IT department or your IT supplier. The actions require knowledge in Windows Server administration. If you have questions you can contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com
Monitor ERP Webshop is installed on a separate server in DMZ which has the Internet Information Server (IIS) installed. If the customer already has the Monitor ERP Web server installed on a server, then it is good to install the webshop on the same server. Certain parts for the webshop should also be installed on the application server (the Monitor server) on the customer's internal network (LAN).
Monitor's tech support will perform the installation for the customer on the two servers. This is carried out out by remote access. The webshop is installed so the web sever responds on the address http://localhost:80, that is, standard TCP port 80 for HTTP. It is recommended, prior to actual startup, to change so the web server responds on the address https://localhost:443, that is, TCP port 443 for HTTPS. The customer's IT department or IT supplier is responsible for ensuring this is done. An SSL certificate should also be installed for this on the webshop's server if it has not already been installed. See the below description of the SSL certificate.

## System recommendations
In our system recommendations for Monitor ERP you’ll also find the system recommendations for Monitor ERP Webshop. These can be found here:
[https://www.monitorerp.com/support/system-recommendations/](https://www.monitorerp.com/sv/support/systemrekommendationer/)
If you have questions regarding hardware for the Webshop, please contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com.

## SSL certificate
1. Purchase an SSL certificate for the server where the webshop will be installed. The certificate should be issued by a certificate authority such as Verisign, Go Daddy, or Comodo. Certificates are either issued for the server's DNS name (e.g. "shop.yourcompany.com") or for an entire domain (as a so-called wildcard certificate "*.yourcompany.com").
2. When you have received the certificate file you should copy it to the server for the webshop.

## Administrator account and user rights
An account with local administrator rights is required on the server where the installation is made. You can use the same account that runs the service for the application server (the Monitor server).
In Windows on the webshop's server, the user right Write will be configured for the account group IIS_IUSRS on the folders Webshop and WebShopGeneralFiles. This is configured in connection with the installation. Examples of paths (which may vary from installation to installation):
C:\inetpub\webshop (Contains system files for the webshop).
C:\Monitor\Adaptations\WebShopGeneralFiles (Contains images/files which should be shown in the webshop).

## Configuration of Internet Information Server (IIS)
On the web server you should configure IIS with multiple roles and functions. In the Windows Server Manager you add this in the map structure according to the table below.
| Structure map | Add |
|---|---|
| Server Roles > Web Server (IIS) > Web Server > Common HTTP Features | Default Document, Directory Browsing, HTTP Errors, Static Content, HTTP Redirection |
| Server Roles > Web Server (IIS) > Web Server > Health and Diagnostics | HTTP Logging, Custom Logging, Logging Tools, Request Monitor, Tracing |
| Server Roles > Web Server (IIS) > Web Server > Performance | Static Content Compression, Dynamic Content Compression |
| Server Roles > Web Server (IIS) > Web Server > Security | Request Filtering |
| Server Roles > Web Server (IIS) > Web Server > Application Development | .NET Extensibility 4.6, ASP.NET 4.6, ISAPI Extensions, ISAPI Filters |
| Server Roles > Web Server (IIS) > Management Tools | Management Console |
| Features > .NET Framework 3.5 Features | .NET Framework 3.5 |
| Features > .NET Framework 4.6 Features | .NET Framework 4.6 |
| Features > .NET Framework 4.6 Features > ASP.NET 4.6 | WCF Services, HTTP Activation, TCP Port Sharing |
| Features | IIS Hostable Web Core |

## Webshop's URL/domain name and port
Domain name, URL, and port for the webshop are decided by the customer's IT department.

## Firewall configuration

### Network's firewall
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 8020 | LAN → DMZ | Used for communication from the application server (the Monitor server) to the webshop's server. |
| TCP | 8020 | DMZ → LAN | Used for communication from the webshop's server to the application server. |
| TCP | 443 | Internet → DMZ | Used for encrypted communication (HTTPS) between end users and webshop. Used for communication with Adaptation Updater and Monitor's package manager. |
| TCP | 80 | Internet → DMZ | Alternatives. Can be used for unencrypted communication (HTTP) between end users and webshop. However, it is not recommended to use unencrypted communication over the Internet. |

### Windows firewall in the application server (the Monitor server)
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 8020 | Inbound | Used for communication from the webshop's server to the application server. |
| TCP | 8020 | Outbound | Used for communication from the application server to the webshop's server. |
| TCP | 443 | Inbound, Outbound | Used for communication with Adaptation Updater and Monitor's package manager. |

### Windows firewall in the webshop's server
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 8020 | Inbound | Used for communication from the application server to the webshop's server. |
| TCP | 8020 | Outgoing | Used for communication from the webshop's server to the application server. |
| TCP | 443 | Inbound | Used for encrypted communication (HTTPS) between end users and webshop. Used for communication with Adaptation Updater and Monitor's package manager. |
| TCP | 80 | Inbound | Alternatives. Can be used for unencrypted communication (HTTP) between end users and webshop. However, it is not recommended to use unencrypted communication over the Internet. |

### Illustration of network and firewall configuration
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/WebshopChart.png)

## Design/layout of the webshop
Standard layouts are included in the webshop. It is possible to adapt the webshop with your own design and layout using CSS JavaScript and HTML code, but this is not within Monitor's area of responsibility. However, the HTML code which form the actual structure of the site cannot be changed.
It may be a good idea for the customer to hire a web design company to create their own design and layout for the webshop. Company logo, images of products/parts, and a "favicon" (icon shown in the web browser's tab and bookmarks) should all be created/added by the customer.
