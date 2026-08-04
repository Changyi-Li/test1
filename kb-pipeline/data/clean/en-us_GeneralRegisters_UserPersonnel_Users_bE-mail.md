### E-mail
Please note! All e-mail settings must be correctly configured before the user can use calendar integration of activities in Monitor ERP.

#### E-mail method
Determines the type of e-mail communication that the user should apply.
- Client based, via Microsoft Outlook – If the user has Outlook installed, you can select this option.
- Server based, via Microsoft Exchange – If the built-in e-mail client in Monitor ERP should be used toward Exchange, you should select this option.
- Server based, via SMTP – If some other e-mail server than Exchange is used, select this option.
- Server based, via Microsoft Exchange Online – If the built-in e-mail client in Monitor ERP should be used toward Exchange Online, select this option. In this case there must be a client application for Oauth 2.0 registered in Microsoft Entra ID (previously Azure Active Directory). Please see [this guide](../../BasicSettings/SystemSettings/GuideOAuth2.0.htm).

#### E-mail address
The user’s email address.

#### User name (Exchange)
If you in the E-mail method setting above selected one of the Exchange options, you must here enter the user name for the user’s account in Exchange.

#### Password (Exchange)
If you in the E-mail method setting above selected one of the Exchange options, you must here enter the password for the user’s account in Exchange. First you need to unlock the field by clicking the padlock button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png).

#### Send copy to own e-mail address
Here you choose if you should receive a copy of the e-mail messages you send from Monitor ERP. The available options are No copy, Copy (CC), and Bcc.
This function is only supported if you have selected a server based alternative in the field E-mail method or in the system setting called E-mail sending method.

#### E-mail signature
Under the E-mail signature button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can add an e-mail signature. You can format the text and add images, links, etc. as a signature. You are able to copy an existing signature from Outlook and paste it in.
If you are using a method for sending e-mails that requires Outlook to be opened externally, the e-mail signature you have entered here will not be carried over. The signature only works with methods that use the inbuilt e-mail client in Monitor ERP.
