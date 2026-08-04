### Order rows
In the Order rows box under the Rows tab you see the order rows as described below:
- List type Picking plan: Here you find all order rows from customer orders for the customer marked in the Delivery status box.
- List type Picking plan – Per customer: See the list type above, but this list is grouped per customer.
- List type Picking in progress: Here you see all order rows in the picking in progress list that is marked in the list to the left.
- List type Release preliminary pick lists: Here you see all order rows in the preliminary pick list which is marked in the list to the left.
For the list types called Picking plan and Picking plan – Per customer, you will at the bottom of the tab see a total of number of orders, number of rows, net weight and gross weight, net volume and gross volume, pick time, and number of handling units, for all order rows where Pick is marked in the list. Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you see shipping information for each handling unit.
The Function menu
By using the Add new row at the end (F5) button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) on the function menu, you can add rows if the pick list has a different status than Ready for invoicing. (Applies to the Picking in progress list type). If the delivery rule called Create delivery note number when delivery planning has been activated, the following applies:
- If regular delivery note number is used, the new row will get the same number as all other rows with the same order number. Otherwise, a new number will be assigned.
- If comprehensive delivery note is used the new row will get the same delivery note number as the rest of the rows.

#### Delete
This checkbox is available when the list type Picking in progress has been selected. If this checkbox is marked, it means the order row will be deleted when you save. This makes it possible to include the row on a different pick list.

#### Pick
The checkbox Pick is available when the list type Picking plan is selected. By marking the checkbox, the order row will be included in the pick list when saving. This checkbox can only be checked on rows for customer orders in the section Ready for delivery in the box Delivery status. It is also possible to check the box in the column heading to mark all order rows.
In the list type called Picking plan – Per customer you can mark the Pick checkbox for customer order rows with the delivery status Ready for delivery and Preliminary. If the row has the delivery status called Preliminary, no clearance will be made. The rows are shown in the pick list together with rows that have the delivery status Ready for delivery. These rows will also not have a location in the pick list.
When an order row is marked to be picked and it is not a preliminary pick list, clearance of the stock balance is automatically made for the order row when the pick list is saved. This reduces the available stock balance of the part for other orders. If the pick list is preliminary, no clearance will be made.
If the order row contains a fictitious part, you can expand the row by clicking the arrow button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to the left of the Pick column. You will then see the underlying order rows and you can mark to pick separate included/incorporated parts in the fictitious part.

#### Status
Only the Picking plan – Per customer list type. Here you see the status of the order rows:
- Ready for delivery – Here you will see orders for which you can print a pick list and also deliver. One pick list will be printed per customer and delivery address.
- Ready for delivery – Credit limit exceeded – Here you see orders you can delivery, but where the customer has exceeded its credit limit. If the Handling of credit limit at delivery system setting has been set to Block, then it is not possible to deliver when the credit limit has been exceeded. With the system setting called Credit limit compared with, you determine what the credit limit should be compared with.
- Ready for delivery – Unpaid advance invoice – Here you see orders you can deliver, but the advance on the order has not been paid in full. If the setting called Check for unpaid advance invoices in the Invoicing plans procedure has been set to Block, then it is not possible to deliver.
- Waiting list – Here you see orders you can deliver, but that are not grouped under "Ready for delivery" because partial delivery is not allowed on order level.
- Shortage list – Here you see orders you should deliver, but that are not possible to deliver because of part shortage.
- Unconfirmed – Here you see orders where the delivery date on the order rows cannot be confirmed.
- Preliminary – Here you see orders where preliminary pick list is applied.

#### Rows with same status
Here you see how many rows that have the same status as this row.

#### Order number
In this column you see the customer order number to which the order row belongs. If there is a fictitious part on the order row, you can expand the row by clicking the arrow button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to show the included/incorporated parts.

#### Position
The Position column shows the position of the order row.

#### Part number
Here you see the part number of the order row.

#### Name
Here you see the part name.

#### Planned picking quantity
In this column you see the planned picking quantity of the order row. The picking quantity is the same as the order row's quantity to deliver or the disposable balance of the part on the order row, if this is less than the quantity to deliver.

#### Quantity to deliver
Here you see the order row's quantity. On order rows of row type 2 and on preliminary pick lists you can enter the quantity to deliver.
When a preliminary pick list has been saved (picking is in progress) and is loaded using the list type Picking in progress, you here see zero as quantity to deliver. But on the printed preliminary pick list you see the order row's quantity to deliver.

#### Total
If the customer order row belongs to a total and if the total's all included/incorporated order rows are ready for delivery, then you will see a sum/total symbol (∑) in this column. If all of the total's included/incorporated order rows are not ready for delivery, you will instead see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) in the column. When you move the cursor over ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) you will see the message "All order rows in the total are not ready for delivery" in a tooltip.

#### Location
On order rows of row type 1 you find the button Location ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). Click this to open a location window where you can enter the quantity to deliver from each location. The quantity to deliver cannot be greater than the disposable balance.
When the pick list is printed, the locations from which the part is picked, becomes registered so that the next pick list for the same part will not suggest the same location if the balance is not sufficient. These locations are blocked for reporting for everything but reporting of the order row, if the whole balance will be picked.
If someone tries to stock report for the location when the order row needs part of the balance, you will see a warning in the affected procedure. This can be e.g. stock withdrawals to manufacturing orders or direct (not planned) withdrawals. Then it is not possible to report in that procedure, if it would result in a shortage against the order row on the pick list.
If the part has partial quantities registered, locations will be suggested from which to pick partial quantities, just as was registered on the customer order.
Other information shown for the locations is the location name and disposable balance. If the part has traceability on batch level you will also see batch number, best-before date, and charge number. If the part has traceability at serial number level you will also see the serial number. For pick lists that are ready for delivery you will see the location's revision.

