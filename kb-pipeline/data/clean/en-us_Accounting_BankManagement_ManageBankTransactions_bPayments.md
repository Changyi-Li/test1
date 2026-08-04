### Payments

#### Row
In this column you will see a fixed row number that is set automatically. It can be used when sorting the list.

#### Payment type
Here you decide which type of payment is concerned. The following payment types are available: Customer invoice, Supplier invoice, and Other payment.

#### Invoice number/Consecutive number
In this field you select or enter the invoice number/consecutive number that you wish to register as paid or partially paid. You can see all invoices/consecutive numbers that have a remaining amount greater than or less than zero. If you enter an invoice number/consecutive number that exists but is already fully paid, you will see an error message in the validation window saying that the invoice is already fully paid. An error message will also appear if you try to enter the same number/consecutive number on several rows.

#### Customer/Supplier/Account
Here you see the customer number/supplier for the invoice/consecutive number in question. If the payment concerns "Other payment", you should instead enter the account the payment should be recorded on. If on account is registered by leaving the field Invoice number/Consecutive number empty, then you should enter which customer/supplier the on account payment should be registered for.

#### Dimensions (CC and CU and Project)
Here you can enter dimension codes for Other payments. Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. can be entered for other payments and only if the entered account allows posting on dimension codes.

#### Specification
Here you can enter a specifications for the current posting row. In order to see a specification here, it is required that you have marked Specification for the affected accounts in the Chart of accounts procedure.

#### Payment date
By default, you will here see the date entered as Payment date for the batch in the Settings box. The payment date refers to the date when the bank states the amount as paid. It is possible to change the date in the field, that is, you can have different payment dates for payments belonging to the same batch. This means that payments in the same batch can be recorded in different vouchers. An error message will appear if you enter a payment date that is earlier than the invoice date. A check is also be made to make sure that the entered date belongs to an open accounting period. If the payment date belongs to a closed or locked period, an error message will appear. However, if the date "only" falls outside the current period, you will see a warning but it is still possible to save.

#### Due date
Here you can see the due date of the invoice/consecutive number. For "other payments", the field is empty.

#### Paid amount
The following only applies for the payment types Customer invoice and Supplier invoice:
The paid amount is entered in the currency of the payment (foreign currency). The remaining amount of the payment is entered by default, but it can be changed. It is possible to enter an amount that is greater than or less than the remaining amount. For Other payments and On account On account is a partial payment (advance payment) which you have made to a supplier or received from a customer. payments it is possible to enter a negative amount.
If the paid amount that you enter is less than the remaining amount, the payment will by default be regarded as a partial payment, unless you select a write-off code in the Write-off field. In that case, the remaining amount of the invoice is set to zero and the invoice is regarded as fully paid. The paid amount is automatically converted to the company currency according to the exchange rate. It is then shown in the Amount field.
If you enter a paid amount that is greater than the remaining amount, you will see a window for overpayment. There you select how the excess amount should be handled: if you wish to register it as a balance in the customer’s favor against us (on account) or if you wish to write it off as a write-off. If you click the Write-off button, the system will keep the entered amount, and you must then select a write-off code for the remaining amount. This way the invoice will be handled as fully paid with zero as remaining amount. If you instead click the On account button, the system will change the paid amount to correspond to the remaining amount. At the same time a new row for on account payment will be added below, with the same customer number and the excess amount filled in.
For an on account payment that does not refer to an overpayment, the amount in the Paid amount field is 0,00 by default. The currency of the amount is loaded from the currency of the customer.
Credit amounts and on account amounts are displayed in red.
The following applies regarding "Other payment":
Payment is entered with a positive or negative amount. A positive amount is handled as an incoming payment, and a negative amount is handled as an outgoing payment.
In the field, you can enter the paid amount in the company currency, even though the invoice was issued in a foreign currency.

#### C (Cash receipt)
Here you can show and print a cash receipt for cash report payments.

#### V (Voucher)
Here you can show the voucher for the cash report payment.

#### Exchange rate
If the payment is in another currency than the company currency, you can here enter the exchange rate for the payment. The exchange rate determines what the paid amount will be in the company currency and also the rate difference that will be recorded (via the standard account for exchange profit/loss, the exception account registered for the customer primarily). You can use Find & replace (Ctrl + H) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) to change exchange rate for all records in the column.
The system settings called Default exchange rate for incoming payments and Default exchange rate for outgoing payments determine which exchange rate is suggested for payment of customer/supplier invoices. For other payments, the system will always suggest exchange rate according to the rate of the payment day.
If this system setting is set to Current exchange rate and you have several invoices in a row in the same currency, the exchange rate of the first invoice row will be suggested for the following invoice rows. If you choose to enter the paid amount in the company currency instead of in the currency of the invoice, the exchange rate used will be based on that. It is also possible to enter exchange rates for on account payments.

