### VAT codes
Under this tab you add or modify VAT codes. The VAT code table may differ depending on in which country the system is run. VAT codes are for example used in the following places in the system:
- On invoices/order rows to determines the row's VAT rate, VAT posting, and VAT information text (the latter alternative is only available during sales).
- On accounts in the chart of accounts to determine how sales/purchase against the current account should be presented in the VAT report. The VAT code on the account also determines which VAT code should be used by default on manual posting rows entered in the accounting. The latter only applies if the system setting below has been activated.
-    
This is entered on posting rows on vouchers, posting rows on supplier invoices, posting rows on customer invoices, etc.
> Please note! VAT codes on posting rows are only of significance if you have selected the option VAT code in general ledger transactions for the system setting Basis for VAT report is loaded from. The system's VAT report will then load the basis for the VAT report from each accounting transaction, via the VAT code saved there. Otherwise, only the VAT code in the chart of accounts will affect the VAT report, that is, the balance on the accounts linked to the current VAT code.

#### VAT
Here you enter the VAT rate for the VAT code. The default value is 0.00%. If the VAT code refers to Reversed liability for payment, the VAT rate should always be 0.00%.

#### Reversed liability for payment
Check the box if reversed liability for payment should apply. If the VAT code should be used during purchase (for example purchase from EU country), the estimated input VAT and output VAT will be posted automatically.
If the setting is activated for a VAT code of the Sales type, no accounts for output and input VAT are entered. Links to the VAT rapport can only be made via the VAT report link – VAT row (sales) column.

#### Reversed liability for payment %
This can be entered if reversed liability has been activated on the VAT code. In this field you enter the VAT percent used to post estimated input and output VAT. This VAT posting takes place in connection with the supplier invoice registration.

#### WHT
With this setting you decide if withholding tax (WHT) should be applied. This column is only available if you have activated the system setting called Use/apply withholding tax.

#### WHT %
This can be entered if WHT has been activated on the VAT code. In this field you enter the percent used for posting of calculated input WHT. This posting takes place in connection with the supplier invoice registration.

#### Input WHT
Here you enter which account should be used for posting WHT. You can enter a dimension for the account if the account has been configured to manage this. Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. are entered using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to the right of the field.

#### Output VAT
Here you select the account that should apply to the output VAT posted on outgoing invoices containing VAT. If you have checked the box Reversed liability for payment, you enter the account used for output VAT during reversed liability for payment. Please note that an account cannot be entered if Reversed liability for payment is activated for a VAT code of the Sales type. You are able to enter a dimension for the VAT account if the account has been configured to manage this. Dimensions are entered using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to the right of the field.

#### Input VAT
Here you select the account that should apply to the input VAT that is posted on incoming invoices containing VAT. If you have checked the box Reversed liability for payment, you enter the account used for input VAT during reversed liability for payment. Please note that an account cannot be entered if Reversed liability for payment is activated for a VAT code of the Sales type. You are able to enter a dimension for the VAT account if the account has been configured to manage this. Dimensions are entered using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to the right of the field.

#### Deductible %
For VAT codes where a part of the VAT is deductible, you can here enter the percentage that should be deductible. The purpose of this is to automate part of the supplier invoice registration in cases where the invoice contains records where the VAT is not deductible in full. For the VAT code you enter how great a share (in %) that is deductible, as well as the account to use for the non-deductible VAT. When you register the supplier invoice only the deductible VAT amount will be posted on the account for input VAT. The remaining share of the VAT will either be posted manually, or automatically on the account entered as account for non-deductible input VAT.

#### Input VAT – Non-deductible
Here you enter the account to use for the non-deductible VAT.

#### VAT information – Invoice
Here you enter VAT information for VAT codes with a VAT rate set to 0%. On the customer invoice you will see the VAT information as an information text explaining why the invoice is exempt from VAT.
> For VAT codes of the Sales type that have Reversed liability for payment activated, more details are shown on the invoice document such as VAT amount, VAT rate, and total value including VAT. This extra information can be found on the left-hand side of the VAT information text. Please note that it is still the ordinary invoice totals to the right of the document that apply when paying the invoice.

