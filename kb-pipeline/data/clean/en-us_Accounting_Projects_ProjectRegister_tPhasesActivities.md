### Phases/Activities
Under this tab, the phases and activities of the project is shown. You can for example see information regarding who is responsible for the activity, reported hours, when the activity is planned to start, and when it is planned to finish. At the bottom of the tab you see totals of planned time, reported time, and remaining time.
You can expand a phase using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to the left of the phase number. In the expanded mode you can see the activities belonging to the phase. You can use the button Expand all on the function menu ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) (Shift + F8) to expand all of the phases at once.
With the button Show lead time chart ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_lead_time_chart.png) you can open the lead time chart in a separate floating window. Read more about the [lead time chart](tLeadTimeChart.htm).
If you in a quick and easy way want to report time/cost for an activity in the activity list in the project, then you can use the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) button and link/go to the procedure Direct project reporting with the record you have marked already loaded. You can also double-click on the row.
Add activities/phases
By using the regular function buttons you can add, insert, and delete rows for activities/phases.
With the button Add activity template ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_template.png) you can add an activity template at the bottom of the list. With the button Insert activity template ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_template.png) you can insert an activity template above the row you are on in the list. When you use these functions a dialog will open where you enter which template to use and the start and end date. Activity templates are handled in the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project.
Change template
It is possible to change activity template with the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) next to the field Activity template on the header row. It is possible to change template if the project is saved, as long as nothing has been reported on the activity. When something has been reported on an activity, it is no longer possible to change template.
When you change template for a project, the start and end times of the activities should be calculated using the start date of the project as a basis. And also using the queue time, lead time, and project responsible from the template. Start date is automatically set according to the project's start date and using the template the end date is calculated. However, it is possible to change the end date and then the start date will be recalculated. The calculated start and end date will be the project's new date under the Main.
> Remember choosing start and end date according to the start and end time of the project. When adding/inserting activity templates, today's date is by default used as start date.
Generate activities via template in new project
If you have registered templates (in the procedure Basic data – Project) for the project type in question, then these will be generated when you create a new project. The activities will then get start and end date automatically calculated by using the start and end date of the project + the lead time and queue time which you entered in the template. The person responsible for the activity and the phases are also entered according to the template.
Change start and end date for the project
In the topic [Project time](bProjectTime.htm) you can read about start date and end date and how the dates of the activities will be affected by changes made.
Phases and Activities
For new phases and activities added separately (that is, added outside a template), information for the activity/phase is loaded according to the settings in Basic Data – Project. If the phases and activities are taken from a template when creating a new project they will get values according to the template.
For an activity list it is not mandatory to have a phase. It is possible to only have activities in a project.
The following fields must be entered for a phase

#### Phase/Activity
Here you can select phases from the Phases tab in the procedure Basic data – Project.

#### Name
You can change the name of the phase.

#### Responsible
Here you see a person default set as responsible according to the settings in the basic data. It is only possible to select users which have the setting Can be set as responsible for activity activated in the Users procedure.
The following fields are shown but cannot be edited

#### Planned time
Here you see the total of planned time from the underlying activities.

#### Planned start date
In this column you see the earliest start date of the underlying activities.

#### Planned finish date
Here you see the latest planned finish date of the underlying activities.

#### Status
This follows the underlying activities:
- Not started – This status is shown if none of the activities has been started.
- Started – This status is shown if any of the activities have been started.
- Finished – This status is shown if all activities have been finished.

#### Reported time
Here you see a total of the reported time from the underlying activities.

#### Actual finish date
Here you see the latest actual finish date of the activities.

#### Print
This checkbox follows the underlying activities. If this Print checkbox is checked for any of the activities, the phase will also be marked. With this checkbox you determine if the activity should be shown on the project report.
The following fields can be edited for an activity

#### Phase/Activity
Here you can select activities from the Activities tab in the procedure Basic data – Project. Activities which are excluded cannot be selected.

#### Name
Here you can change the name of the activity.

#### Responsible
Here you see a person default set as responsible according to the settings in the basic data. It is only possible to select users which have the setting Can be set as responsible for activity activated in the Users procedure.

