## Undo arrival reporting
In this procedure, you can undo previously made arrival reports.
When you undo an arrival reporting, log records will be created in the Stock transaction log procedure. An offset record is created in the accounting that balances the previously reported arrival. Both the previously reported arrival and the undone arrival are labeled in the logs so that they can be excluded in the Supplier rating and Undo arrival reporting procedures.
It is possible to undo arrival reporting in any optional order.
You cannot undo arrival reporting if the invoice basis has been linked to a supplier invoice. Also, it is not possible for undo manufacturing orders with status 9.
Traceable material
If you undo arrival reporting containing traceable material, then the material will be returned to the same mode as before the reporting, regarding status, balance, etc. Serial numbers/batches created at the reporting which are not used in any other cases, will be deleted when you undo delivery reporting.
The following will take place when you undo an arrival:
- An offset record is created in the stock transaction log which resets the stock balance. The arrival log is deleted.
- The invoice basis and the reported receiving inspection will be deleted.
- The batch number, entity number, last arrival date, and location name are reset.
- The status of the purchase order is set to the same as it was before the arrival reporting. If the purchase order is of the type subcontract, the reporting of the manufacturing operation is also undone.
- Linked manufacturing orders and purchase orders will be reset to their original mode.
This means that no signs of the initial arrival reporting can be seen (except for in the stock transaction log).
Warehouse and stock orders
You can only see and undo arrival reporting in one warehouse at a time. Warehouse is selected by using the button Warehouses ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure.
You must undo arrival reporting of stock orders in this receiving warehouse before you can undo the corresponding delivery reporting of the linked stock orders in the sending warehouse.
Example: Three entire order rows on a stock order have been delivery reported and then one of the order rows has been arrival reported. Then you cannot undo the delivery reporting. In this case, the arrival reported order row must first be undone in the receiving warehouse. This is made in this procedure. After that you can undo the entire delivery reporting in the sending warehouse. This is made in the Undo delivery reporting procedure.
This means that you can only undo a delivery reporting as long as all parts included in the delivery are in transit (being transported) between the warehouses.
List types

#### Undo arrival reporting
This list loads arrivals that can be undone.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
