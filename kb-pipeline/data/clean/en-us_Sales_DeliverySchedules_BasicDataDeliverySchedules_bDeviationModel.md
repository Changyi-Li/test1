### Deviation model
Here you can define deviation models that will then be used for analysis in the Analyze delivery schedules procedure.
You connect the deviation models to:
- The customer link under the Sales tab in the Part register.
- The part in the Part register.
- The customer in the Customer register.
Using the buttons on the function menu you can add, delete, and copy.

#### Search sequence for deviation model for delivery schedules
Deviation models for delivery schedules are loaded and applied according to the following search sequence:
1. Deviation model entered in the customer’s part link.
2. Deviation model entered for the part in the Part register.
3. Deviation model entered for the customer in the Customer register.
4. Deviation model entered for the delivery schedule type.
The first model found in this sequence will be applied.

#### Number
A deviation model gets a row number. The first row starts with 1. The row number cannot be changed.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Ignore lag
With this setting you decide if requirements coded as “Lag The term "lag" refers to the total sum of the planned setup time and unit time that has not yet been reported as finished for a planned finish period.” should be ignored when the deviation model is applied.

#### Used in
Here you can see all entities to which the deviation model is linked, as well as which type of link it is (Customer link, Part and/or Customer).
