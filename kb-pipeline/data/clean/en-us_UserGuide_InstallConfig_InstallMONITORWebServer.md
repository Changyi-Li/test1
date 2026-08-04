# Installation of web server for Monitor Mobile
> Please note that these installation instructions are for the web server for Monitor Mobile.

## Preparations
1. Copy the installation file called MONITOR Web Server Setup.exe and the license file MONITOR Certificate - [your system name].rsa for your Monitor system, to a folder on the computer which should be the web server. You can find the file in the server installation file MONITOR Server.
2. Close all other programs on the computer before you start the installation.

## Installation on application server (the Monitor server)
> Follow this guide if mobile clients should only be used locally in the network (for example by personnel who will be recording attendance/work or performing stock reporting using a smartphone/tablet, connected with wifi).
1. Start the web server installation using the file MONITOR Web Server Setup.exe.
2. If the window User Account Control is shown, you should allow the installation to make changes on the computer. Click Yes in that window.
3. In the window called Monitor Web Server Installation which is shown, click Next to start the installation.
4. In the next step you should click the Browse button ... And choose the same license file MONITOR Certificate - [your system name].rsa which was used during the installation of the application server (the Monitor server). Click on Open after you have selected the license file and then click Next.
5. In the next step, you select which Monitor server the web server should use. The default setting Find the Monitor server automatically is recommended. Then click Next.
6. In the next step you select in which path to install the web server. It is recommended to install it in the default path. Click Next.
7. In the next step you enter which port the web server should use to listen for inbound traffic from web clients and apps. Port 443 is set by default. This is the standard port for https (that is, encrypted traffic via SSL).
1. Uncheck Use https, as this is normally not needed when web clients should only be used locally in the network. In doing so, the port is automatically changed to 80, which is the standard port for http (that is, unencrypted traffic).
2. Enter Username, Password, and Confirm password, for the domain administrator account in Windows which will run the web server service. You can use the same account that runs the service for the application server (the Monitor server). Then click Next.
8. In this step you enter which port should be used for the web server's updating service, which is also installed in this installation. The updating service is used to keep the web server updated with the same version as the application server. Port 8714 is set by default. It is recommended you use the default port.
1. Also enter IP address for the web server if this is not prefilled. This address uses the application server when sending update notifications to the web server. Then click Next.
9. Now you will see a summary of the configurations made. If you should regret a selection made up till now, it is possible to go back using the Back button. But if everything is OK, you should click Next to start the installation.
10. Finally, you should finish the installation by clicking Finish.

## Installation on separate computer in DMZ
> Follow this guide if you want it to be possible to use the mobile clients outside the network as well (for example by sales representatives who are visiting customers and want to access quotes, customer orders, and invoices, on a smartphone/tablet, connected to mobile network).
1. Start the installation of the web server in the same way as described above, under Installation on application server (the Monitor server). There you should follow steps 1-6 and then you should follow the description you find here.
2. In this step you enter which port the web server should use to listen for inbound traffic from mobile clients and apps. Port 443 is set by default. This is the standard port for https (that is, encrypted traffic via SSL). It is recommended you use this port. If you use a different port for https you must also remember to make this change in the firewall configuration.
1. Here you should keep the Use https setting activated.
2. Enter Username, Password, and Confirm password, for the domain administrator account in Windows which will run the web server service. You can use the same account that runs the service for the application server (the Monitor server). Then click Next.
3. In the next step you should link the web server to the SSL certificate which has been purchased for the computer (to be able to use https on their web server's port). Click the button … and select the certificate file (.cer) where you saved it on the computer. This is done by marking it and click on Open. Then click Next.
4. In this step you enter which port should be used for the web server's updating service, which is also installed in this installation. The updating service is used to keep the web server updated to the same version as the application server. Port 8714 is set by default. It is recommended you use the default port. If you use a different port you must also remember to make the change in the firewall configuration!
1. You can here leave the Use https setting deactivated, since it is not necessary for this internal traffic between web server and application server. If you activate the setting, the same certificate file will be used as in the previous steps 2-3.
2. In this step you also enter the IP address for the web server if this is not prefilled. This is the address the application server will use to send update notifications to the web server.
3. Then click Next.
5. Now you will see a summary of the configurations made. If you should regret a selection made up till now, it is possible to go back using the Back button. But if everything is OK, you should click Next to start the installation.
6. Finally, you should finish the installation by clicking Finish.

## Verify the installation
1. Start a Monitor ERP Windows client and open the procedure called System settings. Go to the tab System overall and scroll down to the heading Automatic update of adaptations. Check that there is a row with URL and Authentication key entered for the web server in the table.
2. Mark the row in the table and click the button Verify connection ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_test_call.png) to check that the communication with the web server works.
