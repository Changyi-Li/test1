### Settings – Miscellaneous
Here you configure additional settings for the calculation of WIP value.

#### Valuation time
With this setting you select if you wish to load the current WIP value as for today or a historical WIP value for a date in the past. The historical value can be based on the log date or the actual date of the transactions. If you select one of the alternatives for historical value, you will also be able to select for which date you wish to load the WIP value. Today's date is shown by default.
The historical valuation of WIP takes the order status at the selected time into consideration. E.g. if an order is finished today, but it was not finished at the selected date. This is also possible during historical valuation of current and planned/reported costs. Current costs are the costs that were current at the selected historical date. Planned/reported are the costs that were planned/reported at the selected historical date. In the field Valuation date you select which historical date should apply for the valuation.

#### Show
With this setting you determine which additional columns with different information that will be added to the list. Different columns are available to select depending on the selected list type.

#### Print result tabs
In this field you select which lists from the respective result tabs that will be included when printing to a printer. By default, only the list is printed.

#### Minimum value
Here you select an amount limit for the minimum value in the company currency. If the field is empty, the list will include individual rows for all the selected orders, regardless of how low WIP value each of the orders has. If you e.g. enter 100 as minimum value, all the minor positive amounts up to and including 99 and all the minor negative amounts down to and including -99 will be shown as a total under the headings "Total of small amounts". The small amounts are added to/subtracted from the total WIP value. The purpose of the minimum value is to create a shorter list that does not display small amounts.

#### Show configured parts
This setting is available if the option Product configurator is installed in your system. Here you determine if configured parts also should be included in WIP. You can also choose to only include configured parts.
When a manufacturing order contains a configured part, WIP is calculated as: Quantity x Configuration's saved calculations (instead of Quantity x Standard price).

#### Current FIFO price
This setting can be activated if the price alternative for purchased or manufactured part is FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price and the balance alternative is historical balance. If this setting is activated, the price in the list will be the current FIFO price instead of the FIFO price that was reported at the specified time.
