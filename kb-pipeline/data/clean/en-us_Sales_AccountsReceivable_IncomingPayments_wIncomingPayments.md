## Incoming payments
In this procedure you can register incoming payments in the accounts receivable ledger, set-off invoices, and also cancel incoming payments. By registering incoming payments, the invoices get status paid or partially paid in the accounts receivable ledger. Postings are also updated in the accounting.
> The following system settings affect incoming payments: Default exchange rate for incoming payments, Default exchange rate for incoming payments (via file), and Payment method during set-off.
There are three ways to register payments in this procedure. You either register the payments manually (record by record), you confirm via file, or you can register them using a list. If you choose the first alternative, go to the tab called Register manually. Read more about how to manually register payments by clicking on the heading below. If you instead wish to load a list where you can check/mark the records that are paid, then you should select the list type Register via list.
How to manually register payments
1. Start by entering Payment date and Payment method in the Settings box.
2. Continue by filling in all other information in the box or skip the following fields by using the Tab key. Tab until the cursor is placed on the top row in the table where payments are registered in the Incoming payments box.
3. Add a new row by using the shortcut key F5 or + (the plus sign) on the numerical keyboard and select/enter an invoice number. If the incoming payment is an on account payment, leave the invoice number field empty and instead you enter the customer number for the customer who made the payment.
4. Check the row and adjust, if needed, the suggested values for the payment.
5. Add rows for the incoming payments that have been made.
6. When you have entered all the incoming payments you wish to register, click the Save button or the Save and print journal button. In the latter case, the Print incoming payment journal procedure is automatically opened, with the correct journal loaded. At the same time, the procedure is prepared for the next batch of incoming payments to register by emptying all the fields and moving the focus back to the Payment date field in the Settings box.
For each incoming payment, you can see how the posting is created in real time in the Posting box. The Total field at the bottom is updated continuously.
Set-offs and cancellation
It is also possible to pay invoices by offsetting one invoice against another. A invoice with a large amount can e.g. be set-off against a number of debit invoices to the same customer. When you make such a set-off, all the affected invoices will become registered as paid. Set-offs are made under the Set-off tab.
You can also cancel payments and set-offs in the procedure. In order to cancel incoming payments, select the list type Cancel incoming payments. To cancel set-offs, select the list type Cancel set-offs instead.
On account On account is a partial payment (advance payment) which you have made to a supplier or received from a customer.
In this procedure you can also register outgoing payments as on account payments.
That is, when the customer makes an incoming payment that refers to payment of something that does not exist in the accounts receivable ledger, e.g. an advance payment or an overpayment. An incoming payment like that creates a new accounts receivable entry of type "On account" and will then exist as a balance in that particular customer's favor in the the accounts receivable ledger. You add on account payments under the Pay manually tab by leaving the field Invoice number empty.
List types
In this procedure there are three list types. Bases on the selections you make you will see invoices in the List tab.

#### Register via list
This list type is used to create a list containing invoices to register as paid.

#### Cancel incoming payments
This list type is used when you wish to delete already registered payments.

#### Cancel set-offs
This list type is used to cancel set-offs made between invoices.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
