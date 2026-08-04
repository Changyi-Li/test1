### Incoming payment

#### Default exchange rate for incoming payments
This system setting determines which exchange rate should be suggested during incoming payment if the invoice is issued in another currency than the company currency. The following options are available:
- Current exchange rate – The current exchange rate loaded from the Currencies procedure.
- Invoice’s exchange rate – The exchange rate used on the invoice when invoicing.
- Payment day's exchange rate – The exchange rate that applied to the currency in question on the payment day selected on the incoming payment. This information will be loaded from the exchange rate log.
For incoming payments of the Other payments type, the rate of the payment day will always be suggested.

#### Rate type
This setting is available if the Current exchange rate or Payment day's exchange rate option is selected in the system setting above. Here you can select if Current exchange rate, AFS rate, own defined rate type, or Use rate type from invoice (from customer/order type) should be used when receiving payments. (For the own defined rate type to appear in the list, you must first register such under the Rate types tab in the Currencies procedure.)

#### Default exchange rate for incoming payments (via file)
This applies when confirmation is made on currency accounts. When confirming incoming payments from file, you can with the help of this setting choose if the confirmation should take exchange rate profit/loss, if any, into consideration.
The following options are available:
- Current exchange rate – The current exchange rate loaded from the Currencies procedure.
- Invoice’s exchange rate – The exchange rate used on the invoice when invoicing.
- Payment day's exchange rate – The exchange rate that applied to the currency in question on the payment day selected on the incoming payment. This information will be loaded from the exchange rate log.

#### Rate type
This setting is available if the Current exchange rate or Payment day's exchange rate option is selected in the system setting above. Here you can select if Current exchange rate, AFS rate, own defined rate type, or Use rate type from invoice (from customer/order type) should be used when receiving payments via file. (For the own defined rate type to appear in the list, you must first register such under the Rate types tab in the Currencies procedure.)

#### Payment method during set-off
This setting determines which payment method to use when the invoices should be set-off. The payment method must be registered in the Bank settings procedure. It must also be set as Active and have payment type Manual payment.

#### Default write-off code when difference occur in auto-matching
This system setting determines which write-off code should be used by default when differences occur in auto-matching of invoices when using confirmation via file in the Incoming payments procedure. The write-off codes must be registered in the Bank settings procedure.

#### Grace period for cash discount for incoming payments
Here you determine which grace period in calendar days should apply when cash discount is used. If you enter zero days as grace period, the customer must pay no later than the cash discount date. Otherwise, the cash discount will not be applied.
