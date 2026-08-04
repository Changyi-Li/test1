### How to install PostgreSQL for use with Monitor BI

#### Preparations (Windows)
1.   
Go to the [official download site](https://www.postgresql.org/download/windows/) for PostgreSQL.
2.   
Click the Download the installer link to download the installation file. Version 18 or later is required.

#### Installation description
Run the downloaded file and follow the installation guide below.
1.     
Select which components to install. PostgreSQL Server is required for the installation. The other components can be useful for database management. When you have selected which components to install, click Next.
> When the installation is finished you can use pgAdmin 4 (if you installed that application). The pgAdmin 4 application is a graphical tool for managing and developing your database. It is included in the installation package you downloaded.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SelectComponentsPostgreSQL.png)
2.    
Select a directory for PostgreSQL data and then click Next.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/DataDirectoryPostgreSQL.png)
3.     
Enter a password for the PostgreSQL superuser and then click Next.
> Please note! Make sure to remember the password you choose. The password cannot be changed if you forget it.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PasswordPostgreSQL.png)
4.    
Enter the port number (the standard port is 5432), then click Next.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PortPostgreSQL.png)
5.    
Enter your locale/region, then click Next.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/AdvancedOptionsPostgreSQL.png)
6.   
Make sure everything is entered correctly in the summary, then click Next.
7.   
When the installation is finished, you can choose if Stack builder will be used to download additional tools, drivers, and applications to complement the PostgreSQL installation. Finish the installation by clicking Finish.

### Configure user and database in PostgreSQL
> Please note! This is only an example to illustrate how you can configure a user and a database in PostgreSQL to use with Monitor BI. The guide assumes that you install PostgreSQL on the same server as Monitor BI.
1.   
Start pgAdmin4.exe (for example: D:\PostgreSQL\pgAdmin4\runtime\pgAdmin4.exe).
2.    
Right-click Login/Group Roles and select Create - Login/Group Role. Then create a username. In our example we will create the user BIuser.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LoginGroupRolePostgreSQL.png)
3.   
Right-click the user you’ve created and select Properties.
4.    
In order for the user to be able to authenticate and run the service, you need to add a password for the user under the Definition tab. Then click Save. Under the Privileges tab, it is sufficient that the Can login setting is activated for the user.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/DefinitionPostgreSQL.png)
5.   
Right-click Databases, then Create and then Database.
6.    
Under the General tab, you enter the database name in the Database field and the name of the user in the Owner field. Then click Save. In our example, we have chosen the database name BusinessIntelligence.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/DatabaseOwnerPostgreSQL.png)
7.     
Run the file named MONITOR BI Server Setup.exe and install following the [instructions](InstallMonitorBIServer.htm). Select PostgreSQL as database. When you reach the step Database settings – PosgreSQL, you fill out the fields with the following information:
-   
Host: localhost
-   
Port: 5432
-   
Database name: BusinessIntelligence (only an example name)
-    
Username: BIuser (only an example name)
> Please note! Names in PostgreSQL are case sensitive.
-   
Password: The password you chose for BIuser
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/DatabaseSettingsPostgreSQL.png)
8.   
Right-click the two services Monitor BI server and Monitor Product Updater and select Properties. Under the setting Startup type, select Automatic (Delayed Start).
