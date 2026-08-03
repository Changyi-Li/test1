### Saving new calculation
Settings for saving of pre-calculation and price update of parts based on the pre-calculation. If you do not configure any settings here, only the calculation will be saved for the parts. These settings are available for the list type New calculation.

#### Save calculated quantity
With this setting you determine if the quantity entered for the parts under the List tab, should be saved as the parts' calculated quantity. Calculated quantity is not saved by default. You can choose to save the quantity for all parts or for the parts where calculated quantity is missing. Calculated quantity can be saved even if you do not save a price.

#### Save included stock driven parts
This field is available if explosion or recalculation of stock driven M-parts has been selected. By default, the price for included stock driven manufactured parts will not be saved. You can choose to save the prices for all parts or for the parts where calculation is missing. The included stock driven manufactured parts will then be saved in the same way as the main part (according to the lot size for which the calculation was created for each part).

#### Save included order oriented M-parts
This field is available if explosion or recalculation of order orientated M-parts has been selected. By default, the price for included order orientated manufactured parts will not be saved. You can choose to save the prices for all parts or for the parts where calculation is missing. The included order orientated manufactured parts will then be saved in the same way as the main part (according to the lot size for which the calculation was created for each part).

#### Save included fictitious parts
This field is available if recalculation of fictitious parts has been selected. By default, the price for the included fictitious parts will not be saved. You can choose to save the prices for all parts or for the parts where calculation is missing. The included fictitious parts will then be saved in the same way as the main part (according to the lot size for which the calculation was created for each part).

#### Save calculation in spite of warning
This setting is activated by default. This means that the calculation is suggested to be saved also for the parts that have one or several warnings under the List tab after the calculation. If you deactivate the setting, it will not be suggested that you save the calculation for these parts.

#### Save detailed calculation info
Determines the detail level of information that will be saved. If the setting is not activated, only information in the Summary tab will be saved. No detailed information about each operation and material will be saved. Detailed information requires more space in the database.

#### Save even when diff. is 0
This setting is activated by default. If the setting is deactivated, the checkboxes Save calculation and Save price will be unchecked if the difference on the row is 0. These checkboxes will be activated if something is selected in Save from below. Saving calculations even when the difference is 0 requires more space in the database.

#### Save from
Here you select the cost or the quote price in the calculation that should be saved as a price type for the parts.
> You can add more rows in the table to save multiple costs/quote prices to several price types for the parts. This can be done in the same calculation.

#### Save to
Here you select the price or the price list of the parts for which the selected cost in the calculation will be saved to.

#### Price list
Here you can select a price list if a Price list or a Future price list has been chosen to save to.

#### Rate type
Here you can select a rate type to use when the price is saved to a price list in another currency.

#### Number of decimals
The prices that will be saved is by default rounded-off to 2 decimals, but this can be changed. You can here choose to use 0–6 decimals. You can also enter a negative value for decimals, e.g. -2 will round-off the price to the nearest even number of hundreds.
