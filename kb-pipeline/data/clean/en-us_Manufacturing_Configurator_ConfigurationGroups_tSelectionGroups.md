### Option lists
Under this tab you get an overview of the option lists that are included in the configuration group.
By using the buttons on the function menu you can also add and delete option lists. There is also a button called Copy and replace ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png). This can be used to copy the selected option list to a new option list and at the same time the option list marked in the configuration group will be replaced. By default, all formulas in the option list will also be copied to the new option list.

#### Option list
Here you can select among already registered option lists, which ones you want to use in this configuration group. In the table you then see information about the loaded option list.
You can create an option list by entering a new option list code (previously not used) on a new row. The option list must then be placed in the structure under the tab Structure/Guide and you must also enter a description.

#### Minimum number of options/Maximum number of options
Here you determine the minimum and the maximum number of options which should be possible to make in the option list. By default this is set to 1 for a new option list.
If the Minimum number of options field is left empty or if you enter 0, it becomes an option list that is not mandatory. This means that the user does not have to select any part from the option list during configuration. If the field has the value 1 or greater, then it becomes a mandatory option list This means that the quantity entered in the field is the minimum quantity of parts which the user must select from the option list during configuration.
If the Maximum number of options field is left empty then the user can select any number of parts from the option list during configuration. This is useful if the option list contains different accessories which should be possible to add (unlimited) during configuration. Otherwise, the entered value is the maximum number of parts which the user is allowed to select. It is not possible to enter 0 as maximum number of options.

#### Automatic option
With this setting you determine if there should be an automatic option of parts or not, when the option list is included in a new configuration.
The following options are available:
- Yes, first – The first available part at the top of the list in the option list will automatically be selected during configuration. By "available" it means parts that have not been excluded by any rule in a configuration group. Please consider the sorting in the option list when this method is used. This alternative can only be selected when Min. options and Max. options have been set to 1. This setting is most commonly used in option lists which should be handled automatically via rules. If the user during configuration manually or via a rule select another part, that is another part than the first available in the option list, then that option will by default become locked in the configuration. If you unlock the option, the first part possible to select in the list will be selected.
- Yes, all – All available parts in the option list are automatically selected during configuration. This alternative can only be selected when Min. options and Max. options have been left empty. This setting is used if you by using rules exclude all invalid options and want all valid options to become automatically selected.
- No options – Default. No parts will become automatically selected during configuration. This setting is most often used in all option lists where the user manually should decide on options during the configuration.
> If a part in the option list becomes selected via a rule in a configuration group, then automatic options will not apply. Nor will automatic options apply if there is a manually selected part or a part which is not selected but is locked in a configuration.

#### Minimum quantity/Maximum quantity
These fields become activated if Max. options has been left empty. These fields determine the minimum and maximum quantity of the number of selected parts from the option list in a configuration. If these fields are left empty, there will be no limitation of the quantities.

#### Contents of option list
In this section of the procedure you see information about the parts which the marked option list contains.
