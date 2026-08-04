### Planning window
Under this tab you find the planning window for the part. The planning window is actually a table showing all order rows, orders, and reservations, for the part.
The planning window is grouped by what is in the past, what is within lead time, and what is beyond lead time. Each grouping contains a total of number of order rows, orders, and reservations. The button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to the far left allows you to expand/minimize each grouping.
Below the table you see a total of number of orders, order, and reservations for the part.
> You can unpin the entire Planning window box from the tab by using the Floating button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_float_window.png) (Ctrl + U) if you need more space for the planning window. The planning window is updated if you change the part.
Quotes, inquiries, cases, and agreements
At the top left of the box you can use buttons to also show quotes, inquiries, active cases, and agreements for the part.

#### Quotes
This button is active if there are quotes containing the part on quote rows. When clicking the button, information about these quotes will be shown in a separate window. This applies to quotes with status 1 Registered, 2 Printed, and 7 Partial order, and when these quotes' rows containing the part are not linked to any customer order or are configured to be excluded from the quote statistics.

#### Inquiry
This button is activated if there are inquiries concerning the part. When clicking the button, information about these inquiries will be shown in a separate window. This applies to inquiries with status 1, 2, 3, 7 where inquiry rows with the part that are not linked to any purchase order or configured to be excluded from the inquiry statistics.

#### Active cases
This button is available if there are cases in progress for the part, that is, cases that have not been closed. You will then see information about those cases and all of the included parts in each case. This is displayed in a separate window.

#### Agreements
The button is activated if there are active agreements regarding the part.
> Remember that the buttons Quotes, Inquiries, Active cases, and Agreements, are active if there are records in any of the company's warehouses. If the records in question exist in another warehouse than in the current one, the button is still activated but has no content. Then you must choose to display records from the warehouse where these records exist by using the button Companies/Warehouses ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) (Ctrl + Q) on the toolbar.
Filters
At the top right in the tab you find a filter. Here you can select to filter what the planning window should display from: Actual orders, Preliminary orders, Forecasts, and Suggestions. Only Actual orders are selected by default to be displayed.
By clicking the the filter button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_filter.png) shown to the right of each marked alternative, you can filter further by different types of orders; actual orders, preliminary orders, forecasts, and suggestions. All alternatives are marked by default.
If you select Purchase order (advice), the dispatched quantity for a purchase order is shown on a separate row (provided dispatch advice is available). If you choose to not show dispatch advice, the purchase order row is shown with the entire ordered quantity on a row.
When you open the procedure next time, the filter you most recently used is saved by default.
Planning settings
At the bottom of the box you see the parts planning settings in the warehouse in question. These settings are loaded from the Planning tab and they can be changed here for the part.
The Function menu
On the function menu you find the following buttons specific for the planning window:
- Chart ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_chart.png) – here you can see a chart of the part’s disposable balance over time.
- Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) – here you can load the record of the selected row in the procedures available under the button.Reload – here you can reload the part. This can be made to see if any reporting or transaction has taken place for the part
- Requirement calculation ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) – here you can see the rows as requirement calculated (when the button is activated). In this mode you can see which actions are needed for the rows. You can click the button again to go back to the original mode.
- Apply suggestion ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) – here you can execute all actions according to the requirement calculation. The rows that will be turned into orders are the ones that are marked in the Apply column. If it is an unnecessary manufacturing order, the Register manufacturing order procedure will open with the order in question loaded. This order can be deleted directly since it is a separate order. In case it is a purchase order that seems so be unnecessary, a dialog opens where you can open the Print purchase order. There you can print the order or link to the Register purchase order procedure with the order in question loaded. You should not delete this order until you have contacted the supplier and asked them to cancel the purchase in their system.
- Change date format ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_date.png) – By using this button you can change date format between Date and YYWWD in the planning window. You can save the selected date format for yourself by using the Save layout function on the toolbar in the procedure.
- Simulate deletion of row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_simulate_remove.png) (F6) – With this button you can simulate effect on the disposable balance, the total ordered quantity, and the total reservations, for a part if, for example, a purchase order or manufacturing order is deleted.
- Return from simulation mode ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_undo_simulation.png) (Shift + F6) – With this button you reset the planning window when the Simulate deletion of row function has been used.
- Copy selected value ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_to_clipboard.png) – Using this button you can copy the marked value to the Clipboard in Windows. This way you can use Ctrl + V to paste the value where you want it, e.g., in Notepad.
- Create monitoring task ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_create_monitoring_task.png) – This button is available if the Agent option is installed. By using this button you can create a monitoring task for the marked row. There are three options for monitoring tasks which you access via the button. These are: Balance – Part, Arrival – Part, and Arrival – Purchase order row. You select one of these terms for the monitoring task. In the dialog which is then opened, you can configure settings for the monitoring term and select who should be the recipient of notifications from the monitoring task. By using the Save button, the monitoring task is automatically saved to the Monitoring tasks procedure. The monitoring task will be given the next available number in the number series.

