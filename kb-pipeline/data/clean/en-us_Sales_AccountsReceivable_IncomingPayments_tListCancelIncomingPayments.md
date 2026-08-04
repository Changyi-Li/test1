### The Cancel incoming payments list
This list contains payments for invoices including credit invoices. For the list type Cancel incoming payments you will see the following columns:

#### Cancel
In this column you check the invoices for which you wish to cancel incoming payments. The cancellation is executed for the checked invoices when you save. A box will then appear asking you to confirm that you wish to save the cancellation. When canceling payments, the remaining amount of the invoices will be reset. Furthermore, a posting will be created that reverses the posting of the payment. The canceled payment records remain in the system but with status Canceled. You can print canceled payments in the Accounts receivable list procedure, in the list type Payments.

#### Invoice number
Here you see the invoice number that the incoming payment refers to.

#### Show document
With the Show document button you can review the invoice to which the payment refers. Using the Show document button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png), you open the document in a separate window. There you can also reprint the document or attach it to an e-mail message. The invoice is marked with the text "Reprint".

#### Customer
Here you see the customer number of the customer on the invoice.

#### Name
In this column you see the name of the customer on the invoice.

#### Payment method
In this column you see the payment method used when the payment was made.

#### Payment date
The date that was entered as payment date when the incoming payment was registered (usually the payment date stated by the bank).

#### Paid amount
In this column you see the amount registered as paid, regardless of the original amount on the invoice. The amount is shown in the currency in which the payment was registered.

#### Amount written off
Here you see the amount that was written off, if any, when the payment was made. The amount is shown in the currency in which the payment was registered.

#### Total
In this column you see the total of Paid amount and Amount written off. The total is shown in the currency in which the payment was registered.

#### Voucher date
By default you here see the same date as the Payment date. A check will be made to make sure that the voucher date belongs to an open accounting period. If the date belongs to a closed or locked period, an error message will appear. However, if the date "only" falls outside the current period, you will see a warning but you can still save and thereby go ahead with the cancellation of the payment. The voucher date can be changed in order to record the cancellation on another date.

#### Batch number
In this column you see the batch number that was entered for the batch of payments made at the same time. The batch number was loaded from a number series when the incoming payments were saved.

#### Journal number
In this field it is shown in which journal the payment is recorded if you load an existing batch number.

#### Credit
This checkbox is checked if the invoice is a credit invoice. Furthermore, the text on the row is displayed in red if it is a credit invoice.

#### Total
At the bottom of the window, below the list, you see a total amount of the selected invoices. The total of credit invoices, if any, is calculated as negative entries and the total of the other invoices as positive entries.
