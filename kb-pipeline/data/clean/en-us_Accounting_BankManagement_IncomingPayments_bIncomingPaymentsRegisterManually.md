### Incoming payments
In this box you can manually register the invoices that have been paid, or you can load invoices from the List tab. At the bottom of the box, you see totals of the amounts on the rows.

#### Show document
Using this button you can view the invoice to which the invoice refers. The invoice is marked with the text "Reprint".
Using the Show document button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png), you open the document in a separate window. There you can also reprint the document or attach it to an e-mail message.

#### Row
In this column you will see a fixed row number that is set automatically. It can be used when sorting the list.

#### Invoice number
In this field you select or enter the invoice number that you wish to register as paid or partially paid. You can see all invoices that have a remaining amount greater than or less than zero. The invoice number is already filled in if the invoice has been loaded from the List tab. If you enter an invoice number that exists but is already fully paid, you will see an error message in the validation window saying that the invoice is already fully paid. An error message will also appear if you try to enter the same invoice number on several rows. You can leave the field empty in order to register an on account payment.

#### Customer
Here you see the customer number for the invoice in question. For a regular incoming payment where you have entered an invoice number, the customer number cannot be edited. However, if you register an on account payment (when you leave the Invoice number field empty), you must enter a customer number for which the new on account record will be saved. The text "On account On account is a partial payment (advance payment) which you have made to a supplier or received from a customer." will then be displayed in the Invoice number field to clarify that the payment will be registered on account for the customer.

#### Payment date
By default, you will here see the date entered as Payment date for the batch in the Settings box. The payment date refers to the date when the bank states the amount as paid. It is possible to change the date in the field, that is, you can have different payment dates for payments belonging to the same batch. This means that payments in the same batch can be recorded in different vouchers. An error message will appear if you enter a payment date that is earlier than the invoice date. A check is also be made to make sure that the entered date belongs to an open accounting period. If the payment date belongs to a closed or locked period, an error message will appear. However, if the date "only" falls outside the current period, you will see a warning but it is still possible to save.

#### Due date
Here you can see the due date of the invoice. For on account payments, the due date is set to the same date as the payment date, which is then saved in the accounts receivable record.

#### Paid amount
The paid amount is entered in the currency of the invoice (foreign currency). The remaining amount of the invoice is entered by default, but it can be changed. It is possible to enter an amount that is greater than or less than the remaining amount. However, it is not possible to enter a negative amount. In that case, an error symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) is shown and you will see a message saying that the amount has an incorrect sign. However, it is allowed to enter negative amounts for on account incoming payments.
If the paid amount that you enter is less than the remaining amount, the payment will by default be regarded as a partial payment, unless you select a write-off code in the Write-off field. In that case, the remaining amount of the invoice is set to zero and the invoice is regarded as fully paid. The paid amount is automatically converted to the company currency according to the exchange rate. It is then shown in the Amount field.
If you enter a paid amount that is greater than the remaining amount, you will see a window for overpayment. There you select how the excess amount should be handled: if you wish to register it as a balance in the customer’s favor against us (on account) or if you wish to write it off as a write-off. If you click the Write-off button, the system will keep the entered amount, and you must then select a write-off code for the remaining amount. This way the invoice will be handled as fully paid with zero as remaining amount. If you instead click the On account button, the system will change the paid amount to correspond to the remaining amount. At the same time a new row for on account payment will be added below, with the same customer number and the excess amount filled in.
For an on account payment that does not refer to an overpayment, the amount in the Paid amount field is 0,00 by default. The currency of the amount is loaded from the currency of the customer.
Credit amounts and on account amounts are displayed in red.
> In the field, you can enter the paid amount in the company currency, even though the invoice was issued in a foreign currency.

#### Exchange rate
If the invoice is issued in another currency than the company currency, you can here enter the exchange rate for the payment. The exchange rate determines what the paid amount will be in the company currency and also the rate difference that will be recorded (via the standard account for exchange profit/loss, the exception account registered for the customer primarily). You can use Find & replace (Ctrl + H) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) to change exchange rate for all records in the column.
The system setting Default exchange rate for incoming payments determines which exchange rate that will be suggested.
If this system setting is set to Current exchange rate and you have several invoices in a row in the same currency, the exchange rate of the first invoice row will be suggested for the following invoice rows. If you choose to enter the paid amount in the company currency instead of in the currency of the invoice, the exchange rate used will be based on that. It is also possible to enter exchange rates for on account payments.

