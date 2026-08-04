### FAQ – Customer and supplier invoices

#### Customer invoices
How do I create a credit invoice (customer invoice)?
Credit invoices are created in the Register invoices directly procedure.
1.     
Select one of the following two options to create a credit invoice:
1.   
Open the invoice you wish to credit and then choose the Credit invoice option under the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the toolbar of the procedure.
2.    
For a new invoice you mark the Credit checkbox and in the field Crediting of invoice number (which will then become available) you select the debit invoice to credit.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/InvoicingAccountsReceivable2.png)](../../../../Resources/Images/FAQ_Snippet_Images/InvoicingAccountsReceivable2.png)
> If, via a system setting, you have selected a default payment term for credit invoices, the payment term will automatically be changed.
2.      
In the dialog box that opens, you can choose or select the order number* the credit invoice will have. With Include you select which rows to credit. If no other settings are configured, the credit will be created for the full invoice row. If you want to create a price credit, select Price crediting on the row and enter New price. During price crediting, the quantity is not affected. If the invoice row has a setup price, you can also choose for this to be credited in conjunction with the price crediting.
> Please note! You should enter the new price in the field called New price, not the amount which you wish to credit. For example, if the price each on a row should be changed from 350 to 300, you should enter 300, not -50. During price crediting a minus row with the initial price will automatically be created, and also a new row with the new price. This means that the credit amount on the invoice will be the difference between the original price and the new price.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/Credit_invoice_window.png)](../../../../Resources/Images/FAQ_Snippet_Images/Credit_invoice_window.png)
> * It is convenient to use the same order number on the credit invoice as on the debit invoice, and just add the prefix "C". In the invoicing log and accounts receivable you can then search for the order number to find all debit and credit invoices that are invoiced with this order number.
3. When you click OK in the dialog, the credit invoice is saved and other information is entered for the credit invoice in the procedure.
> Please note that if you determine whether the credit affects the stock balance via the Affect balance checkbox. If you check the box Affect balance on an invoice row with row type 1, this will immediately affect the stock balance when registering the invoice basis. This setting can be entered for each part row under the Rows tab.
How do I cancel a customer invoice?
You cancel invoice bases in the Register invoices directly procedure and approved invoices in the Update accounts receivable procedure.
You can delete/cancel an invoice basis as long as it has not been approved (been given status 8). If a pro forma has been created for the invoice basis you must start by deleting the pro forma using the button Delete pro forma invoice ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png) in the Miscellaneous box, before you can delete/cancel the invoice basis.
1. Select an order number and load the invoice basis.
2. Click Delete ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png) (Ctrl + F6) in toolbar of the procedure.
3.    
When you click the button you get two options regarding deletion:
1. Cancel invoice basis without affect on balance – If it is a delivery reported customer order row which is the basis to the invoice basis, then the delivery will not be undone. This option is not available if the invoice basis comes from an invoicing plan on a customer order.
2. Cancel and undo the delivery reporting – The delivery reporting is also undone.
If an invoice basis has been approved (when an invoice is created), but the invoice is unpaid, you cancel the invoice in the procedure Update accounts receivable. If an invoice already has a registered incoming payment, it is not possible to delete/cancel until the payment has been deleted. This is done in the Incoming payments procedure.
> Deleted invoice bases are not shown in the system, but can be included in the list in the procedure Invoice basis – Sales by including status 0 in the selection.
> If you in the system setting called Check open accounting period during order reporting have selected the Block alternative, the delivery will not be possible to undo when deleting/canceling the invoice basis in cases where the date belongs to a closed accounting period.
How do I get started with Interest invoicing?
There are a few settings you need to configure to get up and running:

#### System settings
There are a number of different system settings regarding interest invoicing which you need to review. You find these settings under the heading [Interest invoice](../../GeneralRegisters/BasicSettings/SystemSettings/bInterestInvoice.htm), under the Sales tab in the System settings procedure. Some of the settings have a default value. Please read the description of these system settings in the online help function for that procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/InterestInvoicingSystemSettings.png)
> The last system setting in that section is called Service part for interest invoices. It requires you to first create the following for controlling posting and VAT: Create a product group for interest (call it, e.g., "Interest") and select the sales account for penalty interest 8313 (in Sweden) for all customer groups. This is done under the Product group and Sales account tab in the Posting matrix procedure.Select VAT code 4 (VAT exempt) for the product group for all customer groups. This is done under the Exception per product group tab in the VAT settings procedure.Create a part of the Service type (call it, e.g., "Interest") and choose Unspecified as Service type. Assign the part the product group you created earlier. This is done in the Part register procedure.Finally, select this service part in the above mentioned system setting.

