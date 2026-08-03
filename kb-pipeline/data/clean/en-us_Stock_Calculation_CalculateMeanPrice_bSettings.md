### Settings

#### Number of decimals
Here you enter how many decimals should be saved/managed in the new price. The default option is 2 decimals, and the maximum is 5 decimals.

#### Pre-select "Save"
Use this setting to decide if the Save checkbox should be marked by default in the list.

#### Save mean price which is less than or equal to 0
If you activate the setting Pre-select "Save", this setting will also become activated. However, this setting is not activated by default.

#### Pre-select "Include"
With this checkbox you decide if all arrivals should be selected by default.

#### Only incl. final recorded rows
Here you decide if calculations should only be made on final recorded rows.

#### Include purchase order rows not arrived
With this setting you decide if purchase order rows which have not been arrival reported should be included in the mean price calculation.

#### Include deviating purchase prices
This setting is activated by default. In this column you determine which deviating rows should be included in the mean price calculation. The checkbox I (Include) is then marked by default on these rows.
A purchase price on one row is considered to be deviating if the price is less than (average value - standard deviation) or greater than (average value + standard deviation).
When a purchase order row in the list has a deviating purchase price, all information is displayed in red on the row and a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is displayed in the column New mean price on the part.

#### Weighted price
This setting determines if weighted price should be used during the mean price calculation. This setting is activated if the setting above, Include deviating purchase prices, also has been activated. In order to calculate mean price based on weighted price, rows with deviating purchase prices in the purchase statistics must also be included. This means that weighted price considers the volume that was purchased on each occasion and not only the purchase price itself See the example below:
|   | Quantity | Price each | Total |
|---|---|---|---|
| Purchase 1 | 10 | 500 | 5000 |
| Purchase 2 | 2 | 600 | 1200 |
| Purchase 3 | 3 | 500 | 1500 |
| Total | 15 | 1600 |   |
Mean price: 1600 / 3 = 533.33
Weighted price: 500 x 10 / 15 + 600 x 2 / 15 + 500 x 3 / 15 = 513,33

#### Setup price
This setting is not checked by default. This setting determines if setup price should be included in the calculation. If the calculation is based on purchase statistics, the setup price is included on the order row. This setup price is loaded from the invoicing log. If the mean price is based on supplier price, the setup price on the supplier link is included in the calculation. This setting does not apply when the mean price is based on most recent purchase price or average purchase price, since the setup price is always included in the calculation of these prices.

#### Discount
This setting is activated by default. This setting determines if discount should be deducted from the price each when calculating mean price. If the calculation is based on purchase statistics, the discount is deducted from the price each on the order row. This discount is loaded from the invoicing log. If the mean price is based on supplier price, the discount on the supplier link is deducted from the price each in the calculation. This setting does not apply when the mean price is based on most recent purchase price or average purchase discount, since the discount is always deducted in the calculation of these prices.

#### Discount categories
This setting is activated by default. This setting determines if discount categories will be taken into consideration when discount is deducted from the price each when calculating mean price. Discount is then deducted according to the table entered in the Discount categories procedure. This setting does not apply if a discount is entered for the pre-selected supplier, or if the mean price is based on most recent purchase price or average purchase discount, since the discount is always deducted in the calculation of these prices.

#### Arrival date
Here you can select From date and To date. The calculation is then based on purchases made during this period. If you leave the From field empty, then there is no limit back in time for the arrivals. If you leave the To field empty, it means today's date.

#### Purchase orders
Here you enter the minimum number of purchase orders that must exist for the part in order for the calculation to be made. If the number of purchase orders falls below this, then the Price alternative when no arrival reporting exist is used instead. You can also enter a maximum number of purchase orders.

#### Price alternative when no arrival reporting exists
These price alternatives are used when no arrival reporting exists. The available price alternatives are Most recent purchase price, Standard price, and Supplier price. By using the arrow buttons you can sort the alternatives in order of priority. If all alternatives are unchecked, then parts that have a mean price that is less than or equal to zero will be sorted out. This is useful if you only want to calculate mean price for parts that have been arrival reported.
If the price alternative Supplier price is used and there is a setup price on the supplier link, the mean price might be very high if you only buy one (1) since the setup price is added to the purchase price.
