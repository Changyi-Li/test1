### The Rows tab
Under the Rows tab you can add rows for the parts to be sold in the customer order in question and information regarding them.
You can add rows on different levels. E.g. a part row on level 0 with associated alloy cost or an additional text on level 1. Another example can be a fictitious part on level 0 with included parts on level 1. Level 0 is called main row and level 1 is called sub-row, underlying row, or underlying level. Please note! Fictitious parts cannot be entered on sub-rows.
If the row is a text row (row type 4) you can in the text editor choose on which documents the text row should be shown (text type). There are four different text types for text rows that determine on which documents the text rows should be printed. On additional text rows you can also insert phrase and insert signature by using the buttons on the function menu.
By using the button called Show on the following documents ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_all_docs.png) on the text row, you can click to decide on which documents the additional text row should be displayed.
It is not possible to enter a negative quantity for parts on row type 1. However, this is possible to do on additional order rows (row type 2). On row type 1 you should instead enter negative price each on the rows to reach the same effect.
At the bottom of the tab there is a [summary](bSummaryOfRows.htm) of the order rows.
There are different system settings that affect the order rows on a customer order. Read more about these in the online help function to the System settings procedure, under the section [Order/Quote](../../../GeneralRegisters/BasicSettings/SystemSettings/bOrderQuote.htm).
Check delivery times
If you apply Check delivery times (CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.), which is activated with a system setting, you find the button CDT ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) at the bottom of the tab. By clicking it you can see the default settings for CDT. These settings are configured to be default using different system settings. But you can change the settings temporarily here for the order rows and then do a new calculation with the button Rerun CDT ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png) (Ctrl + R) on the function menu. If you restart the procedure, these CDT settings will be reset on the order according to how they are configured in the system settings. This also means that changed settings will not be saved on order row level.
When CDT is applied, you also find the following columns on the order rows: Earliest delivery date, Difference, and the button CDT. Read more about these below.
Read about [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using Monitor in the online help function.
Customer order transfer
If you have installed the Customer order transfer option, you can use the CDT in remote company button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_balance_prod_company.png) to check the part's balance in the production company. If you also apply CDT in the production company, a CDT will run in the production company and generate suggestions in the sales company.
If you are applying Customer order transfer, you also see the columns called Transfer profile, Transfer status, Transferring comp.'s order no., Transferring comp.'s order row pos., Transferring company's reference, and Transferring comp.'s "Customer's part no." on the order rows. Read more about these below.
Rows that are added to customer order in the production company can be automatically transferred to the sales company.
> If you have added a remote configured part on an order row, this means you can no longer change part on this order row. If you would like to exchange a remote configured part on an order row you have to delete the existing row and register a new row.
Modifications of delivery date, quantity, price, and discount, on the customer order can be transferred to the sales company. A dialog is displayed when you save, and you can there choose if the modification made should be transferred. Modifications of price and discount will only update the related purchase order in the sales company and are also decided by the Price each setting under the Sales Company tab in the Settings for customer order transfer procedure.
Please note! When a customer order row is remote configured, the quantity field is ghosted. The quantity is instead shown in the remote configuration window.
This function facilitates matching of supplier invoices between the companies.
Read more about how customer order transfer works if you are using invoicing plans and [what you should keep in mind](../../../GeneralRegisters/CustomerOrderTransfer/SettingsForCustomerOrderTransfer/bHeader.htm#Arbetssätt_för_att_hantera_faktureringsplan).
The Function menu
The function menu on customer order rows contains a few specific buttons which are described below. These are available in addition to the buttons used to: add, insert, and delete rows, add underlying level (row type 4), insert signature, insert phrase (row type 4), expand, go to procedure, and find & replace.
You can [read more](../../../UserGuide/Interface/FunctionsMenu.htm) about all buttons on the function menu here.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) – Split row (copy row) (Ctrl + Shift + C). With this button you split an order row to a new order row. Please note! Sub-rows for alloy cost will be copied only if the Alloy cost setting in the customer register is set to create alloy cost at order registration. Packaging is not added when you split row since these rows are created at Report delivery. If you have selected the option Split, with dialog in the system setting Function of “Split row” button in Register customer order, the [Split row dialog](bSplitRow.htm) will be shown and you will be given multiple options for how the splitting will be performed..
> If you delete a split row, the quantity on the original row will be restored.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) – Use the dates suggested by the CDT. If you apply CDT, you can with this button apply the earliest finish date calculated by CDT as delivery date. You can choose to do this for the order row in question or for all order rows.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png) – Rerun CDT (Ctrl + R). If you apply CDT, you can with this button rerun the CDT if you for example want to test other settings under the Settings for CDT button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_balance_prod_company.png) – Balance in prod. company. If you have installed the option Customer order transfer, you can use this button to check the part's balance in the production company. If you also apply CDT, this will run in the production company and generate suggestions in the sales company.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_total.png) – Edit total. If the row is a total row (row type 3), then you can use this button to open a dialog window and there you can edit the total of the included order rows.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_to.png) – Recalculate order inflow. Using this button you can recalculate order inflow for a separate order row or for the entire customer order. The current order inflow records will be deleted and new records will be created taking the order rows’ current data such as prices, quantity, and discount, into consideration. Order inflow records will receive the date on the log record according the the order row’s registration date and/or the changed date from the changelog.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) – Disconnect linked order. If the order row is inked to a manufacturing order or a purchase order, you can with this button disconnect the order row from the linked order. You confirm this in a dialog box. Disconnecting from customer order row means the linked order becomes available for other requirements and that clearances made against the customer order row, if any, will be deleted. It is not possible to disconnect an order when the pick list has been printed via the Delivery planning procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_hidden.png) – Show rows with final delivery made. If there are order rows where final delivery has been made, you can choose to show these using this button. By default, rows with final delivery made are shown. The next time you open the procedure, the button will be in the mode you left it in. If you restart the Monitor ERP client, the button will return to the original mode.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PadlockUnlocked.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png) – Lock/Unlock “Price each” and “Discount”. This setting makes it possible to temporarily lock/unlock Price each and Discount for all rows on a quote or a customer order. This is activated with the system setting called Enable temporarily unlocking "Price each" and "Discount".
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_update.png) – Recalculate positions (Ctrl + Shift + O). Recalculates positions on the order. The system setting Recalculate locked positions determines if manually edited (locked) positions will be edited.

#### Position
The position of the first main row is 1, 10, or 100 (as per the Increment of positions system setting) and the next main row to be added will be assigned position 2, 20, or 200 etc.
You are able to manually renumber the positions. Once a position has been renumbered, the position number will be locked. The Recalculate locked positions system setting determines whether locked position numbers will remain the same or be recalculated when position numbers are recalculated on the order.
If the order has status 1 – Registered and you insert a new main row, the position numbers will be automatically recalculated. (Please note that different statuses are applied to different orders, customer orders, blanket orders etc.)
If the status of the order is 2 or 5 and you insert new main rows between two positions, numbers will be assigned between the positions. That way, you can add/insert several new main rows between the positions without them affecting the position numbering of the subsequent rows. When there are no available position numbers left and a new main row is added, the Position numbers when using "Insert new row" system setting determines whether all position numbers will be recalculated or whether you should manually add a position number. If you would like position numbers to be recalculated, in any status, you should select the Recalculate all positions option in system settings.
Only main rows have positions, not sub-rows. To the left of each position with sub-rows you find the following button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/ActiveRow.png). This you can use to expand/minimize the sub-rows. You can use the function button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) in the box to expand/minimize all sub-rows at the same time.
You can sort rows by clicking the column header for Position number. On documents however, rows are sorted by RowIndex, an inbuilt feature that indexes rows in the database. This means that rows on documents are always sorted in the order in which they are registered under the Rows tab.

