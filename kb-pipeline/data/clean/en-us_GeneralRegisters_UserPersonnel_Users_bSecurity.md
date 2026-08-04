### Security

#### Authentication method
Here you can choose an authentication method for the user. The following options are available:
- Password
- Windows account
- OpenID Connect

#### Password
A user password is activated when you choose Password in the Authentication method setting above. A password must be entered for the user if it has been set to be mandatory/forced in the Security settings procedure. In that procedure you find additional settings regarding password policy, such as configuring that new users must change the password at first login, password expiration, password length and complexity. Read more about the settings for [password policy](../../BasicSettings/SecuritySettings/bPasswordPolicy.htm).
Even if it is not configured that password is mandatory to use, it is still recommended that the users always make use of the password function or that they link their user to a Windows account (please see below).
If you activate the setting called Allow login to mobile client, password becomes mandatory even though it is not forced via the security settings.
By using the Change password button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png) the field will become available and you can enter or change password. The password is encrypted using SHA1 one way hashes, so you will never see the user's password.

#### Windows account
In this field you can link a Windows account to the user in Monitor ERP in order to use integrated login. This is activated when you choose the Windows account in the Authentication method setting above.
Integrated login means that the user will be selected by default in Monitor ERP and he/she does not have to enter name and password when the program is started. During start-up, the server checks which Windows account is logged in on the computer. If a user in Monitor ERP is linked to that Windows account, the user will automatically be logged in to Monitor ERP.

#### OpenID Connect
This is activated if you choose OpenID Connect in the Authentication method setting above.
In the OpenID Connect E-mail field, you enter the e-mail address you wish to use to connect your user to OpenID.
The status of the account linkage is automatically updated after your first login. If you want to disconnect the link, you can do this by clicking the button called Remove account link.

#### Allow login to mobile client
Allows the user to log into Monitor ERP mobile client. If you check this setting then you must enter a password for the user.

#### Require password change on next login
If you activate this setting it means the user must change password at next login. You should activate this setting if you, for example, have made a change in your password policy in the Security settings procedure and you want the user to change their password to have it comply with the password policy. After the user logged in and changed his/her password, this setting will automatically be deactivated. A user cannot enter his/her old password as the new password when they change the password.
The corresponding function is available in the Security list in the User list procedure. There you can activate this setting for multiple users at a time.

#### Status
Here you see the status of the [multi-factor authentication](../../BasicSettings/SecuritySettings/bMultifactorAuthentication.htm) (MFA) for the user. The following statuses are available:
- Disabled – MFA is not activate for the user.
- Pending – MFA is activated for the user, but a device has not yet been registered.
- Blocked – MFA is activated for the user, but a device was not registered before the end of the registration period and the user is now blocked.
- Active – MFA is activated for the user and a device is registered.

#### Multi-factor authentication
This setting determines if MFA should be applied for the user to log in to the Windows client and the mobile client. This setting can also be changed for multiple users at a time by using the Security list type in the User list procedure. The following options are available:
- Use default settings – The general security settings configured in the Security settings procedure determine if MFA should be applied for the user by default.
- On – MFA is always activated for the user.
- Off – MFA is always deactivated for the user.

#### Authentication device
By clicking the Register device button you can register an authentication device for the user. The users can also register their devices in the User settings function. Follow this instruction to registered a device for the user:
1. In the dialog under the button, you scan the QR code that appears. You do this in an authentication app on the user's device, such as Microsoft Authenticator or Google Authenticator.
2. If you are unable to scan the QR code you can manually enter the 32-character text code shown under the QR code.
3. In a field in the dialog you then enter the six-digit code which is returned by the app.
4. Click OK in the dialog to register the device.
5. Then you should save the settings made by saving in the procedure.
If the user later on change their device, you should use the Remove device button to remove the user’s device and this makes it possible to register the new device.

#### Device registration date
Here you see the date when the user’s device was registered.

#### Blocked for registration
If the registration period for MFA in the Security settings procedure has expired, you can use the Reset period button to remove the block from the user.

#### Registration period end date
Here you see the end date of the registration period for the user. That is, before when the user must register a device.
