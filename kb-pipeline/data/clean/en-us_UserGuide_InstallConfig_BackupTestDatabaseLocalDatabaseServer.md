## Backup/test company with a separate database server
> This instruction is recommended for backup of company databases, when SQL Anywhere Database Server is installed on a separate server computer, and not the application server (the Monitor server). The instruction is also recommended for creating and scheduling copying of company databases to test companies on the separate server computer. In both cases, the SQL Anywhere backup tool is used to run backup and copying tasks on the database server.
Copy SQL Anywhere backup tool to the database server
Firstly you must copy the SQL Anywhere backup tool to the database server, to be able to create and run backup tasks and copying tasks locally on the database server.
If the SQL Anywhere backup tool is already on the database server, check that the backup tool has the same version as on the application server (hereinafter referred to as the “Monitor server”). If not, the backup tool must be copied once again.
1. Open the Explorer in Windows on the Monitor server and go to the folder called C:\Program Files (x86)\Monitor ERP System AB\MONITOR Installation Manager.
2. Copy the sub-folder called SqlAnywhereBackupTool to a network resource or a USB memory.
3. Go to the root folder C:\Program Files (x86)\Monitor ERP System AB for the Monitor server.
4. Also copy the file certificate.rsa to the SqlAnywhereBackupTool folder on the network resource or the USB memory stick.
5. Open the Explorer in Windows on the database server where the SQL Anywhere database engine and company databases are installed.
6. Copy the folder called SqlAnywhereBackupTool from the network resource or the USB memory stick to C:\ on the database server. This will create the path C:\SqlAnywhereBackupTool.
Create and schedule backup manually with Task Scheduler in Windows
This is a method for manually creating and scheduling backup tasks on the Monitor server. There is also an alternative method for creating and scheduling backup tasks with Monitor ERP Installation Manager on the Monitor server. See below.
1. Open the Task Scheduler in Windows on the database server.
2.    
Create a folder named Monitor ERP System AB under Task Scheduler Library in the left-hand section. Right-click Task Scheduler Library and select New folder... and give the new folder the name.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup1.png)
3.    
When you have marked the Monitor ERP System AB folder, select Create Basic Task... In the right section called Actions.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup2.png)
4.    
Enter a name and a description for the activity in the dialog that appears. Click Next >.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup3.png)
5.    
Choose when to run the activity. Daily is the default and recommended option for backup of databases. For copying to test company you choose one of the options regarding how often you want to copy to the test company. Click Next >.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup4.png)
6.    
In Start you select date and time for when the activity should start. In the Recur every field you enter how often the activity should be repeated. It is recommended to run the activity every day when backup is concerned. When copying to test company is concerned, you can enter any interval of your choice. Click Next >.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup5.png)
7.    
Choose Start a program for the activity. Click Next >.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup6.png)
8. Click the Browse... button and select the Monitor.SqlAnywhere.BackupTool.exe file in the folder called SqlAnywhereBackupTool.
9. In the Add arguments field you need to add arguments according to [the following example](ArgumentsSQLAnywhereBackupTool.htm).
10.    
Leave Start in empty. Click Next >.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup7.png)
11.    
Activate the Open the Properties dialog for this task when I click Finish checkbox. Click Finish.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup8.png)
12.    
Click the Change User or Group... button in the dialog which opens, and enter the Windows account that will run the activity. It is normally the same account which runs the service for the Monitor server or an administration account. Also activate the Run whether user is logged on or not and Run with highest privileges settings. Click the Settings tab.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup9.png)
13.    
Activate the setting called Run task as soon as possible after a scheduled start is missed. Then click OK.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup10.png)
14.    
Finally, this dialog window is displayed where you have to enter the password for the Windows account that will run the activity. Then click OK.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup11.png)
Create and schedule backup with Monitor ERP Installation Manager
This is a method for creating and scheduling backup tasks with Monitor ERP Installation Manager on the Monitor server, and then exporting to the database server.
1. Follow the instructions under the heading Copy SQL Anywhere backup tool to the database server, if this has not already been done.
2. Then follow the instructions in the section [Create and schedule backup](CreateScheduleBackup.htm).
3. The backup task will now be exported in order to be copied to the database server. Open Task Scheduler in Windows on the Monitor server.
4. Select the folder in Task Scheduler where the task is saved, normally Monitor ERP System AB.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup1.png)
5.    
The tasks in the folder are shown in the box on the right. Select the task which is to be exported.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup12.png)
6.    
Select Export... and then save the backup task on disk as an XML file.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup15.png)
7.   
If there are more backup tasks to be exported, repeat steps 5–6, above, for those tasks.
8. Please note! Then delete the backup task in Task Scheduler on the Monitor server. This is important in order than no one can then trigger backup runs from the Monitor server.
9. Copy the exported XML files to any folder on the database server.
10. The backup task will now be imported to the database server. Open the Task Scheduler in Windows on the database server.
11.    
Create the folder Monitor ERP System AB under Task Scheduler Library in the left-hand section. Right-click Task Scheduler Library and select New folder... and give the new folder the name.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup1.png)
12.    
Select the folder and then choose Import Task... in the box on the far right.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup16.png)
13. In cases where the backup task is set up in the Installation Manager on the Monitor server to be run across the network to the database server, you must replace the UNC file paths with local file paths in the backup task. This is done in the Add arguments field (see point 9 above, under the heading Create and schedule backup manually with Task Scheduler in Windows).
14. Also check the other arguments in the field Add arguments in the backup task. You can then add arguments for if and when e-mails will be sent when the backup task is run. See the following [section](ArgumentsSQLAnywhereBackupTool.htm) on the arguments available.
Create and schedule copying to test companies with Monitor ERP Installation Manager
When you have a separate database server, test companies and copying tasks for test companies must always first be created with the Monitor ERP Installation Manager on the Monitor server, and then exported to the database server. This is to ensure a record for each test company is created in the system’s configuration file.
1. Follow the instructions under the heading Copy SQL Anywhere backup tool to the database server, if this has not already been done.
2. Then follow the instructions in the section [Create test databases](CreateTestDatabases.htm).
3. Then, follow the instructions in steps 3–4, above, under the heading Create and schedule backup with Monitor ERP Installation Manager).
Run backup or copying tasks manually with Task Scheduler in Windows
If you have created a backup task or copying task which is not scheduled, or if you want to run the task manually at one time, you must run it with Task Scheduler on the database server.
1. Connect a remote desktop to the database server with Remote Desktop Connection in Windows, or an equivalent program for remote connection.
2. Follow the instructions in steps 1–2 under the heading Change a backup or copying task with Task Scheduler in Windows.
3.    
Then select Run for the selected tasks in the box on the far right.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup18.png)
Change a backup or copying task with Task Scheduler in Windows
If you later need to change a backup task or copying task you can do so with Task Scheduler on the database server.
1.    
Select the folder in Task Scheduler where the task is saved, normally Monitor ERP System AB.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup1.png)
2.    
The tasks in the folder are shown in the box on the right. Select the current task.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup12.png)
3.    
Then choose Properties for the selected task in the box on the far right.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup13.png)
4.   
Make your changes to the task in the dialog which is shown, and then click OK to save.
Remove a backup or copying task with Task Scheduler in Windows
If you later need to remove a backup task or copying task, you can do so with Task Scheduler on the database server.
1.   
Follow the instructions in steps 1–2 under the heading Change a backup or copying task with Task Scheduler in Windows.
2.    
Then choose Delete for the selected task in the box on the far right.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup14.png)
3.    
Select Yes in the dialog which is shown to delete the task.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/SQLAnywhereBackup17.png)
