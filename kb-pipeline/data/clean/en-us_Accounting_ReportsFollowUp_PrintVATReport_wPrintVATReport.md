## Print VAT report
In this procedure you can print and record the company's VAT declaration/VAT report.
The system performs certain checks and presents the result of these in connection with printing the VAT report. The checks will for example make sure that the journals have been transferred, that the output VAT correspond with the turnover, and shows if there are transactions which cause differences. It is also possible to approve and record the VAT report without printing it.
A VAT report file is created if you have activated the setting Create export file in the Settings box. This file can be sent electronically to your tax authority.
The data you see in this report is based on accounts, daily balances (balances saved per day), opening balances, VAT report definitions, and transactions in the general ledger. With the system setting VAT accounting period you determine whether the VAT report should be based on each month, every other month, or each quarter.
> If you have Quarter or Every other month as VAT accounting period as well as split financial year, where the period that will be reported is in two accounting years, there are two options for VAT management:

1. You can approve and print a VAT report for both accounting years, i.e. the whole period and create one file (like other accounting periods).

2. Alternatively, you can approve and print two VAT reports (one per accounting year) and then report the total manually.
Loading of data to the VAT report
The loading of data to the VAT report is governed by the settings configured in the VAT settings procedure. Under the VAT codes tab you enter links to the VAT report, for sales and for purchases.
The rows on the VAT report referring to input and output VAT loads the values based on the VAT code entered for each VAT code in the Chart of accounts.
How the rows referring to purchases and sales load the values for the report depend on how the system setting Basis for VAT report is loaded from is configured as follows:
-   
If the setting option VAT code in chart of accounts has been selected, it means the rows referring to purchases and sales are loaded from the balance for the accounts which are linked to VAT codes concerning sales/purchase (according to the VAT settings). When the option VAT code in chart of accounts is selected, you also see the Detailed/account tab.
-   
If the setting option VAT code in general ledger transactions has been selected, the values are loaded from the general ledger. For each transaction in the general ledger a VAT code is saved depending on settings made for example on customer/supplier. For example when VAT row referring to sales within the EU should be loaded, then the system checks all transactions posted using the VAT code which concerns this. With this method it is possible to have one account using different VAT rows in the VAT report.
It is also possible to load old reports using the list type Reprint – VAT report.
Cancellation of VAT report
It is possible to cancel (undo) an already recorded VAT report, by checking the checkbox Cancel (C) under the VAT report tab. When canceling a VAT report a reversal voucher is automatically created. It is possible to again create a VAT report for the period.
List types

#### VAT report
Under the Selection tab you can choose which dates you want the report to include. If you use monthly VAT, the first date of the calendar month will be suggested in the From field, and the last date of the calendar month will be suggested in the To field. For quarterly VAT, the first date in the quarter will be suggested in the From field and the last date of the quarter will be suggested in the To field.

#### Detailed per VAT row
In this list type you can analyze and view additional details about the records (vouchers and invoices) that are used as basis for the VAT report. This can be done for any selected period, included for already reported periods. The report displays the details grouped by/total by VAT row. You can select the list by different terms, such as, customer, supplier, date, VAT code, and so on. In the list you also see the customers' and suppliers' VAT registration number, if these needs to be checked. If the system is configured to report VAT based on the VAT code in general ledger transactions, you can also update the VAT code for the transactions directly in the list.

#### Detailed per voucher
This list displays the vouchers which have affected the VAT report. The list is grouped by voucher and only shows the voucher rows that affect the VAT report. For each row you find information about VAT code and information about on which VAT row the value is displayed in the VAT report. If the system is configured to report VAT based on the VAT code in general ledger transactions, you can also update the VAT code for the transactions directly in the list.

#### Detailed per invoice (input VAT)
This list is used to display a specification of which invoices and vouchers that form the basis for report of input VAT. If the net amount should be reported in the VAT report, you will also see the net amount and gross amount for each record. In the list it is also checked if the posted VAT amount differs from the VAT amount on the invoice. Under More info you can also see the invoices' amounts in foreign currency (that is, currency other than the company currency).

#### Detailed per invoice (output VAT)
This list is used to display a specification of which invoices and vouchers that form the basis for report of output VAT. If the net amount should be reported in the VAT report, you will also see the net amount and gross amount for each record. In the list it is also checked if the posted VAT amount differs from the VAT amount on the invoice. Under More info you can also see the invoices' amounts in foreign currency (that is, currency other than the company currency).

#### Reprint – VAT report
With this list type you can load old VAT reports. Under the Selection tab you select which reports you want to see. When you load data a result list will be displayed under the VAT report tab, containing the selected VAT reports.
If the VAT report belongs to an open period it is possible to undo/reverse it. Then the VAT report document is deleted and the rectification voucher/reversal voucher will remove the initial report for these dates. After this you can create a new VAT report for the period in question.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
