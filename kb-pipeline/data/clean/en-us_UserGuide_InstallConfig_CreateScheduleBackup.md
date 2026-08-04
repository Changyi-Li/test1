### Create and schedule backup
> This instruction applies when the application server (Monitor server) and SQL Anywhere database server are run on the same server computer (standard installation). Monitor ERP Installation manager is used to create and schedule backup of the company databases. If the SQL Anywhere database server is to be run on a separate server computer, follow the instructions here: [Backup/test company with separate database server](BackupTestDatabaseLocalDatabaseServer.htm). If Microsoft SQL Server is to be used, backup of the company databases is run in the regular tool for database backup on SQL Server.
Create backup task
1.    
Go to the Backup tab in the installation manager and click the button New backup task ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/BackupSettingsTab.png)
2.          
Under the Settings tab you enter a Name of scheduled task.
The default Backup directory for a new backup task is according to Standard path for backup files: in the Settings tab. This is where the backup files* are saved. You can select a different backup directory for this backup task.
The default Directory for backup logs corresponds to the Standard path for backup logs in the Settings tab. Text files with logs of each backup run are saved here.
Truncate log file (default) means the relevant log file "monitor.log” for the database is cleared of transactions after the backup task has been run. Truncation is recommend in order to minimize the size of the log file.
Validate backup means that the backup files are validated after the backup task has run. This validation is performed in a separate session of the database server and checks that the backup files are not corrupt.
Only backup of the log file means that only the log file "monitor.log" is included in the backup. A reason to activate this setting may be that you need to run backup tasks very frequently (e.g., every hour), because there are many transactions made in the database in a short time. Then you can choose to only backup the log file (which is quick to run a backup task on). If a reset should be necessary, it is possible to recreate the database by using the most recent regular backup task of the database file and log file, plus all the separate log files in chronological order for this backup task.
> Please note! A backup task which only backups the log file should be created as a separate backup task. For this backup task there must be a regular backup task which does not have this setting activated, and which runs, for example, 1 time per 24 hours.
Enter Use the following user account when running the task. By default, this is the user logged in to Windows on the server. However, you can use the Change user button in Windows to enter a different user. You can then enter the user’s password.
3.    
Under the Databases tab you mark the database to include in the backup task. This will activate the OK button. By clicking that button you will create a manual backup task. You must then enter the user’s password (see point 7 below). You run manual backup via the button Start ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_to.png) under the Backup tab in the installation manager.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/BackupDatabasesTab.png)
4.       
If you want to create a scheduled backup task, go to the Schedule tab instead of clicking the OK button. There you create the scheduling of the backup task. An alternative that you subsequently use the Edit backup task button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit.png) under the Backup tab.
Under the Schedule tab you activate Scheduled task.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/BackupScheduleTab.png)
Select Type. The options are Week, Month, and Last day of the month.
Enter a Time and the Days or Months on which the backup task should be performed. If Type has been set to Month, you also get to select a Date in the months when the backup task should be performed.
5.      
Under the E-mail tab you configure if and when e-mail should be sent in connection to when the backup task is run.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/BackupEmailTab.png)
Configure the Send e-mail regarding backup setting. Here you decide if an e-mail should be sent Always, In case of error, or Never. The default option is In case of error. This means an e-mail is sent only if the backup task failed. If you select Always, it means an e-mail will be sent also in cases when the backup task was been performed. Choose the Never option if you do not want an e-mail to be sent regardless of if the backup task has been performed or if it has failed.
Configure the E-mail setting to Standard or Manual. Standard is the default option and this will use the general e-mail settings for receiver and subject. If you select Manual, you can change this information in the To and Subject fields for the backup task in question. You can enter more than one e-mail address by separating them using semicolon (;) in the To field.
6.   
Click OK in the dialog in order to create the backup task. A scheduled task is then also created in the Windows Task Scheduler.
7.    
Finally, you must enter the Password for the selected user who will run the task. Then, click OK.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/UserCredentials.png)
> * The backup files are copies of the current database file "monitor.db" and the current log file "monitor.log” for the database. An additional copy is also created here of the current log file, with todays date and time in the file name; "monitorYYYY-MM-DD HHMMSS.log". This means that log file will never be overwritten when the backup task is run the next time. All files are saved in a sub-folder with the same name as the actual (live) database folder, for example "001". Please note! The backup files "monitor.db" and "monitor.log" are overwritten each time a backup task is run! That is why it is important to always backup the entire backup folder after the backup task has run. Save the backup copies in a protected location.
Change scheduled backup task
1. If you need to make changes to an existing backup task, you select the task under the Backup tab and click the Edit backup task button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit.png) (this button is active if you mark a backup task).
2. Make the changes you wish to do under the respective tabs Settings, Databases, Schedule, and E-mail, and then click the OK button.
3. When you have made the changed you must also transfer these changes to the task in the Task Scheduler in Windows. This is done using the Update the scheduled tasks button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) under the Backup tab.
General backup settings
The general backup settings concerns notifications sent via e-mail when running backup tasks, and when copying tasks for test companies. Here you can also configure settings regarding communication with your e-mail server. You only need to configure these settings once. These settings will then apply by default for all backup tasks and copying tasks for test companies, that you create.
1. Click the Backup settings... button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_settings.png) at the bottom left corner of the Backup tab in the installation manager.
2.    
Under the Notifications tab you can activate that notifications should be sent via e-mail to one or several receivers which have entered in the field. You can enter more than one e-mail address by using a semicolon (;) in the field to separate them. With the Test e-mail button you can send a test e-mail to receivers to test the function. Receiver/recipient of notifications can also be entered per backup task.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/BackupGlobalSettingsNotifications.png)
> Detailed information about successful and failed runs of backup task is saved in a log file for each backup task- You access such logs via the Logs button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_log.png) under the Backup tab.
3. Under the tab called E-mail settings you configure which Server (e-mail server) and Port to use to send notification via e-mail. You also enter a User name and Password for a Windows account which have permission to send e-mail via the entered e-mail server. In the Sender address field you enter an e-mail address which will function as the sender of the notifications. Activate Use SSL if the e-mail server requires it. Then you should also enter which Port the e-mail server uses for SSL.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/BackupGlobalSettingsEmail.png)
4. Click the OK button when you have completed the general backup settings.
