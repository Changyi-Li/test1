## Delete parts
> Only a few employees should be authorized to use this procedure since changes made here are extensive.
If you need to delete multiple parts at a time in the database, or if you want to deactivate them, you can use the Delete parts list in this procedure for this action. Individual parts can also be deleted/deactivated in the Part register procedure.
You select parts based on different terms and you can choose to pre-select these parts to be included in a deletion check in the list.
The deletion check is run for each marked part in the list. It checks if the part can be deleted or deactivated. This is the same check as is made if you deleted individual parts in the Part register procedure. This check goes trough all registers where there may be dependencies to the parts. This can, for example, be that the parts are used in active orders, BOM and routing, or if they have a stock balance.
When the check has processed all parts you have marked to include, you will see the parts that can be deleted, the parts that cannot be deleted, and the parts that can be deactivated.
You delete and/or deactivate the parts marked to be included, by first clicking the Delete/Deactivate selected parts button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png) on the function menu. After that you execute the deletion/deactivation by using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) in the procedure.
> Inactive parts: Inactive parts are not shown in the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature in part number fields. It is possible to load inactive parts in part number fields if you enter the entire part number. It is not possible to change any information for inactive parts. The inactive parts are blocked regarding registration and reporting on new quotes, customer orders, inquires, purchase orders, manufacturing orders, BOM and routing, new serial number/batch number, options in configuration, and customer agreements. Inactive parts can be displayed in this list if you activate the Show inactive parts setting. Please note! When you deactivate a part it means BOM and routing will be deleted and these will not be restored if/when you reactivate the part.
List types

#### Delete parts
In this list you can delete/deactivate parts.

#### Reactivate inactive parts
This list can be used, if needed, to reactivate parts which have earlier been deactivated. You can configure which part status should be entered for the parts you reactivate.
