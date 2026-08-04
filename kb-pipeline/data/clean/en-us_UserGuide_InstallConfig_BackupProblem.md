### Backup problem
There appears to be a problem with your backup. No new backups have been carried out for some time, and you need to investigate the situation. Please follow the action list below. If no obvious reasons for the problem can be found and you are unsure how to handle the situation, please contact the Monitor Support Center!
> Please note! Important! Do NOT restart the SQL Anywhere database server. This may, in some cases, result in loss of data.
- Go to the database backup in your selected backup directory and verify that it is not up to date. If so, check when the backup stopped working. You find the path to the backup folder in the backup task in the Installation manager. A log file is created in the backup folder each time the backup is run. It is called monitor[date time].log. This way you see in the file name when the backup task was most recently run.
- Check if there are any errors in backup logs. Under the Backup tab in the Installation Manager there is a button which leads to the folder where backup logs for SQL Anywhere are saved. The default folder is [Unit]:\[Program folder]\Monitor ERP System AB\MONITOR Installation Manager\SqlAnywhereBackupTool\Logs. The errors found in backup logs may highlight and point you in the right direction regarding the cause of the problem, and it is good if you have checked these logs before contacting the Monitor Support Center.
- Check your access (user rights) to the selected backup folder. The user selected to run the backup task must have write permission in that folder. If you have entered a path other than the default path, access may be denied, in which case the backup task will not run successfully.
- Check if there is a scheduled backup – does the scheduling look correct? Check this by opening the MONITOR Installation Manager and changing to the Backup tab. If there are one or more backups present and they haven’t run, you will need to investigate further. In that case, please contact the Monitor Support Center.
Contact information to Monitor Support Center:
Phone: +46 (0)650-766 03
E-mail: [support@monitor.se](mailto:support@monitor.se)
Website (Swedish): [monitorerp.com/sv/support/](https://monitorerp.com/sv/support/)
Website (English): [monitorerp.com/en/support/](https://monitorerp.com/support/)
