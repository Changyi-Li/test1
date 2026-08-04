### Scheduling
In this box you schedule net requirement calculations. You can select if continuous net requirement calculation should be used. You configure the log level, determine if New finish should be calculated (when using CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.), and configure settings for notifications. Under the Selection tab you select the parts that should be included in the calculation. Underlying parts included in other parts are also included in the calculation, even if you have not selected them.
Net requirement calculation
A scheduled Net requirement calculationYou use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. is run for all selected parts. The calculation finds shortages and creates suggestions for manufacturing and purchases of material. You select the days and time when the calculation should run. You can see statistics and history from previous runs.
By clicking the Copy row button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) you can add scheduling of Net requirement calculation, if you want it to start at different times and different days.
With the Delete row button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) you can delete scheduling items you have added.
Continuous net requirement calculation
A continuous net requirement calculation is only run for parts which have been modified since the last netting and the last continuous net requirement. This type of run is much faster than the regular run that is made for all affected parts in the selection.
The following events result in that the part is considered changed/modified, and thereby includes it in the continuous net requirement calculation:
- Modified customer order row
- Modified purchase order row
- Modified manufacturing order
- Modified sales forecasts
- Change in balance
- Modification of BOM and routing
- Changed planning settings for the part
- Change in supplier link
The continuous net requirement calculation is run in a time interval which you enter in minutes. You can also choose if suggestions should be cleared before each run.
The next start time is calculated based on the entered interval and the last continuous net requirement calculation. You find more information by using the History ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button. There you see the date and time when the last run was finished.
Example: You want the continuous net requirement calculation to run every two hours at 13:00, 15:00, 17:00, etc. Then you enter 120 minutes as interval and save this in the procedure at such a time, that is, at 13:00, for example.
> Please note! If the Monitor ERP server is restarted, the time which calculates the next start time will be reset. This means that if the server has been restarted you have to go to this procedure, enter a different interval and save at the time you want the interval to start.

#### Active
With this checkbox you determine if the requirement calculation should be active.

#### Days
(Net requirement calculation) Here you select which days of the week the net requirement calculation should be run. The dates for these days are loaded from the current company calendar and are shown in the history.

#### When
(Net requirement calculation) Here you select the time when the net requirement calculation should start on the selected days. The time is based on the computer date and time on the Monitor ERP server.

#### Interval
(Continuous net requirement calculation) Here you see/enter the time interval between the runs. It is shown in minutes. The start time of the next continuous net requirement calculation is calculated based on the last run continuous net requirement calculation. A manual run will not affect the start time for the next interval of continuous net requirement calculation.
> Please note! If the Monitor ERP server is restarted, the time which calculates the next start time will be reset. This means that if the server has been restarted you have to go to this procedure, enter a different interval and save at the time you want the interval to start.

#### Log level
Here you select what should be logged for the calculation, the different levels to select among are: Closed, Error, Warning, Information, and Debug.

#### Clear suggestion
(Continuous net requirement calculation) This setting is activated by default. This means that the manufacturing and purchase order suggestions for the parts which have been modified, will be deleted before the calculation by new, more up-to-date suggestions. If the suggestions are not cleared, this means that the suggestion still remains even though the requirement has decreased or is completely gone. If the requirement has increased, an additional suggestion will be added to handle the difference between the requirement and the existing suggestion.

#### New finish
If you use Check delivery times (CDT), this checkbox is available. Check this box if the net requirement calculation should calculate New finish which should be saved on all affected operations and manufactured parts.
New finish can also be calculated temporarily by the CDT in the Register customer order and Register manufacturing order procedures, but this is not saved for the affected operations and manufactured parts.

#### Disregard lead time on part
With this setting you determine if the calculation of suggested delivery date in the list should disregard the lead time of the parts and instead be based on the actual requirements.
When this setting is activated, the suggested delivery date is calculated as the requirement date minus the safety time. This setting is not activated by default, and this means the suggested delivery date is calculated as the requirement date minus the safety time and minus the lead time. If Disregard lead time has NOT been selected and the date falls within the part’s lead time, the suggested delivery date will set according to the part’s lead time.
If Disregard lead time has been selected and the date is within the part’s lead time, the suggested date will be used as the requirement date.

#### Merge suggestions
If the setting Disregard lead time is active, you can choose how the purchase order suggestions should be merged (aggregated). You can choose between Past + Within lead time and In past time. Past + Within lead time is selected by default.
- Past + Within lead time – purchase orders are merged (aggregated) into a suggestion for the material requirements In past time and Within lead time, and then into separate suggestions for the material requirements that are Beyond lead time.
- In past time – provides a merged (aggregated) purchase order suggestion for the material requirements In past time, and then separate suggestions for the material requirements that are Within lead time and Beyond lead time.

#### Deduct forecast
With this setting you decide if sales forecasts on the selected parts should be deducted with the customer order's quantity prior to the net requirement calculation. The calculation is made for the parts with the Periodic intervals option.

#### Status
In this column you see the status of the net requirement calculation.

#### Statistics
By using the button Statistics ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), a dialog box appears. Here you see detailed information about how many suggestions were generated and information about how long it took to perform the different parts of the last net requirement calculation. In the dialog box, you also find the button Warnings ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). By using this button you see any warnings that have occurred during the last run.

#### Last run
Here you see the date and time when the last net requirement calculation was finished.

#### Run
By using the Run button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) you manually start a scheduled or a continuous net requirement calculation. If you start a manual run, two saved runs will be logged in the history with the same times.
A manual run will not affect the start time of the interval for the next continuous net requirement calculation.

#### Notify
Here you determine the recipients of notifications and when they should be shown. You can e.g. configure that all users registered as Planners will get a notification/message each time the calculation is started and finished.

#### History
Under the button History ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see a log containing earlier requirement calculations. In each log you can see date and time for the calculation as well as the status of the run. If you place the cursor over the status symbol, a tooltip will show information about how long the calculation took and how many suggestions (manufacturing and purchase) were generated. For each log you also find the button Statistics ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) (see above).

#### Clear all suggestions
All order suggestions will be deleted if you click this button.

#### Cleared saved New finish
If you click this button, the new finished saved on operations and parts during the last net requirement calculation will be deleted.
