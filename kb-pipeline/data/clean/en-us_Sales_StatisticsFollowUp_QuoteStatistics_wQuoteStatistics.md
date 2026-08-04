## Quote statistics
In this procedure you can load lists containing quotes with status Finished. The procedure is used to see how large part of the quotes that lead to actual orders, and you use it to analyze why the other quotes did not become orders. The analysis is done by looking at the cause codes entered for the finished quotes.
The list is not selected by status. All quotes with status 6 to 9 (Finished, Partial order, Order via related quote, and Order) will be shown in the list. The list is mainly based on the quote register and also a few other registers such as the customer and part register. It is not possible to update any information in this list.
List types

#### Detailed
This list type shows detailed information about the quotes. It can be presented as grouped by quote number or grouped by customer.

#### Total
This list type shows total information about the quotes. It can be total by quote number, customer, date, or status.

#### Total by cause code
This list type shows total information about the cause codes which the list is totaled by.
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
