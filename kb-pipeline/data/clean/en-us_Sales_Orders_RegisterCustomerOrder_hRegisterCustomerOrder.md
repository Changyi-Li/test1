### Header row

#### Order number
In this field you enter a new order number or you load an existing one using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature. The order number is alphanumerical and can contain a maximum of 15 characters.
If you do not enter an order number, the system will assign a new order number from the number series when you save the order. If you enter an order number manually, the system will check if the entered number already exists, and in that case, it loads the existing order.
A new record is highlighted by a green dot ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) shown in the field. This dot will disappear when the record is saved for the first time.
If the order number is linked to a case, the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridConnectImage.png) next to the field will be available. By using this button you can open the case in question in the Register case procedure.

#### Order type
Here you select the type of customer order. It is determined by the system setting called Default order type. If you chose the According to user option in the system setting, the order type suggested here will be the order type you have as default in your user account. If you have not configured a default order type there, then the order type you used on the most recent order will be suggested. When needed, it is possible to select another order type. By using the Change order type button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change the order type for an existing order.
If you selected None in the system setting called Default order type, you cannot save the order until you have selected an order type.
The order type New sales is included in the system. Other order types that you need must first be registered in the Order types procedure. The order type determines price strategy, posting group, delivery address of linked purchase order, if delivery planning is applied, if preliminary pick list is applied, payment terms, rate type, credit period, invoice type, payment method, sales statistics, preliminary customer order, and priority.

#### Status
Here you see the status of the customer order illustrated with a symbol. A tooltip displays the status in text.

#### Customer
Here you select the customer from the customer register. When you open the procedure, the cursor is automatically positioned in this field. It is mandatory to have a customer on a customer order. This field is empty the first time you open the procedure. The next time you open the procedure, you will see the customer number that you used the last time. When you have selected a customer number, the customer name will be displayed to the right. By using the button Change customer ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change customer for an existing order.
If the customer is blocked for registration of order, a message will appear where you can also see the cause of the block. In this mode, it is not possible to create an order for the customer. If a notification has been configured for the customer you will see the message/notification, but you can still create an order for the customer. You can reopen the message by using the button Show message ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Customer's order number
In this field you can enter the customer’s order number. A check for that order number will then be made for existing orders on the customer. A dialog is displayed if another order registered for the customer already has the entered Customer’s order number. In that dialog you can select to go to that order instead. However, it is possible to create several customer orders containing the same Customer's order number.
If the customer order created at transfer from a delivery schedule, then the customer's order number is normally already loaded The customer’s order number is also seen on the order rows. Using a setting on the delivery schedule type, you decide if the customer's order number is transferred only to order rows or to both order rows and order header.

#### Quote number
In this field you see the quote number if the customer order in question has been created from a quote. You can link/go to the quote using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png).

#### Order date
Today's date is entered by default in this field, but it can be changed. By default, the rows gets the same date as the order date in the header.

#### EDI
By clicking the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see the EDI information in question.
In the EDI connected field it says Yes if the customer on the order is connected to EDI, otherwise it will read No. The default value is loaded from the customer. When the customer is connected to EDI, it is possible to use the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button next to the field to see which EDI transaction types and directions that apply for the customer in question.
If the customer is connected to EDI, it is possible to send the order confirmation via EDI. This is done by using the Send via EDI button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_send_edi.png) which is then available on the procedure toolbar. It is also possible to by default send the order confirmation via EDI when the printout is approved in the Print customer order procedure. When the order confirmation is sent, it is done according to the EDI behavior to which the customer is linked. This can be monitored in the procedure called Manage EDI transactions.
If the customer is connected to EDI, you can with the Exclude from EDI setting decide if the order in question should be excluded from the EDI flow. This means the order confirmation cannot be sent via EDI, not from here and not from the Print customer order procedure. The Send via EDI button will then also be deactivated.
You can also see the EDI Export status for the order showing date and time for the export.

#### Delivery progress
Here you see the delivery progress of the customer order. This is an icon consisting of arrows, representing how far the order has come based on the status of the phases. A phase can have the following statuses: Not started, Started, and Finished. The delivery process/progress shows one arrow per phase and one colors for each status. That way, it is easy to see what the situation is like for the customer order. Steps that you are not using, for example packing, will remain not filled.
The five phases represent:
- Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. created
- Picking
- Packing
- Shipping
- Delivery
Each phase can have three modes:
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_1.png) – the phase is not started.
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_2.png) – the phase is started.
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_3.png) – the phase is finished/completed.
