## Order inflow – Blanket order
In this procedure you can load containing the blanket order inflow, that is, the result of registered blanket orders and subsequent adjustments that have affected the value. The blanket order inflow is a key example ratio that shows how many blanket orders have been received presented per customer, for parts, over time.
The list contains information that is updated with log dates when blanket order rows are created, modified, and deleted. If, for example, a price is changed for a saved row, a negative row is created in the order inflow. It also contains other information from blanket order rows, the order header, and from tables linked to these.
> If a user does not have default values for the lists in Order inflow and Order inflow – Blanket order, selection rows and settings will be set according to the system settings for Order inflow. This is so that the order inflow matches between users and between different procedures.
> Calls created on blanket orders are not shown in the blanket order inflow.
List types

#### Detailed
This list shows detailed information about the value of each individual order row plus a total of the value in the selected grouping.

#### Total
This list shows total information about the value of all orders per total term. The list can be expanded so that it shows the same information on order row level as the detailed list.
Presentations

#### Detailed by date (acc. to setting)
The Detailed by date (acc. to setting) presentation groups the order inflow according to the dates selected in the system settings:
- New order inflow
- Changed order inflow
This means that new added order rows can be presented as order inflow according to order date, and changes can be presented according to log date.

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
