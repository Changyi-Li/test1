### Day-to-day handling

#### Activate customers for factoring
When new customers are registered, the factoring option is automatically activated, but existing customers need to be manually updated. This can be done for individual customers in the Customer register procedure, or for multiple customers simultaneously via the Customer list procedure.
> For the factoring integration to work properly, the correct corporate ID number must be entered in the Customer register.
Customer register
To manually activate factoring for a customer in the Customer register procedure:
-   
Go to the Settings tab and use the Other invoice settings button.
-   
Check the Factoring box.
-    
Choose a Distribution method – either E-mail or Letter. Please note! If you have previously configured that the customer should receive e-invoices, you do not have to specify a distribution method as the invoice will automatically be sent as an e-invoice in this case.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/FedeltaFactoring_CustomerReg.png)](../../../../Resources/Images/TrainingMaterial/FedeltaFactoring_CustomerReg.png)
-    
If you have selected E-mail as the distribution method, it is mandatory to enter an invoice recipient with a correct e-mail address in the Communication – Delivery address box under the Contact information tab.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/FedeltaFactoring_CustomerReg2.png)](../../../../Resources/Images/TrainingMaterial/FedeltaFactoring_CustomerReg2.png)
-   
Also make sure you have updated contact information (name, e-mail and/or phone number) registered for the customer in the References box. This is important in order for Fedelta to access your customers contact information if they should need to get in touch.
> You can adjust if factoring should be applied per quote, customer order, customer agreement, and invoice in the different procedures. If you have activated factoring for the customer in the Customer register procedure, this will be activated by default.
Customer list
To activate factoring for multiple customer at the same in the Customer list procedure:
-   
Choose the Standard list type and the Miscellaneous presentation.
-   
Make the list possible to update by activating the icon Updateable ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_list.png) on the toolbar.
-   
Check the Factoring box for the customers you wish to activate.
-   
Choose a Distribution method – either E-mail or Letter. Please note! If you have previously configured that the customer should receive e-invoices, you do not have to specify a distribution method as the invoice will automatically be sent as an e-invoice in this case.
-   
You can use the Find & replace function ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) in the function menu to update multiple fields at a time.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/FedeltaFactoring_CustomerList.png)](../../../../Resources/Images/TrainingMaterial/FedeltaFactoring_CustomerList.png)

#### Invoicing and export to Fedelta
By using the factoring integration you do not have to distribute the invoice to the customer. Instead, Fedelta makes an invoice purchase and they will in their turn distribute the invoice to the customer via their systems. Invoicing is made using the regular procedures in Monitor ERP and the invoice is then exported to Fedelta automatically in connection with approving the invoice in the Print invoice procedure. The difference from file based factoring export is that you with the help of the integration with Fedelta can invoice continuously, that is, you do not have to create a “total” file export of invoices at the end of the day.
Review/Approve invoice
In the Review/Approve invoice procedure, there are two setting that are good to know. Under the Selection tab you find the following printout settings: Factoring export and Approve without Print/Send. The Factoring export checkbox detemines if factoring export should be activated for the customers which are invoices via factoring. Mark the Approve without Print/Send checkbox if you want to avoid that the invoice is also printed or sent via e-mail directly to the customer in the Print invoice procedure (distribution of invoices to the customer is handled be Fedelta).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/FedeltaFactoring_ApproveInvoice2.png)](../../../../Resources/Images/TrainingMaterial/FedeltaFactoring_ApproveInvoice2.png)
When you have loaded the list, you can use the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to see if each of the invoices will be sent via factoring or not. When customers that will receive e-invoice are concerned, you will also see info telling you if the e-invoice is distributed via Fedelta. This is shown in the E-invoice column. This information is also displayed in the Print invoice procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/FedeltaFactoring_ApproveInvoice.png)](../../../../Resources/Images/TrainingMaterial/FedeltaFactoring_ApproveInvoice.png)
After the invoices have been approved a question will appear asking if a printout should be made. If you choose to do a printout you will be linked to printing/e-mailing invoices in the Print invoice procedure.
Print invoice
The actual factoring export takes place from the Print invoice procedure. The export is conducted in connection with approving using the button on the function menu. If you did not get here by using links in the Review/Approve invoice procedure, you will first have to select Print/Send ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_mail_and_print.png) on the toolbar before you can approve.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/FedeltaFactoring_PrintInvoice.png)](../../../../Resources/Images/TrainingMaterial/FedeltaFactoring_PrintInvoice.png)
After having approved, a dialog is shown confirming that the invoices have been exported to Fedelta. If a problem should occur during the export (for example, if a valid corporate ID number would be missing for the customer), you will also get information about this as well as which invoice is concerned. You will then have to correct the problem and redo the export for that invoice.
> The invoices which have been sold appear in Fedelta’s client portal a short while after the invoices were uploaded. Read more under Client portal below.
Update accounts receivable
In the Accounts receivable procedure, you can see if an invoice has been exported to factoring or not. If the Factoring checkbox is activated, it means that the invoice has been included/sent in a factoring export.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/FedeltaFactoring_UpdateAR.png)](../../../../Resources/Images/TrainingMaterial/FedeltaFactoring_UpdateAR.png)
> You can also select by invoices you send via factoring in the following procedures: Accounts receivable list, Payment reminder basis, Print statement – Sales, and Interest charge basis. Under the Selection tab you find the Factoring field where you can choose Yes to only show the invoices which are sent via factoring.

