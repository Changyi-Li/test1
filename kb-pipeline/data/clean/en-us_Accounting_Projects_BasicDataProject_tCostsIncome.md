### Costs/Income
Here you register all different types of costs and income which can occur in a project. When you install the system, there are a number of different costs and income included as examples. There are also four project costs for material, subcontract, and work in manufacturing order, and also material in customer order. These costs cannot be deleted, edited, or deactivated. But you can translate their names to different languages. The different types of costs and income are also included as a selection term in different list procedures.

#### Number
Here you can see the number for the position of the row. This field is numerical. A new row will by default be assigned the next available number. The table/list is sorted by this column. A number is unique and cannot occur on more than one row in the table.
It is possible to change the number on the included cost/income types (except for the first four) and the types you register. If you change the row numbers you should re-sort the column via the column heading in order for the rows with changed row numbers should be shown in the correct place.

#### Alias for BI
Here you can change the record's alias. This alias is used during data mining from records in the database in Monitor ERP to the database for Business Intelligence. The default value of alias is the same as the record's code/number, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on multiple records, for example customers, then data from these will be merged into a joint record in the database for business intelligence.
You activate alias for BI with the system setting Use alias when exporting to Business intelligence.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Cost/Income
Here you determine if the row should be a cost and/or income.

#### Cost/Income group
Here you decide if the cost/income should be included in a cost/income group.

#### Result is loaded from
In this column you decide how actual costs an income should be loaded in the projects. The setting also governs which type of costs and income should be possible to select for reporting in different procedures in the system. Regarding costs and income to load from the accounting, you should create a link n the Chart of accounts procedure to the cost type in question.

#### Planned is loaded from
This applies if the row is a cost. Here you determine from where planned/ordered costs for the projects will be loaded for this row.

#### Expected result is loaded from
Here you determine from where the expected result for the projects will be loaded for this row.

#### Cost per hour
This applies if the row is a cost. Here you enter a general hourly cost for the row. The cost is entered in the company currency.

#### Exceptions
This applies if the row is a cost. Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can, per project type, enter a default hourly cost for this row. This overrides the general hourly cost which is entered in the Cost per hour field.

#### Excluded project types
Here you decide for which project types this cost or income should not be possible to use or report. However, please note that the system will always read all costs and income when loading the result. The reason for this is that a change made in this field should not be able to cause different costs or income in the project to disappear.

#### Exception from cost mark-up
This applies if the row is a cost. Here you can enter an exception from the mark-up. The exception will apply to the cost type on the row in question. A mark-up entered here will override the mark-up found under the General tab for the project. Please note! If you enter 0.00%, no mark-up will be used on that cost type. If the field is empty, the mark-up entered for the project will be used.

#### Invoicing
This applies if the row is a cost. This determines whether an invoice basis should automatically be created based on reports for the cost type. The following options are available:
-   
No – no invoice basis is created.
-   
Yes, cost price – an invoice basis will be created automatically, the suggested price will be the reported cost.
-   
Yes, price acc. to part – an invoice basis will be created automatically, the suggested price will be based on the linked part’s price lists. A part is chosen under the Part for invoicing column (see below).

#### Part for invoicing
Here you decide which part you want to use on the invoice basis. Only parts of the type Service can be selected. The invoice basis’ posting is based on the part's product group.

#### Recognized income – PCM
Mark Recognized income – PCM for income types used for revenue calculation. This is done to remove the income type from the expected result (that is, to not show a too high income in the expected result). This income type is also not used for forecast/budget. The income type is only intended for recording of the accrued income according to the revenue calculation.

#### Active
With this checkbox you determine if the cost or the income is active, and thereby possible to select in the project. An inactive cost or income is not possible to post on or to report on. But the information is always read.
