### Reduce the size of the database
This guide outlines how you can reduce the physical file size of a database after BLOB data has been exported from the database, which means empty spaces are created where BLOB data was stored previously.
> Please note! If you run options or adaptations in your Monitor ERP system, the process to reduce the physical file size of the database must take place in dialog with the Monitor Support Center. Otherwise, data may be lost. In this case, contact the Monitor Support Center at support@monitorerp.com The costs associated with managing options and adaptations when reducing the file size of the database are not covered by the Support agreement.
- If the database is run on SQL Server, the size can be reduced by using the SQL commands. You can read more about this in Microsoft’s documentation.
- If the database is run on SQL Anywhere, you can use the console program Monitor.DatabasePortation.Console.exe to reduce its size. The program is included with the application server (Monitor server) and is usually stored at the following path: C:\Program Files (x86)\Monitor ERP System AB\MONITOR Server. The program copies all standard tables from the database to temporary files (Unload), and then creates a new database from these files (Reload). The new database does not contain the empty spaces that arose when the BLOB data was exported, and has a smaller file size as a result.
Reduce size of SQL Anywhere database:
1. Open the Windows Command line interface (cmd.exe) as Administrator and go to the directory above, "MONITOR Server”.
2.         
Enter a command as outlined in the two examples below:
Reduce size of database "001":
Monitor.DatabasePortation.Console -c 001 -d 0
Reduce size of database "001", with the path "e:\data" for temporary files:
Monitor.DatabasePortation.Console -c 001 -d 0 -f e:\data
To see all arguments supported in the program, enter this single command:
Monitor.DatabasePortation.Console
3. The program is run, and when complete you’ll find the new database in a sub-directory of the new database for which you chose to reduce the size. The path is usually C:\ProgramData\Monitor ERP System G5\Databases.
4. Copy over the old database with the new database. In order to do this you must first stop the service for the application server (Monitor server) and then the service for the SQL Anywhere database server. You can then copy over the database. Then, start the services again in reverse order.
