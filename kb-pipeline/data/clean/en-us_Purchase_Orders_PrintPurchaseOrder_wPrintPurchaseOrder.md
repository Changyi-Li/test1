## Print purchase order
In this procedure you can print:
- Purchase orders for material purchases.
- Stock orders for purchase*.
- Subcontract purchase orders.
- Delivery notes for subcontracts.
- Delivery notes for return orders.
- Pro forma Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees. invoices for stock orders.
What to print is selected as list type and in the settings you can make further choices which will specify the printouts.
> * Stock orders are available if you have installed the option Warehouse.
Purchase orders are created in the procedures Register purchase order and Register stock order – Purchase. In these procedures you can also preview and print the purchase orders that have been registered. If you use the list Delivery note (subc.), you can do the same with delivery notes.
All selections you make are used to load entire purchase orders, not individual rows.
You can preview the documents prior to printing. The documents can be printed or sent by e-mail. After that, you can approve the printout or reprint it.
> You can select by status in order to print orders in different status modes. If you select status Printed, you can reprint the order.
List types

#### Purchase order
This list type loads new purchase orders for printout. By default, this applies to orders with status 1 (Registered).

#### Delivery note (subc.)
This list type loads delivery notes for subcontracts for printout. By default, this applies to orders with status 1 (Registered).

#### Modified purchase order
This list type loads purchase orders that have been modified after their most recent printout. The purchase order is regarded as "modified" if quantity or the delivery date on order row has been changed, or if new order rows have been added. By default, this applies to orders with status 1 (Registered), 2 (Printed), and 5 (Partial delivery made). After the printout has been approved, the printout will be reset. This means that you cannot print and approve a modified purchase order more than once. A modified purchase order is a separate document where the modifications are displayed in red text. The text MODIFIED ORDER is also shown as a watermark on the document, below the order rows. If this text should be shown or not is determined by a document setting found in the Document settings procedure.

#### Delivery note – Return order
This list type loads delivery notes for return orders for printout.

#### Pro forma – Return order
This list type loads pro forma invoices for return orders for printout.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
