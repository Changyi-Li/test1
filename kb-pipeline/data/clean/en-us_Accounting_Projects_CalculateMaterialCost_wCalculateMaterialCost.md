## Calculate material cost
In this procedure you can calculate and adjust material costs for projects. This can be useful in cases where not all parts that have been purchased for a project have been used in the project, or the remaining parts that have been purchased for a project have been used in another project.
> The procedure only manages parts that have the setting Purchase on project and Stock update activated in the Part register.
When a part has the Purchase on project setting activated, cost is not loaded from the manufacturing order/customer order, but from the supplier invoice’s posting. This means that the entire cost of the parts is charged to the project the they were purchased for, even if not all of the parts have been used. The same applies the other way around when parts are used in a project that they have not been purchased on. In this procedure you can move both balance and material cost to/from a project by writing up or down the cost, by doing so you get the correct cost in the project as well as the correct balance in the Project list type in the Stock value procedure. Once you have saved your changes, a journal for these entries in the Print material cost calculation journal procedure. When the journal has been approved, you can see a voucher with the increased/reduced cost in the project.
List types

#### Write-down of costs
This list type is used to write down costs for projects. By default, projects are shown with the status Finished.

#### Write-up of costs
This list type is used to write up costs for projects. By default, projects are shown with the status Registered, In progress, and Finished.

#### Log
This list type shows a log of write-downs and write-ups calculated via the above list types. You can see by whom and when the calculations were done for each part and project. Here you are able to cancel calculations (write ups and write downs) if an entry has already been printed via journal, a new journal with a reversal voucher is created.
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
