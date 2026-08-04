### Settings – Write-down of costs and Write-up of costs

#### Price alternative for purchased part
With this setting you decide which price to use for valuation of purchased parts in the project. This is the price that is multiplied with the balance in the list and gives a value for the purchased part. Part balances are always reported in the part's default unit. Therefore, the selected price alternative is converted to the same unit. Read more about the different price alternatives below.
- Standard price – This is entered as standard price for purchased parts. The price is calculated via pre-calculations of manufactured parts and is used in the valuation of parts.
- FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price – The calculated FIFO price is used in the valuation of parts. This price is calculated via the old stock log records existing in the system. All records get a price that is calculated based on the order in which they were reported to stock and the price that applied to each arrival. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means the FIFO value can change even though no stock transaction has taken place after the most recent stock value list was created. Stock count and direct stock reporting (arrival) will have the part's standard price as value. In the Stock translation log procedure you can see the part's history. In the column Arrival reported price you see the price on which the FIFO price is based. If you use the option Warehouse, the FIFO price will be based on transactions made in all warehouses (since it is the same company). This applies even if you have selected to display data from only one warehouse in the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/G5_Stock_SV/Content/Resources/Images/button_warehouses.png).
- Supplier price – This price is entered on the parts' default supplier link and is used in the valuation of parts.
- Most recent purchase price – This is the purchase price that was saved during the part's latest arrival. It is used in the valuation of parts.
- Average purchase price – This is a weighted average value of purchase prices for a part, based on the ten most recent arrivals, and it is calculated as: total quantity x price for the 10 most recent arrivals / total purchased quantity. The price is used when valuing the parts.
- Mean price – This is an alternative average purchase price, which can be calculated in the Calculate mean price procedure. When calculating mean price you can select if you want to base the price on quantity or to use a time limit back in time. You can also calculate a weighted mean price (taking the purchased quantity into consideration).
- Future standard price – This price is the entered future standard price on purchased parts and is used in the valuation of parts.
- Price list – The price in the price list you select is used in the valuation of parts.

#### Price list
Here you choose which price list should be used for purchased parts if you have chosen Price list as price alternative.

#### Rate type
With this setting you select which rate type to use for the price alternative selected for purchased parts. The setting is available if you have selected a price alternative which can be saved in another currency. In that case you can here select a rate type. The price of the purchased parts in another currency is then converted to the company currency, using the exchange rate of the selected rate type. The Default rate type is configured in the System settings procedure under the Stock tab.

#### Historical price
Here you decide if the historical price of purchased parts should be used. The setting is only available for the price alternatives Standard price and Future standard price. Also the selected Balance alternative must be other than Current balance Current balance is the part balance at this moment on the locations. for it to be available. If you activate this setting, the parts will be valued according to the price that applied at the date of the balance alternative. The price for that date is registered in the standard price log in the part register. If you are using FIFO, a historical price is never loaded since it is not possible to use for a FIFO valuation.

#### Include SO mark-up
With this check box you determine if the parts' SO mark-up should be added to the selected price alternative. If you activate this setting, the purchased parts will be valued using: the selected price alternative + SO × the balance.

#### Historical mark-up
With this check box you determine if the parts' historical SO mark-up should be added to the selected price alternative. The historical SO mark-up is loaded from the date you have entered in the Balance alternative.

#### Price alternative for manufactured part
With this setting you decide which price to use for valuation of manufactured parts in the project. This is the price that is multiplied with the balance in the list and gives a value for the manufactured part. Part balances are always reported in the part's default unit. Therefore, the selected price alternative is converted to the same unit. Read more about the different price alternatives below.
- Standard price – The price that is calculated and saved as standard price, via pre-calculations of manufactured parts. It is used in the valuation of parts.
- Post-calculated mean price – The post-calculated mean price is used in the valuation of parts. This price is calculated in post-calculations as a mean price based on a number of selected manufacturing orders.
- FIFO price – The calculated FIFO price is used in the valuation of parts. This price is calculated via the old stock log records existing in the system. All records get a price which is saved at transfer to stock when you report the last operation on the manufacturing order as finished. Those records get the part's standard price as value at the time of the reporting. Other transactions such as negative reporting of material via manufacturing order, do not affect the calculation of FIFO price. If you use the option Warehouse, the FIFO price will be based on transactions made in all warehouses (since it is the same company). This applies even if you have selected to display data from only one warehouse in the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/G5_Stock_SV/Content/Resources/Images/button_warehouses.png).
- Future standard price – The price that is calculated and saved as future standard price, via pre-calculations of manufactured parts. It is used in the valuation of parts.
- Price list – The price in the price list you select is used in the valuation of parts.

#### Price list
Here you choose which price list should be used for manufactured parts if you have chosen Price list as price alternative.

#### Rate type
With this setting you select which rate type to use for the price alternative selected for manufactured parts. In other regards, the setting works in the same way as for purchased parts, see above.

#### Historical price
Here you decide if a historical price of manufactured parts should be used. In other regards, the setting works in the same way as for purchased parts, see above. This setting is deactivated for FIFO price.

#### Balance alternative
Here you select the balance, at different times, on the parts' locations, on which the value will be based. Explanation of the different alternatives:
- Current balance – If you select this option, the balance at this very time will be loaded.
- Last stock count date – With this option, the balance at the time of the last stock count date will be loaded. The parts might have been stock counted on different dates, so the date from which the balance origins may differ from part to part.
- Optional stock count date – With this option, the balance used for valuation is the balance at the selected stock count date. Only the parts and locations which were stock counted on the selected date will be included in the list. A date must be selected in the date field.
- Historical balance (log date) – With this alternative the balance from the selected log date will be loaded. The log date in the stock transaction log is the date on which a log record is created. A date must be selected in the date field. Fictitious parts with a value are also shown in the list.
- Historical balance (actual date) – With this option the balance from the selected date will be loaded. The actual date in the stock transaction log is the date entered during reporting. E.g. at arrival reporting, the date on which the delivery arrived is entered as delivery date and not the date at which the arrival reporting is made. A date must be selected in the date field. Fictitious parts with a value are also shown in the list.

#### Pre-select "Include"
This setting determines whether or not the “Include” box should be checked by default for all rows in the list/result.

#### Show configured parts
This setting is available if you use the option Product configurator. The setting determines if also configured parts should be included in the list.

#### No. of decimals for price
Enter how many decimals should be used in the price. The default option is 2, but you can select 0 to 6 decimals.
