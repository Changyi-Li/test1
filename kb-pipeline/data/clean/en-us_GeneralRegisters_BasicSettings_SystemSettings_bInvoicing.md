### Invoicing

#### Record material cost of goods sold at invoicing
In order to record COGS at invoicing, you also need to select the cost accounts and stock accounts that should be used per product group and customer group in each posting group.
This system setting then determines if the accounts for material cost of goods sold (COGS) should be posted as cost account on the accounting order, with the stock account as offset account. This is made under the Sales account tab in the Posting matrix procedure.
> If the standard price on a customer order row has been manually changed, then this amount will be used as COGS regardless of what has been selected in this system setting.
Posting of COGS in connection with approving the invoice is not made for:
- Row type 2.
- Rows that have been deselected to Affect balance in the Register invoice directly procedure.
- Parts for which stock update has not been activated in the Part register procedure (at the time when the part was delivery reported). Please note! Service parts are excepted from this. For these parts, posting of COGS is always made if the affected accounts are configured to do so in the posting matrix.

#### Price alternative for M-parts (COGS)
If you have activated the system setting above, this system setting will be activated as well. Here you select which price alternative should be used in the calculation of COGS for M-parts. You can choose from the following price alternatives:
- Standard price at delivery – COGS will be posted using the standard price that applies at delivery.
- Standard price at invoicing – COGS will be posted using the standard price that applies at invoicing.
- Material cost excluding SO – COGS will be posted using the material cost excluding SO.
- Material cost including SO – COGS will be posted using the material cost including SO.
- FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price at delivery – COGS will be posted using the saved post-calculated FIFO price for the order in question.
- According to price list – COGS will be posted using the price list selected in the system setting below.
> If the standard price on a customer order row has been manually changed, then this amount will be used as COGS regardless of what has been selected in this system setting.

#### Price list for M-parts (COGS)
If the price alternative for cost of goods sold is set to According to price list, you should select a price list for M-part in this system setting.

#### Price alternative for P-parts (COGS)
If you have activated the system setting called Record material cost of goods sold at invoicing, you should here select which price alternative to use in the calculation of COGS for P-parts. You can choose from the following price alternatives:
- Standard price at delivery excluding SO – COGS will be posted using the standard price that applies at delivery. COGS for purchased parts is posted excluding SO mark-up.
- Standard price at delivery, including SO – The same standard price will be used as above. However, purchased parts are posted including SO mark-up.
- Standard price at invoicing excluding SO – COGS will be posted using the standard price that applies at invoicing. COGS for purchased parts is posted excluding SO mark-up.
- Standard price at invoicing, including SO – The same standard price will be used as above. However, purchased parts are posted including SO mark-up.
- FIFO price at delivery excluding SO – The FIFO price is loaded according to the reported price which may be the arrival reported price, the invoice price according to the linked supplier invoice or from the Distribute expense invoice procedure. The SO mark-up is excluded when using this alternative.
- FIFO price at delivery including SO – The FIFO price is loaded according to the reported price which may be the arrival reported price, the invoice price according to the linked supplier invoice or from the Distribute expense invoice procedure. The SO mark-up is included when using this alternative.

#### Price list for P-parts (COGS)
If the price alternative for cost of goods sold is set to According to price list, you should select a price list for P-part in this system setting.

#### Consider holidays when calculating due date
This system setting determines if the system should consider holidays when calculating due date on invoices and pro forma invoices that are printed. If you select No, the due date will always be the invoice date plus the payment term on the invoice. If you select Yes (use previous workday) and the due date falls on a weekend or holiday, the due date will be moved to the previous workday. If you select Yes (use next workday) and the due date falls on a weekend or holiday, the due date will be moved to the next workday.

#### Calendar for calculation of due date
This system setting is activated if one of the Yes alternatives above has been selected. Here you determine which calendar should be used when calculating the due date. The default calendar is the company calendar which is selected in the Company information procedure. If you have added own holidays in the company calendar, then you might need to use another calendar when calculating due date. For example, if you have added the company's vacation period as holidays in the company calendar. The customer should still be able to pay invoices during this period. Calendars are created in the Calendar procedure.

#### Amount of invoicing charge
Here you enter the amount of the invoicing charge. Which invoices should be charged is determined by the system setting below.

#### Only apply invoicing charge if invoice value is less than
This system setting determines that invoicing charge will be applied to invoices with an invoice value less than the value entered here.

#### Check if price is missing at invoicing
This setting determines if a check should be made to find invoice rows without price. The system will then warn or block when this occur. This applies to the Price each field.

