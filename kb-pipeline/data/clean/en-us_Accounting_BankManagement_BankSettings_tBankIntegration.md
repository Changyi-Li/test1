### Bank integration
Under this tab you can activate Bank integration. To activate bank integration, you need to have first activated your bank under the Bank activation tab, as well as having activated the Register incoming and outgoing payments in the same procedure/journal system setting and created a voucher number series for the journal Payments in the Voucher number series/Journals procedure.
> You can also read about how you get up and running with [Bank integration](../../../UserGuide/Using/BankIntegration/BankIntegration.htm) under Using Monitor in the online help.

#### The following banks are currently supported:

##### Sweden:
- Danske Bank
- Handelsbanken — only File pay ISO
- Nordea (Nordea Business)
- SEB
- Swedbank

##### Norway:
- DNB
- Nordea (Nordea Bedrift) — only Open Banking
- Sparebank1 — only Open Banking
- Handelsbanken — only Open Banking
- Eika — only Open Banking

##### Finland:
- Nordea (Nordea Business) — only Open Banking
> A feature overview for Bank integration can be found [here](../../../UserGuide/Options/BankIntegration.htm).
Bank integration means that you can see the balance of your bank accounts in Monitor ERP and can also sign payments without having to manage payment files via online banking. The feature uses the new generation of payment solutions, Open Banking, under the EU‘s payment services directive (PSD2). This means that the bank permits a third party supplier to make payments via APIs and load account information on your behalf. The third-party supplier of the service is Open Payments. They are licensed and under the supervision of Finansinspektionen (or other competent authority in the EU/EES). Bank integration also offers the more traditional platform for bank integration where ISO files (File pay ISO) are used. In Monitor ERP this is managed via two separate payment methods.
Consent for bank integration is per user, meaning that each user that needs to access the feature, needs to consent to it. Activation and consent takes place via mobile BankID. To active bank integration, your personal identification number needs to be entered as well as your user being linked in the Personnel records – General procedure.
> You can also see all users that have access to bank integration via the Bank integration button under the Bank accounts tab.
You activate bank integration by clicking the Activate bank integration button. A dialog window opens where you need to accept the terms and conditions of the feature. A QR code is then shown which you scan with your BankID app. The system then matches the bank accounts that you have access to with the bank accounts registered under the Bank accounts tab. The result is shown under Bank accounts activated for bank integration. When bank integration is activated for the user in question, electronic consent is given for 180 days. Consent then needs renewing via the Renew consent button.
> To use this function, your company needs to have carried out a mandatory know your customer check. You can read more about this under KYC under Bank integration settings below.
Bank integration settings

#### Bank
Here you determine which bank the integration should be used with. By default, this is the bank activated under the Bank activation tab.

#### Onboarding at bank
Clicking this button links you to your bank for onboarding or to a page with more information on how you can onboard with your bank.

#### Signing of consent
Determines whether signing of consent is done in Monitor ERP or on the bank’s website. This varies depending on the bank.

#### Signing of payments
Determines whether signing of payments is done in Monitor ERP or on the bank’s website. This varies depending on the bank.

#### Activate bank integration
By clicking this button you activate bank integration.
> Please note that you need to onboard with your bank prior to activating bank integration. You can read more about onboarding with different banks [here](../../../UserGuide/Using/BankIntegration/BankIntegration.htm).

#### Renew consent
This button is used to renew consent.

#### Remove consent
Click the Remove consent button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png) if you want to remove consent.

#### Valid for
Shows which user the consent is for.

#### Valid to
Shows the date that the consent is valid until. A week before the consent runs out, the user will receive a notification reminding them of this.

#### Status
Shows the status of the consent – valid or invalid

#### KYC
By clicking this button you can carry out the obligatory KYC (know your customers) checks.
This can be done by any of the following people:
- An authorized signatory of the organization
- A person authorized to act on behalf of the company (e.g. CEO or a head of finance)
This button also activates the service Global Pay free of charge. This feature is used when making international payments. Global Pay involves connecting your bank account (in local currency) to a solution where currency payments are managed by an external party.
> You can read more about international outgoing payments via Global Pay [here](../../../UserGuide/Using/BankIntegration/GlobalPay.htm).

#### Performed/signed by
Here you can see which user and done the KYC check/activated Global Pay.

#### Valid to
Shows the date that the consent is valid until.

#### Status
Shows the status of the consent – valid or invalid
Error messages

#### History
The History button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) shows you a log of any error messages and when they were created.

#### Notify when error occurs
Here you select recipients for any error messages. The error messages are shown as notifications for the affected users in Message center.

#### Download transactions manually
By clicking this button you can download transactions manually. Normally, you do not need to use this button as transactions are loaded over night, but in case there has been any operational disturbance throughout the night, you can can use this button instead of waiting for the following day.
