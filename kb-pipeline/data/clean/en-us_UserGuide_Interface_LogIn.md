### Login
When you start Monitor ERP a login window is displayed. Here you select the company, enter the user name and password, and press Enter or click on the arrow [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LogOnButton.png)](../../../Resources/Images/UserGuide/LogOnButton.png) to log in.
When you start Monitor ERP next time, the company and the user you most recently entered will be default in the login window.
The login window is also shown if you have logged out of Monitor ERP. You log out in the desktop backstage. Use the Close ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_close.png) button in the top right corner to close the login window and shut down the program.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LogOnWindow.png)](../../../Resources/Images/UserGuide/LogOnWindow.png)

#### Password policy
There is support for a password policy which you can set up for the company in the Security settings procedure.
If the system administrator has set up a password policy and you are requested to change password, the new password is verified to ensure it complies with the policy. When a password must be changed, a dialog appears when you enter your current password, press Enter and click on the arrow [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LogOnButton.png)](../../../Resources/Images/UserGuide/LogOnButton.png) in order to log in. In this dialog, you enter and then confirm a new password.
When password policy has been activated there is also a protection function against so-called brute force attacks on passwords with purpose to gain access to the user’s accounts. If an incorrect password is entered six times in a row, a waiting time is activated. That is, 30 seconds must pass before you can enter the password again.

#### Integrated login
The system administrator can link your user account in Monitor ERP to your Windows account, so you will be logged in automatically when you start up Monitor ERP, a so-called integrated login. If you are using integrated login and log out of Monitor ERP, making the login dialog appear, you will see a link below the password field where it says Log in as [user name]. You can then click on the link and be logged in directly without having to enter the password.

#### Multi-factor authentication
If the system administrator has activated multi-factor authentication (MFA) for your user, there’ll be an additional login step whereby you’ll need to register a device – such as your smartphone or tablet – for MFA. This applies when logging in to the Windows client, the Web client and Monitor Mobile.
Begin by installing an authentication app on the device. Your company may have decided to use a particular authentication app. Common examples include Microsoft Authenticator or Google Authenticator.
> Please note! Please note that the system administrator has set a registration period which applies to all users. If you don’t register your device within this period you’ll either be forced to register the next time you log in, or you’ll be blocked for logging in. In the latter case you must contact the system administrator, who can remove the block on your user.
The first time you log in (before the device has been registered):
1.    
In the login window you choose the company and enter the user name and password.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LogOnWindow.png)](../../../Resources/Images/UserGuide/LogOnWindow.png)
2.     
Press Enter or click the arrow [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LogOnButton.png)](../../../Resources/Images/UserGuide/LogOnButton.png) (in Monitor Mobile you press Login) and a QR code will appear.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LogOnWindowMFA.png)](../../../Resources/Images/UserGuide/LogOnWindowMFA.png)
1. If you do not want to register your device during this login, click Skip in the login window, and you’ll be logged in.
2. To register your device, move on to Step 3.
3. Add a new account in the authentication app and choose to add by scanning a QR code.
4. Scan the QR code which is shown in the login window.
If you can’t scan the QR code you can also choose to enter a code manually in the app. You’ll then enter a 32-character text code, which is shown under the QR code in the login window. If you’re using Monitor Mobile, you copy this code using the button next to the code and past it in the app.
5.    
The account is added to the app, and a six-digit code is shown. In the field under the QR code in the login window you then enter the code which is shown in the app, and you’ll be logged in. In Monitor Mobile you can also copy the six-digit code from the app and paste it into the login window. The device is then registered.
> Please note that the code in the app is a one-time code which changes after a short period – usually 30 seconds. So you have to enter the code in the login window within this period, otherwise you must enter the next code that is shown the app.
Subsequent logins (when the device is registered):
1. In the login window you choose the company and enter the user name and password.
2. Press Enter, or click on the arrow [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LogOnButton.png)](../../../Resources/Images/UserGuide/LogOnButton.png).
3. You’ll now be asked to enter a six-digit code in the login window. Open the app to see the relevant code for the account.
4. Enter the code in the login window and you’ll be logged in automatically. In Monitor Mobile you can also copy the six-digit code from the app and paste it into the login window. In Monitor Mobile, a numerical keyboard also appears when you tap in the field for the six-digit code in the login window.
