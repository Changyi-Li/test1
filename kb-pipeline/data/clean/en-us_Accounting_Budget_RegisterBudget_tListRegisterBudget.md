### The list type Register budget
The budget for what you selected is shown in the list. If you under the Selection tab chose to generate empty budget rows, then you will also see rows for accounts which do not have a budget. For those rows, 0 (zero) is shown as budgeted value and you can then change these. Rows for which you leave the 0 (zero), will not be saved in the budget.
You can manually add and delete rows by using the buttons on the function menu. You can export the budget as different file types.

#### Account
Here you see/enter the account that applies for the row. All accounts can be loaded. If you change an account on an existing row, it might affect the available dimensions for the row in question. But amount and quantity columns will be left unaffected. The name of the account is shown in the adjoining field.

#### Warning (W)
In this column you see a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) or a validation error ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) if anything on the row is wrong:
- The budget already exists in the list.
- Income should be entered as negative values. This warning is shown if you have entered a positive value for accounts of the account type Income.
- Costs should be entered as positive values. This warning is shown if you have entered a negative value for accounts of the account type Costs. There is no validation on the other account types.

#### Dimensions (CC, CU, Project)
A check is made against the chart of accounts settings. If it says No in the chart of accounts it means that the columns are not available. When changing the dimensions, this do not affect the amount and quantity columns.

#### Budget chart
Here you can enter the budget chart which should be used in order to automatically distribute the annual budget per period. It is mandatory to select a budget chart. When you enter a budget chart, the period budget amounts will automatically become updated. For existing budget rows (which were already registered) you see the budget chart for the saved budget. For new rows you add (manually or via generation of rows) the budget chart will be set according to the Budget chart setting.

#### Annual budget
Here you see the budgeted amount for the entire accounting year. If you edit this amount, the monthly distribution in the adjoining fields will automatically become updated. The annual budget will also be updated if you enter period amounts. Income is registered as negative values and costs are registered as positive values. A total for the column is made in the footer.

#### Period budget
After the annual budget you see columns for each accounting period. The column headings show the year and month (2017-01 means January 2017). In these columns you see the period amount which applies for the period in question. If you enter values in these fields, the annual budget becomes updated. A total for each column is made in the footer.
