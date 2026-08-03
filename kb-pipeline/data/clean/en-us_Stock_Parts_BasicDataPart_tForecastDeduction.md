### Forecast deduction
Under this tab you add different interval settings regarding forecast deduction for sales forecasts, which can then be selected for a part when the deduction method Periodic intervals has been selected on the part in the Part register.

#### Default
Here you decide if the interval setting should be default when the deduction method Periodic intervals is selected for a part.

#### Number
A row number for the interval settings. This number be changed.

#### Name
Here you see/enter the name of the interval setting.

#### Translations
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Date from customer order
Here you select the delivery date the interval setting should use as base on customer order: initial delivery date or current delivery date. The initial delivery date is normally selected (that is, the delivery date promised to the customer) since the customer probably has made a forecast and then placed the order according to the forecast.

#### Deduct excess from previous period
If you check this box, the forecasts will also be deducted for previous periods provided that a customer order exists that exceeds the period's forecast quantity. See examples in the tables below.
| Setting not activated (default) |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Part X | Period 1 | Period 2 | Period 3 | Period 4 | Period 5 | Total |
| Gross sales forecast | 50 | 50 | 50 | 50 | 50 | 50 |
| Customer orders | 20 | 40 | 20 | 85 | 50 | 215 |
| Net sales forecast | 30 | 10 | 30 | 0 | 0 | 70 |
| TOTAL REQUIREMENT | 50 | 50 | 50 | 85 | 50 | 285 |
| Setting activated |  |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Part X | Period 1 | Period 2 | Period 3 | Period 4 | Period 5 | Total |
| Gross sales forecast | 50 | 50 | 50 | 50 | 50 | 50 |
| Customer orders | 20 | 40 | 20 | 85 | 50 | 215 |
| Net sales forecast | 30 | 10 | 30 | -35 | 0 | 35 |
| Distributed additional deduction* |   | 5 | 30 | -35 |   |   |
| New Net sales forecast | 30 | 5 | 0 | 0 | 0 | 35 |
| TOTAL REQUIREMENT | 50 | 45 | 20 | 85 | 50 | 250 |
> * The forecast for period 2 and 3 has here been redistributed in order to manage the large customer order in period 4.

#### Interval settings
Here you decide if the a forecast calculation should be performed Manually or Monthly. Monthly deductions of forecasts take place using fixed monthly intervals, that is, starting the first of each month. The Intervals box is deactivated if you selected the option called Monthly.
