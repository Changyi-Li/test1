### Order rows
This box shows a list containing the orders that have been arrival reported for the supplier in question. The displayed orders are the ones marked with “Include” in the box above. Here you select which order rows that you wish to link to the supplier invoice in question, alternatively you deselect the order rows that should not be linked. By default, all order rows are selected to be linked.
You can enter prices, discount, setup price, amount, purchase account, etc. on each order row. You can also add new order rows for the supplier invoice. For new rows you can also enter part number, delivered quantity, and if it affects the balance. The prices are displayed in red if they differ from the price on the purchase order.
In the Update price window which you can open using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_update_price.png) button, you can create a new supplier link or select to update different fields on an existing supplier link in the Part register from the inquiry row, the purchase order row, or the supplier invoice row. It is possible to select if this supplier link should be used by default. You can also update standard price. What should be possible to update is determined by the system settings Update supplier link and Update standard price. Please note! It is only possible to do these updates on row type 1. For subcontract purchase order, it is also possible to update the price. Then you can also update existing fields for the subcontract part in the supplier link.
For an existing supplier link you will see the current values in the column Current, and in the column called New you will see the price of the order row. If you choose to update, then it is the value in the New column which will be saved.

#### Supplier link
The following fields can be updated for the supplier link:
- Currency
- Price
- Unit – it is not possible to modify the unit for an existing supplier link. If a new supplier link is created it will get the same unit as the order row.
- Staggered prices
- Setup price
- Discount
- Supplier's part number
- Lead time Number of days between ordering date and delivery date. Normally used for purchased parts.
- Valid through
- Future price
- Future setup price
- Future valid through
- Price comment
- Comment
- Use as default supplier link

#### Standard price
For standard price you will see the current standard price in the column Current and you can enter a new standard price in the New column.

#### Other prices
Here you see the prices from the price log in the Part register.
At the bottom of the box you will see the invoice amount plus a total of the order amount. There you can also see the difference with and without VAT for the rows that have been selected to be included.
By using the function button Allocate diff. you can allocate the difference, if any, on the order rows. The difference will be allocated weighted according to the total amount on the rows. The difference is distributed as a percentage to all current type 1 rows. This can be useful if e.g. a general amount has been added to the invoice, an amount that should be distributed and affect all parts on the order. The order rows that have been linked are automatically added as posting rows to the Posting box under the Supplier invoice tab.
