### Turnover ratio
This list type calculates the selected parts' turnover ratio. This is displayed as a quantity. The information in the list – except for part number, name, part type, and ABC ABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc. code – is described below.

#### Include
Mark this checkbox for the parts for which you want to save the turnover ratio. The selected turnover ratio (Actual or Calculated) in the settings under the Selection tab, is what will be saved for the parts.

#### Selected price
Here you see the part's price according to the selected price alternative in the Settings section under the Selection tab.

#### Actual consumption
Actual consumption shows how much has been used over the select time period. The statistics for consumption is loaded from all stock withdrawals for customer orders and manufacturing orders.

#### Actual consumption value
Here you see the value of the consumption of the part when the selected price alternative is applied.

#### Calculated turnover ratio
This value is calculated as Annual volume / Calculated average stock.

#### Actual turnover ratio
Here you see a value calculated as Actual consumption / Actual average stock.

#### Turnover difference
Here you see the difference between Calculated and Actual turnover ratio.

#### Balance
Here you see the part's current balance. It is shown as a total from all locations in the selected warehouse.

#### Value
Here you see the value of the part's balance. It is shown as Selected price x Balance.

#### Actual average stock
Here you see a value calculated as Actual consumption / Actual turnover ratio.
This value can also be checked in the Stock transaction log by selecting by part and the same time period as entered in the list in the Stock analysis procedure. Balance (after reporting) is compared to the number of days this balance has been valid, i.e. before the next consumption or arrival changed the balance. The weighted value is then totaled and is divided by the time span you have entered in days.
Examples
It could look like the following:
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/ActualTurnoverRatio.png)](../../../../Resources/Images/SubProjects/ActualTurnoverRatio.png)
| Quantity in stock | Number of days | Weighted value |
|---|---|---|
| 100 | 2 | 200 |
| 110 | 30 | 3300 |
| 121 | 325 | 39325 |
| 250 | 1 | 250 |
| 150 | 1 | 150 |
| 100 | 6 | 600 |
The total of the weighted value in this example would be 43825 divided by 365 days which gives an average of 120.068493.

#### Calculated average stock
This value is calculated as Safety stock + (Order quantity / 2).

#### Daily consumption
This value is calculated as Actual consumption / Timeframe in days.

#### Days until depletion
This value is calculated as Balance / Daily consumption.

#### Timeframe in days
Here you see the number of days included in the selected date interval in the From date and To date fields in the settings under the Selection tab.

#### Annual volume
Here you see the part's annual volume.

#### Safety stock
Here you see the part's safety stock.

#### Order quantity
Here you see the part's order quantity.
