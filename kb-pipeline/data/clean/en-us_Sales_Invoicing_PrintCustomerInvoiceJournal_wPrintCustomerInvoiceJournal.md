## Print customer invoice journal
In this procedure you can print journals containing approved invoices with postings. The journals can be reviewed and approved in order to then be transferred to the accounting. Some companies print the journal together with the accounting order, in order to put them in a voucher binder. After the journal has been approved, you can print it again via the reprint list.
> You only need to use this procedure if you apply integration to the accounting via printout of journals. If you apply direct integration of payments, you do not need to print the journal.
New records are added in this procedure when invoices are approved in the Review/Approve invoice and Register invoice directly procedures.
It is also possible to change the posting in the journal before it is approved. In the Preview box, there is a link you can use to open the Edit posting window. It is not possible to modify rows that in the chart of accounts have been marked with Block for manual postings. The journals in this list show the postings in detail per entry and a total at the bottom (total accounting order) shows the posting totaled by posting string.
A break is made per accounting period. If the dates of the invoices are from more than one month, one journal per month will be created. When the journal is approved, vouchers will be created in the accounting. A check will be made to make sure that the periods are open before any approval is allowed. You can approve the journal either via a control question after printout, or by approving it directly in the list using the button Approve ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_approve_document.png) in the toolbar.
You can also print cancellation journals in the procedure. Cancellation of customer invoices is made via the Update accounts receivable procedure.
List types

#### Customer invoice journal
In the document header you will see the company, and user. You also see the date and time for the printout.
The list is sorted by invoice number. Information about the invoice, customer, and amounts are shown in columns.
On one row, you will see the posting information. Via a link you can open Edit posting. There it is possible to edit some of the posting information.
A total of the amounts is displayed at the bottom of the journal.

#### Cancellation journal
In this document you will see the same layout and functions as in the customer invoice journal. The difference is that there is a different journal number series.

#### Reprint – Customer invoice journal
This list type displays a list of approved customer invoice journals to reprint. In the Result box you see which user approved the journal and when.

#### Reprint – Cancellation journal
This list type displays a list of approved cancellation journals to reprint. You will here see the user which approved the journal and when.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
