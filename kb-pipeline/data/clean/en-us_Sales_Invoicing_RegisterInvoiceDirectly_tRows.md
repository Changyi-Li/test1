### The Rows tab
The invoice rows contain the same information as the customer order rows under the [Rows](../../Orders/RegisterCustomerOrder/tRows.htm) tab of a customer order. However, there is one difference and that is described below.
It is possible to use both positive and negative quantity of parts. However, the total value of the invoice is not allowed to be negative if it is a debit invoice. A part row with a negative quantity can only be added if the customer order has the status “Final delivery made”.

#### Affect balance
If you check the box Affect balance on an invoice row with row type 1, this will immediately affect the stock balance when registering the invoice basis. You can then also select locations for withdrawals of the part on the invoice row.

#### Location
If the part on the row has been marked to affect the stock balance, you can under the button Loc. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) select from which location the part should be delivered. In the location window you see the name of the location, the disposable balance, and the delivered quantity. The unit for balance and delivered quantity is the same as the part's unit on the invoice row.
If the part has traceability on batch level you will also see batch number, best-before date, and charge number. If the part has traceability at serial number level you will also see the serial number. When the part has traceability at batch level you enter the quantity to deliver from one or several locations with batch numbers. If the part has traceability at serial number level you enter 1 in quantity to deliver per serial number. You can enter it on one or multiple locations with serial numbers. It is not possible to deliver more parts with traceability than what the disposable balance per location allows. For parts with traceability, negative balance is not allowed.

#### Actual delivery date
If you create a new invoice and add a new invoice row, today's date will be suggested as actual delivery date and planned delivery date. (The planned delivery date is by default found under the More info button and is called Delivery date.) If you create a new row where there is a row above, then the same date will be suggested on the new row as on the above row. But this can be changed.
If the actual delivery date is in the future, you will be shown a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) about this in the field.

#### Blanket order
If there is blanket order registered for the customer and part, the button Blanket order becomes activated. Under this button you can find information about the blanket order. The information shown is the blanket order’s order number, validity trough, initial quantity, called quantity, remaining quantity, and blanket order status. You can disconnect the blanket order from the invoice basis row using the Disconnect blanket order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) in the toolbar.
> What to consider when disconnecting blanket order from invoice basis: The price each on the invoice basis row will be updated according to the part’s price. The price each on the linked customer order row will be updated according to the part’s price. Other invoice basis rows created from the customer order will also be disconnected, but price each will not be changed on those rows.
More info
Most of the columns accessed via the More info button are the same as in Register customer order, but the information that differs is described below.

#### Delivery date
The Delivery date column refers to a planned delivery date. If the delivery date is in the future, you will be shown a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) about this in the field.
> If you use stock accounting or management accounting, a warning or a block can be shown if the delivery date belongs to a closed period. This is decided via the system setting called Check open accounting period during order reporting.
