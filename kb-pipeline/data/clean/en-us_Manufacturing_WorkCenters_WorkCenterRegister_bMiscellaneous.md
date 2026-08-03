### Miscellaneous

#### Planner
Here you select the person who is the planner for the work center. Planner can be used as a selection term in different lists.

#### Work center category
Here you can select a work center category. This is used as a selection and grouping term in lists. By clicking the Category selection button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select a category if categories have been registered in the Categories procedure. If no categories are registered, you can type as you please in this field. Categories can be used as a selection term in different lists. Read more about how categories can be created/constructed in the online help function for the [Categories](../../../GeneralRegisters/Categories/Categories/wCategories.htm) procedure.

#### Include partially reported in Ready to run (P)
With this setting you decide if the filter to show operations ready to run should also include rows where the previous operation has only been partially reported (that is, with a greater quantity than my operation has been reported).

#### Time horizon in priority plan
This applies to the Machine, Manual work, and Pool types. In this field you indicate how far ahead in time (in number of work days) you normally wish to see in the priority plan for the work center in question. The system setting Time horizon filters by determines if the entered time horizon should be based on the option New finish date, Planned start date, or Planned finish date. A tooltip is shown when you hover over the field, displaying the selected option.

#### Default setup time
This applies to the Machine, Manual work, and Pool types. Here you select a default setup time to use in BOM and routing when you create routing for this work center. The unit used here is determined by the system setting Time unit Time units are units used to indicate the setup and unit times at BOM and routing. Normally, minutes or hours are used. for setup and unit time for operations.

#### Default ineffective time
If the system setting Use cycle time and ineffective time in BOM and routing is activated, then it is possible to enter a default ineffective time Ineffective time is time which is necessary in the operation, but not directly productive. for the work center.

#### Default transport cost
This applies to the Subcontract type. Here you can enter a default transport cost for subcontracts on the work center.

#### Default setup cost
This applies to the Subcontract type. Here you can enter a default setup cost for subcontracts on the work center.

#### Default location
Here it is possible to add one or multiple default locations or location intervals, from where material withdrawal should primarily be made for the work center in question. It is possible to choose order of priority for the locations the work center can use, and you can also block withdrawal from locations used for deliveries. If the system setting Apply pick location is activated, then it is also possible to mark which locations should be pick locations.
Locations added here must have the same type, being a pick location or not, as the same location in the Part register in order to be valid. If the location is not valid, its priority will be based on the [rules for prioritizing locations](../../Reporting/RulesLocationsWithdrawMorder.htm).
Locations with high priority will be prioritized above all other locations on the part.
Locations with low priority will be managed after all other locations have managed.

#### CDT additional days
Monitor ERP normally looks for gaps in the existing loading to fit the operation into CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. (check delivery times). However if days are entered in this setting, the loading can be spread over several days. You can set how many additional days can be used.
Please note that an operation being divided onto non-consecutive days will likely mean that either additional setup times or that operations for existing orders will need to be rescheduled to earlier times.

#### Included in CDT
With this setting you decide if the work center should be included in the check of delivery times (CDT). This setting is activated by default for new work centers. Normally you only need to include the work centers that are "bottle necks" (for example different machines) in the CDT. In cases where the work center cannot affect the delivery time, you can uncheck setting.
