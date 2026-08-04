### Order rows
> When using the EIM Workflow option, the Order rows box is not used. Instead, the order rows are shown as sub-rows for each purchase order in the Purchase orders box.
In the Order rows box you see the order rows including sub-rows for the purchase orders selected to be included in the Purchase orders box.
Here you select which order rows you wish to link to the supplier invoice, alternatively you deselect the order rows that should not be linked. If there are sub-rows, these will always be included in the main row when it is linked. By default, all order rows are selected to be linked. You can also add new order rows. You cannot deselect order rows or add rows if the invoice is already final recorded.
On each order row it is possible to update prices, discount, VAT code, and posting. You can also add new order rows for the supplier invoice. For new rows you can also enter part number, delivered quantity, affect balance, and delivery date. If the system setting Create new location at arrival has been activated, you must also enter location on the new order row.
In the Update price window which you can open using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_update_price.png) button, you can create a new supplier link or select to update different fields on an existing supplier link in the Part register from the inquiry row, the purchase order row, or the supplier invoice row. It is possible to select if this supplier link should be used by default. You can also update standard price. What should be possible to update is determined by the system settings Update supplier link and Update standard price. Please note! It is only possible to do these updates on row type 1.
For an existing supplier link you will see the current values in the column Current, and in the column called New you will see the price of the order row. If you choose to update, then it is the value in the New column which will be saved.
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
If you enter a quantity larger than the quantity in the Delivered qty field you will get a validation error. If you on the other hand enter a quantity lower than the delivered row, the row will be split. The quantity you enter remains on the existing row and a new row is automatically created for the remaining quantity.
At the bottom of the box you will see the invoice amount plus a total of the order amount. There you can also see the difference with and without VAT for the rows that have been selected to be included.
By using the Allocate difference button you can allocate the difference, if any, on the order rows. The difference will be allocated weighted according to the total amount on the rows. The difference is distributed as a percentage to all current type 1 rows. This can be useful if e.g. a general amount has been added to the invoice, an amount that should be distributed and affect all parts on the order.
By using the Final record button you can final code the supplier invoice when you have finished the linking of order rows. You will then be transferred to the Supplier invoice tab, and in the Posting box you can see the posting of the invoice, including the postings that you have created through links to order rows. If you have linked an order subject to receiving inspection, you cannot change the quantity or price on the row. It is also not possible to final record an invoice when the order is subject to receiving inspection.
The part number is displayed in red text on rows subject to receiving inspection.
Under More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you will, for example, see the goods label and find information about who has authorized the invoice and the ordered quantity.
What to consider when linking purchase order for configured purchased parts
When posting costs and when calculating price difference when linking a supplier invoice, the invoice price is compared to the standard price on the purchase order row for configured purchase parts. This applies when any of the following price alternatives has been selected in the system setting called Price difference should compare the invoice's price with: Standard price at arrival or Standard price excl. expenses at arrival.
In systems where the Remote configurator option is installed, the invoice’s price will be compared to the standard price saved on the linked purchase order for the production company. This applies for the price alternatives above which concern standard price.