#### Write-off
This write-off column is available if the paid amount registered on the payment is either greater than or less than, the remaining amount. If you enter a paid amount that is less than the amount on the payment and you do not choose a write-off code, the payment will be regarded as a partial payment. If you instead choose a write-off code, the remaining amount will be removed from the payment and posted on the account linked to the selected write-off code. Write-off codes must first be registered in the Bank settings procedure.
The Write-off column is not available on rows with "other payments" and on account payments.

#### Rate difference
If the payment is registered in another currency, you can here see the rate difference in the company currency. This difference will be automatically recorded against the standard accounts for exchange rate differences. The rate difference is the calculated difference between the original rate and the rate entered in the Exchange rate field. The rate difference is not used for the other payments and the on account payments.

#### New remaining amount
Here you can see the new remaining amount in the payment’s currency after the incoming payment or outgoing payment. A new remaining amount is only displayed if the payment has not been fully paid, that is, if it is a partial payment and no write-off code has been entered.
For on account payments, the new remaining amount is always the same as the paid amount. The new remaining amount is displayed in red if it is a credit invoice. Please note! New remaining amount is not used for "other payments".

#### Documents
With the Documents button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png) you can save a document to a payment. To be able to do this, you must first enter an inbox for these documents in the Scan documents procedure. In the document viewing window you can also drag and drop to add a document. The supported file formats are PDF and TIFF. When you register a payment with a document, the document is saved with the voucher in the accounting. A separate voucher is created automatically for the payments with linked documents. The documents can be viewed in several different lists by using the Show document button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png).
In the section Navigation in the procedure you select the inbox you wish to work with. If there are multiple scanned documents in the inbox (you see the number of documents displayed next to the inbox), use the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_previous.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_next.png) at the top of the document viewing window.
Document viewer window
Here you can navigate between the documents in the selected inbox. If a document is in the inbox but shouldn’t be, that is, it is not a document you should register, you can delete the document using the Delete document button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png).

#### The toolbar menu
On the toolbar menu you find the following buttons:
- Keep on top ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/KeepOnTop.png) – With this button you decide if this window should remain the top window.
- Remember size and position of window ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SaveWindowImage.png) – With this button you decide if you want the window size and position to be saved to next time you open the window.

#### The Function menu
The following buttons are available in the function menu for the documet image:
- Marking tool ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/buttonSelectionTool.png) – With this button you mark/select a section on the document..
- Hand tool ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/buttonMove.png) – This is used to move the document image.
- Print ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save_and_print.png) – This is used to print the document.
- Previous/Next page ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/buttonPageUp.png)![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/buttonPageDown.png) – If the document consists of multiple pages, you can use these buttons to browse.
- Find text ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/buttonSearchText.png) – This is used to search for a certain text in the document.
- Rotate ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/buttonRotateImage.png) – This is used to rotate the image.
- Add document ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add.png) – This is used to add documents/enclosures.
- Delete document ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png) – This is used to delete documents/enclosures.
- Replace document ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) – This is used to replace an existing document with another document.
You can see the page number below the document image. There you also find button you can use to adapt height and width, and zoom in/out.
More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns.

#### Initial rate
Here you can see the exchange rate that was applied when the invoice was issued, that is, the rate in the accounts receivable ledger.

#### Invoice date
Here you can see the registration date of the invoice.

#### Invoice type
Shows the type of invoice that the incoming payment refers to.

#### Partial invoice type
Here you see the partial invoice type if the payment concerns an invoicing plan.

#### Comment
Here you can enter a comment regarding the incoming payment. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Customer name/Supplier name
Here you see the name of the customer/supplier.

#### Amount
Here you can see the paid amount converted into the company currency, based on the entered exchange rate. The field can be modified, since it is possible to select whether the paid amount should be entered in the invoice's currency or the company currency.
If the invoice is registered in a currency that differs from the company currency and you change the amount, the invoice will be regarded as fully paid. The paid amount on the row is then set to the remaining amount and the exchange rate will be calculated by dividing Amount by Paid amount. This means that the normal rules for exchange rate no longer apply.

#### Remaining amount
Here you can see the initial remaining amount, that is, the remaining amount of the invoice before any incoming payment was registered.

#### Cash discount date
If cash discount is used, then you see the cash discount date here. Cash discount date and Cash discount % are shown in red font if the payment was made later than the cash discount date.

#### Check number
If a check payment is concerned, you will here see the check number.
