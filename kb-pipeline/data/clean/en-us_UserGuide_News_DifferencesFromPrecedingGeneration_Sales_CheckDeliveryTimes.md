### Check delivery times (CDT)
Check delivery times is not a separate procedure in G5, instead it is activated with a system setting. CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. takes place directly on the customer order row, the quote, or the manufacturing order as soon as part number and quantity are entered.
The result of the CDT is shown directly on the row in three own columns showing earliest delivery date/earliest finish date, difference in number of days compared to the desired date, and a window where you can see detailed information about critical operations/materials, loading, etc.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/CDT.png)](../../../../../Resources/Images/News/CDT.png)
On the customer order this check can result in three different results:
1. The quantity is available in the stock balance and can be delivered at once.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/CDT2.png)
2. The stock balance is not sufficient, but there is an existing order (refill) which will suffice. Then the finish date of that order will be suggested as delivery date.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/CDT3.png)](../../../../../Resources/Images/News/CDT3.png)
3. No stock balance or sufficient orders exists, so new manufacturing must be done. Then the current loading and material will be analyzed. The suggested date is based on critical operation/material.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/News/CDT4.png)](../../../../../Resources/Images/News/CDT4.png)
Additional info about CDT:
- CDT is always run with "check operations again" to directly reach a realistic finish time for part/order. However, critical operations/material are always shown in the result window regardless.
- Alternative work centers and alternative material suppliers can be analyzed for critical operations/material. This makes it possible to use alternatives and to show the cost of these alternatives.
- The pool planning (which is a new feature in G5) is taken into consideration making it possible to bases the delivery date on the earliest possible finish date for the related work centers.
- CDT will always take place when you save. This way a check is made to see if any other user has registered orders – during the time you were registering your order – which have affected the result.
- CDT can be used without order as basis in the Part register. The analysis will then show what the delivery date would become right now, based on the part's set order quantity.
