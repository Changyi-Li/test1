## Post-calculation
The purpose of this procedure is to be able to perform a financial follow-up after a part/an order has been manufactured/reported. Here you compare planned costs with actual costs.
If you want to do an efficiency follow-up of operations, you should instead use the procedure called Operation follow-up.
Post-calculations can be made for orders regardless of order status, but you can only save the price for orders with status 4 (finished) or higher. You can perform post-calculation e.g. for manufacturing orders in progress with status 3 (started) in order to see the costs that have been generated so far, but you cannot save these costs as a price. For parts, however, you can only perform post-calculation for mean price calculation on orders with status 4 or higher. It is the list type that determines whether you perform post-calculation of orders or parts in the procedure.
For manufacturing orders, the costs are calculated per unit or for the entire manufactured quantity. Planned costs are calculated the same way as in the pre-calculation. Reported costs are calculated based on data from the manufacturing order log.
For parts the costs are calculated in the same way as for manufacturing orders. Reported part costs shown are averages, based on reported quantity in one or several manufacturing orders for the part. From the total values for the part you can proceed to see the cost for each involved manufacturing order, both in total and in detailed form.
You can save actual costs per unit to different price lists or only to the calculation register for the part. This applies to both list types. For the list type Total by order, you can also update the status of the order to 5 (calculated).
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
In the section [Calculations](../../../GeneralRegisters/BasicSettings/SystemSettings/bCalculations.htm) under the Manufacturing tab in the System settings procedure, you find settings which affect post-calculations.
Read more about how [post-calculations](../../../UserGuide/Using/Calculation/Postcalculation.htm) work under Using Monitor in the online help function.
List types
The list types determine whether you perform a post-calculation of manufacturing orders or a mean price calculation of parts in finished orders.

#### Total by order
This alternative means that you will perform a post-calculation of manufacturing orders with status 4 (finished) or higher, which is the normal case. But you can also include orders with status 3 (in progress) to see the costs that they have generated so far. This list type is selected by default when you start the procedure.

#### Part (mean price calculation)
This list type means that you can perform mean price calculation of parts in manufacturing orders. However, these orders must have status 4 (finished) or higher.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
