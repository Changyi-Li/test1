### Settings (Safety stock/Reorder point)
Under General you select which parts should be included in the list based on the planning settings. Under Calculation parameters you configure how the list should be calculated. Under Price type you configure the price alternatives for purchased and manufactured parts.
General

#### Planning method
Here you select the planning method for the parts. Net requirement, Stock refill, and Physical are marked by default.

#### Control method
Here you select the control method of the parts. Both Stock driven and Order oriented are selected by default.

#### Lot sizing rule
Here you decide the lot sizing rule for stock driven and order oriented part. All alternatives are marked by default.

#### Formula
Here you select formula to use when calculation order quantity. The Wilson formula is selected by default. It is loaded from the Planning formulas procedure.
Calculation parameters

#### Ordering cost, manufacturing/purchase/subcontract
You can in these three fields enter ordering costs for manufacturing, purchase, and subcontract.

#### Holding cost
Here you can enter a holding cost in percent.

#### Allowed margin for excess balance
Here you can enter the allowed margin (in percent) for excess balance.

#### Use calculated order quantity (formula)
With this setting you decide if the order quantity calculated with the Wilson formula should be used. This setting is activated by default.

#### Add setup cost
With this setting you decide if setup cost (setup price) in supplier links and customer links, and setup cost in subcontracts in BOM and routing, should be included in the calculation. This setting is activated by default.

#### Part value including setup cost
Here you decide if the part's value should be calculated including setup cost or not. This setting is activated by default.
Price type
The price alternatives for purchased and manufactured parts are the bases of calculating values of reorders and excess balances in the list. Standard price is the default option.
If you select Price list for any of these alternatives, the corresponding Price list field becomes active and there you select which price list to apply.
If you have selected Supplier price, Future supplier price, or a price list in a different currency, the Rate type field will become available. There you select the rate type of the currency.
You find an explanation of the different price alternatives in this [topic](../../Parts/PartPrices.htm).
