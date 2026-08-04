### Templates
Here you add main rows and sub-rows with fields in the measuring form. You can combine several main rows and sub-rows that together create sections in the form. The main row becomes a heading for the section and each sub-row is a measuring point or checkpoint.
Use the button Add main row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5) to add a main row. Use the button Add sub-row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_subrow.png) (Ctrl + Shift + F5) to add a sub-row for a field. By using the button Delete selected row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6) you delete the row are on.

#### Code
Here you see/select if it is a main row or a sub-row.

#### Name
Here you see/enter the name of the main row's heading or the sub-row's field.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Type
Here you see/select the type of field that should exist on the sub-row. The available options are Decimal, Text, and Checkbox. If you select Decimal, the following columns are activated.

#### Unit
Here you see/select unit for decimal values. You can select among the units registered in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure.

#### Minimum tolerance
Here you see/enter the minimum allowance for decimal values. This is the minimum tolerance for a control measurement. This must be entered as a negative value. E.g. if the setpoint is 100 mm and 99 mm is the lowest allowed value, -1 should be entered as the minimum tolerance. A validations is made to make sure the minimum tolerance is less than the maximum tolerance.

#### Setpoint
Here you see/enter the setpoint for decimal values. The value which the control measurement should show.

#### Maximum tolerance
Here you see/enter the maximum allowance for decimal values. This is the maximum tolerance allowed for a control measurement. This must be entered as a positive value. E.g. if the setpoint is 100 mm and 101 mm is the highest allowed value, +1 should be entered as the maximum tolerance.

#### Instructions
Here you see/enter an instruction for the row in the measuring form. This can be, for example, an instruction describing how to perform the control measuring.
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Mandatory
With this checkbox you decide if the measuring point is mandatory. If you check this box it means control measuring must first be performed and reported before you can report the operation to which the measuring form is linked. (This is done via a measuring template in the BOM and routing or on the manufacturing order.)

#### Print
With this checkbox you decide if the measuring point should be printed on manufacturing order documents. It will in that case be printed if it is configured on the manufacturing order document in question that the measuring plan should be displayed. That setting is configured in the Document templates – Manufacturing order procedure.

#### Minimum setpoint
Here you enter the minimum setpoint allowed for decimal values before a warning is shown saying that the control measurement is approaching the minimum tolerance.

#### Maximum setpoint
Here you enter the maximum setpoint allowed for decimal values before a warning is shown saying that the control measurement is approaching the maximum tolerance.

#### Default values
Here you see/enter a default value on the row. For rows of the type Decimal, you can enter a numerical value using a maximum of six decimals. For rows of the type Text, you can enter a text. For rows of the type CheckBox, you find a checkbox here. For rows of the type Date, you can select a date.

#### Master tool
If the Tools & Maintenance option is installed, you find this field on rows of the Decimal type. Here you can then select which tool should be used for the control measurement. You can select reusable tools that have a serial number.
