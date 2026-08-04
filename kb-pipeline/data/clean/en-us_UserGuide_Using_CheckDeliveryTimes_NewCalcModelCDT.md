## New calculation model for CDT
In version 25.6 a new calculation model for CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. is launched. This means several important changes. If you use Check delivery times, we recommend that you go over these changes.
Watch the video about the new calculation model (Only available in English).
| English |
|---|
|   |
If you experience problems viewing the video above, please try [this link](https://604-cn-east-2.cdn-vod.huaweicloud.com/asset/7a9f9c2212dba82bf7b2a8382478b8ec/40c39def6ff12c2112b0c8eab1976db8.mp4) instead.
The main improvements in this version regard these four things:
- The calculation is always based on today's date.
- Smarter calculation of available capacity with changed logic and a new setting.
- Better management of overload to prioritize existing orders before new ones.
- Changes to the user interface to make it easier to understand the results of the calculation.
In the below sections, the changes are described in more detail.
Please note that improvements to the new calculation model will keep being developed in upcoming versions. Next up are improvements in the following areas:
- Detailed analysis of registered/ongoing stock driven orders.
- Suggestions from sales forecasts for underlying parts taken into account.
- Detailed analysis of material that is supplied from other warehouses.

#### The calculation is always based on today's date
The delivery time is now always calculated from today’s date instead of from an entered delivery date. Previously, the calculation could vary depending on the selected (future) delivery date (e.g., because of schedule exceptions). Now, the result will be stable and always show the fastest possible delivery time.

#### Smarter calculation of available capacity
One of the most important improvements is that the system can now combine available capacity from the end of a day with the beginning of the following day. This is demonstrated in the example below.
New logic: The operation (red) fits by using the end of Monday + the start of Tuesday (existing loading shown in blue).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CDT1.png)
New logic.
Previous logic: The same operation was not inserted until Thursday.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CDT2.png)
Previous logic.
There is also a new setting called CDT additional days in the Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register. This setting determines if the loading can be spread out over multiple days. You can set how many additional days can be used.
In the example below, a longer operation is shown. For the work center WC2 in the example, 2 additional days have been entered. This means the operation can be distributed to Monday and Tuesday (two days that are not consecutive to the finish date on Thursday).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CDT3.png)
New logic with the CDT additional days setting activated.
Please note that an operation being divided onto non-consecutive days will likely mean that either additional setup times or that operations for existing orders will need to be rescheduled to earlier times.
CDT calculates the theoretical available capacity and shows it under the Loading tab. When the order is made, the system will however place the order on the last possible day without taking other capacity into account. This can lead to overloading on some days. In general, there will be enough available capacity in the additional days that you have entered.
Without the setting activated and using the previous logic, the finish date for the operation would have been calculated to Wednesday the following week.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CDT4.png)
Previous logic without activating the CDT additional days setting.

#### Better handling of overload
Check delivery times will always analyze the loading plan and redistribute potential overload for existing orders.
The comparison between the new and the previous logics can be described in total in the following way:
- New logic: Overloading will be moved back time-wise if there is capacity. If there is no capacity, it will be moved ahead in time. In this way, existing orders are prioritized over new orders.
- Previous logic: The overload was always moved ahead in time, which could delay already planned orders.
In the example below, Tuesday the 9th is overloaded. The loading is 16 hours, but the capacity is 8 hours.
Because there is 8 hours of available capacity on Monday the 8th, Check delivery times will distribute 8 hours of loading backwards in time for these orders, and then read the Monday as fully loaded.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CDT5.png)
Overload.
When the Check delivery times then calculates the finish date for an operation on a new order, the answer will be Wednesday the 10th because of the loading situation described above. Existing orders with overload will be prioritized over new orders. They were planned for the Tuesday but also take up the Monday.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CDT6.png)
New logic.
Using the previous logic, where overloading on existing orders was always moved ahead in time, the example above would have the following result: the new order would have been given a finish date of Monday the 8th, which in practice would have meant that existing orders were at risk of being delayed.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CDT7.png)
Previous logic.

#### Improvements to the user interface
- All results are shown in the same tab, regardless of whether the supply comes from purchases or manufacturing.
- Balance, order suggestion, and order are shown as separate rows, which makes it clear where the supply comes from and what quantity is supplied.
- When you move the cursor over a bar in the Loading tab, you see capacity, loading, and order number. This helps to make comparisons between the CDT result and the loading plan.
- A separate column Diff with material has been added. This way you can easily see if an operation is delayed because of lacking capacity or material shortage. This applies when the date difference is calculated using the setting Individual difference.
- The Date loaded from column displays if the delivery date has been loaded from the Planned finish or the New finish.
- The CDT settings are shown directly in the CDT window.

#### Miscellaneous
- New finish date (also applies to the Priority planning procedure) now takes number of machines per order into account.
- The setting called Check included stock driven part has been removed. Instead, stock driven parts are always checked.
- The date setting for existing manufacturing order, where you could select between New finish and Planned finish has been removed. Now New finish will always be used if it has been calculated by the net requirement calculation. Otherwise, planned finish will be used.
- The Manufacturing order info tab has been removed in order to simplify the user interface. You can instead use the Manufacturing order info procedure.
- The calculation for faster alternative will no longer suggest a delivery date. Because of issues with how that date was calculated, it will now be hidden. An improved calculation model for faster alternative will be launched in an upcoming version.
- For pool planning, the average capacity for the linked work centers will now be used.
