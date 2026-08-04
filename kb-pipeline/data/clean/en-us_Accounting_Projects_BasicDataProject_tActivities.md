### Activities
Here you register the activities that can occur in different projects. Activities can then be added to the projects you register. You can also use activity templates in projects. These consist of different sets of phases and activities.

#### Number
Here you can see the number for the position of the row. This field is numerical. A new row will by default be assigned the next available number. The table/list is sorted by this column. A number is unique and cannot occur on more than one row in the table.
The row number be changed. If you change the row numbers you should re-sort the column via the column heading in order for the rows with changed row numbers to be shown in the correct place.

#### Alias for BI
Here you can change the record's alias. This alias is used during data mining from records in the database in Monitor ERP to the database for Business Intelligence. The default value of alias is the same as the record's code/number, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on multiple records, for example customers, then data from these will be merged into a joint record in the database for business intelligence.
You activate alias for BI with the system setting Use alias when exporting to Business intelligence.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Responsible
Here you enter who is responsible for the activity in question. It is only possible to select users which have the setting Can be set as responsible for activity activated in the Users procedure.

#### Planned time
Here you can enter the time planned for the activity. This should be entered in hours.

#### Lead time
In this column you enter for how long the activity will last. This is entered in number of days.

#### Queue time
Here you can enter how many days should pass before it is possible to start this activity. Queue time Queue time refers to time which is added to create a gap between two operations when the manufacturing order is created. It is normally stated in days, where 1 means the rest of the commenced day will be the "gap". 2 means the rest of the commenced day plus 1 full day will be the gap. For work centers with hourly planning, the queue time is instead entered in hours. The entered queue time will be added before the operation which has a value entered. = 0, means that the following activity's start date will be the same date as the end date of the preceding activity. Queue time = 1, means the day after, and so on.

#### Cost type
You can link the activity to a costs type which you have entered under the Costs/Income tab. This is useful for example if you want to see the cost when you report an activity for a project. Then the cost will automatically be calculated. Also, all hours reported for the activity will automatically be recorded as a cost for the project via the selected cost type.

#### Excluded project types
Here you can select which project types should be excluded for the activity.

#### Report as direct time
With this checkbox you decide if the activity should be reported as direct time.

#### Drilldown info
Here you can select – per activity – if the drilldown should show Total per activity or Detailed per reporting item. If you select the "Detailed per reporting item" option, you will also see comments, if any, which have been entered for the reporting item. This applies to costs reported via project activities, direct project reporting items, or via the TimeCard. These costs can be displayed in detail when using the drilldown function on the cost types under the Costs/Income tab and Time check tab.

#### Active
Here you determine if the activity is active or not. Inactive activities cannot be added to new project templates and new projects.
Please note that any changes made to project templates are not automatically synchronized to existing projects.

#### Comment
You can here enter a default comment for the activity. The comment will also be inherited to a template and to the Project register if the activity is selected.

#### Files
It is possible to link files to the activity. The files will also be inherited to a template and to the Project register if the activity is selected.

#### Print
With this checkbox you determine if the activity should be shown on the project report. It is checked by default for new activities.

#### Reminder
Here you determine if the activity should generate a reminder. A reminder is sent as an internal message in Monitor ERP to the person registered as responsible for the activity.
