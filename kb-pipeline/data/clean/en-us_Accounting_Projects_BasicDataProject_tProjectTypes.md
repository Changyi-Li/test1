### Project types
Here you can register own project types. When you install the system, four different project types are included as examples.
Project types are used to divide the projects in different areas of use. You link/connect templates to the project types and these templates will then determine default settings and values in the projects. Project type is also available as a selection term in different list procedures.

#### Number
Here you can see the number for the position of the row. This field is numerical. A new row will by default be assigned the next available number. The table/list is sorted by this column. A number is unique and cannot occur on more than one row in the table.

#### Alias for BI
Here you can change the record's alias. This alias is used during data mining from records in the database in Monitor ERP to the database for Business Intelligence. The default value of alias is the same as the record's code/number, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on multiple records, for example customers, then data from these will be merged into a joint record in the database for business intelligence.
You activate alias for BI with the system setting Use alias when exporting to Business intelligence.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Basic type
Here you select the basic type for the project type. Today the available option here is Project.

#### Prefix
A prefix with up to 3 characters can be entered and the system will then automatically add the prefix at the start of the number loaded from the number series.
For example, when you register a project and the next number in the number series is 1001 and the prefix is PU on the project type, then the project number will become PU1001.

#### Priority
The priority is used to prioritize quotes, inquiries, orders, or projects. The default value here is 9. You can enter a digit between 1 and 9, where 1 is the highest priority. This field cannot be left empty.
The priority of the project is possible to change at a later time.

#### Cost mark-up
In this column you see/enter a default mark-up for the project type (in percent). The mark-up of the project is possible to change at a later time. The mark-up is calculated based on the costs of the project, and is the basis of the project's result. It is also possible to use mark-up exceptions for different cost types. This is entered under the Costs/Income tab.

#### Inactive
With this checkbox you determine if new projects which you create with this project type should be inactive. If so, someone must then manually change the status of the projects before it is possible to report on them.

#### Project group
The project group you select here will be default for new projects you create using this project type. Project groups are handled under the Project groups tab. Project groups are used as an information field and is also available as a selection field in lists.

#### Activity template
The activity template you select here will by default become linked to new projects you create using this project type. The activity templates are predefined sets of phases and activities in projects. These are handled under the Activity templates tab. The activity template of the project is possible to change at a later time. An activity template can also be excluded from a project type. This means that the specific activity template cannot be linked to the project type in question, and it can also not be selected for projects with this project type.

#### Project manager
The project manager you select here will be default for new projects you create using this project type. You can select among the persons marked as project managers in the personnel records. The project manager for the project is possible to change at a later time.

#### Order type
Here you can determine which order type should be used when invoicing. You can only choose order types of the New sales basic type. If the field is left empty, the order type that is set as default for your user in the Users procedure will be suggested. If you have not configured a default order type there, then the order type you used on the most recent order will be suggested.
> In the Order types procedure you can configure settings for order types such as price strategy, rate type strategy, and posting.
> Please note that the setting Create invoice basis must be activated for the order type.

#### Revenue calculation method
Here you select the revenue calculation method for the project type. The available options are: None and Percentage of completion method. The Percentage of completion method is a method of managing work in progress at year-end closing. This means income is registered as services are being performed and material is consumed, while income is accrued and costs recognized as expenses when resources are consumed. Income is accrued based on the stage of completion, which refers to the percentage of a commission deemed to be completed on the balance sheet date.

#### Level for revenue calculation
Here you decide if the revenue calculation should be performed on the Main project or the Sub-project. It is possible to change this subsequently for the main project in the Project register procedure.

