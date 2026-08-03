### Settings

#### Formula
Here you determine which planning formula you want to use during the calculation. You can select among the formulas found in the Planning formulas procedure. The default formula in that procedure will be suggested here. See more about the different formulas directly in the Planning formulas procedure in the Monitor ERP software. You find more information about definitions for all variables included in the formulas in the Variables box in the Planning formulas procedure directly in the Monitor ERP software.

#### Number of decimals
Here you select how many decimals should be used in the calculated value. You can select 0-2 decimals. The default value here is 0.

#### Rounding
If this setting is activated, the calculated order quantity is rounded up to a multiple of the part's rounding quantity. This box is not checked by default.

#### Annual volume
If you have activated the system setting Show annual budget, annual volume, and order quantity with current pace, it is possible to use Annual volume or Annual volume, current pace in the calculations. Annual volume is selected by default. If the system setting is not activated, you can only use Annual volume.
The annual volume is also used to get a value for Daily pace Daily pace is the consumption per day of a specific part., which is: Annual volume ∕ Number of work days per year. The number of days worked per year that applies in the company is determined by the system setting Number of work days per year. Under Value you will see: daily pace × standard price.

#### Total annual volume from all warehouses
This setting is available if you have installed the option called Warehouse. If you activate this setting, the selected annual volume (Annual volume or Annual volume, current pace) will be totaled for all warehouses in the system when calculating daily pace. The result is saved to the order quantity in the warehouse you are working in. This setting is not selected by default.

#### Pre-select "Save"
This setting determines if the box S (Save) should be checked by default in the list. When this box is checked, you can change the value in the column New safety stock.

#### Save rows without quantity
This setting is available if you have activated the setting Pre-select "Save". This box is not checked by default. This setting determines that only parts in the list that get a new safety stock equal to zero will be saved.

#### Price alternative
With this setting you decide which price should be used for valuation of parts in stock. This is the price that will be multiplied by the balance in the list to provide a stock value for the parts. Standard price is the default price alternative here. Part balances are always reported in the part’s standard unit. That is why the selected price alternative is converted to the same unit.
You find an explanation of the different price alternatives in this [topic](../../Parts/PartPrices.htm).

#### Price list
The price in the price list you select here is used when doing a valuation of parts. If you choose a price list in another currency, you will also be able to select Rate type. The price lists must first be registered in the Price lists procedure.

#### Rate type
With this setting you select which rate type to use for the selected price alternative. The setting is available if you have selected a price alternative which can be saved in another currency. In that case you can here select a rate type. The price of the parts that are in another currency is then converted to the company currency, using the exchange rate of the selected rate type. The Default rate type is configured in the System settings procedure under the Stock tab.
