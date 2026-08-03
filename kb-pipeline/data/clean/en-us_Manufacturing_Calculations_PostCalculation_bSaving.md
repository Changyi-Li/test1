### Saving
Under this heading you can determine if you want to save and update prices for the parts from the post-calculation. If you do not configure any settings here, only the calculation will be saved for the parts.

#### Save calculation in spite of warning
This setting is activated by default. It means that the calculation will be saved even for the orders that have one or several warnings (under the List tab after calculation). If you deactivate the setting, the calculation will not be saved for these orders.
This determines both if the price will be saved and if the status will be updated to Post-calculated for orders that have a warning. If the setting is deactivated and the order has one or several warnings, the Save alternative will be deselected for the order under the List tab.

#### Update status to "Post-calculated"
The setting is shown if the list type Total by order­ is selected.
It determines if the calculation by default should be marked to be saved for all orders after the calculation is made in the procedure. These orders will be updated to status 5 (post-calculated) when you save the procedure. This status is only updated for orders with status 4.

#### Save from
Here you select the cost or the quote price in the calculation that should be saved as a price type for the parts.
> You can add more rows in the table to save multiple costs/quote prices to several price types for the parts. This can be done in the same calculation.

#### Cost type
With this setting you decide if Reported or Planned cost types should be saved. The default option is Reported cost type. Saving of the Planned cost type to, for example, standard price is useful mainly when the BOM and routing is incomplete and you make many alterations directly on the manufacturing order.
> Please note! You cannot save from planned and reported cost type at the same time since only one calculation is saved with all the included costs.

#### Save to
Here you select the price or the price list of the parts for which the selected cost in the calculation will be saved to.
The alternative called Standard price on linked configured C-order row only applies for configured parts.

#### Price list
Here you can select a price list if a Price list or a Future price list has been chosen to save to.

#### Rate type
Here you can select a rate type to use when the price is saved to a price list in another currency.

#### Number of decimals
The prices that will be saved is by default rounded-off to 2 decimals, but this can be changed. You can here choose to use 0–6 decimals. You can also enter a negative value for decimals, e.g. -2 will round-off the price to the nearest even number of hundreds.
