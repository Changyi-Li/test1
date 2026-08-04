### Microsoft Entra ID (Azure Exchange/Sharepoint)

#### Application (client) ID
This applies if you have selected Server based, via Microsoft Exchange Online as E-mail sending method. Copy the Application (client) ID value from your client application in Microsoft Entra ID (previously Azure Active Directory), and paste it here.

#### Directory (tenant) ID
This applies if you have selected Server based, via Microsoft Exchange Online as E-mail sending method. Copy the Directory (tenant) ID value from your client application in Microsoft Entra ID (previously Azure Active Directory), and paste it here.

#### Authentication flow
This applies if you have selected Server based, via Microsoft Exchange Online as E-mail sending method. Here you select authentication flow to use toward Exchange. The following options are available:
- Client secret – Select this authentication flow if you will be using a Client secret. This client secret must be created in the Microsoft Entra ID.
- User name/Password – Select this authentication flow if you will be using the Exchange account's user name and password. At present there are certain limitations when you select this authentication flow – conditional access and multi-factor verification, for example, are not supported by all organizations using Microsoft Entra ID if the administrator has configured multi-factor authentication to be a requirement.

#### Client secret
This applies if you selected Client secret in the system setting above. Copy the value* for the client secret you created in Microsoft Entra ID, and paste it here.
> * Please note! You have to copy the Value for client secret to a different location, in connection with when creating the client secret on the Certificate and secrets page in Microsoft Entra ID, to be able to then copy that value to this field. A client secret also has a certain validity period in Microsoft Entra ID. This means you have to create a new client secret when the validity is about to expire and then copy the new client secret to here.
