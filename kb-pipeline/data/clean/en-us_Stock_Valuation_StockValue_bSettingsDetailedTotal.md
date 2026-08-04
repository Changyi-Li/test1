### Settings – Total, Detailed with location, and Withdrawn reusable tools

#### Price alternative for purchased part
With this setting you decide which price to use for valuation of purchased parts in stock. This is the price that is multiplied with the balance in the list and gives a stock value for the purchased part. The default price alternative here is Standard price. Part balances are always reported in the part's default unit. Therefore, the selected price alternative is converted to the same unit. Read more about the different price alternatives below.
- Standard price – This is entered as standard price for purchased parts. The price is calculated via pre-calculations of manufactured parts and is used in the valuation of parts.
- FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price – The calculated FIFO price is used in the valuation of parts. This price is calculated via the old stock log records existing in the system. All records get a price that is calculated based on the order in which they were reported to stock and the price that applied to each arrival. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means the FIFO value can change even though no stock transaction has taken place after the most recent stock value list was created. Stock count and direct stock reporting (arrival) will have the part's standard price as value. In the Stock translation log procedure you can see the part's history. In the column Arrival reported price you see the price on which the FIFO price is based. If you use the option Warehouse, the FIFO price will be based on transactions made in all warehouses (since it is the same company). This applies even if you have selected to display data from only one warehouse in the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png).
- Supplier price – This price is entered on the parts' default supplier link and is used in the valuation of parts.
- Most recent purchase price – This is the purchase price that was saved during the part's latest arrival. It is used in the valuation of parts.
- Average purchase price – This is a weighted average value of purchase prices for a part, based on the ten most recent arrivals, and it is calculated as: total quantity x price for the 10 most recent arrivals / total purchased quantity. The price is used when valuing the parts.
- Mean price – This is an alternative average purchase price, which can be calculated in the Calculate mean price procedure. When calculating mean price you can select if you want to base the price on quantity or to use a time limit back in time. You can also calculate a weighted mean price (taking the purchased quantity into consideration).
- Future standard price – This price is the entered future standard price on purchased parts and is used in the valuation of parts.
- Price list – The price in the price list you select is used in the valuation of parts.

#### Rate type
With this setting you select which rate type to use for the price alternative selected for purchased parts. The setting is available if you have selected a price alternative which can be saved in another currency. In that case you can here select a rate type. The price of the purchased parts in another currency is then converted to the company currency, using the exchange rate of the selected rate type. The Default rate type is configured in the System settings procedure under the Stock tab.

#### Historical price
Here you decide if the historical price of purchased parts should be used. The setting is only available for the price alternatives Standard price and Future standard price. Also the selected Balance alternative must be other than Current balanceCurrent balance is the part balance at this moment on the locations. for it to be available. If you activate this setting, the parts will be valued according to the price that applied at the date of the balance alternative. The price for that date is registered in the standard price log in the part register. If you are using FIFO, a historical price is never loaded since it is not possible to use for a FIFO valuation.

#### Include SO mark-up
With this check box you determine if the parts' SO mark-up should be added to the selected price alternative. If you activate this setting, the purchased parts will be valued using: the selected price alternative + SO × the balance.

#### Historical mark-up
With this check box you determine if the parts' historical SO mark-up should be added to the selected price alternative. The historical SO mark-up is loaded from the date you have entered in the Balance alternative.

#### Load price from original batch
This setting can be activated if FIFO price is used as price alternative on purchased or manufactured parts. If the setting is activated, the price for a split batch is loaded from the original batch. This is useful if you suspect that the price of the original batch has been updated after the batch was split.

#### Price alternative for manufactured part
With this setting you decide which price to use for valuation of manufactured parts in stock. This is the price that is multiplied with the balance in the list and gives a stock value for the manufactured part. The default price alternative here is Standard price. Part balances are always reported in the part's default unit. Therefore, the selected price alternative is converted to the same unit. Read more about the different price alternatives below.
- Standard price – The price that is calculated and saved as standard price, via pre-calculations of manufactured parts. It is used in the valuation of parts.
- Post-calculated mean price – The post-calculated mean price is used in the valuation of parts. This price is calculated in post-calculations as a mean price based on a number of selected manufacturing orders.
- FIFO price – The calculated FIFO price is used in the valuation of parts. This price is calculated via the old stock log records existing in the system. All records get a price which is saved at transfer to stock when you report the last operation on the manufacturing order as finished. Those records get the part's standard price as value at the time of the reporting. Other transactions such as negative reporting of material via manufacturing order, do not affect the calculation of FIFO price. If you use the option Warehouse, the FIFO price will be based on transactions made in all warehouses (since it is the same company). This applies even if you have selected to display data from only one warehouse in the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png).
- Future standard price – The price that is calculated and saved as future standard price, via pre-calculations of manufactured parts. It is used in the valuation of parts.
- Price list – The price in the price list you select is used in the valuation of parts.

