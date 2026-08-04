### Material
In this box there is a table where you can create a material list (a BOM list) for the part selected in the structure map.
It is possible to add, insert, and delete, material rows by using the buttons Add ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5), Insert new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) (Shift + F5), and Delete ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6) on the function menu.
By using the Move up ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_up.png) and Move down ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_down.png) buttons, you can move the material rows in the list. You can also move the rows by dragging and dropping the row number.
Using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can go to different procedures for the selected material.
Using the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) you can expand all instructions.
Using the button Copy records to Clipboard ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy.png) you copy all material rows to a part clipboard that can be used in another material list (or for example as a clipboard in a procedure).
You can add parts from a part clipboard with the Create from Part Clipboard button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png).

#### Expand row
By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_drill_down.png) to the far left on the row, you expand the row and can then see the instruction and the configured instruction which have been entered for the material.

#### Warehouse (WH)
Applies if you have installed the Warehouse option). If you change to another warehouse you will see the WH column. On the rows which belong to another warehouse than the selected warehouse you will see a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses_alt.png) in the column. A tooltip for the symbol informs you of which warehouse the row belongs to. Values and texts in all columns for these rows are displayed in italics.
In many of the procedures you can change the warehouse which you will be working in by using the Companies/Warehouses button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure. It is also possible to generally change in which warehouse to work. This is applied to all procedures.This is done in the desktop backstage.. In registration procedures for quotes, inquiries, different orders, and invoice bases, you can in a field select to which warehouse the record belongs.

#### Row
Here you can see the row number of the material. For each row added, one will be added to the number in this column. The row number cannot be edited.

#### Position
What is entered in this column refers to a particular position in the material list for a drawing. The field is alphanumerical and can contain a maximum of 10 characters. If the same position is used on several rows, you will see a warning.

#### B (Block information)
If the part is blocked for BOM and routing, this column is shown.

#### Part number
Here you can see/enter the part number of the included material. You can choose from the parts in the part register. If you enter a part number which does not exist, a new part will be created. You can then enter a name for the part, select a part type and a part template, as well as enter a standard price. This is saved to the part register when you save the BOM (bill of material/material list) in the procedure. When you have saved, it will no longer be possible to edit these fields. If you leave the field empty when you add a new part, the next part number from the number series will be used.
If the same part number is selected for more than one material row, a warning is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) by default in this field. This warning can be disabled via the system setting called Warn if material is not unique.
For underlying part nodes in the structure map, there is a validation making sure you cannot add the same part number as the part of one of the higher level part nodes. That is, a manufactured part cannot be included in itself.

#### Name
Here you can see the name of the selected material. If you are creating a new part number, you can enter the name here.

#### Translations
Clicking this button you can enter a translation of the material's name. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Part status
In this column you see the status of the part.

#### Replacement part
Here you can see the replacement part if the part (material) on the row has status Phasing out. The replacement part is only shown if the part has a replacement part entered in the Part register.

#### Part type
Here you can see the part type of the selected material. If you are creating a new material, you can enter the part type here.

#### Lot sizing rule (LSR)
The lot sizing rule of the material determine the suggested quantity in order suggestions when a shortage occur. The lot sizing rule you select will also become updated in the field Lot sizing ruleThe lot sizing rule determines the suggested order quantity when a shortage occurs of a part. Lot sizing rules are used for parts for which requirement planing is performed. in the part register. This way the part will have the same lot sizing rule in other material lists. If you switch between lot sizing rules with different control methods, for example from Lot-for-lot (order oriented) to Fixed order quantity (stock driven) or the opposite, then the field Control method in the part register will also become updated.
- Lot-for-lot – This lot sizing rule generates a linked order suggestion where the quantity matches the quantity of the requirement/shortage. Structure explosion will take place. The part's balance and other purchases might be a supply.
- Fixed order quantity – This lot sizing rule generates a suggestion (not linked) which is the same as the order quantity.
- Period requirement – This lot sizing rule reviews all shortages within the period length and creates a joint suggestion (not linked) for these. Firstly, a check will be made to see if there are any rescheduling suggestions (that are simulated as performed) within the days of grace.
- No requirement calculation – This lot sizing rule means that no order suggestions will be provided and no structure explosion will take place. This setting can be used for parts for which the planning method "physical" has been activated.
- Linked requirement – This lot sizing rule generates a linked order suggestion where the quantity matches the quantity of the requirement/shortage. Structure explosion will take place. Here only linked orders or reporting can be a supply.

