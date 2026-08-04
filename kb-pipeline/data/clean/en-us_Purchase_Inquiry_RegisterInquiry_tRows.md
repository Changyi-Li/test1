### Rows
Under this tab you add rows for the parts that are to be included in the inquiry in question, and information regarding them.
The information and functions on inquiry rows and below the rows in the tab, are the same as on [purchase order rows](../../Orders/RegisterPurchaseOrder/tRows.htm). The information that only exists on inquiry rows is described below.
Update price on row
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

#### Position
The position of the first main row is 1, 10, or 100 (as per the Increment of positions system setting) and the next main row to be added will be assigned position 2, 20, or 200 etc.
You are able to manually renumber the positions. Once a position has been renumbered, the position number will be locked. The Recalculate locked positions system setting determines whether locked position numbers will remain the same or be recalculated when position numbers are recalculated on the order.
If the order has status 1 – Registered and you insert a new main row, the position numbers will be automatically recalculated. (Please note that different statuses are applied to different orders, customer orders, blanket orders etc.)
If the status of the order is 2 or 5 and you insert new main rows between two positions, numbers will be assigned between the positions. That way, you can add/insert several new main rows between the positions without them affecting the position numbering of the subsequent rows. When there are no available position numbers left and a new main row is added, the Position numbers when using "Insert new row" system setting determines whether all position numbers will be recalculated or whether you should manually add a position number. If you would like position numbers to be recalculated, in any status, you should select the Recalculate all positions option in system settings.
Only main rows have positions, not sub-rows. To the left of each position with sub-rows you find the following button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/ActiveRow.png). This you can use to expand/minimize the sub-rows. You can use the function button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) in the box to expand/minimize all sub-rows at the same time.
You can sort rows by clicking the column header for Position number. On documents however, rows are sorted by RowIndex, an inbuilt feature that indexes rows in the database. This means that rows on documents are always sorted in the order in which they are registered under the Rows tab.

#### Price alternative
Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can choose to use another price than the one current on the inquiry row. Here you see standard price, supplier's supplier links with price, and supplier's part number. You can select among all of these prices. All properties from the selected supplier link will then be loaded to the row.

#### Delivery date
The delivery date of the inquiry is empty by default. This is the default option since you may not know when you wish to have the delivery of an inquiry. If the delivery date is empty when the inquiry row is turned into a purchase order row, the delivery date of the purchase order row will be set according to the number of days in the delivery time, considering the delivery days and the work days of the supplier.
If you choose a delivery date on the inquiry row, the purchase order row will be given that same delivery date. If the selected delivery date is not one of the supplier's delivery days or not one of the supplier's work days, a warning about this will be shown in the field ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png).
If you have entered a delivery date in past time, you will also see a warning.

#### Purchase order
This check box determines that the inquiry row will be included if the inquiry is turned into a purchase order. If the inquiry row has already been turned into a purchase order, you will not see the checkbox. And in the next column called Purchase order you will instead see the purchase order number.

#### Link to purchase order (L)
If the inquiry row is turned into a purchase order row, you can use this link and open the purchase order in question in the Register purchase order procedure.

#### Exclude from statistics
This check box determines whether or not the inquiry row should be included in the Inquiry list procedure. However, it is possible to show excluded rows in that procedure.

#### Posting
Posting is never mandatory for an inquiry row, but it can be mandatory for purchase order rows. This is configured with the system setting Mandatory posting on order row. If you apply mandatory posting and do not select a posting on the inquiry row, you will get a warning asking you to post the purchase order row after the inquiry row has been turned into a purchase order row.
More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### VAT code
If the row is of row type 1 or 2, the default VAT code for the VAT group on the order will be displayed. If an exception from VAT code has been entered for the part’s product group, you will see that VAT code instead. The VAT code can be changed per row.
The default VAT code for VAT groups and exceptions from VAT code per product group, if any, are entered in the VAT settings procedure.

#### CN code
The CN code (statistical goods code) will be used on the Instrastat report. You can manually enter a CN code for the part on the order row. It is possible to override the part's CN code. Normally, you enter the CN code for the part (in the Part register) and do not change it for row type 1. However, it might be necessary to change for row type 1 for "generic parts" (that is, where one part number is used for several different parts which are one-time-only purchases. This part does not have to be registered in the Part register).
For row type 2 however, it is common to change this code.

#### Transaction type
Transaction types are used for Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. reporting. The transaction type indicates which type if transaction applies to deliveries (of customer order rows and purchase order rows) that are made within EU. It is possible to override the transaction type if you change or set a transaction type on the row. Transaction type and row type 2 work in the same was as for row type 1.
Rules for how transaction types are displayed on the order rows:
1.   
The saved transaction type on the row (for the existing record) is primarily displayed.
2.   
Secondarily, the transaction type based on the order type on the order is displayed. If a link is missing to transaction type for the order type in the Order types procedure, then item 3 applies.
3. Thirdly, the transaction type based on the type that is set as default in the Transaction types – Intrastat procedures is displayed.
Transaction type is also displayed on subcontract purchase orders.