#### Delivery status
If nothing on the row is delivered, the column is empty. If a delivery is reported, a symbol is displayed for delivery status according to the following:
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPartiallyShipped.png) – Partial delivery made
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusDeliveredOpFullyShipped.png) – Final delivery made.

#### Row type
Here you can see/enter the row type of the order row. Row type 1 is entered by default when registering a new order row. The following row types exist for customer orders:
- 1) Part row – This row type can only contain parts that are registered in the part register (manufactured, purchased, fictitious parts, and services). When you have entered or selected a part number, data from the part will be loaded on the row. Part number is mandatory. If you have added an order row of row type 1, and then not entered or selected a part number, you will see an error symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) in the part number field, and in that mode you cannot save the order, until you fill in the part number.
- 2) Additional order row – This row type can also contain parts that are not registered in the system. Information about the part can be filled in manually. The part number is not mandatory but the name is. An error symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) will be displayed in the name field, and in that mode, you cannot save the order until you have entered a part name.
- 3) Total row – This row type is a total of the rows (row type 1-2) on the preceding positions. The total price for the rows can be entered in a dialog window. In the dialog window you can also uncheck the Include box for rows that should not be included, starting with the first position. New amounts are calculated based on the total price and are shown per row, the existing discount will not be taken into consideration. All rows in the total price will get the same discount in the order row’s Total row’s discount (code 3). The new amounts will update the statistics. On linked documents (quote, order confirmation, and invoice) price each, new calculated discount rate or amount, will not be shown on the rows included in the total price. It is possible to have multiple total rows per order. Part rows and additional order rows, which are added after a total row, will not be included in the calculation but will be added to the order's total. If total rows (row type 3) are added to orders, or if changes are made that affect the currency on the order, a validation message is shown stating that the total row needs to be updated manually. Partially or final delivered total rows cannot be edited. To edit a partially or final delivered total row, the delivery must be undone. If the currency is changed on an order, the total row needs to be manually updated. A validation will be displayed as a reminder of this. If a total row is added on customer order and it has been delivered (partially or final), it is not possible to make changes for this total row or the order rows it contains on the customer order or on the invoice basis. In order to make changes, the delivery must be undone.
Read more about [fields in the total window](FieldsInTotalWindow.htm).
- 4) Text row – This row type is intended for formatted text you enter on the row. A text row can be a sub-row and in that case it is linked to a main row of row type 1 or row type 2. If the text row is not a sub-row, it is not linked. It then means it belongs to the actual order, not to a specific row. A linked text row will be included to the delivery reporting each time the main row is delivered. An unlinked text row will only be included to the delivery reporting the first time a main row is delivered.
In systems with the Customer order transfer option, the formatted text in row type 4 will be transferred. This way all formatting and also images will be transferred.

#### Show on the following documents
For row type 4 you can click this button and select on which document types the additional text row should be shown. You can select among Quote, Order confirmation, Delivery note and Invoice. All document types are marked by default. By using the checkbox at the top you can also select/deselect all documents at the same time.

#### Delivery progress
By clicking this button you access information about in which phase of the delivery process the order row is. The Delivery progress window shows all pick lists which have been created for the order row and you can also see if the pick list/pick lists are being used for picking at the moment (via Monitor Mobile), packing, or has been sent.
The phase view shows the following phases:
- Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. created
- Picking
- Packing
- Shipping
- Delivery
If an order row is in progress in one of the phases, this is indicated with a light blue color. If the phase is completed, this is indicated with a dark blue color.
At the top of the window you see information about the entire row quantity, picked quantity, packed quantity, delivered quantity, etc. In the table you see information per pick list since an order row can be divided into multiple pick lists. In addition, you also see delivery note number, shipment number, and actual delivery date.

#### Part
Here you enter the part number for the order row. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard.feature, you can search the part register for parts.
For row type 2, you can also leave the field empty or enter an optional part number. If you enter a blank space (space bar) before or after the part number, this will be deleted when you leave the name field on a new additional order row.
If it is a fictitious part on a new order row, a dialog window will appear when you have selected the part. There you can enter quantity, unit, variant code, and delivery date for all parts included in the fictitious part. If the fictitious part has the sales setting Show structure when registering orders activated in the part register, you will instead see a dialog window where you see the part structure and if there are any other included fictitious parts in it. In the dialog window you can modify the material list for each fictitious part in the structure and enter quantity and discount for each included/incorporated part in the material list. You can also add or delete parts in the material list.
If the part on a new order row is linked to a configuration group, a configuration window is automatically opened when you have selected the part. This applies in cases where the setting Open automatically is activated for the part. Otherwise you open the configuration window by using the button Configuration on the order row (see below). In this window you configure the part on the order row according to the customer's wishes.
For row type 4 you here find a text editor where you can write and format texts and insert images. In the part register it is possible to enter a comment in the customer link. The comment is shown on this row if it has been set to be displayed on order confirmation. By clicking the Show on the following documents button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_documents.png) you will see on which other document types this additional text is selected to be displayed. The same button is also available directly on the additional text row If there is no comment in the customer link, but the part has a general sales comment, then this will instead be shown in the same way as described for the comment in the customer link.

#### Name
For row type 1, the part name is automatically loaded from the part register when you have entered the part number, but it can be changed on the order. In case the part name is not translated to the language of the mailing address and delivery address, the name will be displayed in the user's language. This also applies to order confirmations and delivery notes.
For row type 2, the name field will be empty if you have entered a part number that is not registered, but the field is then mandatory and you need to enter a part name, preferably in the language of the mailing address.

#### Part type (T)
This column shows a symbol for the type of part loaded on the row. Read more about [part types in the Part register](../../../Stock/Parts/PartRegister/hPartRegister.htm#Artikeltyp).

#### Lot sizing rule (LSR)
This field shows the part's lot sizing rule. There is no lot sizing rule for services. The lot sizing rule is displayed as a letter according to the following:
- LL – Lot-for-lot.
- LR – Linked requirement.
- FQ – Fixed order quantity.
- PR – Period requirement.

#### B/N (Block/Notify)
In the Block/Notify column you see if the part is blocked or if there is a message regarding registration of customer order. It is possible for you to edit a customer order containing blocked parts if the customer order was created prior to when the part was blocked. However, you cannot add new rows with the blocked part.

#### Quantity
The quantity of the part. The field displays two decimals by default, but it is possible to enter up to six decimals.
For row type 1, quantity must be greater than zero. For row type 2, quantity can be negative but not zero.
There are three system settings for quantity of the part that can be activated for different checks according to the following: Check quantity on order/quote against quantity/package, Check quantity on order/quote against minimum quantity for warehouse, and Check quantity on order/quote against the part's quantity for lead time.
If the part has partial quantities, you cannot enter a quantity in the field. You should instead use the Partial quantities button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) on the order row to enter a quantity.

#### Unit
For row type 1, you here see the part's default unit. If there are more than one unit registered for the part, you will see the unit marked for customer order under the button Default units/usage in the Part register. You can change to another unit if there are several units registered for the part. If you change to another of the part’s units you will be asked if the quantity should be recalculated according to the entered conversion factor. The price each will also be affected if you change the unit. Unit is mandatory for row type 1.
For row type 2, no unit will be suggested, but you can select among all units in the system. By clicking the X button next to the Unit field, you can delete the unit on this row. It is optional to enter a unit for row type 2.
The unit is always displayed in the user's language. On printouts of order confirmations it is displayed in the language of the mailing address. On printouts of pick lists it is displayed in the user's language. On printouts of delivery notes it is displayed in the language of the delivery address.
The unit cannot be changed if the order row has status Partial deliver made or Final delivery made.

