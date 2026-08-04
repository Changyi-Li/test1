## Print incoming payment journal
In this procedure, you can print journals of incoming payments and their postings. You can review the journal and then approve it without printing. You can also print the journal/accounting order and approve the printout, e.g. in order to put it in a voucher binder.
You can also approve and print set-off journals. Set-offs can be made if there are unpaid customer invoices and supplier invoices to/from the same company. If set-offs should be applicable for the customer and supplier they must either have the same corporate ID number or the same VAT registration number in the customer register and supplier register. Then you can set-off customer invoices (debit) against supplier invoices (debit).
You can load new records in this procedure in connection to registering or canceling incoming payments in the Incoming payments procedure. When you approve a journal, or print a journal and approve the printout, the entries/records will get a journal number and the journal is transferred to the accounting. The entries/records will then disappear from this procedure. However, you can reprint the journal if you select the list type Reprint – Incoming payment journal.
You only need to use this procedure if it is configured in the system that integration to the accounting should be made when printing journals. If the integration to the accounting is set to be made as direct integration, you do not have to print a incoming payment journal. How the integration should be applied, or if you do not wish to apply any accounting integration at all, is configured in the Voucher number series/Journals procedure. There you can also configure the number series for the incoming payment journal and in which voucher number series it should be recorded. It is recommended that the journal number series continue across the year-end. However, the voucher numbers for the payment journals will automatically restart from 1 when starting a new accounting year.
If you do not use the Accounting module in Monitor ERP, you can use this procedure to create/load and print accounting records for bookkeeping in another accounting system.
At the end of each journal you will see a total accounting order. The total accounting order summarizes all the postings of the journal total by account and dimension. When transferring to the accounting, it is the total accounting order that creates the voucher in the accounting.
> This procedure is available in the Sales module and the Accounting module, with the same contents.
List types

#### Incoming payment journal
This list loads new incoming payment journals for approval and printout.

#### Set-off journal – Between accounts payable and accounts receivable
With this list type you load journals for set-offs that should take place between the accounts payable and accounts receivable.

#### Reprint – Incoming payment journal
In this list you can print already printed and approved incoming payment journals.
