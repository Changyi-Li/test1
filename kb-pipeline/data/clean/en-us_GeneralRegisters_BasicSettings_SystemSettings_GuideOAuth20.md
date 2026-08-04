### Activate OAuth 2.0 with Microsoft Entra ID
Here you find information about what actions are needed in Microsoft Entra ID (previously Azure Active Directory) and in Monitor ERP to be able to use OAuth 2.0 authentication for incoming e-mail to Monitor ERP from Exchange Online.

#### Register an application
Register a client application for Monitor ERP in Microsoft Entra/Microsoft Azure. See [this guide](https://help.monitor.se/EN/MONITOR_G5/PDF/Setup_oauth_client_secret.pdf) (in English) if you choose the authentication process called Client secret. See [this guide](https://help.monitor.se/EN/MONITOR_G5/PDF/Setup_oauth_username_password.pdf) (in English) if you choose the authentication process called User name/Password.
> Please note! When addressing this issue you should, if needed, contact your IT consultant for help with the required actions!

#### Additional settings for e-mail in Monitor ERP
As of version 22.6, you have to configure the additional settings in Monitor ERP mentioned below, in the respective procedures. Here you find a [description of the settings](bEmail.htm).
System settings:
- E-mail method – Select the option called Server based, via Microsoft Exchange Online.
- Application (client) ID – Paste the value from Application (client) ID from your client application.
- Directory (tenant) ID – Paste the value from Directory (tenant) ID from your client application.
- Authentication flow – Select authentication flow to use for Exchange Online. You can choose between Client secret and User name/Password.
- Client secret – If you selected the Client secret option as authentication flow, you should paste the key from Value in the client secret you created in your client application.
Users:
If you have specific e-mail settings for users (which overrides the corresponding system settings), you may need to make adjustments/additions to these settings as well.
If you gave the Webshop option, you must also configure the following settings for the WEBSHOP user (which is used for the webshop):
- E-mail method – Select the option called Server based, via Microsoft Exchange Online.
- User name (Exchange) / Password (Exchange) – If the above system setting, Authentication flow, is set to User name/Password, you must enter the user name and password for the Exchange account.
Settings for incoming e-mail:
If you have registered e-mail accounts for different types of incoming e-mail, for example, Monitor-to-Monitor, you must complement with the settings which correspond to the system settings, and copy the same values to paste here.

#### Additional settings for e-mail in options for Monitor ERP
In the Webshop – Administration you must complement with the setting below regarding e-mail. Here you find a [description of the setting](https://help.monitor.se/SV/webshop_G5/latest/Content/Using/e_mail/settings.htm).
- E-mail method – Configure as According to user settings in Monitor G5.
