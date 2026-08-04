### Backup

#### Number of days before warning
Here you select the number of days before you receive a warning about the backup not having been completed. You can select a number of days between 1 and 5 days. The default option here is 3 days.
If more days (based on today's date) than the selected Number of days before warning have passed since the most recently completed backup of a live company database, the users with the role of ERP manager or System administrator will receive a notification in the Message center. Also, an e-mail is sent from the below e-mail sender. In the notification and in the e-mail, it says: "The most recent backup of database [Database number] is more than [Warning interval] days old ([date and time]). Make sure the backup is working correctly or contact the Monitor Support Center."
If more days (based on today's date) than the selected Number of days before warning x 3 have passed since the most recently completed backup, all users will receive the same notification in the Message center.

#### E-mail sender of backup notifications
Here you enter the e-mail address which should be used as sender of e-mails sent from the backup program.
If the e-mail should be sent via the Microsoft Exchange e-mail server, you should enter the e-mail address of a valid account in Exchange.

#### User name (Exchange)
If the method to send e-mail is set to Server based, via Microsoft Exchange in the System settings procedure, you should here enter the e-mail sender's user name in Exchange for login to the e-mail server. This is normally the account's name in Active Directory.
If the method to send e-mail is set to Client based, via Microsoft Outlook or Server based, via SMTP, you should leave this field empty.

#### Password (Exchange)
Here you enter the above user name's existing password used to login to the e-mail server.
