### Export
Under this tab you configure settings for the different export types available in Monitor ERP. Some export types have several alternatives. You can select which alternative should be used by default.
Customer orders
For customer orders you enter a path to a directory where the export files should be saved. If no directory has been entered, or is incorrect, a temporary directory will be used instead.
Payment file
Here you configure settings for payment files to different banks. You activate the formats for each bank under the Bank activation tab in the Bank settings procedure.
You link the payment formats to the electronic payment methods in the Bank settings procedure. However, you can make exceptions per supplier and format, if needed. This is done by using the Export settings button in the Supplier register procedure.

#### Path
Here you enter the path to the directory where the payment files should be saved.

#### File name
Here you see/enter the name of the payment file. The file name is pre-filled as a template with variables. The %T variable inserts the number of the transaction list into the file name. The %x variable inserts today's date into the file name. When you hover over the field, a tooltip appears with an explanation of the variables.

#### Monitoring time of credit invoices
LB, SPISU, UTLI. Here you enter the monitoring time for credit invoices. This is entered in number of days. The default option here is 365 days.

#### Priority code/Payment method
Applies to SPISU Determines how the transactions should be prioritized. The available alternatives are: 0 = Normal, 1 = Express, and 2 = Check.

#### Cost charge code
Applies to SPISU This setting determines who will pay for the cost of the transaction. The available alternatives are: 0 = Sender pays all the costs (OUR) or 2 = Payee pays own costs (SHA).

#### Transfer method
UTLI. Determines how the transactions should be prioritized. The available alternatives are: B = Normal, T = Express, and C = Check.

#### Distribution of cost
UTLI. This setting determines who will pay for the cost of the transaction. The available alternatives are: 0 = Each party pays their own costs, the normal case (SHA), 1 = Recipient of payment pays all costs (BEN), or 9 = Sender of payment pays all costs (OUR).

#### Signer ID/Corporate ID number (ISO)
ISO. You will receive this information from your bank.

#### Agreement/Customer number (ISO)
ISO. You will receive this information from your bank.

#### Merge payments
ISO. This controls whether payments are merged. If multiple invoices are sent at the same time to the same supplier, they can be merged into one overall total in the payment file.

#### Use batch payment
This applies to Danske Bank (Sweden and Norway) and Nordea (Finland). If you, in your payment file, send multiple invoices at the same time to the same supplier, you can with this setting determine if these should be merged into one payment in the file, or if they should be handled as separate payments per invoice. If you deactivate this setting, the system will send each invoice to the supplier as a separate payment. This may result in a higher transaction fee, but can also mean that the recipient of payment has an easier time matching the payments in the receiving system. This is the general setting for all suppliers. If you wish to make an exception from this setting for specific suppliers, this can be done by using the Export settings button in the Supplier register procedure.
Technically, the Use batch payment means that all invoices are placed within the same CdtTrfTxInf section in the file, where the invoices’ numbers are shown in the unstructured reference section <Ustrd>. If it is deactivated, the system will place the invoices in separate CdtTrfTxInf sections.
Shipping
For shipping you configure settings for your account at Pacsoft Online, nShift Delivery, nShift Web-TA, LogTrade, Export to file, SFTP, Export to file, FTP, or Export to file. Both of the export to file variants change the file format to JSON. The purpose of exporting to file is to enable third party integrations to a TA system (Transport Administration system).

#### User name
Here you enter the account's user name.

#### Company ID
nShift Web-TA, LogTrade. Here you enter the company's identification in the account.

#### Password
Here you enter the account's password.

#### License
LogTrade. The license number of the account.

#### Run against a test environment
Here you determine if a test environment should be used. This can be useful before the startup in order to verify that the shipping flow works properly against the shipping agent When a test environment is used, the text "Test" is shown on labels. No EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. export (no file will be generated) when using a test environment.

#### ID for goods tracking
nShift Web-TA. Here you enter the account's identification used for goods tracking.

#### Profile group
nShift Delivery, Pacsoft Online. Here you enter the profile group for shipments that are exported.

#### Login, User ID
nShift Delivery, Pacsoft Online. Here you enter a specific user name for login.

#### Login, Profile
nShift Delivery, Pacsoft Online. Here you enter a profile for login (if this is created).

#### Login, Password
nShift Delivery, Pacsoft Online. Here you enter a password for login.

#### Show messages
nShift Delivery, Pacsoft Online. Here you select which types of messages from nShiftDelivery or Pacsoft Online should be displayed during export of shipments. The available options are Errors and warnings and Only errors.

