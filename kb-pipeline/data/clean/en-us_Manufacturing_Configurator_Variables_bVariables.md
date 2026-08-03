### The Variables table

#### Code
Here you see/enter the code of the variable. This code is used when you want to insert the variable in formulas. The field is alphanumerical and can contain a maximum of 35 characters. This field is case sensitive. This means that the codes "H1" and "h1" are different variables.

#### Name
Here you see/enter a description of the variable. This text will then be used on documents and you can see it when you write formulas. The variable name will be suggested as name when you create new variables. The field is alphanumerical and can contain a maximum of 80 characters. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Type
Here you select the type of the variable. The different variable types are: Text, Number, Boolean, and Date. For a variable of the type Number, the closest following three fields are active. There you can enter number of decimals, select a unit, and enter a multiple.

#### Number of decimals
(Number) Here you enter how many decimals which should be used for values for the variable. If you enter zero (0), you will only be able to enter the variable as integers in configurations.

#### Unit
(Number) Here you enter the unit of the variable. The units you can select among are the ones registered in the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part.

#### Multiple
(Number) Multiple of value. The value you enter here determine that values entered for the variable in formulas only can be multiples of this value.

#### Default value
The default value of the variable. For the variable type Number, a validation will be made to see that the default value matches the value in the multiple column, if any. For the variable type Boolean it is possible to select Yes or No. For the variable type Date you can select a date. For the variable type Text the field is alphanumerical.

#### Formula
Here you see the formula which you enter under the f(x) button.

#### Formula for variable f(x)
For the variable types Text and Number you find the button Formula for variable ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_formula.png) in the f(x) column. Here you can create a formula for the variable. When a formula has already been entered for the variable, another symbol is shown on the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_formula_info.png) and the fields Multiple and Default value are deactivated.
A formula can consist of other variables, operators, terms, and functions. Formulas can also be used to make variables into constants. For example, you can create a variable and name it "pi" and enter the value "3.141592" as formula for the variable.
A formula for a variable cannot contain the variable which the formula is written for, that is, the variable cannot contain itself in a formula.
A formula which you create here for a variable cannot be modified in the places where the variable is used, for example in a configuration group. In that case you must go here to modify the formula. The variable register then functions as a central formula register. If you modify a formula here it will also directly affect configurations where the variable is used.
It is possible to create a formula for a variable directly in a configuration group, but then the formula will only apply in the configuration in question.
> You can start a row with /// if you want to write a comment for your formula.
Read more in the section [Formulas](../../../UserGuide/Using/Configurator/Formulas.htm) in Using MONITOR about the product configurator.

#### Show on document
Here you decide on which of the documents that the variable and its value should be shown: Customer order, Manufacturing order, or Purchase order.

#### Comment and Files
Here you can enter a comment and also link files to the variable. These are shown to the user who creates configurations with variables on orders.

#### Active
A new variable is by default set as active and thereby it becomes available in configuration groups. If the variable is used in any configuration group, then it is not possible to deactivate it. A deactivated variable is possible to delete if for example it is no longer used.
