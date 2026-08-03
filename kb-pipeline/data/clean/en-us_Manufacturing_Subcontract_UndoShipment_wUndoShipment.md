## Undo shipment
In this procedure you can undo already made shipments of subcontract purchase order. If multiple shipments have been made, you can undo any of them.
You can undo a shipment as long as the subcontract purchase order has not been arrival reported in the Report arrival procedure (in the Purchase module).
Arrival reporting made on the subcontract purchase order can be undone in the Undo arrival reporting procedure (also in the Purchase module), as long as the invoice basis has not been linked to a supplier invoice. However, it is not possible to undo an arrival reporting of subcontract purchase order if the manufacturing order has been given status 9.
If the option Warehouse is used, the list displays subcontract purchase orders from the warehouses from which you have chosen to show records via the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png).
The following will take place when you undo a shipment:
- The records in the stock transaction log will be deleted so that the material’s stock balance is reset while counter items are created in the manufacturing order log.
- Reported quantity and remaining quantity of the material will be changed back.
- Shipped quantity and quantity at subcontractor for the operation will be changed back.
- The status of the operation will be reset.
This means that no signs/trace of the initial shipment can be seen (except for in the manufacturing order log).
In the procedure Manufacturing order log you can with a setting select to also show undone reporting items in the list. With that setting activated. undone shipments will also be shown.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
