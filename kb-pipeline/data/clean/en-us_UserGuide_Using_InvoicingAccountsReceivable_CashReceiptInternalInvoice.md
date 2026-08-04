### Cash receipt and Internal invoice

#### Cash receipt
You use cash receipt when making sales where you receive cash payment (in actual cash or via card payment) in connection to when you approve and print the invoice, for example when selling in a store. Cash receipt can also be selected when you register customer orders.
The cash receipt will be paid automatically in the accounts receivable when approved. Posting of the cash receipt is recorded in the customer invoice journal. No incoming payment journal will be printed for this invoice type (even though it automatically becomes set as paid).
On invoices of the type cash receipt, no payment terms are shown.
Cash receipt has a separate document template and can also have a separate number series (optional).

#### Internal invoice
Internal invoices are for internal use to handle sales of internal customer orders, for example when withdrawing goods for a trade fair, etc. Then you wish to register the withdrawal from stock and to get a delivery note for the withdrawal, but the invoice should only be recorded as internal sales and not to be sent to customer. Here you often use an internal customer number on the order (referring to the own company or sometimes departments in the company). You might also use it when dealing with internal invoicing between group companies.
Posting of the internal invoice is recorded in the customer invoice journal.
Internal invoice has a separate document template and can also have a separate invoice number series (optional).

#### Determining invoice type on order and invoice
Order type
On order types for customer orders and on payment terms you determine which Invoice type should be used on order and invoice. For order types you either choose According to customer's pmt terms, Internal (invoice), or Cash receipt. For a new order type it will by default be According to customer's payment terms, but it is possible to change.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CashReceiptInternalInvoiceOrderTypes.png)](../../../../Resources/Images/TrainingMaterial/CashReceiptInternalInvoiceOrderTypes.png)
Payment terms
If you choose Internal or Cash receipt for the order type you must also select a Payment term. A payment term determines how the order should be invoiced, that is, the invoice type of the term. All payment terms where you enter a credit time of one or several days will always get the invoice type Invoice and cannot be changed. For payment terms without credit time, that is, which have zero (0) set as number of credit days, it is also possible to select cash receipt or internal invoice as invoice type. A new payment term will by default be given the invoice type Invoice.
You need to configure your payment terms for cash receipt and internal invoice, depending on which you wish to use. This is done in the Terms procedure. For these payment terms you enter zero (0) as number of credit days. In the column Invoice type you select Cash receipt or Internal.
When invoicing cash receipt and internal invoice, these will automatically be set as paid. For cash receipt the payment method affects which cash account the invoice will be recorded against. That is why there is a default payment method for that payment term in the procedure. For internal invoice the payment method is not really important, since the posting is loaded from a standard account and not from the account of the payment method.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CashReceiptInternalInvoicePaymentTerms.png)](../../../../Resources/Images/TrainingMaterial/CashReceiptInternalInvoicePaymentTerms.png)

#### Register customer order
In this procedure you find the field Invoice type in the Invoicing box. According to above, it is the order type or the payment term which determines the invoice type used on the order. It is also possible to manually change order type, change payment term or invoice type of the order in this procedure, as long as the order has not been invoiced. When the order is invoiced it will get the invoice type you selected.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CashReceiptInternalInvoiceOrderTypeOnOrder.png)](../../../../Resources/Images/TrainingMaterial/CashReceiptInternalInvoiceOrderTypeOnOrder.png)
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CashReceiptInternalInvoicePaymentTermInvoiceTypeOnOrder.png)](../../../../Resources/Images/TrainingMaterial/CashReceiptInternalInvoicePaymentTermInvoiceTypeOnOrder.png)

#### Register invoice directly
Regarding order type, payment terms, and invoice type, this procedure works in the same way as the Register customer order procedure. But here you can also change the invoice type to interest invoice. It is also possible to credit a cash receipt and internal invoice in this procedure.
