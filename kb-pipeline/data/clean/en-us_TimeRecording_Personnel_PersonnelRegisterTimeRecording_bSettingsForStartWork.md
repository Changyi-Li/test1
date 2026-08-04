### Settings for Start work
In this box you find settings for the person in question regarding start of work in the recording terminal.

#### Work method
Here you decide how the person should work. If the person should only be able to change between work items, or be able to start and stop work items at will.
- Only change – (Default) This option means that the person changes work items in two steps. In step 1, choose to stop the work which the person has in progress, or choose to start a new work item. In step 2, choose to start a new work item, or choose to stop/end the their work item in progress.
- Start/Stop at will – This option means that the person freely can choose to start or stop one or several work items in only one step. This work method can cause inaccuracies in the time recording since total worked time and attendance time for the employee may differ.
The Method to select work table
In this table you see the methods available to select work. Here you mark the methods which should be Allowed and which of the marked methods that should be Default for the person. The following methods are available:
- Report number – If you check this option it means the person is allowed to start direct work based on the report number of an en operation.
- Priority plan – If you check this option it means the person can start direct work from the priority plan of a selected work center.
- Indirect codes – If you check this option it means the person can start indirect work using codes for indirect work.
- Project activity – If you check this option it means the person can start work from the project activity.
The Work center table
In this table you can add which work centers (and thereby which report numbers) the person should only be allowed to select among in the priority plan, and when starting work via report numbers.
You can also use the button Add from person ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_to.png) to add the same work centers as on the person you select under the button. This speeds up the work if you need to add the same work centers for multiple persons.
> Please note! If the table is empty, it is not possible for the person to select work center when starting direct work. However, it is possible to start any indirect work item via report number.

#### Show in priority plan
Here you determine if the work center should be displayed and be possible to select when starting direct work.

#### Default
With this checkbox you decide if the work center should be selected by default when starting direct work.

#### Capacity for
Here you are able to link the person as capacity for the work centers for work centers of the type Manual work and Machine. In the Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register procedure you can use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) next to the field Number of persons, to see which persons that are considered capacity for the work center in question.

#### Availability
For work centers of the type Manual work and Machine which the person is capacity for, you should enter the person's availability in the work center. This is entered in percent. The default value is loaded from the work center's availability factor. The field cannot be left empty if Capacity for has been marked.
The fields called Capacity for and Availability on persons linked to this work center are used to automatically calculate the capacity of the work center. The calculation then takes the work center’s basic time (not the employees' basic schedule), the employees’ availability and planned absence, into consideration.

#### Default filter
With this setting you can apply a default filter for the person in question. The filter will determine which operations will be shown in the priority plan for the selected work center.
- Prioritized – This filter will show you the prioritized operations.
- Ready to run (P) – This filter will show operations where the previous operation is finished, that is, where the column P (Previous operation) displays an F for Finished.
- Ready to run (M) – This filter will show you operations that either have cleared material or do not have a material requirement, that is, where the M column (Material availability) shows a C for Cleared material or is empty.
- Time horizon – This filter will show you the time horizon of the work center, in number of days. You will see the operations which have a date within the time horizon. Which date is used for the filtering is determined by the system setting Time horizon filters by. If you select an operation via the report number, you will see this operation regardless of the time horizon which applies for the work center.

#### Lock filter
If you mark this checkbox you can also lock the default filter so it can not be changed by the person in question. This means the filter field becomes deactivated (gray) in the recording terminal, meaning that the person can not change or delete the filter.

#### Allowed indirect codes
With this setting you can limit which codes the person should be allowed to select among during start of indirect work. If this table is empty it means all codes are allowed.

#### Allowed project activities
Here you can limit which project activities the person should be allowed to report on. If this table is empty it means all activities are allowed. Project activities must first be registered in the procedure Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project.
> Please note! A person can always report on project activities where the person's user is set as responsible or where the activities has been assigned to the person in question. This is possible regardless if those project activities are registered here as allowed project activities.