#### Customer register
For some of the above mentioned system settings it is possible to make exceptions per customer. You find these in the [Exceptions](../../Sales/Customers/CustomerRegister/bExceptions.htm) box, under the Settings tab in the Customer register procedure. If a setting here is empty (no alternative has been selected), it means the system setting applies. But if you enter/select a setting, this will override the corresponding system setting when interest invoicing to that customer in question.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/InterestInvoicingCustomerSettings.png)

#### Document settings
For interest invoices there is a document template called Interest invoice in the Document settings procedure. You need to review the settings of this document template. Read more about these settings in the [Settings](../../GeneralRegisters/DocumentManagement/DocumentSettings/bSettings.htm) topic.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/InterestInvoicingDocumentSettings.png)](../../../../Resources/Images/FAQ_Snippet_Images/InterestInvoicingDocumentSettings.png)
You can read more about [Interest invoicing](../../Using/InvoicingAccountsReceivable/InterestInvoicing.htm) here.
What is a cash receipt?
You use cash receipt when making sales where you receive cash payment (in actual cash or via card payment) in connection to when you approve and print the invoice, for example when selling in a store. Cash receipt can also be selected when you register customer orders.
The cash receipt will be paid automatically in the accounts receivable when approved. Posting of the cash receipt is recorded in the customer invoice journal. No incoming payment journal will be printed for this invoice type (even though it automatically becomes set as paid).
On invoices of the type cash receipt, no payment terms are shown.
Cash receipt has a separate document template and can also have a separate number series (optional).
What is an internal invoice?
Internal invoices are for internal use to handle sales of internal customer orders, for example when withdrawing goods for a trade fair, etc. Then you wish to register the withdrawal from stock and to get a delivery note for the withdrawal, but the invoice should only be recorded as internal sales and not to be sent to customer. Here you often use an internal customer number on the order (referring to the own company or sometimes departments in the company). You might also use it when dealing with internal invoicing between group companies.
Posting of the internal invoice is recorded in the customer invoice journal.
Internal invoice has a separate document template and can also have a separate invoice number series (optional).

