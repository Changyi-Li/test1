### Outgoing payment

#### Default exchange rate for outgoing payments
This system setting determines which exchange rate should be suggested during outgoing payment if the supplier invoice is issued in another currency than the company currency. The following options are available:
- Current exchange rate – The current exchange rate loaded from the Currencies procedure to be used as default exchange rate in the Purchase module.
- Invoice’s exchange rate – The exchange rate used on the supplier invoice.
- Payment day's exchange rate – The exchange rate that applied to the currency in question on the payment day selected on the outgoing payments payment. This information will be loaded from the exchange rate log.
For outgoing payments of the Other payments type, the rate of the payment day will always be suggested.

#### Rate type
This setting is available if the Current exchange rate or Payment day's exchange rate option is selected in the system setting above. Here you can then select if Current exchange rate, AFS rate, own defined rate type, or Use rate type from invoice (from supplier) should be used when making payments. (For the own defined rate type to appear in the list, you must first register such under the Rate types tab in the Currencies procedure.)

#### Default exchange rate for outgoing payments (via file)
This applies when confirmation is made on currency accounts. When confirming outgoing payments from file, you can with the help of this setting choose if the confirmation should take exchange rate profit/loss, if any, into consideration.
The following options are available:
- Current exchange rate – The current exchange rate loaded from the Currencies procedure to be used as default exchange rate in the Purchase module.
- Invoice’s exchange rate – The exchange rate used on the supplier invoice.
- Payment day's exchange rate – The exchange rate that applied to the currency in question on the payment day selected on the outgoing payments payment. This information will be loaded from the exchange rate log.

#### Rate type
This setting is available if the Current exchange rate or Payment day's exchange rate option is selected in the system setting above. Here you can then select if Current exchange rate, AFS rate, own defined rate type, or Use rate type from invoice (from supplier), should be applied when making payments via file. (For the own defined rate type to appear in the list, you must first register such under the Rate types tab in the Currencies procedure.)

#### Method for calculating payment date
Here you determine which method should apply when calculating payment date and this date falls on a weekend or holiday. The available alternatives are Previous workday or Next workday.

#### Calendar for calculation of payment date
Here you determine which calendar you want to use when calculating payment date. The default calendar is the company calendar which is selected in the Company information procedure. If you have added own holidays in the company calendar, then you might need to use another calendar when calculating payment date. For example, if you have added the company's vacation period as holidays in the company calendar. Outgoing payments should still be possible to perform during this period. Calendars are created in the Calendar procedure.

#### Payment date for overdue electronic payments
With this setting you decide when payment of overdue electronic invoices should take place from the Outgoing payments procedure. If you are unsure of which setting to use, check with your bank regarding their cut-off times for payments withing the same day.
-   
Next workday
-    
Today
> If Today is selected, today’s date is taken into consideration if you have activated the Consider cash discount date setting in the Outgoing payments procedure.