#### Pricing
Here you select pricing for the project type. The available options are Continuous price, Fixed price, or Continuous price with profit mark-up. If you have selected the pricing option called "Continuous price with profit mark-up", the mark-up entered for the project type will be used (from the Profit mark-up The profit mark-up is a percentage mark-up on the cost price which will generate a suggested quote price. column). This profit mark-up can be edited for the project in the Project register procedure.
If you have selected the pricing option called "Continuous price with profit mark-up", the Profit mark-up tab will become activated. Under this tab you can register exceptions, if any, for profit mark-ups for each cost type and income type for automatic forecast generation for the project. If you do not want to include a specific cost type when calculating profit mark-up, you should enter an exception of 0.00% for it.
Calculation example with varied pricing models
Continuous price
Formula: Continuous price = (Stage of completion x Income according to forecast) – Income according to result (advances recorded in the income statement and customer invoices).
Continuous price with profit mark-up
Formula: Continuous price with profit mark-up = Costs according to result x (Percent for Profit mark-up+100)/100 - Income according to result (advances recorded in the income statement and customer invoices).
The Profit mark-up field from the Project register is used, but you can also use exceptions from profit mark-up for different cost types in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project procedure. Profit mark-ups are entered for the project type but they can be changed in the Project register procedure.
Fixed price
Formula: Fixed price = (Stage of completion x Income according to forecast) – Income according to result (advances recorded in the income statement and customer invoices).
When applying this price alternative, the Result, income + Recognized income cannot exceed the forecast income.
When using the Fixed price option, you must record anticipated loss, if any, as soon as this loss is identified. This is due to the precautionary principle which is central when valuating records in the accounting.
If you use fixed price and apply one of the following terms:
a) Income according to forecast < Costs according to forecast.
b) Income according to forecast = Cost according to forecast (which means that CM The contribution margin (CM) is the difference between the standard price and the sales price. is 0.00 and CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. is 0%).
Then you must do a different calculation for this project as follows:
Recognized income = (Income according to forecast - Costs according to forecast) - (Income according to result - Costs according to result).
Example to illustrate this:
Income according to forecast = EUR 29,900
Costs according to forecast = EUR 34,300
Income according to result = EUR 29,500
Costs according to result = EUR 33,800
Reported income (loss) = (29,900 - 34,300) - (29,500 - 33,800) => (-4,400) - (-4,300) => -100

#### Profit mark-up
Here you can enter a general profit mark-up in percent. If profit mark-up should be exempted, such exceptions should be registered under the Profit mark-up tab.

#### Dimensions
Here you select the dimensions to use for the recognized income for this project type. (Applies to project types with the revenue calculation method set to Percentage of completion method.)

#### Costs
By clicking the Costs button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can – for the project type in question – configure if and how costs for material, subcontract, and work should be loaded from manufacturing order to the projects and which price alternative should be used for the costs.
For each of the costs – material, subcontract, and work – you can configure the following:
- No – Means that the cost is not loaded.
- Planned/Expected result – Means that the cost is loaded to the Cost columns under Planned and Expected result in the projects.
- Planned/Result/Expected result – Means that the cost is loaded to the Cost columns under Planned, Result, and Expected result in the projects.
The price alternatives available for these three costs are:
- Planned/Reported
- Current
For customer orders you can configure if material cost should be loaded. If material cost should be loaded, you have the following options:
-   
Yes (all transactions) – With this option all transactions will be included as material costs.
-   
Yes (only rows with "Affect balance") – With this option only the order rows with affect on balance will update the project with costs, This means that, for example, credit invoices which do not affect the balance will be excluded when the project's costs are updated.
Loading of costs from customer order can be applied when you do not record COGS on project and you have parts on the customer order which have been taken from stock. This can, for example, be spare parts and such which should be carried as an expense on the project, but that have not been posted on the project at the time of the purchase or have a manufacturing order which is linked to the project. For this type of reading to take place, it is required that the part is not labeled with "Purchase on project" in the Part register procedure, and that the rows are posted on project on the revenue account. Costs for order driven manufactured parts will not be loaded. The value loaded is primarily the manually entered standard price on the order row, secondarily the standard price from the Part register procedure.
Other cost types which should be possible to add to projects should be registered under the tab Costs/Income.

#### Comment (internal/external)
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png). Here you can enter a default internal comment and a default external comment for the project type. It is only the external comment that will be printed on documents. The comments for the project is possible to change at a later time.

#### Files (internal/external)
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button. Here you can link default internal and default external files to the project type. It is possible to add or delete linked files to the projects at a later time.

#### Active
With this checkbox you determine if the project type is active. This means that the project type is possible to select for projects that you register.