#### Template
Here you see the part template.

#### For operation
Here you can enter the operation number for which the material will be used. The first operation is selected by default. If you enter an operation number that does not exist, you will see a warning.
If the material is included in a fictitious part, you can enter a 0 (zero) as the operation number. By entering a zero, the material will inherit the operation number from the fictitious part that was superior (on a higher level) when placing the order. It will also be moved up a level in the structure, and the fictitious part will be deleted. It may be necessary to enter a zero as operation number for included material of a fictitious part. This ca be the case if the fictitious part appears in several places in other BOM lists (it may get different operation numbers).

#### Quantity
Here you see the quantity of the part or material that will be used in the next operation. The quantity on a new material row is by default 1.00 of the material's default unit. By using the Weight calculation button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) on the material row, you can perform a weight calculation of the quantity entered in this field.
If you add a tool, the quantity will be set to 0.00. The Setup quantity will instead be used and will by default be set to 1.00. You can add tools as material for the operation, if the Tools & Maintenance option is installed.

#### Quantity formula f(x)
Applies if you have installed the Product configurator option. In the f(x) column you find the button Quantity formula ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_formula.png). This button opens a window where you can add a formula for quantity and setup quantity for the material row. When a formula already exists, the symbol on the button will be different ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_formula_info.png). You can select one of three different functions for a quantity formula which will be taken into consideration when an order is registered for the part. It is possible to multiply, add, or replace the regular value with the result of the formula. Read more in the section [Formulas](../../../UserGuide/Using/Configurator/Formulas.htm) in Using Monitor about the product configurator.

#### Formula
This button opens a small table where you can add parts as terms for the material row.

#### Weight calculation (WC)
By clicking the Weight calculation button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) you access a calculator where you can create a weight calculation for the Quantity field. A weight calculation can also be created for the part in the Part register procedure (under the Miscellaneous heading under the Manufacturing tab). That weight calculation works as a template and is shown here by clicking the button on a new material row.
You select Type of profile in the calculator. You can select among: Area, Flat bar, Hexagon bar, L-profile, Round bar and Weight per unit.
Calculation formula for type of profile
- Area – Calculated as: Area x Length x Density.
- Flat bar – Calculated as: ((Length x Width x Height) - (Length x Inner width x Inner height)) x Density.
- Hexagon bar – Calculated as: (Length x 1.5 x Diameter2 / √3) x Density. Where the Diameter is measured between two sides according to this [illustration](../../../../Resources/Images/SubProjects/Hexagon.png).
- L-profile – Calculated as: Length x (Width + Height - Thickness) x Thickness x Density x Factor.
- Round bar – Calculated as: (((π x Diameter2 / 4) x Length) - ((π x Inner diameter2 / 4) x Length)) x Density.
-    
Weight per unit – Calculated as: Weight per unit x Length x Width. Weight per unit is used when you know the weight in kg for a piece of a material with the length and/or width 1000 mm, for example, length or width of a complicated aluminum profile.
Example: A certain aluminum profile weighs 2 kg per meter. You then enter 2.00 kg as Weight/unit. If the length of the material is 2 meter, you enter 2000 mm as Length and 0.00 mm as Width. The weight will then be 4.00 kg. If you enter 0.00 mm as Length or Width, that factor will be left out. If you enter both a Length and a Width > 0, the Weight/unit will be = kg/m².
You can select a Material registered in the Material and densities. You will then get a default Density shown in kg/dm3 according to the settings configured for the material in the procedure mentioned. But you can also enter a density of your own without first selecting a material.
You add a calculation row in the calculator and enter Position, Drawing number, Quantity, and the different measures from the drawing. The different measures for Length, Width, Height, and Thickness, should be entered in mm. The Area is entered in mm2. The measures which can be entered are based on the selected type of profile. If you have selected an L-profile, you can also enter a Factor in percent, with which the weight will be multiplied. The factor is used to adjust for material in radius for L-profiles. The default factor is 2.00 percent. The calculated Weight in kg, is shown on the row.
You can add more calculation rows for a material row in the calculator. Adding more calculation rows can be used when the part on the material row is composed of multiple materials.
Above the calculation rows you see Total weight in kg. This is added together for all calculation rows. With the button called Apply calculation you insert the calculated total weight in the Quantity field on the material row and the calculator is then closed.
> Take the Unit of the material into consideration when you insert a calculated weight in the Quantity field. The calculated weight is saved for the material row in the BOM and routing and is used as calculate quantity of the material in the manufacturing. The calculated weight is not saved to the part's net weight in the part register.

