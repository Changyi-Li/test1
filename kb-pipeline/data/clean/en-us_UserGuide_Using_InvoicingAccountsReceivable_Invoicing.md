### Invoicing

#### Register invoice directly
You use this procedure when you want to invoice customers directly without having an underlying customer order. You can create invoice bases for debit invoices. The invoice bases can be approved and printed in this procedure. An alternative is to approve and print in the Review/Approve invoice procedure. The procedure is also used to credit invoices in cases when you need to credit customers. It is also possible to modify existing invoice basis and delete invoice basis.
The row types on an invoice are the same as on customer orders. You find a description of row types in the topic [The Rows tab](../../../Sales/Orders/RegisterCustomerOrder/tRows.htm) in the online help function for the Register customer order procedure.
Create debit invoice:
1. Select which customer to invoice and select/enter the other information.
2. Add part rows and enter information on the rows.
3. When you save in the procedure a invoice basis is created.
4. After this you can approve the invoice directly by clicking the button Approve invoice ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_approve_document.png) on toolbar. You will then be asked if you want to print the invoice or do it at a later time. You can also skip the step of approving the invoice in this procedure and instead choose to approve the invoice basis and print the invoice in the Review/Approve invoice procedure.
Create credit invoice:
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
> Please note! When a credit invoice is loaded in the procedure you see the procedure name and invoice number in red text in the title bar.
Modify existing invoice basis:
1. Select an order number and load the invoice basis.
2. Modify the information on the invoice basis.
3. Save in the procedure.
> It is also possible to modify invoice bases in the Review/Approve invoice procedure. Use the Edit invoice ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit.png) button to open an editing window for the invoice basis chosen.
Cancel invoice:
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

#### Invoice basis – Sales
In this procedure you see what has been delivered but not invoiced. You can also value at standard price in stock valuation purposes. The procedure can also show deleted/canceled invoice basis.

#### Review/Approve invoice
After a customer order has been delivery reported in the Report delivery procedure, there are invoice bases ready to be approved for invoicing. Invoicing is handled in this procedure. Here you review and approve the invoice bases and print the invoices. Before an invoice basis is approved it is possible to edit certain information on the basis. You make changes by clicking the Edit invoice ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit.png) button in the function menu. In connection with approving an invoice basis, the invoice is created and it gets an invoice number. A record is generated in the accounts receivable and posting is generated in the customer invoice journal.
You review and approve interest invoices, internal invoices, and cash receipts, in this procedure. Invoice bases for interest invoices are created via the Interest charge basis procedure.
1. Mark Include in the Result box for the invoice bases which should be approved.
2. Click the button Approve invoice ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_approve_document.png) on the toolbar.
3. After approval a question appears asking if you wish to print the invoices. You will then automatically be linked to the procedure Print invoice with the approved invoices loaded. You can also choose to only approve the invoices to print them at a later time in that procedure.

#### Print invoice
In this procedure you print the invoices approved in the Review/Approve invoice procedure. You can choose to automatically open Print invoice after the invoices have been approved.
Here you can also print old already printed invoices by checking the setting called Reprint.

#### Print customer invoice journal
In this procedure you print and approve the customer invoice journal. It contains postings of approved invoices. It is also possible to approve the journal without printing it. The accounting becomes updated when you approve the journal. Here you can also create a reprint of a customer invoice journal.
When using direct integration of customer invoices to the accounting, this step is not included in the work flow.
> Monitor tip! Use Monitor-to-Monitor to send invoices as PDF files and an XML file via e-mail. The recipient of the XML file can then use it to register it in their Monitor ERP system. The file can be imported to Monitor ERP directly from the e-mail message. Use the Invoicing log to view sales statistics per customer, part, period, etc. Use Review/Approve pro forma invoice to print a pro forma invoice before the actual invoicing. A pro forma invoice must accompany the goods for customs purposes during international deliveries. Use Update accounts receivable to enter an unpaid record directly into the accounts receivable, without invoicing or in order to change the due date/payment terms. Here you can also cancel an invoice, as long as no incoming payment has been registered for it. If there is an incoming payment for the invoice, you first have to cancel that incoming payment in the Incoming payments procedure.
