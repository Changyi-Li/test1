### Maintenance templates
Here you create the maintenance templates you need for your tools and machines. To a maintenance template you then link a maintenance type and a form template. On the maintenance template you enter what you want to be the trigger of a specific maintenance item. For the selected trigger you then enter a start value and a frequency. You can also enter a minimum tolerance and a maximum tolerance for the start value, but this is optional. You can also select a part to load BOM and routing from, to add to new maintenance orders based on the maintenance template.

#### Code
Here you enter a code or number for the maintenance template. You can use a maximum of 20 characters.

#### Name
Here you see/enter the name of the maintenance template.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Maintenance type
Here you select the maintenance type to link to this maintenance template. The maintenance type determines where the maintenance template belongs in the maintenance structure you have created for statistics.

#### Form code
Here you select the code for the form template you want to link to this maintenance template. You create form templates in the Form templates procedure.

#### Triggered by
Here you select what should trigger maintenance with this maintenance template. In the Planned maintenance procedure you see which maintenance items need to be performed on tools, based on trigger type. You link the tools to the maintenance template via a maintenance plan registered in the Maintenance plans procedure. The available trigger types are:
- None – No trigger of maintenance is used in this maintenance template. This option deactivates the following columns in the table. If you choose this option, no analysis of planned maintenance is made in the Planned maintenance procedure.
- Calendar – A date in the calendar is the trigger. This option is used when planned maintenance should be analyzed based on calendar (an even interval).
- Number of cycles – The value for Number of cycles for the serial number is the trigger. This option is used when planned maintenance should be analyzed based on number of cycles.
- Operation time – The value for Operation time for the serial number is the trigger. This option is used when planned maintenance should be analyzed based on operation time.
- Distance – The value for Distance for the serial number is the trigger. This option is used when planned maintenance should be analyzed based on distance.

#### Start
Here you enter the start value based on the selected trigger. This means when the first maintenance should take place.

#### Frequency
Here you decide how often or with what interval the maintenance should be performed.

#### Minimum tolerance
The value in this column decides how much "too early" it is OK to perform the maintenance.

#### Maximum tolerance
The value in this column decides how much "too late" it is OK to perform the maintenance.

#### Use BOM and routing from
Here you can choose from which manufactured part to load operations and material to new maintenance orders which are based on this maintenance template. This part will then automatically be selected on new maintenance orders which are based on this maintenance template.

#### Variant code
Here you can enter a variant code for this maintenance template. The variant code will then automatically be entered on new maintenance orders which are based on this maintenance template.
