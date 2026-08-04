## Time bank log
In this procedure you can load a list of logs containing transactions made in time banks.
All logs contain information about balance changes, closing balance, log date, and actual date. This means the logs have two date fields. Each time a time balance is changed, the change is logged showing date and time, and the new closing balance. In cases where there are more than one day of absence to deduct from the balance, one log per day will be created. For example when an employee has used two days of comp (compensatory leave).
Example: You adjust a recording item on 02/15/2020 at 09:23. The date of the adjusted recording item will be set as actual recording date. The log date is set to 02/15/2020 09:23.
A useful application of the procedure is to select the list Historical balance with the setting Date alternative configured to Actual date set to the final day of a certain month. Then you can see the actual balance for each respective time bank for the last day of the month in question. These balances include all adjustments made on days prior to the selected date, even if the adjustmens where actuallly made much later.
List types

#### Standard
This is a standard list which shows all logs in the time banks. The list is grouped by employee number.

#### Historical balance
In this list type you see historical balances based on the log date or actual date selected in the Settings box.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
