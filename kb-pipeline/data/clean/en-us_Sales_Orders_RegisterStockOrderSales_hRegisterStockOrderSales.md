### Header row

#### Order number
In this field you enter a new order number or you load an existing one using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature. The order number is alphanumerical and can contain a maximum of 15 characters.
If you do not enter an order number, the system will assign a new order number from the number series when you save the order. If you enter an order number manually, the system will check if the entered number already exists, and in that case, it loads the existing order.
A new record is highlighted by a green dot ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) shown in the field. This dot will disappear when the record is saved for the first time.
If the order number is linked to a case, the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridConnectImage.png) next to the field will be available. By using this button you can open the case in question in the Register case procedure.

#### Order type
In this field you see the stock order type. It is determined by the system setting called Default order type. If you chose the According to user option in the system setting, the order type suggested here will be the order type you have as default in your user account. If you have not configured a default order type there, then the order type you used on the most recent stock order will be suggested. It is possible to select another order type, when needed.
If you selected None in the system setting called Default order type, you cannot save the order until you have selected an order type.
The linked stock order for purchase will get the order type that is linked to the order type you select here.
By using the button Change order type ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can change order type, as long as you did not save when the linked stock order for purchase was created.
The order type Stock order is included in the system. If you want to add more order types to stock order for sales, this is made in the Order types procedure. The order type determines price strategy, the purchase order's delivery address, whether or not delivery planning should be applied, which order type for purchase that the link should be made to, if to apply automatic arrival reporting, priority, and if stock order should be included in the sales statistics.

#### Status
Here you see the status of the stock order illustrated with a symbol. A tooltip displays the status in text.

#### Customer
Here you see/enter the customer (receiving warehouse) from the customer register. It is mandatory to have a customer on a stock order. This field is empty the first time you open the procedure. The next time you open the procedure, you will see the customer number that you used the last time. You can only select among the customers registered as "internal" customers, that is, warehouses. The selected customer must also be linked to a warehouse. This is configured for the warehouse in the Company information procedure. When you have selected a customer number, the customer name will be displayed to the right. By using the button Change customer ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change customer. This is possible as long as you did not save when the linked stock order for purchase was created.
If the customer is blocked for registration, a message will appear where you can see the cause of the block by using the button Show block cause ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png). In this mode, it is not possible to create an order for the customer. If you for the customer have selected Notify, you will see the message/notification by using the button Show message ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png). In that case it is still possible to create an order for the customer.

#### Receiving warehouse
Here you see to which warehouse the internal customer on the order is linked.

#### Linked purchase order
When the stock order for sales is saved, a stock order for purchase (purchase order) is created in the receiving warehouse and will be linked to this stock order. Here you see which purchase order number it was assigned. By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can open the order in question in the Register stock order – Purchase procedure. The linked purchase order number corresponds to Your order number on a regular customer order.