#### Rate type
With this setting you select which rate type to use for the price alternative selected for manufactured parts. In other regards, the setting works in the same way as for purchased parts, see above.

#### Historical price
Here you decide if a historical price of manufactured parts should be used. In other regards, the setting works in the same way as for purchased parts, see above. This setting is deactivated for FIFO price.

#### Show calculation information
If you activate this setting, you will also see (in addition to the value of the manufactured part) sub-totals of material, SO, subcontract, SC, and processing. You can only see this information if there is a calculation linked to the price in the selected price alternative. The sub-totals are displayed on each part row. In the list total you will also see a breakdown of the processing for the cost factor alternatives in the calculation.
If you have activated the alternative Historical price, the date of the selected price alternative is also taken into account when calculation information is displayed. If you have selected e.g. a historical balance and activated the setting Historical price, the system will try to match the price with a calculation, via the standard price log in the part register, based on the date of the historical balance. If there is no calculation for that date, no calculation information will be displayed in the list (e.g. if the price has been manually changed).

#### Balance alternative
Here you select the balance, at different times, on the parts' locations, on which the stock value will be based. Explanation of the different alternatives:
- Current balance – If you select this option, the balance at this very time will be loaded.
- Last stock count date – With this option, the balance at the time of the last stock count date will be loaded. The parts might have been stock counted on different dates, so the date from which the balance origins may differ from part to part.
- Optional stock count date – With this option, the balance used for valuation is the balance at the selected stock count date. Only the parts and locations which were stock counted on the selected date will be included in the list. A date must be selected in the date field.
- Historical balance (log date) – With this alternative the balance from the selected log date will be loaded. The log date in the stock transaction log is the date on which a log record is created. A date must be selected in the date field. Fictitious parts with a value are also shown in the list.
- Historical balance (actual date) – With this option the balance from the selected date will be loaded. The actual date in the stock transaction log is the date entered during reporting. E.g. at arrival reporting, the date on which the delivery arrived is entered as delivery date and not the date at which the arrival reporting is made. A date must be selected in the date field. Fictitious parts with a value are also shown in the list.

#### Show
With this setting you determine which dates to be displayed for the parts in the list. For all list types, the available option are: Last consumption date, Last arrival date, and Last stock count date. For the detailed list type there is also an option called Price date, that is then shown for the selected price alternative in the list.

#### Also include parts without balance
With this checkbox you determine if parts with a zero balance for the selected balance alternative will be also included in the list.
This setting is not available for the list type Withdrawn reusable tools. That list type is available if you have installed the Tools & Maintenance option.

#### Minimum value
Here you enter an amount limit of a part's minimum stock value in the company currency for the selected balance alternative. If the field is empty, the list will include individual rows for all parts selected, regardless of how low a stock value each of the parts has. If you e.g. enter 100 as minimum value, all the minor positive amounts up to and including 99 and all the minor negative amounts down to and including -99 will be shown as a total under the headings "Total of small positive amounts" and "Total of small negative amounts". The small amounts are added to/subtracted from the total stock value. The purpose of the minimum value is to create a shorter list that does not display small amounts.

#### Difference between actual date and log date
This setting is available if Balance alternatives has been set to Historical balance (actual date). Then you can here enter a maximum number of months back in time from the actual date to show difference compared to the log date for each record. The default option here is 3 months. The maximum is 100 months. You can enter the number of months to 0 in this setting meaning an infinite number of months back.
> Please note! It will take longer to load the list if you do not enter a time interval.
Example of what difference between actual date and log date means: If the log date is set back 1 month in time because a reporting was forgotten a month ago, the difference between actual date and log date is 1 month.

#### Show in unit for stock count and stock reporting
Here you decide if the unit selected for stock count should be used in the stock value list.

#### Show configured parts
This setting is available if you use the option Product configurator. The setting determines if also configured parts should be included in the list. These parts are then valuated in the same way as other parts according to the available price alternatives.
> For configured parts, the configurations' calculated price is saved in the stock transaction log. This affects the valuation according to FIFO on new reporting items.

#### Current FIFO price
This setting can be activated if the price alternative for purchased or manufactured part is set to FIFO price, and if the balance option selected is historical balance. The price in the lists is shown with the current FIFO price for each arrival that has been added to the total balance at the specified time, instead of the FIFO price which was reported at the specified time. If this setting is activated, the FIFO price in the stock value will take price changes in the stock balance made after the date entered in the selection, into consideration.

#### No. of decimals for price
Enter how many decimals should be used in the price. The default option is 2, but you can select 0 to 6 decimals.

#### No. of decimals for value
Enter how many decimals should be used in the value. The default option is 2, but you can select 0 to 6 decimals.

#### Ignore renamed locations
Can be used in the list type Detailed with location if Historical balance or Last stock count date is selected as balance alternative.
Location names that were modified in Monitor G4 can cause renamed locations to be displayed with a balance in the Detailed with location list type. If you activate this setting, the system will try to identify such name changes and ignore the balance for these locations.
