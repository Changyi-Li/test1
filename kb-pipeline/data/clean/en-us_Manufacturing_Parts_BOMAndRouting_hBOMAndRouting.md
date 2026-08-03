### Header row

#### Part number
The part number is the primary information in the Part register and in the BOM and routing procedures. In this field you will see the part number that was most recently loaded. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature, you can select another part number. If the selected part is blocked, the part number is displayed in red.
A new record is highlighted by a green dot ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) shown in the field. This dot will disappear when the record is saved for the first time.
You can enter a new part number (alphanumerical, with a maximum of 20 characters) and leave the field using Tab or Enter in order to create a new part. You can also click the Create new button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_new.png) or press (Ctrl + N) to create/register a new part. If you leave the field empty, the next available part number will be loaded from the number series for part numbers in the Number series procedure when you save in the procedure.
> Part number can be shown as a bar code on different documents in Monitor ERP. If you plan to use extended characters in your part numbers (for example, Å, Ä, and Ö), please remember that these characters are not supported by certain bar code types.

#### Name
Here you can see the name of the part. For new parts, you enter the name in the Name field you find in the General box. By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see translations made of the name text.

#### Configuration group
You can here select the configuration group which should apply for the part. The selected configuration group's name is shown to the right of the field. For a configured part, different terms apply as described below:
- The part should have a basic BOM and routing which you create in the BOM and routing procedure, if it is of the type Manufactured.
- The part should have traceability at Batch A batch is the set of components/products manufactured at the same time and made from the same original material. level or at Serial number A serial number is a number that is used for traceability for parts on entity level. level. A warning will be displayed if traceability is not activated for the part.
- The part should have lot sizing rule Linked requirement in all warehouses. A warning will be displayed if traceability is not activated for the part.

#### Open automatically
With this setting you decide if the configuration window should open automatically when you register an order for the part.

#### Default configuration/template
Here you can select a template to apply as default configuration when you register an order for the part. Templates can be created in the configuration window in connection with registering an order for the part. Templates can also be created directly in the Configuration templates procedure.
> If your Monitor ERP system is converted from Monitor G4, there is already a template selected for the part. This template is called Standard and have the same components selected in its configuration, what was previously called Default for selection alternative for selection group in the previous generation of Monitor.
Miscellaneous
Under the Miscellaneous ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button it is possible to enter more information for configuration as seen below. When saved information already exists, the symbol on the button will be different ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png). These settings are used for parts which are options in a configuration, that is, parts included in option lists, not on the configured main part.

#### Price formula
By clicking the Price formula ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_formula.png) button you can enter a price formula for the part by using variables from a configuration group you first select. The function of the price formula is to multiply the regular price value with the result of the formula. When a saved price formula already exists for the part, the symbol on the button will be different ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_formula_info.png).
Price formulas are normally used to calculate prices for parts when they are included in different configurations. A price formula makes it possible for the price of an included part to vary, depending on variable values in the configuration where the part is included. Price formula is mostly used on purchased parts with lot sizing rule Linked requirement, where the design and the price varies.
A price formula can also, when needed, be used for flexible pricing of the main part (the part which is being configured). The result of a price formula for the main part is multiplied when configuring the part's regular price.
When the part has a price formula, the calculated price will be used in pre-calculations and orders. In pre-calculations, the price alternative in the selection is calculated with the price formula. If a linked purchase order is created from a requirement of the part via manufacturing order, the supplier price and the part's standard price will be calculated using the price formula and is saved on the order row. On the purchase order row, the calculated price each will be locked by default. If a material included in a manufacturing order has a price formula, the calculated price will be used as planned price and reported price. The calculation is based on the price alternative (according to system setting) which will be recalculated with the price formula.

#### Alternative name
Here you can enter an alternative name which replaces the regular name of the part when it is used in a configuration. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Extended description
Here you can enter an extended description text for the part. This description is shown below the part's name or alternative name on order documents for configurations where the part is included. In the text editor you can write and format texts, insert images, signatures, and hyper links, etc. By clicking the button Insert phrase ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_phrase.png) it is possible to insert different phrases which are registered in the Phrases procedure. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.
However, extra names on parts which you select in a configuration will not be shown on order documents.
