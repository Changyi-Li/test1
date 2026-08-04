### Import
Under this tab you configure settings for different import types available in Monitor ERP. Some import types have several alternatives. You can select which alternative should be used by default.
Customer orders
Today, there are no settings regarding customer orders. Importing customer orders via Monitor-to-Monitor is standard functionality.
Supplier invoice
Importing supplier invoices in Monitor ERP can be using Monitor-to-Monitor standard functionality.
We recommend you to acquire the EIM (Electronic Invoice Management). option. You then get access to a plugin for import of interpreted supplier invoices via CrossState (Crediflow). In this option an agreement with Crediflow is included.
If you already have your own agreement with a different e-invoice service, there is also a cost-free plugin for import of interpreted supplier invoices via the Peppol BIS 3.0 format.
Please contact Monitor ERP System AB for additional information and to purchase options.
> Contact the Monitor Support Center if you need help regarding how to enter the e-invoice information.
E-faktura PEPPOL
To be able to import supplier invoices via the format Peppol BIS 3.0, you need to configure the following settings:

#### Use FTP
Check this box in order to configure settings and receive invoice files via FTP.
> Check with your e-invoice supplier which FTP settings you should configure.

#### FTP server
Enter the address to the operator's FTP server, for example. "ftp.company.com". You do not have to use "ftp://" at the beginning of the address. Check with your e-invoice operator how the FTP settings should be configured.

#### Port
Here you enter the port for FTP communication. The standard port is 21 (control channel for unencrypted FTP). This is selected by default. If you select Implicit (FTPS) as encryption method below, the port should be changed to 990 (control channel for implicit FTPS).

#### Encryption method
Select if the FTP connection should be SSL encrypted as Implicit (FTPS) or Explicit (FTPS). The default alternative is None (FTP), that is, unencrypted FTP. Implicit encryption is normally initiated over port 990. Explicit encryption is initiated over the standard port 21.

#### User name
Enter the user name for the FTP account.

#### Password
Enter the password for the FTP account.

#### Path
Here you enter the source path to the directory on the FTP server from where your import files should be loaded.

#### File in source path
Here you configure if the import file should be deleted or not in the source path after an import has been made.

#### Test connection
By clicking Test connection, you can verify that the connection to the FTP server works.

#### Target path
Here you configure the path to the directory where the import file should be saved after an import has been made. You must enter a UNC path to a shared directory, for example \\your_server\shared_directory.

#### Most recent loading
Here you see time and date of the most recent loading.

#### Most recent status
Here you see a log containing the most recent loading. If everything is working, an OK is displayed. If something goes wrong, an error message appears.

#### Scheduling active
Check this box if automatic download of e-invoice should be active. Download is scheduled to take place every hour.

#### Notify when error occurs
Here you select recipients for any error messages. The error messages are shown as notifications for the affected users in the system.
E-invoice CrossState
> If you need help to configure these settings, please contact the Monitor Support Center. More information about how you create an account is also available [here](../../../UserGuide/Using/EInvoice/SettingsEInvoiceImport.htm).
> Please note! When you are registering the account and you are about to use the Workflow option, it is important that the Activate EIM Workflow system setting has been set to Yes before you create the account in order to generate correct settings for the application.
Please note! This requires the EIM option. To be able to import supplier invoices via CrossState, the following settings must be configured.

#### Company ID
If you are already a customer with Crediflow and have a CrossState account, you should here enter your company ID. If you are not a customer with them, you should use the button Create account. Once the account has been created, the company ID will automatically be filled in.

#### CrossState server
-   
Production – refers to a production account with CrossState used to import interpreted supplier invoices. Production accounts get the extension @crossstate.se in the e-mail address.

#### Upload registers/Import invoices
With this setting you determine if registers should be uploaded, and if it should be possible to import invoices. When you activate this setting it means invoices can be imported to Monitor ERP and it is possible to upload registers. Register here means the supplier register, order register, and – depending on if you have activated Reference matching – signers. Under the Upload/download method setting you choose if registers should be uploaded manually or if it should be scheduled. You upload registers in order to, for example, make it possible for CrossState to match the supplier on invoices you receive. This applies to both e-invoices and interpreted supplier invoices.

#### Upload/download method
Here you can choose how your registers should be uploaded to CrossState, as well as how invoices can be imported to Monitor ERP from CrossState.
-   
Scheduled/Manual – Registers are automatically uploaded every night (between 19:00-22:00 CET), but you can also upload registers manually by using the Manual upload button. Invoices are imported automatically once an hour (EIM) or according to your scheduling settings (EIM Workflow), but can also be imported manually via the Update button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) in the Register supplier invoice procedure.
-   
Manual only – Registers can only be uploaded manually via the Manual upload button. Invoices can be imported manually via the Update button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) in the Register supplier invoice procedure.
This setting is only active if you have selected Yes for the Upload registers/Import invoices setting.

#### Manual upload
This button is used to manually upload the supplier register. It is suitable to use the first time when you activate the account to make sure everything can be uploaded as it should. If a problem should occur during the uploading, you will be shown a notification about this and information about which supplier cannot be uploaded.

