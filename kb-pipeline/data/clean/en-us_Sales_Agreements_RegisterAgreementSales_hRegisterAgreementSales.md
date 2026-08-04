### Header row

#### Agreement number
In this field you enter a new agreement number or you load an existing one using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature. The agreement number is alphanumerical and can contain a maximum of 15 characters.
If you do not enter an agreement number, the system will assign a new order number from the number series when you save the agreement. If you manually enter an agreement number, the system will check if the entered number already exists, and in that case, it loads the existing agreement.

#### Order type
Here you see/select an order type for the agreement. The order type you have entered as default for your user will be suggested here. If you have not configured a default order type there, the order type you used on the most recent agreement will be suggested instead. If needed, you can select a different order type. This require you to have multiple order types registered based on the basic type called Agreement. These are registered under the Customer agreement tab in the Order types procedure. By using the Change order type button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change agreement type for an existing agreement, as long it has status 1 (Negotiation).
If you selected None in the system setting called Default order type, you cannot save the order until you have selected an order type.

#### Status
Here you see the status of the agreement illustrated with a symbol. A tooltip displays the status in text.

#### Customer
Here you select the customer from the customer register. When you open the procedure, the cursor is automatically positioned in this field. It is mandatory to have a customer entered on an agreement. This field is empty the first time you open the procedure. The next time you open the procedure, you will see the customer number that you used the last time. When you have selected a customer number, the customer name will be displayed to the right. With the Change customer button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change customer for an existing agreement, as long as it has status 1.
If the customer is blocked for registration of order, a message will appear where you can also see the cause of the block. In that case, it is not possible to create an agreement for the customer. If a notification has been configured for the customer, you will see the message/notification, but you can still create an agreement. You can reopen the message by using the button Show message ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Customer's agreement number
In this field you can enter the customer’s agreement number. A check regarding that agreement number will then be made for existing agreements for the customer. A dialog is displayed if another agreement registered for the customer already has the entered Customer’s agreement number. In that dialog you can select to go to that agreement instead. However, it is possible to create several agreements with the same Customer's agreement number.
