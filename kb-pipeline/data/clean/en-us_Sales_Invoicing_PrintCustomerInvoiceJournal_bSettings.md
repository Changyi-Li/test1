### Settings
Settings are available for the list types Customer invoice journal and Cancellation journal.

#### Enter voucher date manually
With this setting you determine whether or not the user should be able to enter a specific date for the vouchers. This can only be done if e.g. there are old entries belonging to a locked period. If you check this box, the field for voucher date below this setting will become activated.

#### Voucher date
With this setting you decide the voucher date according to the setting above. The field shows today's date by default.

#### Integration
Here you can see the type of integration configured for the list type in question. This is nothing you can change in this procedure. It is done in the Voucher number series/Journals procedure. The following integration options are available:
- No – With this alternative, no voucher is updated in the accounting.
- Via journal per invoice – With this alternative, the posting of each invoice will create a separate voucher in the accounting. The invoice number will be the voucher number. Information in the voucher will be saved in order to create traceability to the accounting. That way, you can trace the customer invoice to which the voucher refers.
- Via journal – Total – With this alternative, the journal will be recorded automatically in the accounting. The voucher numbers created are the next numbers in the current voucher number series.
An invoice in a foreign currency is always transferred together with the posting in the company currency, even if the invoice refers to another currency. Transactions will be transferred in parallel currencies only if the account is configured as a currency account.
