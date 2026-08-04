# Relocation from SQL Anywhere to SQL Server
This instruction describes relocation of the Monitor ERP database server from SAP SQL Anywhere to Microsoft SQL Server.

## Requirements
Monitor ERP supports versions of av Microsoft SQL Server which are included in the Microsoft Mainstream support. The version you use should always include the latest updates.
Microsoft SQL Server 2025 is at present only available as a pre-release version. That is why it is not included in our recommendations yet.
Microsoft SQL Server is installed by your IT partner on a separate server computer, unless you already have an existing SQL Server which will run the Monitor ERP databases.
Your SQL Server must have the setting SQL Server and Windows Authentication mode activated on the Security page in Server Properties.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLServerRequirement.png)
We recommend that you configure the same character set (collation) in SQL Server which the databases have in Monitor ERP. The character set to be chosen depends on the country package included in the your Monitor ERP, as shown below:
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
> If the country package you use in Monitor ERP is not listed above, contact the Monitor Support Center.

## Options and adaptations in Monitor ERP
> Please note! If you have options or adaptations in your Monitor ERP system, these must be handled separately in the process when moving from SQL Anywhere till SQL Server. Options include Machine integration, Bank integration, Webshop and Vertical Storage Lift Integration, for example. If you have options, contact the Monitor Support Center at support@monitorerp.com Adaptations include reports, dashboards and blackbox, for example. If you have adaptations, contact Monitor’s Adaptation Department at adaptation@monitorerp.com and include your company and contact details. The department will get back to you with a quote, and the time they estimate the work will take to complete. The costs associated with modifying existing adaptations to ensure they work with SQL Server are not covered by the update agreement for adaptations. You are also recommended to set up a test environment in Monitor ERP which you move to SQL Server, where you then test and verify all the options, adaptations and daily routines in Monitor ERP.

## Preparations
You must first modify the file MonitorCompanyConfiguration.json in the Monitor ERP System AB folder. This folder is usually found in the path C:\Program Files (x86)\.
In older installations there is only a connection for SQL Anywhere in a "ConnectionString” property in the file. The connection must then be moved to a new "ConnectStrings” property. For the previous "ConnectString” property, set the value to “null”. See the example below:
"ConnectString": null,
"ConnectStrings": {
"SqlAnywhere": "ASTART=NO;ENG=MonitorG5_MyServerName",
},
A row should be added under “ConnectStrings” for SQL Server. See the example below:
"ConnectStrings": {
"SqlAnywhere": "ASTART=NO;ENG=MonitorG5_MyServerName",
"MicrosoftSqlServer": "integrated security=SSPI;data source=DbServerName,1433"
},
The value for “data source” is the name of your SQL Server. You can enter the name either as [DbServerName]:[Port] or as [DbServerNname]\\[SQLServerInstanceName]. In the above example, SQL Server listens to connections to port 1433.

## Create login for Monitor ERP in SQL Server
The next step is to run the program Monitor.DbConnectionManager.exe in the Monitor ERP System AB\MONITOR Server folder, in order to create logins for Monitor ERP in SQL Server. When logging in to the program, you must use an account which has the server role "sysadmin” in SQL Server.
Start the program and log in with the user name and password for the account which has this user right.
You then select Generate new passwords at the top, and then Save. You will then have generated passwords for the logins required for Monitor ERP on SQL Server.
> This is an important step, as these logins must be present when you create the SQL Server database during the database portation.

## Database portation
Database portation from SQL Anywhere to SQL Server database is run with the program Monitor.DatabasePortation.Console.exe in the folder Monitor ERP System AB\MONITOR Server on the application server (Monitor server). The program is run in a console window.
> Please note! Before you port a database you must ensure the database and application server (Monitor server) where the program Monitor.DatabasePortation.Console.exe are run have the same version. This is to ensure tables and columns in the database are matched correctly. Only standard tables and columns in the database are included during the database portation. If you have options or adaptations in your Monitor ERP system you must firstly contact the Monitor Support Center or Adaptation department. See under Options and adaptations in Monitor ERP, above, for details. Under no circumstances may users or other programs be connected to the database! If data is changed or added upon database portation, this causes problems with the database.
You open Windows Command Interpreter (cmd.exe) as Administrator in the folder above, and enter a command according to the examples below:
Port database 001 to a database in the same name 001 on SQL Server:
Monitor.DatabasePortation.Console -c 001
Port database 001 to a database with the name Monitor001 on SQL Server:
Monitor.DatabasePortation.Console -c 001 -n Monitor001
Port database 001 to a database with the name Monitor001 on SQL Server, and with the file path e:\data for temporary files:
Monitor.DatabasePortation.Console -c 001 -n Monitor001 -f e:\data
To see all arguments supported in the program, enter the command:
Monitor.DatabasePortation.Console
You run the command for the databases that will be ported to SQL Server. It is possible to run a hybrid environment, with certain databases on SQL Anywhere and certain databases on SQL Server.
> Please note! The SYS database must also be ported to SQL server in the same way.
During database portation, all standard tables in the source database are exported to temporary files and then imported to the target database in SQL Server. After the import, all files are deleted automatically. The database portation therefore requires that there is at least as much free disk space as the size of the source database.
During database portation, all logins are linked in the target database which was created by the program Monitor.DbConnectionManager.exe.
> The program Monitor.DatabasePortation.Console.exe can also be used in other contexts in order to port a database from SQL Server to SQL Anywhere, or to [reduce the size](../../GeneralRegisters/SystemMaintenance/DatabaseAdministration/bChangeBLOBStorageLocation.htm) of an SQL Anywhere database.

## Connection to SQL Server
You now have a database for Monitor which is run on SQL Server, however, you need to make a change in the file MonitorCompanyConfiguration.json in order that the application server (Monitor server) can connect to the database on SQL Server. You must change "DatabaseName" and "Dialect" in the file for each database which has been ported to SQL Server. You should also do this for the SYS database. See excerpt from the file below:
"Databases": [
{
"Number": "SYS",
...
"DatabaseName": "SYSDatabaseNameInSQLServer",
...
"Dialect": 1,
...
},
{
"Number": "001",
...
"DatabaseName": "001DatabaseNameInSQLServer",
...
"Dialect": 1,
...
Now that everything is complete, you can start the Monitor ERP clients and test to make sure you can work in the ported databases Monitor ERP.
