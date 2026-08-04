### Transfer of backup to new solution
In a newly launched version of Monitor Installation manager, your existing backup tasks (and copying tasks of test companies) will be transferred to a new solution. In the new way of working, the tasks will run in the background by the Windows Task Scheduler and not by the Monitor server (the application server).
This is how you transfer your tasks:
1.    
Start the Installation manager on the Monitor server and the following dialog will appear. Click OK.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/TransferBackup1.png)
2.    
In the next step you enter name and password for the Windows account that will run the tasks in the Task Scheduler in Windows. By default you see the name of the logged in account in Windows. Click Next to start the transfer.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/TransferBackup2.png)
3.    
In the next step the transfer of backup tasks and copying tasks of test companies will begin automatically. The tasks which have been transferred are displayed with a green check mark ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) in the dialog when they are completed. Finally, click Finish.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/TransferBackup3.png)
