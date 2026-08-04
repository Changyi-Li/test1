# Relocating the Monitor ERP Server
This instruction describes relocation of Monitor ERP Server with SQL Anywhere to a new server computer.

## Preparations
> If you cannot perform the relocation by yourselves, the Monitor Support Center offers installation help for Monitor ERP, charged on an ongoing basis. There are different prices for daytime, evenings or weekends. We will then create a remote control session and perform the relocation. Program for the remote control session can be downloaded from our website [https://www.monitorerp.com/mos](https://www.monitor.se/mos/).
> Important information for customer when moving server Please note! When moving Monitor ERP, options such as Web server, Machine integration, EDIEDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system., Bank integration, Creditsafe, adaptations, etc. are not automatically carried over. They may need reinstalling, reconfiguring, or have update paths after moving server. What the customer is responsible for The customer is responsible for informing Monitor which options and integrations the system has before commencing the move. Without this information, some functionality may be missing after the move.
1. Order a server relocation package for Monitor ERP Server from the Monitor Support Center. This package contains installation files for server and client, certificate file, and instructions (for example, this instruction).
2. When you have received the package you can perform an installation of Monitor ERP Server on the new server computer, see below.
3. Firstly, make sure all users have shut down their Monitor ERP clients.
4. Then you should open Services in Windows on the old server computer and shut down the service SQL Anywhere - [server name] (for the database engine). Also deactivate the service making it impossible for it to restart, for example, if the server computer is restarted. To deactivate, change the Startup type of the service from Automatic to Disabled.

## Installation on the new server computer:
1. Start the installation according to the instruction called Install Monitor ERP Server which was included with the installation files, and follow the steps in the initial items.
2. When you reach item 7 in the installation you select Install an existing environment. Then click Next.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/MONServerMove1.png)
3. In the next step you select your existing environment called Production and click Next.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/MONServerMove2.png)
4. The following steps should be taken according to the instruction called Install Monitor ERP Server.

## Copy files from the old server computer:
1. Create a backup of the file called MonitorCompanyConfiguration.json in the Monitor ERP System AB folder on the new server computer. You find this file in the path where you installed Monitor ERP Server. Save the backup copy in a different folder.
2. Then you should copy the same json-file from the old server computer to the new server computer. Select to overwrite the existing file on the new server computer.
3. Open the file on the new server computer using a text editor and change the "SqlAnywhere" server name in "ConnectStrings" and also the file paths in "DatabaseDirectory" and "BackupDatabaseDirectory", making them correspond with server name and paths for the new server computer. See the highlights in yellow in the image below.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/MONServerMove3.png)
4. Shut down the service called SQL Anywhere - [server name] (for the database engine) on the new server computer.
5. Copy both the Databases folder and the DatabaseBackup folder from the old server computer to the new server computer. Select to overwrite the existing Databases folder on the new server computer. You find the folders via the path where the databases are installed on the old and the new server computer, respectively.
6. Start the service for the database engine on the new server computer.
7. In the MONITOR Installation Manager in Windows on the new server computer, you should now create and schedule backup tasks and copying tasks of test companies, making the tasks correspond to how it is configured on the old server computer. Make sure that the path to the folder for database backups is correct in the backup tasks you create on the new server computer.
8. If you have folders with linked files on the old server computer, you should copy these to the new server computer.
9. Update the file paths in the Paths procedure in Monitor ERP on the new server computer. If the paths lead to folders on the old server computer, they should be changed so that the paths go to the corresponding folders on the new server computer.

## Reinstall Monitor ERP clients
1. Uninstall the Monitor ERP client on the users' computers.
2. Install the Monitor ERP client again on the computers, by using the installation file MONITOR Client Setup.exe. Follow the instruction called Install Monitor ERP Windows client available in the server relocation package.
3. Start the Monitor ERPclients and make sure that everything is working as it should.
