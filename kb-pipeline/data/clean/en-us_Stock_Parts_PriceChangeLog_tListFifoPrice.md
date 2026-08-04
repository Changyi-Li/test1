### The FIFO price list
This list shows detailed information about FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price changes for the selected parts.

#### Log date
Here you see the date when the price change was made.

#### Time
Here you see the time when the price change was made.

#### Old price
Here you see the price before the change was made.

#### New price
Here you see the price after the change was made.

#### Price difference
Here you see the difference between the old and new price.

#### Balance
Here you see the balance of the part.

#### Value
Here you see the value for the part.

#### WIP balance
Here you see the current WIP balance for the part at the time of the price change.

#### Transfer to stock WIP
Here you see quantity reported reported finished into stock from WIP on the order at the time of the price change.

#### WIP value
Here you see the current WIP value for the part at the time of the price change.

#### Delivered balance, not invoiced
Here you see the balance which has been delivered but which has not yet been invoiced.

#### Delivered value, not invoiced
Here you see the value of what has been delivered but that has not yet been invoiced.

#### Invoiced balance
Here you see the current invoiced balance for the part at the time of the price change.

#### Invoiced value
This is the invoiced quantity x the price difference.

#### Bal. betw. WH (Balance between warehouses)
Here you see the balance (the number of parts) that is considered to be in transit between warehouses. This column is only available in systems with the Warehouse option.

#### Value betw. WH (Value between warehouses)
Here you see the value of the parts that are considered to be in transit between warehouses. This column is only available in systems with the Warehouse option.

#### Order number (WIP)
Here you see which manufacturing order number the WIP balance is registered on at the time of the price change.

#### Order number (Arrival)
Here you see the arrival's order number.

#### Consecutive number
Here you see the supplier invoice's consecutive number which affects that price change.

#### Voucher date
Here you see the voucher date for the consecutive number above.

#### User
Here you see the user who has changed the price.

#### Type of change
Here you see how the price change was made. That is, if it was manually changed or if it was changed by a pre-calculation.
