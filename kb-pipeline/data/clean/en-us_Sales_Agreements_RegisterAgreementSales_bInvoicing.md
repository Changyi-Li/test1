### Invoicing

#### Customer number, invoice
Here you see/enter the customer that should be invoiced after delivery. This is by default the same customer number as on the header row of the agreement, unless the customer has a different Customer number, invoice in the customer register. The customer number you see here is the customer to whom the invoice should be sent for the agreement, for example, a head office. The customer on the order (the customer number on the header row) is the customer utilizing the agreement.
> Please note! The accounts receivable is updated for the customer of the invoice and the sales statistics is updated for the customer on the agreement.

#### Invoicing method
In this field you decide if the selected invoicing interval should be invoiced in advance or in arrears. The default invoicing method is In advance.
The suggested date when using In advance will be the last of the month prior to the period which the agreement concerns. When using In arrears, the suggested date is the first in the next period which the arrears concerns. It is possible to change these date when printing the invoice.
If you change invoicing method, the invoicing date will be changed for the invoicing bases not already released. A default invoicing method can be configured for the agreement type in the Order types procedure.
Important if you have suspended VAT activated during advance invoicing for agreements
When invoicing, the VAT account for suspended VAT is used as well as the standard account for preliminary accrual account.
When payment is made, the suspended VAT is transferred to the account for output VAT and the net amount is transferred to the accrual account according to the agreement.
If the Basis for VAT report is loaded from system setting has been set to VAT code in general ledger transactions, the following applies: When paying an advance invoice a VAT code is entered on the posting row regarding paid advances. The VAT code is loaded from the invoice being paid. This results in a correct accounting of turnover in connection with when the VAT accounting loads the basis for the VAT report via VAT code on general ledger transactions.
If the system setting is set to load VAT code in chart of accounts, the VAT code will be used according to the setting of the account, when you do not consider the VAT code of the transaction. In order not to create differences in the VAT accounting, the account for paid advances is linked to the VAT row for turnover liable to VAT.

#### Planned invoice date
You can use this function to decide how many days before or after a period the Planned invoice date will be set.
For example, if an agreement has Invoicing method set to In advance, the Invoicing interval set to Monthly, and Planned invoice date set to 5 days, then the Planned invoice date on the agreement basis will become February 24 for the period 2022-03-01–2022-03-31.

#### Invoicing interval
Here you can choose the invoicing interval to use. The following options are available:
- Monthly
- Every other month
- Quarterly
- Every four months
- Every six months
- Annually
In the Order types procedure you can choose a default Invoicing interval for the agreement type. By clicking the Invoicing interval button in the Order types procedure you can also configure if accrual accounting should be applied for the order type's invoicing interval.

#### Price definition
Here you can define what type of price you enter on the agreement. For example, if you have negotiated a price for a year with the customer, but that it should be invoiced on a monthly basis. The default option here is No. This means it is the selected Invoicing interval that will decide the type of price on the agreement.
The following options are available:
-   
Day
-   
Week
-   
Month
-   
2 months
-   
Quarter
-   
4 months
-   
6 months
-   
Annual

#### Comprehensive invoice
Here you decide if comprehensive invoice should be used. The following options are available:
- No
- Per customer
In order for it to be possible to create a comprehensive invoice there is a number of criteria which has to be fulfilled. You can read more about this under the heading Comprehensive invoice in the [Invoicing](../../Customers/CustomerRegister/bInvoicing.htm) section of the Customer register procedure.

#### Create basis for
Here you decide for how many years ahead you want to create invoice bases. Please see [Valid to](bGeneral.htm#Giltig_till) for additional information about how a basis is created.

#### Invoice current month
The Invoice current month function is normally used when the beginning of the agreement is the same as the current month. The invoice date is the day before the agreement's start date. This field can only be edited when the invoicing method In advance has been selected. The setting called Invoice current month is not marked by default.
> If the current month should be invoiced, the entire month will be included. If only a part of the month should be invoiced, this must be manually managed on the invoice basis afterwards.

#### Release basis automatically
If you have activated the Create basis for release setting, you can choose if invoice basis should be created automatically. The release takes place during the night of the agreement basis' planned invoice date. If this setting is activated by default or not, is determined in Order types procedure.

#### Use accrual accounting
When the invoicing method is set to In advance you can mark the accrual accounting. In that case, it is mandatory to select an accrual account.

#### Accrual account
Select an accrual account if accrual accounting should be applied. You cannot save the agreement if no accrual account has been selected/entered and you have chosen to accrual account the invoice. If you have entered a standard account for accrual accounting in the Standard accounts procedure, this will be suggested.
> Remember to enter an accrual account for each respective customer group, and that all accrual accounts need to be linked to the same VAT row as the income account, in order to avoid differences in the VAT report.

#### Factoring
With this setting you select if this factoring should be used for this agreement. If factoring is activated for the customer in the Customer register, this checkbox will be activated by default on the agreement.
