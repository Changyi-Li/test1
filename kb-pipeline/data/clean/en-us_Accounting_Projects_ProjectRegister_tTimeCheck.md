### Time check
Under this tab you get an overview of all time (shown in hours) in the project. The hours are shown per cost type. These hours are planned, budgeted, forecast, and actually reported. Under this tab you will also see the expected result and a comparison to the result. In the footer of the table you find totals of all columns.

#### When you apply the Percentage of completion method
The stage of completion is calculated based on hours according to result in relation to hours according to forecast and is presented in the total field under the Result column.
Linking
The cost types Material – Manufacturing order, Subcontract – Manufacturing order, and Material – Customer order are not shown since they are not possible to budget/forecast/plan/report. Work – Manufacturing order is included.
In the table there is a drilldown function available on each row. There you find the saved detail records for each cost type and from here you can go to different procedures depending on which type the row is. For example, you can load the manufacturing order in question in the procedures Manufacturing order information and Post-calculation.
When you use the drilldown function for direct project reporting, you can decide if Total per activity or Detailed per reporting item should be displayed in the drilldown. This is configured for the activity in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project procedure.
You can go to/link to the Time check procedure with the records already loaded for the C/I type you have marked. The purpose of this is to see additional details about the records, for example which dates they are recorded/registered on.
Budget

#### Time
From the Budget/Forecast tab you load the hours which you have budgeted for the cost type. If no time has been budgeted, nothing will be shown.

#### Difference
Here you see the difference between the budgeted hours and the result. If the result is greater than the budgeted hours, then a negative value will be shown.

#### Difference %
This is calculated as budget − result ∕ budget. If the result is greater than the budgeted hours, then a negative value will be shown in %.
Planned/Ordered

#### Time
From manufacturing orders for the cost type Work – Manufacturing order the planned hours will be loaded. Other cost types can only have planned hours if there is a registered activity which is linked to the cost type. Then you can calculate planned hours. Cost types which have no activity in the project will not be included.

#### Difference
Here you see the difference between the planned and the result. If the result is greater than the planned hours, then a negative value will be shown.

#### Difference %
This is calculated as planned − result ∕ planned. If the result is greater than the planned hours, then a negative value will be shown.
Result
In this column you will see the actual reported times for the cost types.
For the cost type Work – Manufacturing order you will see total reported time from manufacturing orders which are registered with a project number.
For the other cost types you will see the reported time for the shown activities, that is, activities linkes to the cost types. Additionally, you see the direct reported hours for the cost type (hours registered without an activity).
Real time reporting of activities on project are also found. These are saved and read via direct reporting items.
Expected result
The definition of the expected result for time on the manufacturing order is:
- If no quantity is reported: remaining time = planned time − reported time.
- If a quantity is reported: remaining time = planned time for the remaining quantity.
For other cost types it is the basic data setting which decide how the expected result is calculated. With result + remain. we here mean result + remaining time on activities linked to the cost type in question.
Forecast

#### Time
From the Budget/Forecast tab the cost type's forecast hours are loaded. If no time has been registered, nothing will be shown.

#### Difference
Here you see the difference between the forecast hours and the result. If the result is greater than the forecast hours, then a negative value will be shown.

#### Difference %
This is calculated as forecast − result ∕ forecast. If the result is greater than the forecast hours, then a negative value will be shown.
Compile hours from multiple projects
For a main project it is possible to compile hours from the sub-projects. By default, only records from the main project are loaded, but by using the button Select project ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_project.png) it is possible to select additional records.
> In the Users procedure you can configure if you want sub-projects to be loaded by default when a main project is loaded.
Show in groups
By using the Show in groups button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_in_groups.png) you can choose if costs and income should be displayed grouped in costs/income groups. Costs/income groups are displayed in bold font and adds together the time for the included C/I types. You register costs/income groups under the C/I groups tab in the Basic data – Project procedure.
