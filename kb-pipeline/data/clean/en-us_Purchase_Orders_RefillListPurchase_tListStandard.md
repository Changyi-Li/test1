### The Standard list
This list is grouped by supplier. The suggestions is sorted by priority and part number.

#### Priority
Here you see the priority of the suggestion.

#### Change supplier etc.
Under the button Change supplier etc. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you will see a dialog box where you temporarily can change the supplier for an order suggestion. If there are any suppliers linked to the part, you will see them here. In the dialog box you can also modify the information that is possible to update for an order suggestion, for example price and posting.

#### Part number
Here you can see the number of the part in the order or suggestion. If the same part number exists on several subsequent rows, the part name will only be displayed on the first row.

#### Part name
In this column you see the name of the part. The name is displayed in the user's language. If there is no translation to that language, the name will be displayed in the company language.

#### Balance
Here you can see the current balance of the part.

#### Unit
The unit is selected under the Selection tab. If there are alternative units registered for the part, you can change to one of those units.

#### Days
In this column you see how many days the current balance will suffice when the part's daily pace is taken into consideration.

#### Ordered
Here you see how many parts have already been ordered.

#### Reserved
Here you see how many parts that are reserved for future consumption, for example via customer order or manufacturing order.

#### AVAILQ
In this column you see the available quantity within lead time. AVAILQ is calculated as balance plus order which should be delivered within the lead time minus the greatest value of the maximum theoretical consumption within lead time or planned reservations within the lead time. The planning formula is expressed like this: AVAILQ = BAL + ORQLT - Max (ADU x LT , RESLT).

#### Quantity
Here you see the quantity to order. This value can be changed.

#### Delivery date
Here you can see the suggested delivery date for the purchase. Changed delivery dates are displayed in italics and in blue color. A tooltip over the date displays the suggested delivery date.
If the delivery date is further ahead than the requirement date, a warning is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) letting you know that the delivery date is later than the requirement date. If the delivery date is more than a year away (ahead), a warning will also be displayed.
A warning is also shown if the delivery date is within the lead time. In that case the warning will also show the lead time date and lead time.
If the selected delivery date is not one of the supplier's delivery days or not one of the supplier's work days, a warning about this will also be displayed.
If you have entered a delivery date in past time, you will also see a warning.

#### Apply
The suggestion rows that are selected in this column will generate actual purchase orders when you click the button Generate purchase order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) (Ctrl + R) on the toolbar of the procedure. These orders are opened in a window.

#### Amount
In this column you can see the amount of the suggestion. It is always displayed in the company currency, by supplier and as a total.

#### Part status
Here you see the part status.

#### Warehouse
Here you see which warehouse the suggesting belongs to.

#### Reorder point
In this column you see the part's reorder point.

#### B/N S
In the Block/Notify part column you see if the supplier is blocked or if there is a message.

#### B/N P
In the Block/Notify part column you see if the part is blocked or if there is a message.

#### Lead time
In this column you can see the lead time in number of work days. The lead time is primarily loaded from the default supplier link and secondarily from the general lead time for the part. If you refill the part from warehouse (via a planning setting configured for the part), you will see the general lead time.

#### Annual volume
In this column you see the annual volume of the part.

#### Daily pace
Here you see the part's daily pace. This is the annual volume divided by the number of work days entered in the system setting called Number of work days per year.

#### Order quantity
Here you can see the part’s order quantity for the current warehouse.

#### Supplier's part number
Here you can see the supplier’s part number loaded from the supplier link.

#### Disposable balance
Here you see the disposable balance for the part. All reservations and orders have been taken into consideration.

#### Blanket order
If the purchase order row is a call off row to a blanket order, you see information about the blanket order by using the button Blanket order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png). The information shown is, for example, validity period, initial quantity, called quantity, remaining quantity, and blanket order status. By using the Link to blanket order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can link to the row on the blanket order. If there are several blanket orders or blanket order rows with the same part, you can change default row. By using the button Disconnect blanket order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) you can remove the link between blanket order and purchase order. If the link is removed, the price and any discount will be loaded from the supplier link.

#### Link to blanket order (B)
By using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can open the linked blanket order.

#### Consumption 3, 6, 12 months
These columns show the quantity consumed of the part the last 3, 6, and 12 months. The consumption is displayed in the unit selected for the suggestion.
