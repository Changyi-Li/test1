### Settings for EIM
Here we have described the different settings required to configure before you can start using EIM in Monitor ERP.
Users
In this procedure you configure settings regarding different user rights for the users who will be working with EIM.

#### The Roles/User rights tab
There are predefined user rights for EIM in the different roles included in the system, for example the roles Financial manager and Purchaser. In the box Resulting user rights you see all the user rights included in a role after you have added the role to the user. In most cases the roles available for the users of EIM are sufficient, but in some cases you also need to configure unique user rights for these users. For EIM you configure the settings in the sections called Scan supplier invoice, EIM, and EIM document in the box User-specific user rights.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMUsersRolesRights.png)](../../../../Resources/Images/TrainingMaterial/EIMUsersRolesRights.png)
In the example above a user with the role Financial assistant has also been given permission to change authorized row, which is then shown in the box Resulting user rights.
System settings
You should only activate the system setting called Use extended authorization on posting rows if you want it to be possible to enter who should review/authorize the invoice on posting row level for expense invoices. This setting also determines the head signer for both expense invoices and material invoices (order invoices). Via settings on accounts and dimensions you can determine who should authorize each posting row depending on the posting. This applies to systems with EIM and EIM Workflow.
With the system setting Activate EFH Workflow you can activate the EFH Workflow option. When you purchase EFH Workflow, the system setting is deactivated by default.
Authorization settings – EIM
In this procedure you make settings for authorization of supplier invoices.
The Signers tab
Add the users who should authorize supplier invoices. Complement with settings for Authorization limits, Absence from authorization of invoice, Reminders, Forward authorization, and User right to view invoice documents. The final setting can also be found under the EIM button in the Users procedure. The Reminders settings also determine whether reminders should be shown in the Tasks – EIM desktop component.
The Signer groups tab
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMSigners.png)](../../../../Resources/Images/TrainingMaterial/EIMSigners.png)
Create signer groups, if needed. In a signer group it is enough if one of the included signers authorize the invoice, then the invoice can go ahead in the flow. This is different from an authorization list where it is required that all signers in the list authorize the invoice.
The Authorization lists tab
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMSignerGroups.png)](../../../../Resources/Images/TrainingMaterial/EIMSignerGroups.png)
Create authorization groups, if needed. An authorization list is a list of signers, and the invoice must be authorized by all signers in the list before it can be final recorded. In distinction from a signer group, when an invoice is sent to an authorization list it needs to become authorized by all signers in the order of the list.

#### An authorization list can have Parallel authorization. If you activate this setting, the invoice will be sent for authorization to all signers at the same time, that is, the invoice does not have to be authorized in a specific order.
The Authorization limit exceptions tab
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMAuthorizationLists.png)](../../../../Resources/Images/TrainingMaterial/EIMAuthorizationLists.png)
Create exceptions from authorization limits, if needed. These exceptions might be based on supplier category, supplier group, or supplier.
The DimensionsDimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. tab
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMAuthorizationLimitExceptions.png)](../../../../Resources/Images/TrainingMaterial/EIMAuthorizationLimitExceptions.png)
If you apply authorization at row level (activated with the system setting called Use extended authorization on posting rows, this tab will be available. Here you configure Signer/Approver and Head signer per dimension code. For projects you can select Project manager or Our reference from the Project register as Signer/Approver and Head signer.
The Priority for row authorization tab
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMPostingDimensions.png)
If you apply authorization at row level (activated with the system setting called Use extended authorization on posting rows, this tab will be available. Here you enter the central rules regarding priority which determine who should be the signer/head signer of the row if there are multiple persons responsible for the same posting row. For example, that authorized signer for the account is carry more weight than the authorized signer for the cost center.
The tab User right to view invoices
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMPriorityRowAuthorization.png)
Create user rights groups for viewing of invoices and configure terms per group regarding which invoices should be shown and not. A signer can then, if needed, be linked to a user rights group.
The Scheduling tab
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMUserRightViewInvoices.png)](../../../../Resources/Images/TrainingMaterial/EIMUserRightViewInvoices.png)
Activate the two services called Forward authorization and Reminder via e-mail and select a schedule or a time interval in the Settings box, this will determine when the services will run. Using the Run button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) you can also run the services manually. Also make settings in the box Settings for Reminder via e-mail for the service Reminder via e-mail.
Settings for incoming e-mail
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMScheduling.png)](../../../../Resources/Images/TrainingMaterial/EIMScheduling.png)
In this procedure you can add an e-mail account tied to an Exchange or IMAP e-mail server and select the type Monitor-to-Monitor for the account in question. The purpose is to get incoming Monitor-to-Monitor e-mail invoices straight in to the EIM work flow. Using the button Validate selected address ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) you can test that the account settings are correct. If they are correct, a green check mark will be shown in the column to the far left. If the information has not been entered in a correct way, a yellow warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) will be shown. Incoming Monitor-to-Monitor e-mail invoices will then automatically be placed in the separate inbox called Inbox Monitor-to-Monitor in the Register supplier invoice procedure. This inbox is also available as a desktop component (see further down).
Settings for export/import
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMSettingsIncomingEmail.png)](../../../../Resources/Images/TrainingMaterial/EIMSettingsIncomingEmail.png)
If you have installed options for OptoSweden or Readsoft e-invoices, you can in this procedure check that you have the support for these formats. This is done by selecting the import type Supplier invoice under the Import tab. For OptoSweden, you’ll see the format OPTO-to-Monitor. For Readsoft, you’ll see the format READSOFT-to-Monitor. However, the Default setting is not significant for this import type.
On advanced scanners there is a display where you can choose how/where to save the files. If you have such a scanner you can on the scanner select to save the files in the folder you have configured as inbox, as described to below. Then you do not need to use the procedure Scan supplier invoices when scanning.
The Scan tab
> Configure settings for scanner and select a path to the inbox in the Settings box The path must be entered in the box PDF inboxes under the next tab.
The tab Paths for inboxes
In the box called PDF inboxes under this tab you register at least one path to a folder which will be the PDF inbox for scanned paper invoices. This is where the PDF files should be saved at the scanning.