#### Unit
This field shows the default unit of the material. If there is an alternative unit and you change to it, you will see the Quantity and Standard price in that unit. Make sure to select the unit “kg” before activating the weight calculation.

#### Standard price
Here you can see the standard price of the material in the company currency and per selected unit. If you are creating a new material, you can here enter the standard price.

#### Revision
Here you can see the active revision of the material.

#### Only calculation
If you check this box, the material will only be included in the calculation but not on the order.

#### Instruction (I)
Here you can see/enter a material instruction. This instruction text will be printed on the manufacturing order documents.

#### Files (F)
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
Here you can choose if you wish to print linked files automatically together with the manufacturing order documents. You can also choose if a unique file (copy) should be created of the linked file on the manufacturing order and if the unique file should be allowed to be opened in an external program in Windows. Read more about Link files in the section [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm) in the online help function.

#### Configured instruction (CI)
(This applies if you have the option Product configurator) Here you can enter a configured material instruction. If there is also a regular material instruction (I), this will be combined with the configured material instruction on the manufacturing order documents.
By clicking the button CI you open a window where you can create a configured instruction per configuration group you add. You can enter variables by using the mouse pointer to drag and drop to the places in the instruction text where you want them. You can also manually enter a variable in the instruction text as [v:variable code]. You can create formulas from the available variables and add the formulas in the instruction text using drag and drop. It is also possible to manually enter a formula in the instruction text as [f:formula name]. Validations are made to make sure the entered variables and formulas are available.
You can test the outcome by using the button Preview instruction ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_preview.png) next to the instruction text.
Read more about configured instructions in the topic called [Basic data](../../../UserGuide/Using/Configurator/BasicData.htm) in the chapter about using the Product configurator.

#### Traceability
Here you see if it is a material with traceability and on what level.

#### Alternative material
By clicking this button you can add alternative materials. Such material will be shown if a shortage occur for your standard part and you can change to this at material clearance. The alternative material will also be suggested when changing part on a manufacturing order. 
If an alternative material is selected in the BOM and routing, this will override an alternative material selected in the Part register.
More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Setup quantity
In this column you can enter a fixed quantity in addition to the calculated quantity and extra quantity as a percentage, if any. You can use Setup quantity as an alternative to, or in combination with, Extra % on the material row.
For tools, 1.00 is automatically suggested as setup quantity instead of the regular quantity. If you create a new tool on the material row, the setup quantity is set to 0.00. And the regular quantity will be used instead.
> Keep in mind: for existing reusable tools added in the material list, the setup quantity should always be 1.00.

#### Extra %
Here you can enter a percentage for overflow of quantity. This can be used if it is more convenient to add a percentage rather than a fixed overflow.

#### Terms
By using different terms on material rows (and operation rows), you can apply alternate BOM and routing. The terms available are: Finish date, Quantity, Customer number, Order, Revision, Variant code, Part status, and Warehouse. You choose to apply a row with a term in one of the following ways in the BOM and routing:
- add this extra row (+)
- replace previous row (±)
- delete this row (-)
The Finish date term
If you use the Finish date term and choose to use start date when registering manufacturing order and you leave the finish date empty, the start date will be used for the term instead.

#### From
Here you can enter a "from value" of the selected term.

#### To
Here you enter the "to value" for the selected term. By entering a value in From and To you decide within which interval the material row with the terms will be met.

#### Quantity per cycle
This is where you enter the number of pieces that will be manufactured when the tool has been used one cycle. For example, a certain casting mold is capable of manufacturing 10 pieces when it is used in one cycle. Then you should enter 10 in this field. This only applies to reusable tools that are handled as entities, that is, they have serial numbers entered.

#### Cycle time
Here you enter the time it will take to use the tool during one cycle. This only applies to reusable tools that are handled as entities, that is, they have serial numbers entered.

#### Net weight
Here you see the weight in part's standard unit. The weight is loaded from the Net weight under the General tab in the Part register procedure. The net weight is not calculated if you change unit.
