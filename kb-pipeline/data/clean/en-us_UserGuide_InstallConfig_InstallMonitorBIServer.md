# Installation of Monitor BI Server

## Preparations
You must have Monitor ERP version 24.5 or later installed.
1. Copy the installation file named MONITOR BI Server Setup.exe. You can find the file in the server installation file MONITOR Server. Also copy the license file MONITOR Certificate - [your system name].rsa for your Monitor system, to a folder on the computer which should be the BI-server.
2. To run Monitor BI, the computer must have Microsoft Windows Desktop Runtime 8 (x64) and Microsoft ASP.NET Core 8.0.3 (x64) – Shared Framework is installed. Both are required and need to be the same version. We recommend that you install the latest version of Microsoft Windows Desktop Runtime 8 (x64) and Microsoft ASP.NET Core 8 (x64) – Shared Framework.
> Please note! Remember to check whether the standard port 443 and 80 is available and that it is not already being used by another service. If the standard port is already being used, choose another port that isn’t being used.

## Choice of installation
You can choose to install Monitor BI Server on the application server (the Monitor server) or on a separate server computer. Follow the guide Installation on the application server if Monitor BI will only be used locally in the network. Follow the guide Installation on a separate server computer to install Monitor BI on a separate server computer. This can be a good option if you wish to relieve the load on the server where the application server (the Monitor server) is run. If you install Monitor BI on the same server as the application server, intense use of Monitor BI may affect the performance of the rest of Monitor ERP. An installation on a separate server computer is mainly recommended for larger Monitor ERP systems which handle large amounts of data and/or many users.

## Installation on application server (the Monitor server)
1. Start the installation of Monitor BI Server with the file MONITOR BI Server Setup.exe.
2. If the window User Account Control is shown, you should allow the installation to make changes on the computer. Click Yes in that window.
3. In the window called Monitor BI Server Installation, click Next to start the installation.
4. In the next step you should click the browse button ... and select the license file MONITOR Certificate - [your system name].rsa. Click on Open after you have selected the license file and then click Next.
5. In the next step, you select which Monitor server the BI server should use. The default setting Find the Monitor server automatically is recommended. Then click Next.
6. In the next step you select in which path to install the BI Server. It is recommended to install it in the default path. Click Next.
7. In this step you enter which port the BI server should use to listen for inbound traffic from BI clients. Port number 443 is selected by default. This is the standard port for https (encrypted communication via SSL). 
1. Deactivate the setting Use https, as it is generally not a requirement when Monitor BI will only be used locally in the network. In doing so, the port is automatically changed to 80, which is the standard port for http (that is, unencrypted traffic).
2. Enter Username, Password, and Confirm password, for the domain administrator account in Windows which will run the BI service. You can use the same account that runs the service for the application server (the Monitor server). Then click Next.
8. Here you choose which port should be used for the updating service for Monitor BI which is also installed in this installation. The updating service keeps Monitor BI updated with the latest version. Port 8007 is selected by default and we recommend that this is used.
9.     
In the next step, you select which database engine to use for Monitor BI.
> SQLite is the database engine which is easiest to install and handle/maintain. SQLite is best suited for Monitor ERP systems with up to 20 users. Larger systems are recommended to use Microsoft SQL Server or PostgreSQL. If you have experience with SQL Server and are already using that database engine for Monitor ERP, this is a good choice. If not, we recommend PostgreSQL.
1.   
SQLite – This alternative does not require any external database engine installation.
2.   
PostgreSQL – This alternative requires an external installation of PostgreSQL version 16 or later and you also need to create a database and account before you continue with the installation. Please see [this guide](InstallMonitorBIWithPostgreSQL.htm).
3.   
Microsoft SQL Server – This alternative requires an external installation of Microft SQL Server and you also need to create a database and account before you continue with the installation.
10. Enter Host, Port, Database name, Username and Password if you have selected PostgreSQL or Microsoft SQL Server as database engine. If you have selected SQLite, this step will not be shown and the installation will instead continue to the next step.
11. Now you will see a summary of the configurations made. If you should regret a selection made up till now, it is possible to go back using the Back button. But if everything is OK, you should click Next to start the installation.
12. Finish the installation by clicking Finish.

