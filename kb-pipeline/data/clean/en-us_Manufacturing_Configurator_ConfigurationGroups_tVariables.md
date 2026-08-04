### Variables
If variables should be included in the configuration group you can add and delete them under this tab. You can also set different default values in the variables. A variable must be unique in the configuration group.

#### Code
Here you see/enter the code of the variable. You can select among the variables registered in the Variables procedure. In the Name column you see a descriptive name of the variable. In the Type column you see the type of the variable. In the Unit column the variable's unit is shown (applies to variables of the type Number).
The variable must then be placed in the structure under the tab Structure/Guide.

#### Minimum value / Maximum value
In these fields you enter the variable's minimum value allowed and maximum value allowed.

#### Multiple
A multiple of the value is loaded from the variable register if such has been entered, but you can override this here for the variable in the configuration group in question.

#### Default value
A default value is loaded from the variable register if such has been entered, but you can override this here for the variable in the configuration group in question.

#### Link to field
Link to field is used together with Determined by option list. Instead of creating variable values on the options (which are shown in the bottom section) in the option list selected in the field Determined by option list, you instead select a field here and then enter the values directly on that field in the part register. This method is appropriate if the same part occurs as an option in multiple configuration groups since you then only have to register the values once. The following fields can be selected:
- For variables of the Number type: Standard price, Net weight, Extra fields, Selected quantity, and Setup quantity.
- For variables of the Text type: Part number and Extra fields.
- For variables of the Date type: Extra fields.
- For variables of the Boolean type there are no alternatives at present.

#### Aggregation method
AggregationAggregation is data that is totaled or combined, creating new data. method is used together with Determined by option list. A variable can only have one value and since you in some cases can make multiple options that affect the value, you must enter how this should be handled. You must configure a setting even if you know that it is only possible to make one selection. The available options are:
- For variables of the Number type: First, Quantity, Total, Average value, Min., and Max.
- For variables of the Text type: First, Min., Max., and Join.
- For variables of the Boolean and Date types: First, Min., and Max.

#### Extra fields
Extra fields are used together with Determined by option list and when you in Link to field have selected Extra fields. Here you then select the which extra field which should be used. First there should be at least one extra field registered for parts in the Extra fields procedure. The extra field in the part register is then used to give variables values in the configurator.

#### Formula f(x)
By clicking the Formula button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_formula.png) you can enter a formula for the variable which only apply in the configuration group in question. When a formula has already been entered, another symbol is shown on the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_formula_info.png) and the fields Multiple and Default value are deactivated. If the formula for the variable is entered in the Variables procedure, you can see the formula and the variables included in the formula. It is possible to override the default formula by unlocking the padlock under the formula editor. The variables which should be included in a formula must also be added here.
> You can start a row with /// if you want to write a comment for your formula.

#### Determined by option list
Here you can select if this variable should be determined by one or multiple option lists. The function is used when you want a variable to automatically get its value, depending on one or multiple options. You select among the option lists that exist in the configuration group. It is possible to add values for each option in the bottom table. A user then does not need to enter the variable value when configuring an order, it will instead get a value suggested based on the part which is then selected from the determining option list.
> Please note! If a variable is both determined by option list and has a formula entered, then the system will only take the formula into consideration during order registration.

#### Show on document
Here you decide on which of the documents that the variable and its value should be shown: Customer order, Manufacturing order, or Purchase order. The setting is loaded from the variable register, but you can override this here for the variable in the configuration group in question.

#### Mandatory
Here you determine if the variable is mandatory or not. By default it is set as mandatory. This means that the user has to fill in a value on the variable when configurating an order. In that case, leave the field Default value empty.
