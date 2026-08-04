### Value to post

#### Quantity
The options here depend on the Log and the Transaction type. The table below shows the alternatives available for each log and transaction type.
| Log | Transaction type | Quantity |  |  |  |  |
|---|---|---|---|---|---|---|
| Stock transaction log | All transaction types | Balance change |  |  |  |  |
| Manufacturing order log * | Processing * Subcontract * | Processing * | Subcontract * | Reported time * Planned time for reported quantity * Reported cost * Planned cost for reported quantity * Reported SC mark-up * Planned SC mark-up * | Reported time * Planned time for reported quantity * | Reported cost * Planned cost for reported quantity * Reported SC mark-up * Planned SC mark-up * |
| Processing * |  |  |  |  |  |  |
| Subcontract * |  |  |  |  |  |  |
| Reported time * Planned time for reported quantity * |  |  |  |  |  |  |
| Reported cost * Planned cost for reported quantity * Reported SC mark-up * Planned SC mark-up * |  |  |  |  |  |  |
| Price change log | Stock balance Balance between warehouses ** WIP balance Invoiced balance ** Delivered balance, not invoiced ** | Stock balance Balance between warehouses ** | WIP balance Invoiced balance ** Delivered balance, not invoiced ** | Stock balance WIP balance and "To stock" balance at time of price change * WIP balance at time of price change "To stock" balance at time of price change Stock in – stock at time of price change | Stock balance | WIP balance and "To stock" balance at time of price change * WIP balance at time of price change "To stock" balance at time of price change Stock in – stock at time of price change |
| Stock balance Balance between warehouses ** |  |  |  |  |  |  |
| WIP balance Invoiced balance ** Delivered balance, not invoiced ** |  |  |  |  |  |  |
| Stock balance |  |  |  |  |  |  |
| WIP balance and "To stock" balance at time of price change * WIP balance at time of price change "To stock" balance at time of price change Stock in – stock at time of price change |  |  |  |  |  |  |
| Calculation difference * | Calculation difference * | Reported quantity * |  |  |  |  |
| Invoicing log * | All transaction types * | Invoiced quantity |  |  |  |  |
* Alternatives marked with an asterisk are included in the Management accounting Management accounting is an option in Monitor ERP. It is used as a complement to the standard function called Stock accounting. The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5. The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor. Calculation differences are posted and these can be followed up per product, per order, etc. This function also contains extended management of cost of goods sold. option.
** Alternatives marked with double asterisks are only used when FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. is applied.
Alternatives in italics are default.

#### Price alternative for purchased part
With this setting you select which price alternative to use for purchased parts. The available alternatives depend on the selected Part type, Log, and Transaction type.

#### Price list
This field becomes available when "Price list" is selected as option for purchased parts in the stock transaction log and in the invoicing log. If the price list is in a different currency, then the rate type used when posting logs is determined by what is entered in the system setting Default rate type under the Accounting tab.

#### Price alternative for manufactured part
With this setting you select which price alternative to use for manufactured and fictitious parts. The available alternatives depend on the selected Part type, Log, and Transaction type.

#### Price list
This field becomes available when "Price list" is selected as option for manufactured parts in the stock transaction log and in the invoicing log. If the price list is in a different currency, then the rate type used when posting logs is determined by what is entered in the system setting Default rate type under the Accounting tab.

#### Price type
Price type is only available if the option Management accounting is installed. Here you select which price type should be used for processing costs. Price type is also used for posting of transactions in the invoicing log.
Manufacturing order log, transaction type Processing cost:
- Current
- Reported (default)
Invoicing log, transaction type Cost of goods sold (COGS):
- Price at delivery (default)
- Price when invoicing

#### Cost factors
The cost factors field is only available if the option Management accounting is installed. Here you select cost factor alternatives for posting of manufacturing order log and calculation differences. For example if cost factors such as direct work and manufacturing overhead (MO) should be posted separately.

#### Planned cost before invoice has been linked
This setting is only available for Manufacturing order log and transaction type Subcontract. The quantity must also be set to Reported cost or Reported SC mark-up. If this setting is activated, the system books the planned cost upon arrival. The cost can be adjusted when the supplier invoice is linked, that is, when the actual cost is known.
