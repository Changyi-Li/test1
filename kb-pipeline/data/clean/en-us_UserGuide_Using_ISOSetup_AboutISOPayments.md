### What to bear in mind when using ISO outgoing payments
Other information which may be relevant for supplier payments via ISO is provided here.

#### Credit invoices and negative amounts in the payment file.
The following applies for outgoing payment via file for ISO. If you use ISO payments, you cannot send a file with a negative amount to the bank. That is, the amount of the debit invoices must exceed the amount of the credit invoices. Furthermore, you can for most banks only have a group of 4 invoices per supplier and payment date, if a credit invoice is included in the payment file. That is, you can, for example, have 3 debit invoices and 1 credit invoice per date and supplier, or 2 debit invoices and 2 credit invoices, and so on. If you have included a credit invoice in the file, you will not be able to create the file when there are more than 4 invoices on the same date. For example, if you have 1 credit invoice and 7 debit invoices for the same date to the same supplier, it will not work.
To make it easier, there is a built-in functionality in the Outgoing payments procedure for the list type called Payment suggestion. The functionality detects whether the invoices have the ISO payment method, and if so, the payment date is adjusted automatically for credit invoices. The payment date is adjusted in such a way that the credit amount will be covered by the debit amount as much as possible.
The functionality is based on the below circumstances:
-   
The credit invoice and the debit invoice have the same payment method (ISO).
-   
The credit invoice and the debit invoice are registered on the same supplier.
-   
The credit invoice and the debit invoice are issued in the same currency.
> Please note! You need to ensure that the number of invoices per supplier and payment date does not exceed 4.

#### Merge payments for unstructured payments in ISO XML 20022
When you generate payment files in the ISO XML format with unstructured references, multiple payments to the same supplier, in the same currency, and with the same payment date, can be merged into a single transaction.
The number of invoices that can be included in a merged payment depends on which bank you use:
-   
Banks supporting up to 140 characters for the payment reference – Merge payment is based on the available reference length, which allows more invoices to be included in the same payment.
-   
Banks not supporting 140 characters – A limitation applies, allowing a maximum of 4 payments per merged payment.
Banks not supporting 140 characters (a maximum of 4 payments):
- Sweden: Nordea, Danske Bank, BNP Paribas Bank
- Norway: Danske Bank
- Denmark: All banks except Nordea
- Finland: Nordea
- Poland: Bank Pekao, PKO BP, BOŚ Bank, BNP Paribas Bank, SEB
- United Kingdom: SEB, Lloyds Bank
- Estonia: ISO Estonia
- Germany: ISO Germany
> In the transaction list you can see how many invoices are merged for payment by checking the number of invoices per sub-total.
