# Preparation for installation of Monitor ERP Web server
> These actions should be performed by your IT department or your IT supplier. If you have questions you can contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com
Monitor ERP server can either be installed on the application server (the Monitor server) or on a separate computer in the DMZ network. Installation on the Monitor server is the recommended method if Monitor Mobile will only be used locally in the network. Installation on a separate computer in DMZ is the recommended method if Monitor Mobile should also be able to be used outside the network. For this installation you also need an SSL certificate for the computer, please see below.
Regardless of the method for installation of the web server, you are required to have an account in Windows with local administrator rights on the computer where the installation is made. During the installation Monitor ERP Web server, you get to select an account which will run the services installed in connection with the installation. Then you should select this account. You can use the same account that runs the service for the application server (the Monitor server).

## SSL certificate
1. Purchase an SSL certificate for the server that will function as web server. The certificate should be issued by a certificate authority such as Verisign, Go Daddy, or Comodo. Certificates are either issued for the computer's DNS name (e.g., "monitor.yourcompany.com") or for an entire domain (as a so-called wildcard certificate "*.yourcompany.com").
2. When you receive the certificate file, install it on the server that will function as web server. The certificate file must be installed with the private key linked to your certificate, so we can then connect this certificate during installation.

## Firewall configuration
The tables below describe how firewalls should be configured for Monitor Web server. At the end, there is an illustration of the network in a complete environment with both application server (Monitor server*), web server, distribution servers**, Windows clients, and mobile clients. In this illustration you can see which ports are used, and the direction of the traffic.
> * When the application server (the Monitor server) was installed, firewalls were configured for communication between Windows clients, the application server, and the distribution server. This means you can skip those parts in the tables below.
> ** The distribution servers provide updates for Monitor ERP, options, and licenses. These servers are maintained by Monitor ERP System AB and are available for the Europe and China regions. The DNS names are cdn-eur-01.monitorerp.com and cdn-chn-01.monitorerp.cn. At present there is one server node per region (node number 01). A server node number 02 will shortly be added (DNS name cdn-eur-02.monitorerp.com and cdn-chn-02.monitorerp.cn respectively).
> Please note! Remember to check whether the standard port 443 and 80 is available and that it is not already being used by another service. If the standard port is already being used, choose another port that isn’t being used.

### Network's firewall
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | DMZ → LAN | Used for updating the web server. |
| TCP | 8001 | DMZ → LAN | Used by the web server for communication with the application server (the Monitor server). |
| TCP | 8714 | LAN → DMZ | Used for updating the web server. |
| TCP | 443/80 | Internet → DMZ | Used for all communication between the mobile clients and the web server. Port 443 is used for SSL; port 80 is used otherwise. |
| TCP | 443/80 | LAN → Internet | Used for all communication between the application server and the distribution server. Used for all communication with external services for the application server and clients. Port 443 is used for SSL; port 80 is used otherwise. External services include currency update services and shipping services, for example. |

### Windows firewall in the application server (the Monitor server)
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | Inbound, Outbound | Used for updating Windows clients. |
| TCP | 8001 | Inbound, Outbound | Used by Windows clients and web server for communication with application server. |
| UDP | 8002 | Inbound, Outbound | Used by Windows clients to automatically find the application server. |

### Windows firewall in the web server
| Protocol | Port | Direction | Function |
|---|---|---|---|
| TCP | 7710 | Outbound | Used for updating the web server. |
| TCP | 8001 | Outbound | Used by the web server for communication with the application server (the Monitor server). |
| TCP | 443/80 | Inbound | Used for communication between the mobile clients and the web server. Port 443 is used for SSL; port 80 is used otherwise. |
| TCP | 8714 | Inbound | Used by the application server (the Monitor server) to communicate updates to the web server. |

### Illustration of network and firewall configuration
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/NetworkChart.png)
