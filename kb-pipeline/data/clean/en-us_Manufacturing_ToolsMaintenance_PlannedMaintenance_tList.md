### The List tab
The list shows the serial numbers that have planned maintenance according to the selections you have made.
The most common use of this list is to make a selection to show the serial numbers where it is time to perform maintenance. But by choosing to show all rows (including the ones which are not supposed to be performed now), you will get a good overview of the entire maintenance plan.
The list is grouped by maintenance type. You register maintenance types in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Maintenance procedure.
Each row in the list represents a type of maintenance for a serial number, that is, a certain machine or a certain tool.
In the Trigger column you see a date or a quantity, depending on how the maintenance is triggered. For maintenance that should be performed at regular time intervals, the Trigger value shown is calculated as the date of the most recent maintenance + the interval. If no maintenance has been performed, the Trigger value column will show: the date when the serial number was created + the interval. For maintenance which is based on one of the serial number's counters, the Trigger value will show: the meter reading at the most recent maintenance + the interval. For a row with a triggered required maintenance, the triggering value is shown with a red background.
In this list you see the next reservation of the tool and which order or order suggestion that has reserved the tool.
Values for Cycles since service, Distance since service and Run time since service, display how many cycles or how long of a distance/run time has passed since the most recent maintenance.
If there are planned maintenance items, you can see the number of active maintenance items. You can then expand the row and see more information about these maintenance items.
You see the date and service number (consecutive number) for the most recent reporting.
There are multiple columns which show where the serial number is located. The information shown in the columns is determined by the setting configured for the serial number under the Location/site section in the Serial number A serial number is a number that is used for traceability for parts on entity level./Batch A batch is the set of components/products manufactured at the same time and made from the same original material. procedure. If the serial number is available at a location at the moment, that information is also shown. This information helps if you should, for example, collect a measuring tool for calibration. You can also filter by using the information if you, for example, want to see all maintenance items per department or per work center.
List functions

#### Finish date
Here you see the suggested finish date for the maintenance. This date can be changed for each maintenance item on the respective serial number.
For maintenance items governed by interval days, the finish date will be calculated as Last reporting date + Frequency.
For maintenance items governed by other terms, for example, number of cycles, the finish date will be calculated as Today’s date + Lead time Number of days between ordering date and delivery date. Normally used for purchased parts. for order. This is the same way it is calculated as when you manually register a regular manufacturing order.
The calculation will primarily be based on the part in Use BOM and routing from on the maintenance plan. Secondarily, it is based on the part in Use BOM and routing from on the maintenance template. And thirdly, it is based on the part with the serial number.

#### Create maintenance orders
By marking the Create maintenance order checkbox and clicking the Create maintenance orders button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) (Ctrl + R), you create a maintenance order for the maintenance item on the row.
A condition for this is that the maintenance template in the maintenance plan has a part with BOM and routing selected in the Use BOM and routing from field in the Maintenance plans procedure. Alternatively, that the part with the serial number has a BOM and routing. Otherwise an error message is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) saying that the part is missing BOM and routing.

#### Maintenance in progress
By checking the Maintenance in progress box and saving, the status of the serial numbers you are working on will be updated. Then you can also enter a Message regarding the action that is being saved for the serial number.

#### The Function menu
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the function menu, you can go to related procedures.
- You can go to the Serial number/Batch procedure to, for example, configure status of the marked serial number.
- You can go to the Report maintenance procedure to report the maintenance directly.
- You can go to the Register maintenance order procedure if you work with maintenance orders, and you can either create a maintenance order or load an existing order.
- You can also go to the Form templates procedure to be able to make changes in the form linked to the maintenance.
- You can also go to the Part register procedure for the part linked to the serial number. There you can, for example, see the planned use in the planning window.
