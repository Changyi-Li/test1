### Posting
In this box you see posting rows in an existing recorded voucher and add and edit posting rows in a new or preliminary voucher, unless the account on a row is blocked for manual postings.
Apply accrual accounting
When you have selected an account, the chart of accounts settings for the voucher date's accounting year will be applied. Automatic posting/allocation become generated when you post on an account where this is registered. If the account has the setting Accrual account activated in the Chart of accounts procedure, this will also be taken into consideration. Then the accrual accounting function will automatically be activated when you leave the amount field, otherwise you can manually activate the accrual accounting function using the function button Apply accrual accounting ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_period.png). If the account row in an existing voucher contains an accrual account then you can link to the procedure Register accruals to see the accrual of the posting row.
Register/complement fixed assets object
If you have not activated the setting Fixed assets account in the Chart of accounts procedure, but still wish to register fixed assets on the row in question, then you can mark the specific row and click the button Register/complement fixed assets object ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_fixed_assets_object.png). If you on the other hand have activated the setting mentioned above, the system will know this.

#### Account
In this column you see the account number from the chart of accounts. In a new or a preliminary voucher it is possible to select account number.

#### Dimension columns
The dimensions configured are shown in the columns for the posting rows, for example, cost center, cost unit, etc. Which dimensions that are open for posting is determined by the account settings for the respective dimension in the chart of accounts.

#### Specification
Here you see a specification, if any, of the posting. In a new or a preliminary voucher it is possible to enter a specification for the posting, but only if Specification has been activated for the account in question in the chart of accounts.

#### Amount
Here you see/enter the amount to post. The posting is made in the company currency, unless the account is a currency account. In that case you post in the currency that is linked to the account.
The amount that you enter (positive or negative number) is automatically entered in the columns Debit or Credit (always in the company currency). That is, if you enter a positive amount, the amount will be put in the Debit column, if you enter a negative amount it will be filled in in the Credit column.
When you have entered an amount and you leave the field, you will automatically be placed on a new posting row. On the new row a balancing of the voucher is automatically suggested (difference between debit/credit) when you have selected an account, but of course it is possible to change the amount.
An alternative is to leave the Amount empty and instead you enter the amounts in the debit and credit columns.

#### Debit
Amounts that should be recorded on the debit side, it is always recorded in the company currency. The column is filled in automatically if you have entered a positive amount in the Amount column. The debit amount can also be negative (this is used to undo a debit posting).
If the account is configured as a credit account, the cursor will skip the debit column and become placed in the credit column.

#### Credit
Amounts that should be recorded on the credit side, it is always recorded in the company currency. The column is filled in automatically if you have entered a negative amount in the Amount column. The credit amount can also be negative (this is used to undo a credit posting).

#### Balance
Here you see the accumulated balance.

#### Comment (posting)
Here you can add a comment for the posting row. You are able to add a comment regardless of whether the voucher belongs to a closed or locked period. The comment will also be visible in the following procedures: Balance information, Voucher list, and General ledger.

#### Comment (account)
Under this button you see the comment, if any, entered on the account in the chart of accounts.
More info
Under this button you can generally find additional columns.

#### VAT code
In this field you see the VAT code for the posting row in question. A VAT code on posting row is only of significance if you have selected the option VAT code in general ledger transactions for the system setting Basis for VAT report is loaded from.
It is possible to adjust the VAT code for recorded vouchers. This is possible to do if:
- The accounting period is open for accounting.
- The VAT report loads data for the report based on VAT code on general ledger transactions. This is determined via the system setting called Basis for VAT report is loaded from which should be set to VAT code in general ledger transactions.

#### Debit (currency)
Here you can see the debit amount in the currency of the account.

#### Credit (currency)
Here you can see the credit amount in the currency of the account.

#### Balance (currency)
Here you can see the balance in the currency of the account.

#### New balance
Here you see the balance of the account when the posting row in question has been taken into consideration, that is, what the account balance will be after you have saved the voucher. If the voucher you have open is an existing voucher (already saved), you will see the current balance of the account.

#### New balance (currency)
The same function as above but shown in the currency of the account.

#### Exchange rate
In this column you see the exchange rate for the posting row in question. If the posting is made using another currency than the company currency, then the suggested exchange rate will be loaded via the voucher date (the rate that applied to the currency in question on that specific date). However, this can be changed. The rate type used is the one selected with the system setting Default rate type in the system settings. To be able to post only in the company currency on a currency account (e.g. when revaluating currency accounts) you enter "0,00" in the currency account.

#### Quantity
Here you see the recorded quantity. The recorded quantity is shown as a total at the bottom of the Posting box.

#### Accrual accounting
If accrual accounting is activated for the posting row you will here see the accrual number.

#### Automatic posting active
Here you can see a marked checkbox if the account has automatic posting or automatic allocation. It is possible to uncheck the box if you will not use automatic posting/automatic allocation for this posting row.

#### C/I type
Here you see which cost/income type the posting will be registered as in the project accounting.

#### Order number
If the account has the setting Order number activated in the Chart of accounts procedure, the order number will be shown.

#### CO2e
If you have linked an emission type to the account in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Sustainability procedure, the value is automatically entered based on the amount recorded. The value is calculated as Amount x Emission factor. You can also enter a value manually if you have received the information from another source. A manually entered value is shown in italics.

#### Emission type
Here you are able to select an emission type if you want to manually enter a value. If you have linked an emission type to the account in the Basic data – Sustainability procedure, the emission type will be entered automatically.