#### Price each
Here you can see the part’s price each. The price is always excluding VAT, regardless of whether the order is intended for a corporate customer or a private person/private customer. However, if the customer is a private person, you can show the price including VAT on the order.
The price each can be set to zero, which can be useful when you cannot confirm the price. With the system setting called Handling of "zero price" on row you decide what should occur if there is no sales price for a part. Depending on how you configure the system setting, a warning will be shown, a block will be applied, or nothing should happen.
For row type 1, the price loaded on the row is determined by the price strategy selected for the order type (in the Order types procedure):
- Price list – This option means the price list selected in the Order types procedure, will be used.
- Standard price – This option means the standard price on the part will be used.
- According to customer – This means that the price will primarily be loaded from the customer link. If there is a staggered price in the customer link, this will be used in cases where there is a staggered price matching the quantity on the order row (if the price has been loaded from staggering prices, the price is displayed in italics). If the quantity on the row is less than the lowest staggered price, the normal price in the customer link will be used. If there is no customer link or if no price is registered in the customer link, the price list on the part that the customer is linked to will be used instead. If there is no price in the price list, the suggested price will be zero. Regarding the customer link, it refers to the customer on the order, not the customer in the Customer number on invoice field.
The suggested price for row type 2 is always zero for parts that are not registered in the Part register. If the part is registered in the Part register, the loading of prices to the row will work in the same way as for row type 1.
A warning will be displayed if the currency of the price list is does not match the currency on the order. The price will then be converted to the currency used on the order.
If the price has been loaded via staggering, the price will be displayed in italics. You must always enter a price in the Price each field on the customer link in the Part register in order for the staggered price from the customer link to show on the order row. If you do not enter price, the price will be shown as 0.00.
If you manually enter a price each, the field will become locked ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png). But it is possible to unlock the field by clicking on the padlock button, making it change symbol to unlocked ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PadlockUnlocked.png). When a customer order is assigned status Final delivery made, the field becomes locked.
The number of decimals is determined by how many decimals have been entered in the system setting Number of decimals in price on quote, customer order and invoice.
If the selected part on the order row is linked to a configuration group, the price each is loaded from the configuration. If there is a Configuration price list selected on the customer, then this price list will be used for parts that can be configured. The price can either be net price or gross price plus discount. This is determined with the system setting Total of price on order row.

#### Price each including VAT
By activating Price each including VAT it is possible to enter a price including VAT. By entering a price including VAT, the price will be changed to price each excluding VAT.
By using the calculator function in the Part register procedure you can calculate which appropriate price the part should have if you want a specific price including VAT.

#### Price alternative
Under the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button you can choose a different price alternative than the one that is current for the order row. The price alternatives here are the price lists registered in the Price lists procedure. It is also possible to choose the customer price alternative (from the customer link on the part) or the standard price. If there is staggered prices in the selected price alternative, the staggered price is entered automatically based on the entered quantity of the part on the order row.

#### Partial quantity
If the part has partial quantities, the Partial quantities button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) is shown on the order row. By clicking this button you can see the registered partial quantities of the part. You can enter a quantity of one or multiple partial quantities and quantity from each partial quantity, as well as link a packaging part for each partial quantity. It is also possible to add/delete rows of partial quantities.
Packaging parts that are selected for partial quantities will become default in packaging structures for pick lists that are created in the Delivery planning and are shown in the Pack for delivery procedure.
If the part on the order row has the control method set to Order oriented and you create a linked manufacturing order or linked purchase order (depending on part type), that order will by default be assigned the same partial quantity as on the customer order row. If you then change the partial quantity of the customer order row, a dialog is shown where it is default to also update the linked order.
Quantity x the partial quantity’s Quantity are added together and entered in the quantity field of the order. It is not possible to make changes in the quantity field on the order if there are partial quantities. The number of partial quantities you have entered under the button will only be saved on the order, not for the part.

#### Configuration
If the selected part on the order row is linked to a configuration group, the Conf.column is shown. This column contains a button for configuration of the order row. If the button has this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Available.png) it means the order row is not configured. Then it will not be possible to save the order. By clicking this button you access a configuration window where you can configure the part. When you confirm the configuration using the Confirm button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) in that window, the symbol on the button will change. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png) illustrates that the order row is configured. Then it is also possible to save the order. Read more about [the configuration window](../../../UserGuide/Using/Configurator/ConfiguratingWindow.htm).
The part can have be set to automatically open the configuration. In that case the configuration window will open as soon as you have selected the part on the order row.
The part can also have a default configuration determined in the part register. In that case this will automatically be loaded to the configuration window.
When you save the order, a pre-calculation is also saved for the configured part, based on the quantity entered on the order row.

#### Price comment
The ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_information.png) symbol is shown and the price comment is shown in the validation window if a comment has been entered for the price alternative.

#### Discount
The discount that applies for the part on the row. For row type 1, the discount will be suggested based on the following rules:
1. Discount on customer link
2. Discount from discount category
3. Discount on customer.
For row type 2, you can manually enter a discount for the row if the part is not registered in the Part register. If the part is registered in the Part register, the loading of discount will work in the same way as for row type 1. It is also possible to enter a different discount on the order row in question. This can be done for all row types. The discount is always entered in percent. It is possible to enter a negative discount. If row type 3 is used, the discount rate will be negative in case the total on the row is greater than the included/incorporated rows’ actual total.
If the order row is part of a total row (row type 3), or if an order discount has been added on the order, there may be multiple discounts for the order row. The row’s total discount rate will then be displayed in this column, and the field will be ghosted and not editable.
If you manually enter a discount, the field will become locked ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png). But it is possible to unlock the field by clicking on the padlock button, making it change symbol to unlocked ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PadlockUnlocked.png). When a customer order is assigned status Final delivery made, the field becomes locked.

#### Discounts
Clicking the Discounts button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_discount.png) opens a window that displays the row’s various discounts. There are four different discounts: Discount (code 1), Order discount (code 2), Total row’s discount (code 3) and General project discount (code 4) , Order type discount (code 5), and Discount on discount (code 6).
Discount is the discount that comes from customer link, discount category, or customer (see rules under Discount above). Discount is editable. This discount has priority 1. This means that it will always be calculated on the order row’s original price each.
Order discount is the discount entered or calculated based on the entered order value in the order footer. This discount has priority 10, meaning that it will be used last when calculating Price after discount.
Total row’s discount is the discount entered or calculated based on the entered total for a total row (row type 3). Order discount and total row’s discount cannot be used on the same order.
General project discount is the discount that has been entered on the project linked under the Header tab. This discount is automatically given priority 40 and is editable. It can be set to 0 if you don’t want a customer order row to have this discount.
Order type discount is the discount that has been entered on the order type. The priority for this type of discount can be changed.
Discount on discount. The priority for this type of discount can be changed.
This window can be opened by using the shortcut key Ctrl + Shift + 5.
If you activate the button Keep on top ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/KeepOnTop.png), the discounts window will remain open and in the same place as long as the procedure is open. Switching between order rows updates the discount rows in the discounts window. The discounts on the selected order row will be displayed in the window.
Using the button Remember size and position of window ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SaveWindowImage.png) lets you decide how large the discounts window will be, and where on the screen it will be placed.
You can change the size and the placement of the columns. Using Save layout ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_layout.png) in the procedure’s menu, you can save the changes that have been made.
Columns in the discounts window
- Name – displays the name of the discount.
- Code – displays the code of the discount.
- Priority – displays the priority of the discount.
- Price each – displays the original price each that has been entered on the order row.
- Percent – displays the discount in percentage.
- Apply – if the discount should be applied on the order row, the Apply checkbox should be checked. If the discount should not be applied on the order row, the Apply checkbox should be unchecked. The discount will remain, but it will be excluded when calculating the overall discount.
- Copy to all rows – copies the values for the Percent, Priority, and Apply columns to all the rows on the order.
- Discount amount – displays what amount the discount percentage represents in the currency on the order.
- Price each after discount – displays the price each after the discount has been applied. Price each after discount for the first discount will be the price each before discount for the next discount on the order row.
Totals for discounts given are shown in the footer.
- Price each before discounts – shows the original price, meaning the price each on the order row.
- Price each after discounts – shows the final price each after the discounts have been applied.
- Total discount in percent – shows the total discount rate for the order row in percent.
- Total discount amount – shows the total discount for the order row in the order’s currency.

