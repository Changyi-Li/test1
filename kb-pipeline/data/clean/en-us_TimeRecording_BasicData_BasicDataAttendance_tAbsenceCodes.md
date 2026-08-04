### Absence codes
Absence codes are used to allow recorded absence times to be categorized and linked to the right salary types and/or time balances.

#### Row number
This is a consecutive number for the row. You can re-sort the list of absence codes in this column by using the drag and drop function with the cursor.

#### Code
Here you enter the absence code using a maximum of 4 characters. This code will be used in places where there is not enough room for the actual name.

#### Name
In this column you see/enter the name of the absence code. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Time bank
Here you see/enter the time bank which is applied for the absence code.

#### Salary types
Here you see/enter the salary type(s) which apply for the absence code.

#### Absence 1 and Absence 2
With this checkbox you determine if salary types for Absence 1 and Absence 2 should be added from the schedule on the absence code, in addition to the earlier selected salary type(s). This might be necessary in cases where different time types apply for a day in the schedule (for example IWH during absence and IWH sickness).
You select salary types for Absence 1 and Absence 2 in the Salary typeSalary types are used to create salary bases for worked time and absence. Different salary types are used, for example, for work during regular working hours, flex, overtime, shorter working hours, and sick leave. The salary bases are used to manage salaries in a payroll system. Salary types are linked to absence codes in addition to work schedules and overtime schedules. box for schedules in the Schedules procedure. You name Absence 1 and Absence 2 using the system settings Name – Absence 1 and Name – Absence 2.

#### Included in daily working hours
With this checkbox you determine if the absence code should be included in the daily working hours when calculating overtime.

#### Included in shorter working hours (SWH)
With this checkbox you determine if the absence code entitles to shorter working hours.

#### Not continued
With this checkbox you determine if the absence code should continue to apply the following day. If this setting is checked, the absence code only applies to the current day, rather than until the next time you clock in. This is recommended for absence types such as for example flex. This is to ensure that if, for example, someone records two hours negative flex on a Friday and then becomes ill and is home sick for a week, the entire week long absence will not be recorded as flex withdrawal. Rather, the person will be able to select the proper absence code upon returning to work.

#### Deduct from OT/Flex
In the column called "Deduct from OT/Flex" you find a checkbox. This is used to determine if times with this absence code should be deducted from overtime/flex in cases where daily working hours have not been fulfilled.

#### Statistics
For absence statistics you can here select if the absence code is Unpaid, Paid, or Attendance. Unpaid absence is a late arrival, for example. Paid absence can for example be a leave of absence and certain types of sick leave. Furthermore, absence is considered paid where the time is deducted from a time balance, e.g. flex, comp, or makeup time. Absence of the type Attendance can for example be used for business travels. Please note! Time outside the schedule can also be accounted for as attendance. This can be useful when for example a business travel takes place outside scheduled working hours.

#### Maximum time
Here you see/enter the maximum time (in hours) the users are allowed to record using the absence code. If you enter a maximum time, you must also select a subsequent absence code. The system will automatically select this absence code for the exceeding time the user records.

#### Subsequent absence code
Here you see/enter an absence code to be used for the exceeding time if the maximum time has been reached. It is also used for different types of automatic recording, for example change of period.

#### Consecutive
With this checkbox you decide if the absence should be analyzed to see if it is a consecutive absence lasting over for example a weekend. It can for example be a sick leave which stretches over a turn of the month (i.e. different salary periods) and the turn of the month occurs in a weekend with non-working days. Then the non-working days needs to be included as days of absence.
The purpose is to be able to handle consecutive absence which runs over weekends, during export of certain file formats to payroll programs. Otherwise absence over the weekend might not be correctly handled.
If this checkbox is activated and the absence starts the day before the weekend and continues the day after the weekend, this means that absence will also be recorded for the days of the weekend but with zero (0) hours of absence.
