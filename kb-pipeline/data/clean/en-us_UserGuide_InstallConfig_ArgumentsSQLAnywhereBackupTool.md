### Arguments to Monitor.SqlAnywhere.BackupTool.exe
1. Mark all text from one of the examples below and copy it using Ctrl + C.
2. Use Ctrl + V to paste it in a text editor, for example, in Notepad.
3. Edit what is marked with yellow color in the example, to make it correspond to your environment.
4. Mark all text in the text editor and copy it again using Ctrl + C.
5. Paste the text using Ctrl + V in the argument field described in step 9 in the installation instruction [Backup/test company locally on separate database server](BackupTestDatabaseLocalDatabaseServer.htm).

#### Example 1: Backup of company databases
-d C:\Databases -s SQLANYs_MonitorG5_Server1 --dbn 001,002,003 -o C:\DatabaseBackup -n C:\DatabaseBackup\{yyyy-MM-dd}.log -r --ms your.smtpserver.com --mp 25 --md SenderName --mn BackupSender@yourcompany.com --mu SmtpUsername --mw C:\somewhere\pwd.txt --mr BackupRecipient1@yourcompany.com,BackupRecipient2@yourcompany.com --mb MailSubject --mt 0

#### Example 2: Copy to test company
-d "C:\ProgramData\Monitor ERP System G5\Databases" -s DatabaseServerName --dbn 001 -t 001_1 -o "C:\ProgramData\Monitor ERP System G5\Databases" -n "C:\ProgramData\Monitor ERP System G5\Databases\001_1\{yyyy-MM-dd}.log" -r --ms your.smtpserver.com --mp 25 --md SenderName --mn BackupSender@yourcompany.com --mu SmtpUsername --mw C:\somewhere\pwd.txt --mr Recipient1@yourcompany.com,Recipient2@yourcompany.com --mb MailSubject --mt 0
> Please note! In an argument, you must enclose a value using "" if it contains spaces.

#### Explanation of all arguments (English)
| Option | Required/Optional | Description | Example |
|---|---|---|---|
| -d "database path" | Required | Supply file or root path of the database to backup. | -d C:\Databases |
| -s "server name" | Required | Service name of the SQL Anywhere database server. | -s SQLANYs_MonitorG5_Server1 |
| --dbn "database names" | Required | Comma-separated list of database names. | --dbn 001,002,003 |
| -o "output path" | Required | The folder root path where backups are placed. | -o "C:\DatabaseBackup" |
| -n "logPath{datetimeformat}" | Optional | Backup error log. If none is specified then the executable's location is used. Supply either file or directory path. If a filename is not specified then the default name is: yyyy-MM.[databaseNames].log Datetime patterns can be specified in the filename. | -n C:\log -n C:\log\{yyyy-MM-dd}.log |
| -v | Optional | If specified then a validation will be done once the backup has completed. | -v |
| -m | Optional | If specified then only back up log file. | -m |
| -r | Optional | If specified then truncate log file. | -r |
| --tm | Optional | If specified then only test the supplied mail settings. Used when setting up the backup jobs to ensure mailing works. When this option is used no other backup parameter will run, even if you have included backup options. | --tm |
| -u | Optional | If specified then each backup will be created in a new folder named yyyyMMddHHmmss | -u |
| -t "test company" | Required | Copy a database to the named test company. Supply the database name of the test company. Used in conjunction with --dbn "database name", the database to copy from. | -t 001_1 |
| --ms "mailserver" | Required | Specify the e-mail server name. | --ms your.smtpserver.com |
| --mp "port number" | Required | Specify the e-mail server port number. | --mp 25 |
| --md "display name" | Required | Specify the e-mail display name. | --md SenderName |
| --mn "Sender email address" | Required | Specify the sender e-mail address. | --mn BackupSender@yourcompany.com |
| --mu "username" | Required | Specify the user name for login on the e-mail server. | --mu foo@bar.com --mu SmtpUsername |
| --mw "password file path" | Required | Specify a path to a text file that contains the actual password of the sender e-mail address that will send e-mail reports. Permissions for this file should be restricted so that only the Windows account that runs the scheduled task has exclusive access to the file. | --mw C:\somewhere\pwd.txt |
| --mr "mail recipients" | Required | Comma-separated list of recipients. | --mr Recipient1@yourcompany.com,Recipient2@yourcompany.com |
| --mb "subject" | Required | Specify the mail subject. | --mb MailSubject |
| --mt "mail trigger" | Required | Specify the trigger for when an email should be sent. Default is always. 0 = Always 1 = Error | --mt 0 |
| --ml | Optional | If specified then SSL will be used. | --ml |