#### Import of transactions from Fedelta
Monitor ERP automatically loads the transactions which affect the clearing account from Fedelta.
The following transaction types are managed:
- Payment invoice (these are automatically checked and recorded as paid in the accounts receivable)
- Recourse – the customer didn’t pay and the invoice is sold back to the company (only an accounting entry, it’s registered as “other payment”)
- Payment recourse – the customer paid after the invoice was repurchased (only an accounting entry, it’s registered as “other payment”)
- Invoice purchasing credit invoice (these are automatically checked and recorded as paid in the accounts receivable)
- Invoice write-off – concluded that the customer isn’t going to pay (only an accounting entry, it’s registered as “other payment”)
- Fee (only an accounting entry, it’s registered as “other payment”)
- Invoice service – information post that invoice purchase didn’t go through and that the invoice has been added to invoice service (this can happen e.g. If your credit limit with Fedelta has been exceeded or if a customer is insolvent.)
- Payment invoice service (these are automatically checked and recorded as paid in the accounts receivable)
> The invoice purchases are normally imported from Fedelta the same day as you do the invoicing.
Manage bank transactions
The transactions are handled via the Manage factoring transactions tab in the Manage bank transactions procedure.
By clicking the Load transactions button ![](https://help.monitorerp.cn/CN-MONITOR_G5/G5_Accounting_SV/Content/Resources/Images/button_import.png), the transactions are imported to the procedure according to the settings configures and the selected period. The transaction that are being imported have automatically been loaded by Monitor ERP from Fedelta via en scheduler which is run every 4 hours.
> If you want to load the latest transactions straight away (without awaiting the scheduler), it is possible to load them manually via the button called Trigger manual loading from Fedelta ![](https://help.monitorerp.cn/CN-MONITOR_G5/G5_Accounting_SV/Content/Resources/Images/button_download.png) found on the function menu.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/FedeltaFactoring_ManageFactoringTransactions.png)](../../../../Resources/Images/TrainingMaterial/FedeltaFactoring_ManageFactoringTransactions.png)
Invoice purchase and Payment invoice service records are automatically matched with the accounts receivable. Other transaction types are managed and posted automatically using standard accounts. When a payment invoice is posted, Fedelta will charge a fee. As this is subject to VAT, input VAT is posted automatically on the cost.
Fedelta charges different types of fees. These are imported as separate records and can relate to general fees at company level, but also fees that are debited per invoice, e.g., payment invoices. These fees are posted automatically and as they are subjected to VAT, the input VAT is posted automatically on this cost.
> [Here](PostingExamples.htm) you find posting examples.
Invoice service records are solely informational and cannot be matched or recorded. The records let you know that an invoice that has been sent for invoice purchase has not been approved by Fedelta and has therefore been moved over to invoice service. This can happen when a limit is exceeded for example. In the backstage of the Accounts receivable list, you can add the selection row and the Factoring service column which shows whether an invoice has been sent to invoice service.
Payment invoice service records are imported when the customer has paid the invoice. These are automatically checked against the accounts receivable. If the customer doesn’t pay the full amount, the invoice is matched but will be registered as a partial payment of the invoice in the accounts receivable. The procedure also manages small rounding differences, meaning that if the paid amount for the service invoice varies slightly from the invoice amount by up to 20 cents, it will be matched automatically and the difference will be posted as rounding.
By using the checkbox in the Exclude column, you can except a record from being recorded. This can be useful if you e.g. intend to record the payment manually (not using this procedure), or if the payment has already been recorded.
When you save in the procedure, all records that are green will be confirmed and recorded. The saved records are recorded via the regular payment journal for the voicher number series which you have entered in the Settings box. Any remaining records will stay there until the next time you load data to the procedure.
> Ensure that a Specification is entered in the chart of accounts on your clearing account and your standard accounts relating to factoring. This way, the system can specify which invoice each transaction corresponds to in the general ledger.

#### Client portal
Fedelta has a web-based client portal where you can get an overview and monitor the invoices handled via factoring. In connection with the onboarding, the credentials for login to this portal should have been sent via e-mail to the contact for Fedelta at your company. You can also access the client portal by using the Fedelta client portal button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_url.png) found in the Settings for export/import procedure.