#### Last invoice import
Here you see the date and time of the most recent import of supplier invoices.

#### Last update of registers
Here you see the date and time of the most recent register update sent to CrossState.
> Please note! If you notice that these dates shown are a few days old, this is a sign that there might be a problem since invoice import takes place once per hour and the register update takes place once per day.

#### Activate manual verification and interpretation of invoices via e-mail
With this setting you decide if manual verification of supplier invoices should be applied and that the supplier invoices should be sent using e-mail for interpretation. This setting activates the fields below and the table for e-mail addresses.
E-mail for invoice interpretation
Here you enter the e-mail address that should be used during manual verification and interpretation of supplier invoices via e-mail. The domain part of the e-mail address is obtained from CrossState. It is recommended that you enter an e-mail address according to the following format: companyname_abbreviatedcompanyname@crossstate.se.
> Please note! The e-mail address can consist of a maximum of 21 characters (not including @crossstate.se). Only use the following characters: a-z, A-Z, 0, 1-9, _, -.
Leave the e-mail field using Tab when you have entered the e-mail address.
E-mail for deviation notification
Here you enter the e-mail address for messages about deviations in CrossState. That is, when CrossState receives attachments for interpretation that are not supported/cannot be processed. We recommend that you enter an address here to ensure you don’t miss any information if something goes wrong when uploading invoices to CrossState. Remember not to enter an address where forwarding of e-mail is configured.
Activate invoice-received notification
If you mark this setting, you will receive an e-mail with a confirmation/notification for each invoice you send to CrossState for interpretation/verification. This checkbox is not checked by default.
Verification
Here you can choose how your expense invoices should be verified. By default, the verification is carried out in Monitor G5 but you can choose to verify it in CrossState. If you are only using EIM, we recommend you to carry out the verification in Monitor G5. If you are using EIM Workflow, your order invoices are always verified in CrossState.
> Please note! To verify invoices in CrossState, training is required!
Reference matching
For expense invoices it is possible to activate reference matching. This means the entered reference (our) on an interpreted supplier invoice will be matched to our references who are signers.
When verifying in CrossState, the list of signers is exported to CrossState and matching will take place there. When verifying in Monitor ERP, the matching will take place at import when the invoice is registered.
If a match is found, the reference person will be entered as signer for the registered invoice. An imported matched invoice will go straight to authorization after registration.
If a match cannot be made, the invoice will be sent to the Pending inbox after the registration. If the EIM Workflow option is used, the invoice will instead be placed in the inbox called Create authorization list.
> Please note! If the supplier of the interpreted invoice has a main signer selected in the supplier register, that signer will always be used on the invoice.

#### Notify when error occurs
Here you select the recipients of error messages, if any. These messages will be shown if something goes wrong when exporting registers or importing supplier invoices. The error messages are shown as notifications for the affected users in Monitor ERP.

#### Delete supplier register
By using this button you can delete the uploaded supplier register in CrossState. The button is only available when an account has been registered and when deletion is possible to perform. This function is useful in cases when you want to purge the entire register or when duplicates have been created in the uploaded supplier register. Duplicates in the supplier register may be created if you, for example, in the start-up phase of Monitor G5 have uploaded the supplier register to CrossState but at a later stage imported the supplier register again to Monitor. This will result in the matching of correct supplier on the invoices not working as intended.
> Please note! Please note! This means that the interpretation function’s stored "knowledge” will also be deleted.

#### Create account
Use this button to register an account with CrossState if you do not already have an account with them.
In the dialog shown you first have to select a partner type. Select Crediflow if an independent customer account should be created with CrossState. Select Monitor if a Monitor partner account should be created with CrossState. Monitor is selected by default.
If you have a GLN number registered, please contact the Monitor Support Center to get help to activate it on your account (Global Location Number).
Make sure the company information is correct and enter a contact person and that person's contact information.
Activate/register for e-invoice
Here you determine if e-invoice should be activated. Deactivate this setting to keep from accidentally getting actual supplier invoices in to the test company during the test period.
Check the Register my party in Peppol directory setting if you want to register your company as receiver of e-invoice in the official Peppol register. This registration can be done directly when creating a new account, or it can be done later on if you already have an account.
Check the I have read and accepted the terms/conditions for this service box.
The account becomes created when you click the Create account button. The account is created via an API connection to CrossState. If everything works correctly you will automatically receive your company ID. Now the account registration is completed. Remember to save.

#### Show registered information
This button is available when you have entered your company ID or created an account. Here you see the registered company information and information registered regarding the e-invoicing.

