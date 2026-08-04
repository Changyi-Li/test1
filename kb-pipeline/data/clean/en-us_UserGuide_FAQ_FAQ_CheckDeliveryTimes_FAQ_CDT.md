### FAQ – Check delivery times
What is check delivery times?
The check delivery times (CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.) is a function in Monitor ERP which is mainly used to control and calculate the delivery date of a customer order. The CDT takes existing requirements and reservations into consideration, as well as available capacity and material. The check is made in connection with the order being created.
The purpose of CDT is to offer better master plans with reasonable delivery dates on customer orders and reasonable finish dates on manufacturing orders. However, it is optional to use the delivery dates and finish dates calculated by the CDT.
You can read more about [Check delivery times](../../Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) here.
How do I get started with Check delivery times?
To apply check of delivery times (CDT) you need to activate the system setting Apply check delivery times by selecting the option Yes (in red). When you activate this system setting, additional settings will become available below (see image).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/SystemSettingsCDT.png)](../../../../Resources/Images/FAQ_Snippet_Images/SystemSettingsCDT.png)
With these settings you determine what the CDT should check by default, regarding capacity availability (in blue) and material availability (in green). By default it is set to check capacity availability in work centers included in CDT (bottleneck work centers) and to check material availability.
Read more about each system setting in the Check delivery times topic in the online help function for the System settings procedure.
However, you can override the system settings for CDT for a specific quote, customer order, or manufacturing order, by using the button CDT in the respective procedures (see the image below).
Use safety time determines whether the part's safety time should be included in the calculation.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/FAQ_Snippet_Images/SettingsCDT.png)](../../../../Resources/Images/FAQ_Snippet_Images/SettingsCDT.png)
