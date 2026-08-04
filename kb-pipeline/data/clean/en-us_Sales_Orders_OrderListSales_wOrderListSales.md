## Order list – Sales
In this procedure you can create lists of existing customer orders and customer orders based on agreements. The lists are available both as detailed and total, which is determined by the list type selected. In the total list you can also show data as a bar chart. The amounts are displayed by default.
In the detailed list you can update discount rates on the order rows. In order to update other information on an order, you can use a link to go to the Register customer order procedure from the order in the list. It is also possible to include delivered order rows in the list.
Please note! Customer orders of the Agreement type cannot be updated in the Register customer order procedure.
There are additional list types in this procedure which you can use to check if there is a standard price for parts in the existing orders. There is also a list type for stock orders (if the option Warehouse is installed). If you are using the check delivery times function (CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.), you also find a list type for CDT. Read more about all list types below, and in the online help topics for each list type.
> Agreements are also included in the Order list.
The orders are loaded by warehouse to the lists.
List types

#### Detailed
The detailed list displays information from both the order header and the rows, grouped according to the selected presentation. The list can be grouped by order number, customer, or delivery date. In this list it is possible to update discount rates on each order row.

#### Configuration – Detailed
This list is available if the option Product configurator is installed in your system. The list displays detailed information regarding configured parts in different designs or variants on customer order rows. For each configured part you can see the different choices made in the configuration.

#### Total
The total list displays amount, contribution margin and contribution ratio, totaled according to the selected presentation. The list can show total by order number, customer, or delivery date. The list can also displayed data in a bar chart. The amounts are displayed by default.

#### Configuration – Total
This list is available if the option Product configurator is installed in your system. This list shows total information about configured customer order rows.

#### Stock order
This list type displays information from both the order header and the rows for stock orders (sales), grouped according to the selected presentation. The list can be grouped by order, customer, or delivery date. This list type is available if you have the option Warehouse.

#### Check standard price
This list type is used to check that ordered parts have a standard price. The list also displays the contribution margin and contribution ratio for the order rows.

#### Edit order header
In this list you can update most fields available under the Header tab in the Register customer order procedure.

#### Check delivery times
If check delivery times (CDT) has been activated with the setting Apply check delivery times, you also find this list type. It is used to run a check of delivery times for multiple customer orders at a time. In this list you can see if there are any delayed orders.
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
