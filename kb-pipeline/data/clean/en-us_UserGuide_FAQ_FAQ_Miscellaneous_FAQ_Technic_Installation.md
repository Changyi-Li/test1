### FAQ – Technical questions and installation
How do I update Monitor ERP to a new version?
Here you can read how to update Monitor ERP to a [new version](../../InstallConfig/UpdateMONITOR.htm).
How do I install Monitor ERP Web server?
Here you can read how to install Monitor ERP [Web server](../../InstallConfig/InstallMONITORWebServer.htm).
How do I install BI server?
Here you can read how to install [the BI server](../../InstallConfig/InstallMonitorBIServer.htm).
How do I create a test company?
You can read more about creating a [test company](../../InstallConfig/CreateTestDatabases.htm) here.
What is the purpose of a test company?
Test companies are used for training purposes or for carrying out tests that should not be performed on company databases. You can, for example, test new features or work flows in Monitor ERP before you start using them for real.
Where do I find backup files?
1. Start the Monitor ERP installation manager on the application server.
2. Go to the Backup tab.
3. Mark the backup task and press the Edit backup button.
4. Under the Settings tab you can see Standard path for backup files where backup files are saved. This applies if Monitor ERP Server is installed for SQL Anywhere.
I’ve got a link from support to upload to a database. How do I do it?
If you’re using SQL Anywhere database, do the following:
1. Go to General registers | Database administration and select the Uploading of database tab.
2. In the Link for uploading file to Monitor (link provided by the Monitor Support Center) field, paste the whole code key (token) that you received from the Monitor Support Center.
3. The field contains a pre-filled web address to Monitor's file server. This cannot be deleted. The code key you have received is unique for your system. When you paste it in the field it will be added to the pre-filled web address.
4. Press Tab or Enter when you have pasted the link (the code key) you have received from us. If the code key is correct, a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) is shown next to the field.
5. Click the button Upload database ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_upload.png) on the toolbar.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Database_upload.png)
> If it is an SQL Server database, you need to upload the file manually, via the link you have received from the Monitor Support Center. Or you may have to contact your IT department or ERP manager.
How do I print from Monitor Mobile?
To be able to print from Monitor Mobile, you first need to register a so-called “server printer” in the Server printer procedure. You can read [more](../../../GeneralRegisters/BasicSettings/ServerPrinters/wServerPrinters.htm) here.
After that you have to register server printer for the users who should be able to print from Monitor Mobile under the Printers tab i the Users procedure. You can read [more](../../../GeneralRegisters/UserPersonnel/Users/bPrinters.htm) here.
When my company is the customer, what do I have to do to activate a partner solution in Monitor ERP?
1.    
Log in and sync
- Log in to Monitor ERP.
- Make sure the system is synchronized.
2.    
Go to Security settings
- Go to the Security settings procedure in the General registers module. Select the Partner solutions­. Please note that the Partner solutions tab will only be visible once the solution has been delivered.
3.    
Create new row
- Click the button called Add new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png).
- Name: This is where you name the API key. Use a clear name so that it is easy to understand which solution the key belongs to.
- Access key: The generated access key that should be copied into the solution’s integration settings.
- Access key expiration date: The default validity period is 6 months. It is possible to unlock the field and change the expiration date. When the expiration date is closing in, you will receive a message and you can choose to extend the date or to generate a new key.
4.    
Open the firewall
-    
Make sure that TCP port 8001 is open in your firewall in order to let your system communicate with the partner solution. For additional security: Only allow traffic from the partner’s IP addresses.
If you are using Monitor Cloud, our Monitor Support Center will help you with this.
5.    
Create a user
-   
Create a regular user. The user does not have to have a license or any specific user rights in the Monitor ERP.
6.    
Provide info to the partner
- Provide the partner with the generated access key.
- Share the login information (user name and password) for the user you have created. The user does not need a license or any special user rights in the Monitor ERP.
