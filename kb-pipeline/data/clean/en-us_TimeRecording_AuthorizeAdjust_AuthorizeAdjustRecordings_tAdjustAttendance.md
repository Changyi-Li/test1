### Adjust attendance
Under the Adjust attendance tab you can authorize and adjust attendance the personnel's recordings per day.
In the box to the right of the table for additions you can enter comments regarding the adjustment you make for the day in question. For example you can comment on why you have changed absence code or modified a recording time. If a person has entered a comment in the recording terminal, it is also displayed here.
By checking the OK by employee box, the employee can show that the day is OK to be authorized (used in TimeCard). This is a signal to the signer that the employee has completed his/her adjustments of recording items for that day.
If the day is locked for adjustments, it means you cannot adjust any of the day's attendance recordings. Then you will see a padlock symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png) to the right of the Authorized checkbox. You can activate this lock/block in connection to when salary export is made in the procedure Export of salary basis (to make sure no-one can adjust an attendance recording after the salary basis has been exported and for example been sent to the salaries department). You can also lock and unlock in the Lock/unlock attendance recording items procedure.
> An empty field in the Out time means that this is a recording item in progress. If you type a time in the field you will see a warning saying the recording item in question then will become ended. That is, the employee will no longer be clocked-in if you make this change for an attendance recording.

#### Schedule number
Here you see the schedule which applies for the person in question. Using the button Change schedule ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) to the right of the field you can select another schedule in order to see and adjust attendance recording items for that schedule. It is possible to change overtime schedule for a specific day, that is, which overtime schedule should apply when working outside the regular time on the attendance schedule. To do this you must unlock the field New overtime schedule and thereby disconnect from automatic change when changing attendance schedule. It is possible to change overtime schedule on any day in the schedule cycle. For example, if the Friday should have a different overtime than other workdays in the week.

#### Calculate overtime
With this setting you determine how the overtime calculation should apply: for all overtime or only after fulfilled daily working hours.

#### Authorized
With this checkbox you decide if the selected day should become authorized when you save.

#### Log
By clicking this button a log is shown containing the day's attendance recording items. If you have activated the system setting called Activate site recording, a log over the sites is also shown.

#### Salary types
By clicking this button you see the salary types used for the attendance recording items and the number of hours recorded per salary type. You can add and delete salary types and modify the number of hours for the salary types you have added on your own. You also see salary types from additions here. You cannot change the salary types that are generated from the times on the rows for the day in question. These can only be adjusted by adding positive and negative records in the dialog box.

#### The Attendance recording table
In this table you see the attendance recording for the selected day. Here you can adjust these recording items. For a recording item which is in progress, the field called Out is empty.
You can also add and delete recording items. Recording items can be attendance, absence, and breaks, shown with times In and Out. Attendance recording and absence recording items cannot overlap. Break recording items must be within the break flex zones.
The Time column shows the worked time between clocking in and clocking out (minus break time entered in the schedule). By using the button Calculate ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) in the function menu, you can update that time on the rows.
For an added absence recording item you must enter an absence code. The absence code can also be changed for existing absence recording items.
In the Deduct from OT/Flex column you can mark the checkbox if you want the time on the row to be deducted from overtime. This only applies to absence recording.
The columns Overtime before and Overtime after becomes available if clocked in time is before schedule start or if clocked out time is after schedule end. Here it is then possible to select overtime type. For attendance recording after midnight, the overtime schedule for that day will be applied.
Below the table you see a total of difference between planned schedule time and actual recorded time. You also see totals of attendance, absence, overtime, flex time, and worked hours, for the selected day. Difference, if any, between reported attendance and reported time on work items, is also shown.

#### The Additions table
In this table you see the additions for the selected day. Here you can adjust the addition quantity, time "From" and "To" for which the addition should apply, and a comment for the addition. You can also add and delete additions.
An addition can for example be compensation for travel time in hours, mileage allowances, allowances for expenses full day/half day, or other expenses.
The additions you can use are the ones manually created in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Attendance procedure. There are also two additions included in the system. These are for Positive time bank adjustment and Negative time bank adjustment. These cannot be used here. They are intended to automatically create transactions from the Update time balances procedure.
