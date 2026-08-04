## Database administration
> Please note! This procedure should only be used by the administrator or ERP manager, preferably in consultation with a support agent at Monitor ERP System AB.
The procedure can be run in all companies in the system and has the following purposes:
- Updating the database in the company in question via specific patches. The patches are created by Monitor Support Center and can for example be attached as a .mql file in an e-mail message.
-    
Uploading of database including different log files to the Monitor Support Center via a link for uploading file or via FTP. The purpose is for the personnel at the Monitor Support Center to be able to test, troubleshoot, and solve problems/errors, if any, in the database.
> Uploading database is only possible to do from here if the database is run on SQL Anywhere. If the database is run on Microsoft SQL Server you must upload it manually, via a link that you get from the Monitor Support Center.
- Creating optimization statistics for one, several, or all tables in the database. This is normally done while the database server is running. Only in exceptional cases you might need to manually create new optimization statistics.
- Changing the password for database access. The password is linked to the SAP SQL Anywhere database user ReadOnlyUser.
- Changing the optimization level for SQL Anywhere.
