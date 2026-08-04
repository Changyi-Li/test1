### Settings

#### Ledger date
Enter the date for which you want to create the list. The invoice will not be included in the list if it – on the entered date – was paid in full or canceled.

#### Rate type
You register rate types in the Currencies procedure. The rate type you select here is used to convert records in foreign currency according to the now applying exchange rate for the selected rate type.

#### Include
This setting is used to decide if Debit invoices, Credit invoices, and Zero invoices, should be included in the revaluation.

#### Show invoices with zero in adjustment amount
With this setting you decide if you want to show invoices that have an adjustment amount of zero. For example, if the invoice is registered with the same exchange rate as the AFS rate.

#### Create voucher
Here you decide if a voucher should be created for the adjusted amount.

#### Voucher number series
Here you select the voucher number series to use for the voucher you create.

#### Voucher text
The default text is "Revaluate account to {0} {name of the selected rate type}". These texts are handled in the Voucher texts procedure.

#### Voucher date
Here you select a voucher date for the revaluation. This is by default the same as the ledger date. If you change the ledger date, this date will also be changed, but not the other way around. A validation takes place to make sure the period is open.

#### Account for revaluation
Here you decide on which account the revaluation/adjustment should be recorded. The following options are available:
-   
According to ledger account
-   
According to standard account

#### Create reversal voucher in accrual accounting
Here you decide if a reversal voucher should be created as an accrual. Most of the times it is a reversal in the next accounting period (can also be a future accounting year).

#### Date
Here you select the date for the reversal voucher. The default date here is the first of the month following the date you entered as voucher date.