#### Setup price
The setup price for the part on the row. For row type 1, the setup price entered for the customer in customer link of the part will be suggested, otherwise the field is empty. For row type 2, the field is always empty if the part is not registered in the Part register, but you can enter a setup price. If the part is registered in the Part register, the loading of setup price will work in the same way as for row type 1.
The number of decimals is determined by how many decimals have been entered in the system setting Number of decimals in price on quote, customer order and invoice.
When a customer order is assigned status Final delivery made, the field becomes locked.

#### Delivery date
For row type 1 and 2, it is here possible to enter a date for the planned delivery. You can only enter a delivery date on main rows, not on sub-rows (such as alloy costs). This is normally the customer’s desired delivery date. The date is shown in italics if the order has been changed which resulted in the current date not being the same as the initial date.
The system setting Default delivery date on order rows determines if the suggested date should be Today (today's date) or Today + lead time. If you add new order rows, they will get the same delivery date as the order row above. If Today + lead time has been selected in the system setting, then the delivery date will primarily be based on the lead time in the customer link of the part, and secondarily it will be based on the part's lead time to customer. If no lead at all exists on the part, then today's date will be suggested. If you manually enter a delivery date within the part's lead time, a warning will be shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png).
The dates that can be suggested are also determined by what has been entered as delivery days on the customer. The week days configured as the customer’s delivery days can be selected for the customer in the Customer register procedure. A warning will appear if you enter a delivery which does not correspond to one of the customer’s delivery days. The customer’s delivery days are also displayed at the bottom of the tab.
The suggested date is also checked against the national calendar. If you change the delivery date to a non-working day, a warning will appear. A check regarding the entered delivery date is also made in order to see that it is not a date in past time. If you have entered a date in past time, you will see a warning.
If partial delivery is not allowed in the delivery rules of the order, the same delivery date must be entered on all the rows. If the rows have different delivery dates, the delivery date will be marked with an error symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) on the rows that differ from the delivery date on the first row. A tooltip on the error symbol shows a text stating that the delivery date must be the same on all rows when partial delivery is not allowed. In that mode, you cannot save the order until those rows have the same delivery date as the first row.
It is possible to leave the date empty. This can be useful if you cannot confirm the delivery date. With the setting Show delivery date under More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you determine if the delivery date for the row should be shown. If the Show delivery date is not marked, a text is shown on the order confirmation, saying that the delivery date cannot be confirmed and that the delivery date will be confirmed shortly. This text is possible to edit in the Document texts procedure. Order rows without confirmed delivery dates are not included in the requirements planning and you cannot create any manufacturing orders or purchase orders based on those order rows.
> Order rows without a confirmed delivery date cannot be delivered.
If you are using the check delivery times function (CDT), you can also use the delivery date suggested by the CDT calculation (see the following three columns). Read more about the [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using Monitor in the online help function.

#### Delivery date incl. transport
Here you see the delivery date including the transport time. The transport time is loaded from the Transport time Transport time is the number of work days that it takes to send a shipment from sender to a receiver. field below the Rows box. If you change the transport time in the Transport time field, the "Delivery date incl. transport" will be updated.

#### Earliest finish date
In this column you can see the earliest possible finish date according to the CDT calculation. If it is possible to deliver the order row on the entered delivery date or earlier, the earliest finish date is displayed in green color. If the earliest possible finish date is a date after the entered delivery date, the earliest finish date is displayed in red color.
Using the Use the dates suggested by the CDT button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) on the function menu, you can choose to apply the earliest delivery date to the Delivery date field. If you click the button, there are two alternatives. You can here choose to apply earliest delivery date to the selected order row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) (Ctrl + D) or to apply the date to all order rows ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace_all.png) (Ctrl + Shift + D).
However, you should be aware that if partial delivery has been set to Not allowed under the button Delivery rules on the order, the it is not allowed to have different delivery dates on the order rows. In that case you can only use the alternative which means that earliest finish date will be applied for all order rows. The delivery date will then become the date when all rows can be delivered at the same time, that is, the order row with the "latest" Earliest finish date controls which date that will become the delivery date on all order rows.

#### Difference
Here you can see the difference between the suggested delivery date and the earliest delivery date. The difference is shown in number of work days, and in the same color as in the preceding field.

#### CDT
The button in this column has a symbol which indicates how the order row is supplied, or what the action is to supply it. A tooltip over the button displays the same in text.
If the CDT has selected an alternative supplier or work center for the order, you will will also see an asterisk (*) on the button. This information will also be included in the tooltip available on the button.
If you click on the button you will see a result window from the CDT. There you can e.g. see the CDT's planning window. Depending on how the order row is supplied, you can also see purchase order suggestion, manufacturing order suggestion, order information, and a loading chart. You can used the result window to investigate where there are critical operations/material, that is, the operation or material that determines which the earliest delivery date can be.
In the Summary table at the top part of the result window, you can on the first row see the entered delivery date on the order row. On the next row you see what will be the earliest delivery date if the standard work centers are used, and also the order rows Contribution margin and Contribution ratio. On the third row you can see which the earliest delivery date will be if the alternative suppliers and work centers selected by CDT are used. You will also see the order row’s Contribution margin and Contribution ration will be in that case. If there are alternative suppliers or work centers selected by CDT, then you can check the Apply box on the third row if you wish to use that alternative. If you do not check this box, the standard work centers will be used. By using the button Confirm ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) you confirm which row that should be used. The result window will then close and the finish date of that row will be loaded to the Delivery date field on the order row.
Read about [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using Monitor in the online help function.
> Please note that an alternative supplier or work center selected in the CDT will not be included if you select to create a manufacturing order for the order row by checking the box in the M-order column on the order row when you save. This applies regardless if you have selected to use the alternative supplier/work center in the window Result from CDT. Instead, the supplier or work center that is standard will be used. On the created manufacturing order you can afterwards manually change supplier or work center to the alternative that the CDT selected.

#### At customer
The Delivery date plus the Transport time is by default the date At customer, that is, when the part on the row should have arrived at the customer’s location. This date can be changed. The column is only shown if the system setting Show delivery date "At customer" on order row/quote row is activated. It is suitable to enter the same date in this field as what has been stated on the order from the customer, if there is a date on it for when the delivery should arrive at the customer's location.

#### Amount
In this column you will see the order row's total amount according to the formula: Quantity × Price each − Discount + Setup price. The amount is shown in the currency of the order.

#### Serial number
Under the Serial number A serial number is a number that is used for traceability for parts on entity level. button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can enter both individual serial numbers and intervals of serial numbers. If a serial number has been entered here then you see the following symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png).
Serial numbers can be created manually by entering From serial number and Quantity. You can also enter a remark for each serial number or interval of serial numbers. A check is made to see that the entered serial number does not already exist linked to parts on other orders. Serial numbers can also be created automatically from a number series if you for the part activate a setting to generate serial numbers when registering customer orders.
The quantity of serial numbers must be the same as the quantity of the part on the row. If the total quantity of serial numbers does not match, you will see an error message in the Quantity field, and you cannot save the order.
If you create a manufacturing order from the customer order row, then the serial number will be loaded to the manufacturing order.
Please note! Serial numbers should not be created on customer order rows for stock driven parts with traceability at serial number level. Serial numbers on customer order rows should be used in cases where you need to link a serial number as an ID for a product you are selling, normally an order oriented part. The product as an entity will then be saved in the Serial number/Batch A batch is the set of components/products manufactured at the same time and made from the same original material. procedure, where you can add additional information for new sales, after market, etc. But you will not have traceability back to a purchase with this serial number.
But traceability at serial number level on the other hand, means that a serial number is created for each entity of a part during arrival reporting, either from purchase or from manufacturing. In that case a serial number must be manually entered or imported from a file at arrival to location, for each entity of the part. If you for example arrival report 10 pieces of purchased parts with traceability at serial number level, then 10 serial numbers must be created. The serial number is then tied to the part and will be used on the customer order and at delivery reporting. This way, it is possible to trace the part back, from sales too the part which was purchased by the supplier. This requires traceability throughout the entire chain, that is, all parts where the part is included must also have traceability at serial number level. These serial numbers are also saved in the Serial number/Batch procedure and there you can add additional information to each serial number.

