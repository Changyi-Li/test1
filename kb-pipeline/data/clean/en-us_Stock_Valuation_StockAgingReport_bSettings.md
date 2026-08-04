### Settings

#### Price alternative for purchased part
With this setting you decide which price to use for valuation of purchased parts in stock. This is the price that is multiplied with the balance in the list and gives a stock value for the purchased part. The default price alternative here is Standard price. Part balances are always reported in the part's default unit. Therefore, the selected price alternative is converted to the same unit. Read more about the different price alternatives below.
- Standard price – This is entered as standard price for purchased parts. The price is calculated via pre-calculations of manufactured parts and is used in the valuation of parts.
- FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price – The calculated FIFO price is used in the valuation of parts. This price is calculated via the old stock log records existing in the system. All records get a price that is calculated based on the order in which they were reported to stock and the price that applied to each arrival. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means the FIFO value can change even though no stock transaction has taken place after the most recent stock value list was created. Stock count and direct stock reporting (arrival) will have the part's standard price as value. In the Stock translation log procedure you can see the part's history. In the column Arrival reported price you see the price on which the FIFO price is based. If the Warehouse option is used, the FIFO price will be based on the transactions of all warehouses (since it is the same company).
- Supplier price – This price is entered on the parts' default supplier link and is used in the valuation of parts.
- Most recent purchase price – This is the purchase price that was saved during the part's latest arrival. It is used in the valuation of parts.
- Average purchase price – This price is calculated as an average value of the part's purchase price on the ten most recent arrivals. It is used in the valuation of parts.
- Mean price – This is an alternative average purchase price, which can be calculated in the Calculate mean price procedure. When calculating mean price you can select if you want to base the price on quantity or to use a time limit back in time. You can also calculate a weighted mean price (taking the purchased quantity into consideration).
- Future standard price – This price is the entered future standard price on purchased parts and is used in the valuation of parts.
- Price list – The price in the price list you select is used in the valuation of parts.

#### Price list
If you have selected Price list in the setting above, you must her choose which price list should be used during the valuation.

#### Rate type
With this setting you select which rate type to use for the price alternative selected for purchased parts. The setting is available if you have selected a price alternative which can be saved in another currency. In that case you can here select a rate type. The price of the purchased parts in another currency is then converted to the company currency, using the exchange rate of the selected rate type. The Default rate type is configured in the System settings procedure under the Stock tab.

#### Historical price
Here you decide if the historical price of purchased parts should be used. The setting is only available for the price alternatives Standard price and Future standard price. Also the selected Balance alternative must be other than Current balanceCurrent balance is the part balance at this moment on the locations. for it to be available. If you activate this setting, the parts will be valued according to the price that applied at the date of the balance alternative. The price for that date is registered in the standard price log in the part register.

#### Include SO mark-up
With this check box you determine if the parts' SO mark-up should be added to the selected price alternative. If you activate this setting, the purchased parts will be valued using: the selected price alternative + SO × the balance.

#### Price alternative for manufactured part
With this setting you decide which price to use for valuation of manufactured parts in stock. This is the price that is multiplied with the balance in the list and gives a stock value for the manufactured part. The default price alternative here is Standard price. Part balances are always reported in the part's default unit. Therefore, the selected price alternative is converted to the same unit. Read more about the different price alternatives below.
- Standard price – The price that is calculated and saved as standard price, via pre-calculations of manufactured parts. It is used in the valuation of parts.
- Post-calculated mean price – The post-calculated mean price is used in the valuation of parts. This price is calculated in post-calculations as a mean price based on a number of selected manufacturing orders.
- FIFO price – The calculated FIFO price is used in the valuation of parts. This price is calculated via the old stock log records existing in the system. All records get a price which is saved at transfer to stock when you report the last operation on the manufacturing order as finished. The part's standard price at the time of the reporting is set as value on the records. Other transactions such as negative reporting of material via manufacturing order, do not affect the calculation of FIFO price. If you use the option Warehouse, the FIFO price will be based on transactions made in all warehouses (since it is the same company). This applies even if you have selected to display data from only one warehouse in the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png).
- Future standard price – The price that is calculated and saved as future standard price, via pre-calculations of manufactured parts. It is used in the valuation of parts.
- Price list – The price in the price list you select is used in the valuation of parts.

#### Rate type
With this setting you select which rate type to use for the price alternative selected for manufactured parts. In other regards, the setting works in the same way as for purchased parts, see above.

#### Historical price
Here you decide if a historical price of manufactured parts should be used. In other regards, the setting works in the same way as for purchased parts, see above.

#### Balance alternative
Here you select the balance, at different times, on the parts' locations, on which the stock value will be based. Explanation of the different alternatives:
- Current balance – If you select this option, the balance at this very time will be loaded.
- Historical balance (log date) – With this alternative the balance from the selected log date will be loaded. The log date in the stock transaction log is the date on which a log record is created. A date must be selected in the date field.
- Historical balance (actual date) – With this option the balance from the selected date will be loaded. The actual date in the stock transaction log is the date entered during reporting. For example during arrival reporting, the date on which the delivery arrived is entered as delivery date and not the date when the arrival reporting is actually made. A date must be selected in the date field.

#### Balance date
For the balance alternatives Historical balance (log date) and Historical balance (actual date) you should select a balance date.

#### Show in unit for stock count and stock reporting
Here you decide if the unit selected for stock count should be used in the stock aging report.

#### Show configured parts
This setting is available if you use the option Product configurator. The setting determines if also configured parts should be included in the list. These parts are then valuated in the same way as other parts according to the available price alternatives.

#### Calculate price per age interval
This setting is available when FIFO is applied. This means that the Value per interval is based on the price for each arrival in the time interval.

#### Age interval
Here you see the default number of age intervals and number of days per age interval. This is configured in the system settings Number of intervals and Number of days per interval. You can add and delete age intervals You can enter a maximum of 12 age intervals. 30 days per interval is most commonly used. For each age interval you can enter a Price deduction in percent.
If you enter age intervals in full years, you should enter 365 days for each year in the interval.
Example of correctly entered age interval for full calendar year:
| Year 1 | 365 days |
|---|---|
| Year 2 | 365 days |
| Year 3 | 365 days |

#### Price deduction for collecting interval (+)
The final age interval is automatically generated. It contains parts which fall outside the entered age interval. Here you enter a price deduction for the collecting interval, that is, where the remaining quantity and value will end up.
