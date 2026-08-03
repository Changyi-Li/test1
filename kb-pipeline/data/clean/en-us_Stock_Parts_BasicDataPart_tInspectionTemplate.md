### Inspection templates
Under this tab you register different inspection templates which can be used for receiving inspection on part. The inspection templates are used to trigger receiving inspection when different nonconformities occur, for example, if a part gets a new revision, if a case is registered for the part, or if previous receiving inspections have resulted in rejected material.
Changes made for inspection templates in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part and Basic data – SRM procedures will not affect parts/suppliers which have already been assigned the inspection template in question.
That is, if you have assigned an inspection template to a part and you then make changes to, for example, the frequency for that template in the Basic data – Part procedure, these changes will not affect that part.

#### Template code
Here you enter a code for the inspection template. This code is unique and cannot occur on more than one row in the table.

#### Name
Here you can write a descriptive text as a name. The name text is entered in the company language and is displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Included nonconformities
Here you select which types of nonconformities that should trigger receiving inspection. The following options are available:
- New revision – Inspection is triggered if the part has status 5 (New revision).
- Registered case on part – Inspection is triggered if there is a case registered for the part and this case has status 1 – Registered, 2 – Printed, or 3 – Started.
- Rejected quantity on inspection – Inspection is triggered if arrival reporting resulted in a rejected quantity.

#### Active
With this checkbox you determine if the inspection template in question should be active. By checking the box you make the inspection template available to select in fields for Inspection settings in different parts of the system.

#### Level
Here you see the number of the inspection level. This field is numerical and cannot be edited. A new row will by default be assigned the next available number. The table/list is sorted by this column.

#### Number of arrivals
Here you enter the number of arrivals which require receiving inspection. If several levels has been entered in the table, the number shown here is the number of deliveries which should be performed before the inspection template activates the next level.

#### Inspection frequency
Here you enter the frequency of the receiving inspection, that is, how often it should take place. For example, if you have entered 2.00 it means every second arrival will be inspected.

#### Revert back to previous level
With this setting you decide if the inspection template should go back to the previous level if any of the entered nonconformity types has been discovered. This setting is only available if the table contains more than 1 level.

#### No. of inspections after nonconformity
This setting is only possible to edit when Included nonconformities is activated. Here you enter the number of inspections which should be made if a nonconformity has occurred.
