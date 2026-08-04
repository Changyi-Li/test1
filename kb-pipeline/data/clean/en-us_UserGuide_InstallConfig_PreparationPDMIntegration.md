# Preparing to install PDM Integration
> These steps need to be carried out by your IT department or IT supplier. Knowledge of Windows Server administration is required. If you have questions you can contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com
Monitor’s PDM Integration consists of two parts. A web service which users access to work with the PDM Integration and a background service which manages communication between Monitor ERP and the web service for the PDM Integration. Both services are installed as Windows services, often on the application server (the Monitor server) on the customer’s internal network (LAN). You are however able to install the PDM Integration on a separate server as long as it can communicate with the API from the server. You are also able to split the installation of the web service and the background service. These services are installed by Monitor’s technical support. This in performed by remote access via a program named Splashtop.

## PDM Integration URL/domain name and port
The web service for the PDM Integration needs to be open for users that will work in the program. This is why a URL/domain name and open port are needed. The web service is by default installed on http://localhost:10XXX, and the XXX is the company number in Monitor ERP that the PDM Integration should be linked to. Both the URL and port can be changed if needed. It’s also recommended to run HTTPS which means that an SSL certificate is required. The customer’s IT department or IT supplier is responsible for ensuring that the server that the program is installed on answers the selected port, and that the SSL certificate is installed on the server for the PDM Integration if it is not already installed. See the description below of the SSL certificate.

## Shared file area
The communication between the PDM system and the PDM Integration is file-based. Due to this, a shared file area is required that both the background service for the PDM Integration and the PDM system have write permission for. The user running the background service for the PDM Integration can be changed if needed to make it easier to manage write permission for the service.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PDM_installation2.png)

## System recommendations
Our system recommendations for Monitor ERP also cover the system recommendations for the PDM Integration. These can be found here:
[https://www.monitorerp.com/support/system-recommendations/](https://www.monitorerp.com/sv/support/systemrekommendationer/)
If you have questions regarding hardware for PDM Integration, please contact the Monitor Support Center by phone: +46 650 766 03 or by e-mail: support@monitorerp.com.

## SSL certificate
An SSL certificate for the PDM Integration is not necessary, but is recommended.
1. Purchase an SSL certificate for the server that the PDM Integration will be installed on. The certificate should be issued by a certificate authority such as Verisign, Go Daddy, or Comodo. Certificates are either issued for the server's DNS name (e.g. "monitorportal.yourcompany.com") or for an entire domain (as a so-called wildcard certificate "*.yourcompany.com").
2. Once you have the certificate, you copy the file to the server for the PDM Integration.

## Overview
Below you will find an overview of what a typical PDM Integration set-up looks like:
- SHARED FOLDER is the shared file area.
- MONITOR PDMI G5 SERVICE is the background service.
- MONITOR PDMI G5 CLIENT is the web service.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PDM_installation.png)
