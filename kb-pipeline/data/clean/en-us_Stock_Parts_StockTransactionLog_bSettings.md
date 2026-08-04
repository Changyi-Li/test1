### Settings

#### Show prices
With this setting you determine if prices will be shown in the list. The prices are arrival reported price (price of the purchase order), standard price, and value. If this setting is activated the four following settings will become available.

#### Arrival reported price including SO mark-up
With this setting you determine if the part's SO mark-up should be added to the arrival reported price. This only applies to purchased parts.

#### Show calculation information
Here you decide if the standard price for manufactured parts should display its division in consumed material, subcontract costs, and manufacturing costs. If you selected the current standard price in the setting above, the calculation information will be loaded from the calculation that created the current standard price. If you selected the reported price in the setting above, the calculation information will be loaded from the calculation that created the price that applied at the time of the reporting.

#### Show only arrivals for the current stock balance
(Detailed) With this setting you determine if only arrival records (positive changes of the balance) should be displayed. You will in that case see the arrivals as of today and earlier, until the total of the balance change covered by the part's actual stock balance is reached.
This setting is good to use if you wish to track FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. prices which load arrival reported price from arrivals that created the balance.
Example: The current stock balance is 100 pieces. The stock transaction log contains positive changes with arrival records which have increased the balance with 50, 20, 60, 40 pieces. If this setting is activated, only the first three log records will be shown in the list. That is, the arrival records which increased the balance with 50, 20, and 60 pieces. This is made since the current stock balance of 100 pieces only can consist of these three arrivals.

#### Show weight
Here you decide if the part's weight per unit should be multiplied by the balance change and shown as a column in the list.

#### Use unit for statistics
If the part has a unit selected to be used for statistics in the part register, you can activate this setting in order to display the part's balance after reporting and the balance change in that unit.

#### Load price from
- Price, P-part – Here you decide which price alternative should be used for purchased parts. Reported is loaded from the stock transaction log. The other price alternatives are loaded from the part register.
- Price list – This field is only available if Price list has been selected as price alternative.
- Rate type – This setting determines which rate type should be used by default when valuing purchased parts based on supplier price, future supplier price, and price list in another currency. Rate types must first be registered in the Currencies procedure.
- Price, M-part – Here you decide which price alternative should be used for manufactured parts. Reported is loaded from the stock transaction log. The other price alternatives are loaded from the part register.
- Price list – This field is only available if Price list has been selected as price alternative.
- Rate type – This setting determines which rate type should be used by default when valuing manufactured parts based on price list in another currency. Rate types must first be registered in the Currencies procedure.
