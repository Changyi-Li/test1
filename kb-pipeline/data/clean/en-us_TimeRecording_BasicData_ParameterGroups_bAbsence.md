### Absence

#### Absence check
With this checkbox you determine if absence check is activated for the parameter group in question. This means that when you clock out within the regular working hours, a warning window will appear saying that clock out will take place before end of schedule and persons linked to the parameter groups must then select an absence code. This will also take place when you clock in too late.
If absence check is not activated for the parameter group, the differences between planned and recorded time will always be set to zero. Also, no log records will be created for differences in the list Discrepancy between planned/recorded time in the procedure Recording log.

#### Non-regulated working hours
With this checkbox you decide that individuals linked to the parameter group have non-regulated working hours, that is, they are not required to record attendance every day, but record their attendance and work afterwards. This function is only used in combination with the Monitor TimeCard option.

#### Indirect code for TimeCard
If the setting called Non-regulated working hours is activated, you must here select an indirect code for attendance and work that is non-regulated working hours. The indirect code must first be registered in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Work procedure.

#### Plan absence via recording terminal
With this setting you decide if registration of planned absence should be possible in the recording terminal.

#### Allow absence recording in negative flex zone
With this setting you decide if absence recording should be possible in the negative flex zone. When clocking in and also when clocking out it will then be possible to select an absence code. When clocking out within the negative flex zone it is also possible to select if the absence should apply as of now (this will not result in any negative flex time for today) or if the absence should apply as of tomorrow. If persons/individual linked to the parameter will have a balance less than the minimum limit for negative flex, when recording absence in the negative flex zone, then the time under the limit will be registered as unpaid absence.

#### Invalid absence codes
Here you can select the absence codes which should not be available to choose when recording. For example, you might not show the absence code "Flex withdrawal" for shift workers.

#### Alternative salary type at absence
Here you can add the absence codes which should have other salary types than the default salary types for the absence codes selected in the procedure Basic data – Attendance.
