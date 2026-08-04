### Check of capacity availability

#### Basic principle for chack of capacity
The basic principle for operations is that the CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. function checks the available capacity in the future, that is, when the earliest possible time is to start each operation, if manufacturing is needed. If an operation for example takes four hours, the CDT will look in the future for four hours available capacity in a row.

#### Time precision and how capacity is analysed
For work centers with the time precision set to Day planningDay planning is used when you are NOT applying hourly planning. It means that all operations are planned to a date and not to a specific time on a date., the CDT function will check for these four hours on day level, that is the CDT will analyze the available capacity/loading per day. For work centers with the time precision set to Capacity via schedule or Hourly planningHourly planning refers to when planning per work center is done per hour. Hourly planning is activated with a system setting. Period is then entered as date and time. You can view loading on hour basis., the CDT function will check for these four uninterrupted hours in the defined schedule.
The system setting Time when order day/start day changes to next day determines if the capacity is available during the day or the next day.

#### Availability factor and required capacity
The calculation of when an operation can be performed also considers the work center's availability factor. If the work center fore example have an 80% availability and it is an operation which takes 8 hours, then the CDT must find 10 hours of uninterrupted capacity (8 ∕ 0.8) in the schedule of the work center. The operation can in that case not be planned to be completed on a schedule with eight hours.

#### Lag and overload
The CDT function also takes lag in the loading plan into consideration. The hours of the lag is then added to other loading – which is not lag – and affects when there is capacity available.
Overload, if any, is evened out and is included in the CDT. If there is available capacity back in time, it is used to even out the overload. If available capacity prior to the overload is missing, it will instead be distributed ahead in time as lag.

#### Calculating earliest finish date per operation
When the analysis has been made for each separate operation, the CDT has found an earliest finish date for each operation. These dates does not have a relation to each other. This might cause them to no be in phase. For example, the first operation can have an earliest finish date on 2022-04-14 and the second operation get an earliest finish date on 2022-04-12, even though the operations will not run in that order.

#### Difference and critical operation
Each operation has a difference between the finish date it should have had if the order was placed the for planned date and the earliest possible finish date that the CDT has calculated.
- The difference is displayed in work days for operations with day planning.
- The difference is displayed in hours for operations with Hourly planning.
The difference can be:
- Positive – the operation can run earlier than planned.
- Negative – the operation must run later than planned.
The operation with the largest negative difference (or the smallest positive) is the operation which is critical.

#### Synchronizing of operations and puzzle difference
The CDT then checks if the other operations can be planned in the right time/order in relation to the critical operation. If capacity is missing for operations before or after, the CDT will search for new earliest finish dates.
The process will repeat until all operations:
- have sufficient capacity.
- can be run in the correct order.
- have the right number of queue days.
When this is completed, the analysis is done. The CDT has then calculated a finish time for the final operation – the earliest finish date when the part can be ready for delivery. This is called a "puzzle difference".

#### Presentation of critical operation in the result window
In the [result window](ResultFromCDT.htm), the critical operation is indicated with a light red color. This allows you to see which operation determined the finish date. By allocating more capacity to this operation you can affect the finish date.

#### Work centers of the Pool type
For work centers of the Pool type, the loading of the pool and the included work centers are combined. These are compared to the total capacity of the included work centers.
This provides a complete loading for the work centers and can be used to search for available capacity for additional loading. This means you will get the same result regardless if BOM and routing was created on a pool work center or directly for one included work center.

#### Alternative work centers
As yet another step in the calculation, the CDT can suggest an alternative work center to the regular one. Alternative work centers can be linked to operations in the BOM and routing, and the CDT can suggest to exchange the critical operation.
You can also manually change to an alternative work center in the result window and run the CDT again using the new work center. However, these manual replanning items are not saved so you have to manually perform these after the manufacturing order has been created.
You will see the cost difference both when making an automatic and a manual change. When you confirm your choice in the result window, the standard price, CMThe contribution margin (CM) is the difference between the standard price and the sales price. and CRThe contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. on the order row will also be updated as a result of the calculation.

#### Checking of rescheduling
With this setting you can see if an existing manufacturing order can be rescheduled to start earlier. The following alternatives are available:
- Main part"Main part" is the term used for the part in the top node (highest level) in a structure of parts. – will only try to move your order.
- All parts – include stock driven parts, if any.
In practice, you remove your order along with any stock driven orders and then check whether there is capacity to manufacture it/them earlier.