#### Balance
In this field you can see the part’s current stock balance for the selected warehouse on the row in question. However, stock balance is not displayed for parts of type Service and the parts that are not stock updated. With the system setting Show disposable balance on order row/quote row, you can determine if this field should be displayed, regardless of part type.

#### Disposable balance
Here you see the disposable balance The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. for the part. However, disposable balance is not displayed for parts of type Service and parts that are not stock updated.
The system setting called Show disposable balance on order row/quote row determine if and how the disposable balance should be displayed: for order row's delivery date, for all reservations, or for all reservations and orders.

#### Included in invoicing plan
If you have selected an invoicing plan for the order and the row should be included in an invoicing plan, then you should check this box. Invoicing plan is shown if the system setting Handle invoicing plans on quotes/customer orders is activated.

#### Manufacturing order
Here you can select to create linked manufacturing order from a customer order row. For the rows where the checkbox M-order is checked (and are not yet linked to any manufacturing order) new manufacturing orders will be created when you save the customer order. If the checkbox in the column heading is checked, all the rows will be selected and create manufacturing orders. In the column M-order/P-order you will then see the manufacturing order numbers created based on the rows.
It is also possible to create a manufacturing order based on a stock updated part. In the Part register and Part list procedures, you can for the part configure that it is allowed to create manufacturing order from customer order. If the row is saved for such a part, the registration will open where the manufacturing order is possible to edit.
If it is a configured part, the manufacturing order which is created will inherit the configuration you find under the button Configured ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png) on the customer order.
The following changes on the customer order can affect the replanning of the manufacturing order:
- Delivery date
- Quantity
- Revision
- Configuration
- Priority on customer order
- Warehouse
- Variant code
> If you are using the check delivery time function (CDT) it is recommended to always create manufacturing order from customer order row. Then the Continuous net requirement calculation should be activated in the Net requirement calculation You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. procedure.
Read more about creating and updating the manufacturing order from customer order rows.
It is possible to automatically create manufacturing orders for order oriented manufactured parts on customer order rows. The row type must be 1 and a delivery date must have been selected/entered.
The system setting Create manufacturing order when creating/editing customer order determines if the check box M-order will be checked by default on the customer order row.
The system setting M-order number is created determines whether the manufacturing order number will be created from a number series or as customer order number + position number of the customer order row in question.
The information included from the customer order/customer order row to the new manufacturing order in the Register manufacturing order procedure is:
- Order type – This will be the same as on the customer order.
- Prefix – This will be the same as on the customer order.
- Part number – This will be the same as on the customer order row
- Quantity – The manufacturing order is only registered in the part's default unit, so if another unit has been used on the customer order row, the quantity will be converted to match the part's standard unit.
- Finish date – This will be the same as the current delivery date on the customer order row minus the safety time registered for the part, if any.
- Priority – This will be the same as on the customer order.
- Revision – This will be the same as on the customer order row.
- Customer order – This shows the customer order number of the linked customer order.
- Customer – This shows the customer of the linked customer order.
- Project – This will be the same as the project in the posting on the customer order row.
- Variant code – This will be the same as on the customer order row.
- Warehouse – This will be the same as on the customer order row.
In the Register manufacturing order procedure it is not possible to edit the information on the it order which was loaded from the customer order, except for the finish date. If you wish to edit information such information on the manufacturing order, this must be done on the customer order in Register customer order.
If you change quantity or delivery date on the customer order row and save, the Register manufacturing order procedure will automatically open with the new quantity/date suggested on the linked manufacturing order. There you can select if you want to replan the order with the new information by saving the procedure.
On the customer order row it is also possible to disconnect a linked manufacturing order. This is done via the button Disconnect linked order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) on the function menu. This can be useful if you for different reasons want to undo a linked manufacturing order, for example to replan a quantity without having to change the quantity on the customer order, get rid of locked clearances to make it possible to delivery report the customer order row. When a manufacturing order is disconnected it is also possible to undo reporting items made on it.

