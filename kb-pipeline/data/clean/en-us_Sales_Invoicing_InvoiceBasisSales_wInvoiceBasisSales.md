## Invoice basis – Sales
In this procedure you can load a list containing deliveries that have not yet been approved/invoiced. The displayed records here have been created when delivery reporting customer orders or via the procedure Register invoice directly.
The procedure is used in order to:
- See what invoice bases exist in the system which have not yet been invoiced in the system.
- Create reports that are then used when reconciling the stock to see the value of what has been taken from the stock but has not yet been invoiced.
- See already invoiced invoice bases if that status is entered in the selection.
- Show canceled invoice basis if that status is selected under the Selection tab.
- Split invoice basis (the list is activated using the system setting Enable split invoice basis).
- Undo split invoice basis (the list is activated using the system setting Enable split invoice basis).
- Change certain information in the invoice header.
As standard there is a detailed and a total list with a few different presentations. You can regroup the list and save your layouts in order to use them again in the future. There is also a list that makes it possible to edit invoice header, allowing you to update multiple invoice bases as once.
> Tip! 
Select by status 0 Canceled to see the canceled invoices in the list.
List types

#### Detailed
This list type shows information about both invoice header and invoice rows. The list can be grouped by order number, customer, or delivery note number.

#### Total
This list type shows total information about the grouping term. The list can show total by order number, customer, or delivery note number. You can expand the rows in the list to see detailed information about the orders. At the bottom of the total list you can see a chart displaying the amount, the contribution margin, and the contribution ratio.

#### Edit invoice header
This list displays the information found in the invoice header. It is possible to update information in this list.

#### Split invoice basis
In this list it it possible to split an invoice basis in two parts. This can be done if a quantity of units have been delivered, but the entire quantity should not be invoiced at the same time. For an invoice basis to be splittable, it must have status 3 – Pending.

#### Undo split invoice basis
In this list it is possible to undo the split of an invoice basis. To undo a split, both the invoice bases need to be listed, and the splitted invoice bases need to have status 3 – Pending.

#### Check prices
In this list, you can check if there are differences between the prices in the Part register and the prices on the invoice basis.
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
