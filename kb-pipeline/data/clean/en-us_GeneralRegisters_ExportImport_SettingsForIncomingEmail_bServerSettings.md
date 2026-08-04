### Server settings
In this box you configure server name and polling interval. You also select if it is an Exchange or IMAP e-mail server.

#### Service
The type of service can be set to Exchange, Exchange Online, or IMAP.
If you will be using the Exchange Online, you need to register a client application for OAuth 2.0 in Microsoft Entra ID (previously Azure Active Directory). Please see [this guide](../../BasicSettings/SystemSettings/GuideOAuth2.0.htm).

#### Server name
Here you enter the e-mail server's DNS name or IP address.

#### Polling interval
Here you enter the polling interval, that is, how often Monitor ERP should check for new e-mail messages on the server. This interval is entered in number of minutes.

#### Application (client) ID
This applies if you have selected Exchange Online as Service. Copy the Application (client) ID value from your client application in Microsoft Entra ID, and paste it here.

#### Directory (tenant) ID
This applies if you have selected Exchange Online as Service. Copy the Directory (tenant) ID value from your client application in Microsoft Entra ID (previously Azure Active Directory), and paste it here.

#### Authentication flow
This applies if you have selected Exchange Online as Service. Here you select authentication flow to use toward Exchange Online. The following options are available:
- Client secret – Select this authentication flow if you will be using a Client secret. This client secret must be created in the Microsoft Entra ID.
- User name/Password – Select this authentication flow if you will be using the Exchange account's user name and password. At present there are certain limitations when you select this authentication flow – conditional access and multi-factor verification, for example, are not supported by all organizations using Microsoft Entra ID if the administrator has configured multi-factor authentication to be a requirement.

#### Client secret
This applies if you selected Client secret in the setting above. Copy the value* for the client secret you created in Microsoft Entra ID, and paste it here. An effect of this is that the user does not have to enter the password.
> * Please note! You have to copy the Value for client secret to a different location, in connection with when creating the client secret on the Certificate and secrets page in Microsoft Entra ID, to be able to then copy that value to this field. A client secret also has a certain validity period in Microsoft Entra ID. This means you have to create a new client secret when the validity is about to expire and then copy the new client secret to here.
