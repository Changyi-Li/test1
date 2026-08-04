## Print transaction list
In this procedure you can print transaction lists for outgoing payments that are sent electronically to the bank in a file. These files are created when you approve the transaction lists. You approve the list either via printout or via the button Approve ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_approve_document.png).
The transaction list is a form of receipt of which payments that have been sent to the bank. It specifies the invoices that are included and when these should be paid, etc. Each transaction list is numbered. This provides an identity to the payment files that becomes created. These numbers are not displayed on the transaction list, but is saved in the system when you created the list/file.
> This procedure is available in the Purchase module and the Accounting module, with the same contents.
Print transactions from Outgoing payments
You only need to use this procedure if payment files should be created via printouts of transaction lists. In the Outgoing payments procedure you can create payment files without printing transaction lists. The number of the transaction list is saved regardless of which method that is used.
Normally, this is not a procedure which you open manually to work in. It is more common that it is opened automatically from the Outgoing payments procedure when you choose to print transaction lists. However, if you for example want to reprint a list or change the status of a payment file to the previous status, this is the procedure you need to go to.
New records are added to this procedure when electronic payments are executed in the Outgoing payments procedure. When the transaction list has been approved and a file has been created with a successful result, then the records will be removed from the procedure. However, they can be reprinted.
Change status to resend
By using the list type Change status to resend, you can change the status back to a previous status on one or several payments that are included in a transaction list. This means that the payments will be put back in the transaction list in order to be possible to send again.
> You must select a valid payment method in the selection in order to be able to load the list.
List types

#### Transaction list
The transaction list is a document that is tied to a payment format. The information that is shown about the payment is giro transfer, account deposit, and cash payment. Under the respective main grouping there are sub-groupings per payment currency (this means that for example invoices in the company currency and invoices in EUR are shown separately). At the bottom you find the total row for hash total. In the Transaction list ISO you find both a currency total and the total row for hash total.

#### Reprint – Transaction list
In this list type you can load transactions lists that have already been printed. These documents can then be previewed and printed or sent by e-mail.

#### Change status to resend
This list type is used when you need to put the payments back in the transaction list (change status to resend). The rows for the payments can be selected and saved in order to change the status back to a previous status. These payments can then be loaded to the transaction list again. Then it is possible to resend the payment files.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
