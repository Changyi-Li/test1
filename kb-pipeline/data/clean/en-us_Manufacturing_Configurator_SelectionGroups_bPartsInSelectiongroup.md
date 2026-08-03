### Parts in option list
In this table you add the parts which should exist in the option list.
Buttons on the function menu
You can manually add/delete rows with parts by using the buttons Add ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5) and Delete ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6).
An alternative is to add parts from a part selection by using the button Create from Part Clipboard ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png).
By using the button Add underlying level ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_subrow.png) (Ctrl + Shift + F5) you can also add one or several sub-rows to a part row (main row). The parts you add on sub-rows become linked to the main row and will always be included to complement the structure on a manufacturing order when the part is selected in a configuration. The main purpose with this is to via an option be able to include multiple parts under different main parts. Read about main part below.
You can change the order of the part rows with the buttons Move up ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_up.png) and Move down ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_down.png).
By using the button Sort ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_sort_right.png) you can sort all parts in the option list based on he different alternatives you see when clicking the button.
Using the button Copy records to Clipboard ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy.png) you copy all part rows (including sub-rows) in the option list to a part clipboard that can be used in another option list (or for example as a clipboard in a list procedure).
The first row of an option list contains default values which apply for all rows you add. The default values will apply in the columns which do not contain data from the selected part You cannot delete the first row. However, you can override a default value in a column by entering a value in that column on a part row. If you leave the column on the part row empty, the value on the first row will be loaded when the part is selected in a configuration.
> Many of the columns on a part row, as for example For op. and Default qty, are the same as on material rows in a BOM and routing. Read about these columns in the help topic [Material](../../Parts/BOMAndRouting/bMaterials.htm) in the procedure BOM and routing.

#### Position
Here you can enter a specific position number for each part row which corresponds to position number in the material list in a BOM and routing.

#### Part number
For each row, you here select the parts which should always be included as fixed options in the option list.

#### Clipboard
When you click this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/modified_image.png) a window opens where you can configure a selection of parts which should be possible to choose among in the option list during configuration, in addition to the parts which you add as fixed options on separate rows in the option list. When a selection has been configured you will instead see a filter symbol on the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_filter.png).
Selection is especially useful if there are many options in an option list or if users often add new options during configuration. By using a clever selection, new parts which fall outside the selection will automatically become possible to select without you having to update the option list.
> It is good to use a filter by part status Normal in order to easily make sure that only active parts are possible to select during configuration.
At the top of the tab Configure selection in the window you select which columns with part data that should be shown when a user is about to select a part form the selection during configuration. The Part number column is always included among the selected column and it cannot be deleted. You can also enter a width for each column. This is entered in number of pixels. In the table at the bottom of the window you can add one or multiple rows for the actual part selection, based on the different selections you can make there. If you do not make any selections, the user will be able to choose from all parts in the part register.
At the bottom of the tab you configure the term for the selection. This works in the same way as when making a selection for a list.
Under the Selection tab you see the result of the selection you have made.
You save the selection with the OK button. Using the Delete button you can delete the selection from the option group.
When configuring, a separate row is shown at the bottom of the option list in the configuration window where the user ca select a part based on the selection you have configured. The user can (if the setting of Maximum no. of options in the option list allows it) also insert new rows during configuration, with more parts from the same selection.

#### Formula for quantity and setup quantity f(x)
In the f(x) column there is a button with this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_formula.png). When a formula already exists, the symbol on the button will be different ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_formula_info.png). By clicking this button you access a formula editor where you can enter a formula for quantity and a formula for setup quantity for the part in the option list. Since an option list can be included in several configuration groups you must first enter for which configuration group the formula applies. Each new formula gets a formula number. You can link the same formula number to several configuration groups.
If you add formulas on the first row in the table, it will apply to all parts in the option list, unless you do not add separate formulas on the rows. Quantity formulas on parts will be taken into consideration during configuration and they will always replace the regular quantity value with the result of the formula. The quantity will then not be possible to edit during configuration.
A formula can consist of variables, operators, terms, and functions. The variables you can select among are the ones that are included in the configuration group you add in the formula editor.
Read more about Formulas in the online help function.

