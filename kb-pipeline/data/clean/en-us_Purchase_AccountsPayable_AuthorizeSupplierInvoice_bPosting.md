### Posting
In this box you see the posting of the invoice. It is possible to post and also authorize per row. Row authorization is not necessary in order for the invoice to become authorized on invoice level. Unlike the posting in the Register supplier invoice it is not possible to perform accrual accounting on posting rows. However, it is possible to authorize posting rows. A row that has already been authorized by a person is completely locked and cannot be changed or deleted. (There is a user rights setting with which you can decide that authorizations can be modified or deleted by another person).
Posting of dimensions can be performed automatically when they are linked to registers. This is determined by settings in the Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. procedure.
If the invoice is linked to purchase order, the postings from the purchase order are shown automatically. You are not allowed to edit the amount on these posting rows. This is instead done by changing the prices under the Order link tab.

#### Account
In this column you select an account number from the chart of accounts.

#### Dimension columns
The dimensions configured are shown in the columns for the posting rows, for example, cost center, cost unit, etc. Which dimensions that are open for posting is determined by the account settings for the respective dimension in the chart of accounts.

#### Specification
Here you can enter a specification for the posting.

#### Amount
Here you see/enter the amount to post. The posting is made in the company currency, unless the account is a currency account. In that case you post in the currency that is linked to the account.
The amount that you enter (positive or negative number) is automatically entered in the columns Debit or Credit (always in the company currency). That is, if you enter a positive amount, the amount will be put in the Debit column, if you enter a negative amount it will be filled in in the Credit column.
The field is locked for posting rows that have been created based on link to purchase order. Adjustment is instead made under the Order Link tab.

#### Debit
The amount that should be recorded on the debit side, it is always recorded in the company currency. The column is filled in automatically if you have entered a positive amount in the Amount column. The debit amount can also be negative (this is used to undo a debit posting).

#### Credit
The amount that should be booked on the credit side, it is always recorded in the company currency. The column is filled in automatically if you have entered a negative amount in the Amount column. The credit amount can also be negative (this is used to undo a credit posting).

#### Authorize row (A)
In this column you decide which posting row you want to authorize. When you activate the check box, your user name is shown in the Authorized by field. It is not possible to authorize a row if it already has been authorized by somebody else.

#### Authorized by
Here you see the person who performed the authorization of the row. If someone has already authorized the row, you will see that person’s user name. It is not possible to edit this row. If you check the Authorize row box (A), you will here see the user name of the user as which you are currently logged on.

#### Signer code
If authorization at row level is applied (activated with the system setting called Use extended authorization on posting rows). When authorizing the invoice the system will only show the posting rows you need to authorize. However, you can use a button on the function menu to show the other posting rows. When applying amount limit, the total of the rows you authorize will be checked, not the total net amount of the invoice.
Order invoices are assigned a signer on row level based on a different set of rules. Primarily, the person entered as authorized signer for the supplier will be used, and secondarily, the person selected as reference on the purchase order will be used. However, regarding overstepping of amount limits the same rules are applied as for expense invoices. That is, according to responsible on account, cost center, etc.

#### Authorization log (A. log)
Here you find a log of the ones who have already authorized the row.
More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Quantity
The quantity that should be recorded.

#### VAT Code
In this field you see the VAT code for the posting row in question. A VAT code on posting row is only of significance if you have selected the option VAT code in general ledger transactions for the system setting Basis for VAT report is loaded from.

#### Automatic posting active
Here you can see a marked checkbox if the account has automatic posting or automatic allocation. It is possible to uncheck the box if you should not use automatic posting/automatic allocation for this posting row.

#### C/I type
Here you see which cost/income type the posting will be registered on in the project accounting.
