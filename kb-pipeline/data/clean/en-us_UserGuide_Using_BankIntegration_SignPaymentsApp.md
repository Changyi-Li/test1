### Signing payments in Monitor Mobile
In Monitor Mobile, our mobile client/app, you can:
- Signing payments
- Countersign payments (only with the following banks: SEB, Nordea Business, DNB, Sparebank1, Nordea Corporate Netbank, Handelsbanken Norge, and Eika Gruppen Norge)
- Countersign consent (only with Nordea Corporate Netbank)
You can only sign payments made via Open Banking. This feature can not be used for signing/counter signing payments via File Pay (ISO). These payments can only be signed via online banking.
> Please note that signing in Monitor Mobile is required by certain banks when using Open Banking for payments when counter signing. Read more under Countersign payments below.

#### Preparations
Version 25.3 or later of Monitor ERP is required.
Installation
To use Monitor Mobile, a web server must be installed. This is usually done by someone from Monitor Support Center (if not already installed).
You can read more about Preparation for installation of Monitor ERP Web server [here](../../InstallConfig/PreparationWebServer.htm), and Installation of Monitor ERP Web server [here](../../InstallConfig/InstallMONITORWebServer.htm).
The user must also have the mobile client installed as an app.
Read more about Install Monitor ERP mobile client app [here](../../InstallConfig/InstallMONITORApp.htm).
User
The user must have the Allow login to Monitor Mobile setting activated. The setting is found under the Security tab, in the Users procedure.
To access the Signing payments procedure in Monitor Mobile, the user needs to have at least one of the following rights:
- Signing payments (Monitor Mobile)
- Countersign payments (Monitor Mobile) – if you have Nordea Corporate Netbank, this setting gives the user the right to countersign consent.
Rights can be configured in the Roles/User rights tab in the Users tab.
> Read more about Monitor Mobile (mobile client) [here](../../GettingStarted/MobileClient.htm).

#### Signing payments
Once you’ve saved the list (payment suggestion) in the Outgoing payments procedure, press the Open transaction list button and close the procedure without signing. You will then be able to sign payments in Monitor Mobile. This means you will be able to choose whether you want to sign payments in Monitor ERP or in Monitor Mobile, as well as being able to sign payment suggestions that someone else has created.

#### Countersign payments.
Countersigning payments means that one person signs the payment in the Outgoing payments procedure in Monitor ERP and the other person countersigns the payment in Monitor Mobile. Please note that countersigning is not activated in Monitor ERP but is activated and configured via online banking. You must however activate the user’s rights in Monitor ERP so they’re able to access the signing function in Monitor Mobile (see Users above).
Signing in Monitor Mobile is a requirement for certain banks when using Open Banking and countersigning is necessary. In other words, if the bank requires the payment to be signed by both signers in the ERP system before the payment comes to the bank. This is the case for the following banks:
- SEB
- Sparebank1
- Nordea Business
- Nordea Corporate Netbank
- Handelsbanken Norway
- Eika gruppen
> For Nordea Corporate Netbank the app is needed for both countersigning payments via Open Banking and for countersigning consent (activate Bank integration for a user).