#### If other users of the EIM should have access to scanned invoices in the inbox, during registration in the procedure Register supplier invoice, then the path should point to a shared folder on a computer in the network. The other users must have the permission to Modify in Windows for that folder.
Option for OptoSweden and Readsoft
> If you have installed one of the options OPTO-to-Monitor or READSOFT-to-Monitor for EIM, you should register a path to a folder which will be the XML inbox for e-invoices (electronic invoices) received via OptoSweden or Readsoft (Lexmark). You register this path in the box called XML inboxes. The folder in question must be located on the Monitor ERP server. You should also to register a path to a filing folder to make it possible to file these e-invoices which have been registered. This folder must also be located on the Monitor ERP server.
Supplier register
The Settings tab
Select a default Signer code per supplier. The signer codes you can select among are the signers and authorization lists registered in the procedure Authorization settings – EIM. The selected signer or authorization list will then be default to authorize invoices from the supplier in question.
Chart of accounts
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMSignerCodeSupplierRegister.png)](../../../../Resources/Images/TrainingMaterial/EIMSignerCodeSupplierRegister.png)
If you apply posting on row level (activated via the system setting called Use extended authorization on posting rows, you may have to enter a Signer/Approver and Head signer for accounts.
Backstage
Desktop
All users who are signers can add the components Tasks – EIM and Inbox Monitor-to-Monitor, and Inbox e-invoice/XML in their desktop configuration. An alternative is than the administrator adds these components in a desktop template which the signers can then use.

#### Having these three components on your desktop will make it easier to monitor activities related to supplier invoices and you can also easily register/preliminary record invoices.
You can double-click a task on the desktop, this will take you to Tasks and you can perform the task assigned to you.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMDesktopBackstage.png)](../../../../Resources/Images/TrainingMaterial/EIMDesktopBackstage.png)
You can double-click an invoice in the inbox, this will take you to Register supplier invoice with the invoice loaded, to register/preliminary record the invoice.
The component called Inbox e-invoice/XML displays the e-invoices/XML files which have been received. The component scans the XML inboxes which are registered under Paths for inboxes in the Scan supplier invoices procedure. If you have received invoices, you can start the import by clicking ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png) or double-clicking on the row. You can start downloading from the operator’s server manually by clicking ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png). Click ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_preview.png) in order to preview the PDF invoice.
The component called Inbox e-invoice/XML displays the e-invoices/XML files which have been received. The component scans the XML inboxes which are registered under Paths for inboxes in the Scan supplier invoices procedure. If you have received invoices, you can start the import by clicking ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png) or double-clicking on the row. You can start downloading from the operator’s server manually by clicking ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png). Click ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_preview.png) in order to preview the PDF invoice.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EIMDesktop.png)](../../../../Resources/Images/TrainingMaterial/EIMDesktop.png)