#### Action
When you have activated Requirement calculation, a symbol is shown representing the action that is needed on the row. If you place the mouse pointer over the symbol you will see a tooltip regarding the action. This is the action that will be executed when you have marked the Apply button on rows and then clicked the button Apply suggestion.

#### Date
In this column you see the date of the planned transaction. This is the finish date of the manufacturing order, reservation date for material requirement, delivery date of the customer order and purchase order. The throughput time on a manufactured part and lead time on a purchased part will also affect the date. For incoming stock orders, the delivery date is affected by both part's lead time and internal supplier's (warehouse's) transport time. For blanket order – sales, the date will be displayed if the setting Include in net requirement calculation is marked for the blanket order. Then the quantity on the blanket order will affect the disposable balance for the part.
The throughput time on a manufactured part and the lead time on a purchased part are shown with a colored background in the date field according to below:
- Red = Past.
- Yellow = Within lead time.
- Green = Beyond lead time.

#### Type
Here you see which type of order it is: actual order, preliminary order, forecast, or suggestion. The different types are displayed in their respective module color. The types that can be used here are the ones you have chosen to include by applying the filter at the top of the tab If it is a balance row, you will see the word "Balance" in black color.

#### Status
In this column you see the status of the order or the order row in question. When you hover over the field, a tooltip will display the status in text form.

#### Confirmed purchase order (C)
A "Yes" is shown for purchase orders if the order row is confirmed from the supplier.

#### Dispatched
A "Yes" is shown for purchase orders if a dispatch has been reported for the order row.

#### Delivery note number
Here, delivery note numbers for dispatched purchase orders are shown.

#### Order number
Here you can see the order number of the respective orders. If it is a material requirement, you will see the manufacturing order for the main part where this part is incorporated. If it is a suggestion, you will see the suggestion number. The order number is shown in italics if the order has been changed which resulted in the current date not being the same as the initial date.

#### Customer/Supplier/Main
This column shows the customer/supplier on the order. For rows of the types material requirement and different suggestions, you will see the main part of the requirement.

#### Information
With the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you access a window showing detailed information about the marked row. For a balance row you will see information about the current balance of the part's respective locations in the warehouses selected on the toolbar of the procedure. On rows for manufacturing and material you will see information about manufacturing orders and other information. For material requirements you can use the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) button next to the Main part"Main part" is the term used for the part in the top node (highest level) in a structure of parts. (order) field to load the manufacturing order's main part to the procedure (in the record selector). The Main part field displays in which the part is included. On sales rows you see information about customer, customer order row, and information about pick list, if any.
For purchase order suggestions/manufacturing order suggestions you see the causing requirement from Linked order displayed with the order number in italics.
For return orders you see the return quantity and the delivered quantity, delivery date, and initial arrival date. The initial purchase order's order number, as well as arrival reported quantity and case number, if any, are shown in the Initial purchase order section.
In the window you open with the button you can use the context menu which you access by right-clicking. There you find functions to, for example, copy values in the fields of the window and go to different related procedures for the row in question.

#### Consuming order
Here you will see a tree structure of suggestions from the net requirement calculation so that you can see where the requirement comes from.

#### Ordered
The ordered quantity is shown in green. The total of this column is displayed at the bottom of the box.

#### Reserved
The reserved quantity is shown in dark red. The total of this column is displayed at the bottom of the box. If a forecast deduction has been made in a sales forecast, you will see the reserved quantity in italics. A tooltip over the quantity shows the reserved quantity before deduction, and the deducted quantity.

#### Partial quantity
This column is displayed if the part has partial quantites and there are order rows with partial quantities. By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) on the separate rows, you see the partial quantity and the packaging part for the partial quantity entered for each order row.

#### Linked order
Here you see if the order is linked. If you mark a linked order, the background in the order number field for the selected row as well as the linked row will be highlighted in yellow.

#### Cleared
In this column you will see a C if the record on the row is already fully cleared. If the record is partially cleared, you will see a P here.

