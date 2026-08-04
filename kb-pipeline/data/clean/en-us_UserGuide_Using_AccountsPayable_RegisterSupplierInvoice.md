### Register supplier invoice
In this procedure you register and final record incoming supplier invoices.
> Depending on your internal authorization flow and also depending on if you are using the option Electronic invoice management (EIM), the work flow in this procedure might vary. This chapter describes application without EIM. See separate [documentation](../EIM/ElectronicInvoiceManagement.htm) for application when using EIM.
With a system setting you can also activate preliminary recording of supplier invoices. Then a posting will be made against preliminary accounts when the invoice is registered prior to the final recording. If you apply preliminary entry of supplier invoices at registration, you can choose if the VAT should be reported during preliminary entry or final recording. Preliminary entry is selected by default.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/AccountsPayablePreliminaryEntrySuppInvSystemSetting.png)
You can distinguish between two types of supplier invoices based on if there are corresponding purchase orders or not:
- Material invoices – These invoices have corresponding/related purchase orders.
- Expense invoices – These invoices do not have corresponding/related purchase orders.

#### Material invoices
One of the possible work flows when registering material invoices is to first select the purchase order number on the header row. The supplier in question will then become loaded and some of the information from the invoice header will also be loaded from the purchase order. Then add the rest of the invoice information. It is also possible manually enter a supplier without entering an order number.
The Order link tab
Under this tab you can link the supplier invoice to the right purchase order. If the order has already been entered, it means that the order/order rows are selected by default. In the Order rows box you see the row information you can link to the invoice. You can adjust prices etc. if there are nonconformities. You can also add more rows which have been added on the invoice (e.g., freight costs). If the invoice should not be final recorded (e.g., if it should be sent for authorization or awaits arrival of goods) you save the invoice. The selected order rows will then be preliminary linked to the invoice.
If the invoice is fully processed and it corresponds to the purchase order then you should click the Final record button at the bottom of the tab. The invoice is now ready for payment. The posting of the invoice is printed in a supplier invoice journal. When using direct integration the posting is automatically entered in the accounting.

#### Expense invoices
When there is no purchase order you start by selecting the supplier on the main row and enter the invoice information. You post the invoice in the Posting box in the lower part of the procedure. Here you can add the invoice’s purchase accounts. It is also possible to enter a default purchase account in the supplier register. This will then be used in cases where there is no purchase order.
If the invoice should not be final recorded directly, but only registered, then you finish by saving in the procedure.
In connection with final recording the invoice you load the invoice and check the Final entry checkbox in the Posting box. Posting will automatically be done on accounts for e.g. VAT and accounts payable. Complement with purchase accounts or confirm the postings which were created during the registration of the invoice. The invoice is now ready for payment. Posting of invoice is printed in the supplier invoice journal. When using direct integration the posting is automatically entered in the accounting.
Use the tab Recent invoices to see how invoices from the same supplier have previously been recorded. It is also possible to copy the posting from there and past it in the current invoice.

#### Cancel invoice
You can cancel a supplier invoice e.g. if it is registered by mistake or registered in an incorrect way. It is possible to cancel an invoice as long as there are no payment entries for it. Depending on the status of the invoice an automatic offset of the invoice is made which can be printed in the Print supplier invoice journal procedure.
If the invoice is linked to a purchase order, this link will be deleted when canceling. The purchase order can then be linked to another invoice. An invoice that is canceled is not deleted. Instead, it is given status Canceled, and by default it is not visible in all the different reports, and it cannot be paid or modified. It is not possible to undo a cancellation.
How to cancel a supplier invoice
1. Enter the consecutive number of the supplier invoice you want to delete and then click the Cancel button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/G5_UserGuide_SV/Content/Resources/Images/button_delete.png) on the toolbar.
2. In the window that appears called Comment for cancellation you must enter why the invoice is being canceled.
3. Then click OK in the Comment for cancellation window.
4. The status of the supplier invoice is then set to Canceled.
If the canceled invoice was only registered, no offset entry will be created. If it has a preliminary entry, a preliminary offset entry will be created. If it is final recorded, a final offset entry will be created.
If the canceled invoice has a preliminary entry and the preliminary entry date is outside the open accounting period, you will see a window where you can enter the date for when the cancellation should be recorded. The date that will be suggested is the first date in the first open period. If the canceled invoice is final recorded and the date is outside the open accounting period, you will see a corresponding window. When you cancel the invoice, the entries created for the invoice will be removed from the supplier invoice log.
If the canceled invoice has preliminary linked or linked order rows, the invoice bases will be released from the invoice and again made available for linking to a new invoice.
> Please note! It is not possible to cancel a supplier invoice which has a registered payment. In that case, you first have to cancel the payment in the Outgoing payments procedure.

#### Credit order invoice
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

#### Credit an expense invoice
To credit a supplier invoice of the expense type, you do the following:
1. Open the Register supplier invoice procedure and select Create new on the toolbar. If you have the EIM option, you instead select the invoice you want to register from the inbox.
2. Make sure that you select Credit as the Invoice type.
3. Enter the consecutive number of the debit invoice in the Consecutive number field under the Invoice type field. If the option EIM is activated in the system, then there is a button next to the field Consecutive number. You can use this to display the debit invoice to be credited.
4. Choose if the entire debit invoice should be credited or not. If you choose not to credit the entire invoice, you must manually enter the invoice amount and posting to be credited.
