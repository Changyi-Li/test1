### The Detailed list
The list in the procedure is grouped by supplier and the purchase order suggestions are sorted by part number and delivery date. This list type will include new purchase order suggestions and replanning suggestions. This affects that performance of the list and makes it slower than the New purchase order suggestions list.

#### Action
This column shows a symbol representing the action that applies to the row. A tooltip displayed over the symbol displays information about the action in text, for example "Rescheduling suggestion – In".

#### Change supplier etc.
Under the button Change supplier etc. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you will see a dialog box where you temporarily can change the supplier for an order suggestion. If there are any suppliers linked to the part, you will see them here. In the dialog box you can also modify the information that is possible to update for an order suggestion, for example price and posting. A number on the button shows you how many suppliers are linked to the part.
When there is an alternative supplier who offers a better environmentally, that is, produces less CO2e emissions, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_sustainability.png) on the Change supplier etc. button.

#### Order number
Here you can see a purchase order number if you have chosen to reschedule an existing order. In this field you will instead see a suggestion number if you are about to create a new purchase order. Suggestion numbers are indicated with a pound sign #.

#### Position
Here you see the position of the order row on the existing purchase order.

#### Part number
Here you can see the number of the part in the order or suggestion. If the same part number exists on several subsequent rows, the part name will only be displayed on the first row.

#### Name
Here you see/enter the name of the part. The name is displayed in the user's language. If there is no translation to that language, the name will be displayed in the company language.

#### Suggested quantity
The suggested quantity can be changed for purchase order suggestions. The changed quantity is displayed in italics and in blue color. A tooltip over the quantity displays the previously suggested quantity. If the lot sizing rule of the part is set to Lot-for-lot, you will be asked to change the quantity of the causing requirement instead. If the lot sizing rule of the part is set to Linked requirement, you cannot change the quantity. If it is a rescheduling suggestion or a suggestion to delete an unnecessary order, the order's quantity will instead be displayed here. It cannot be changed.

#### Unit
In this column you will see the part’s default unit for purchase order as the suggested unit. If there are alternative units registered for the part, you can change to one of those units.

#### Order date
Here you see the suggested order date for the purchase order suggestion. It is the delivery date minus the lead time, the lead time being primarily loaded from the supplier link and secondarily from the general lead time for the part. If you manually change the quantity on the suggestion, the order date might not be correct any longer. This is indicated by then displaying the order date in italics. The net requirement calculation does not generate suggestions with order dates in past time.
If there is a shortage within the lead time, the order date will be set to today or tomorrow depending when during the day the net requirement calculation is run and also dependent of the system setting Time when order day changes to next day.

#### Delivery date
In this column you see the suggested delivery date for the purchase order suggestion. If you change the delivery date, it is displayed in italics and in blue. A tooltip over the date displays the suggested delivery date.
If the delivery date is further ahead than the requirement date, a warning is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) letting you know that the delivery date is later than the requirement date. If the lot sizing rule of the part is set to Lot-for-lot or Linked requirement, you will in the warning see a reference to change the delivery date of the causing requirement instead. If the delivery date is more than a year away (ahead), a warning will also be displayed.
A warning is also shown if the finish date/delivery date is within the lead time. In that case the warning will also show the lead time date and lead time. The Disregard lead time on part setting under the Selection tab determines that the suggested delivery date should not take the lead time of the parts in the supplier links into consideration. If the delivery date has already passed, the suggestion will never be entered for a passed date. The suggestion will always get today's date if it is without lead time. If lead time and safety time are used, the suggestion will be given today's date + the lead time and the safety time.
If the selected delivery date is not one of the supplier's delivery days or not one of the supplier's work days, a warning about this will also be displayed.
If you have entered a delivery date in past time, you will also see a warning.

#### Current delivery date
Here you see the current delivery date, that is, the delivery date which applies at the moment.

#### Requirement date
Here you can see the date when the requirement of the part will occur. If the requirement date is earlier than the delivery date, the date is displayed in red color. This is done in order for you to notice that the requirement occurs before the purchased part can be delivered. That is, when the disposable balance will fall below the safety stock.

#### Execute the purchase orders
The suggestion rows that are selected in this column will generate actual purchase orders, alternatively they will be rescheduled, when you click the button Generate/Replan purchase order or inquiry ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar of the procedure. These orders are opened in a window. Suggestions for deletion are shown in a separate window. From this window, you can go to the Register purchase order procedure to delete the orders.
You cannot apply purchase orders and inquiries at the same time.

