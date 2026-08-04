### General

#### Order type
Here you can choose an order type for the maintenance. By default you will see the order type with the lowest row number. That is, the lowest row number of the order types with the basic type Maintenance registered in the Order types procedure.

#### Status
Here you see the status of the maintenance order as a symbol and in text. The status can be: Registered (1), Printed (2), Started (3), Finished (4), Post-calculated (5), Delivered (6), or Historical (9). The number in brackets is the status in digit form. It is not the main part that is shown, it is the status of the order. This status is based on the following set of rules:
- 1 – All parts in the order structure have status 1.
- 2 – There is one or several parts with status 2, but the other parts have status 1.
- 3 – There is one or several parts with status 3, but the other parts have status 1-2.
- 4-9 – The main part has status 4-9.

#### Project
If the maintenance order should belong to a project, you should here select which project. Projects are registered in the Project register procedure in the Accounting module. If the serial number has a project registered, this project will be selected automatically.

#### Start date
Here you enter the date when the maintenance order should start. The start date field is empty by default for new maintenance orders. It is calculated when the order is saved by using so-called "back planning" (in normal cases). However, it is possible to enter another start date even if the finish date is pre-filled. The manufacturing order will then be "compressed" or "extended" in time, in relation to the start date that would have been calculated. If you only enter the start date and delete the finish date, the system will apply so-called "planning ahead" and calculate the finish date instead. If the start date is in past time, the date will be displayed in red text.

#### Finish date
The finish date is the date when the maintenance order should be finished. The suggested finish date when the order is registered manually is: today's date + throughput time for the part in work days. The finish date of the order is the same as the last operation's Planned finish. If the finish date is in past time, the date will be displayed in red. A validation of the date will be made. A warning will appear if it is in past time or more than one year ahead in time.
If you are using the check delivery times function (CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.), you can also use the earliest finish date suggested by the CDT calculation (see the next field). Read about [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using Monitor G5 in the online help function.

#### Earliest finish date
In this column you can see the earliest possible finish date according to the CDT calculation. If it is possible to report the order as finished on the entered finish date or earlier, then the date is displayed in green color. If the earliest possible finish date is a date after the entered finish date, then the date is displayed in red color.
Using the button Use the dates suggested by the CDT ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) on the toolbar, you can choose to apply the earliest finish date to the field Finish date. If you click the button, there are four options. You can here choose to apply earliest finish date to the selected order row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) (Ctrl + D) or to apply the date to the orders on all rows ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace_all.png) (Ctrl + Shift + D). You can also choose to run the CDT again ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png) (Ctrl + R). If you have run the CDT you can open the result window from CDT with the CDT button. The result window from CDT is the same as you find under the CDT button on a regular manufacturing order.

#### Difference
Here you can see the difference between the suggested finish date and the earliest finish date. The difference is shown in number of work days, and in the same color as in the preceding field.

#### CDT
The CDT button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) is shown if you have activated the function check delivery times (CDT). This is activated with a system setting. By clicking the button you access a window where you can modify the settings available for CDT. These settings are also available as system settings where they are activated by default. If you modify the settings here, these modifications will apply right now for the manufacturing orders you have loaded in the procedure. If you restart the procedure, these CDT will be reset according to how they are configured in the system settings. This also means that changed settings will not be saved on order level.
When analyzing CDT for existing/saved maintenance orders, the setting for Existing manufacturing order is used.
If you made changes to the settings, you then have to do a new calculation by using the Rerun CDT button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png) (Ctrl + R). You find this by clicking the Use the dates suggested by the CDT button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) on the toolbar.

#### Explosion
Here you select the explosion method:
- Structure (order oriented) – (default) If the order should be a structure order, the manufactured parts will be exploded (parts with the lot sizing rule Lot-for-lot or Linked requirement). Orders will be registered for all such parts in the entire structure with the same order number.
- Plain – With this alternative, no structure explosion will take place. The order is only registered for the part (one level) that is on the row.
- No material requirement – This alternative works in the same way as "Plain", but no material list is created for the order, only the operation list is created.
- Structure (all) – This alternative will create a structure order also for included manufactured parts that are stock driven. This is not done for the explosion alternative Structure (order oriented).

#### Check overload
If this setting is activated, an analysis is made of the concerned work centers’ loading when you save the order. The loading is only checked against actual orders, both with and without the current order, at week level for the weeks when the operations are planned to be run. In case of overload, the Overload tab will become activated. There you will find the work centers which have an overload.
