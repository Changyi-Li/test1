### Formulas
Formulas are used in several places in the configurator and the thing they have in common is the use of variables to perform calculations. The formulas are basically used in two ways:
- To calculate values.
- To analyze if a term is true or false.
The different formulas you can create are determined by the different types of variables that exist. These can be Text, Number, Boolean, and Date. The different types of formulas that exist are:
- Time formulas – Used for operations to calculate unit times and setup times.
- Quantity formulas – Used to calculate quantity and setup quantity for materials.
- Price formulas – Used to calculate prices for included/incorporated parts and can also be used for flexible pricing of main parts (the parts you configure).
- Variable formulas – Used on variables to calculate values on variables.
- Instruction formulas – Used to calculate values which should be displayed in an instruction.
- Rule formulas – Used in rules when you want to create terms which apply variables. These formulas always result in "true" or "false".
You create the formulas in a formula editor on the records when formulas can be created. You access the formula editor by clicking the button Formula ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_formula.png). When there already exists a saved formula, you will see a different symbol on the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_formula_info.png).
The formulas are constructed as logical and mathematical expressions of available variables, operators, terms, and functions. Under the Use (times) column, you can see how many times a variable has been used in a formula.
For all different types of formulas (except for variable formulas and rule formulas) you add one or multiple configuration groups in the formula editor (to see the available variables) and you select/add a formula number for each configuration group. You can add more formula numbers and create different formulas for these in the formula editor. You can also choose to use the same formula number for multiple configuration groups.
Different validations are made in the formula editor. Validations are for example made to make sure the result of the formula is of the right type, e.g. a number or a text. Validations are made to see that the entered variables exist, for example if a formula is copied from one material row to another material row and that a configuration group is selected in the formula editor. If validation errors occur, what is wrong will be displayed in red text. Then you cannot save the formula using the OK button in the formula editor until you have corrected the problem.
> Formula functions
For a time formula or quantity formula for operation or material in BOM and routing, you can choose one of three different formula functions to be taken into consideration when registering an order. These are to multiply, add, or replace the regular value of unit time/setup time and the quantity/setup quantity with the result of the formula. You select this in the top left part of the formula editor.
For a price formula on a part in the part register, the formula function is always to multiply the regular value on the part's price by the result of the formula. That function cannot be changed in the formula editor.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/formulaFunction1.png)](../../../../Resources/Images/TrainingMaterial/formulaFunction1.png)
For a variable formula on a variable, the formula function is always to give the variable the value of the formula's result.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/formulaFunction2.png)](../../../../Resources/Images/TrainingMaterial/formulaFunction2.png)
For a rule formula in a rule definition, the formula function is always to give the variable the value "true" or "false" from the formula's result.
For a instruction formula in a configured instruction, the formula function is always to give the variable the value of the formula's result.
IntelliSense in the formula editor
In order to help you write formulas quickly and ensure you don’t write variable codes incorrectly, the formula editor includes a function called "IntelliSense” which provides ongoing suggestions for variables and functions as you write in the formula editor.
To get suggestions for variables in the formula editor, enter the left square bracket [ using the keys Alt Gr + 8. This will show a list of the variables available in the selected configuration group.
Variables must be written inside square brackets [ ] in this formula editor. The variables are also case sensitive. For example, the variable code “Wide” is not the same as the variable code “wide”.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/intelliSense1.png)
There are two differences compared to writing variables in the formula editor in the Planning formulas procedure. There, variables are always written in capital letters and without square brackets.
Over the Result field, a tooltip displays the variable values used when testing the formula.
If you enter a letter in the formula editor you’ll get suggestions for all of the functions that begin with that letter. For example, if you enter an “s” you’ll get a list of suggestions with the functions that begin with this letter.
You select variable or function using the arrow keys and press Enter to insert it in the formula. You can also double click the row to insert it. To the right in the list you will see a description of the marked variable or function.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/intelliSense2.png)
Using the key combination Ctrl + space you access all available variables and all function.
> Details of all functions in the formula editor:
Name
| Description | Syntax | Result | Abs |
|---|---|---|---|
| Returns the absolute value of a specified number. | Abs(-1) | 1M | Acos |
| Returns the angle whose cosine is the specified number. | Acos(1) | 0d | Asin |
| Returns the angle whose sine is the specified number. | Asin(0) | 0d | Atan |
| Returns the angle whose tangent is the specified number. | Atan(0) | 0d | Ceiling |
| Returns the smallest integer greater than or equal to the specified number. | Ceiling(1.5) | 2d | Cos |
| Returns the cosine of the specified angle. | Cos(0) | 1d | Deg |
| Returns the degrees of an angle that is specified in radians. | Deg(0) | Deg(Pi()) = 80 | Exp |
| Returns [ e ] raised to a specified power. | Exp(0) | 1d | Floor |
| Returns the largest integer less than or equal to the specified number. | Floor(1.5) | 1d | IEEERemainder |
| Returns the remainder resulting from the division of a specified number by another specified number. | IEEERemainder(3, 2) | -1d | Log |
| Returns the logarithm of a specified number. | Log(1, 10) | 0d | Log10 |
| Returns the base 10 logarithm of a specified number. | Log10(1) | 0d | Maximum |
| Returns the larger of two specified numbers. | Max(1, 2) | 2 | Min |
| Returns the smaller of two numbers. | Min(1, 2) | 1 | Pi |
| Returns the value of Pi with 14 decimals. | Pi() | 3.14159265358979 | Pow |
| Returns a specified number raised to the specified power. | Pow(3, 2) | 9d | Row |
| Returns the radians of an angle that is specified in degrees. | Rad(0) | Rad(180/Pi()) = 1 | Round |
| Rounds a value to the nearest integer or specified number of decimal places. The mid number behavior can be changed by using EvaluateOption.RoundAwayFromZero during construction of the Expression object. | Round(3.222, 2) | 3.22d | Sign |
| Returns a value indicating the sign of a number. | Sign(-10) | -1 | Sin |
| Returns the sine of the specified angle. | Sin(0) | 0d | Sqrt |
| Returns the square root of a specified number. | Sqrt(4) | 2d | Tan |
| Returns the tangent of the specified angle. | Tan(0) | 0d | Truncate |
| Calculates the integral part of a number. | Truncate(1.7) | 1 | in |
| Returns whether an element is in a set of values. | in(1 + 1, 1, 2, 3) | true | if |
| Returns a value based on a condition. | if(3 % 2 = 1, 'value is true', 'value is false') | 'value is true' | For trigonometric functions (such as cosine, sine and tangent), the angle is always stated in radians. For example, if you have a variable v which is stated in degrees, and you want to calculate the cosine of the variable, the formula is Cos(Rad(v)). |
Values in variables of the type Text are written using apostrophes, for example Blue is written 'Blue'. Values in variables of the type Date are written surrounded by number signs, also called hash. For example, the date 2018-11-14 is written as #2018-11-14#.
In addition to variables and functions, you can also use the below operators and terms in formulas. For operators and terms you will not get suggestions. These have to be entered manually in the formula.
Read about all operators and conditions in the formula editor:
Operators
| Conditions | < > = <> if(condition, true, false) and or not |
|---|---|
| + - * / % ( ) | Adding variables and formulas using drag and drop |
In configured instructions (the CI button) on operations and material in BOM and routing as well as for options in option lists, you can also enter variables and formulas using drag and drop. There you mark the variable you want in the variable table or the formula you want in the formula table, and then you drag it using the mouse pointer to the place in the instruction where you want it.
Variables and formulas can also be entered manually within square brackets in configured instructions. A variable is written as [v:variable code]. A formula is written as [f:formula name]. Please note! You should start with "v:" or "f:" within the square brackets. A validation is made to see that a variable or formula is available when you manually enter them.
Variables and formulas can also be entered manually within square brackets in configured instructions. A variable is written as [v:variable code]. A formula is written as [f:formula name]. Please note! You should start with "v:" or "f:" within the square brackets. A validation is made to see that a variable or formula is available when you manually enter them.