#### Activate e-invoice
This button is active even if you have NOT chosen to activate yourself when you created the account above. A red message appears if it was not possible to create an account with e-invoice recipients when registering.
The reason why it was not possible to create an e-invoice account (activation failed) may be that your company information/organization information is "locked" to a different operator. This often happens if your company has been using e-invoice in a different ERP system and was then using a different operator.
If that is the case, you MUST contact your old operator and ask them to release your organization information. The Monitor Support Center (together with Crediflow/CrossState) cannot take over this ID. You must actively notify your current operator that you want to change operator. This is similar to a mobile phone number which is tied to an operator and you must ask them to move the phone number to a different operator.
Once the information is "released" you can click Activate e-invoice again.
Please note! It might be difficult to know if your organization information is locked to a specific supplier since this information can be very hard to access in some systems. If you are unsure of which operator you have registered, you can contact the Monitor Support Center and we can find out for you.
It is wise to plan ahead regarding changing the operator, so you are sure you have the correct operator on the go-live date and you use e-invoice. You must then notify your current operator that you are terminating the agreement and on which date they should release the information for your new operator to activate.
If you have entered an incorrect GLN number, it is not possible to create the account in a correct way. This button will then be shown. Here you can then correct that number and update/add contact information.
Accounting
For accounting SIE import (Sweden) you configure setting in the Export/Import procedure in the Accounting module.
Confirmation outgoing payments
Here you configure settings for confirmation of outgoing payments. You activate the formats for each bank under the Bank activation tab in the Bank settings procedure.
You select which Payment format should apply per electronic outgoing payment method under the Payment method tab in the Bank settings procedure.

#### Path
Here you enter the path to the directory from where files should be loaded.

#### Filing path
Here you enter the path to the directory where you want to save confirmed files.
Confirmation incoming payments
Here you configure settings for confirmation of incoming payments. You activate the formats for each bank under the Bank activation tab in the Bank settings procedure.
You select which Confirmation format should apply per electronic incoming payment method under the Payment method tab in the Bank settings procedure.

#### Path
Here you enter the path to the directory from where files should be loaded.

#### Filing path
Here you enter the path to the directory where you want to save confirmed files.

#### Matching rule
Here you determine which matching rule should apply:
- Invoice number + amount – Match both invoice number and the amount. If the difference between the paid amount and the invoice amount is greater (both higher and lower) than the maximum allowed difference, no automatic matching of the record is made.
- Invoice number – Match the invoice number. If the difference between the paid amount and the invoice amount is higher than the invoice amount, no automatic matching will be performed. If, on the other hand, the difference between the paid amount and the invoice amount is lower than the invoice amount, the record will be matched automatically with the write-off code Partial payment.
Differences between the paid amount and the invoice amount that are within the scope of the maximum allowed difference will be automatically matched for both matching rules with the write-off code you specified in the system setting called Default write-off code when diff. occur in auto-matching.

#### Maximum difference allowed
Here you can enter the maximum difference allowed of amounts for matching. See above under Matching rule. The system setting called Default write-off code when diff. occur in auto-matching applies here as well.
Order response
Today, there are no settings regarding order responses. You can import order responses via Monitor-to-Monitor.
Bank account reconciliation
Here you configure settings for bank account reconciliation via file in the JSO XML format.

#### Path
Here you enter the path to the directory where files should be saved.

#### Filing path
Here you enter the path to the directory where you want files to be filed.
Monitor Expense
Here you configure settings for import of vouchers/expense reports from Monitor Expense.

#### API key
Here you enter the API key from Monitor Expense.
> This API key is created in Monitor Expense by the user who is the administrator. You create an API key by going to Users, then click API keys and choose Add API key. Then activate the checkbox called Access token (long-term), enter a description for your API key and save. In the Client secret/Access token column you now find your API key.

#### Environment
Here you select the environment in which your Monitor Expense account is created. The default option is Production.

#### Automatically import valid vouchers
With this setting you decide if you want valid vouchers to be imported automatically. If this setting is activated, all valid vouchers will be automatically imported to the bookkeeping, instead of being handled manually in the Import from Monitor Expense procedure.

#### Generate auto. postings/allocations when saving
With this setting you decide if automatic postings/allocations should be recorded when you save the voucher in the Import from Monitor Expense procedure. If your vouchers are imported automatically, the automatic postings/allocations will also be made automatically if this setting is activated. You can choose whether automatic postings/allocations should be generated for vouchers regarding Business cards, Private expenses, or both.

#### Attachment type
Here you see which attachment type has been selected for Monitor Expense. The attachment type is selected in the Scan documents procedure.

#### Import log
Here you find a log containing the imports made from Monitor Expense. In the log you see the number of valid and invalid vouchers.
> Invalid vouchers must always be handled in the Import from Monitor Expense procedure.

#### Synchronize dimension codes
Here you can decide if the dimension codes should be synchronized with Monitor Expense. This means that you in Monitor Expense will be able to select among the dimension codes available in Monitor ERP in a dropdown menu. If the checkboxes are not marked, you have to manually post dimension codes (entered as additional text) in Monitor Expense.
> Please note! Dimension codes created in Monitor Expense will be deleted regardless of the setting being activated or not.

#### Notify when error occurs
Here you select the recipients of error messages, if any. These messages will be shown if something goes wrong when importing vouchers/expense reports from Monitor Expense. The error messages are shown as notifications for the affected users in Monitor ERP.

#### Start import
Click here to start the import. If you have activated the setting called Automatically import valid vouchers, vouchers will be imported every night (between 7 p.m. and 11 p.m. CET).
