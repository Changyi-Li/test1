## Print manufacturing order
In this procedure you can print two types of documents: manufacturing order documents and transport labels based on orders (not reporting). The list shows the result of the selection and the settings made.
If the status of an order is 1 (registered) and you print a manufacturing order document, the status will be changed to 2 (printed). A printout log will be created for the order.
Warehouse
The warehouse selector works as a filter for which documents should be included in the list:
- For the document Traveler (where all operations in a part node are shown), the selection takes place for the node's warehouse.
- For the document Operation document (where only one operation is shown), the selection takes place for the operation's warehouse. For these two documents the material is included as a whole without selection taking place on the warehouse of the material.
- For the document Material document (where all materials are shown), the selection takes place for the material's warehouse.
- For the document Transport label (which is available for the first operation in each part node) the selection takes place for the operation's warehouse.
List types
There are two list types in this procedure: Manufacturing order and Transport label. You select the manufacturing orders/transport labels you wish to print. For each list type there are different settings. For the Transport label list type there are additional settings you can configure under the Documents tab. The selection you make is shown under that tab when you load the list, and you can choose which documents/ transport labels that should be printed.

#### Manufacturing order
In this list type you will see the manufacturing order documents that are registered in the system.

#### Transport label
This list type shows transport labels based on the orders’ first operations. The purpose of this transport label is to label the pallet before reporting.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
