## Undo reporting
In this procedure you can undo reporting items for manufacturing order which have been made in any of the reporting procedures in the Manufacturing module. It is inly possible to undo reporting of orders with status 1–4.
Undoing reporting in the procedure covers own operations, material, and rejections on part nodes in order structures. You can only undo whole reporting items. It is not possible to select separate operations or material to undo in a reporting, if there are more than one. For example, if 3 operations and 10 material items were reported in the same reporting item, you will undo all 3 operations and all 10 materials.
You undo one reporting item at a time on the same manufacturing order. It does not have to be the most recent reporting. It might as well be an earlier reporting.
It is always possible to undo reporting of operations without linked material and which does not result in transfer to stock. Operations without quantity reporting are also always possible to undo (that is, only reporting of time). You can undo reporting of operations with linked material without traceability. Reporting of material without traceability can always be undone.
However, you cannot undo reporting where the reported balance has already been consumed, e.g. for a delivered customer order. This applies to all kind of consumption, not only customer orders. If the balance of the part which was arrival reported in the reporting item, has already been consumed in a higher part node, then it is not possible to undo the underlying reporting. The location that had affect on balance (transfer to stock) when reporting, must primarily have a balance that is enough to undo the reporting. If the order number does not exist on the location anymore, the part must have a total balance that is enough to undo the reporting.
If it is not possible to undo a reporting item, this is shown in the Reporting box with a block symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) and an explanatory text in a tooltip when you hover over the symbol.
> Please note! If you have undone one or multiple reporting, the part node's status and the order's status will not be reset. You can manually change the status back by using the Change status button on the order in the Register manufacturing order procedure.
Undo reporting items in the Recording terminal
If there are reporting items made via work recording in the Recording terminal procedure (in the Time recording module), then you must undo these in the procedure Undo work recording (also found in the Time recording module).
Undo subcontracts
If there are reported subcontracts that you want to undo, you must use the procedure Undo arrival reporting (in the Purchase module) to undo arrivals of the subcontracts' purchase orders.
Traceable material
If you undo reporting items containing traceable material, then the material will be returned to the same mode as before the reporting. But you have to undo the reporting items in the correct order. Serial number A serial number is a number that is used for traceability for parts on entity level./batch created at the reporting, and which are not used in any other cases, will be deleted when you undo the reporting.
You cannot undo withdrawal of traceable material linked to a main part with traceability at serial number level, when transfer to stock has been reported on the main part. That is, if a quantity of the main part has been reported as finished on the final operation (when transfer to stock takes place) and there is traceable material linked to the main part's node, then you cannot undo reporting of these material withdrawals.
When an operation is finished it is also not possible to undo only withdrawal of material, if the material has batch traceability. First you must undo the operation so it does not have zero as remaining quantity. This is because it is not allowed to report an operation for a traceable part as finished when there is remaining material with traceability.
Warehouse
You can see and undo reporting items in multiple warehouses. You select which warehouses you want to see by using the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure.
The following will take place when you undo a reporting item:
- Counter items are created in the stock transaction log and the manufacturing order log which resets the stock balance on part nodes and material.
- The batch number and serial number will be reset.
- The reported quantity, remaining quantity, and actual finish date of the nodes will go back to the quantity and date that applied before the reporting.
- Linked manufacturing orders and purchase orders will be reset to their original mode.
- The actual finish date in existing serial numbers that was updated in the original reporting, is now moved back to the date that applied before the reporting.
This means that no signs/trace of the initial reporting can be seen (except for in the stock transaction log and the manufacturing order log).
However, in the procedure Manufacturing order log you can with a setting select to show undone reporting items.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
