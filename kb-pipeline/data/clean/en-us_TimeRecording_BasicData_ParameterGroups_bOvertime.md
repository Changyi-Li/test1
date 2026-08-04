### Overtime

#### Allow overtime
With this checkbox you determine if overtime should be allowed for the group in question. Other settings in this box are only available if Allow overtime is activated.

#### Overtime in flex zone
With this checkbox you determine if overtime recording should be allowed within the flex zone. If time is recorded which is outside the regular working hours but within the flex zone, this setting makes it possible to choose overtime instead of flex time. This setting is available if you have checked the Flex time checkbox in the box called Flex time settings.

#### Overtime limit before and after
Here you enter the overtime limit (in minutes) for overtime to be registered when clocking in and clocking out before and after the regular working hours. These settings are available to prevent minor overtime items to be recorded each time you work longer than the regular working hours. If it is not allowed to record overtime in flex zone, both the overtime limit and the flex zone must be passed if it should be possible to record overtime.

#### Rounding overtime
With this checkbox you decide if the overtime should be rounded off. If you check this box, the following two settings will become available.

#### Round off to
Here you enter the time in minutes which should be used when rounding the overtime. If you for example enter 6 minutes in this field it means a rounding down of the recorded overtime will be made to the nearest 6 minute interval. Example: The working hours end for an employee at 16:00. The employee clocks out at 16:27, that is, 27 minutes of overtime. Then the overtime will become rounded off to 24 minutes.

#### Add rounded overtime to time bank
With this setting you determine if the rounded off time should be added in a time bank. No is selected by default in this setting. You can also select the option All time, or the option Time within flex zone which means only time rounded off within the flex zone be added to the time bank. To be able to add the rounded off time to a time bank, you must also select such in the next setting.
Example: If the employee recorded 27 minutes of overtime according to the example regarding the setting above, then 24 minutes is recorded as overtime if the rounding is set to 6 minutes. If a time bank is selected for the overtime which has been rounded off, then the 3 minutes not recorded as overtime will be added to the time bank.

#### Time bank to which to add the rounding
Here you select the time bank to which the rounded off time will be added. Time banks are handled in the procedure Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Attendance.

#### Calculate overtime
With this setting you decide how to calculate the overtime. The default option After fulfilled daily working hours means that overtime will only be registered after the scheduled number of hours for the day have been recorded by the employee. If the daily working hours is not fulfilled, and time is registered in the overtime period (time outside the schedule), it will not be recorded as overtime. If you select the option All overtime it means all time registered in the overtime period will be regarded as overtime even though the daily working hours have not been fulfilled.
Example: If the employee clocks in 1 hour late and then works 1.5 hour overtime, then overtime compensation will only be generated for 0.5 hours if the option "After fulfilled daily working hours" was selected.

#### Salary type according to total overtime
If you check this setting it means the overtime salary type is not affected by which the time the overtime was recorded. This is used in some collective agreements (labor contracts), for example in Finland.

#### Overtime types
Here you select which overtime types to which the employees in the group should have access. At least one type must be selected. The overtime types are handled in the procedure Basic data – Attendance.

#### Automatic overtime question
With this setting you decide if an automatic overtime question should be shown when the employee records outside the regular overtime, and forgets to select the button Out – Overtime. This setting activates the time settings below.

#### Time before schedule start and Time after schedule end
Here you enter time limits in minutes for how long time before the schedule start and for how long after the schedule end then automatic overtime question should appear.
