### Settings – Bank integration
These settings become available if you have activated the Bank integration option.
Bank information

#### Bank
Here you select the bank that the payment method will be applied to.
Type of bank integration for outgoing payments

#### Type of bank integration
Here you can decide which type of bank integration the payment method should use, Open Banking or File pay (ISO).

#### Internet bank website
Here you enter the website to the Internet bank to which the payment is made. When the payments have been exported, the Internet bank's website will open automatically in your browser. This can only be entered with File pay (ISO)
Transaction list

#### Document
Here you select which transaction list should apply to the outgoing payment.
Check the recipient of payment

#### Check if bank account is missing
Here you determine if a check should be made to see if bank account is missing. Then you can choose if the system should warn or block if bank account is missing.
For electronic payment methods, a warning or block can be shown if bank account information is missing for the invoice. This is configured for each respective payment method in the Bank settings procedure.
Confirmation of payment

#### Matching rule
Here you can decide how the system automatically matches records with the ledger. You can choose between the following options: Invoice number + amount, Invoice number, Reference no./Invoice no. + Amount, or Reference no./Invoice no..

#### Maximum diff. allowed
This determines how much the amount in the payment record and the amount in the ledger can differ when being automatically matched.

#### Automatic confirmation of payments
This setting means that the system automatically matches and records payments. This occurs every night when bank statements are loaded from the bank.
> We recommend that you do not have the setting Automatic confirmation of payment activated the first time using Bank integration.

#### Link to bank account/bookkeeping account
Here you link currencies to bank accounts. If the company has different currency accounts at the bank, you can determine which account should be charged depending on the currency on the supplier invoice. The link is also used when posting outgoing payments in connection with the confirmation to make sure that the correct bookkeeping account is used depending on the currency in which the payment was made.
> Only bank accounts in the local currency can be linked to the payment method with the Open Banking integration (Except for Sparebank1 in Norway).
