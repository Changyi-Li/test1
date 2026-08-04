## Print payment journal
In this procedure, you can print journals of payments and their posting. You can review the journal and then approve it without printing. You can also print the journal/accounting order and approve the printout, e.g. in order to put it in a voucher binder.
You can load new records in this procedure in connection to registering payments in the [Handle bank transactions](../ManageBankTransactions/wManageBankTransactions.htm) procedure. When you approve a journal, or print a journal and approve the printout, the entries/records will get a journal number and the journal is transferred to the accounting. The entries/records will then disappear from this procedure. However, you can reprint the journal if you select the list type Reprint – Payment journal.
In the journal the payments are divided into sections for customer payments, supplier payments, and other payments.
You only need to use this procedure if it is configured in the system that integration to the accounting should be made by printing journals. If the integration against the accounting is set to be made as direct integration, you do not have to print any payment journals. How the integration should be applied, or if you do not wish to apply any accounting integration at all, is configured in the Voucher number series/Journals procedure. There you can also configure the number series for the payment journal and in which voucher number series it should be recorded. It is recommended that the journal number series continue across the year-end. However, the voucher numbers for the payment journals will automatically restart from 1 when starting a new accounting year.
If you do not use the Accounting module in Monitor ERP, you can use this procedure to create/load and print accounting records for bookkeeping in another accounting system.
At the end of each journal you will see a total accounting order. The total accounting order summarizes all the postings of the journal total by account and dimension. When transferring to the accounting, it is the total accounting order that creates the voucher in the accounting.
List types

#### Payment journal
This list loads new payment journals for approval and printout.

#### Reprint – Payment journal
In this list you can print already printed and approved and payment journals.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
