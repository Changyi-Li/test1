### Post-calculation
The purpose of this procedure is to be able to perform a financial follow-up after a manufacturing order has been manufactured/reported. Here you compare planned costs with actual costs.
Efficiency follow-up of operations is done in the Operation follow-up procedure.

#### Order status and the ability to save price
Post-calculations can be made for orders regardless of order status, but you can only save the price for orders with status 4 (finished) or higher. You can perform post-calculation e.g. for manufacturing orders in progress with status 3 (started) in order to see the costs that have been generated so far, but you cannot save these costs as a price.
For parts, however, you can only perform post-calculation for mean price calculation on orders with status 4 or higher.
It is the list type that determines whether you perform post-calculation of orders or parts in the procedure.

#### Cost calculation for manufacturing order
For manufacturing orders, the costs are calculated per unit or for the entire manufactured quantity. Planned costs are calculated the same way as in the pre-calculation. Reported costs are calculated based on data from the manufacturing order log.

#### Cost calculation for part
For parts the costs are calculated in the same way as for manufacturing orders. Reported part costs shown are averages, based on reported quantity in one or several manufacturing orders for the part. From the total values for a part, you can go on to see the cost for each manufacturing order involved, both in total and in detailed form.

#### Saving actual costs and updating order status
You can save actual costs per unit to different price lists or only to the calculation register for the part. This applies to both list types.
For the list type Total by order, you can also update the status of the order to 5 (calculated).

#### Valuation of incorporated/included parts
The incorporated parts are normally valued according to the standard price that was applied during the order registration or reporting. However, it is also possible to value according to current price alternative.

#### The Selection tab
Here you configure settings for the post-calculation.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Postcalculation.png)](../../../../Resources/Images/TrainingMaterial/Postcalculation.png)
List types
The list types determine whether you will perform a post-calculation of manufacturing orders or a mean price calculation of parts from several finished orders.
- Total by order – With this list type it means you perform a post-calculation of manufacturing orders with status 4 (finished) or higher. But you can also include orders with status 3 (in progress) to see the costs they have generated so far. This list type is selected by default when you start the procedure.
- Part (mean price calculation) – This list type means that you can perform mean price calculation of parts in manufacturing orders. However, these orders must have status 4 (finished) or higher.
Settings
Most settings for post-calculation are the same as the settings for the pre-calculation. You find the description of these settings in the topic under the help section [Post-calculation](../../../Manufacturing/Calculations/PostCalculation/wPostCalculation.htm).
> Save the settings to be used in your company by using the function Default values in the backstage of the procedure.

#### The List tab
The List tab becomes available after you have used the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) button on the toolbar. This tab shows, depending on the list type selected, the selected manufacturing orders or the selected parts. Here you can choose which orders/parts not to include in the calculation or the mean price calculation. You start the calculation using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar.

#### Other tabs
The other tabs in the procedure become available after you have started the calculation. The tabs show information corresponding to the information in the Pre-calculation procedure. You find the description of these tabs in the help section Post-calculation [Post-calculation](../../../Manufacturing/Calculations/PostCalculation/wPostCalculation.htm).
