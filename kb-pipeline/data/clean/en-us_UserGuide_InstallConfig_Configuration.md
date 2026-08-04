# Configuration
This section of the online help is meant for system administrators.
The configuration concerns actions to take prior to training and the subsequent go live in the ERP system Monitor ERP.

#### Web client
The ERP system consists of a database server and an application server which you install on the computer which should be the Monitor ERP Server. The server is updated using a program called Monitor ERP Installation manager. The program becomes installed when the Monitor ERP Server is installed.
The web client is available from all modern devices with a browser (Chrome, Edge, Firefox, Safari). Usage is not limited to a PC with Windows. You do not need to install or update the Windows client. The latest version is always available straight in your browser.

#### Windows client
The ERP system consists of a database server and an application server which you install on the computer which should be the Monitor ERP Server. A Windows client is included in the purchase of the ERP system and this should be installed separately on the computers where the ERP system should be run.
The server is updated using a program called Monitor ERP Installation manager. The program becomes installed when the Monitor ERP Server is installed. Windows clients are automatically updated when they are started for the first time after the server program has been updated.

#### Monitor Mobile
There is also a mobile client for the ERP system which you can use regardless of whether your company uses the Web client or the Windows client on company computers. Monitor Mobile is especially designed for smaller devices such as smartphones, hand-held scanners, and tablets that often do not have a keyboard or mouse. Monitor Mobile focuses on functionality like scanning barcodes and working on the warehouse floor. The mobile client is run either in a regular web browser or as an app for Android and IOS. The app is available at Google Play and at Apple App Store. To be able to use the app and Monitor Mobile the Monitor ERP Web server must be installed and your firewall must also be configured. Description of these installations and how to configure the firewall is available in separate documents delivered together with the installation programs.

#### Backups
You need to create scheduled backup of the company's databases. Read more about this in the [Create and schedule backup](CreateScheduleBackup.htm) section.

#### Configuration and setup of basic data
After the installation, Monitor ERP should be configured by the system administrator, ERP manager, and authorized personnel.
Various default system settings should be gone over, checked, and possibly changed based on how the company will use the system. Different basic data should also be registered. This work must also to a certain extent be performed when the company converts from Monitor G4. It is also possible to import basic data (parts, part balances, customers, suppliers) from another ERP system. These imports are performed directly in Monitor ERP. This work is normally done after the installation but before you start the training in the system.
Examples of basic data are users and these should then be assigned roles linked to user rights. This needs to be done so members of the personnel can log in to Monitor ERP and access different procedures. Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. is also parts, BOM and routing, work centers, customers, suppliers, schedules, posting dimensions, etc. Parts with balances, locations, batch numbers, and suppliers can be imported from another ERP system or spreadsheet application. Read more about the work concerning basic data and settings in the [Basic data and settings](../Using/RegisterBasicData/BasicDataSettings.htm) topic.
When basic data has been registered and all settings have been controlled, the system administrator should also create one or more test databases which should then be used when training in the system. Read more about this in the [Create test databases](CreateTestDatabases.htm) section.
> We recommend that registration of basic data and controlling/changing default settings should best be done in consultation with consultants/instructors from Monitor ERP System AB.
