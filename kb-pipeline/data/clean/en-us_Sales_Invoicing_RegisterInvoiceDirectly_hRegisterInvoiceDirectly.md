### Header row
The main row in the procedure is the starting point when you create a new invoice basis or when you load an existing invoice basis.
Some of the information and functionality on the header row for the invoice is the same as on the [header row](../../Orders/RegisterCustomerOrder/hRegisterCustomerOrder.htm) in the Register customer order procedure. The information that differs from that procedure is described below.

#### Order number
In this field you select an order number. Only order numbers for existing invoice bases can be selected. Partial delivery numbers (for partial deliveries of the order) are entered with a slash plus the partial delivery number after the order number, for example "100/1". A sub-number is always entered for an order when you create a new basis where you have manually entered the order number. All invoice bases must have a minimum of one delivery that is displayed as "/1" after the order number. If the invoice basis has status 8 (Approved) or 9 (Printed), you can also select order number based on the invoice number created when the invoice was approved.

#### Order type
Here you select the type of customer order. The order type you have set as default in your user account, will here be suggested by default. If you have not configured a default order type there, then the order type you used on the most recent order will be suggested. When needed, it is possible to select another order type. By using the Change order type button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change the order type for an existing order.
The order type New sales is included in the system. Other order types that you need must first be registered in the Order types procedure. The order type determines price strategy, posting group, delivery address of linked purchase order, if delivery planning is applied, if preliminary pick list is applied, payment terms, rate type, credit period, invoice type, payment method, sales statistics, preliminary customer order, and priority.
Order types where Create invoice basis is deactivated cannot be selected in this procedure.

#### Status
Here you see the status of the invoice illustrated with a symbol. A tooltip displays the status in text.

#### Invoice customer
Here you select the customer on the invoice from the customer register. When you open the procedure, the cursor is automatically positioned in this field. If the selected customer has a different Customer number, invoice, then a question will appear where you can choose if you want to change to that customer number on the invoice. If the customer has overdue invoices, a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) will be shown next to the field. In a tooltip shown when you hover over the symbol, this warning is displayed in text as well as the value of the overdue invoices.

#### Complement order
With this checkbox you decide if a supplementary invoice should be made for a previously invoiced customer order. In such cases you check the box and in the Order field you select the order number for which a supplementary invoice should be made. When saving, the invoice basis will get this order number plus a new partial delivery number, provided that the order number was not entered manually.
The rows that you make a supplementary invoice for, will be added on the customer order.

#### Invoice number
The invoice number is displayed here for an existing invoice basis which has been approved for invoicing.
