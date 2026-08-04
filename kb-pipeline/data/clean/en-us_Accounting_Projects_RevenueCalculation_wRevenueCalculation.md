## Revenue calculation
In this procedure you perform revenue calculation for projects with the revenue calculation method called Percentage of completion method. It is always the profit mark-up that is used for the revenue calculation.
The intended way of working is to create and save the revenue calculation at the very end of each month after all invoices are recorded and after recording items/reporting items which may affect the project and its calculation are all completed. Then you print the revenue calculation journal with a voucher date on the last of each month.
> You should reverse the income accrual for the previous month before you perform the revenue calculation for the period.
Revenue calculation methods and examples with varied pricing models
Continuous price
Formula: Continuous price = (Stage of completion x Income according to forecast) – Income according to result (advances recorded in the income statement and customer invoices).
Continuous price with profit mark-up
Formula: Continuous price with profit mark-up = Costs according to result x (Percent for Profit mark-up The profit mark-up is a percentage mark-up on the cost price which will generate a suggested quote price.+100)/100 - Income according to result (advances recorded in the income statement and customer invoices).
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
List types

#### General
For the revenue calculation you use the General list type. You can redo the calculation as long as the journal is not reset.
Only projects with status 3 (In progress) that have the Revenue calculation method selected for the project type, are shown in the list.
> Please note! If you work with main projects/sub-projects and have selected the Main project level for the calculation, it is important you make sure that all sub-projects that should be included in the calculation also have status 3, In progress. Sub-projects with a status other than 3 will not be included in the calculation.

#### Previous calculations
In this list type you will only see already performed calculations where the revenue calculation journal for that period is reset. The list shows the conditions on which the calculation was based at the time it was performed regarding forecast, result, stage of completion, mark-up, and recognized income.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
