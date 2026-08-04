### Interest invoice

#### Charge penalty interest, default customer setting
This system setting determines if and how penalty interest should be charged to new customers. The available options are: Interest invoice, Next regular invoice, and No charge.

#### Penalty interest, general interest rate
Here you enter the general interest rate that should apply to the penalty interest. For new ledger records, the information is primarily loaded from the customer and secondarily from this system setting. The interest rate is locked for existing ledger records.

#### Minimum amount of interest charge
Here you enter the lowest total interest amount required in order for a customer’s record to appear in the list in the Interest charge basis procedure. The total interest amount is calculated for all invoices that are paid too late by the customer.

#### Minimum amount of interest charge per invoice
Here you enter the lowest interest amount per invoice required to charge interest.

#### Days of grace for interest
Here you enter the number of extra days that should apply as days of grace for interest. If for example the days of grace is set to 3 days, it means that the customer has three extra days after the due date to pay the invoice without being charged interest.

#### Interest-free days
Here you enter the number of interest-free days that should apply. The days are calculated from the invoice date and ahead in time.
- If the invoice has a payment term with fewer days than the interest-free days, then interest will not be charged until the number of interest-free days have passed.
- If the invoice has a payment term with more days than the interest-free days, then interest will be charged as of the due date.
Example:
| Payment term | Interest-free days | Interest will be charged |
|---|---|---|
| 10 days | 30 days | 20 days after the invoice's due date |
| 60 days | 30 days | As of the invoice's due date |

#### Amount of payment reminder fee
Here you enter the amount of the general payment reminder fee to all customers. Reminder fee is charged on interest invoices to the customer. The reminder fee will be added as a mark-up to the total on the interest invoice.

#### Payment terms on interest invoices
This system setting determines the payment term on interest invoices, that it, the interest invoices' credit time.

#### Days per year that the interest is based on
Here you enter the days per year on which the interest is based. The default option here is 360 days.

#### Service part for interest invoices
This system setting determines which service part should be used on the invoice row when charging interest. The part must be created using the type Service in the Part register procedure.
Please make sure that the service's product group is exempt from VAT in the VAT settings procedure. The account for penalty interest is selected for the product group in the Posting matrix procedure.
