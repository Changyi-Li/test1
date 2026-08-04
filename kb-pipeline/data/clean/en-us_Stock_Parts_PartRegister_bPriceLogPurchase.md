### Price log
In this box you can see information about purchase prices from the price log. The prices are shown in the company currency and the unit is the unit entered on the main row. Read more about the different [price alternatives](../PartPrices.htm).

#### Most recent purchase price
In this field you can see the part's last purchase price. This is the price from the most recently arrival reported purchase order, or the price from the most recent invoice, depending on which happened most recently.

#### Average purchase price
This is an average of a purchased part’s price, based on the ten most recent arrivals, and it is calculated as: quantity x price / total quantity. If one of the ten most recent arrivals is returned, this will be deducted from the calculation of the average purchase price.

#### Mean price
The mean price can be calculated by the user by choosing the date interval etc. The saved mean price is displayed here.

#### FIFO price
This field is shown for purchased and manufactured parts. Here you will see the current price according to the principle "First In – First Out" (FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit.). Data from the stock transaction log will be loaded in order to calculate the cost for the balance in stock at the moment.

#### Supplier price log
By clicking this button you can display a log of supplier prices from the supplier links.
