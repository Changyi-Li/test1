### The Rows tab
This tab shows information registered on the order rows in the Register purchase order procedure.
If you are using the Stock location system option, you can use Open putaway dialog ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StockBalance.png) to receive suggestions about which location the parts should be stored in.
The order rows that can be arrival reported are the ones that are shown in the list in the Orders section. You can enter quantity to arrival report, unit, and location. You can also choose to activate/deactivate Delete remaining, Receiving inspection, or All (used to arrival report all, that is, the entire quantity on the order rows). If you activate the Inspection checkbox (receiving inspection), you cannot enter a location, but instead, you can enter a goods location. For subcontract order rows, you can also enter price and setup price.
For purchase orders of the type Buy material, you can also add new order rows to arrival report. If you add a new order row, you can for that row select row type 1, 2, or 4. For row type 1, you must select a part number. For row type 2, you must enter a name. For row type 4, you can enter an additional text and a text type, but it is not mandatory. Order rows added here will also be added to the purchase order.
On purchase orders of the Subcontract type, you can add freight rows and packaging rows in connection with the arrival reporting.
On purchase orders of the Stock order type (option), it is not possible to add new order rows in connection with the arrival reporting.
On purchase orders of the Return order type, it is only possible to add row type 4, text rows.

#### Arrival reported quantity
Here you enter the quantity that should be arrival reported on the order row.
If the setting Suggest remaining quantity is activated in the Selection tab, you will here see the entire remaining quantity of the order row.
If it is a subcontract, the default quantity is also determined by the setting Suggested quantity for subcontract.
If it is a stock order, the default quantity is also determined by the setting Suggested quantity for stock order.
If it is a return order, you can only arrival report a negative quantity, that is, the arrival reporting will be a "delivery" for return to the supplier.
If the part has multiple locations, you can enter a quantity to arrival report per location in the Location box. There you also enter batch number per location if the part has traceability at batch level. If the part has traceability at serial number level, you must enter the arrival reported quantity as well as serial number per location and entity in this box. Read more about the [Location](bLocation.htm) box.

#### Unit
The default unit for the part is the unit selected in the part register, the Usage button, to be used when arrival reporting, but it can be changed.

#### Delete remaining
Indicates that the remaining quantity on the order row will be deleted. This check box is only shown if you have entered a quantity to arrival report, and if the row still has a remaining quantity
If you delete rest on the order row, the underlying alloy cost rows will also be deleted.
If the order row belongs to a stock order (option) for purchase, this checkbox is only shown if you have chosen to arrival report the entire quantity that has been delivery reported in the sending warehouse (in transit) and if the row still has a remaining quantity. If you delete the remaining quantity on the order row, then the remaining quantity on the corresponding order row on the linked stock order for sales will also be deleted.
It is not possible to delete remaining quantity for return orders.

#### Receiving inspection
In this column you can determine if the order row should be subject to receiving inspection. This is activated by default if receiving inspection has been configured for the part, supplier, or order. You can also activate receiving inspection for the particular arrival on the order row.
For a subcontract that has a measuring plan, the checkbox for receiving inspection will be automatically activated.
Receiving inspection cannot be activated for return orders.

#### All
If you activate the checkbox All, it means that the entire quantity in the Remaining quantity column will be arrival reported automatically.

#### Goods location
You can enter a goods location for the rows where receiving inspection is activated and for rows with subcontract where it is not the final operation of the manufacturing order. The goods location is a temporary location for arrived goods waiting to be receiving inspected or to be otherwise handled in the manufacturing. You can enter a maximum of 40 characters for goods location.

#### Customer order/Manufacturing order/Stock order
If the purchase order row is based on a customer order/manufacturing order/stock order, you will here see the order number in question. That is, the customer order, manufacturing order, or stock order that causes the requirement of this purchase order row. The position is shown after the linked order number.
This does not apply to return orders.

#### Stock count request
Stock count request is mainly used if you find that the stock balance does seem to add up and you wish to signal this in Monitor ERP. When you activate this checkbox, today's date and the time will be set in the Request date field.
The parts for which there is a stock count request can be shown in the Create stock count basis list in the Stock count in list procedure. This is done by activating the Include requested stock counts setting. You can also select by Stock count request date. The list also displays the comment. When the stock count has been performed and saved for the part, the field and the comment will be cleared.

#### Request comment
If you have checked the Request comment checkbox, you can here add a comment regarding the cause of this request.
