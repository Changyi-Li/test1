### Settings

#### Forecast codes
This table is available for the list types called Create new forecasts and Add/Remove parts in forecast. Here you can add rows with new forecast codes. You must enter a forecast code and a name for the forecast code. Forecasts are generated for entered forecast codes in the table by using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) button on the toolbar in the procedure.
In the Forecast code column you enter a new forecast code or load an existing code by using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature (F4).
In the Name column you see/enter a descriptive text. The name text is entered in the company language and is displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.
With the Active checkbox you determine if the sales forecast should be active or not. An inactive forecast will not be included in the requirement calculation.
In the columns called Customer, Customer group, and District, you connect customer, customer group, or district to the forecast. It is only possible to link/connect the forecast to one of these alternatives. If you link a forecast to a certain customer, only customer orders for that specific customer will be deducted from the forecast. The same function applies if you link a forecast to a customer group or to a district. If you for example have linked a sales forecast to customers in the USA (in the district column), it means only customer orders for customers in that district will be deducted from the forecast.
Existing forecast codes can be activated/deactivated or deleted in the Register sales forecasts procedure.

#### Forecast code
In the Add/Remove parts in forecast list type you choose the forecast code in which you wish to add or delete parts.

#### Add/Remove
In the Add/Remove parts in forecast list type you choose if you want to add or delete parts for the selected forecast code.

#### Distribution of rows
In the Start field you select a start date for the forecast. Today's date is selected by default.
In the table below you distribute the rows over the requested periods. You can for example create daily forecasts in near future, followed by weekly and monthly forecasts. The default values are:
|   | Number of periods | Day in period | Start | End | Explanation |
|---|---|---|---|---|---|
| Daily | 0 | First day | Shows start date | Shows end date | You can choose between First day and First work day. |
| Weekly | 16 | Monday | -"- | -"- | You can select among the days Monday to Friday. |
| Monthly | 8 | Working days | -"- | -"- | The Working days option is the only one available. |
The default values above mean that weekly forecasts will be created for the first 16 weeks. Then 8 monthly forecasts will be created.
With the Calendar setting you select which calendar you want to use for the calculation. Calendars are created in the Calendar procedure.
With the setting called Consider lead time you decide if the forecast calculation should take the lead time into consideration or not. The following options are available:
- No
- Part's lead time.
- Lead time Number of days between ordering date and delivery date. Normally used for purchased parts. to customer
The calculation for lead time is always based on today's date. If you for example select the Part's lead time option and a part has three days lead time and the start date for the forecast is today, then the first three days will not be included in the calculation since they are within the part's lead time.

#### Load quantity from
With this setting you determine if quantity should be loaded from:
- Annual volume
- Annual budget – You should enter year from and year to. The default value here is the current year.
- Forecast rows
Factor has to be entered regardless the selected alternative. The default value here is 1.00. A factor of 1.20 means an increase of 20%, while a factor of 0.80 means a decrease of 20%.
Please note! Quantity from earlier than the selected start date of the forecast will not be included.

#### Distribution – Budget chart
The following alternatives exist for Distribution:
- None/Even distribution – This alternative means that the quantity will be divided by the length of the forecast.
- Budget chart – This alternative means that you must select a budget chart. You register budget charts in the Budget charts procedure.
- Budget chart for part – Here you select a budget chart for the part. Start year and Next year should be entered in the fields that are displayed. If the part does not have a budget chart for Next year, you can instead select a Fallback budget chart for the part.
- Manual – This alternative means that you should manually enter a distribution in percent under the % per period (month) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button.
Under Rounding you find the following alternatives:
- None – No rounding will take place.
- Integer – Rounding will be made to nearest higher whole number.
- Part's rounding quantity – The part's rounding quantity will be used.
- Part's quantity/package – The part's quantity/package will be used.

#### Default setting
The Add or replace field is available for the Update forecasts list type and you can then choose between the following alternatives:
- Delete and replace all existing rows – This means that the existing forecast rows will be deleted by default and are replaced by new forecast rows.
- Add new rows and keep existing rows – This means that existing forecast rows by default will be kept and new forecast rows will be added.
Use the Pre-select "Include" setting to decide if all forecast rows by default should be marked to be included.
Use the Save rows without quantity setting to determine if forecast rows with zero in quantity should be saved. These rows are not saved by default.
