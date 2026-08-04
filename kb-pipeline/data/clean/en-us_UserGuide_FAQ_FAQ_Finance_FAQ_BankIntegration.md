### FAQ – Bank integration
Which banks are supported?
The following banks are currently supported:

##### Sweden:
- Danske Bank
- Handelsbanken
- Nordea
- SEB
- Swedbank

##### Norway:
- DNB
- Nordea
- Sparebank1
- Handelsbanken
- Eika

##### Finland:
- Nordea
How do I get up and running with Bank integration?
You can activate the Bank integration yourself, directly in the Monitor ERP. This is done in the Bank settings procedure.
You find more information about activation and settings [here](../../Using/BankIntegration/BankIntegration.htm).
What is Open Banking?
Read more about Open Banking [here](../../Using/BankIntegration/OpenBanking.htm).
What is Global Pay?
Read more about Global Pay [here](../../Using/BankIntegration/GlobalPay.htm).
What is File pay ISO?
Read more about File pay ISO [here](../../Using/BankIntegration/FilePayISO.htm).
I received an error message when activating the Bank integration, what do I need to do?
| Error message | Explanation/Action |
|---|---|
| Failed due to invalid or missing user rights | The user does not have correct access to the bank account. Go to your online bank and make sure the user has access to the bank account. |
| The user is not authorized to perform requests in Open Banking | This can occur when the user does not have sufficient access rights to access the bank account via Open Banking. Check the settings in your internet bank and that the setup is been completed according to the onboarding. |
| Invalid activation request | This can occur when the user does not have sufficient access rights to access the bank account via Open Banking. Check the settings in your internet bank and that the setup is been completed according to the onboarding. |
| Unauthorized | This is due to the time being wrong in Windows on the Monitor server. Adjust it to the correct time. |
| Internal server error | This is because Monitor doesn’t get a response when contacting the bank. Try again later. If the problem persists, contact the Monitor Support Center and report it. |
When does Monitor ERP load bank transactions from the bank?
Normally, Monitor ERP loads bank transactions from the bank between 07:00-09:00. This is the case for all banks except Swedbank (08:00-09:00) and Handelsbanken (07:15-09:00). Prior to the transactions being loaded, the system checks whether the payment details have been filled out. If the information is missing (due to a delay from the bank’s side), the system will wait and try to download the transactions again an hour later. This is repeated on an hourly basis until the transactions are ready to be downloaded. When the download is delayed, a notification is sent to the users entered under Notify when error occurs explaining why there aren’t any records to confirm. It is therefore important that you have entered users under the Notify when error occurs button under the Bank integration tab, in the Bank settings procedure so that they receive these notifications.
This means that you may not be able to confirm payments early in the morning as the transactions may not have been loaded yet.
Why can I not access the Manage transactions via bank integration tab in the Manage bank transactions procedure?
To access this tab you need to activate Bank integration for your user. Only users that have registered consent with their bank can access the tab. You also need to have access to the bank account via the bank in order to be able see this in Monitor ERP. You activate your user in the Bank settings procedure.
Why isn’t the Bank account info desktop component available?
To access the desktop component you need to activate Bank integration for your user. Only users that have registered consent with their bank can access the tab. You also need to have access to the bank account via the bank in order to be able see this in Monitor ERP. You activate your user in the Bank settings procedure.
No transactions to be confirmed are being loaded in Manage bank transactions, what can I do?
1. Check that your consent is still valid. Newly given consent can be activated in the Bank integration tab in the Bank settings procedure.
2. Use the Download transactions manually button in the Bank integration tab in the Bank settings procedure.
3. Check date and time in the Latest enrichment made in the Bank account info desktop component. The column is found under the More info button.
When loading transactions from the bank, the system checks that the transactions have been enriched with CAMT data from the bank, thereby ensuring that all necessary reference and payment information is available. This information helps you quickly see whether an account is ready to retrieve transactions or whether a delay in data enrichment may be the reason why transactions are missing. This check is done per bank account.
If the problem persists, please contact the Monitor Support.
How to I undo/cancel payments sent via Bank integration?
This depends on your bank. If you bank with SEB (Sweden) or Nordea (Sweden) and pay via Open Banking, you cancel payments in Monitor ERP and the payment is then automatically canceled by the bank. Otherwise, you need to cancel the payment manually both via the bank and in Monitor ERP. Payments are canceled in Monitor ERP via the Cancel outgoing payments list type in the Outgoing payments procedure.
How are user rights of those who can sent payments managed?
This is determined by your permission settings in the bank.
How are credit invoices managed in Bank integration?
In Bank integration there is no limit to the number of credit invoices per supplier and payment dates like there are with traditional ISO files. Regardless of whether you use File pay (ISO) or Open Banking, payment orders are sent at net value. The net value must however be positive.
However, please note that there is a limitation regarding the number of characters used for payment reference. The maximum character limit for total number of characters for the payment reference is 70 characters in connection to batch payment of debit invoices containing deductions for credit invoices. The limit applies to the total number of characters in the payment reference for all supplier invoices in the same batch. The limit applies per supplier and payment day.
How are File pay (ISO) and Open Banking payments signed? Is countersigning supported?
For File pay (ISO) payments, the bank file is uploaded to the bank via API and signing is done through the bank.
For Open Banking payments, signing is done through Monitor ERP. If you use countersigning, the first signing is done in Monitor ERP, and the second via the bank. Please note that SEB and Nordea do not currently support countersigning via Open Banking.
What is counter signing?
Counter signing means that multiple persons need to sign the payments. You set this up with your bank.
Does signing with BankID on card work?
Yes, most banks have support for using the bank’s login page (which opens embedded in Monitor ERP) to log in through methods other than Mobile BankID.
I have a yellow warning/red cross in Payments to sign, what does that mean?
If the payment has a green tick under Status, it means that the payment has gone to the bank. If there is a yellow warning or a red cross, it means that something has gone wrong and the payment has not gone to the bank. This can occur for individual payments or for an entire signing session. Under the Message button for the payment record, you can see what is stopping the payment from being sent to bank. If the error is for the entire signing session, you will see an error message in the Message column on the main row (the row at the very top) instead.
If a signing error occurs, the payment must be canceled. If the signing error is for the entire signing session, you will need to cancel the whole transaction list. If it is only individual payments, you only need to cancel the payments in question as the others have been sent to the bank. The issue needs to be resolved before you can resend the payment.
Below is a list of the most common error messages and what you need to do in order to resolve them:
| Error message | Explanation/Action |
|---|---|
| The OCR reference is invalid | The OCR number is missing or is incorrect. Check the number on the invoice and cancel the outgoing payment. Enter the correct OCR number on the invoice in the Register supplier invoice procedure and create a new outgoing payment. You may also need to activate or deactivate OCR in the Supplier register. |
| The specified amount limit (or daily amount limit) at the bank has been exceeded | Adjust the amount limit with your online banking service (internet bank). |
| The specified amount limit for the user at the bank has been exceeded | Adjust the amount limit for the user with your online banking service (internet bank). |
| Extended Mobile BankID is required | Swedbank requires that the user has extended BankID (applies to the person who is to sign the new recipient of the payment). If the person is a client with Swedbank, he/she can acquire extended BankID via online banking. If the person is not a Swedbank client, he/she needs to get an extended BankID by visiting a bank branch. |
| Direct customer to the bank to complete the task | The payment is stuck with the bank because they need to check it (e.g., an AML check). Contact your bank. This can occur when the bank detects a change in the payment habits of the company (for example, when starting to pay using Open Banking). The payment has to be cancelled in Monitor ERP and then created again after the bank has given the go-ahead to proceed. |
| Referenced basket not found | This is because the duality function for payments has been activated. Duality means that countersigning is required for payments to be executed and unfortunately the bank in question does not support it. You can work around it by changing or deactivating settings regarding duality, or you can pay via FilePay (ISO) instead. |
| Client is not onboarded for ISO Payments | The outgoing payment via FilePay (ISO) failed because the bank connection setup between OpenPayments and the bank is incomplete. |
| The consent has expired | Renew you consent in the Bank settings procedure under the Bank integration tab. |
| Invalid activation request | Please contact the Monitor Support Center to troubleshoot the issue. |
| Unauthorized | This is due to the time being wrong in Windows on the Monitor server. Adjust it to the correct time. |
How are bank charges in connection to international payments handled via Global Pay?
When using this payment method, you (the sender) are the one paying the bank charges. It is not your regular bank's fees/charges that apply, but a fee charged by Open Payments. This fee is often lower than what the banks usually charge. There will be no fee at all for the receiver since it is regarded as a domestic transaction.
You can also see the bank charge that will be charged for international payments via Global Pay in advance, before you send the payment. You can see this in the payment suggestion via the Load provided exchange rate and bank charge button. The fee will then be displayed in the list, in the Provided exchange rate column. The fee is recorded in connection with the payment confirmation in the Manage bank transactions procedure.
How are bank charges handled for international payments via File pay (ISO) if Global Pay isn’t used?
With this payment method, the outgoing payment is always sent with the bank charge code SHAR, which means that the sender and recipient pay for their own bank's costs.
Why can I not see the supplier’s bank account and payment reference in payment information when paying via Global Pay?
They payment is done in two stages when you pay via Global Pay:
1.   
The payment first goes into a client account with Open Payments. Therefore you cannot see the recipient’s (the supplier’s) bank account and payment reference in your bank’s payment information. It is Open Payment which is shown as the receiving account with the payment reference “OPESEXXXX” As you’re paying in the local currency and Open Payments manages all currency exchange, the payment will show in the local currency with your bank.
2.   
Open Payments exchanges the currency and sends the payment to the recipient’s (your supplier’s) bank account. The recipient receives the correct currency amount and the correct payment reference (invoice number) will show up on their bank statement.
Example of a company in Finland using Global Pay:
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/BankIntegration_GlobalPay_Flow2.png)](../../../../Resources/Images/TrainingMaterial/BankIntegration_GlobalPay_Flow2.png)
> When confirming payments made via Global Pay, an accounting record is automatically attached when the records are loaded from the bank. This accounting record shows more information about the payment (Proof of payment information). This document is automatically saved as a PDF to the voucher which is created during the confirmation reporting. This is a record of Open Payments paying your supplier and can be provided as proof of payment should you need to provide proof that the payment has been made. Read more about payment confirmation [here](../../Using/BankIntegration/BankIntegration.htm#Återrapportering).
How does currency conversion work with Global Pay? How are exchange rate differences recorded?
With Global Pay, an automatic conversion is performed at the time of each payment. The exchange rate offered at the time of conversion, along with the bank fee, is displayed in the payment suggestion. When you make the payment, you therefore know in advance which rate will apply. The exchange rate difference is posted during confirmation (based on the offered rate).
How are incoming payments (via Bankgiro) shown as a single bank transaction, matched?
Additional data is added to the incoming payment record resulting in separate records being created when performing the confirmation. Matching can then be done automatically with the accounts receivable.
