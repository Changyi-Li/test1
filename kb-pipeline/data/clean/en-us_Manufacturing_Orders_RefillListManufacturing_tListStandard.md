### The Standard list
The suggestions in the list is sorted by priority and part number.

#### Priority
Here you see the priority of the suggestion.

#### Part number
Here you can see the number of the part in the order or suggestion.

#### Part name
In this column you see the name of the part. The name is displayed in the user's language. If there is no translation to that language, the name will be displayed in the company language.

#### Balance
Here you can see the current balance of the part.

#### Unit
If there are several alternative units registered for the part, you can here change to one of those units.

#### Days
In this column you see how many days the current balance will suffice when the part's daily pace is taken into consideration.

#### Ordered
Here you see how many parts have already been ordered.

#### Reserved
Here you see how many parts that are reserved for future consumption, for example via customer order or manufacturing order.

#### AVAILQ
In this column you see the available quantity within lead time. AVAILQ is calculated as balance plus order which should be delivered within the lead time minus the greatest value of the maximum theoretical consumption within lead time or planned reservations within the lead time. The planning formula is expressed like this: AVAILQ = BAL + ORQLT - Max (ADU x LT , RESLT).

#### Quantity
Here you see the quantity to manufacture. This value can be changed.

#### Finish date
The suggested date here is today's date plus lead time. Primarily, the part's general lead time will be used. And secondarily, it will be loaded from the saved calculation. This value can be changed.

#### Apply
The suggestion rows that are selected in this column will generate actual manufacturing orders when you click the button Generate manufacturing order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) (Ctrl + R) on the toolbar of the procedure. These orders are opened in a window.

#### Part status
Here you see the part status.

#### Warehouse
Here you see which warehouse the suggesting belongs to.

#### Reorder point
In this column you see the part's reorder point.

#### B/N P
In the Block/Notify part column you see if the part is blocked or if there is a message.

#### Throughput time
Here you see the throughput time in work days. The throughput time is loaded from the part. If you refill the part from warehouse (via a planning setting configured for the part), you will see the general lead time.

#### Annual volume
In this column you see the annual volume of the part.

#### Daily pace
Here you see the part's daily pace. This is the annual volume divided by the number of work days entered in the system setting called Number of work days per year.

#### Order quantity
Here you can see the part’s order quantity for the current warehouse.

#### Disposable balance
Here you see the disposable balance for the part. All reservations and orders have been taken into consideration.

#### Consumption 3, 6, 12 months
These columns show the quantity consumed of the part the last 3, 6, and 12 months. The consumption is displayed in the unit selected for the suggestion.
