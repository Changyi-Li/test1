## Undo receiving inspection
This procedure is used to correct mistakes that have been made when reporting in the receiving inspection. In the procedure, the receiving inspection is undone and the part’s status is reset to Arrival reported.
It is only possible to undo entire purchase order rows. It is not possible to undo the receiving inspection in the following cases:
- If parts have been consumed.
- If the invoice for the purchase order has been registered.
When you undo a receiving inspection, log records are created in the Stock transaction log procedure.
The following will take place when you undo a receiving inspection:
- An offset record that restores the stock balance is created in the stock transaction log.
- The inspection frequency is reset to the previous frequency.
- For subcontract purchase orders, the rejected quantity will be restored and the remaining quantity on the purchase order will be updated.
- Rejected quantity is restored and the quantity on the purchase order is reset.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