#### Purchase order
Here you can select to create a linked purchase order from a customer order row. For the rows where the check box P-order is activated (and that are not yet linked to any purchase order) a new purchase order will be created when you save the customer order. If the check box in the column heading is activated, all the rows will be selected and create purchase orders. The created purchase order is displayed in a dialog. In the column M-order/P-order you will afterwards see the purchase order numbers created based on the row.
Read more about creating and updating the purchase order from customer order rows.
It is possible to automatically create purchase orders for order oriented purchased parts on customer order rows. The row type must be 1 and a delivery date must have been selected/entered. The purchased parts must also have a supplier link. If there are several supplier links, the default link will be used.
The system setting Create purchase order when creating/editing customer order determines if the check box P-order will be checked by default on the customer order row.
> The setting Purchase order's address (in the Customer order tab in the Order types procedure) determines if the delivery address on the purchase order will be the company’s delivery address (our supplier sends us goods) or the customer order’s delivery address (our supplier sends goods directly to our customer).
When the customer order is saved for the first time you will see a dialog with information about the linked purchase orders that have been created for each respective the customer order row. There you can print all the purchase orders directly or open them per order in the Register purchase order procedure.
The information included from the customer order/customer order row to create new purchase orders is:
- Order type – This will by default be the order type entered for the user.
- Goods label – This will be the customer order number.
- Part number – This will be the same as on the customer order row
- Quantity – The purchase order is only registered in the part's default purchase unit, so if another unit has been used on the customer order row, the quantity will be converted to match the part's purchase unit.
- Delivery date – This will be the same as the current delivery date on the customer order row minus the safety time registered for the part, if any. The delivery date also considers the supplier's fixed delivery days, work days, and calendar exceptions (vacation period, etc.). If the purchase order row's suggested delivery date falls within a calendar exception, the last workday prior to the calendar exception/day off will be used as delivery date.
- Priority – This will be the same as on the customer order.
- Revision – This will be the same as on the customer order row.
- Customer order – This will be the customer order number from the linked customer order.
- Customer – This will be the customer from the linked customer order.
- Project – This will be the same project as in the posting on the customer order row.
- Warehouse – This will be the same as on the customer order row.
Other information on a created purchase order can be filled in on that order in the same way as during manual registration of purchase orders.
If the part on the customer order row is linked to a configuration group, the calculated standard price is saved to the purchase order row.
If you later on update quantity or delivery date on the customer order row and save, a dialog box appears where you can choose if the corresponding information on the linked purchase order should be updated or not. You see the purchase order row's new quantity and new delivery date in the dialog box.
In the Register purchase order procedure you can edit some of the information on the linked purchase order that was included from the customer order row, even though it is linked. Modifications, if any, must normally be made on the customer order/customer order row, but it is possible to change e.g quantity, price, discount, and delivery date on the purchase order.
If you change quantity or delivery date on the purchase order row and save, and dialog box appears where you can choose if the corresponding information on the linked customer order row should be updated.
On the customer order row it is also possible to disconnect a linked purchase order. This is done via the button Disconnect linked order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) on the function menu. This can be useful if you for example want to undo a linked purchase order for different reasons. When a purchase order is disconnected, it is also possible to undo arrival reporting items made on it.

#### M-order/P-order
In this column you see the number of the manufacturing order or purchase order created, depending on if the part on the row is manufactured or purchased. The position is shown after the linked order number. If the number is shown in italics, it means that the part is stock driven and that the manufacturing/purchase order is not linked to a Linked requirement via the lot sizing rule on the part.

#### Change linked order (C)
By using the Change linked order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can link a customer order row to an already created manufacturing order or purchase order with order oriented part.
This may be useful if the purchase order/manufacturing order was created before the customer order. A warning will be displayed in cases where quantity or date differs between these two orders.
If you link/connect orders for parts which can be configured, it is possible for you to choose for which order to keep the configuration. Then you can – depending on how far along in the manufacturing it is – select which manufacturing order to link.
> Please note! No synchronization of manufacturing orders will take place.

#### Link to order
The button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) is displayed on rows which already have generated a manufacturing or purchase order. By using this button you can open the linked order in the procedure in question.

#### Blanket order
If there is a blanket order registered for customer (the customer in question or for one of the customer’s parent companies) and part, the button Blanket order is activated. Under this button you can find information about the blanket order. Here you can see the blanket order’s order number, customer number and customer name for the customer registered on the blanket order, validity period, initial quantity, called quantity, quantity left, and blanket order status. You can disconnect the blanket order from the order row using the Disconnect blanket order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) in the toolbar.
Blanket orders that are used for calls are determined by the following priority:
1. The purchase order is registered for the same customer that is registered on the blanket order or for a customer whose parent company is registered on the blanket order.
2. Within the validity period (how the validity period is calculated is determined by if you have selected Order date or Delivery date­ date on the blanket order).
3. Priority.
4. Valid from (oldest first).
5. Valid to (oldest first).
6. Requirement date (oldest first).
7. Quantity left to call (smallest quantity first).
8. Order date (oldest first).

#### Link to blanket order
You can go to the blanket order using the Link to blanket order button.![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png)

#### Sales account
Here you enter the account on which the sale should be posted. With the system setting Mandatory posting on order row you determine if a sales account must be selected on the row.

#### Posting
The Posting button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) opens a posting window where you can distribute the posting in different dimensions against the sales account on the row. The posting dimensions on the sales account are also displayed in separate columns on the order row between the column Sales account and the Posting button. The default posting is loaded to the row from the posting matrix (for row type 1), but when posting on dimensions you can also post based on the warehouse on the row in question. Provided the Warehouse option is used and you have activated settings for posting of CC, etc. based on warehouse.
Posting of dimensions can be performed automatically when they are linked to registers. This is determined by settings in the Dimensions Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. procedure. If you have a dimension linked to Employee, you will get an automatic posting via the seller entered in the Header tab.
In addition to the Sales account there can also be separate posting rows for the posting types Setup, Material, and Stock. The posting types handled on an order row are determined by the system setting for setup: Posting of setup price is set as posting of the part and the system setting for material and stock: Record material cost of goods sold at invoicing.
You can also enter a specification text for each posting row in the posting window. The text will be included in the accounting.
If you in the posting have already entered a project number and the part also has a serial number, the project number will be saved to the serial number in the Serial number/Batch procedure.

#### Standard price
For order rows of row type 1, you will see the part's current standard price displayed in the company currency. You can enter a standard price and it is shown with a maximum of six decimals.
This field is locked by default ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png). It is possible to unlock the field by clicking on the padlock button, making it change symbol to unlocked ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PadlockUnlocked.png). Then you can modify the standard price of the row.
For order rows of row type 2, you need to manually enter a standard price.
The standard price on the row forms the basis for CM The contribution margin (CM) is the difference between the standard price and the sales price. and CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. in, for example, statistics and in the accounting.

#### Contribution margin (CM)
Here you can see the part's contribution margin in the company currency. The contribution margin (CM The contribution margin (CM) is the difference between the standard price and the sales price.) takes changed standard price on the row into consideration. The contribution margin on the row also considers the system setting Basis for CM and COGS posting is loaded from fictitious part when calculating CM of fictitious part structures.

#### Contribution ratio (CR)
Here you can see the part's contribution ratio (CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage.) in percent.

#### Variant code
Here you can enter a variant code (previously called "alternate preparation code") that can affect the sub-rows if the main row is a fictitious part. If a manufacturing order is created from the customer order row, the variant code is included in the manufacturing order.
The variant codes origin in the operation list or the material list in the BOM and routing procedure. By using the variant code, the order row will apply for a specific variant of a structure part.

#### Type of requirement
Here you see/decide which type of requirement the order row has in the requirement planning. Subsequent order rows added will by default get the same type of requirement as this row, but it is possible to change. The available options are:
- Fixed order – This states that it is an actual/real order row. This type of requirement is entered by default when you add new order rows of row type 1 or 2.
- Manufactured – This means that the order row can be manufactured but not delivered. It is only for information purposes.
- Buy material – This indicates that it is OK to procure the necessary material for the order row.
- Forecast – This means that it is a forecast order row. You can take sales forecasts into account when performing requirements planning. When Forecast is selected on the order row, then it is not possible to create a manufacturing order or purchase order from it. If a linked order is already created, you cannot select Forecast as type of requirement. In that case you must first remove the linked order.
> The types of requirement called Manufactured, Buy material, and Forecast, are handles as forecasts in the system, and not fixed orders. In order to make the system take order rows with these types of requirement into consideration in the requirements planning, you have to activate the setting called Sales forecast (customer order) in the Existing suggestions/orders in the Requirement calculation procedure. The Net requirement calculation procedure always takes forecasts into consideration.

#### Row Status
Here you see the status of the order row. The statuses which can occur on an order row correspond to the statuses available for the order in the Status field in the order header, but can differ from the status of the order.
Example:
An order row on a new order that is included in a pick list is assigned row status 4 (Picking in progress). The order will then also get status 4 (Picking in progress). An order row that is being delivered in full is assigned row status 9 (Final delivery made), but the order has order rows left with remaining quantity and is because of this given status 5 (Partial delivery made).

