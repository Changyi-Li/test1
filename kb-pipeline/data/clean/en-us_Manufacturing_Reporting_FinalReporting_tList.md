### The List tab
The list shows information about all the selected manufacturing orders.
Here you select the manufacturing orders for which you wish to update the status to 6 or 9 (depending on which alternative you chose under the Selection tab).
You can also see which manufacturing orders that have warnings, meaning that the status will not be updated by default. For these orders you can use the function button called Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) to go to the Report manufacturing order procedure with the marked manufacturing order loaded, to report the remaining quantity.

#### Include
With this checkbox you determine whether or not the manufacturing order will be included in the status update. When saving, the status will be updated for the manufacturing orders for which you have checked the Include box. They will disappear from the list.

#### Operation or material has remaining quantity (Q)
This column shows a button with a warning symbol if the manufacturing order has an operation, a part node, or material, with remaining quantity. Under the Warnings tab you can see more information about the warning.

#### Operation is missing reported time or cost (T)
In this column you can see a button with a warning symbol if the manufacturing order in question has an operation with 0 (zero) as reported total time or a subcontract with 0 (zero) as reported total cost.

#### Recording status (Rec. s.)
In this column you see a symbol illustrating the recording status (if the order has such a status). An order cannot be final reported if there is an active recording for a person. That is, a work item (an operation) is started (in progress) in the procedure Recording terminal in the Time recording module.
