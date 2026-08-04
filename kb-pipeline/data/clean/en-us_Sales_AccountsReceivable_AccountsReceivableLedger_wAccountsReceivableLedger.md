## Accounts receivable list
In this procedure you can load information from the accounts receivable for different purposes. The data in the accounts receivable comes from invoices and payments linked to customers, postings, and vouchers.
You can use the information to:
- Reconcile unpaid invoices against the accounts receivable balance in the general ledger.
- Search for different things, for example payment status of invoices for a certain customer.
- Show accounts receivable sorted by age (age analysis).
- See postings of invoices and payments.
With the different list types in the procedure, you decide what data to load to the list.
The Function menu
By using the Print/Send invoice documents button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_mail_and_print.png) you can "mass print" images of customer invoices for many invoices at the same time. In the dialog you can see how many invoices will be printed/exported, and you can choose if you want to Print, Send by e-mail, or Save as PDF (export to folder).
List types
The list type determines the list that will be loaded and the settings that can be configured under the Selection tab.

#### Ledger – Detailed/Total
These lists display a detailed/total list of invoices with remaining amounts per a certain ledger date. The presentation Grouped by VAT registration number in the Ledger – Detailed list type makes it possible to group the invoices that have been sent to the same VAT registration number (even if they are included within the same customer number).

#### Payments
This list shows detailed information about invoices and the connected payment records.

#### Age analysis – Detailed/Total
These lists display a total or detailed age distributed accounts receivable list per a certain ledger date. The list is based on age intervals of Invoice dates or Due dates. An age analysis based on due date shows how the invoices will become overdue according to different time intervals. An age analysis based on invoice dates shows when you invoiced according to different time intervals.

#### Reconciliation
This list is used to reconcile the balance (the remaining amount) of the accounts receivable against the balance of the general ledger per a certain ledger date.

#### Reconciliation/day
This list type is used to reconcile the accounts receivable with general ledger transactions on day level. If there are any warnings they will be displayed under a separate tab. They will also have a link ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) to the procedure in which you can perform the necessary actions.

#### Bookkeeping
This list shows how invoices and incoming payments are recorded. The report only includes invoices and payments that have been entered in journals or are posted in the accounting.

#### Balance per customer
This list shows the ledger balance per customer with a layout similar to general ledger reports. For each customer you will see the period's balance brought forward, transactions (invoices and payments) and balance carried forward.
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
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
