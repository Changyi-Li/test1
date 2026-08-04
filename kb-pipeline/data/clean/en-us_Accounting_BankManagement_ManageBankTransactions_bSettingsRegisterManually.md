### Settings – Register manually

#### Payment date
Here you select the payment date of the invoices, that is, the date when the bank has stated the payment as made. Today's date is displayed by default, but it can be changed. The payment date you enter here will by default also apply to all payments registered in the same batch.

#### Payment method
Here you select the payment method that will be used for the invoices in the batch. The payment method determines how the payments will be posted, that is, on which bookkeeping account. In this field you will also see on which bookkeeping account the payment will be posted.
You can choose between the payment methods registered in the Bank settings procedure. You can select among the ones of the type Manual payment or Cash payment. The payment methods must be Active if you should be able to select them. For the Cash payment payment method you can use cash book.

#### Automatic posting of VAT
With this setting you decide if automatic posting of VAT should take place when you register other payments. Please note! The VAT posting will currently only take place in cases where posting takes place on one offset account for the bank account.
The following options are available:
- No – No automatic posting of VAT takes place.
- Yes, post gross amount – The system will re-allocate the posted amount so that the net amount is retained on the posting row, and the VAT amount is posted on a separate row.
> Via the system setting called Automatic posting of VAT on other payments, you can enter which option should be used as default.

#### Voucher number series
Here you see the voucher number series for the voucher. Voucher number series must first be created in the procedure Voucher number series/Journals. A default voucher number series can be configured in the Users procedure.
Voucher number series intended for cash book can only be used for transactions which should be registered in cash books.

#### Voucher text
Here you select the text that will be used as voucher text for incoming payments that you register. The default text is Payments, and for payments referring to cash payments in the cash book it says Cash payments. In the Voucher texts procedure you can create texts to use as pre-defined voucher texts.

#### Batch number
The batch number is a hidden, automatic function that assigns an internal number for an incoming payment batch that corresponds to the payment summary you get from the bank. The batch number is loaded from a number series and does not exist until you have saved the registration of incoming payments. The payments you report with the same payment date will be grouped together with the use of this number. Furthermore, you can search by batch number in both the ledgers and the accounting.
If you do not want to use batch number for incoming payments you should enter 0 (zero) as start code for that number series.

#### Batch total – Debit bank
Batch A batch is the set of components/products manufactured at the same time and made from the same original material. total for incoming payments to the bank account.

#### Batch total – Credit bank
Batch total for outgoing payments from the bank account.

#### Remaining batch – Debit bank
Here you see the difference between amount paid in, in the Payments box and in Batch total – Debit bank.

#### Remaining batch – Credit bank
Here you see the difference between amount paid out, in the Payments box and in Batch total – Credit bank.

#### Cash report
Here you select the cash report in which the cash payment should be registered.

#### Opening balance
Here you see the opening balance for the account linked/connected to the selected payment method.

#### Balance brought forward
Here you see the balance brought forward for the account linked/connected to the selected payment method.

#### Closing balance
Here you see the closing balance for the account linked/connected to the selected payment method.
