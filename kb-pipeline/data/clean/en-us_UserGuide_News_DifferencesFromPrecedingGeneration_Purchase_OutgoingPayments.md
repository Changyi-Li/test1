### Outgoing payments
- The procedure contains a collection of functions which in G4 were scattered over different procedures in G4 (Payments Out, Payment Suggestions, Confirmation, On Account Payments / Set-offs, Cancel Outgoing Payments).
- The payment methods are no longer hardcoded. They can now be registered and linked to different payment formats and bookkeeping accounts via the Bank settings procedure.
The following differences apply to the list type Payment suggestion and the tab Pay via bank (order):
- Better handling of cash discounts. Up to three levels of cash discounts. When selecting by due date, the system will take the cash discount date of the invoices into consideration. In the presentation Cash discount it is also possible to make partial payments.
- New column: Payment date. In G4 you changed the due date in order to decide the date when the invoice should be paid.
- Comment button in the list.
- More information about the recipient account and sender account is now shown. This information can be changed on invoice level.
- LB files now have support for account deposits (recipients without giro number).
- You can create payment file directly without having to print a transaction list.
- You can select where to place the payment file and what to call it (possible to create defaults).
- The file name for payment files can contain the number of the transaction list and date including time.
- In the Payment suggestion list type, the handling of credit invoices has been improved regarding electronic outgoing payments via ISO. When the list is loaded, the system analyzes the credit invoices and moves the payment dates of these to days where they will be covered by debit invoices (from the same supplier). This is done to make sure the payment in total will result in a positive amount per supplier and per payment date. If there are not enough debit invoices to in total exceed the amount of the credit invoice, the credit invoice will automatically be deactivated from payment in the list.
The following differences apply to list type Confirmation:
- There is a Selection tab for the confirmation which makes it possible to select by other selection terms than date, for example consecutive number and supplier.
- More information is shown about the payments, for example the supplier name.
- The coding/posting is not hidden under a button but is now shown at the bottom of the window. You can also see a total coding/posting for all payments.
- Account is selected based on the currency for which the confirmation is made.
- When confirming via file you will now see clearer information about warnings for records which cannot be imported, and they can be printed.
- When confirming via file the file which you have used for confirmation can automatically be moved to a filing folder.
The following differences concern the tab called Pay manually:
- BatchA batch is the set of components/products manufactured at the same time and made from the same original material. total can be entered in external currency.
- It is optional to enter the paid amount in the currency of the invoice or in the company currency.
- It is no longer allowed to pay the invoice prior to its voucher date.
- Coding/posting of payments are clearly shown in the interface (not hidden under a button).
- You can (with a system setting) decide which exchange rate should be suggested when using external currency: current rate, initial rate, or payment day's exchange rate.
- Difference code has been renamed, it is now called write-off code and it is a separate table which can be created in the Bank settings procedure.
- It is possible to register an on account payment by leaving the field Consecutive number empty.
-   
You can show the current balance and new balance for the account you post on.