#### Revision
For row type 1, you will see the part's active revision. You can change among the existing revisions of the part. If the active revision is not selected, the revision will be displayed in italics. By placing the cursor on the revision field, you will see an explanation in a tooltip. The Modified order confirmation will be printed if the part's revision has been changed after the order confirmation was printed.

#### Drawings
If there are drawings linked to the part in the part register (at the time of the order registration), you will see information about those drawings here. By clicking the button you see the drawing number, active drawing revision, comment, and files linked to the drawing's revision. You can change revision on the row, and a warning will be displayed if the row’s revision does not match the current revision on the part. You can also synchronize the revision on the order row with the revision in the Part register, as long as the order/quote has status 1, Registered.

#### Warehouse
Here you can decide the warehouse in which the order row will be registered. The warehouse entered by default is the one selected in the Warehouse field in the Header tab, but this can be changed per row. If the part on the row has a warehouse selected in the field Default warehouse on customer order in the Part register, that warehouse will be selected by default.
> If the order row has a linked manufacturing order or a linked purchase order and you change warehouse on the order row, then the warehouse will also be changed on the manufacturing order/purchase order. If you have already reported a transfer to stock on the main part (the top node) on the linked manufacturing order, then it is no longer possible to change warehouse on the order row.

#### Extra fields
In the Extra fields procedure you can to add extra fields for order rows. If such fields already have been created, these will be available under the Extra fields button on order rows.

#### Amount (company currency)
If the currency on the order differs from the company currency, you can in this column see the amount of the order row displayed in the company currency.

#### Price each (company currency)
If the currency on the order differs from the company currency, you can in this column see the unit price displayed in the company currency.

#### Customer's order number
This field is used to enter the customer's purchase order number on row level. The field can contain a maximum of 30 characters. In many cases, you enter the customer’s order number in the header of the order, but if you for example are working with delivery schedules it is common that order numbers or call numbers are used which are unique for that specific order row. This is not the same order number as in the header of the order. If you are using EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system., this value will be entered via the order file you import. But if you manually register an order, then you should yourself enter the order number on the row if the customer requires it. The value in this field will be included when using EDI to export for example order confirmation and invoice. This is done so the customer can match it with their purchase order.

#### Customer's order row position
This field is used to keep track of the row number which the customer has stated in their purchase order. The field can contain a maximum of 15 characters. This value is entered via EDI import of an order, but it is also possible to manually enter it, if you want to. The value in this field will be included when using EDI to export for example order confirmation and invoice. This is done so the customer can match it with their purchase order row on this order row position. It is especially important to keep track of the customer's order row position in cases where the customer order row is split. For example if it is not possible for you to deliver everything now, but the row must be split and a you enter a later date for a part quantity on the new row. Then it is important to know which order row position at the customer that the new row refers to.

#### Desired delivery date
The row's desired delivery date is by default set as the same as the current delivery date on a new row. The desired delivery date is the date when the customer wishes to get the delivery. This date can be changed until the point when the order is delivered in full.
With the system setting Question when changing delivery date, applies to frozen initial/desired you determine whether the desired delivery date should be automatically changed if the current delivery date is changed after it is "frozen" for desired delivery date, or whether a question should appear asking if the desired delivery date is to be changed after it is "frozen".

#### Initial delivery date
The row's initial delivery date is by default the same as the current delivery date on a new row. The Initial delivery date is the date that first was entered when the row was registered. This date can be changed until the point when the order is delivered in full.
The system setting described above for Desired delivery date also affects the Initial delivery date in the same way.

#### Remaining quantity
Here you see the number of parts on the row that have not been delivery reported.

#### Under picking
This field shows the number of parts on the row that have been included in the pick list in the Delivery planning procedure, but have not been delivered yet.

#### Delivered quantity
Here you see the number of parts on the row that have been delivered.

#### Forecast deduction
Here you decide if the quantity on the order row should be included in the deduction of sales forecasts on the part. All order rows are included in the deduction of sales forecasts by default.

#### Show prices
With this checkbox you determine if the price each and the amount should be displayed on the order confirmation. If you uncheck the checkbox, you will see a text on the order confirmation after the order row, saying that the price cannot be confirmed and will be confirmed later on. This text is possible to edit in the Document texts procedure.

#### Show delivery date
With this checkbox you determine if the delivery date should be shown on the order confirmation. See the description under Delivery date above.

#### Order date
The order date on the row is by default the date in the field Order date under the Header tab, but it can be changed per row.

#### New finish
New finish is calculated by the net requirement calculation and shows the date when (at the earliest) the customer order row can be supplied by manufacturing order, purchase order, or stock order.

#### Net weight
If the row is of row type 1, the part's net weight registered in the part register will be displayed by default, but it can be changed on the row. The weight will be displayed in the unit of the order row. This means that a conversion will be made via a conversion factor if the unit on the row is not the standard unit of the part. For row type 2, you need to manually enter a net weight.
The net weight is used in order to calculate the total weight for all rows on the order, in the unit kg/order unit. The calculation is shown under the Shipping information button at the bottom of the tab.
With the system setting Update shipping information on customer order/invoice you decide if the total weight in the shipping information should become updated when you change the net weight on an order row. Using that setting you can choose to update with or without a dialog, or not to update at all.
Please note! If you change the net weight on the part in the Part register, it will not be updated on existing order rows containing the part.

#### VAT code
If the row is of row type 1–2, the default VAT code for the VAT group on the order will be displayed. If an exception from VAT code has been entered for the part’s product group, you will see that VAT code instead. The VAT code can be changed per row.
The default VAT code for VAT groups and exceptions from VAT code per product group, if any, are entered in the VAT settings procedure.

#### CN code
For row type 1, you will see the part's CN code (goods code) from the Part register procedure. The CN code will be saved on the order row if you change/enter another CN code. When Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. is then compiled, the CN code will be loaded from the row if there is a saved code, otherwise the code is loaded from the part register.
If the row is of row type 2, you should manually enter or select a CN codes and then the number will be saved on the order row.
Packaging rows and rows with alloy cost will inherit the CN code from the main part. If a packaging part is used separately (as a normal row type 1), the part will follow the normal rules and will get the CN code entered on the part.

#### Transaction type
Transaction types are used in Intrastat reporting. The transaction type indicates which type if transaction applies to deliveries (of customer order rows and purchase order rows) that are made within EU. It is possible to override the transaction type if you change or set a transaction type on the row. The transaction type functions in the same way for row types 1 and 2.
Rules for how transaction types are displayed on the order rows:
1.   
The saved transaction type on the row (for the existing record) is primarily displayed.
2.   
Secondarily, the transaction type will be shown based the order type. If a link is missing to transaction type for the order type in the Order types procedure, then item 3 applies.
3. Thirdly, the transaction type based on the type that is set as default in the Transaction types – Intrastat procedures is displayed.

#### Fixed assets objects
If the option Fixed assets register is installed and you have user rights sufficient to sell/retire fixed assets, then this column is available. Here you then select the assets object which should be sold. It is only possible to select objects which have not already been sold or exist on another order. If the object doesn't exist in the part register, you should use an additional order row (row type 2).
In connection with approving the invoice for the order, the sales will automatically become registered in the fixed assets register and a journal record will be create in the fixed assets journal. Sales price excluding VAT, and information about customer and invoice number will be registered on the object's sales information. If the sales price exceeds or falls below the residual value, this will be recorded either as profit or loss in the fixed assets journal. If the fixed assets object is a main object it means that all sub-objects will also be sold.

