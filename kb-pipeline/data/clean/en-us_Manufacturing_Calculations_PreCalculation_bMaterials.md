### Material
These settings are available for the list type New calculation in the Pre-calculation.

#### Price alternative for purchased part
With this setting you decide which price to use for valuation of purchased parts. The default price alternative is determined by the system setting Price alternative for purchased parts when registering and reporting orders. Normally, the default price is set to Standard price. If you in the system setting selected the FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price option, that alternative will not be available here. The Standard price will then be the fallback alternative.
If you select the option Price list you can then choose a price list to use in the field below. You can also choose if Setup price and/or Staggered prices should be included.
If you select the option Supplier price or Future supplier price then you can also select rate type. This can be used in cases where the supplier uses another currency than the your company currency.
You find an explanation of the different price alternatives in this [topic](../../../Stock/Parts/PartPrices.htm).

#### Price list
Purchased parts will be valuated based on the price list you select here. If you choose a price list in another currency, you will also be able to select Rate type. The price lists must first be registered in the Price lists procedure.

#### Rate type
Here you select which rate type to use when valuing purchased parts based on a price list or a supplier which uses another currency. Rate types must first be registered in the Currencies procedure. The suggested rate type is determined by the system setting Default rate type under the Manufacturing tab.

#### Include
- Setup price – If you activate this setting, it means that when the price calculation of purchased parts is performed, the setup price in the price list/default supplier link will also be included in the calculation. The setup price is displayed under the Direct material tab.
-    
Staggered prices – The price each of purchased parts can be determined by the quantity in the price calculation if staggered prices are applied in the price list/default supplier link. Staggered prices are managed as described below.
If a requirement for the part exists, which is greater than the limit value for a staggered price, then the staggered price will be loaded to the calculation. Otherwise, the regular purchase price for the part will be used in the calculation. In the columns Price each and Staggered qty under the Direct material tab, you will see the staggered price and the staggered quantity. Otherwise, the regular purchase price will be shown and the staggered quantity will be 0 (zero).
The quantity used for staggering is different depending if it is an Order oriented (the requirement) or Stock driven (saved order quantity), but min. quantity and rounding are always used.

#### Valid through
A valid through date can be entered here for supplier price or future supplier price for these prices on purchased parts. Parts with purchase prices and a valid through date older than the selected date are displayed under the Warning list tab. This is used to see if the calculation is based on material prices that are expired. This field is empty by default, which means that no check against the valid through date will be made.

#### Explode
For stock driven M-parts, this means that they will be calculated for manufacturing in the calculation, using the quantity that is needed for one order. In this case, these parts are treated as if they were order oriented M-parts. This setting is not activated by default. These parts are then valued based on the selected Price type for stock driven M-part, unless you have chosen to recalculate stock driven M-parts (see below). 
For order oriented M-parts, this means that it is possible to save the exploded part since these have already been exploded in the regular calculation with the quantity that is used for 1 order.
The quantity of the exploded part is only used to save the exploded part. In your main calculations, an individual exploded quantity is always used for that specific part. If the exploded part is included in multiple main parts, the quantity shown will be an average of the main parts in which that part is included and those parts are shown in a separate section in the calculation result.

#### Recalculate
Here you can decide to recalculate the price for stock driven M-parts, order oriented M-parts and/or fictitious parts. This means that the price is recalculated for these parts so that the planned costs in the calculation will be current for the parts.
- Stock driven M-parts – This alternative is not available if you have chosen to explode stock driven M-parts. This alternative affects the price of the included stock driven manufactured parts in the calculation. The parts are recalculated using the part's order quantity.
- Order oriented M-parts – This alternative is not available if you have chosen to explode order oriented M-parts. This provides a unique calculation for the order oriented manufactured parts according to their own calculation quantity and making it possible to save a new price for the parts in question. However, this new price is not used in the ordered calculation. It is only an extra "side calculation" according to the part's own order quantity. In the main calculation it will always be calculated according to the quantity corresponding to the requirement in each structure.
- Fictitious parts – This alternative works just as for order oriented manufactured parts. Fictitious parts can be recalculated and saved.

#### Price alternative for stock driven manufactured part
With this setting you determine the price alternative that the cost will be valued to for stock driven manufactured parts. The default price alternative is determined by the system setting called Price alternative for stock driven parts when registering and reporting orders. Normally, the default price is set to Standard price. If you in the system setting selected the FIFO price option, that alternative will not be available here. The Standard price will then be the fallback alternative.
If you select the option Price list you can then choose which price list to use in the field below.
You find an explanation of the different price alternatives in this [topic](../../Topics/Stock/Parts/PartPrices.htm).

#### Price list
Here you select which price list that should be used to valuate stock driven manufactured parts.. If you choose to use a price list in another currency, you will also be able to select a rate type in the field below. The price lists must first be registered in the Price lists procedure.

#### Rate type
In this field you select the rate type to use when valuing stock driven manufactured parts based on a price list in another currency. Rate types must first be registered in the Currencies procedure. The suggested rate type is determined by the system setting Default rate type under the Manufacturing tab.

#### Oldest price
The prices for the parts that are older than the selected date are displayed under the Warning list tab. This function, oldest price, is used in order to see if the calculation is based on material prices that are outdated and that have not been revised for a long time. You can compare all the price alternatives, except for Average purchase price and Most recent purchase price, since those do not have any price dates.
