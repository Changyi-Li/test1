## Pack for delivery
You use this procedure if you apply packing in Monitor ERP. Here you get an overview of what there is to pack from a pick list, and you can add, delete, and move packages in the package structure, as well as save the pick list. Here it is not possible to create a new pick list or to delete a pick list.
All packing events are based on pick lists created via the list type Picking plan in the Delivery planning procedure. You can pack based on both preliminary and regular pick lists. You the do the delivery reporting in the Report delivery procedure. The packing is done between the delivery planning and the delivery reporting.
By clicking the Create shipment button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_shipping.png) on the toolbar of the procedure you can create a shipment for the saved pick list in question, which will then open in the Register shipment procedure will information from the package structure already entered.
When you have loaded a pick list number, you will under the Package tab see the parts that should be packed and which packaging parts that are linked to the parts.
You can also see all packaging parts that exist in the part register and then use the "drag and drop" function to add more packaging parts in the package structure. It is also possible to add more packaging parts directly in the package structure. You can move packages and their related parts up and down in the structure. You can move a package and its related parts in under a different package. For example, you can add a pallet and you can then move in your existing boxes to it.
You can also add more of the parts to pack in the package structure. To do this, use your mouse pointer to "drag and drop". This is useful if you, for example, want to add packaging parts there to distribute the number of parts to pack to additional packages.
At the bottom of the package structure there is a total with different information about the packages and parts.
All boxes under the Package tab are possible to unpin to separate windows by using the Floating button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_float_window.png) (Ctrl + U). This can be done to get a better overview if there many parts in the pick list and large package structures.
Under the Document tab you can preview and print pick list, pack list, transport label with package structure, and transport label, sales.
> The order rows included in a pick list will remain in the "under picking" status for the entire picking process.

#### Packing rules
In the Packing rules procedure you can create packing rules and link customers or order types. The packing rules determine if and how packaging parts should be added as delivery rows when delivery reporting. Packing rules also determine if multiple delivery notes should be allowed per pick list or if this should result in a warning. You can also use packing rules to manage a check to see if packaging rows are completely missing in pick lists when delivery reporting. The result of the check can be a warning or a block for reporting the delivery.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_log.png)
Additionally, there is a log called Printed by ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_log.png) which shows the name of the person or user that printed the pick list.
> To be able to use the packing function, all required packaging parts must first have been registered in the Part register procedure. For both packaging parts and regular parts sold, you must update shipping information and net weight. This should also be done in the part register.

#### Packing of fictitious parts
It is possible to add fictitious parts in the package structure. When a fictitious part is added in a package, the fictitious part will be included together with its sub-levels.
- Underlying rows cannot be packed separately.
- If you move the fictitious part, it also means that the underlying levels are moved.
- Clearances are made on the underlying levels.
- The clearances must match the defined multiple value for the relation between the fictitious part and its sub-levels/underlying levels.
