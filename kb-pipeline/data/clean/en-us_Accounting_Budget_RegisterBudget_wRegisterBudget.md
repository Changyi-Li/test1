## Register budget
In this procedure you register budgets. The procedure is, in distinction from other registration procedures, built as an updateable list procedure. The budgets can be printed and exported. You can either register new budgets or create budgets by copying data, for example copying of budget and result from previous years.
It is possible to register multiple parallel budgets for the same accounting year. In the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Budget you first have to decide the number of budgets that should be possible to handle.
You select the list by accounts, cost centers, etc. When you load data to the list you will see if there already is a budget, otherwise the list will be empty. You can manually enter budgets row by row (compared to the Opening balance procedure).
If you want to register a new budget, but you do not want to register the account strings manually, then you can load a list with empty budget rows and there enter budget amounts. This can also be done if you wish to register a budget for example for a specific cost center. Then you can create a list with empty rows with that cost center entered. This is determined by the settings under Generate budget rows.
The budget chart which should be used during registration is by default loaded from the chart of accounts, but it is also possible to select from a chart you enter under the Selection tab.
You register and handle budget charts in the Basic data – Budget or in the Budget charts procedure in the General registers module.
Budget charts can be also imported separately using a file in the Budget import procedure.
It is possible to work with a budget in an Excel sheet and then import that file. The file then needs to be divided according to the columns required by the budget import. You can also export budgets from the list.
List types

#### Register budget
This list type is used for registration of budget by entering values in the list.

#### Copy budget
This list type is used to create a budget by copying from result or budget.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