#### Dock – Row
Here you enter the dock to which the part on the order row should be delivered. This is often used on delivery schedules.

#### Dock description
Here you can enter a text describing the dock.

#### Storage
Here you see/enter the storage to which the part on the order row should be delivered. This is often used on delivery schedules.

#### Kanban number
Here you see the Kanban number for the part on the order row, if this is entered. This is often used on delivery schedules.

#### Reference number for manufacturing
Here you see/enter the customer's reference number for manufacturing. This is something which is primarily used if you have customers within the car industry where it sometimes happens that the customer, in their delivery schedules, earmarks requirements with for example chassis numbers. You need to refer to this reference number in both the dispatch advice message sent to the customer in connection with shipping the goods, as well as on the transport labels with which the goods have been labeled.

#### Reference number for delivery
Here you see/enter the customer's reference number for delivery. This is something which is primarily used by those who have customers within the car industry where it sometimes happens that the customer, in their delivery schedules, earmarks requirements with is called Part consignment number. You need to refer to this reference number in the dispatch advice message sent to the customer in connection with shipping the goods.

#### Row's goods label
Here you can enter the customer order row's goods label. If you create a purchase order or a manufacturing order from the customer order, then the row's goods label will be included to the field Customer order row's goods label on the manufacturing order and to the field Customer order row's goods label on the purchase order.

#### Customer's part number
Here you see the customer's part number from the customer link in the Part register.

#### Customer’s order change number
Displays the order change number that the customer used when requesting a change to this order.

#### Customer’s order change date
Displays the date on which the customer requested a change to this order.

#### Customer’s reason for change
Displays the customer’s reason for changing the order.

#### Comparative price
This field is activated if the system setting “Comparative price” is activated. For order rows of row type 1, you will see the part's current comparative price in the company currency. The comparative price can be edited manually.
For order rows of row type 2, you need to manually enter a comparative price.
The comparative price on the row can be used to follow up on how CM/CR develops due to currency changes.

#### CM based on comp. price
This field is activated if the system setting “Comparative price” is activated. Here you can see the part's contribution margin in the order’s company currency. This contribution margin uses the comparative price in the calculation. CM based on comp. price takes into consideration changed comparative price on the row.

#### CR based on comp. price
This field is activated if the system setting “Comparative price” is activated. Here you can see the part's contribution ratio in percent based on the comparative price.

#### Customer’s action code
Here you select which action the customer has requested. You can choose from the following alternatives:
- Added
- Changed
- Canceled
- No action

#### Original row quantity
This field is used when you have split a row using the Split row button. The field shows the original row’s quantity before splitting.

#### Split counter
The split counter is a counter value that counts the times a row has been split. Each new split of the original row increases the value by one. The split counter is per part number on the order.

#### Our reason for change
Here you can select your company’s reason for the change. These reasons (cause codes) need to be registered in the Cause codes procedure before they can be used. If Mandatory comment is checked, you must also enter a comment in the field below.
Please note that neither Our reason for change nor the related comment are available in the document templates.

#### Remote configuration
This column is shown if you have both the Customer order transfer and the Product configurator options. The column is displayed when the part on the order row has the Remote configured setting activated in the supplier link. This means the part has a configuration in the production company (the supplier).
When a transfer profile is selected on the order row, a button with this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Available.png) is activated in the column. It lets you know that the order row is not configured. You use this button to connect to the production company and configure the order row in the Remote configuration window, with the help of the part's configuration in the production company. Once the order row is configured the button will display this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png). It lets you know the order row is configured. Read more about the [Remote configuration](../../../UserGuide/Using/Configurator/RemoteConfigurating.htm) window.
As long as a new order row is not remote configured, an error sybol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) is shown in the Part field, letting you know the order row is missing a configuration from the part in the production company. Then it is not possible to save in the procedure.

#### Transfer profile
This field is shown if the option Customer order transfer is used. Here you see the part's default transfer profile on a new order row, if the part has a default transfer profile configured in the part register. Otherwise you can select a transfer profile for this row. This should be done in the sales company.
If you also use the Product configurator option and the order row has been remote configured, then it is not possible to change the transfer profile.
You can leave the field empty or clear the field, if the new order row shouldn't have a transfer profile.
If you add an order row which has a transfer profile in the sales company, a customer order/customer order row will be created on the same part number in the production company. A transfer of the order row is made when you save the order.
If you after this make changes to such an order row in the sales company or in the production company and save, the corresponding information on the order row will be transferred to the other company (today, only the Delivery date will be transferred).
If the customer order in the production company is locked for editing (for example, partial delivery made), a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_information.png) is shown in the field together with information about it in a tooltip.
If you add an order row in the production company without selecting a transfer profile, a warning will be displayed ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) informing you that no transfer profile has been selected.
If you delete an order row with a transfer profile in the sales company, that order row will be deleted on the corresponding order in the transfer to the production company.
If you delete an order row with a transfer profile in the production company, that order row will not be deleted in the transfer to sales company.
For an order row with a transfer profile you cannot change the Row type after the order row has been transferred.
It might be allowed to disconnect existing customer order rows (this is determined by the transfer profile). Then you can, when needed, disconnect an order row in the production company, by clearing the field. In the sales company it is always possible to disconnect an order row, regardless of how the transfer profile is configured. Read more about consequences of disconnecting customer order row in the online help function for the procedure Settings for customer order transfer.

#### Transfer to
This field is available if the Customer order transfer option is used and it is only displayed in the production company.
If you add an order row to the customer order in the production company, and have selected a transfer profile for the order row, you can here select if the order row should be transferred to the sales company's Customer order and purchase order or Only purchase order. The default option here is Customer order and purchase order.
If the production company adds a sub-row for an alloy cost, Only purchase order will automatically be set for the row. Read more about [customer order transfer and alloy cost](../../../UserGuide/Options/COT.htm).
The Only purchase order option is useful if the production company invoices for freight on an order row to the sales company, but when the freight should not be invoiced to the end customer.
If the order row was added in the sales company and transferred to the production company, you cannot edit this field. The default option here will then be Customer order and purchase order.

#### Transfer status
This field is shown if the option Customer order transfer is used. Here you see the transfer status for this order row. It can be Not transferred or Fully transferred. This information, and the information in the following two columns, are saved on the row when transferring to the remote company. This takes place when you save the order. You can click the button Reload ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) (Ctrl + Shift + R) on the toolbar of the procedure, to update the values in the fields.

#### Transferring comp.'s order no.
This field is shown if the option Customer order transfer is used. Here you see the transferring company's customer order number. If you are in the sales company, you will see the production company's order number, and the other way around.

#### Transferring comp.'s order row pos.
This field is shown if the option Customer order transfer is used. Here you see the transferring company's customer order row position. If you are in the sales company, you will see the production company's customer order row position, and the other way around.

#### Transferring company's reference
This field is shown if the option Customer order transfer is used. Here you see the transferring (sales) company's reference on the customer order in the receiving company (production).

#### Transferring comp.’s “customer's part no.”
This field is shown if the option Customer order transfer is used. This field shows the sales company’s customer's part number. This part number is transferred to the production company’s customer order. In the production company, this part number is printed as Our part number on the delivery note, delivered document if the setting Delivery in the Settings for customer order transfer procedure is set to delivery directly to end customer.

#### CO2e
Here you see the CO2e value from the Part register. You can change the value, if needed. The CO2 e value is used in sustainability calculations.
