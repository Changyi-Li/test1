### Material
Here you select how the reported material should be valued in the post-calculation. The calculation is always based on the reported quantity, but here you can determine the cost for this. Material refers to purchased and stock driven parts.

#### Material cost
There are two alternatives for material cost:
- Planned/Reported (default) – With this alternative the material cost will be valued to the price that applied at the time of the reporting. The price alternatives that have been used are the ones selected in the system settings Price alternative for purchased parts when registering and reporting orders and Price alternative for stock driven parts when registering and reporting orders. By using this alternative, you will get the same material cost regardless of when the calculation is made (as long as the reported quantity is not changed).
- Current – This alternative will valuate the material cost based on the price alternative that you select in the fields Price alt. for purchased part and Price alt. for stock driven M-part that will be displayed when you select Current. The current prices for the parts will then be loaded from the selected price alternatives. The price alternatives suggested in the fields are the ones selected in the system settings mentioned above.

#### Include cost for rejection
Default. Here you determine if the cost for rejections should be included in the post-calculation.

#### Post-calculate stock driven M-parts
This checkbox becomes available if you selected the list type Part (mean price calculation) and if the material cost has been set to Planned/Reported.
By using this alternative you can load reported costs on included stock driven parts, rather than using a planned price according to a price alternative. The calculation of costs is then performed based on the order manufactured closest to the planned consumption date for the part. If there are no orders to base the calculation on, the parts will be valued according to the planned/reported price for the affected manufacturing orders. You can also post-calculate included stock driven manufactured parts even when they exist in several levels.

#### Price alternative for purchased part
With this setting you decide which price to use for valuation of purchased parts. The default price alternative is determined by the system setting Price alternative for purchased parts when registering and reporting orders. Normally, the default price is set to Standard price.
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

#### Price alternative for stock driven manufactured part
With this setting you determine the price alternative that the cost will be valued to for stock driven manufactured parts.
If you select the option Price list you can then choose which price list to use in the field below.
You find an explanation of the different price alternatives in this [topic](../../../Stock/Parts/PartPrices.htm).

#### Price list
Here you select which price list that should be used to valuate stock driven manufactured parts.. If you choose to use a price list in another currency, you will also be able to select a rate type in the field below. The price lists must first be registered in the Price lists procedure.

#### Rate type
In this field you select the rate type to use when valuing stock driven manufactured parts based on a price list in another currency. Rate types must first be registered in the Currencies procedure. The suggested rate type is determined by the system setting Default rate type under the Manufacturing tab.
