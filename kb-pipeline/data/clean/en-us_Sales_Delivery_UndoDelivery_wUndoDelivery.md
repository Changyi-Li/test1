## Undo delivery reporting
In this procedure, you can in a list undo delivery reporting made earlier for customer order rows.
When you undo a delivery reporting, the previous logs and data are deleted. In that case, there will be no sign of the previously reported delivery or of the undoing of the delivery.
It Is possible to undo any delivery reporting on each order.
The delivery cannot be undone if:
- The delivery has been invoiced (the invoice basis has status 8 or 9).
Traceable material
If you undo delivery reporting items containing traceable material, then the material will be returned to the same mode as before the reporting, regarding status, balance, etc. Serial numbers/batches created at the reporting which are not used in any other cases, will be deleted when you undo delivery reporting.
The following will take place when you undo a delivery:
- An offset record is created in the stock transaction log which resets the stock balance. The delivery log and the invoice basis will be deleted.
- The batch number and serial number will be reset.
- The status of the customer order will be changed back to the status that the order had before the delivery reporting. Please note that the order can only be changed back to one of the following statuses after undoing a delivery: 1, 2, or 5. If the order had status 4 (picking in progress) before delivery, the order will not be given status 4 if you undo the delivery. The order will instead be given the status that the order had before you created the pick list.
- The serial number created in the original delivery will be deleted. The actual delivery date will be set back for the existing serial numbers that were delivered in the initial delivery.
- Any clearances created from arrivals of linked purchase or manufacturing orders will be reset to cleared.
- Released but not invoiced interest rows, will be deleted from the customer order. The interest rows will be put back on the interest basis list.
This means that no signs of the initial delivery reporting can be seen (except for in the stock transaction log).
Warehouse and stock orders
You can only see and undo delivery reporting of different orders from the selected warehouses. Warehouse is selected by using the button Warehouses ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure.
A delivery reporting of a stock order can be undone in the sending warehouse, as long as a quantity of the parts in the delivery has not yet been arrival reported for the linked stock order in the receiving warehouse.
Example: Three entire order rows on a stock order are delivery reported and then one of the order rows has been arrival reported. Then you cannot undo the delivery reporting. In that case the arrival reported order row must first be undone in the Undo arrival reporting procedure in the receiving warehouse. After this, you can use this procedure to undo the entire delivery reporting.
This means that you can only undo a delivery reporting as long as all parts included in the delivery are in transit (being transported) between the warehouses.
Invoicing plan
If the customer order has an invoicing plan and no delivery of order rows has been made, then you can undo any delivery reporting (of the invoicing plan). As soon as delivery reporting of order rows has been made, you have to undo the latest delivery first, and then the preceding delivery, etc.
When you undo a delivery reporting of order rows included in an invoicing plan, then all rows in the delivery which is included in the invoicing plan will become undone. That is, other order rows included in the invoicing plan and the deduction rows for advances and in arrears, will all be undone. Order rows which are not included in the in invoicing plan can be undone without affecting the in invoicing plan.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