#### Preceding activity/phase
Here it is quick and easy to create a link/dependency to the preceding activity. It is possible to select one or multiple activities as preceding activity. A preceding activity with a dependency can also be an activity in a different phase. As soon as you have created a dependency between activities, you will no longer have the option to create dependencies between phases and the other way around. It is not possible to mix dependencies between activities and phases in the same list. When a preceding activity/phase is entered, the start date and end date of the activity will automatically be affected, depending the dependency type entered. An activity/phase that has a preceding activity/phase cannot be reported if the preceding activity/phase has not been finished/started (depending on the dependency type).

#### The Dependencies button (D)
The Dependencies button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) becomes activated if you have entered a preceding activity. Here it is possible to configure multiple settings.
Here you see which activities that are preceding and you can also select [Dependency type](bRelationTypes.htm) between the activities.

#### Comment
This comment is loaded from the basic data. It is possible to edit the comment.

#### Files
Linked files are by default loaded from the basic data. You can add and delete files.

#### Planned time
The planned time is by default loaded from the basic data.

#### Planned start date
The planned start date is by default loaded from the basic data.

#### Planned finish date
The planned finish date shown here is set according to start date + the lead time of the activity.

#### Status
The following status can be used for an activity.
- Not started – This status is used if none of the activities has been started.
- Started – This status is used if any of the activities have been started.
- Finished – This status is manually selected by the user if all activities have been finished. If you have selected this status, the Actual finish date will be set to today's date and in the Performed by column the logged in user will be entered. These fields ate possible to edit.

#### Remaining time
Here you can update the time remaining on the activity if you find you have to replan an activity and postpone the finish date.
The remaining time is automatically set to the same as the planned time when you create an activity. Each reporting you make is then deducted from this time. However, it is possible to enter the remaining time again. It will then continue to deduct at each reporting, from the value you entered.
This affects several procedures, such as e.g. Direct project reporting, Activity list – Project, and Report activity – Project.

#### Delegate
This column is only available if the module Time recording is installed in your system. By clicking the D button a window opens where you can delegate the activity to one or several employees by adding them in the table. With the setting Only employees in the list can start delegated work you can decide that no other than the employees to whom you delegated the activity, will be able to start the activity. The purpose of this is to dedicate the activity to one or several employees. The activity can the be started and finished/stopped in the Recording terminal.
When the activity is delegated to an employee, the employee number will be shown on the button. If the activity is delegated to more than one employee, then the text Multiple will be shown on the button. A tooltip for the button displays the employee numbers and names in text.

#### Print
With this checkbox you determine if the activity should be shown on the project report. This checkbox is by default set according to the basic data.

#### Reminder
Here you determine if the activity should generate a reminder. A reminder is sent as an internal message in Monitor ERP to the person registered as responsible for the activity.

#### Calendar
Here you determine if this activity should be synchronized with a calendar program. Using the Calendar button, the user who is set as responsible for the activity and the user that the activity has been assigned to are able to create a calendar booking which is linked to the activity. In the dialog box that opens, the Sender/Responsible, Location of the meeting, Date & time, and Duration in hours are entered.
Under Participants you can enter the e-mail addresses of both internal and external contacts. An e-mail with an invitation is sent to the addresses you entered when you save the activity. Using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calendar_next.png) Add e-mail addresses of employees with delegated activity, you can load the e-mail addresses of all the users assigned to the activity.
When Calendar is activated, a check is also made to make sure there are e-mail settings in the system, and settings for the user who is set as responsible for the activity. If any information is missing for e-mail settings in the system or for the user, a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is displayed in the column. A tooltip for the symbol informs you of what information is missing.
E-mail settings
- In the Users procedure, in the E-mail section, the settings: E-mail address, User name, and Password, should be configured. The setting E-mail method can be set to Client based, via Microsoft Outlook if the user wants to use Outlook locally for calendar synchronization and to send e-mails.
- In the System settings procedure, in the E-mail section, under the System overall tab, you will find: E-mail sending method, Server address (Exchange/Exchange Online), Port (Exchange/Exchange Online), and Use SSL (as Yes or No, depending on whether or not the e-mail server requires it).
The following fields are shown but cannot be edited

#### Reported time
Here you see the accumulated reported time. When calculating/data mining in the project, this column will become updated with the total reported time for the activity in question.

#### Actual finish date
This date will by default be set to the date when you select the status Finished.

#### Performed by
In this column the user who is logged in and enters the status Finished for the activity, will be entered.
