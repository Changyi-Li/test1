### Check delivery times
Read about [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using MONITOR in the online help function.
> The system settings configured here will apply during check delivery times (CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.). However, the CDT system settings can be overridden for a specific manufacturing order, for stock order – sales, customer order, or quote. This is done by using the button CDT ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) in the affected procedure.

#### Apply check delivery times
This system setting determines if CDT should be used or not. When this system setting has been activated, the system settings below will also be activated. These system settings will in turn determine how the CDT calculation should be made.
If this system setting has been activated, it is possible to calculate and save New finish - date on customer order rows and manufacturing orders in the Net requirement calculation You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. procedure. This applies if you have checked the box New finish on the order row in the Net requirement calculation.
Check capacity availability
This is the main system setting for the capacity availability in CDT. When this system setting has been activated, the following two system settings will also be activated. If you do not activate this system setting, no analysis of the capacity availability will be made.

#### Only work centers that are included in CDT
There is a setting in the work center register that determines if the work center should be included in CDT. If this system setting is activated only the work centers included in CDT will be checked. If this system setting is not activated, the check will be made on all work centers' operations on an order.

#### Calculate with suggestion
This system setting determines if the calculation should be made using existing manufacturing order suggestions. You can activate this system setting if for example you have performed requirements planning for delivery schedules and the loading from these order suggestions should be given priority over the simulation. The loading created via the manufacturing order suggestions can of course result in a part, for which there is a requirements, will be manufactured. Such a suggestion is therefore presented as asset under the Planning window tab in the result window in CDT.
Check availability of
This is the main system setting for the material availability in CDT. With this setting you decide if the CDT checks the availability of Parts (material) and/or Consumable parts (tools of the basic type Consumption). If you have activated a checkbox in this setting, the following three system settings will also be available.

#### Calculate with suggestion
This system setting determines if the calculation should be made using existing material requirement suggestions. This way, material requirements belonging to manufacturing order suggestions will be included when disposable balance is calculated.

#### Consider sales forecasts
This setting determines if the CDT should also take sales forecasts into consideration.

#### Automatically run analysis
This system setting determines if CDT should be run automatically on new quote rows, customer order rows, and manufacturing orders.

#### Difference
Here you determine how differences that appear when running CDT should be calculated. The available options are:
- Individual – Calculates the total difference that occurs when CDT places separate operations and material on the order in the loading plan.
- Puzzle – Calculates the difference that occurs when CDT places all included operations and material in the loading plan. This is made exactly as it looks like on the order (CDT puzzles with the order as a whole).