#### Supplier invoices
How do I credit a supplier invoice linked to a purchase order?
To credit a supplier invoice of the order invoice type, you do the following:
If the crediting concerns credit of the quantity on the row:
1. Open the Register supplier invoice procedure and select Create new on the toolbar. If you have the EIM option, you instead select the invoice you want to register from the inbox.
2. Make sure that you select Credit as the Invoice type.
3. Enter the consecutive number of the debit invoice in the Consecutive number field under the Invoice type field. If the option EIM is activated in the system, then there is a button next to the field Consecutive number. You can use this to display the debit invoice to be credited.
4. A new window for crediting invoice is opened. There you will see the contents (order rows) from the debit invoice and you can mark the order rows that you want to credit. If a comprehensive invoice is concerned, these rows will be shown. An order row can also be partially credited by entering a quantity and choose if the crediting affects the balance.
5. Mark Create new invoice basis if the supplier will send a new invoice for the credited quantity.
6. Click OK to create a credit invoice. The order number on the credit invoice will be the same as the debit invoice, but with a sub-number.
7. Send the invoice for authorization or final record it.
8. Save.
If the crediting concerns credit of the price on the row:
1. Open the Register supplier invoice procedure and select Create new in the toolbar. If you have the EIM option, you instead select the invoice you want to register from the inbox.
2. Make sure that you select Credit as the Invoice type.
3. Enter the consecutive number of the debit invoice in the Consecutive number field under the Invoice type field. If the option EIM is activated in the system, then there is a button next to the field Consecutive number. You can use this to display the debit invoice to be credited.
4. A new window for crediting invoice is opened. There you will see the contents (order rows) from the debit invoice and you can mark the order rows that you want to credit. If a comprehensive invoice is concerned, these rows will be shown. Mark Price credit and enter Credited price or New price. Monitor ERP calculates the price which you have not entered.
5. Click OK to create a credit invoice. The order number on the credit invoice will be the same as the debit invoice, but with a sub-number. Now a row is created with original price to remove the debit invoice, and a row with the new price.
6. Send the invoice for authorization or final record it.
7. Save.
> By using this function it will be clearer which debit and credit invoices that belong to a specific purchase order. Purchase statistics for parts and cost in the Post-calculation (for subcontract) is affected by the crediting. There is support to better handle calculation of FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. when material is credited.
How do I credit an expense invoice (a supplier invoice not linked to a purchase order)?
To credit a supplier invoice of the expense type, you do the following:
1. Open the Register supplier invoice procedure and select Create new on the toolbar. If you have the EIM option, you instead select the invoice you want to register from the inbox.
2. Make sure that you select Credit as the Invoice type.
3. Enter the consecutive number of the debit invoice in the Consecutive number field under the Invoice type field. If the option EIM is activated in the system, then there is a button next to the field Consecutive number. You can use this to display the debit invoice to be credited.
4. Choose if the entire debit invoice should be credited or not. If you choose not to credit the entire invoice, you must manually enter the invoice amount and posting to be credited.
How do I cancel a supplier invoice?
1. Enter the consecutive number of the supplier invoice you want to delete and then click the Cancel button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/G5_UserGuide_SV/Content/Resources/Images/button_delete.png) on the toolbar.
2. In the window that appears called Comment for cancellation you must enter why the invoice is being canceled.
3. Then click OK in the Comment for cancellation window.
4. The status of the supplier invoice is then set to Canceled.
If the canceled invoice was only registered, no offset entry will be created. If it has a preliminary entry, a preliminary offset entry will be created. If it is final recorded, a final offset entry will be created.
If the canceled invoice has a preliminary entry and the preliminary entry date is outside the open accounting period, you will see a window where you can enter the date for when the cancellation should be recorded. The date that will be suggested is the first date in the first open period. If the canceled invoice is final recorded and the date is outside the open accounting period, you will see a corresponding window. When you cancel the invoice, the entries created for the invoice will be removed from the supplier invoice log.
If the canceled invoice has preliminary linked or linked order rows, the invoice bases will be released from the invoice and again made available for linking to a new invoice.
> Please note! It is not possible to cancel a supplier invoice which has a registered payment. In that case, you first have to cancel the payment in the Outgoing payments procedure.
I cannot see the invoice viewing window, what do I do?
Applicable to those of you that have the EIM option.
If you have closed the invoice viewing window in any of the Register/Authorize supplier invoice procedures, you can click the Show invoice image button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png) to open the window again.
If you have only minimized the invoice viewing window, you can open it by hovering your mouse over the Monitor icon in the task bar and click the invoice image window.
Sometimes if you have switched screens, or e.g., from two screens to a laptop, the computer may be displaying the invoice viewing window on a screen which is no longer connected. If this is the case, you can hover your mouse over the Monitor icon in the task bar, right-click, and select Maximize on the invoice image window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ/FAQ_InvoiceImage.png)](../../../../Resources/Images/FAQ/FAQ_InvoiceImage.png)
What is the difference between EIM and EIM Workflow?
The EIM (Electronic Invoice Management) option
The basic application of EIM provides system support for scanning and digital handling of the company's supplier invoices. The entire flow, from scanning, registration, authorization, final recording, and search is streamlined by using this function. The EIM option also makes it possible to activate a digital invoice flow. This means you can activate services for invoice interpretation and receiving of e-invoices.
Once the facility to receive e-invoices is activated, all suppliers will be able to start sending you e-invoices. Incoming e-invoices will automatically be registered by the system (all of the information at invoice header level is registered) If automatic registration can not take place, the invoice will be sent to the Register supplier invoice procedure to be checked or for further action. You can also allow incoming e-invoices from suppliers to be automatically sent for authorization. This takes place if there is an authorized signer selected for the supplier in the Supplier register procedure.
By sending the supplier invoices to the interpretation service, the data/information at invoice header level is interpreted, for example, supplier, invoice type (debit/credit), invoice number, invoice date, and amount. The information is then imported together with the invoice image into the For registration/verification inbox in the Register supplier invoice procedure. In the inbox, you verify the interpreted data and ensure that the correct values ​​have been found.
The EIM Workflow option
The EIM Workflow option is an addition to the EIM option. Providing the conditions are met, EIM Workflow will automatically match the invoices to purchase orders. All you need to do is carry out the final recording, or if you wish to optimize the work flow even more, you can have the system do an automatic final recording when a complete match is made. For it to be a complete match everything on the invoice must match the purchase order. Please note! There are settings where you can configure intervals regarding how exact a match must be in order to considered a complete match.
This option contains all the same functions as the EIM option but where the interpretation function must be activated in order to be able to match purchase orders. The invoice data is imported into EIM Workflow in Monitor ERP after the supplier invoice has been interpreted in CrossState. The verification of invoice information takes place in CrossState. The invoice is then automatically matched with the purchase order, both at header level and, as appropriate, row level. If EIM Workflow detects deviations that exceed what has been entered in the system settings, the invoice is sent for authorization. It is possible to set exceptions from the system settings for specific suppliers. In the event of a complete match – taking any exceptions and amount limits into account – the invoice can be directly forwarded for final recording.
If deviations are detected, EIM Workflow will primarily send the invoice to the signer code which is entered in the Supplier register, and secondarily to the reference stated on the purchase order. If none of these links exist, you must manually send the invoice for authorization via an authorization list in EIM Workflow. During the process, you can also change the authorization list by adding or removing signers or simply forwarding an invoice to another signer, directly from the inbox or from the invoice you have opened.
The invoices with no purchase order (that is, expense invoices) are automatically referred for a check/authorization.
Once the final signer has handled the invoice, it is forwarded for final recording. The adjustments made to the invoice during authorization in terms of price and posting are automatically captured during final recording, and just have to be approved in order for the invoice to be signed off for payment.
