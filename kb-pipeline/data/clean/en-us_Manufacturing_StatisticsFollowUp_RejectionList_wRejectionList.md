## Rejection list
In this procedure you can follow up on rejections that have been reported for operations and for individual material in manufacturing orders.
The Rejection list loads data from the manufacturing order log and cannot be updated. You can only see reporting items here that contain rejections. The actual date for the material's rejection is shown.
You can see rejections that have been reported in one or several warehouses. You select warehouse in the toolbar of the procedure.
Cost calculation of operation rejections
The cost calculation of operation rejections includes the order’s planned costs for the rejected quantity. This is calculated for material and operations up to and including the operation where the rejection takes place. The operation's costs are calculated as planned setup time for the operation, multiplied by the default setup cost for the work center.
The staffing factor for setup cost registered for the operation can affect the cost calculation. This is determined by the system setting called Staffing affected cost factors. Furthermore, the unit cost is added as the operation's planned unit time multiplied by the default unit cost for the work center. The staffing factor for unit cost registered for the operation can affect the cost calculation. This is determined by the same system setting as for the setup cost. Unit cost and setup cost are shown together as processing cost in the list.
Cost calculation of material and subcontract rejections
For material and subcontract, the cost calculation is less complex. There the price is entered directly on the operation. For material, the planned quantity is the operation quantity that has been rejected. Material cost comes from both materials linked to both earlier and current operations. With a setting for the rejection code you can determine that material should not be rejected. This only applies however to material linked to the operation that the rejection is reported on.
List types

#### Operations – Detailed
This list type shows detailed information about rejections reported on operations. The list can be grouped by rejection code, rejection date, part, and work center.

#### Operations – Total
This list type shows total information about rejections reported on operations. The list can be total by rejection code, rejection date, part, and work center.

#### Material – Detailed
This list type shows detailed information about rejections reported on material. The list can be grouped by rejection code, rejection date, and part.

#### Material – Total
This list type shows total information about rejections reported on material. The list can be total by rejection code, rejection date, and part.
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
