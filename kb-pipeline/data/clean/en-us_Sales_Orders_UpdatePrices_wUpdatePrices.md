## Update prices – Customer order
This procedure is used to check and update prices (price each) for existing order rows. The prices will be modified based on the updated prices in the Part register procedure.
It is possible to update the price for order rows on orders with status 1-5 and have a remaining quantity.
The following order rows cannot be updated with a new price using this list:
- Alloy cost.
- Order rows where final delivery have been made.
- Order rows concerning blanket orders.
- Order rows containing configured parts or remote configured parts.
- Order rows with row type 2.
- Order rows included in a Total row (row type 3).
- Order with order discount or order value.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
