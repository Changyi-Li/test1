## Register return order
In this procedure you can register return orders for purchase orders as well as print pick lists for return orders. Using the return order feature you can, when needed, return arrival reported purchase order rows to your suppliers.
A return order can be described as basically a purchase order with a negative quantity and it has the order type called Return order.
In the list you can see all arrival reported purchase order rows for the marked supplier and you can create a return order with the entire quantity or a partial quantity, for the purchase order rows you choose to include. It is also possible for you to link a case to each purchase order row included on the return order.
You can include purchase order rows from more than one purchase order on a return order to the supplier. For return orders in the Register purchase order procedure, a text row is automatically created above each returned purchase order row per purchase order. Here you find information about order number, supplier's order number, delivery note number, and arrival date.
When a return order has been created for a purchase order row, more information will be shown on the returned purchase order row in the Register purchase order procedure. You can see the Returned quantity. By clicking the Return order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you find information about return order number, a link to the return order, the supplier's order number, returned quantity, what is left to return, and date of return (that is, the date when the order is expected to be returned).
In the Report arrival procedure you execute the delivery of return orders. When a return order is delivered the stock balance becomes updated and an invoice basis is created. This invoice basis can then be matched with a credit invoice from the supplier.
List types

#### Register return order
This list type is used to create return order.

#### Pick list – Return order
This list type is used to print print pick lists for return order. Please note! These lists are not saved in the database.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
