### E-mail
Most document printouts (for example orders) can also be sent via e-mail. However, the recipient's e-mail address must first be entered in the header of the document. The documents are automatically attached as PDF files and in some cases also as XML files. To be able to send e-mail from Monitor ERP you must configure settings for an e-mail server here.
Please note! These e-mail settings are also used for calendar integration of activities in Monitor ERP.

#### E-mail method
Here you select a general method used to send and receive e-mails in Monitor ERP. There are four methods:
- Client based, via Microsoft Outlook – If the users have Outlook installed, you can select this option.
Client based, via Microsoft Outlook
> Please note! The client based method for e-mails is not supported if the users have installed the new Outlook.
- Server based, via Microsoft Exchange – If the built-in e-mail client in Monitor ERP should be used toward Exchange (on-premises), select this option.
- Server based, via SMTP – If some other e-mail server than Exchange is used, select this alternative.
- Server based, via Microsoft Exchange Online – If the built-in e-mail client in Monitor ERP should be used toward Exchange Online, select this option. In this case you need to register a client application for Oauth 2.0 in Microsoft Entra ID (previously Azure Active Directory). Please see [this guide](GuideOAuth2.0.htm).
The corresponding setting is also available on user level in the Users procedure, and it will in that case override this general system setting.

#### Server address (Exchange/SMTP)
Here you enter the e-mail server's IP address or DNS name.
Check e-mail settings
By using the button Check e-mail settings ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) next to the field, you can make sure the e-mail settings are correct by sending a test message.
In the dialog box that is displayed when clicking the button, you can choose one of the two server based methods in the system setting E-mail sending method. Here you also enter e-mail address for Recipient and Sender. The e-mail address in these fields will by default be loaded from the logged in user. If the E-mail sending method is set to Server based, via Microsoft Exchange, you can also enter User name and Password for authentication toward the Exchange server.
When you have clicked the Test button, "OK" is displayed in the Result field if the settings work. The recipient should also receive a test e-mail in his/her inbox. If any of the settings are incorrect, the cause will be displayed in the Result field.

#### Port (Exchange/SMTP)
Here you enter the TCP port for the e-mail server's IP address or DNS name. By default it says 0. This means that the standard port for Exchange or SMTP will be used. If the system setting called Use SSL has been activated, the port should normally be set to 587 (TLS) or 465 (SSL).

#### User name (SMTP)
Here you enter the user name for the account which should be used to login to the SMPT e-mail server. Depending on which SMTP server or SMTP service should be used, this might be an account name or an e-mail address.
The user name used to login to an Exchange e-mail server is entered per user in the Users procedure.

#### Password (SMTP)
Here you enter the above user name's existing password used to login to the SMTP e-mail server. The password used to login to an Exchange e-mail server is entered per user in the Users procedure.

#### Use SSL
This system setting should be activated if the e-mail server requires a separate network connection via TLS or SSL. Then you must also change the system setting above called Port (Exchange/SMTP).

#### Maximum size for files in e-mail
Here you decide a maximum total size in megabyte (MB) for files included as attachments in e-mails to supplier/customer that contain multiple orders. The default value here is 10 MB.
If the attachments’ combined size in such an e-mail is greater than the value entered here, the e-mail will be divided into two or more e-mails. The attachments are then distributed among these e-mails.
If an e-mail does not contain multiple orders, but it contains a number of attachments which together exceeds the size entered here, the e-mail will not be divided.
