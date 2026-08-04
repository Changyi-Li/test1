### Settings

#### Payment date
Here you select the payment date of the invoices, that is, the date when the bank has stated the payment as made. Today's date is displayed by default, but it can be changed. The payment date you enter here will by default also apply to all payments registered in the same batch.

#### Payment method
Here you select the payment method that will be used for the invoices in the batch. The payment method determines how the payments will be posted, that is, on which bookkeeping account. In this field you will also see on which bookkeeping account the incoming payment will be posted.
You can choose between the payment methods registered in the Bank settings procedure. You can select among the ones of the type Manual payment. The payment methods must be Active if you should be able to select them.

#### Voucher text
Here you select the text that will be used as voucher text for incoming payments that you register. The default text is Incoming payments. In the Voucher texts procedure you can create texts to use as pre-defined voucher texts.

#### Batch total
The Batch A batch is the set of components/products manufactured at the same time and made from the same original material. total field can bu used as an optional control function. The purpose of the batch total field is to enter the total amount that the bank has stated as paid into the account. After having registered all the incoming payments, the system will then warn if the amount does not match the entered batch total. In the field to the right of the Batch total there is a field for currency. There you can select currency used in the Batch total field. By default the company currency is selected, unless you have selected a payment method linked to a currency account. In that case, this currency will be suggested instead. You will find information about whether an account is a currency account or not in the Chart of accounts procedure.

#### Remaining batch
The remaining batch displays the difference between the Batch total and the amount of the incoming payments you have registered. When all the incoming payments have been registered, the remaining batch should be zero. If it is not zero when saving, you will see a warning but it is still possible to save, even though there is a remaining batch.
The remaining batch takes the currency of the batch total into consideration. The remaining batch only add together invoices registered in the same currency as the batch total. If you change the currency, the remaining batch will only add together invoices in the new currency. That way you can check the remaining batch per currency if you have registered payments in different currencies.

#### Batch number
The batch number is a hidden, automatic function that assigns an internal number for an incoming payment batch that corresponds to the payment summary you get from the bank. The batch number is loaded from a number series and does not exist until you have saved the registration of incoming payments. The payments you report with the same payment date will be grouped together with the use of this number. Furthermore, you can search by batch number in both the ledgers and the accounting.
If you do not want to use batch number for incoming payments you should enter 0 (zero) as start code for that number series.