#### Minimum quantity/Maximum quantity
Here you can enter a minimum quantity and/or a maximum quantity of the part. This is done using the default unit which applies to the part selected on the row. If you do not enter any limits here, the default quantity in the field Default qty will apply and the user will not be able to change this when configuring for example a customer order.

#### Multiply by main quantity
This setting only applies for a sub-row (underlying level) to a part row. If you activate this setting, the quantity on the sub-row will be multiplied with the quantity on the part row (main row) when it is added in the structure. If this quantity is not activated, the quantity on the sub-row will be added, regardless of the quantity entered on the main row.

#### Instruction (I)
Here you can see/enter a material instruction. This instruction text will be printed on the manufacturing order documents.

#### Exception from showing on documents (E)
By clicking this button you open a box in which you can override which information for the selected parts in the option list during configuration, should be shown on sales documents, manufacturing documents, and purchase documents. With the system settings Show on sales documents, Show on purchase documents, and Show on manufacturing documents, you decide what should be shown by default.
If you want all rows to have the same settings, then you should use the button on the top row in the table. Activate Exception <dokument> and then choose which columns that should be shown. By default, no columns are chosen. This is to make it easy to configure which information should not be shown on the documents.

#### Configured instruction (CI)
(This applies if you have the option Product configurator) Here you can enter a configured material instruction. If there is also a regular material instruction (I), this will be combined with the configured material instruction on the manufacturing order documents.
By clicking the button CI you open a window where you can create a configured instruction per configuration group you add. You can enter variables by using the mouse pointer to drag and drop to the places in the instruction text where you want them. You can also manually enter a variable in the instruction text as [v:variable code]. You can create formulas from the available variables and add the formulas in the instruction text using drag and drop. It is also possible to manually enter a formula in the instruction text as [f:formula name]. Validations are made to make sure the entered variables and formulas are available.
You can test the outcome by using the button Preview instruction![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_preview.png) next to the instruction text.
Read more about configured instructions in the topic called [Basic data](../../../UserGuide/Using/Configurator/BasicData.htm) in the chapter about using the Product configurator.

#### Comment to configuration
Here you can enter a comment for part in the option list. The comment is shown when you configure for example a customer order and it can contain an image or a description of the part.
More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Standard price
Here you can see the standard price of the material in the company currency and per selected unit. If you are creating a new material, you can here enter the standard price.

#### Variant code
Here you see the part's variant code. An option list is often used to control a section of the entire variant code. Variant codes from multiple option lists are added together to create complete variant codes during configuration. Read more about variant codes in the online help function for the procedure BOM and routing.

#### Only calculation
If you check this box, the material will only be included in the calculation but not on the order.

#### Setup quantity
In this column you can enter a fixed quantity in addition to the calculated quantity and extra quantity as a percentage, if any. You can use Setup quantity as an alternative to, or in combination with, Extra % on the material row.
For tools, 1.00 is automatically suggested as setup quantity instead of the regular quantity. If you create a new tool on the material row, the setup quantity is set to 0.00. And the regular quantity will be used instead.
> Keep in mind: for existing reusable tools added in the material list, the setup quantity should always be 1.00.

#### Extra %
Here you can enter a percentage for overflow of quantity. This can be used if it is more convenient to add a percentage rather than a fixed overflow.

#### Files (F)
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
Here you can choose if you wish to print linked files automatically together with the manufacturing order documents. You can also choose if a unique file (copy) should be created of the linked file on the manufacturing order and if the unique file should be allowed to be opened in an external program in Windows. Read more about Link files in the section [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm) in the online help function.

#### Main part
Here you see/enter the row part's main part. If the main part field has been left empty, the row part will be added on the top level in the manufacturing order structure. That is, directly under the part which the user is configuring. By selecting a main part you can direct parts in option lists to manufactured parts on other levels than the top level. If the part on the row should be added to a manufactured part which can differ (depending on other options) then you can use a fictitious part as main part. Then you enter this fictitious part in the manufactured parts which you want the row part to be added under.

#### Alternative name
Here you see the part's alternative name used in configurations. You enter an alternative name for parts in the Configuration box in the Part register procedure.
