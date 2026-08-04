### Settings (Columns)
In this box you configure settings for each column in the report. Many of the settings are connected to which Type of column is selected and that is why the help topic here is grouped based on the type of the column as seen below.
Type Account/Dimension

#### Contents
With this setting you decide which contents will be shown in the column.
Type Numerical

#### Contents
With this setting you decide which contents will be shown in the column.

#### Balance type
Here you select the type of balance that will be used in the column. This field is not available if the Contents setting is set to Budget or Budget quantity. The following options are available:
- Balance – This option means the total balance will be shown for the account in question.
- Debit balance – This option shows the total value recorded as debit on the account.
- Credit balance – This option shows the total value recorded as credit on the account.
- Net balance (debit) – This option shows the total balance on the account if the account has been charged/debited more than it is credited. If the account in total has been recorded more on the credit side, then you see a zero in this column.
- Net balance (credit) – This option shows the total balance on the account if the account has been credited more than it is charged/debited. If the account in total has been recorded more on the debit side, then you see a zero in this column.

#### Budget number
With this setting you determine from which budget number data should be loaded to the column. This field is only available if the Contents setting is set to Budget or Budget quantity.

#### Time perspective
Here you select the time perspective for data in the column. The following options are available:
- Opening balance – Shows the year's opening balance for the accounting year you have selected within.
- Selected period – Shows result/budget/quantity for the time period you selected by when you print the report (period balance).
- Accumulated for the selected period – Shows result/budget/quantity accumulated up to and including the time period you select by when you print the report.
- Year – Shows result/budget/quantity for an entire year. You decide which year the column should contain in the Year field.
- Rolling – Shows rolling result/budget/quantity back in time, for example the latest year.
- Balance brought forward – Shows the balance brought forward.

#### Year
Here you select from which accounting year data should be loaded in the column. It can be for the year you selected by or up to nine years back in time from the selected year.

#### Period selection
If the Time perspective setting is set to Period you use this field to select if a fixed period should be entered or if a displacement from current selected period should be entered. If you select a fixed period it is always the entered periods valued that is loaded, regardless of which period you selected by when printing the report. If there is a displacement from the current selected period, then the column will display values from a period which is prior to the period you selected by when printing the report.

#### Period / Number of periods
If the Period selection setting is set to Enter a fixed period you should here enter which period that applies. If the Period selection setting is set to Enter displacement from current selected period you should here enter the displacement in number of periods.

#### Number of months back in time
If the Time perspective setting is set to Rolling you should here enter the number of months back in time which should be shown in the report.

#### Document configuration – General Ledger/Journal
Here you can select a variant of the document configuration for General ledger (drilldown) and Voucher (drilldown), if there are more than one variant of the documents registered in the Document templates procedure.
By using the button Edit document configuration ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_xtrareport_designer.png) you open the document in the program DevExpress Report Designer. This is a third-party tool which is included in Monitor ERP for document design.

#### Filter
Here you can filter the column based on the dimensions or heading and select if the filtered dimensions should be included or excluded.
Type Calculated

#### Expression
Here you select the calculation expression which applies for the column. You can use the four rules of arithmetic and integers to calculate columns of the type Numerical, Calculated, and Compare section.
By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) you find a guide where you can select among the columns in the report as well as +, -, *, /, to use in the calculation expression. You add each column by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the respective row. You see the resulting expression in the field in the guide.
> Please note! If you wish to use division "/" you must manually alter the calculation expression regardless if you are using the guide or if you enter the expression manually. For example, if you wish to divide the two columns C7 and C8 and add them in the guide, the resulting expression will become [C7]/[C8]. Then you must manually change the expression making it DIV{ [C7] / [C8] }. The spaces must also be included in the expression.
> Two special columns of the type Calculated are available called Index and Add/Subtract. These will help you when creating different calculating columns, so you don't have to manually write calculation expressions.
Type Compare section

#### Compare column
Here you select a column to compare with a total row. Only numerical columns can be selected.

#### With the total row
Here you select the total row in the Footer under the Section tab to which you want to compare the selected column.

#### In column
Here you decide which column the section should be compared with. That is, the total row above is loaded from this column.

#### Number of decimals
With this setting you decide the number of decimals which values should be shown with in the column. This field is not available if the column type is not set to Account/Dimension.
