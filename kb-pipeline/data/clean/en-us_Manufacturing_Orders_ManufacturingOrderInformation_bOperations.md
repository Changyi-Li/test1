### Operations
This box displays the operations that are included in the selected part in the respective manufacturing order in the structure.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the function menu, you can go to related procedures, for example, Report measuring data for the marked operation row.
The Create monitoring task button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_create_monitoring_task.png) is found on the function menu if the Agent option is installed. By using this button you can create a monitoring task for the marked operation (as long as it is not reported as finished). There are three options for monitoring tasks which you access via the button. These are: Operation started, Operation reported, and Operation finished. You select one of these terms for the monitoring task. In the dialog which is then opened, you can configure Notification type and select who should be the recipient of notifications from the monitoring task. You can also change the name. By using the Save button, the monitoring task is automatically saved to the Monitoring tasks procedure. The monitoring task will be given the next available number in the number series.
The box contains basically the same columns as the [Operations](../RegisterManufacturingOrder/bOperations.htm) box in the Register manufacturing order procedure. Read more about these columns in the online help function for that procedure. Below you will find a description of the columns that are only available in this box.
Unique columns

#### Initials
Here you see the initials for the last reporting employee.

#### Recording status (Rec. s.)
This column is only shown if you have the option Work recording installed and there is at least one operation with a recording status. A button will then be available here showing a symbol for the recording status in question. The different recording statuses are In progress, Clocked out, and Standby. A tooltip is shown when you hover over the symbol, displaying the status in text. If you click the button you can see which employee has recorded, as well as date and time for the recording, and the status of the recording.

#### Priority of operation (P. op.)
In this column you see the operation's priority in the priority plan.

#### New finish
Here you see the new finish date calculated by the net requirement calculation. This requires that the setting New finish is activated in the Net requirement calculation You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. procedure.

#### Diff. (days)
This column shows the difference between Planned finish and New finish. This requires that the setting New finish is activated in the Net requirement calculation procedure.

#### Reported setup time and Reported unit time
Here you see the reported total time divided into reported setup time and reported unit time.

#### Link to case (C)
If the operation in the manufacturing order is linked to a case under the Actions tab in the Register case procedure, you will in this column see a link which you can use to open the case in question.
