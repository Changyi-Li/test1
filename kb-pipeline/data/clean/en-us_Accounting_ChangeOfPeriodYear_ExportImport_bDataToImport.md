### Import

#### Opening balances
With this checkbox you decide if opening balances in the import file should be imported. This box is checked by default.

#### Vouchers
With this checkbox you decide if vouchers in the import file should be imported. This box is checked by default. If the voucher is incorrect, a warning is displayed and the voucher will be set to Preliminary.

#### Previous year
With this checkbox you decide if data referring to the previous year in the import file should be imported. By default, this setting is not activated.

#### Budget
With this checkbox you decide if budget data in the import file should be imported to the selected budget number. This box is checked by default.
Existing data in the selected budget number is overwritten in the import. If you want to import to a new budget number you first have to register that number in the procedure called Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Budget.

#### Automatic posting of VAT
With this setting you decide if posting of VAT should be generated in connection with the creation of vouchers via this procedure (when you save the import and the voucher is created). This can be useful if the file contains posting concerning sales or purchase which is liable to VAT and you want the system to post the VAT for these transactions. To be able to automatically post the VAT, the amounts in the file must be posted including VAT (gross). The system will in that case re-post these transactions, they will then be posted with the net amount on the intended account and the VAT is posted on the VAT account. VAT posting is generated from the VAT code entered on the sales/purchase account in the Chart of accounts procedure.