#### Save temporary files at export
Here you determine if exported shipments also should be saved as temporary files in the folder configured with the environment variable %TEMP% on the server computer. The setting is only used during troubleshooting of shipments.

#### FTP server
Export to file, FTP. This is the address for the FTP server for Export to file, FTP. Next to the field is a button to Validate connection ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_test.png).
Export to file, SFTP. This is the address for the SFTP server for Export to file, SFTP. Next to the field is a button to Validate connection ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_test.png).

#### Port
Export to file, FTP. Here you enter the port for the FTP communication.
Export to file, SFTP. Here you enter the port for the SFTP communication. The SSH port.

#### Authentication
Export to file, SFTP. Here you choose the type of authentication you wish to use. Depending on which option you choose, certain fields will be activated/deactivated. The following authentication options are available:
- User name and password – The user name and password that are used for authentication.
- Public key – The public key in the key file will be used for authentication.
- User name and password + Public key – The user name and the password plus the public key in the key file will be used for authentication.

#### Connection mode
Export to file, FTP. Here you are able to decide whether the connection and subsequent file transfer should be Active or Passive. The options are:
- Active – The FTP connection mode will be active. This is the “older” connection mode where the client decides the port number which is to be used for the data transfer.
- Passive (Auto) – The FTP connection mode will be passive. This is the “modern” connection mode where the server site decides which port number which is to be used for the data transfer. This is the standard option.
- Passive (PASV) – The FTP connection mode will be passive. PASV is used for older servers.
- Passive (PASVEX) – The FTP connection mode will be passive. PASVEX is used for older servers.

#### Encryption method
Export to file, FTP. Here you can select whether the FTP connection should be SSL encrypted as Implicit (FTPS) or Explicit (FTPS). The standard option is None (FTP), i.e. unencrypted FTP. Implicit encryption is normally initiated over port 990. Explicit encryption is initiated over the standard port 21. The options are:
- None (FTP) – This is the standard option.
- Explicit (FTPS)
- Implicit (FTPS)

#### User name
Export to file, SFTP. Here you enter the user name for the SFTP account. This field is deactivated if you the Public key option is selected in Authentication.
Export to file, FTP. Here you enter the user name for the FTP account.

#### Password
Export to file, SFTP. Here you enter the password for the SFTP account. This field is deactivated if you the Public key option is selected in Authentication.
Export to file, FTP. Here you enter the password for the FTP account.

#### Key file
Export to file, SFTP. Here you enter/select the file name, including the path, of the file containing the authentication key.
> Use Windows generated keys, for example, according to the following:
ssh-keygen -m PEM -t rsa -b 4096 -f .\your_key.pem

#### Key file password
Export to file, SFTP. Here you can see/enter the password of the key file.

#### Host key's “hash fingerprint”
Export to file, SFTP. If you leave this field empty, it will automatically be updated with the host key's hash fingerprint when the source or target is tested.

#### Path
Export to file, SFTP, Export to file, FTP, Export to file. The path to the destination folder for the export file. The path can be a local folder or a URL path. To the right of the field there is a file chooser where you are able to browse local server folders or add a UNC path. The field for Export to file, FTP can be left empty.

