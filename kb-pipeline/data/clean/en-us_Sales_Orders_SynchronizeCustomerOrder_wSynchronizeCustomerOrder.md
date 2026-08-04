## Synchronize customer order
> It is not possible to synchronize stock orders in this procedure.
In this procedure you can check and update customer orders and customer order rows based on new data in for example the customer register, part register, posting matrix, and VAT settings. The data might be e.g. currency, customer group, VAT group, and project in the customer order header. And on the customer order rows it might be data such as price each, discount, setup price, and posting.
- To be able to update a customer order, the order status must be lower than 9.
- To be able to update a customer order row, it must have a remaining quantity greater than 0.
- Customer orders with status 4 (Picking in progress), cannot be synchronized since clearance has been made by printing of the pick list (Picking plan) in the Delivery planning procedure.
> The only discount that can be synchronized is discount code 1: Discount, meaning the regular discount. Project discount, order type discount, and discount on discount are not synchronized.
> Please note! If you change the part's conversion factor, the quantity on the customer order row will also change based on the new conversion factor. This applies if the order part on the order row has an alternative unit.
Alloy cost
If prices on the alloy cost have been changed, these will be updated when synchronizing. If quantity or alloy cost has been changed on the part, this will also be updated when synchronizing. This makes it possible to add and delete part numbers when synchronizing.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