#### Write-off
This Write-off column is available if the paid amount registered on the invoice is either greater than or less than, the remaining amount. If you enter a paid amount that is less than the amount on the invoice and you do not choose a write-off code, the payment will be regarded as a partial payment. If you instead choose a write-off code, the remaining amount will be removed from the invoice and posted on the account linked to the selected write-off code. Write-off codes must first be registered in the Bank settings procedure.
The Write-off column is not available on rows with on account payments.

#### Rate difference
If the invoice is registered in another currency, you can here see the rate difference in the company currency. This difference will be automatically recorded against the standard accounts for exchange rate differences. The rate difference is the calculated difference between the original rate and the rate entered in the Exchange rate field. The rate difference is not used for on account payments.

#### New remaining amount
Here you can see the new remaining amount in the invoice’s currency after the payment. A new remaining amount is only displayed if the invoice has not been fully paid, that is, if it is a partial payment and no write-off code has been entered.
For on account payments, the new remaining amount is always the same as the paid amount. The new remaining amount is displayed in red if it is a credit invoice.

#### Bank charge
Here you can enter a bank charge, if any. By default, no bank charge is displayed.
If the setting Record bank charge separately is activated for the payment method in the Bank settings procedure, the bank charge is always entered in the company currency. Otherwise, the bank charge is entered in the currency of the invoice.
Depending on whether this setting is activated or not for the payment method in question, it also affects how the bank charge is posted. If the setting is activated, the bank charge will be charged to the account entered for bank charge for the payment method. If it is not activated, the bank charge will be taken from the same account as the payment. The actual bank charge cost is recorded against the standard account for bank charge, defined in the standard accounts, unless an exception account has been entered for the customer.
Bank charge can also be entered for on account payments.

#### Interest charge
Here you determine if a delayed payment will be forwarded to the interest invoicing procedures.
There are a few factors in the system that determine whether or not interest will be charged for the incoming payment. Firstly the system checks if the setting called Penalty interest has been activated on the accounts receivable record. If it is activated, interest will be charged by default. The system checks if penalty interest should be used based on the system setting Days of grace The term days of grace (or grace period) is used at requirements planning in order to calculate rescheduling of actual orders that cover the requirement but that are too late in time, instead of suggesting a new order. for interest If the payment has been made within the days of grace, no interest will be charged. If the payment is made after the days of grace, a check of the system setting Minimum amount of interest charge per invoice will be made. If the amount of interest to charge is equal to or greater than what is entered in the system setting, interest will be charged by default. Otherwise, no interest will be charged by default.

#### Interest amount
If the incoming payment of the invoice is late, you will here see the current interest amount in the company currency. The interest amount is displayed, regardless of whether Interest is checked or not. The interest is calculated according to a general percentage for the penalty interest entered in the system setting Penalty interest, general interest rate. You can also use customer specific percentages for the penalty interest. These should then be entered in the Customer register procedure. A customer-specific percentage (other than 0,00%) overrides the general percentage.
[Read more about Interest invoicing here](../../../UserGuide/Using/InvoicingAccountsReceivable/InterestInvoicing.htm).
More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/G5_Sales_SV/Content/Resources/Images/button_more_info.png), you can generally find additional columns.

#### Payment method
The payment method shown here by default is the same as the one entered in the Settings box, but it can be changed. However, postings might be affected if the payment method is changed.

#### Initial rate
Here you can see the exchange rate that was applied when the invoice was issued, that is, the rate in the accounts receivable ledger.

#### Invoice date
Here you can see the registration date of the invoice.

#### Comment
Here you can enter a comment regarding the incoming payment. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Invoice type
Shows the type of invoice that the incoming payment refers to.

#### Credit
With this checkbox you determine if the incoming payment is a credit invoice.

#### Customer name
Here you see the name of the customer.

#### Amount
Here you can see the paid amount converted into the company currency, based on the entered exchange rate. The field can be modified, since it is possible to select whether the paid amount should be entered in the invoice's currency or the company currency.
If the invoice is registered in a currency that differs from the company currency and you change the amount, the invoice will be regarded as fully paid. The paid amount on the row is then set to the remaining amount and the exchange rate will be calculated by dividing Amount by Paid amount. This means that the normal rules for exchange rate no longer apply.

#### Remaining amount
Here you can see the initial remaining amount, that is, the remaining amount of the invoice before any incoming payment was registered.

#### Cash discount date
If cash discount is used, then you see the cash discount date here. Cash discount date and Cash discount % are shown in red font if the payment was made later than the cash discount date.
