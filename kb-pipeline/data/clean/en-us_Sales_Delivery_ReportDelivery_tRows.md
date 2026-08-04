### The Rows tab
If you have loaded the list type Free selection, you will here see information from customer order rows. If you have loaded the list type Via pick list, you will here see information both from customer order rows and from pick lists.
The part's Unit, Location, and Quantity to deliver, can be modified. You can choose to delete remaining quantity. Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can also change the Dock – Row, and Storage.
Using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the function menu you can use the link to go to related procedures for the marked row, for example, to change other information on the row.
By clicking the button Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5) you can also add order rows and text rows to deliver. Order rows and text rows added here will also be added on the customer order. If you add a new order row, you can for that row select row type 1, 2, or 4. For row type 1, you must select a part number. For row type 2, you must enter a name. For a new order row of row type 1-2 you can also enter and edit Price each, Setup price, Discount, Standard price, Dock – Row, and Storage. For row type 4 you can enter an additional text, and by clicking a button in the additional text window you can select on which documents (Quote, Order confirmation, Delivery note, Invoice) the additional text should be displayed.
You can use the button Add underlying level ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_subrow.png) (Ctrl + Shift + F5) to insert a sub-row of row type 4 as linked text row to a main row of row type 1 or row type 2. A row of row type 4 (text row) which is not a sub-row to a main row, belongs to the actual order as an unlinked text row. On a text row you can also insert phrase and signature by using the buttons in question.
By using the Shipping info function button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPartiallyShipped.png) you can see and edit the shipping information of the customer order. It is possible to add and delete rows of shipping info.
If it is a fictitious part which is price managed, then it is not possible to add alloy cost for a incorporated part to the fictitious part.
Packaging part rows
If the list type Free selection is selected and the part on an order row has a packaging part linked in the part register, the packaging part will be inserted as delivery row on a sub-row to the order row.
If the list type Via pick list is selected, you can add packaging parts as delivery rows in two different ways. This is determined using packing rules in the Packing rules procedure. Either you insert the packaging parts the same way as when using the list type Free selection, or you add the packaging parts in the package structure from the Pack for delivery procedure on own delivery rows under the order rows. You link customers or order types to packing rules, this means packaging parts can be added in different ways depending on the orders you deliver. Packing rules also determine if multiple delivery notes should be allowed per pick list or if this should result in a warning. You can also use packing rules to apply a check to see if packaging rows are completely missing in pick lists when delivery reporting. The result of the check can be a warning or a block for reporting the delivery in this procedure.
Information possible to update on the order rows

#### Unit
Here you can see the unit of the part. The default unit here is the unit selected for the part in the part register to be used when arrival reporting, but it can be changed.

#### Status
Here you will see the status of the order row. If the reporting results in a negative stock balance, this will be indicated with this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeDowngrade.png). If the order row is ready for delivery, this is indicated with a different symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png).

#### Quantity to deliver
The default value for quantity to delivery for the selected orders, is determined by the setting Suggested quantity under the Selection tab. If you add a new order row to deliver, 1,00 will always be suggested regardless of what has been entered for the setting Suggested quantity.
If the quantity is greater than the disposable balance on the order row, then the quantity is shown in red color and a symbol is shown in the Status column. On the symbol, a tooltip displays information saying the reporting will result in a negative stock balance.
For row type 1, quantity must be greater than zero. For row type 2, quantity is allowed to be negative.
If the part has traceability, you must instead enter the quantity to deliver and the batch number or serial number in the Location box.
How to handle a negative balance on part is determined by the system setting Check if balance is negative during reporting and the related system setting Check against.
If there are clearances for the part it is not possible to delivery more than the disposable balance.
If the quantity to delivery differs from the packed quantity, entered on the pick list in the Pack for delivery, then a warning symbol is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png). A tooltip on the warning symbol informs you of this in text form.
The system setting called Warn/Block if multiple users try to report delivery at the same time is used to decide if it should be possible for multiple users at the same time to report delivery for the same order/pick list.
> If the part has the lot sizing rule Linked requirement, and there is a linked manufacturing order or purchase order for the order row, then only what is reported as finished and the arrival reported quantity on the order will be shown as disposable balance.

#### Delete remaining
If the quantity to deliver is smaller than the planned quantity on the order row, then the Delete remaining checkbox on the row will become activated. If you mark this checkbox, the remaining quantity on the order row will become deleted when you save in the procedure.

#### Price each, Setup price, Discount, Standard price
If you have added a new order row, you can update the prices and discounts of the order row.

#### Dock – Row
Here you enter the dock to which the part on the order row should be delivered. This is often used on delivery schedules. This information can be changed.

#### Storage
Here you see/enter the storage to which the part on the order row should be delivered. This is often used on delivery schedules. This information can be changed.

#### Stock count request
Stock count request is mainly used if you find that the stock balance does seem to add up and you wish to signal this in Monitor ERP. When you activate this checkbox, today's date and the time will be set in the Request date field.
The parts for which there is a stock count request can be shown in the Create stock count basis list in the Stock count in list procedure. This is done by activating the Include requested stock counts setting. You can also select by Stock count request date. The list also displays the comment. When the stock count has been performed and saved for the part, the field and the comment will be cleared.

#### Request comment
If you have checked the Request comment checkbox, you can here add a comment regarding the cause of this request.

#### Request date
Here you see the date and time when the stock count request was made. That is, when the Stock count request checkbox was marked.

#### Transfer profile
If you are using the Customer order transfer option, you will here see which transfer profile is being used. If you add an order to deliver, you can choose to add a transfer profile for transfer to the sales company. Read more about this field in the help topic regarding order rows in the Register customer order procedure.

#### Transfer to
If you are using the Customer order transfer option, you will in the production company here see if the order row is transferred to the sales company’s customer order and purchase order, or only to the sales company’s purchase order. If you add an order row to deliver, you can choose how the order row should be transferred to the sales company. Read more about this field in the help topic regarding order rows in the Register customer order procedure.
Explanation of different information
No. of handling units: In the Via pick list list type you see the number of handling units for each pick list. This is the number of packages on the top level in the package structure saved in the pick list in the procedure Pack for delivery.
Disposable balance The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity.: Here you see the disposable balance The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. of the part. If the option Warehouse is installed, you can use the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) on the toolbar of the procedure to choose which warehouses the information should be loaded from.
Partial quantity: If the order has partial quantities of the part, the Partial quantity button is activated. By clicking the button you find information about quantity of each partial quantity registered for the order.
Block/Notify customer: If the customer is blocked or if a message has been registered for the customer, you can click the button in the B/N C (Block/Notify customer) column in order to see the cause of the block or read the message. It is not possible to report delivery for customers which are blocked for reporting. For customers that are blocked for registration, it is not possible to add order rows.
Information: In the I column you will see a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusPackageImage.png) for packaging if the row contains a packaging part.
Delivery note number: On the list type called Via pick list you here see the delivery note number created if the customer order applies Delivery planing and the order has the setting to create delivery note number when delivery planning.
Package structure ready for delivery: Here you see "Yes" if the pick list is ready for delivery. Otherwise you will here see "No". You can update this in the procedure Pack for delivery.
Packed quantity: Here you see the quantity of parts on the pick list that have been completely packed. You can update this in the procedure Pack for delivery.
