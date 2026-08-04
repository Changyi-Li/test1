### Posting
In this box you can see the default posting for the row you have checked in the box Set-off against.
Method of posting
On all occasions, a posting record will be created per payment record. In the posting record the accounts receivable/accounts payable is always recorded on one side of the posting. On the other side of the posting, an interim account will be used. The purpose of this account is to temporarily balance the posting. This interim posting will be offset posted automatically for the posting record for the invoice you set-off against.
Example 1
Credit invoice 9001 is set-off against debit invoice 5001. The amount to set-off is SEK 1000.
The posting for credit invoice 9001 will be:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 1510 Accounts receivable | 9001 | 1000 |   |
| 9000 Interim account set-off |   |   | 1000 |
Posting for debit invoice 5001 will be:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 1510 Accounts receivable | 5001 |   | 1000 |
| 9000 Interim account set-off |   | 1000 |   |
The total posting that will be recorded is:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 1510 Accounts receivable | 9001 | 1000 |   |
| 1510 Accounts receivable | 9001 |   | 1000 |
Example 2
The debit invoice 5001 is set-off against consecutive number 110 in the accounts payable. The amount to set-off is SEK 1000.
The posting for customer invoice 5001 will be:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 1510 Accounts receivable | 5001 |   | 1000 |
| 9000 Interim account set-off |   | 1000 |   |
Posting for consecutive number 110 will be:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 2440 Accounts payable | 110 | 1000 |   |
| 9000 Interim account set-off |   |   | 1000 |
The total posting that will be recorded is:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 1510 Accounts receivable | 5001 |   | 1000 |
| 2440 Accounts payable | 110 | 1000 |   |
Example 3
Credit invoice 9001 is set-off against debit invoice 5001. The amount to set-off is USD 1000. Initial rate on the credit invoice 9001 is 8,00. Initial rate on the debit invoice 5001 is 9,00.
The posting for credit invoice 9001 will be:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 1510 Accounts receivable | 9001 | 8000 |   |
| 9000 Interim account set-off |   |   | 8000 |
Posting for debit invoice 5001 will be:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 1510 Accounts receivable | 5001 |   | 9000 |
| 9000 Interim account set-off |   | 8000 |   |
| 8180 Exchange losses |   | 1000 |   |
The total posting that will be recorded is:
| Account | Spec. | Debit | Credit |
|---|---|---|---|
| 1510 Accounts receivable | 9001 | 8000 |   |
| 1510 Accounts receivable | 5001 |   | 9000 |
| 8180 Exchange losses |   | 1000 |   |

#### Total accounting order
If the checkbox Total accounting order is checked you will see a total posting for all account payable and account receivable records in the window. If you perform a set-off between the accounts payable and the accounts receivable, then the total posting is divided and first shows posting of the invoice to set-off and then shows a total for the invoice against which the set-off should be made.

#### Posting for invoice to set-off
If this setting is activated, you will see the posting for the ledger record which is in the Invoice to set-off box.
