## Operation follow-up
In this procedure you can compare planned and actual times for finished operations in a list. This is done in order to follow up if the planned times correspond with reality.
You can compare total times (including setup times and unit times), and you can also compare setup times separately. The total times can be shown with costs. The compared times are shown with an efficiency factor This is a measure of the outcome (result) between planned and actual time. Calculated according to the following: E= (Planned total time x Reported quantity/ Planned quantity ) / Reported total time. (E-factor), both in the detailed list and in the total list. An efficiency factor falling below 1.00 means that the operator has used more time than planned for the quantity that has been produced. The E-factor is shown in red if the value is less than 1.0. The result is based on the planned times for the operations and reporting in the manufacturing order log. Follow-ups made for setup times is only worthwhile in cases where you actually report setup time separately.
You can load data from one or several warehouses. You select warehouse in the toolbar of the procedure.
How the E-factor is calculated
The E-factor is used to get a quick overview of which orders, work centers etc. that are doing well and not. The E-factor (E) is calculated by using planned time for the reported quantity according to the following formula:
E = (Planned total time x Reported quantity/Planned quantity) / Reported total time.
If the planned and reported quantity is not the same, you cannot use the remaining sub-totals to calculate the average E-factor.
On the total row, you will then find an E-factor which is a weighted average of all the included sub-totals. This is calculated by dividing the sum of the E-factor x Reported time (for each row) with the total Reported time.
List types

#### Total time – Detailed
This list type loads planned and reported quantity, planned and reported total time, and efficiency factor (E-factor) for the total time. The list can be grouped by work center and by actual finish date.

#### Total time – Total
This list type loads planned and reported quantity, planned and reported total time, and efficiency factor (E-factor) for the total time. The list can be total by work center and by actual finish date.

#### Setup time – Detailed
This list type loads planned and reported setup time, and efficiency factor (E-factor) for the setup time. The list can be grouped by work center and by actual finish date.

#### Setup time – Total
This list type loads planned and reported setup time, and efficiency factor (E-factor) for the setup time. The list can be total by work center and by actual finish date.
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
