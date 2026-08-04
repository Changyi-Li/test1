## Interest charge basis
This procedure is used to see the customers that have paid invoices after the due date. This is done in order to create a basis for charging of penalty interest. This procedure is based on data from the accounts payable. Interest invoices are filtered out from these lists. The data can only be updated in the detailed list type.
Work flow in the procedure
Under first tab you select what should be loaded to the list. Then you go over the invoices in the list to select if and how interest should be charged, Interest is charged either via an interest invoice or it is charged on the next regular invoice. It is also possible to choose this per overdue payment.
If you choose to charge via Interest invoice, then you can release the interest invoices by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar. After this you will be linked to the Review/Approve invoice procedure, to review the interest invoices which have been created, and then send them to the customers.
If you choose to charge interest via the Next regular invoice and save, then the row will become gray and it is no longer possible to release that basis. Instead you can add these interest bases to the next regular invoice in the procedure Review/Approve invoice by clicking the Add interest button which you find at the top of the Result box.
How the interest should be charged is configured per customer in the field Interest charge in the Customer register. This choice can be adjusted in the Incoming payments procedure in connection to when then customer pays the invoice. This can also be adjusted afterwards in the Update accounts receivable procedure.
> Before you can start charging interest you must configure some settings in the system. Read more about this in the [Interest invoicing](../../../UserGuide/Using/InvoicingAccountsReceivable/InterestInvoicing.htm) topic.
List types

#### Detailed
With this list type you load a detailed basis for interest charge. The list contains partially paid invoices and fully paid invoices, which have interest that should be charged the customer. Based on this list you can release bases for interest charge. The list is grouped by customer.

#### Total
This list shows about the same information as the detailed list, but it is shown as total per customer. In this list it is not possible to update any information or release any invoice bases. However, you can expand the rows to show the detailed information. The list is total by customer.
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
