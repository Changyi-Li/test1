### Stock reporting

#### Check if balance is negative during reporting
This system setting determines if a check should be made to see if the balance is negative during reporting. If the balance is negative you can choose to display a warning in the quantity field or you can block for reporting.
The system setting also affects which quantity will be suggested to deliver in the Report delivery procedure (list type Free selection). If the system setting is set to Warn or Block, the Disposable balance The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. will be suggested to be delivered in the procedure. If the system setting is deactivated, the Remaining quantity will be suggested for delivery.

#### Check against
This system setting determines what the setting above should be checked against. The available alternatives are Location's balance and Part's total balance.

#### Block stock reporting if the part has no standard price
With this setting you decide if stock reporting should be blocked for parts that are stock updated and do not have a standard price (is 0,00). This block is activated for all stock transactions (in and out) in different procedures, as well as during stock count. The block also applies to tools which are stock updated when the Tools & Maintenance option is installed.
If the system setting is set to Yes, an error message is shown when performing stock transactions for parts which are stock updated and are missing s standard price. This means stock reporting cannot be done for these parts.

#### Valuation method for purchased parts in stock transactions
Here you decide which price to use when the stock has "non-traceable" increases due to different direct stock reporting items resulting in a balance increase. This type of reporting does not have a purchase order price or an invoice price as a basis, and must therefor be given a price if you apply FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit.. The following options are available:
- Standard price
- FIFO price – This option will make the system settings below available. There you get to select a price alternative.

#### Reported price on stock count (balance increase)
With this system setting you decide which price should be used when the stock has "non-traceable" increases due to stock count. This type of reporting does not have a purchase order price or an invoice price as a basis, and must therefor be assigned a price. The following options are available:
- Standard price – This option is default and the standard price is loaded from the part register.
- Most recent purchase price – The price is loaded form the purchase price which was most recently registered.
- Average purchase price – This price is an average value for the last ten purchase prices.
- Mean price – This is an alternative type of average purchase price for purchased parts, a so-called Mean price. This mean price is calculated in the Calculate mean price procedure.
- None – This option means that the increase will be valued to 0 and the user can manually decide which price should be used for this increase. This is done via the Price adjustment and the list type called Change price on stock increases – FIFO.

#### Reported price on direct stock reporting (balance increase)
Here you decide which price to use when the stock has "non-traceable" increases due to different direct stock reporting items resulting in a balance increase. This type of reporting does not have a purchase order price or an invoice price as a basis, and must therefor be assigned a price. The following options are available:
- Standard price – This option is default and the standard price is loaded from the part register.
- Most recent purchase price – The price is loaded form the purchase price which was most recently registered.
- Average purchase price – This price is an average value for the last ten purchase prices.
- Mean price – This is an alternative type of average purchase price for purchased parts, a so-called Mean price. This mean price is calculated in the Calculate mean price procedure.
- None – This option means that the increase will be valued to 0 and the user can manually decide which price should be used for this increase. This is done via the Price adjustment and the list type called Change price on stock increases – FIFO.

#### Reported price on negative reporting (balance increase)
A negative reporting resulting in a balance increase is, for example, a "minus withdrawal", when you put the parts back into the stock by reporting a negative withdrawal. The following options are available:
- Standard price – This option is default and the standard price is loaded from the part register.
- Most recent purchase price – The price is loaded form the purchase price which was most recently registered.
- Average purchase price – This price is an average value for the last ten purchase prices.
- Mean price – This is an alternative type of average purchase price for purchased parts, a so-called Mean price. This mean price is calculated in the Calculate mean price procedure.
- None – This option means that the increase will be valued to 0 and the user can manually decide which price should be used for this increase. This is done via the Price adjustment and the list type called Change price on stock increases – FIFO.

#### Valuation method for manufactured parts in stock transactions
Here you decide which price to use when the stock has "non-traceable" increases due to different direct stock reporting items resulting in a balance increase. This type of reporting does not have a standard price as a basis, and must therefor be given a price if you apply FIFO.
The following options are available:
- Standard price
- FIFO price – This option will make the system settings below available. There you get to select a price alternative.

#### Reported price on stock count (balance increase)
With this system setting you decide which price should be used when the stock has "non-traceable" increases due to stock count. This type of reporting does not have a standard price as a basis, and must therefor be given a price. The following options are available:
- Standard price – This option is default and the standard price is loaded from the part register.
- Future standard price – With this option, the future standard price is loaded from the part register.
- None – This option means that the increase will be valued to 0 and the user can manually decide which price should be used for this increase. This is done via the Price adjustment and the list type called Change price on stock increases – FIFO.

#### Reported price on direct stock reporting (balance increase)
Here you decide which price to use when the stock has "non-traceable" increases due to different direct stock reporting items resulting in a balance increase. This type of reporting does not have a standard price as a basis, and must therefor be given a price. The following options are available:
- Standard price – This option is default and the standard price is loaded from the part register.
- Future standard price – With this option, the future standard price is loaded from the part register.
- None – This option means that the increase will be valued to 0 and the user can manually decide which price should be used for this increase. This is done via the Price adjustment and the list type called Change price on stock increases – FIFO.

#### Reported price on negative reporting (balance increase)
A negative reporting resulting in a balance increase is, for example, a "minus withdrawal", when you put the parts back into the stock by reporting a negative withdrawal. The following options are available:
- Standard price – This option is default and the standard price is loaded from the part register.
- Future standard price – With this option, the future standard price is loaded from the part register.
- None – This option means that the increase will be valued to 0 and the user can manually decide which price should be used for this increase. This is done via the Price adjustment and the list type called Change price on stock increases – FIFO.

#### FIFO start date
Here you can see start dates for FIFO from the Generate connections according to FIFO procedure.

#### Use as actual date when undo reporting
Here you determine which date should be used for stock transactions that undo/reverse a reporting item affecting the stock balance. This is used with FIFO as valuation method.
- Today's date – With this option, today's date will be used for the transaction. This is default.
- Actual reporting date – This option will use the date on which the reporting was actually made.
