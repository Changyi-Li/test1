### Settings – Check delivery times
Settings for the list type Check delivery times. This is available if the system setting Apply check delivery times is activated.
Loading

#### Check capacity availability
This is the main system setting for the capacity availability in CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.. If this system setting is not activated, no analysis of the capacity availability will be made.

#### Only work centers that are included in CDT
When this setting is activated, the check of the loading situation will only be made for work centers included in check delivery times (this means that the work center might be a "bottleneck", for example a machine). If this setting is not activated, the check will be made on all work centers' operations on an order.
You decide whether or not a work center should be included in CDT in the work center register.

#### Calculate with suggestion
This system setting determines if the calculation should be made using existing material requirements suggestions and purchase order suggestions. You can activate this system setting if for example you have performed requirements planning for delivery schedules and these order suggestions should be included in such a simulation.
Material

#### Check material availability
This is the main system setting for the material availability in CDT. If you do not activate this system setting, then no analysis of the material availability will be made.

#### Calculate with suggestion
This system setting determines if the calculation should be made using existing material requirements suggestions and purchase order suggestions. You can activate this system setting if for example you have performed requirements planning for delivery schedules and these order suggestions should be included in such a simulation.

#### Check included stock driven part
This setting determines if included stock driven parts should be included in the CDT. The check is made for the lot size defined for those parts or more if the requirement is larger. The loading and material are checked in the same way as the main part, but for the included operations and material in the stock driven parts. This will then apply instead of saved throughput time including material procurement.

#### Consider sales forecasts
This setting determines if the CDT should also take sales forecasts into consideration.

#### Existing manufacturing order
With this setting you decide how the date on existing manufacturing orders should be handled by the CDT when checking when customer orders can be delivered. The date alternatives that exist are New finish (calculated for the operations in the priority plan) and Order's finished date (which is the planned finish date for the manufacturing order). What should be suggested here by default, is configured with the system setting Existing manufacturing order.
