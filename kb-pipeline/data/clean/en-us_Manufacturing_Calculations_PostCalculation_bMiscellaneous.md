### Miscellaneous
Here you find additional settings for the post-calculation.

#### Show values per unit
This checkbox determines whether the values, after calculation, by default should be shown per unit or with the part quantity on the order based on the quantity of the main part. You can then under each respective tab choose to display the values in the lists per unit.

#### Comparative price
Here you can select a price alternative in order to compare the result of the calculation to another price for the parts. It is the same price that is used to calculate CMThe contribution margin (CM) is the difference between the standard price and the sales price. and CRThe contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. % in relation to the actual costs per unit. The price alternative Customer order/Invoice applies only to the manufacturing orders that are linked to a customer order. If the customer order is invoiced, the price is loaded from the invoice, otherwise it is loaded from the customer order row.

#### Rate type
In this field you select the rate type to use when valuing purchased parts based on a price list in another currency. Rate types must first be registered and activated in the Currencies procedure. The default type is determined by the system setting Default rate type.

#### Print result tabs
In this field you select which lists that you want to include when printing to a printer. By default, only the Summary list will be printed.

#### Number of orders (min./max.)
Here you can select a minimum and a maximum value for the number of orders that must have been manufactured for the part in order for it to be included in the list. This option is available for the list types Part (mean price calculation) and Total by part code.

#### Include already excluded orders
If you check this setting, orders that have already been excluded from the mean price calculation of the parts will be included in the post-calculation. The setting is activated by default if you have selected Total by order as list type, but it is deactivated by default if you have selected Part (mean price calculation) or Total by part code as list type.
Orders that are excluded are orders that you do not want to include in calculation because they are not representative for different reasons, e.g., it can be a prototype order. You can create exceptions from mean price calculation for orders under the List tab (after the calculation has been made, list type Total by order).
