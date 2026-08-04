## Undo work recording
> You should only use this procedure if you want to undo work recording items where traceable material has been reported. In other cases you should use the procedure Authorize/Adjust recording.
It is only possible to undo work recording on manufacturing orders with status 1–4. It means that for these orders an adjustment should be made so a different work item should be added instead of the work recording item which you undo in this procedure. This adjustment can be made in the Authorize/Adjust recording procedure.
You cannot undo reporting items where the reported balance has already been consumed, e.g. for a delivered customer order. This applies to all kind of consumption, not only customer orders. Also, you cannot undo reporting items made in the Manufacturing module. For such reporting items you should use the procedure Undo reporting.
The following will take place when you undo a work recording item:
- Counter items are created in the stock transaction log and the manufacturing order log which resets the stock balance on part nodes and material.
- All log records which were created by the recording item become deleted except for the recording item on the person, this is not deleted.
In the procedure Manufacturing order log (in the Manufacturing module), you can via a setting choose to show undone recording items. This also includes work recording items undone in this procedure and adjustments made in the procedure Authorize/Adjust recording.
Warehouse
You can see and undo reporting items in multiple warehouses. You select which warehouses you want to see by using the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure.
List types
There is only one list type in this procedure. This is used to undo work recording.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
