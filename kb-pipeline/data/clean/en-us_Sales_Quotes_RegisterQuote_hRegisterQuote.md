### Header row

#### Quote number
In this field you enter a new quote number or you load an existing one using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature. The quote number field is alphanumerical and can contain a maximum of 15 characters. You can also create a new quote by not entering a quote number. When you save the quote, the system will then pick a new number from the number series.
If you manually enter a quote number, the system will check if the entered number already exists, and in that case it will load the existing quote.
A new record is highlighted by a green dot ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) shown in the field. This dot will disappear when the record is saved for the first time.

#### Order type
Here you select order type, in this case one of the different quotes. It is determined by the system setting called Default order type. If you chose the According to user option in the system setting, the order type suggested here will be the order type you have as default in your user account. If you have not configured a default order type there, the order type you used on the most recent quote will be suggested instead. It is possible to select another order type, when needed.
If you selected None in the system setting called Default order type, you cannot save the quote until you have selected an order type.
The Quote order type is included in the system. Other order types must be registered in the Order types procedure. The order type determines price strategy, posting group, rate type, document structure (per language), and the priority. By using the Change order type button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can change the order type for an existing quote.

#### Status
Here you see the status of the quotes illustrated with a symbol. A tooltip displays the status in text.

#### Customer
Here you select the customer to load from the customer register. When you open the procedure, the cursor is automatically positioned in this field. It is mandatory to have a customer on a quote. This field is empty the first time you open the procedure. The next time you open the procedure, you will see the customer number that you used the last time. When you have selected a customer number, the customer name will be displayed to the right. By using the button Change customer ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can change customer for an existing quote.
If the customer is blocked for registration you will see the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png), and using it you can see the cause of the block. In that case, it is not possible to create a quote for the customer.
If a notification has been configured for the customer you will see the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png), and using it you can view the message/notification. It is possible to create a quote even though there is a message on the customer.

#### Customer's inquiry number
This is a field for the customer's inquiry number. A check is made to see if existing quotes for the customer in question, have the same inquiry number. If this is the case, a message will appear and you can go to the existing quote with that inquiry number. However, it is possible to create quotes that have the same inquiry number for the customer.
