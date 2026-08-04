## Order list – Purchase
In this procedure you can load purchase orders in detailed, total, and chart form. The delivery date and confirmation can be updated in the detailed list. There are standard list types with different presentations included in the system. You can regroup the list and save own layouts in order to use them in the future.
Subcontract
Subcontract is a special order type for purchase. The rows for this type of purchase order are linked to specific operations on manufacturing orders. In the order list you also see the order type called subcontract in all lists. Under the Selection tab, you can choose which order types that will be loaded.
With the list types Subcontract and Shipped subcontract, you can only load information about subcontracts. Only orders that at the moment have a number of operations at the supplier will be shown in the list type Shipped subcontract. That list type shows orders with a shipped quantity greater than the reported quantity.
List types

#### Detailed
This list type shows information about both order header and order rows. The list can be grouped by order number, supplier, or delivery date.

#### Detailed – Editable
This list type shows information about both order header and order rows. You can update delivery date, price each, and ordered quantity. You can also mark rows as confirmed by the supplier. Subcontract orders are excluded from the list. Changes to subcontract orders should be made on the manufacturing order.

#### Total
This list type shows total information about the grouping term. The list can be grouped by order number, supplier, or delivery date.

#### Subcontract
This list type shows information about the link to the specific operation on a manufacturing order. The list can be grouped by order number or supplier.

#### Shipped subcontract
This list type shows only purchase orders that currently has operations at the supplier. The shipped quantity is greater than the reported quantity. The list can be grouped by order number or supplier.

#### Stock order
This list type displays information from both the order header and the rows for stock orders (purchase), grouped according to the selected presentation. The list can be grouped by order number, supplier, or delivery date.
This list type is available if you have the option Warehouse.

#### Loading plan
This list type shows a loading plan for arrivals. By using a setting you can select if you only want to include purchase of material, shipment of subcontract, or arrival reporting of subcontract. Under the List tab you will see information from the order backlog about arrivals as a loading plan for selected orders. For shipment of subcontracts, the information is loaded from the start date on the operations (subcontracts) and the purchase order rows in the order backlog to which they belong.

#### Check delivery times
This list runs a check of the delivery times (CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.) for selected purchase orders in order to analyze and show the consequences a delayed arrival of these orders would result in. There are setting where you choose if CDT should analyze actual orders, suggestions, and forecasts. You can also add a number of days in a simulated delay of confirmed and unconfirmed order rows to see the resulting consequences.

#### Posting
This list type is used with the purpose of reviewing and updating posting items for purchase orders. Only order rows that have a remaining quantity are shown in the list. You can update both account and dimensions in the list and you can use the Find & replace function. It may be useful to mass update accounts, for example, when making the shift to begin recording your stock on a stock account in the balance sheet, rather than on a cost account.

#### Edit order header
In this list you can update most fields available under the Header tab in the Register purchase order procedure.
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
