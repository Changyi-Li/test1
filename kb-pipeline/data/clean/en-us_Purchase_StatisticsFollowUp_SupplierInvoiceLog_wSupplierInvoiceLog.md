## Supplier invoice log
In this procedure you can load a list displaying a log/statistics of purchases. It is based on the supplier invoices that are final coded in the system. The lists show information both from linked order rows and posting rows in the final recording.
When you final record an expense invoice (is not linked to an order) the log will show posting rows from the final recording (only the rows that have created the net value of the invoice, that is, not VAT and for example supplier debt).
When you final record an order invoice the log will display the linked invoice rows. In the log you will also see postings made manually outside the order link, due to difference.
If the function to create invoice basis at arrival reporting has been deactivated (either on supplier or via system setting) the supplier invoice log will not show purchase statistics for order and part level. For you to be able to see detailed purchase statistics at order and part level, you then have to get that information using the Arrival log and Stock transaction log procedures.
You can search and present the information in different ways, for example per supplier invoice, supplier, order, etc. There is both a detailed and a total list type. It is not possible to update information in these lists.
The Function menu
By using the Print/Send invoice documents button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_mail_and_print.png) you can "mass print" images of supplier invoices for many invoices at the same time. You can in this dialog choose if correspondence with the supplier should be included, see how many invoices will be printed/exported, and you can choose if you want to Print, Send by e-mail, or Save as PDF (export to folder).
List types

#### Detailed
In this list type you find detailed information from the supplier invoice log.

#### Total
In this list type you find total information from the supplier invoice log. On each row you can drill down and view the detailed information.
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
