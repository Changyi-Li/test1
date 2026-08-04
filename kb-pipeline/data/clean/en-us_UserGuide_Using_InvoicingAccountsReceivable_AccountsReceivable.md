### Accounts receivable

#### Incoming payments
In this procedure you find all of the methods to report incoming payments in Monitor ERP.
- The list type Register via list is used to report multiple incoming payments in a list.
- The tab Register manually is used to register incoming payments one at a time. If you add a row without an invoice number, it then becomes an on account incoming payment. It is possible to add a partial amount and then select if the rest should remain in the accounts receivable or if it should be written off.
- The tab Confirmation via file is used to load a file from the bank containing data of paid customer invoices. The data in the file will then be matched against the open records in the accounts receivable.
- The list type Cancel incoming payments is used to delete one or several incoming payments when needed. When you have loaded the list you mark the incoming payments to cancel. When you save the list, a question will appear asking if you wish to cancel the selected payments. When an incoming payment is canceled you can again see the invoice in the list type Register via list.
- The tab Set-off is used to set-off a debit invoice against a credit or an on account incoming payment. You can also set-off customer invoices against supplier invoices here. To be able to do this, it is required that customer and supplier have a joint VAT number or corporate ID number in the registers.
- This list type Cancel set-offs is used to cancel set-offs between invoices.

#### Print incoming payment journal
In this procedure you print the incoming payment journal and approve it. It is also possible to approve the journal without printing it. The accounting becomes updated when you approve the journal. Here you can also create a reprint of an incoming payment journal.
When using direct integration of incoming payments to the accounting, this step is not included in the workflow.

#### Accounts receivable list
The purpose of this procedure is for example to:
- Show or reconcile unpaid invoices and the accounts receivable balance in the general ledger.
- Search for different things, e.g. the payment status of invoices to a certain customer.
- Show an age-distributed accounts receivable (age analysis).
- Show postings of invoices and payments.

#### Payment reminder basis
In this procedure you see a list of overdue invoices for which you can print payment reminders. By default all overdue invoices are selected. But you can uncheck those invoices for which you do not want to print payment reminders.

#### Print payment reminder
In this procedure you print all payment reminders. It is possible to select an interval of customers. You can also print account statements. As opposed to the payment reminders, the statements also show invoices that are not yet overdue.

#### Interest charge basis
In this procedure there is a list showing the delayed/overdue incoming payments that have been registered in the system. You can choose to create a separate interest invoice or to add the interest to the next regular invoice. You then create the interest invoices by pressing the button Release interest invoices ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar. You are then linked to the approval and printing of these in the Review/Approve invoice procedure.
> To be able to create interest invoices there are a few settings you need to configure. You can read about this in the topic [Interest invoicing](InterestInvoicing.htm).

#### Update accounts receivable
This procedure is used when there is a need to make changes to certain information on accounts receivable records (invoices) or when you need to delete/cancel them. It is possible to cancel invoices as long as no incoming payment has been registered for the invoice in question. You cancel incoming payments in the Incoming payments procedure.
You can also register new accounts receivable records in the procedure, but this is normally only done when changing from another financial system to Monitor ERP.
> Monitor tip! Use the links on invoices in the Accounts receivable list procedure to e.g. pay, set-off credit invoices, or to view additional information about the invoice via the Update accounts receivable procedure. Use the Cash flow forecast procedure to see expected incoming and outgoing payments per period.
