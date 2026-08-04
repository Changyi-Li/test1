### Incoming payments
- This G5 procedure contains a collection of functions which in G4 were scattered over different procedures (Payments In, Incoming Payment List, Payment Matching, On Account Payments / Set-offs, Cancel Incoming Payments).
- In G5 you can register the payment methods. This is done in the Bank settings procedure.
- BatchA batch is the set of components/products manufactured at the same time and made from the same original material. total can be entered in external currency.
- It is optional to enter paid amount in the currency of the invoice or in the company currency.
- It is no longer allowed to pay the invoice prior to its voucher date.
- Message if the customer is blocked.
- Coding/posting of payments are clearly shown in the interface (not hidden under a button).
- Posting when using currency account takes place against actual currency amount field to the general ledger instead of via quantity.
- You can (with a system setting) decide which exchange rate should be suggested when using external currency: current rate, initial rate, or payment day's exchange rate.
- Difference code has been renamed and is now called Write-off code. Such coded can be registered as you please in a table in the Bank settings procedure.
- It is possible to enter that interest should be charged on the next regular invoice.
- It is possible to register an on account payment by leaving the field Consecutive number empty.
-   
You can show the current balance and new balance for the account you post on.
The following news items concern the tab called Confirmation via file:
- A file you have confirmed can automatically be moved to a filing folder.
- It is possible to use filters to only see unmatched records from the file.
- It is possible to match multiple payment records in the file to one and the same accounts receivable record.
- When you manually match a greater amount in the file with a lower invoice amount in the accounts receivable, it is possible to select if it should be handled as a partial matching, be registered as on account payment, or if it should be written off.
-   
When reporting via file, merged incoming payments (multiple payments) are now automatically matched too.
The following news items concern the tab called Set-off:
- It is possible to set-off multiple invoices against each other at the same time by using a list where you mark the invoices to set-off.
- When setting off a customer invoice against a supplier invoice, separate journals are created for the incoming payment and the outgoing payment.
- When using set-offs a "transit account" is automatically used to offset the accounts receivable/accounts payable.
