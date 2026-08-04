### Reconciliation via file
This tab is used to import bank statements ISO XML file format.
The bank statement contains the company's:
- Balance brought forward in the bank account.
- Transactions made during the period in question.
- Closing balance in the bank account.
And:
- Number of the bank statement.
- Bank account number
- Company name
- Period
A closing balance which differs compared to the balance on the bank account in the accounting might depend on different things, for example:
- The bank has charged fees or deposited interest on the bank account.
- Payments have been incorrectly recorded in the accounting.
- Invoices in the accounts payable and accounts receivable are not recorded as paid (confirmed).

#### Matching rules
When the system automatically matches the records in the bank statement to the general ledger the following will be checked:
- That the amount in the bank statement corresponds to the amount in the general ledger.
- That the reference information in the bank statement corresponds to the invoice number/reference number in the accounts payable/accounts receivable.

#### Reconciliation
All transactions in the general ledger which correspond to the bank statement will automatically be marked as "reconciled" and are handled as reconciled with the bank account. Transactions which cannot be matched must be manually handled by the user. You can either match them manually by dragging and dropping a row from the top box to a row in the bottom box, or you can add the missing transactions. There is also support to match one or multiple rows in the bank statement to one or multiple entries in the general ledger. This is done via a function button on the menu. For other payment records (which are not linked to invoices), these can be recorded automatically via "Bank transaction rules” that you configure in the Bank settings procedure. You can configure it to match on reference or on bank transaction code. Matching will primarily be made on reference, and secondly it will match on the bank transaction code.
In order to facilitate reconciliation when the bank statement is specified per invoice it may be necessary to transfer the incoming and outgoing payment journals to the general ledger "row by row" with details for each invoice. You activate this by marking the Detailed posting setting for the incoming and outgoing payment journals in the Voucher number series/Journals procedure.
For bank account reconciliation there is a separate journal type in the Voucher number series/Journals procedure.

#### Import of bank statement
The default path for the import file is configured in the Settings for export/import procedure, under the Import tab, the import type Bank account reconciliation.
