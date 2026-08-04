### Variables
In this table you see the variables that are included as standard. These variables can be used to create own planning formulas.
[See an explanation of all the variables](ExplanationVariables.htm).
You can choose a part to test to see what impact different simulated variable values will have on the part in a selected formula in the Formulas box. This is shown in the Result field.
In the lower portion called Manual variables, you can create own variables that can be used in planning formulas.
> The variables called ORQ– Quantity, actual orders, ORQDE– Quantity, actual orders in past time, and ORQLT– Quantity, actual orders within lead time, are used to load the quantity which is ordered for refill. This can be ordered via purchase orders, manufacturing orders, or stock orders. The variables called RES– Reservations, RESDE– Reservations in past time, and RESLT– Reservations within lead time, are used for the quantity which according to registered orders will be consumed. This can be via customer orders, stock orders, or material rows on manufacturing order.

#### Part
Here you can select a part and this part's planning settings will be shown among the variable values in the table.

#### Code
The variable code that is entered in the formulas. The variable codes that are used in the selected formula have a dark yellow background.

#### Name
The name of the variable.

#### Updated in procedure
Here you see in which procedure the variable's or constant's value is updated.

#### Constant
Here you see the value if it is a constant.

#### Simulated value
Initially shows the current variable value for the selected part in the Part field. Here you can make temporary changes to these values in order to simulate the impact it will have on the result of the selected formula in the Fomulas box. The result is shown in the Result field.
Manual variables
In this table you can add own variables with values that are either constants or values from extra fields. These variables can be used if you create own planning formulas in the procedure.

#### Code
The variable code that is entered in the formulas.

#### Name
A name that describes the variable. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Type
The variable can be Constant or Extra fields. Constant is used if it is a fixed value. Extra field is used if the value should be loaded from an extra field on parts.

#### Value
If the variable is a constant, you enter the value of the constant. If the variable is an extra field, you select from which extra field the variable should load the value. Extra fields of the type Decimal number or Integer must be registered for parts in the Extra fields procedure.

#### Simulated value
Works in the same way as Simulated value in the table above.
