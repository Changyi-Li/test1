### Outgoing payments
In this box you register outgoing payments of invoices with manual payment methods . The registration is performed by manually entering which invoices have been paid. You can also move invoices (with manual payment methods) to this tab from the List tab. At the bottom of the box, you see totals of the amounts on the rows.

#### Row
In this column you will see a fixed row number that is set automatically. It can be used when sorting the list, but it is not possible to change.

#### Consecutive number
Here you select or enter the consecutive number that you wish to register as paid or partially paid. You can see all invoices that have a remaining amount greater than or less than zero. If you enter an existing consecutive number that is already paid in full, you will see an error message in the validation window saying that the invoice is already fully paid. An error message will also appear if you try to enter the same consecutive number on several rows. Leave the field empty in order to register an on account payment.

#### Supplier
Here you see the supplier number for the invoice in question. For a regular outgoing payment where a consecutive number has been entered, the supplier number cannot be changed. If you on the other hand register an on account payment (that is, you leave the Consecutive number column empty) then you must enter a supplier number. It is for that supplier that the new on account record is saved in the accounts payable. The text "On account On account is a partial payment (advance payment) which you have made to a supplier or received from a customer." will then be displayed in red in the Consecutive numberfield to clarify that the payment will be registered on account for the supplier.

#### Payment date
By default, you will here see the date entered as payment date for the batch in the Settings box. The payment date refers to the date when the bank states the amount as paid. It is possible to change the date in the field, that is, you can have different payment dates for payments belonging to the same batch. This means that payments in the same batch can be recorded in different vouchers. An error message appears if you enter a payment date that is earlier than the invoice date. A check is also be made to make sure that the entered date belongs to an open accounting period. If the payment date belongs to a closed or locked period, an error message appears. However, if the date "only" falls outside of the current period, you see a warning but it is possible to save.

#### Due date
Here you can see the due date of the invoice. For on account payments, the due date is set to the same date as the payment date, which is then saved in the accounts payable entry.

#### Paid amount
Here you enter the amount that you have paid. This column shows the invoice's remaining amount by default. You can change the amount here if you have entered a consecutive number or a supplier. It is possible to enter an amount that is greater than or less than the remaining amount. For "On account payments" it is possible to enter a negative amount.
> In the Amount field you can enter the paid amount in the company currency even though the invoice is in foreign currency.
If the paid amount that you enter is less than the remaining amount, the payment will be regarded as a partial payment, unless you select a write-off code in the Write-off field. In that case, the remaining amount of the invoice is set to zero and the invoice is regarded as fully paid. The paid amount is automatically converted to the company currency according to the exchange rate. It is then shown in the Amount field.
If you enter a paid amount that is greater than the remaining amount, a dialog box for overpayment will open. There you can select how the excess amount should be handled: if you wish to register it as a balance in our favor against the supplier (on account) or if you wish to write it off as a write-off.
Write-off
If you select Write-off, the system will keep the entered amount. You must then enter a write-off code for the excess amount. This is done in order for the invoice to be managed as fully paid with a remaining amount of zero.
On account
If you click the On account button, the system will change the paid amount to correspond to the remaining amount. A new row for an on account payment will be added below, with the same supplier number and the excess amount filled in.
For an on account payment that does not refer to an overpayment, the amount in the Paid amount field is zero by default. The invoice for the amount is loaded from the supplier. You are not allowed to enter negative amounts for on account payments either.
Credit amounts and on account amounts are displayed in red.

#### Exchange rate
If the invoice is issued in another currency than the company currency, you can here enter the exchange rate for the payment. The exchange rate determines what the paid amount will be in the company currency. The exchange rate also determines the rate difference that will be recorded via the standard account for exchange profit/loss, the exception account registered for the supplier primarily. You can use Find & replace (Ctrl + H) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) to change exchange rate for all records in the column.
The system setting Default exchange rate for outgoing payments determines which exchange rate that will be suggested.
If this system setting is set to Current exchange rate and you have several invoices in a row in the same currency, the exchange rate of the first invoice row will be suggested for the following invoice rows. If you choose to enter the paid amount in the company currency instead of in the currency of the invoice, the exchange rate used will be based on that. It is also possible to enter exchange rates for on account payments.

#### Write-off
This column is available if the paid amount registered for the invoice is either greater than or less than the remaining amount. If you enter a paid amount that is less than the amount on the invoice and you do not choose a write-off code, the payment will be regarded as a partial payment. If you instead choose a write-off code, the remaining amount will be removed from the invoice and posted on the account linked to the selected write-off code. Write-off codes are handled in the Bank settings procedure.
The Write-off field is not available on rows for on account payments.

#### Rate difference
If the invoice is registered in another currency, you can here see the rate difference in the company currency. This difference will be automatically recorded against the standard accounts for exchange rate differences. The rate difference is the calculated difference between the original rate and the rate entered in the Exchange rate field. The rate difference is not used for on account payments.

#### New remaining amount
Here you can see the new remaining amount in the invoice’s currency after the payment. A new remaining amount is only displayed if the invoice has not been fully paid, that is, if it is a partial payment and no write-off code has been entered.
For on account payments, the new remaining amount is always the same as the paid amount. The new remaining amount is displayed in red if it is a credit invoice.

#### Bank charge
Here you can enter a bank charge, if any. By default, no bank charge is displayed.
If the setting Record bank charge separately is activated for the payment method in the Bank settings procedure, the bank charge is always entered in the company currency. Otherwise, the bank charge is entered in the currency of the invoice.
Depending on whether this setting is activated or not for the payment method in question, it also affects how the bank charge is posted. If the setting is activated, the bank charge will be charged to the account entered for bank charge for the payment method. If it is not activated, the bank charge will be taken from the same account as the payment. The actual bank charge cost is recorded against the standard account for bank charge, defined in the standard accounts, unless an exception account has been entered for the supplier.
Bank charge can also be entered for on account payments.
More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Payment method
The payment method shown here by default is the same as entered in the Settings box, but it can be changed. However, postings might be affected if the payment method is changed.
> If you want to send an on account outgoing payment via file, you can here change to an electronic payment method for the record.

#### Amount
Here you can see the paid amount converted into the company currency, based on the entered exchange rate. The field can be changed, since it is possible to select whether the paid amount should be entered in the invoice's currency or in the company currency.
If the invoice is registered in a currency that differs from the company currency and you change the amount, the invoice will be regarded as fully paid. The paid amount on the row is then set to the remaining amount and the exchange rate will be calculated by dividing Amount by Paid amount. This means that the normal rules for exchange rate no longer apply.

#### Remaining amount
Here you can see the initial remaining amount, that is, the remaining amount of the invoice before any outgoing payments was registered.

#### Initial rate
In this column you can see the exchange rate that was applied when the invoice was registered, that is, the rate in the accounts payable.

#### Comment
Comments regarding the outgoing payment. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Cash discount %
Cash discount % is shown in red font if the payment was made later than the cash discount date.

#### Cash discount date
Cash discount date is shown in red font if the payment was made later than the cash discount date.
