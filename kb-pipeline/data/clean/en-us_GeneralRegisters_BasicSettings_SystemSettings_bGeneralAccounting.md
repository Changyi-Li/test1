### General (Accounting)

#### Today's date as default voucher date
This system setting determines if today's date always should be set as default voucher date on new vouchers. Otherwise, the default voucher date will set to the same date as on the latest voucher (with the highest number) in the series you book the voucher.

#### Basis for VAT report is loaded from
This system setting determines where the basis for the VAT report's sales and purchase should be loaded from.
VAT codes on posting rows are only of significance if this system setting has been set to VAT code in general ledger transactions. The system's VAT report will then load the basis for the VAT report from each accounting transaction, via the VAT code saved there.
Via the setting VAT code in general ledger transactions, you can also override the VAT code that is used when registering supplier invoices. In the Chart of accounts procedure, you can select Override VAT code (Register supplier invoice) for an account's VAT code for VAT type Purchase account. Then the account's VAT code will be suggested instead of the invoice's VAT code when posting purchase on supplier invoices. This can be useful if there are accounts in the chart of accounts that always should be posted on a specific VAT code.
If you have configured the setting VAT code in chart of accounts, the VAT report is determined by the chart of account's VAT code. That is, the accounts that are linked to the current VAT code.
Please read the online help function for the VAT settings procedure to see schematic illustrations of how the VAT accounting works depending on how the system setting is configured.

#### VAT accounting period
This system setting determines if the VAT accounting period should be per month, every other month, or per quarter.

#### EC sales accounting period
This system setting determines if the accounting period for EC sales should be per month, every other month, or per quarter.

#### Release the accruals on the last day of the period
This system setting determines if the accruals should be released on the last day of the period. Otherwise, they will be released the same day in the period as the start date.

#### Register incoming and outgoing payments in the same procedure/journal
With this setting you decide if incoming and outgoing payments should be registered in the same procedure, in Manage bank transactions in the Accounting module. You have to restart in order for these procedures to be shown. You must register a voucher number series for payment journal and enter the next journal number. This is done in the Voucher number series/Journals procedure. If you use batch number for payments, you must enter a start number for batch number under the Accounting tab in the Number series procedure.

#### Use cash book functionality
With this setting you decide if the cash book functionality should be used in the system. This function is mainly intended for countries in Eastern Europe where there are certain rules regarding the handling of liquid funds and cash in the accounting. In the cash book you register cash withdrawals and deposits. These could include transactions relating to customers, suppliers, employees or banks, etc. The setting activates the Cash reports tab in the Manage bank transactions procedure and you can print a Cash receipt for each transaction registered in the cash book. Please note! You have to create a payment method for the cash book in the Bank settings procedure.
The function can only be activated if the system setting Register incoming and outgoing payments in the same procedure/journal is activated.

#### Post canceled/reversed records with negative amounts in debit and credit (red storno)
This system setting determines how cancellations/reversals should be recorded.
- No – (Default) Means that cancellations/reversals are posted as positive amounts on the side opposite of the initial posting. (The method is also called Black storno.)
- Yes – Means that cancellations/reversals are posted as negative amounts on the same side as the initial posting. (The method is also called Red storno.) Please note! It is also possible to manually book using negative numbers.

#### Check open accounting period during order reporting
With this setting you decide if and how a check should be made to see that the accounting period in question is open when different stock transactions take place. This check concerns stock accounting and management accounting. If there is a voucher number series for stock transaction log and/or manufacturing order log, a check is also made to see that these voucher series are not locked for the accounting period in question. The check is made of the actual date when reporting/undoing arrival reporting of purchase order, reporting/undoing delivery reporting of customer order, reporting/undoing reporting of operation (which results in transfer to stock) in manufacturing orders, stock count, direct stock reporting, and authorizing/adjusting recording items. The available options are:
- No – (Default) No check is made during order reporting.
- Warn – A check is made to make sure the period in question is open and that the voucher series are not locked, otherwise a warning will be displayed during the order reporting.
- Block – A check is made to make sure the period in question is open and that voucher series are not locked, otherwise the order reporting will be blocked.
> This check is not made when reporting in the Recording terminal. These reports are always updated with today’s date, regardless of this system setting.

#### Automatic posting of VAT on voucher registration
This system setting decides if posting of VAT should take place when you record vouchers concerning purchases and sales liable to VAT. The default value in the Register vouchers and Voucher import procedures is determined by this system setting. The following options are available:
- No – No automatic posting of VAT takes place.
- Yes, post net amount – The system will automatically enter the VAT amount on a separate posting row.
- Yes, post gross amount – The system will re-allocate the posted amount so that the net amount is retained on the posting row, and the VAT amount is posted on a separate row.

#### Automatic posting of VAT on other payments
With this setting you decide if automatic posting of VAT should be done by default when you register other payments under the Register manually tab, or when a transaction is posted as an other payment (without matching with an invoice) under the Manage transactions via file or Manage transactions via bank integration tab, in the Manage bank transactions procedure. Please note! The VAT posting will currently only take place in cases where posting takes place on one offset account for the bank account.
The following options are available:
- No – No automatic posting of VAT takes place.
- Yes, post gross amount – The system will re-allocate the posted amount so that the net amount is retained on the posting row, and the VAT amount is posted on a separate row.

#### Block from making changes in voucher rows
Here you decide if it should be possible to make changes to voucher rows in already recorded vouchers.
-   
No – (default) The system will not block users from making changes to voucher rows.
-   
Yes – The system will block users from making changes in voucher rows, it means you can only make changes in preliminary vouchers.

#### Parent company's corporate ID in bank integration
This setting determines whether the parent company’s corporate ID should be used when activated bank integration. This applies to group structure for the banks SEB and Handelsbanken.
The system setting activates the Parent comp.'s corp. ID no. field under the Bank integration tab in the Bank settings procedure.

#### Zero balancing cash pool
Applies if you have activates the Bank integration option. With this setting you determine if “zero balancing” should be taken into consideration in connection to confirmation and reconciliation of payments. Zero balancing is a cash pool service with the bank which means all balances from the bank account are moved to a central master account, so the individual accounts will have a zero balance. If you activate the system setting, all balancing transactions will be ignored and will not be imported when confirming/reconciling.
