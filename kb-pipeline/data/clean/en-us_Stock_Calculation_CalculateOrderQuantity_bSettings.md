### Settings
General

#### Planning method
This setting is used to limit the part selection in the list. Net requirement, Stock refill, and Physical are marked by default.

#### Control method
This setting is used to further limit the part selection in the list. If you have selected Net requirement, then both Order oriented and Stock driven are shown. If you only have selected Physical, then no selection can be made here.

#### Lot sizing rule
This setting is used to limit the part selection in the list. The following four alternatives are available: Lot-for-lot and Linked requirement belong to the control method Order oriented. Fixed order quantity and Period requirement belong to the control method Stock driven.

#### Formula
Here you determine which planning formula you want to use during the calculation. You can select among the formulas found in the Planning formulas procedure. The default formula in that procedure will be suggested here.

#### Include staggered prices
With this checkbox you determine if staggered prices should be used when calculating. Calculations are made according to the following principle:
- Order quantity is calculated as per the Wilson formula for the lowest price.
- If the order quantity is valid, that is, that it is larger than the quantity limit applicable to get this price, the order quantity is economically optimal and no more calculation is needed.
- If the order quantity is not valid, meaning that the order quantity is lower than the quantity limit, order quantity is calculated to the next price level.
- If this order quantity is valid, the total cost is calculated for the latest calculated order quantity as well as all higher price limit quantities.
- The suggested order quantity will be the order quantity that gives the lowest total cost.
For example:
To use the Wilson formula, the following values are required: Ordering cost (EUR 200), Annual volume (4,600 pcs), and a Holding cost (25%). In this example, we have the following staggered prices:
| Limit value | Price |
|---|---|
| 100 pcs | EUR 80 |
| 1.000 pcs | EUR 75 |
| 2,500 pcs | EUR 72.50 |
Calculation:
1. Order quantity for the lowest price, i.e., EUR 72.50 is calculated. The order quantity is 318.62 pcs., meaning that the quantity does not fulfill the requirement of 2,500 pcs.
2. The next price level is then calculated, which in this case is EUR 75. The order quantity is then 312.26 pcs, which does not fulfill the requirement of 1,000 pcs either.
3. The next price level is EUR 80. The order quantity is then 303.32 pcs and fulfills the requirement of at least 100 pcs needing to be ordered for the price to be valid.
4. The total cost is worked out for the calculated order quantity as well as the total costs for all lower price levels and limit values.
1. 303.32 pcs for EUR 80 = EUR 374,066
2. 1000 pcs for EUR 75 = EUR 355,295
3. 2500 pcs for EUR 72.50 = EUR 356,524
5. In this case, the order quantity 1,000 pcs will be chosen as this results in the lowest total cost.
| Limit value | Price | Order quantity | Total cost for calc. order quantity |
|---|---|---|---|
| 100 pcs | EUR 80 | 303.32 pcs | EUR 374,066 |
| 1,000 pcs | EUR 75 | 313.26 pcs | EUR 355,295 |
| 2,500 pcs | EUR 72.50 | 318.62 pcs | EUR 356,524 |

#### Annual volume
If you have activated the system setting Show annual budget, annual volume, and order quantity with current pace, it is possible to use Annual volume or Annual volume, current pace when calculating order quantity. Annual volume is selected by default. If the system setting is not activated, you can only use Annual volume.

#### Daily pace
If you have activated the system setting Show annual budget, annual volume, and order quantity with current pace, it is possible to use Daily paceDaily pace is the consumption per day of a specific part. or Daily pace, current pace in calculations with Max. and Min. number of consumption days. Daily pace is selected by default. If the system setting is not activated, you can only use Daily pace.

#### Save to
If the system setting Show annual budget, annual volume, and order quantity with current pace has been activated, you can choose to save the result to Order quantity or to Order quantity, current pace. Order quantity is selected by default. If the system setting is not activated, you can only save to Order quantity.

#### Pre-select "Save"
This setting determines if save should be selected by default.

#### Save order quantity = 0
When this setting is activated, save will be selected by default for all parts except for parts where the order quantity is zero or negative.

#### Total annual volume from all warehouses
This setting is available if you have installed the option called Warehouse. If you activate this setting, the selected annual volume (Annual volume or Annual volume, current pace) will be totaled for all warehouses in the system. The result is saved to the order quantity in the warehouse you are working in. This setting is not selected by default.
Calculation parameters

#### Ordering cost, manufacturing
Here you enter the administrative cost per order to manufacture this part. If you leave this field empty, the Wilson formula cannot be used when calculating order quantity for manufacturing parts. The cost shall be entered in the company currency. The currency unit is displayed next to the entered cost.

#### Ordering cost, purchase
Here you enter the administrative cost per order to purchase this part. If you leave this field empty, the Wilson formula cannot be used when calculating order quantity for purchased parts. The cost shall be entered in the company currency. The currency unit is displayed next to the entered cost.

#### Ordering cost, subcontract
Here you add an ordering cost for subcontract. The ordering cost is multiplied by the number of subcontracts that exist for the part. Samples of specific ordering costs for subcontracts are: ordering, report dispatch, and supplier invoice management. Transport cost has a separate field and should therefore not be included in the ordering cost. The cost is entered in the company currency. The currency unit is displayed next to the entered cost.

#### Holding cost
Here you enter the holding cost that should be used in the Wilson formula. This is entered in percent. It is not possible to enter a negative value.

#### Add setup cost
Here you enter if the setup cost should be added to the ordering cost. For manufacturing parts, the setup cost according to the calculation applies. For purchased parts, the setup price for purchase applies. If the setup cost should be added, the field Cost factors is activated where you select a cost factor alternative. For subcontracts this alternative also means that the entered transport cost is added to the ordering cost.

#### Cost factors
This option is activated if you have selected Add setup cost or Part value including setup cost. Here you enter the cost factor alternatives that shall apply to the calculated setup cost. You can select among the three cost factors registered in the system. The alternatives are marked according to the system setting Default cost factors under the Calculations heading under the Manufacturing tab.

#### Number of orders per year
Here you enter how many orders per year are made for the parts you selected. This is a simplified method of calculating the part's order quantity by dividing the part's annual volume by the value entered here.
If no value is entered here, this method cannot be used.
If you have entered a value in this field as well as in the order quantity fields, then both the Wilson formula and this method will be used to calculate the order quantity. Read more about this in the section Calculations.

#### Minimum quantity
This setting determines if minimum quantity shall be used.

#### Rounding
This setting determines if rounding quantity shall be used. If this setting is activated, the calculated order quantity is rounded up to a multiple of the part's rounding quantity. This setting is activated by default.

#### Part value including setup cost
This setting determines if the setup cost shall be included in the part's price used when calculating order quantity. This setting is not checked by default.
Number of consumption days

#### Minimum value (Min.)
Here you can enter a minimum value for the order quantity in the unit "days consumption". For example, enter "5" if the order quantity cannot be less than 1 week's consumption. This value is then multiplied by the part's daily pace and is compared with the calculated order quantity. The Wilson formula does not have that kind of built-in limit.

#### Maximum value (Max.)
Here you can enter a maximum value for the order quantity in the unit "days consumption". For example, enter "250" if the order quantity cannot be more than 1 year's consumption. This value is then multiplied by the part's daily pace and is compared with the calculated order quantity. The Wilson formula does not have that kind of built-in limit.
