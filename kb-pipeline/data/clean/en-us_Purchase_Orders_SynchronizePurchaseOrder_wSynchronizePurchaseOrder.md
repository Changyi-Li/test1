## Synchronize purchase order
> It is not possible to synchronize stock orders in this procedure.
In this procedure you can check and update purchase orders and purchase order rows with new data from, for example, the supplier register, part register, posting matrix, and VAT settings. This can concern information such as currency, supplier group, and VAT group in the purchase order header, and for example posting on purchase order rows.
- To be able to update a purchase order, the order status must be lower than 9.
- To be able to update a purchase order row, it must have a remaining quantity greater than 0.
> Please note! If you change the part's conversion factor, the quantity on the purchase order row will also change based on the new conversion factor. This applies if the order part on the order row has an alternative unit.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
