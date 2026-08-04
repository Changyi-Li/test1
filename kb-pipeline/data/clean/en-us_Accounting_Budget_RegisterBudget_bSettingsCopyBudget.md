### Settings – Copy budget
How to use the copy feature
Example: You wish to create a forecast for the current year which is based on the result this year (e.g. the first quarter) and a budget for the rest of the year.
Then you add two rows in the table Copy from:
- Row 1 – Result as value to copy. Periods 1–3.
- Row 2 – Budget as value to copy. Periods 4–12.
In the section Copy to you enter to what budget the calculation should be saved. For example an alternative budget which you called "Forecast".
Copy from

#### Accounting year
Here you select from which accounting year to copy data. It is possible to copy from historical years, AFS, and regular years. A validation error is shown if you have entered the same year to copy to.

#### Values to copy
Here you choose if you want to copy the result (default) or the budget from the accounting year you selected in the first column. If you select the budget option you must also in the next column select from which budget to copy.

#### Adjust with
Here you can enter a percentage change up or down (negative value) in connection with the copying.

#### From period –To period
Here you select from which accounting period the copying should be made. The default period to copy from is 1. If you have more than one row in this table you must enter which periods each row refers to. You will also see a validation error if you have entered overlapping periods.
Example:
Allowed: period 1–6 for row 1 and period 7–12 for row 2.
Not allowed: period 1–3 for row 1 and period 1–12 for row 2.
> If you enter that copying should be done of a selection of periods (not the entire year) then the existing budget for the other periods will not be deleted.
Copy to

#### Accounting year
Here you select to which accounting year to copy data. It is possible to choose future accounting years.

#### Budget number
Here you select to which budget to copy data.
To copy

#### Dimensions
You can here enter on which level the budget should be copied, that is, which dimensions the copying of budget should be made to. This is useful if you do not want to use budget on for example cost units but you have the result on that dimension. In that case you can uncheck the cost unit (CU) in this setting. This means that the copying of result to budget will not include the budget for cost units.
Example for copy from result Year 1 to Budget Year 2
Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. to copy is set to cost center.
| Year 1 | Account | CC | CU | Proj. | Amount |
|---|---|---|---|---|---|
| Result | 4100 | 10 | 1560 | – | 1000 |
| Result | 4100 | 10 | 1570 | – | 1500 |
| Year 2 | Account | CC | CU | Proj. | Amount |
|---|---|---|---|---|---|
| Budget | – | – | – | – | – |
| Budget | 4100 | 10 | – | – | 2500 |

#### Quantity
With this setting you determine if quantity should be copied. If you activate this setting, budget will be created for quantity and columns for this will also be shown in the list.
