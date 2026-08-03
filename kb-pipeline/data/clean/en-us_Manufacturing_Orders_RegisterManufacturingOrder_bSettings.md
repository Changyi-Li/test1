### Settings
These settings apply to all manufacturing orders that you have added in the Orders box.

#### Explosion
Here you select the explosion method:
- Structure (order oriented) – (default) If the order should be a structure order, the manufactured parts will be exploded (parts with the lot sizing rule Lot-for-lot or Linked requirement). Orders will be registered for all such parts in the entire structure with the same order number.
- Plain – With this alternative, no structure explosion will take place. The order is only registered for the part (one level) that is on the row.
- No material requirement – This alternative works in the same way as "Plain", but no material list is created for the order, only the operation list is created.
- Structure (all) – This alternative will create a structure order also for included manufactured parts that are stock driven. This is not done for the explosion alternative Structure (order oriented).

#### Check overload
If this setting is activated, an analysis is made of the concerned work centers’ loading when you save the order. The loading is only checked against actual orders, both with and without the current order, at week level for the weeks when the operations are planned to be run. In case of overload, the Overload tab will become activated. There you will find the work centers which have an overload. In the Orders box you see the column O and a warning symbol for the orders which created the overload.

#### Settings for CDT
The CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) is shown if you have activated the function check delivery times (CDT). It is activated with the system setting Apply check delivery times. By clicking the button you access a window where you can modify the settings available for CDT. These settings are also available as system settings where they are activated by default. If you modify the settings via this button, these modifications will apply right now for the manufacturing orders you have added in the procedure. If you restart the procedure, these CDT will be reset according to how they are configured in the system settings. This also means that changed settings will not be saved on order level.
When analyzing CDT for existing/saved manufacturing order in the Register manufacturing order procedure, the setting for Existing manufacturing order is used.
If you have made any modifications of these settings you should then perform a new calculation by using the button called Run the check of delivery times again ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png). You find this button on the function menu in the Orders box, or you can use the shortcut key Ctrl + R.
Read more about [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using monitor on the start page of the online help function.