#### VAT report link – VAT row (purchase)
The VAT report in the accounting identifies the VAT codes in order to decide where in the report it should be shown. If the current VAT code is used during purchase where the VAT basis for the acquisition should be reported in the VAT report, you enter on which VAT row in the report it should be reported. The VAT rows are defined in the Create VAT report procedure.

#### Purchase links
Purchase links is an extended setting to the column VAT report link – VAT row (purchase). Here you enter how the purchase/sales should be reported in the country's VAT report. There is support to handle multiple parallel VAT reports in the system (one VAT report per country). Under the button, you enter on which row in the VAT report the purchase should be shown. This is done for each respective country's VAT report. Normally, you only enter the VAT row for the VAT report that is set as default in the Create VAT report procedure

#### VAT row – Input VAT
The VAT report in the accounting identifies the VAT codes in order to decide where in the report it should be shown. If the current VAT code is used during purchase where the input VAT should be reported in the VAT report, you enter on which VAT row in the report it should be shown. The VAT rows are defined in the Create VAT report procedure.

#### Links – Input VAT
Links – Input VAT is an extended setting to the column VAT row – Input VAT. Here you enter how the input VAT should be reported in each respective country's VAT report. There is support to handle multiple parallel VAT reports in the system (one VAT report per country). Under the button, you enter on which row in the VAT report the VAT should be shown. This is done for each respective country's VAT report. Normally, you only enter the VAT row for the VAT report that is set as default in the Create VAT report procedure

#### VAT report link – VAT row (sales)
The VAT report in the accounting identifies the VAT codes in order to decide where in the report it should be shown. If the current VAT code is used during sales where the VAT basis for the sales should be reported in the VAT report, you can in this column enter on which VAT row in the report the values should be shown. The VAT rows are defined in the Create VAT report procedure.
One and the same VAT code can be used during both purchase and sales. This means that the code can be linked to both sales and acquisition in the VAT declaration. For example, a VAT code referring to EU trading is reported both as sales to EU country and purchase from EU country depending on if the account on which it is recorded has VAT type Purchase account or Sales account.

#### Sales links
Sales links is an extended setting to the column VAT report link – VAT row (sales). Here you enter how the sales/purchase should be reported in the VAT report of each country concerned. There is support to handle multiple parallel VAT reports in the system (one VAT report per country). Under the button, you enter on which row in the VAT report the purchase should be shown. This is done for each respective country's VAT report. Normally, you only enter the VAT row for the VAT report that is set as default in the Create VAT report procedure

#### VAT row – Output VAT
The VAT report in the accounting identifies the VAT codes in order to decide where in the report it should be shown. If the current VAT code is used during sales where the output VAT should be reported in the VAT report, you enter on which VAT row in the report it should be shown. The VAT rows are defined in the Create VAT report procedure.

#### Links – Output VAT
Links – Output VAT is an extended setting to the column VAT row – Output VAT. Here you enter how the output VAT should be reported in each respective country's VAT report. There is support to handle multiple parallel VAT reports in the system (one VAT report per country). Under the button, you enter on which row in the VAT report the VAT should be shown. This is done for each respective country's VAT report. Normally, you only enter the VAT row for the VAT report that is set as default in the Create VAT report procedure

#### EC sales list (only applies to EU countries)
Here you create a link to the EC sales list. The report for the EC sales list (EU sales) identifies VAT codes on accounts or transactions (depending on the system setting mentioned above) to determine if the sales refers to EU trading. This is entered in this column. You also enter how the values should be reported, as Trade is goods, Services, or Three-party trading.

#### ISO code
This is configured automatically, but it can be changed if needed. ISO codes are used for E-invoices.

#### Log
Next to VAT codes that have been modified you see this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). When clicking this button, you see who changed the VAT code, date and time of the change, and which changes have been made.

#### Active
Here you determine if the VAT code is active or not.
