### Backup and migration of databases
> Please note! This description applies if the databases run on SQL Anywhere. If the databases run on SQL Server, the update cannot copy or move databases as in the descrption below. The databases will instead be migrated directly on SQL Server. That is why it is important that you first backup the databases in Microsoft SQL Server Management Studio according the Microsoft’s documentation, before you start the update of Monitor ERP Server.
> Starting from version 25.2 of Monitor ERP, it is possible to specify an external drive for storing temporary files during the update process. This means that automatically copied database backups will be placed on the external drive, minimizing the risk of the system starting up with full disk space. The path for the external disk is UpdateBackupPathOverride in the configuration file MonitorCompanyConfiguration.json.
> Please note! To be able to specify an external drive in the configuration file, you need version 25.2 or later. If you have an earlier version of Monitor ERP, using UpdateBackupPathOverride will result in unsuccessful updates.
Backup and migration of SQL Anywhere databases, in connection with update of Monitor ERP Server takes place in the following way. This will all take place automatically:
1. All databases are copied from the regular database directory to the Installation_temp directory under C:\ProgramData\Monitor ERP System G5\. The company configuration file is also copied to the directory.
2. After this, a migration of the databases to the new version in the temporary directory will be carried out.
3. After the migration in the temporary directory, the following takes place:
1. All databases in the regular database directory are moved to the Installation_old directory, under C:\ProgramData\Monitor ERP System G5\.
2. The migrated databases in the temporary directory are then moved to the regular database directory.
4. When the Monitor server starts up after the update, the system database and BI database are also migrated.
If migration of the databases should fail for some reason, the entire update is canceled.
