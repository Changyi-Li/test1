## Report delivery
In this procedure you report deliveries of customer orders and stock orders for sales. You can select any orders to delivery or deliver orders via pick lists. This is determined by the selected list type. Stock orders for sales are available if you have installed the Warehouse option.
Delivery reported customer orders are updated on row level and new status is set on the order depending on if a partial delivery or a delivery in full has been made. Read about [using partial delivery](../../Customers/CustomerRegister/bDeliveryShipping.htm#Delleverans).
When the delivery is saved in this procedure, an invoice basis is created for delivered order rows and packaging.
You can then print/e-mail the documents called Delivery note, delivered and Transport label, sales from this procedure. This is done under the Documents tab. It is also possible to print these documents separately in the Print delivery documents procedure. Shipping information is automatically calculated for the delivered quantity. You can also send advice via e-mail.
From the Result box found under the Documents tab, you can also create a shipment for the orders or pick lists which have been marked to include. A shipment draft with all of the information pre-filled is then created in the Register shipment procedure.
As long as the invoice concerning the delivery has not been printed, the delivery can be adjusted, either by reporting delivery of an additional quantity or by undoing the delivery in the Undo delivery reporting procedure. When additional quantity is reported, a new invoice basis will be created.
If an order row you deliver is linked to a manufacturing order, the manufacturing order will get status 5 (Partial delivery made), but only if it had status 4 (Finished) before the delivery.
You can send delivery documents and/or shipment advice via e-mail.
Delivery of order with invoicing plan
For orders that have an invoicing plan, the following applies for delivery reporting. Only delivery rows can be reported in this procedure. The deduction is always made in proportion to the delivered value.
Advance rows and In arrears rows are not handled in this procedure. These should instead be delivered by release in the procedures Register customer order or Invoicing plan list. The deduction of advances and in arrears is always made in proportion based on the delivered portion of the invoicing plan.
There is a setting under the Invoicing plan tab in the Register customer order procedure called Check for unpaid advance invoices at delivery. This setting can either be set not to check, or to warn or block. If it is configured to warn, a warning will be displayed if the advance has not been paid in full, but it will still be possible to deliver. If the check is configured to block deliveries, an error message will be displayed and it is not possible to delivery report. This check applies to both list types.
> Please note! Rows which you add during the delivery reporting will no be included in the invoicing plan, and will also not be included in the deduction of advance and in arrears.
Delivery of stock order
If the customer order is a stock order (functionality included in the option Warehouse) and its order type has Automatic arrival reporting activated, then the Report arrival procedure will open after you have reported a delivery of a quantity on the customer order. In that procedure the linked purchase order is loaded, and you can then choose to directly report arrival of the delivered quantity. The arrival is then made in the purchase order's warehouse.
Delivery of order with total rows
If all order rows in the total are ready for delivery, then the name of the total row is show as usual. If any of the order rows in the total is not ready for delivery, a warning will appear on the total row. If you excess report or report less on order rows included in a total row, then the price on the total row will be updated on the invoice. The total row will not be set to "final delivery made" until all included/linked rows have been final delivered.
Partial delivery of included parts in fictitious part
You can perform partial delivery of included parts in a fictitious part. A tip is to check the document setting called Show included parts in fictitious for the documents "Delivery note" and "Delivery note, delivered" in the Document settings procedure. This way the included/incorporated fictitious parts will be shown on the documents, otherwise only the main part will be shown, that is, the fictitious part on the documents.
If you only deliver sub-rows for the fictitious part, the invoice basis will be set to status Pending. Both the invoice basis and the customer order will be invoiced via the comprehensive invoice Per order. Invoicing should be done together with the fictitious part not to cause problems in the management accounting.
This applies if the system setting called Fictitious part with price on customer order/quote has been set to Yes.
Delivery with customer order transfer
When the Customer order transfer option is installed, rows which are added at delivery reporting can automatically be transferred to the receiving company. This makes it easier when you, for example, add freight and packaging in the production company, to transfer it to the sales company.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the toolbar, you can include orders from the result under the Documents tab to the Handle transfers procedure. This applies to orders containing order rows that have a transfer profile.
> Please note! If you use customer order transfer in combination with invoicing plans it means the customer order transfer will not take any invoicing plan on customer order in the sales company, into consideration. If the invoicing plan, for example, contains an advance which has to be paid before any delivery can be made, this type of information (a warning or a block) will not be included to the production company. The production company can therefor deliver to the customer even though the advance has not been paid.
List types

#### Free selection
You use this list type if you wish to freely select which orders to delivery report among the orders that are ready for delivery.

#### Via pick list
Select this list type if you wish to deliver via selected pick lists. You also use this list type if you apply packing in Monitor ERP. Packing is a step which takes place between the delivery planning and the delivery reporting.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
