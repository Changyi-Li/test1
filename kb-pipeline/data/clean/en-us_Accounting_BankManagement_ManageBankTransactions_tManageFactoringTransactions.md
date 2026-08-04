### Manage factoring transactions
If you have activated the Monitor Factoring option, you use this tab to manage your factoring transactions.
By clicking the Load transactions button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png), the transactions are imported to the procedure according to the settings configures and the selected period. The transaction that are being imported have automatically been loaded by Monitor ERP from Fedelta via a scheduler which is run every 4 hours.
> If you want to load the latest transactions straight away (without awaiting the scheduler), it is possible to load them manually via the button called Trigger manual loading from Fedelta ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_download.png) found on the function menu.

#### Transactions to handle
Here you see all transactions loaded from Fedelta according to the settings that you have configured.
Records concerning invoice purchase are matched automatically to the accounts receivable. Other transaction types are handled and posted automatically with the use of standard accounts. In connection to invoice purchases, a fee charged by Fedelta will also be posted. Since this fee is liable to VAT, input VAT will automatically be posted for this cost.
The following transaction types are handled:
-   
Invoice purchase (matched and recorded as paid in the accounts receivable)
-   
Recourse – Customer did not pay the invoice and the invoice is sold back (only a recording entry, registered as an other payment)
-   
Payment recourse – Customer did not pay the invoice and the invoice is sold back (only a recording entry, registered as an other payment)
-   
Invoice purchase (matched and automatically recorded as paid in the accounts receivable)
-   
Invoice is written off – It is confirmed that the customer will not pay (only a recording entry, registered as an other payment)
> The invoice purchases are normally imported from Fedelta the same day as you do the invoicing.
By using the checkbox in the Exclude column, you can except a record from being recorded. This can be useful if you e.g. intend to record the payment manually (not using this procedure), or if the payment has already been recorded.
When you save in the procedure, all records that are green will be confirmed and recorded. The saved records are recorded via the regular payment journal for the voucher number series which you have entered in the Settings box. Any remaining records will stay there until the next time you load data to the procedure.
> It is good to have Specification entered for you clearing account in the chart of accounts in order for the system to specify in the general ledger which invoice each of the transactions refer to.
