## Order inflow
In this procedure you can load a list containing the order inflow, that is, the result of registered customer orders and subsequent adjustments that have affected the value. The order inflow is a key ratio that shows how many orders have been received presented per customer, for agreements, for parts, over time.
All events on customer orders are entered in the order inflow on today’s date. Order inflow can be considered a log of what happens on the customer order. The list contains information that is updated with when customer order rows are created, modified, and deleted. If, for example, a price is changed for a saved row, a negative row is created in the order inflow. It also contains other information from order rows, the order header, and tables linked to these.
The order inflow is displayed according to how you’ve grouped the lists.
- If the presentation “grouped by log date” is selected, the order inflow will be displayed by log date.
- If the presentation “grouped by order date” is selected, the order inflow will be displayed by the order rows’ order date.

#### This is the process regarding order inflow in Monitor
- Newly registered order rows receive today’s date as log date.
- The order row receives an order date according to the order’s order date, but the order date can be changed per order row.
- If you make a change on an order row, this change will be logged on today’s date. The order row keeps its order date.
- If you split a row, the change will be logged for the original row on today's date.
- The new copied row is saved to the order inflow on today’s date.. The order date will be copied from the original row to the new row.
- If you add a new order row when delivery reporting, the order inflow will be logged on today’s date.
- If you delete/cancel an order row when delivery reporting, this will not affect the order inflow.
- If an order row has been deleted, it will still be shown in the list, but it will have a negative record with today’s date as log date.
- The order inflow is also affected when the commitment level (represented by Type of requirement on the customer order row) is changed from Manufactured, Buy material, or Forecast to Fixed order.
- When changing the Type of requirement to Fixed order, an order inflow record will first decrease the order inflow value for the order row and then add it again, now taking the order row’s current values into consideration and with the log date = today’s date.
> If a user does not have default values for the lists in Order inflow and Order inflow – Blanket order, selection rows and settings will be set according to the system settings for Order inflow. This is so that the order inflow matches between users and between different procedures.
> To include agreements in the order inflow, you can select by Order type – Basic type Agreement.
Example: when Type of requirement is changed
I register a customer order with part number 101001, 100 kg with the price 87.60 EUR/kg, order date 2023-04-03. Type of requirement for the order row = 4 (Forecast).
This results in the following order inflow (grouped by log date =today, grouped by order date = 2023-04-03):
Quantity: 100 kg
Price: 87.60 EUR/kg
Type of requirement: 4 (Forecast)
TOTAL: 8,760 EUR
I change the quantity to 150 kg. A new order inflow record is added to the list with the log date = today, and the order date = 2023-04-03.
Quantity: 50 kg
Price 87.60 EUR/kg
Type of requirement: 4 (Forecast)
The added amount after the change of quantity: 4,380 EUR
TOTAL: 13,140 EUR
I now change the type of requirement to 1 (Fixed order) and at the same time I change the quantity to 175 kg.
This will create two new order inflow records.
A negative record for Type of requirement 4 and a positive record for Type of requirement 1 with log date = today, and order date = 2023-04-03.
Quantity: -150 kg
Price: 87.60 EUR/kg
Type of requirement: 4 (Forecast)
This results in a negative total, that is, a decrease of Type of requirement 4: -13,140 EUR
The positive new record for Type of requirement 1 displayed in the order inflow:
Quantity: 175 kg
Price: 87.60 EUR/kg
Type of requirement: 1 (Fixed order)
TOTAL: 15,330 EUR
If you choose to show order inflow for Type of requirement 4, you will see 3 records with a total of 0 EUR.
If you choose to show order inflow for Type of requirement 1, you will see 1 record with a total of 15,330 EUR.
If you choose to show order inflow for Type of requirement 1 and 4, you will see 4 records with a total of 15,330 EUR.
List types

#### Detailed
This list shows detailed information about the value of each individual order row plus a total of the value in the selected grouping.

#### Total
This list shows total information about the value of all orders per total term. The list can be expanded so that it shows the same information on order row level as the detailed list.
Presentations

#### Detailed by date (acc. to setting)
The Detailed by date (acc. to setting) presentation groups the order inflow according to the dates selected in the system settings:
- New order inflow
- New order inflow at delivery
- Changed order inflow
If you want the order inflow for newly added order rows to be presented according to log dates, you set the system setting New order inflow to Log date.
New order rows added when delivery reporting can be presented according to log date, order date, or delivery date.
If you want the order inflow for changes made to order rows (e.g., changed price or ordered quantity) to be presented according to order date, you set the system setting Changed order inflow to Order date.

#### General information about presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, it is possible to create your own presentations. This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../Topics/UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
