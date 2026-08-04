### Header row

#### Order number
In this field you enter a new order number or you load an existing one using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature. The order number is alphanumerical and can contain a maximum of 15 characters.
If you do not enter an order number, the system will assign a new order number from the number series when you save the order. If you enter an order number manually, the system will check if the entered number already exists, and in that case, it loads the existing order.
A new record is highlighted by a green dot ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) shown in the field. This dot will disappear when the record is saved for the first time.

#### Order type
In this field you see the stock order type. It is determined by the system setting called Default order type. If you chose the According to user option in the system setting, the order type suggested here will be the order type you have as default in your user account. If you have not configured a default order type there, then the order type you used on the most recent order will be suggested. When needed, it is possible to select another order type. By using the Change order type button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change the order type for an existing order.
If you selected None in the system setting called Default order type, you cannot save the order until you have selected an order type.
The linked stock order for sales will get the order type that is linked to the order type you select here.
By using the Change order type button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change order type. This is possible as long as you have not saved. When you save, the linked stock order is also created for sales.
The order type Stock order is included in the system. If you want to add more order types to stock order for sales, this is made in the Order types procedure. The order type determines the priority as well as if the stock order should be included in the purchase statistics.

#### Status
Here you see the status of the customer order illustrated with a symbol. A tooltip displays the meaning of the icon in text.

#### Supplier
Here you select a supplier (sending warehouse) from the supplier register It is mandatory to have a supplier on a stock order. This field is empty the first time you open the procedure. The next time you open the procedure, you will see the supplier number that you used the last time. You can only select among the suppliers that are registered as "internal" suppliers, that is, warehouses. The selected supplier must also be linked to a warehouse. This is configured for the warehouse in the Company information procedure. When you have selected a supplier number, the supplier name will be displayed to the right. By using the button Change supplier![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change supplier. This is possible as long as you have not saved. When you save, the linked stock order is also created.
If the supplier is blocked for registration, a message will appear where you can see the cause by using the button Show block cause ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png). In that case, it is not possible to create an order for the supplier. If you for the supplier have selected Notify (Block/Notify), you will see the message/notification by using the button Show messages ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png). In that case it is still possible to create an order for the supplier.

#### Sending warehouse
Here you see to which warehouse the internal supplier on the order is linked.

#### Linked customer order
When the stock order for purchase is saved, a stock order for sales (customer order) is created in the sending warehouse and will be linked to this stock order. Here you see which customer order number it was assigned. By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can open the order in question in the Register stock order – Sales procedure. The linked customer order number corresponds to Your order number on a regular purchase order.