#### Apply inquiry
The suggestion rows that are selected in this column will generate inquiries, alternatively be replanned, when you click the button Generate/Replan purchase order or inquiry![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar of the procedure. These inquiries are opened in a window. Suggestions for deletion are shown in a separate window. From this window, you can go to the Register inquiry procedure to delete the orders.
You cannot apply purchase orders and inquiries at the same time.

#### Distribution
If distributed purchase is used, the distribution is shown here.

#### Text
Under the Text button you can enter an optional text that will be registered as a row type 4 under the part on the order.

#### Instruction (I)
If there is an instruction entered on the material row of the manufacturing order or on the customer order row, that instruction is shown here (if the system setting Transfer info from causing requirement to purchase order is activated for manufacturing order/customer order. The instruction is transferred to row type 4 on the purchase order.

#### Instruction – Plain text
See instruction above.

#### Part status (P)
Here you can see the part status indicated with a symbol, but only if it deviates from status 4 (Normal). An explanation to the part status is displayed in a tooltip.

#### Block/Notify supplier (B/N S)
If a block or notification has been configured for the supplier, you can click the button in this column in order to see the cause of the block or read the message. If the supplier is blocked you are not allowed to use Apply for the suggestion.

#### Block/Notify part (B/N P)
If a block or notification has been configured for the part, you can click the button in this column in order to see the cause of the block or read the message. If the part is blocked you are not allowed to use Apply for the suggestion.

#### Disposable balance
Here you can see the disposable balance for the current period of time (the delivery date) in the unit entered on the row.

#### Lead time
In this column you can see the lead time in number of work days. The lead time is primarily loaded from the default supplier link and secondarily from the general lead time for the part.

#### Lot sizing rule
Here you can see the part’s lot sizing rule for the current warehouse.

#### Safety stock
Here you can see the part’s safety stock for the current warehouse.

#### Safety time
The safety time of the part for the current warehouse.

#### Order quantity
Here you can see the part’s order quantity for the current warehouse. If you apply current pace and a value for order quantity current pace exists, it is that order quantity you will see here.

#### Min. quantity
Here you see the minimum quantity of the part for the current warehouse.

#### Rounding quantity
Here you can see the rounding quantity of the part for the current warehouse.

#### Period length
The period length of the part for the current warehouse.

#### Causing requirement
The causing requirements displayed here can be e.g. a material requirement, safety stock, or a sale that has caused the requirement or suggestion.

#### Requirement date from reservation
Here you see the time when the disposable balance will fall under zero.

#### Causing order
Here you see the order number of the causing order or suggestion. To separate parts with a linked requirement from the ones without a linked requirement, you will see the Causing order number in italics for parts with the lot sizing rule Linked requirement.

#### Account
Here you can see the suggested purchase account.

#### Project
Here you see to which project the part is linked.

#### Posting
The posting dimensions, such as Cost center, Cost unit, Project etc., are displayed in the columns following Posting. In the Posting column under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see and modify the posting of the suggestion.

#### Price
The suggested price each from the supplier link. If the price is loaded from a staggered price, it will be displayed in italics. The price can be changed.

#### Discount
Here you can see the calculated discount. The discount can be changed.

#### Setup price
Shows the setup price from the supplier link. The setup price can be changed.

#### Amount
The amount of the suggestion. It is always displayed in the company currency, by supplier and as a total.

#### Receiving inspection
If receiving inspection is not activated for the part or the supplier, you can activate it for the purchase order suggestion. Receiving inspection will then be activated for the generated order row.

#### Instruction
If receiving inspection is activated, you can here enter an instruction for the inspection.

#### Files
If receiving inspection is activated, you can here link files to the inspection instruction.

#### Valid through
In this column you can see the valid through date for the purchase price loaded from the supplier link. If the date is in past time, the date will be displayed in red.

#### Revision
Here you can see the current revision of the part, but it is possible to change revision to some of the other revisions registered for the part. The selected revision is then used on the generated order row.

#### Administrator
The person that is the administrator of the part.

#### Information
Under the More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button you can see additional information about the administrator.

#### Price comment
If there is a price comment from the supplier link, you can here see it under the button Price comment ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png) that will be displayed on the suggestion row.

#### Type
Shows whether it is a suggestion or an existing purchase order on the row.

#### Weight
In this field you can see the total weight of the suggested quantity of the part in the suggestion. Weight per unit is loaded from the part. The weight is displayed per supplier and as a total. Only the suggestion rows where Apply is activated are included in the totals.

#### Volume
In this field you can see the total volume of the suggested quantity of the part in the suggestion. Volume per unit is loaded from the part (and if needed, also from the linked packaging). The volume is displayed per supplier and as a total. Only the suggestion rows where Apply is activated are included in the totals.

#### Emissions, part
Here you see the part’s CO2e emissions per unit.

#### Emissions, transport
Here you see the part’s CO2e transport emissions per unit. This is calculated as follows: Supplier’s transport distance x Part's net weight x Delivery method's Co2e2e emissions.

#### Emissions, total
Here you see the total emissions for this purchase. This is calculated as follows: (Quantity x Emissions, part) + (Quantity x Emissions, transport).

#### Blanket order
If the purchase order row is a call off row to a blanket order, you see information about the blanket order by using the Blanket order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png). The information shown is for example valid from and valid to, initial quantity, called quantity, remaining quantity, and blanket order status. By using the Link to blanket order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can go to the order row on the blanket order. The same button is also available directly on the purchase order row (see below). If there are several blanket orders or blanket order rows with the same part and supplier, you can change the default row. By using the button Disconnect blanket order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) you can remove the link between blanket order and purchase order. If the link is removed, the price and any discount will be loaded from the supplier link.

#### Link to blanket order (B)
By using the Link to blanket order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) in the B column (Blanket order), you can go to the order row on the blanket order.

#### Consumption 3, 6, 12 months
These columns show the quantity consumed of the part the last 3, 6, and 12 months. The consumption is displayed in the unit selected for the suggestion.

#### Supplier's part number
Here you can see the supplier’s part number loaded from the supplier link.

#### Supplier's order row position
Here you see the supplier's position number on their corresponding customer order row. This is used on EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. purchase orders.

#### Suggestion created
Here you can see the date and time when the suggestion was created by the net requirement calculation.

#### Difference
Here you can see the difference in work days between the current and the suggested finish date. The difference is only displayed for rescheduling suggestions.

#### Warehouse
For existing orders (for example rescheduling suggestions) you here see the purchase order's warehouse loaded from the order header. For new suggestions, the warehouse of the suggestion will be shown.