#### Delivery date
Here you see the order row's delivery date.

#### Pick list's delivery date
Here you see the pick list's planned delivery date if this has been entered in the settings for the list.

#### Disposable balance
The disposable balance The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. in stock of the part.

#### Remaining quantity
In this column you see the remaining quantity on the order row which have not yet been cleared and are not included on a pick list.

#### Net weight
Here you see the part's total net weight for the disposable balance.

#### Net volume
Here you see the part's total volume for the disposable balance.

#### Gross volume
Here you see the part's total net volume including packaging volume for the disposable balance. If the part does not have a packaging, you will here see the part's total volume for the disposable balance.

#### Packaging
Here you see which packaging is linked to the part.

#### Percentage packed
Here you see a bar and a value in percent if the order row is packed. On new pick lists you see 0 percent. When a regular pick list has been saved (picking in progress) and is loaded via the list type Picking in progress, you will here see 100%. When the pick list is set to picking is in progress, the parts that should be picked are also considered packed. On a preliminary pick list on the other hand, you will see 0 percent even when it is saved and you load it via the list type Picking in progress.
Percentage packed is only relevant when packing is applied in Monitor ERP. In the procedure Pack for delivery you will in the pick list see which packages in the packaging structure that are completely packed. Here on the order row the percentage value is changed based on how many of the packaging items that are marked as completely packed.
The More information button
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Customer's order number
This field is used to enter the customer's purchase order number on row level. The field can contain a maximum of 30 characters. In many cases, you enter the customer’s order number in the header of the order, but if you for example are working with delivery schedules it is common that order numbers or call numbers are used which are unique for that specific order row. This is not the same order number as in the header of the order. If you are using EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system., this value will be entered via the order file you import. But if you manually register an order, then you should yourself enter the order number on the row if the customer requires it. The value in this field will be included when using EDI to export for example order confirmation and invoice. This is done so the customer can match it with their purchase order.

#### Customer's order row position
This field is used to keep track of the row number which the customer has stated in their purchase order. The field can contain a maximum of 15 characters. This value is entered via EDI import of an order, but it is also possible to manually enter it, if you want to. The value in this field will be included when using EDI to export for example order confirmation and invoice. This is done so the customer can match it with their purchase order row on this order row position. It is especially important to keep track of the customer's order row position in cases where the customer order row is split. For example if it is not possible for you to deliver everything now, but the row must be split and a you enter a later date for a part quantity on the new row. Then it is important to know which order row position at the customer that the new row refers to.

#### Dock – Row
Here you enter the dock to which the part on the order row should be delivered. This is often used on delivery schedules.

#### Dock description
Here you can enter a text describing the dock.

#### Storage
Here you see/enter the storage to which the part on the order row should be delivered. This is often used on delivery schedules.

#### Kanban number
Here you see the Kanban number for the part on the order row, if this is entered. This is often used on delivery schedules.

#### Reference number for manufacturing
Here you see/enter the customer's reference number for manufacturing. This is something which is primarily used if you have customers within the car industry where it sometimes happens that the customer, in their delivery schedules, earmarks requirements with for example chassis numbers. You need to refer to this reference number in both the dispatch advice message sent to the customer in connection with shipping the goods, as well as on the transport labels with which the goods have been labeled.

#### Reference number for delivery
Here you see/enter the customer's reference number for delivery. This is something which is primarily used by those who have customers within the car industry where it sometimes happens that the customer, in their delivery schedules, earmarks requirements with is called "Part consignment number" You need to refer to this reference number in the dispatch advice message sent to the customer in connection with shipping the goods.

#### Row's goods label
Here you can enter the customer order row's goods label. If you create a purchase order or a manufacturing order from the customer order, then the row's goods label will be included to the field Customer order row's goods label on the manufacturing order and to the field Customer order row's goods label on the purchase order.

#### Partial delivery
Here you see if partial delivery is allowed per order or per order row, for the customer order on the row. This information is only shown if a customer order appears more than once. E.g. If there is an order with rows with both status Ready for delivery and Shortage list. Otherwise, the column will instead show a dash (“-”) as the result.
If partial delivery is allowed per order, and there are order rows ready for delivery, Allowed on order will be shown.
If partial delivery is allowed per order row, and there are order rows ready for delivery, Allowed on order row will be shown.
If not, a dash "-" is shown. This occurs if partial delivery is not allowed, if partial delivery per order/order row is allowed and the order row is on the shortage list, or if the order applies preliminary pick list.

#### Packed quantity
Here you see the quantity in the packages that are marked as completely packed in the procedure Pack for delivery.

#### Delivery note number
If it is marked on the order that the delivery note number should be created when delivery planning, you will here see the delivery note number.

#### Customer's part number
Here you see the customer's part number, if such has been entered.

#### Desired delivery date
Here you see the date on which the customer wants the delivery.

#### Initial delivery date
The row's initial delivery date is by default the same as the current delivery date on a new row. The Initial delivery date is the date that first was entered when the row was registered. This date can be changed up to the point when the order is delivered in full, but in this procedure you cannot update the initial delivery date.

#### Person
Applies to the list types Picking plan and Picking plan – Per customer. Here you see the person responsible that you selected under the Selection tab, but it is possible to can change the person for the row here as well.