#### Default payment terms on credit invoices
This system setting determines which payment term should be selected by default on credit invoices. The payment term must be registered in the Terms procedure.

#### Exchange rate at invoicing
This system setting determines which exchange rate should be used when invoicing in a foreign currency. However, any forward rate on the invoice basis will override this. The alternatives are:
- Current rate – (default) the exchange rate that applied when the invoice was registered.
- Rate according to invoice date – the exchange rate that applied at the invoice date (the printout date on the invoice).

#### Print to printer when e-mailing invoices
This setting determines if the invoices also should be printed to printer when they are sent via e-mail. This is useful if you want to save the invoices in a binder.

#### Default number of copies
If the setting above has been activated, this setting will be activated as well. Here you enter the default number of copies that should be printed to printer when sending invoices via e-mail.

#### Recipient of invoice via e-mail is loaded from
This setting determines if the invoice recipient's e-mail addresses should be loaded from invoices or customer register.

#### Use invoice number for pro forma
With this setting you decide if the pro forma’s invoice number should be loaded form the invoice basis. This means that the pro forma invoice will be assigned the same invoice number as the regular invoice. The invoice number becomes reserved when you approve the pro forma invoice and this is only possible when you create a pro forma from pick list and from invoice basis. If you approve a pro forma invoice that was created from/based on a customer order, the pro forma invoice will be assigned a number from the pro forma number series.
- No – No invoice number is reserved when you approve the pro forma invoice. The number will instead be loaded from the number series for pro forma invoices.
- Yes, from pick list – Here you determine if the pro forma should get the same number as the regular invoice. An invoice number from the invoice number series is reserved when you approve the pro forma in the Review/Approve pro forma invoice procedure, list type Pro forma Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees. from pick list.
- Yes, from invoice basis – Determines if the pro forma should get the same number as the regular invoice. An invoice number from the invoice number series is reserved when you approve the pro forma invoice in the Review/Approve Pro forma invoice procedure, list type Pro forma from invoice basis.

#### Printout/e-mail during export of e-invoice
This system setting determines if the invoices also should be printed to printer/sent via e-mail when they are exported as e-invoices. If you select No, the invoices will be exported to the operator without being printed in Monitor ERP, or without being sent via e-mail from Monitor ERP.

#### "Affect balance" activated by default when registering invoice
With this setting you decide if the stock balance should be affected by default when you register an invoice. The setting does not apply when registering credit invoice.

#### Assign delivery note number when invoice basis does not affect balance
With this system setting you decide if a delivery note number from the number series should be generated when the rows on an invoice basis does not affect the stock balance. This is useful if you, for example, have created an invoice basis for freight costs (or other services which do not affect the stock balance) and you thereby do not need a delivery note number.

#### Service part for collective discount invoice
This system setting determines which service part should be used on the collective discount invoice row. The part must be created using the type Service in the Part register procedure. The account for collective discount is entered for the part’s product group in the Posting matrix procedure.

#### Generate text rows for invoices included in collective discount invoice
This system setting determines if text rows should be shown on collective discount invoices. The text rows contain invoice numbers and invoice dates for the invoices that form the basis for the discount.

#### Enable split invoice basis
With this setting you decide whether or not an invoice basis can be split into multiple invoice bases. When this setting is set to Yes, the list types Split invoice basis and Undo split invoice basis become available in the Invoice basis – Sales procedure.
You can use this feature to split an invoice basis if a quantity of units have been delivered, but the entire quantity should not be invoiced at the same time. Stock transactions are also split when you split an invoice basis.
For an invoice basis to be splittable, it must have status 3 – Pending. It is only possible to undo a split on invoice bases that have status 3.
> Splitting an invoice basis also splits stock transactions so we recommend that systems running FIFO do NOT use this feature.

#### Check if delivery date is later than the invoice date at invoicing
This setting determines whether a warning or block message will be shown when invoice bases that have a delivery date later than the invoice date are loaded into the Review/Approve invoice procedure.
- Inactive (default) – If the Inactive option is selected, no warning or block is shown in Review/Approve invoice if the invoice contains a delivery date later than the invoice date.
- Warn – If the Warn option is selected, a warning will be shown in Review/Approve invoice if the invoice contains a delivery date later than the invoice date. The warning indicates that the invoice contains one or more deliveries with later dates that the invoice date.
- Block – If the Block option is selected, a block message will be shown in Review/Approve invoice if the invoice contains a delivery date later than the invoice date. The message indicates that the invoice contains one or more deliveries with later dates that the invoice date and prevents the invoice from being issued.
