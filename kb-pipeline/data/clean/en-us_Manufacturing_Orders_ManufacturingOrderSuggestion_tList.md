### The List tab
The list in this procedure is primarily sorted by part number, and within each part, the suggestions are sorted by start date.

#### Action
This column shows a symbol representing the action that applies to the row. A tooltip over the symbol displays information about the action in text. For example, suggestions to register a new order or to reschedule an existing order.

#### Confirmed as delayed
This column shows if the order is confirmed as delayed.

#### Order number
Here you can see the order number or suggestion number. Suggestion numbers are indicated with a pound sign #.

#### Status (S)
Here you see the status of the order. New suggestions do not have a status.

#### Part number
Here you can see the number of the part in the order or suggestion. If the same part number exists on several subsequent rows, the part number will only be displayed on the first row.

#### Name
Here you see/enter the name of the part. It is displayed in the user's language. If there is no translation to that language, the name will be displayed in the company language.

#### Suggested quantity
Here you can see the suggested quantity. It is possible to change for manufacturing order suggestions. The changed quantity will be displayed in italics and in blue. A tooltip over the quantity displays the suggested quantity. If the lot sizing rule of the part is set to Lot-for-lot, you will be asked to change the quantity of the causing requirement instead. If the lot sizing rule of the part is set to Linked requirement, you cannot change the quantity. If it is a rescheduling suggestion or a suggestion to delete an unnecessary manufacturing order, then the order's quantity will instead be displayed here.

#### Start date
Here you see the suggested start date for the manufacturing. The start date is affected by the throughput time which is calculated in the net requirement calculation for the suggested quantity. If you change the suggested quantity manually on the order suggestion, the start date that is displayed might become incorrect. To make this easy to see, the start date is displayed in italics.

#### Finish date
Here you can see the suggested finish date for the manufacturing. Changed finish dates are displayed in italics and in blue. A tooltip shown over the date displays the suggested finish date. If the lot sizing rule of the part is set to lot-for-lot or linked requirement, you will be asked to change the finish date of the causing requirement instead.

#### Requirement date
Here you can see the date when the requirement of the part will occur. If the requirement date is earlier than the finish date, the date is displayed in red. This is done in order to call attention to that the requirement is in past time or within lead time, which means that the requirement cannot be supplied in time. The procedure will never suggest to register or reschedule orders in past time. That is, when the disposable balance will fall below the safety stock.

#### Apply
The suggestion rows that are marked will be turned into actual manufacturing orders, be rescheduled or be deleted, when you apply/execute the action for the row. It depends on the type of suggestion.

#### Part status (P)
In this column you can see a symbol representing the status of the part.

#### Coordinated processing (CP)
In this column you will see a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/CoordinatedProcessing.png) for the suggestions which "are connected" in coordinated processing. These suggestions will be turned into orders as a group even though you only check Apply for one of the suggestions. The suggested quantity for each suggestion is calculated based on the requirement of each separate part and then distributed on all parts in the group. Each part's disposable balance, safety stock, and throughput time are decisive for which quantity is suggested.

#### Block/Notify part (B/N P)
If the part is blocked or if a message has been registered for it, you can click the button in order to see the cause of the block or read the message.

#### Disposable balance
Here you can see the disposable balance for the current period of time (the finish date).

#### Manufacturing order’s throughput time (TPT)
Here you can see the throughput time of the order in work days.

#### Lot sizing rule
Here you can see the part’s lot sizing rule for the current warehouse.

#### Safety stock
Here you can see the part’s safety stock for the current warehouse.

#### Safety time
The safety time of the part for the current warehouse.

#### Order quantity
Here you can see the part’s order quantity for the current warehouse. The order quantity is shown if Current pace is applied and has a value for order quantity.

#### Minimum quantity
Here you see the minimum quantity of the part for the current warehouse.

#### Rounding quantity
Here you can see the rounding quantity of the part for the current warehouse.

#### Period length
The length of the period for the part is shown here for the current warehouse.

#### Requirement date from reservation
Here you see the time when the disposable balance will fall under zero.

#### Causing requirement
The causing requirements displayed here can be e.g. a material requirement, safety stock, or a sale that has caused the requirement or suggestion.

#### Causing order
Here you see the order number of the causing order or suggestion. To separate parts with a linked requirement from the ones without a linked requirement, you will see the Causing order number in italics for parts with the lot sizing rule Linked requirement.

#### Revision
Here you can see the active revision of the part. It is possible to change the revision to another revision registered for the part. The selected revision will be used on the manufacturing order that becomes generated.

#### Administrator
Here you can see the name of person who is the administrator of the part.

#### Information
Under the More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button you can see additional information about the administrator.

#### Planned time
Here you see the planned time calculated for the suggestion. It means the time on the operations for which orders will be registered in the entire structure included in the suggestion. That is, operations for the main part and for included M-parts with the lot sizing rule Lot-for-lot and Linked requirement. Planned time is totaled for the suggestions you checked in the Apply column. Planned time is also crossed out until you have checked the suggestion in that column.

#### Consumption 3, 6, and 12 months
These columns show the quantity consumed of the part the last 3, 6, and 12 months. The consumption is displayed in the unit selected for the suggestion.

#### Suggestion created
Here you can see the date and time when the suggestion was created by the net requirement calculation.

#### Difference
Here you can see the difference in work days between the current and the suggested finish date. This is only shown for rescheduling suggestions.

#### Warehouse
For existing orders (for example rescheduling suggestions) you here see the purchase order's warehouse loaded from the order header. For new suggestions, the warehouse of the suggestion will be shown.
