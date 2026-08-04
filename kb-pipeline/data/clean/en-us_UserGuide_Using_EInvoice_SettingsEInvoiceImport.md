### Settings for import of e-invoice and invoice interpretation
Follow the steps below to activate e-invoice and interpretation of incoming supplier invoices in Monitor ERP.
> Make sure you have entered the correct information (VAT registration number, addresses, etc.) in the Company information procedure before configuring the settings.
> These settings are based on the most recent version of Monitor ERP. If you have an older version the settings may be different looking. Please contact our Support Center if you need help.

#### Before you can begin using the services in the system, the following settings must be configured:
1. Go to the Import tab in the Settings for export/import procedure.
2. Select Supplier invoice under import type.
3. Check E-invoice CrossState.
4. Enter the Company ID if you are already a customer with Crediflow and have a CrossState account. If not, you create an account with CrossState using the Create account button below. Once the account has been created, the company ID will automatically be filled in.
5. Select Production to use a production account with CrossState in order to import interpreted supplier invoices. Production accounts are given the extension @crossstate.se in the e-mail address.
6. Upload registers/Import invoices determines if registers should be uploaded, and if it should be possible to import invoices. When you activate this setting it means invoices can be imported to Monitor ERP and it is possible to upload registers. Register here means the supplier register, order register, and – depending on if you have activated Reference matching – signers. Under the Upload/download method setting you choose if registers should be uploaded manually or if it should be scheduled. You upload registers in order to, for example, make it possible for CrossState to match the supplier on invoices you receive. This applies to both e-invoices and interpreted supplier invoices.
7.     
Upload/download method – Here you can choose how your registers should be uploaded to CrossState, as well as how invoices can be imported to Monitor ERP from CrossState.:
-   
Scheduled/Manual – Registers are automatically uploaded every night (between 19:00-22:00 CET), but you can also upload registers manually by using the Manual upload button. Invoices are imported automatically once an hour, but can also be imported manually via the Update button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) in the Register supplier invoice procedure.
-   
Manual only – Registers can only be uploaded manually via the Manual upload button. Invoices can be imported manually via the Update button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) in the Register supplier invoice procedure.
This setting is only active if you have selected Yes for the Upload registers/Import invoices setting.
8.   
Use the Create account button to register an account with CrossState if you do not already have an account with them. In the dialog shown you first have to select a partner type. Select Monitor to create a Monitor-partner account with CrossState. Monitor is selected by default. The option Crediflow should only be selected in exceptional cases if an independent customer account should be created with CrossState. This is if you are an existing customer to CrossState and want to start importing invoices in Monitor ERP.
Make sure the company information is correct and enter a contact person and that person's contact information. If you have a GLN number (Global Location Number) registered, please contact the Monitor Support Center to get help to activate it on your account.
9.   
Activate e-invoice
Select Activate e-invoice in order to activate e-invoice for import of actual supplier invoices to Monitor G5. If you only want to create an account for invoice interpretation, do not mark this checkbox.
Check the setting Register my party in Peppol directory if you want to register your company as receiver of e-invoice in the official Peppol register. This registration can be done directly when creating a new account, or it can be done later on if you already have an account. For Norway it is Register my party in ELMA register. This is used on order to be shown as being a receiver of e-invoice in the ELMA register.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CreateAccount_CrossState.png)](../../../../Resources/Images/TrainingMaterial/CreateAccount_CrossState.png)
> Depending on which country package your company is applying, the company may also become automatically registered in e-registers when you create an account. The E-register functions as a list of electronic addresses where it is stated if your company can receive and/or send e-invoices. For Sweden the registration is done in NEA, for Finland it is done in TIEKE, and for Denmark it is done in NemHandelsregister.
10.   
Check the I have read and accepted the terms/conditions for this service box. The account becomes created when you click the Create account button. The account is created via an API connection to CrossState. If everything works correctly you will automatically receive your company ID. Now the account registration is completed.
11.   
Use the button Manual upload to manually upload the supplier register. This button is suitable to use the first time when you activate the account to make sure everything can be uploaded as it should. If a problem should occur during the uploading, you will be shown a notification about this and information about which supplier cannot be uploaded. The manual uploading cannot be done until you have an account.
12.   
How to activate invoice interpretation
Select Activate manual verification and interpretation of invoices via e-mail, which determines if manual verification and interpretation of invoices should be used. In the field called E-mail for invoice interpretation you enter the e-mail address that should be used during manual verification and interpretation of invoices via e-mail. The domain part of the e-mail address is obtained from CrossState. It is recommended that you enter an e-mail address according to the following format: CompanyName_AbbreviatedCompanyName(@crossstate.se). Leave the e-mail field using Tab when you have entered the address.
> Please note! The e-mail address can consist of a maximum of 21 characters (not including @crossstate.se). Only use the following characters: a-z, A-Z, 0, 1-9, _, -.
In the E-mail for deviation notification field you enter the e-mail address for messages about deviations in CrossState. That is, when CrossState receives attachments for interpretation that are not supported/cannot be processed. We recommend that you enter an address here to ensure you don’t miss any information if something goes wrong when uploading invoices to CrossState. Remember not to enter an address where forwarding of e-mail is configured.
Activate invoice-received notification – Here you decide if you should receive an e-mail with a confirmation for each invoice you send in to CrossState for interpretation/verification. This checkbox is not checked by default.
When you have entered the e-mail address, a row is created where you can see, for example, invoice type, application ID, e-mail address, and reference matching. The e-mail address shown on this row is the address to which you should send your PDF invoices for interpretation. You should send your invoices to the specified address regardless if they are order invoices or expense invoices, and it also does not matter if you apply EIM or EIM Workflow. However, if you have EIM Workflow you must also configure additional settings for your suppliers in order to determine if invoices should be imported as order invoices or as expense invoices. See [Settings for supplier](SettingsSupplier.htm).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/OneApplication_CrossState.png)](../../../../Resources/Images/TrainingMaterial/OneApplication_CrossState.png)
Verification – Here you can choose how your expense invoices should be verified. By default, the verification is carried out in Monitor ERP but you can choose to verify in CrossState. If you are only using EIM, we recommend you to carry out the verification in Monitor ERP. If you are using EIM Workflow, your order invoices are always verified in CrossState.
> Please note! To verify invoices in CrossState, training is required.
Reference matching – For expense invoices it is possible to activate reference matching. This means the entered reference (our) on an interpreted supplier invoice will be matched to our references who are signers. When verifying in Monitor ERP, the matching will take place at import when the invoice is registered. When verifying in CrossState, the list of signers is exported to CrossState and matching will take place there.
If a match is found, the reference person will be entered as signer for the registered invoice. An imported matched invoice will go straight to authorization after registration. If a match cannot be made, the invoice will be sent to the Pending inbox after the registration. If the EIM Workflow option is used, the invoice will instead be placed in the inbox called Create authorization list.
Please note! If the supplier of the interpreted invoice has a main signer selected in the supplier register, that signer will always be used on the invoice.
13.   
You can select the recipients of error messages by clicking the Notify when error occurs button. These messages will be shown if something goes wrong when exporting registers or importing supplier invoices. The error messages are shown as notifications for the affected users in the system.
14.   
Save in the procedure.
> Please contact the Monitor Support Center if a problem occurs when you register the account.

#### Last invoice import
Here you see the date and time of the most recent import of supplier invoices.

#### Last update of registers
Here you see the date and time of the most recent register update sent to CrossState.

#### Show registered information
This button is available when you have entered your company ID or created an account. Here you see the registered company information and information registered regarding the e-invoicing.

#### Activate e-invoice
This button is active even if you have NOT chosen to activate yourself when you created the account above. A red message appears if it was not possible to create an account with e-invoice recipients when registering.
The reason why it was not possible to create an e-invoice account (activation failed) may be due to your organization information being associated with a different operator. This might for example occur if your company has been using e-invoice in a different ERP system and was then using a different operator.
If that is the case, you MUST contact your old operator and ask them to release your organization information. You must actively notify your old operator that you want to change operator. This is similar to a mobile phone number which is tied to an operator and you must ask them to move the phone number to a different operator.
Once the information is released you can click Activate e-invoice again.
> Tip! If you are unsure of which operator you have, please contact the Monitor Support Center for assistance.
It is wise to plan ahead regarding changing the operator, so you are sure you have the correct operator on the go-live date and you use e-invoice. You must then notify your current operator that you are terminating the agreement and on which date they should release the information for the new operator to activate.
