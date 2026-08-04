### Phases/Activities
In this box you enter information about all planned activities for the case. The default phases and activities depend on the template entered in the header. Some activities are conditional for the specific case. E.g. It might be an activity to return parts to the supplier that you only activate for the specific case.
An activity always belongs to a phase. Phases and activities can be inserted, deleted, and modified after the case has been saved. You can either report the activities in this procedure or in the Tasks view in the Message center (on the title bar of the program window). You can use drag and drop to change the phase order.
With the Insert activity template button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_template.png) you can add an activity template in the list. Activity templates are handled in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Case procedure.
The following fields must be entered for a phase

#### Dependency types
The following dependency types exist between phases or activities:
Finished – Start
Activity B cannot be started until activity A is finished.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/RelationTypeFinishedStarted.png)
Started–Start
Activity B cannot be started until activity A is started.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/RelationTypesStartedStart.png)
> Please note! There is a limitation of dependencies, a case can either have dependencies between activities or dependencies between phases.

#### Phase/Activity
Here you can select phases among the ones registered under the Templates/Default tab in the Basic data – Case procedure.

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
This checkbox follows the underlying activities. If this Print checkbox is checked for any of the activities, the phase will also be marked. With this checkbox you determine if the activity should be shown on the report.

#### R (Reminder)
Here you determine is a reminder should be sent.

#### C (Charge)
Here you decide if the activity should be charged.
