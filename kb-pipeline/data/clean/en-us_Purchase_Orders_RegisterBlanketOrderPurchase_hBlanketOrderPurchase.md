### Header row

#### Order number
In this field you enter a new order number or you load an existing one using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature. The order number is alphanumerical and can contain a maximum of 15 characters.
If you do not enter an order number, the system will assign a new order number from the number series when you save the order. If you enter an order number manually, the system will check if the entered number already exists, and in that case, it loads the existing order.
A new record is highlighted by a green dot ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) shown in the field. This dot will disappear when the record is saved for the first time.

#### Order type
Here you select blanket order type. It is determined by the system setting called Default order type. If you chose the According to user option in the system setting, the blanket order type suggested here will be the order type you have as default in your user account. If you have not configured a default order type there, then the blanket order type you used on the most recent order will be suggested. When needed, it is possible to select another blanket order type. By using the Change order type button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change the blanket order type for an existing order.
If you selected None in the system setting called Default order type, you cannot save the order until you have selected an order type.
The order type Blanket order is included in the system. Other order types that you need must first be registered in the Order types procedure. The order type determines the priority and the order's validity period. By using the button Change order type ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change the order type for an existing order. You can choose if you want to update Priority, VAT code, and Modify "Valid to" when the order type is changed.

#### Status
Here you see the status of the blanket order illustrated with a symbol. A tooltip displays the status in text.

#### Supplier
Here you select a supplier from the supplier register. It is mandatory to have a supplier on a blanket order. It is only possible to select suppliers with the supplier role Material supplier. This field is empty the first time you open the procedure. The next time you open the procedure, you will see the supplier number that you used the last time. When you have selected a supplier number, the supplier name will be displayed to the right. By using the Change supplier button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png), you can also change supplier for an existing blanket order.
If the supplier is blocked for registration, a message will appear where you can see the cause by using the button Show block cause ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png). In that case, it is not possible to create a blanket order for the supplier. If you for the supplier have selected Notify (Block/Notify), you will see the message/notification by using the button Show messages ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png). In that case it is still possible to create an order for the supplier.

#### Supplier's order number
In this field you can enter the supplier’s order number. If the order’s status is 1 (Registered) or 2 (Printed) when you enter the supplier’s order number in this field, the Confirmed box is automatically checked. This checkbox is linked to the order's status and shows that the supplier has confirmed the purchase order.
