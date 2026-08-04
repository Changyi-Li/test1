### Settings for Percentage of completion method
Before you can use the Percentage of completion method (PCM), you need to configure some settings in Monitor ERP.

#### Basic data – Project
Only the settings specific for the Percentage of completion method are addressed here. For other settings, please see the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project procedure.
The Project types tab
- Revenue calculation method – Here you decide which revenue calculation method should be used for the project type. The available options are: None and Percentage of completion method.
- Level for revenue calculation – Here you decide if the revenue calculation should be performed on the Main project or the Sub-project. It is possible to change this subsequently for the main project in the Project register procedure.
- Pricing – Here you select pricing from the following alternatives: Continuous price, Fixed price, or Continuous price with profit mark-up. If you select the pricing alternative Continuous price with profit mark-up, the mark-up entered for the project type (in the Profit mark-upThe profit mark-up is a percentage mark-up on the cost price which will generate a suggested quote price. column) will be used. This can be changed on the project you register with this project type. The Profit mark-up tab is activated, where you can enter any exceptions.
Calculation example with varied pricing models
Continuous price
Formula: Continuous price = (Stage of completion x Income according to forecast) – Income according to result (advances recorded in the income statement and customer invoices).
Continuous price with profit mark-up
Formula: Continuous price with profit mark-up = Costs according to result x (Percent for Profit mark-up+100)/100 - Income according to result (advances recorded in the income statement and customer invoices).
The Profit mark-up field from the Project register is used, but you can also use exceptions from profit mark-up for different cost types in the Basic data – Project procedure. Profit mark-ups are entered for the project type but they can be changed in the Project register procedure.
Fixed price
Formula: Fixed price = (Stage of completion x Income according to forecast) – Income according to result (advances recorded in the income statement and customer invoices).
When applying this price alternative, the Result, income + Recognized income cannot exceed the forecast income.
When using the Fixed price option, you must record anticipated loss, if any, as soon as this loss is identified. This is due to the precautionary principle which is central when valuating records in the accounting.
If you use fixed price and apply one of the following terms:
a) Income according to forecast < Costs according to forecast.
b) Income according to forecast = Cost according to forecast (which means that CMThe contribution margin (CM) is the difference between the standard price and the sales price. is 0.00 and CRThe contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. is 0%).
Then you must do a different calculation for this project as follows:
Recognized income = (Income according to forecast - Costs according to forecast) - (Income according to result - Costs according to result).
Example to illustrate this:
Income according to forecast = EUR 29,900
Costs according to forecast = EUR 34,300
Income according to result = EUR 29,500
Costs according to result = EUR 33,800
Reported income (loss) = (29,900 - 34,300) - (29,500 - 33,800) => (-4,400) - (-4,300) => -100
- DimensionsDimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. – here you select the dimensions to use for the recognized income for this project type.
The Costs/Income tab
Here you register the income type to use for the revenue calculation. Item 1 in the image below. This is the income type you should enter for the income accounts which will then be used in the Standard accounts procedure. Please note! This income type should be entered for the Project dimension for the actual account in the Chart of accounts procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PCM1.png)
It is important that you check the Recognized income – PCM checkbox for the income type used for revenue calculation. Item 2 in the image above. The income type will not be displayed in the expected result (this would cause a too high income/revenue in the expected result). This income type is also not used for forecast/budget. The income type is only intended for recording of the accrued income according to the revenue calculation.
The Profit mark-up tab
The Profit mark-up tab is activated when you have the pricing alternative Continuous price with profit mark-up entered for the project type. There you can enter an exception per cost type as well as a an income type for automatic updating of the forecast on the project. The forecast will be updated automatically on the project based on the costs incurred + profit mark-up. If you do not enter an exception, the profit mark-up for the project will apply. If you enter a percentage of 0.00 for a cost type, no profit markup will be calculated.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PCM12.png)

#### System settings
Under the Accounting tab and under the Project heading you find system setting which affect the revenue calculation.
-    
Mandatory to enter project cost type in chart of accounts – This system setting determines if it should be mandatory to enter project cost in the chart of accounts. If you want the dimensions to be set to Yes for projects on the balance accounts, you cannot have any type of project cost/income selected for these accounts. The amount will in that case be presented as an income/cost on the project, this is not correct since it is an asset/liability item in the balance sheet. You can determine this with the system setting.
> Please note! If you select the Mandatory option for dimensions for PCM accounts, you must also enter a fixed value for this in the Standard accounts, so at present, we do not recommend this.
- Editable stage of completion in the Revenue calculation – Here you decide if the calculated stage of completion in the revenue calculation should be possible to edit.

#### Chart of accounts
For the accounts that should be used in Standard accounts, you should the income type from the Costs/Income tab in the Project dimension.
.[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PCM2.png)](../../../../Resources/Images/UserGuide/PCM2.png)

#### Standard accounts
Here you enter the accounts to use for recording. If you have entered a dimension for the project type, it is important that the account has dimensions set to Yes for these fields.
We recommend you regarding dimensions select Yes in the Project field for the income accounts, and that you link them to the income type you will use for the percentage of completion method.
Please note! The Reduce of income/Anticipated loss (balance account) account is used both for recording of expected loss at fixed price, and for recording of reduction of income, for example, due to a too high advance invoicing compared to income according to stage of completion.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PCM4.png)](../../../../Resources/Images/UserGuide/PCM4.png)
If you want the application of dimensions to be set to Yes for projects on the balance accounts, you cannot have any type of project cost/income selected for these accounts. The amount will in that case be presented as an income/cost on the project, this is not correct since it is an asset/liability item in the balance sheet. This is determined via the system setting called Mandatory to enter project cost type in chart of accounts.
> Please note! If you select the Mandatory option for dimensions for PCM accounts, you must also enter a fixed value for this in the Standard accounts, so at present, we do not recommend this.

#### Voucher number series/Journals and integration of the revenue calculation journal
Here you should register the voucher number series for the revenue calculation. Then select Via journal – Total as the integration option for the Revenue calculation journal and select the voucher number series that you registered.