## Installation on a separate server computer
1. Start the installation of Monitor BI Server with the file MONITOR BI Server Setup.exe.
2. If the window User Account Control is shown, you should allow the installation to make changes on the computer. Click Yes in that window.
3. In the window called Monitor BI Server Installation, click Next to start the installation.
4. In the next step you should click the browse button ... and select the license file MONITOR Certificate - [your system name].rsa. Click on Open after you have selected the license file and then click Next.
5. In the next step, you select which Monitor server the BI server should use. The default setting Find the Monitor server automatically is recommended. Then click Next.
6. In the next step you select in which path to install the BI Server. It is recommended to install it in the default path. Click Next.
7. In this step you enter which port the BI server should use to listen for inbound traffic from BI clients. Port number 443 is selected by default. This is the standard port for https (encrypted communication via SSL) and we recommend that you use this. If you use a different port for https you must also remember to make this change in the firewall configuration.
1. The setting Use https should be activated.
2. Enter Username, Password, and Confirm password, for the domain administrator account in Windows which will run the BI service. Then click Next.
8. In the next step you should link the BI server to the SSL certificate which has been purchased for the computer (to be able to use https on their BI server's port). Click the Choose certificate … button and select the certificate file (.cer) where you saved it on the computer. This is done by marking it and clicking on Open. Then click Next.
9.      
At this step, you select which database engine to use for Monitor BI.
> SQLite is the database engine which is easiest to install and handle/maintain. SQLite is best suited for Monitor ERP systems with up to 20 users. Larger systems are recommended to use Microsoft SQL Server or PostgreSQL. If you have experience with SQL Server and are already using that database engine for Monitor ERP, this is a good choice. If not, we recommend PostgreSQL.
> Please note! If you’re using SQLite as a database engine, it should be installed on the same computer as the BI server and be reachable via the internet. This poses a slight security risk.
1.   
SQLite – This alternative does not require any external database engine installation.
2.   
PostgreSQL – This alternative requires an external installation of PostgreSQL version 16 or later and you also need to create a database and account before you continue with the installation. Please see [this guide](InstallMonitorBIWithPostgreSQL.htm).
3.   
Microsoft SQL Server – This alternative requires an external installation of Microft SQL Server and you also need to create a database and account before you continue with the installation.
10. Enter Host, Port, Database name, Username and Password if you have selected PostgreSQL or Microsoft SQL Server as database engine. If you have selected SQLite, this step will not be shown and the installation will instead continue to the next step.
11. Now you will see a summary of the configurations made. If you should regret a selection made up till now, it is possible to go back using the Back button. But if everything is OK, you should click Next to start the installation.
12. Finish the installation by clicking Finish.

## Verify the installation
1. Start a Monitor ERP Windows client and open the System settings procedure. Go to the tab System overall and scroll down to the heading Automatic update of adaptations. Check that there is a row with URL and Authentication key entered for the BI server in the table.
2. Select the row in the table and click the button Verify connection ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_test_call.png) to check that the communication with the BI server works.
3. The MONITOR BI Server and MONITOR Product Updater services have been installed.
> Note the communcation protocoll, server name/IP address, and port for the installation and inform the users that will access Monitor BI.

## Getting started
Before you can log in to Monitor BI, the user in Monitor ERP must be assigned the role called ERP manager or System administrator. The user in Monitor ERP must also have a password and the license type called Complete or Daily management.
To start the BI client, you write the IP address for your selected BI server in the browser’s address bar. When you are logged in, you can – as a Monitor BI administrator – give other Monitor ERP users access to Monitor BI.
