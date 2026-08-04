# Configure ODBC link
You have to enter a password for the SQL Anywhere database user ReadOnlyUser. Read mote about how to enter a new password or how to change password for ReadOnlyUser in the help topic called [Change password for ReadOnlyUser](bChangePasswordReadOnlyUser.htm).
In addition to account information, you need to configure the following settings:
- Database name – The company's number (for example, "001")
- Server name – The name of the SQL service. In Monitor ERP (Monitor G5) it is normally called "monitorG5_servername" (listed under "Services" on the database server).
- Host – The IP address of the Monitor server or its DNS name.
- Port – 2638 (the port can vary if Monitor G4 and Monitor ERP (Monitor G5) are run on the same server, in that case check which port is used by the SQL service).
