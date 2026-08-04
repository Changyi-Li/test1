### Multi-factor authentication
Here you configure settings regarding multi-factor authentication (MFA) for users in the company.

#### Enable by default for users
With this setting you decide if MFA should be activated by default for all uses in the company. If you do not activate this setting you can still activate MFA for specific uses. This is done under the Security tab in the Users procedure.
When you activate the setting, the following setting will also become available: Enable for users with Windows account.
> Please note! When MFA is activated for a user, the [login window](../../../UserGuide/Interface/LogIn.htm#MFA) for Monitor ERP will display a QR code for registration of an authentication device. It will also show an entry field for a six-digit, one-time code supplied by an authentication app.
If you deactivate the setting you will receive a question asking if all registered devices should be removed. If you click Yes to this question, the users must register their devices again, if you should choose to reactivate the setting.

#### Enable for users with Windows account
With this setting you determine if users, who are using integrated login in Monitor ERP via a Windows account, should be included in MFA.

#### Days to register authentication device
Here you enter the length of the registration period. That is, how many days users should be given to register their device. They must register the device the first time they log in to Monitor ERP. The registration period starts after you have activated MFA for the user.
If you enter zero (0) days it means no registration period will be applied. In that case the setting called Rights after expired registration period below will determine what the users are allowed to do in the system.

#### Rights during registration period
Here you decide access and user rights for the users during the registration period, in cases where the user choose to skip the device registration in the login window. The following options are available:
- Regular user rights – (default) This option will grant the user access to the procedures which he/she normally can access via their regular user rights in the Users procedure.
- Force device registration at login – This option means that if the user decides to skip the device registration in the login window, everything will be blocked in Monitor ERP. That is, the user must register a device during login in order to be able to use Monitor ERP.

#### Rights after expired registration period
Here you decide access and user rights for the users after the registration period expired. The following options are available:
- Force device registration at login – (default) This option means that if the user decides to skip the device registration in the login window, everything will be blocked in Monitor ERP. That is, the user must register a device during login in order to be able to use Monitor ERP.
- Block users – This option will deny the user access to the Monitor ERP client. An error message will be displayed in the login window if the user tries to log in again. In that case, the user has to contact a system administrator who can remove the block from the user in the Users procedure.