#### Clearance information
Under the Clearance information button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), information regarding Cleared quantity, Location name, and Serial numberA serial number is a number that is used for traceability for parts on entity level./BatchA batch is the set of components/products manufactured at the same time and made from the same original material. is displayed.

#### Disposable balance
The disposable balance is the current balance + ordered quantity; or the current balance - the reserved quantity. It is displayed in red color if it falls below the safety stock. Disposable balanceThe disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. can be displayed with two to six decimals.

#### Start date
Start date is shown for purchase orders only if the Requirement calculation button has been activated. For purchase order suggestions you will see the Order date in the column. The start date displayed for manufacturing order rows is the start date for the first node (level) in the structure.

#### Finish date
Finish date is only shown if the Requirement calculation button is activated. This applies to both actual manufacturing orders and purchase orders as well as to manufacturing order suggestions and purchase order suggestions.

#### Apply
This column is displayed if you have marked to include Suggestions in the filter in the planning window. If you mark Apply for a suggestion and click the Apply suggestion button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the function menu, the action for the suggestion in question will be executed. For example, if a purchase order suggestion is concerned, the action will be to create an actual purchase order from the suggestion.
If the part has distributed purchase by order, and there are multiple purchase order suggestions, the purchase order will be generated according to the order of the suppliers stated in the distribution. If you mark only one of the suggestions (and it is not the first suggestion according to date), a warning will be displayed ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) letting you know that purchase order will not be generated according to the part's distribution.

#### Match
This column is displayed if you have marked to include Suggestions in the filter in the planning window. The match column is used to match the quantity on an existing purchase order if the quantity on the underlying requirement has been changed. This can only be applied on parts that have the lot sizing rule set to Lot-for-lot.

#### Calculated requirement date
The calculated requirement date is shown when a requirement calculation is performed in the planning window. The date is calculated at requirement calculation and is used on manufacturing and purchase orders when the disposable balance will falls below the safety stock level. A date is also shown on suggestions generated in a net requirement calculation.

#### Warehouse (WH)
Here you will see the warehouse to which the balance belongs.

#### Confirmed as delayed
An orange clock is shown in this column if the order has been confirmed as delayed.

#### Confirmed quantity difference
Here you see if the quantity on the order suggestion differs from the causing requirement. This can only occur if the Pick from stock first option has been selected in the Purchase on project setting. If the checkbox is marked, it means the quantity on the suggestion and the causing requirement differs.

#### Supplied by
If you use CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. you will here see which order will refill the balance making the row possible to deliver.

#### Configuration
If you have installed the option Product configurator, this column appears where you can see the order's configuration.
More info
Under the button More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), to the far right in the planning window, the following field is shown by default.

#### New finish
If you apply Check delivery times (CDT) and the order has a date for New finish via the net requirement calculation, this date is shown here.

#### Last requirement date
A last requirement date is shown when a requirement occurs. The date is calculated at requirement calculation and is used on manufacturing and purchase orders. That is, when the disposable balance will fall below the safety stock.

#### Requirement date from reservation
Here you see the time when the disposable balance will fall under zero.

#### Dock – Row
Here you enter the dock to which the part on the order row should be delivered. This is often used on delivery schedules. This is loaded from the customer order row.

#### Dock description
Here you can enter a text describing the dock. This is loaded from the customer order row.

#### Storage
Here you see/enter the storage to which the part on the order row should be delivered. This is often used on delivery schedules. This is loaded from the customer order row.

#### Kanban number
Here you see the Kanban number for the part on the order row. This is often used on delivery schedules. This is loaded from the customer order row.

#### Reference number for manufacturing
Here you see/enter the customer's reference number for manufacturing. This is something which is primarily used if you have customers within the car industry where it sometimes happens that the customer, in their delivery schedules, earmarks requirements with for example chassis numbers. You need to refer to this reference number in both the dispatch advice message sent to the customer in connection with shipping the goods, as well as on the transport labels with which the goods have been labeled. This is loaded from the customer order row.

#### Reference number for delivery
Here you see/enter the customer's reference number for delivery. This is something which is primarily used by those who have customers within the car industry where it sometimes happens that the customer, in their delivery schedules, earmarks requirements with is called "Part consignment number" You need to refer to this reference number in the dispatch advice message sent to the customer in connection with shipping the goods. This is loaded from the customer order row.

#### Name
Here you see the name of the customer, supplier, or main part.

#### Order category
If you use Categories on customer order, purchase order, or manufacturing order, this is where you will see the category.
