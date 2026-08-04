### VAT

#### VAT type
You can select a VAT type for an account, if needed. By default, no VAT type is registered for a new account. VAT type should be entered if transactions on the account should affect the VAT report.
The VAT type control:
- In combination with the VAT code, the VAT type determines which VAT row the sale, purchase, and VAT should be recorded with in the VAT declaration.
Explanation of the different alternatives:
- None (default) – Select this option if transactions on the account should not affect the VAT report, for example cash and bank.
- Sales account – Select this option if transactions on the account should affect the revenue/sales in the VAT report, for example domestic sales subject to VAT.
- Purchase account – Select this option if transactions on the account should affect the acquisitions/purchases in the VAT report, for example purchases from EU country.
- Input VAT account – Select this option if the concerned account is a VAT account for input VAT.
- Output VAT account – Select this option if the concerned account is a VAT account for output VAT.

#### VAT code
Here you see/select a default VAT code. VAT codes must first be registered and activated in the VAT settings procedure.
VAT code is deactivated of the VAT type is set to None. The field is activated if the VAT type is set to Sales account, Purchase account, Input VAT account, or Output VAT account. You can the select a VAT code. The VAT code on the account has several functions:
- It determines which VAT code should be used for manual posting rows for example in the Register vouchers procedure. This is significant if the VAT report has been set to read VAT code on transaction level.
- It determines on which row in the VAT report the recording should be made. This applies if the VAT report uses VAT code in the chart of accounts to decide where in the VAT report the value should be recorded in the VAT report. It is decided with the system setting Basis for VAT report is loaded from. For companies wishing to load bases for the VAT report from the transaction's VAT code, it is the VAT code for the transaction and not the account which determines on which row the sales/purchase should be recorded. In that case the VAT code in the chart of accounts is only significant for which default VAT code should be used when manually postings are made on the account in the Register vouchers procedure.
Please read the online help function for the VAT settings procedure to see schematic illustrations of how the VAT accounting works depending on how the system setting Basis for VAT report is loaded from has been configured.

#### Override VAT code (Register supplier invoice)
This setting is available if you have selected the option VAT code in general ledger transactions in the system setting Basis for VAT report is loaded from. If the VAT type above is set to Purchase account, the setting is activated. If you activate the setting, the account's VAT code will be suggested instead of the invoice's VAT code when posting purchase on supplier invoices. This can be useful if there are accounts in the chart of accounts that always should be posted on a specific VAT code.
Please read the online help function for the VAT settings procedure to see schematic illustrations of how the VAT accounting works depending on how the system setting Basis for VAT report is loaded from has been configured.

#### VAT row
VAT row is deactivated of the VAT type is set to None.
If the VAT type has been set to Sales account or Purchase account, Input VAT account, Output VAT account, you will in this field see information about which VAT row the selected VAT code will be recorded on in the VAT declaration. The link between VAT code and VAT row is defined in the procedure VAT settings.
