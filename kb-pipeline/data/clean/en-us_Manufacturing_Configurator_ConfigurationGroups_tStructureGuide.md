### Structure/Guide
Under this tab you create the structure of the configuration group. This will also become a guide which is used during configuration when an order is created.
You create the structure by adding sections (pages) in a sequence, where you the add option lists and variables in each section. You can also add sections in several levels.
When registering an order, each section is shown as a page. On order documents sections function as a grouping with a heading and a footer.
You can create new option lists and variables directly in the structure under the tab by adding rows, selecting Option list or Variable as Type and then entering a new code and description for the new rows. This might be good to do when you are creating a product structure.
A new option list will by default be of the type Mandatory. It will be shown under the Option lists tab, but to edit the option list you must use the Option lists procedure. There you also make settings for the option list as well as to add contents (parts) to it.
When you create a new variable you must choose which type of variable it should be; Text, Number, Boolean, or Date. The new variable is shown under the Variables tab, and there you can configure different settings for it that will only apply for the specific configuration group. The variable is also shown in the Variables procedure and there you can configure general settings for the variable which should apply in all configuration groups.
If you instead add option lists and variables under the tabs Option lists and Variables, they will be shown here in the box Not used components. From there you move them in to the section in the structure which you have marked, by using the button Place in active section ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_to_section.png). An alternative is to use the drag and drop function to place them in the right place.
In the Options box you see the parts which the option list (marked in the structure) contains. This is the same information as in the Contents of option list section under the Option lists tab.
It is also possible to move objects from the structure back to the box Not used components. This is done with the button Move to "Not used" ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_from_section.png) or by drag and drop.
You can drag and drop sections, option lists, and variables, to move them around in the structure. An alternative is to use the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_up.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_down.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_in.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_out.png) on the function menu to move up, down, in, or out in the structure. Using these buttons you can move option lists and variables within the same section. If you want to move option lists and variables between two different sections, you must use the "drag and drop" function. You can also move one or several option lists or variables in under other option lists, in multiple levels. By adding option lists and variables under other option lists you can use rules to exclude or include that entire branch in the structure.

#### Type
Section, option list, and variables, are shown in this column with the following symbols:
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridFolderImage.png) – Section
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridMandatoryYesImage.png) – Option list (Mandatory)
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridMandatoryNoImage.png) – Option list (Not mandatory)
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridVariableImage.png) – Variable

#### Description
Here you see the name of the section, option list, and variable. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Visible
Here you determine if the section should be visible or not during the configuration. It can be used to hide options which are automatically taken care of via rules.

#### More info
Under the Mer info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can for a section configure the settings Show on document and Show footer. This means, on which documents should the section be shown: customer order, manufacturing order, and purchase order. By default the section is shown on all documents. The footer for a section shows a total of amounts from the rows in the section. On new sections, the setting is default set that the footer should not be displayed.
