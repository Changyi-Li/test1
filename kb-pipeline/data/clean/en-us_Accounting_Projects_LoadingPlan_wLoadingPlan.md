### Loading plan – Project
In this procedure you can see how different project activities generate loading over time. The loading is shown on a time axis, either per month, week, or day. Week is selected by default, since it is the most commonly used option.
Loading is created based on the following information in the Project register:
-   
Start and finish time for activities (lead time)
-   
Remaining time on activities
> To display loading, it is not enough to have registered activities with a start and finish date. You must also have planned times registered for the activities.
You can see the state of the loading for example for one or several projects, persons, or activities at the same time, depending on the settings made under the Selection tab. The loading list is grouped per person responsible for activity, but at the same time you can also show the list as total per project, phase, activity, responsible for activity or main project.
In the loading plan, the remaining time on the activities will be evenly distributed. For example, an activity with a lead time of 5 days and 5 hours remaining time will create a loading of 1 hour per day. That is, the time is evenly distributed between the start date and the finish date. However, when there is a lag, the already reported time will be deducted from the start date and onwards. The remaining time is distributed up to the finish date of the activity. The loading is calculated taking the calendar into consideration to avoid loading to be placed on weekends.
Example – Calculation of loading in connection to a lag 
The lead time is 5 work days, Monday to Friday.
The activity has 25 hours of planned time, 5 hours of reported time, and 20 hours of remaining time.
In this case, the remaining 20 hours should not be evenly distributed between the start date and finish date. Instead, the already reported 5 hours should first be deducted from the start date and ahead, and after that the remaining time is evenly distributed. This means that instead of 20 hours distributed as 4 hours per day from Monday up to and including Friday, the distribution will be 5 hours per day for Tuesday up to and including Friday. The 5 hours already reported will be deducted from Monday.
At present, the loading will not take the employee's schedule into consideration. However, the schedule is considered when calculating the employee's capacity. You can also choose if capacity should be displayed in relation to the loading. To be able to display capacity, settings have to be configured per user. These settings are configured in the Users or User list procedure where you can choose if capacity should be calculated based on schedule or fixed capacity.
It is not possible to update the loading chart, but under the List tab you can replan the planned start time and finish time of the activities, if you have chosen to make the list possible to update ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_list.png) on the toolbar.
