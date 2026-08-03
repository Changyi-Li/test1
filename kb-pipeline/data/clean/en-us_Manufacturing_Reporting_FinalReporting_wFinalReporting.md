## Final reporting
In this procedure you can in a list update the status of finished manufacturing orders either to status 6 (delivered) or 9 (historical).
One purpose of final reporting is to finish/complete the manufacturing order and lock it for further reporting, by setting the status to 9 (historical).
Final reporting for correct WIP value
Another reason to final report is to make the calculation of WIP value correct in cases where manufacturing is made directly against customer orders. When a customer order is delivery reported, an invoice basis will be generated (that will later turn into an income). At the same time, the manufacturing order(s) that are reported as finished and are included in the customer order, must be final reported by changing the status to 6 (delivered). If you do not final report these manufacturing orders, the parts in these orders will remain as WIP value, which will provide an incorrect result, as the customer order will later generate an income. This applies when WIP value is calculated for manufacturing orders with status 4 and 5.
What can be updated in the procedure?
The status is the only thing that can be updated for manufacturing orders in this procedure. Material with traceability where there is a remaining quantity, cannot be reported.
List types
The list shows information about all the selected manufacturing orders.
Here you select the manufacturing orders for which you wish to update the status to 6 or 9 (depending on which alternative you chose under the Selection tab).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
