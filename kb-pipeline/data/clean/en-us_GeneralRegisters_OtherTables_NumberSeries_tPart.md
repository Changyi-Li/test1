### Part
Number series for parts.
The Series box
Here you add the number series that you want to use for parts. By using the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) you can change the order of the number series. The top row of the number series which have the same condition. This will be used if the condition is fulfilled. The bottom row works as a general number series which is used if none of the conditions are met in any of the number series.

#### Row
Here you see a fixed number on the row of the number series. If you move a number series up or down in the table, the number series will get the number of the row which it is placed on.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Next number
Here you can see the next number that will be used in this number series for part numbers. Please note that if the next number is entered manually when creating a part in the part register or when importing a part, this number will not be updated. A check is however carried out when a part is to be assigned the next number to see whether the number is available. If not available, the next number in the series is assigned and the number in this field are updated.

#### Format
In this field you enter one or multiple tags that describe structure and contents of the number series The tags available to use in part numbers are described below. You must always include the <code> tag in the field.
| Tag | Description |
|---|---|
| <code> | The next number in the number series. |
| <yyyy> | The year, containing four digits, for example "2016". |
| <yy> | The year, containing two digits, for example "16". |
| <MM> | The month, where "01" means January. |
| <dd> | The day in the month, for example "22". |
| <HH> | Hour. |
| <mm> | Minute. |
| <ss> | Second. |
| <week> | The week number, containing two digits, for example 01-53. |
A number series can be composed by different tags which are separated with an optional character, see example below.
Examples of composed number series:
<code>-<yyyy> results in numbers such as "10001-2020", "10002-2020".
<code>:<yy>-<MM>-<dd> results in numbers such as "10001:20-02-19", "10002:20-02-19".

#### Active
With this checkbox you decide if the number series is active and can be used.
The Conditions box
Here you add terms/conditions which decides when the number series in question will be used.
If you add multiple conditions with different grouping terms, then the number series will be used when all of these conditions are fulfilled. If you add multiple conditions with the same grouping term, then the number series will be used when one of these conditions are fulfilled.

#### Grouping term
The grouping term determines for what the number series should be used. You can select from the following: Part template, Part code, Product group, and Part type.
Which of the number series in the Series box should be used depends on the grouping term and its interval. A part can in theory be included by multiple number series. If multiple number series match the grouping term, it is the order of the number series which applies (the number series row which is at the top of the rows with the same grouping term).

#### From and To
In these fields you can enter an interval for the selected grouping term. This determines when the number series should be applied within the grouping term.

#### Exclude
Here you decide if the selected interval in the condition should be excluded. This means, the number series should not be used within the grouping term for the specified interval.