#### File name
Export to file, SFTP, Export to file, FTP, Export to file. The file name or the file name pattern for the destination folder. Here you are able to use file name variables to enter the file name. (The variables are the same as for [EDI – Targets](../../EDI/EDIChannels/bTargetSettings.htm#Variabler_i_filnamn)).

#### Consecutive number
Export to file, SFTP, Export to file, FTP, Export to file. Here the next row in the file name is shown. If variable for consecutive number is entered in the file name in the File name field, this field will be activated and you can change the consecutive number.

#### Use temporary file extension
Export to file, FTP, Export to file, SFTP. Here you decide whether a temporary file extension should be used in the file name while the file transfer is in progress. Once the file transfer is complete, the usual file extension is set according to the file name above. Temporary file extensions are used if the receiver uses a program which regularly checks and loads files via the export path on the FTP/SFTP server. To avoid this program loading a semi-finished file while a file transfer is in progress.

#### Temporary file extension
Export to file, FTP, Export to file, SFTP. Here you enter the temporary file extension (e.g. “tmp”) when you have selected Yes in the above setting. You do not need to enter a period (.) in the beginning of the file extension.
Accounting
For accounting you configure settings for the export files called SIE type 4E – Transactions (complete) and SIE type 4I – Transactions (plain). Where SIE-type 4E contains complete information regarding the chart of accounts, balances and voucher records. This file format can be used to export the journal postings for the year to a program for transaction analysis. SIE-type 4I only contains voucher records. The file format is used when a preliminary system, for example, a payroll or invoicing program, is to generate an accounting order to be loaded into the accounting program.

#### Path
Here you enter a path to a directory where the export files should be saved.

#### File name
Here you enter a file name of the export files.

#### Export chart of accounts/dimensions
Applies to SIE-type 4I. Here you decide if chart of accounts/dimensions should be exported.

#### Export blank voucher number series and voucher number
Determines if blank (empty) voucher number series and voucher numbers should be exported in the file.

#### Export balances
Applies to SIE-type 4E. Determines if balances should be exported.

#### Dimensions
Here you enter dimension numbers in the SIE file for the different posting dimensions.
Purchase order
For purchase orders you enter a path to a directory where the export files should be saved. If no directory has been entered, or is incorrect, a temporary directory will be used instead.
Invoice
For invoices you enter a path to a directory where the export files should be saved. If no directory has been entered, or is incorrect, a temporary directory will be used instead.
VAT report

#### Path
Here you enter the path to the directory where the VAT report should be saved as an XML file.

#### File name
The file name of the VAT report. The file name is pre-filled as a template and it contains, e.g., the variable %P. The variable inserts the period number in the file name. The period number consists of year and month, for example "201802" for February 2018. When you hover over the field, a tooltip displays an explanation of all the available variables.

#### Website
Factoring
Here you configure settings for invoice export via file for factoring. The banks and factoring companies supported today are Handelsbanken Finans (Falk, Sweden), Nordea Finans (Norway), DNB (Norway), Sparebank1 (Norway), and Nordea Finans (Finland). Also the e-invoice format Peppol BIS 3.0 is supported.

#### E-invoice address
Peppol BIS 3.0. Here you enter the company's e-invoice address as well as the factoring company's e-invoice address, based on which E-invoice address ID you select in the next field. An e-invoice address can, for example, be the Corporate ID number or VAT registration number.
> For factoring customers that are invoiced via Peppol BIS 3.0, a corporate ID number must be entered in the Customer register procedure.

#### E-invoice address ID (EIAD)
Peppol BIS 3.0. Here you select an ID for the company's e-invoice address as well as for the factoring company's e-invoice address.

#### Path
Here you enter the path to the directory where the invoice file should be saved.

#### File name
EC sales list

#### Path
Here you enter the path to the directory where the EC sales list should be saved as an XML file.

#### File name
The file name of the EC sales list. The file name is pre-filled as a template and contains the variable %P. The variable inserts the period number in the file name. The period number consists of year and month, for example "201802" for February 2018. When you hover over the field, a tooltip displays an explanation of the variable.

#### Website
Here you can enter the address to a website to which the user should be linked after the EC sales list has been exported.
Intrastat
Here you configure settings for the Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. report that should be exported to file and be transferred to the affected authority.
E-invoice
Settings for export of e-invoice. You don’t have to order this function – you simply activate it yourself in Monitor ERP if you are using the Swedish, Norwegian, Danish, German, or Finnish country package.
When activation takes place, an account is automatically created for you with our partner Crediflow. Crediflow is the operator which manages the underlying distribution of e-invoices. You don’t need to have your own agreement with Crediflow.
Monitor ERP System AB will charge on a monthly basis according to the volume of invoices that are sent and received. Using a service for paper invoice – provided by Crediflow – you can also transfer all distribution of customer invoices. Also including those recipients unable to receive e-invoices.
You find current price information for E-invoice SENT and Paper invoice SENT on [this site](https://monitorerp.com/sv/efh-tolkning-villkor-och-priser/). You can also contact our sales department by e-mail at sales@monitorerp.com for additional information.
If you already have your own agreement with a different e-invoice service, there is also a plugin for export of e-invoice in the Peppol BIS 3.0 format.
E-invoices in Peppol format which are sent to German customers, as well as within Germany, follow the Xrechnung format.
> Make sure that port 443 is open for outgoing traffic in your firewall, so that Monitor ERP can communicate with Crediflow.

#### Company ID
Crediflow. If you already are a customer with Crediflow, you enter your company ID here. If you are not a customer with Crediflow, you should use the button Create account instead. Once the account has been created, the company ID will automatically be filled in.

#### E-invoice address
Crediflow, Peppol. Here you enter your company's e-invoice address based on which e-invoice address ID you select in the field below. E-invoice address can, for example, be the Corporate ID number or VAT registration number. For Crediflow, information about the E-invoice address will be automatically entered. This information is filled in to fulfill the Peppol format validations in the system.

#### E-invoice address ID (EAID)
Crediflow, Peppol. Here you select an alternative for the company's e-invoice address ID. For Crediflow, the information about E-invoice address ID (EAID) will be automatically entered. This information is filled in to fulfill the Peppol format validations in the system. In Finland, the EAID is usually "LY-tunnus".

#### Enclose embedded PDF in XML
Here you decide if PDF file with Invoice and/or Linked files should be attached with the XML file. The setting is deactivated by default. Please note! Only files of the PDF type, with a maximum size of 4 MB, can be included with the XML file.

#### Activate test mode for sending invoices
Crediflow. If you activate test mode you can send invoices for testing of the data in the e-invoices. The test will take place towards Crediflow’s live endpoint, but with test data. The invoices that you send will be handled as live invoices when importing. However, the data will remain with Crediflow and not continue in the process flow. This means you can test status calls, etc.

#### Path for manual validation of e-invoice file
This setting is used to test/validate e-invoices. If you enter a path, Save to file is shown under the E-invoice column in the Review/approve invoice and Print invoice procedures, where you can choose to save the e-invoice to file in the path you have entered here. At this time an e-invoice is also sent to the operator/customer. The purpose, for example, is to send the e-invoice to the Support Center for troubleshooting (by reprinting), or to send it to a customer for verification before going live. If you enter something in the path, this overrides the setting Activate test mode for sending invoices.

#### Message in invitation
Crediflow. Here you enter a message shown if you need to send an invitation to customers to be able to send e-invoices to the customer.

#### Create account
Crediflow. Use this button to register an account with Crediflow if you do not already have an account with them.
If you have a GLN number registered, please contact the Monitor Support Center to get help to activate it on your account (Global Location Number).
Make sure the company information is correct and enter a contact person and that person's contact information including the e-mail address. Also enter a "Message in invitation". This message is used when you send an invitation to the customer asking if this customer wants to receive e-invoices from you. This invitation is sent from the Customer register.
Check the I have read and accepted the terms/conditions for this service box.
The account becomes created when you click the OK button. The account is created via an API connection to Crediflow. If everything works correctly you will automatically receive your company ID. Now the account registration is completed. Remember to save.

#### Deregister account
Crediflow. If you have an account with Crediflow, you can use this button to deregister the account, if needed.

#### Path to file
Peppol . Here you configure the path to a directory where the export files (XML and PDF) should be saved after uploading to the operator’s server. You must enter a UNC path to a shared directory, for example \\your_server\shared_directory.

#### File name
Peppol. The following variables can be used:
- %i – invoice number
- %c – corporate ID number
- %C – company name
If you do not enter a file name, the XML file will be named by the invoice number.

#### Use FTP
Peppol. Check this box in order to configure settings and send invoice files via FTP. This means the invoices can be uploaded directly to your operator's FTP page.
FTP settings (Peppol)
> Please note! Check with your e-invoice operator which FTP settings you should configure.

#### FTP server
The address to the FTP server, for example. "ftp.company.com". You do not have to use "ftp://" at the beginning of the address.

#### Port
Here you enter the port for the FTP communication. The standard port is 21 (control channel for unencrypted FTP). This is selected by default. If you select Implicit (FTPS) as encryption method below, the port should be changed to 990 (control channel for implicit FTPS).

#### Encryption method
Select if the FTP connection should be SSL encrypted as Implicit (FTPS) or Explicit (FTPS). The default alternative is None (FTP), that is, unencrypted FTP Implicit encryption is normally initiated over port 990. Explicit encryption is initiated over the standard port 21.

#### User name
Here you enter the user name for the FTP account.

#### Password
Here you enter the password for the FTP account.

#### Path
Path to the directory on the FTP server to which files should be exported.

#### Test connection
By clicking Test connection, you can verify that the connection to the FTP server works.
Sanctions list
This is an option which is used by the Sanctions list procedure. Here you configure settings for that procedure.

#### Levenshtein distance
The tolerance (measured in number of characters) for example for misspelled words, configured as Levenshtein distance in sanctions lists. The default value is two characters.

#### Sanctions lists
You can activate up to five different sanctions lists drawn up by the EU, the UN, Great Britain, the US, and Switzerland.

#### Path
For each activates sanctions list you enter or select a Path using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_browse.png) next to the field.

#### File name
You enter an optional File name for each activated sanctions list. All of the sanctions lists are in the XML format. Once you have entered both a path and a file name and left the field, the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_down.png) button will be activated next to the field. By using this button, you download sanctions to the path and file name you have entered.
