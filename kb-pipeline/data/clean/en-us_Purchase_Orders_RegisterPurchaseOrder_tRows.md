### Rows
Under the Rows tab you can add rows for the parts that are to be ordered in the purchase order in question and information regarding them.
At the bottom of the tab you see a total of the order’s remaining excluding VAT as well as the order’s total excluding and including VAT. All totals are shown in both the order currency and in the company currency. A total of the order's total net weight and total volume are also shown. The transport time is also shown at the bottom of the tab. It refers to the transport time to the selected delivery address, primarily on the order and secondarily on the delivery address entered on the supplier. This can also be changed on the order. The supplier's delivery days are also displayed. Here you see the order’s total emissions in kg CO2e. Read more about transport time and delivery days in the topic [Delivery/Shipping](../../Suppliers/SupplierRegister/bDeliveryShipping.htm) in the help function for the Supplier register.
The Function menu
On the function menu on purchase order rows you find buttons as detailed below, and also to add ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5), insert ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) (Ctrl+F5), and delete ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6) order rows.
You can [read more](../../../UserGuide/Interface/FunctionsMenu.htm) about all buttons on the function menu here.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_subrow.png) – Add underlying level (Ctrl+Shift+F5.) There can be rows on different levels. E.g. a part row on level 0 with associated alloy cost or additional text on level 1. Another example can be a fictitious part on level 0 with included parts on level 1. Level 0 is called Main row and level 1 is called Sub-row/Underlying row/Underlying level.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) – Split row (copy row) (Ctrl + Shift + C). With this button you split an order row (main row) to a new order row. If you have selected the option Split, with dialog in the system setting Function of “Split row” button in Register purchase order, the [Split row dialog](bSplitRow.htm) will be shown and you will be given multiple options for how the splitting will be performed.
> If you delete a split row, the quantity on the original row will be restored.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_split_row.png) – Split the row if quantity in the linked blanket order is exceeded. If the order row is linked to a blanket order and the row quantity exceeds the remaining quantity from the blanket order, a button is activated ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_split_row.png) which you can use to split the order row into the remaining quantity from the blanket order, plus a new order row with the exceeding quantity. The new order row will not be linked to the blanket order. But by clicking the Blanket order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) on the order row you can link if to a different blanket order (if such order is available).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_phrase.png) – Insert phrase. On Text rows (row type 4), you can insert phrase.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_signature.png) – Insert signature. On Text rows (row type 4), you can insert signature.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_update_price.png) – Update price. Updates the price on the order row (see below).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) – Go to procedure. Links to related procedures for the part on the order row. If the Agent option is installed, it is also possible to create monitoring tasks straight from the order row. The monitoring task you can create are: Arrival – Part or Balance – Part.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) – Find & Replace (Ctrl + H). This button lets you find and replace values in the column on the current order row or on all order rows.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png) – Run the check of delivery times again. Runs a check delivery times (CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.) on the order row (see below).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_hidden.png) – Show rows with final delivery made. If there are order rows where final delivery has been made, you can choose to show these using this button. By default, rows with final delivery made are shown. The next time you open the procedure, the button will be in the mode you left it in. If you restart the Monitor ERP client, the button will return to the original mode.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_update.png) – Recalculate positions (Ctrl + Shift + O). Recalculates positions on the order. The system setting Recalculate locked positions determines if manually edited (locked) positions will be edited.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PadlockUnlocked.png) – Lock/Unlock “Price each” and “Discount”. This setting makes it possible to temporarily lock/unlock Price each and Discount for all rows on a purchase order. This is activated with the system setting called Enable temporarily unlocking "Price each" and "Discount".
Check delivery times
If you apply check delivery times (CDT), which is activated with a system setting, you find this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png) on the function menu. This is used to run a check of the delivery times for the selected order row. This button becomes available after you have saved the order. If you click the button, an analysis is made to see if the order row's planned Delivery date will result in any consequences later in the chain of requirements. For example, if delays regarding the material are causing the order not to be finished on time. When you have run the check of the delivery times, the button CDT ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypePurchase.png) is activated on the order row. You also see data in the columns Requirement date (when the requirement of the part on this order row occurs) and Difference (the difference between the order row's planned delivery date and the requirement date). By using the CDT button you can see the result of the analysis, which consumers (requirements) the order row should supply. Read more about this in the chapter CDT below.
If you for example change the order row's planned delivery date and save, you must run the check of delivery times again by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png). Read about [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using Monitor G5 in the online help function.
Update price on order row
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
Update linked purchase order row
If a purchase order row is linked to a customer order row or manufacturing order and you change the purchase order row's delivery date so that it affects the customer order row's planned delivery date or the manufacturing order’s or operation's material requirement date, you can also choose to replan the customer order or manufacturing order. When you save the purchase order, a dialog window opens. There you can choose to update the linked customer order row with a new delivery date. For linked manufacturing orders, you can use the button Open manufacturing order in the dialog window to replan the manufacturing order in the Register manufacturing order procedure.
If the purchase order row is linked to a customer order row, you can change the quantity on the order row. When you save the purchase order, a dialog window opens. There you can choose to update the linked customer order row with a new quantity.
If the purchase order row is linked to a manufacturing order, you cannot normally change the quantity on the order row. The field is then blocked. But if the part on the linked purchase order row has a partial quantity registered in the Part register, you can replan the quantity by clicking the Partial quantity button on the purchase order rown. This replanning will not affect the quantity of the manufacturing order.
If the linked purchase order row is deleted, then the link to the customer order row or manufacturing order will also be deleted.

#### Position
The position of the first main row is 1, 10, or 100 (as per the Increment of positions system setting) and the next main row to be added will be assigned position 2, 20, or 200 etc.
You are able to manually renumber the positions. Once a position has been renumbered, the position number will be locked. The Recalculate locked positions system setting determines whether locked position numbers will remain the same or be recalculated when position numbers are recalculated on the order.
If the order has status 1 – Registered and you insert a new main row, the position numbers will be automatically recalculated. (Please note that different statuses are applied to different orders, customer orders, blanket orders etc.)
If the status of the order is 2 or 5 and you insert new main rows between two positions, numbers will be assigned between the positions. That way, you can add/insert several new main rows between the positions without them affecting the position numbering of the subsequent rows. When there are no available position numbers left and a new main row is added, the Position numbers when using "Insert new row" system setting determines whether all position numbers will be recalculated or whether you should manually add a position number. If you would like position numbers to be recalculated, in any status, you should select the Recalculate all positions option in system settings.
Only main rows have positions, not sub-rows. To the left of each position with sub-rows you find the following button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/ActiveRow.png). This you can use to expand/minimize the sub-rows. You can use the function button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) in the box to expand/minimize all sub-rows at the same time.
You can sort rows by clicking the column header for Position number. On documents however, rows are sorted by RowIndex, an inbuilt feature that indexes rows in the database. This means that rows on documents are always sorted in the order in which they are registered under the Rows tab.

#### Delivery status
If an arrival is reported, a symbol is displayed for delivery status according to the following:
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPartiallyShipped.png) – partial delivery made (remaining quantity greater than 0).
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusDeliveredOpFullyShipped.png) – final delivery made (remaining quantity is 0).
An order row that have been delivered in full cannot be modified, e.g. you cannot change the quantity or part number.

#### Row type
Here you can see/enter the row type of the order row. Row type 1 is entered by default when registering a new order row. The following row types exist for purchase orders:
- 1) Part row – This row type can only contain parts that are registered in the part register (manufactured, purchased, fictitious parts, and services). When you have entered or selected a part number, data from the part will be loaded on the row. Part number is mandatory. If you have added an order row of row type 1, and then not entered or selected a part number, you will see an error symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) in the part number field, and in that mode you cannot save the order, until you fill in the part number.
- 2) Additional order row – This row type can also contain parts that are not registered in the system. Information about the part can be filled in manually. Neither part number nor name are mandatory.
- 4) Text row – This row type is intended for any additional text you want to enter on the row. A text row can be a sub-row and in that case it is linked to a main row of row type 1 or row type 2. If the text row is not a sub-row, it is not linked. It then means it belongs to the actual order, not to a specific row.

#### Show on the following documents
For row type 4 you here find a text editor where you can write and format texts, insert images and hyperlinks. In the part register it is possible to enter a comment in the supplier link. For row type 4 you can click this button and select on which document types the additional text row should be shown. You can select among Inquiry, Purchase order, and Delivery schedule Silf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands.. All document types are marked by default. By using the checkbox at the top you can also select/deselect all documents at the same time.

#### Part
The part number on the row. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard.feature, you can search the part register for parts.
For row type 2, you can also leave the field empty or enter an optional part number. If you enter a blank space (space bar) before or after the part number, this will be deleted when you leave the name field on a new additional order row.

#### Name
For row type 1 the part’s name is automatically loaded from the part register after you have entered the part number. You can change the name on the order. In case the part name is not translated to the language of the mailing address and delivery address, the name will be displayed in the user's language. This also applies to order confirmations and delivery notes.
For row type 2, the name field is always empty unless a registered part number has been entered or selected. It is best to enter the part name in the language of the mailing address.

#### Part type (T)
This column shows a symbol for the type of part loaded on the row. Read more about [part types in the Part register](../../../Stock/Parts/PartRegister/hPartRegister.htm#Artikeltyp).

#### Order's part status (P)
In this column you can see the order’s part status in form of a symbol, except for the status Normal where the field is empty. A tooltip over the symbol displays the part status in text.

#### B/N (Block/Notify)
In the Block/Notify column you see if the part is blocked or if there is a message regarding registration of purchase order. It is possible for you to edit a purchase order containing blocked parts if the purchase order was created prior to when the part was blocked. However, you cannot add new rows with the blocked part.

#### Quantity
The quantity of the part. The field displays two decimals, but it is possible to enter up to six decimals. It is possible to enter a zero quantity on purchase order rows.
The default quantity of the part is determined by the system setting Default quantity on new order row. There are also two system settings regarding quantity of the part for different checks: Check quantity on order against minimum quantity for warehouse and Check quantity on order against quantity/package.
If the purchase order row is linked to a manufacturing order (material requirement), you cannot change the quantity. See the section Update linked purchase order row above.
If the order is a return order, the quantity will be negative. This is the quantity that was entered to be returned when the return order was registered in the Register return order procedure. This quantity cannot be changed and it is the quantity which will be deducted from the location when the return order is "delivered" in the Report arrival procedure.
For a partially arrival reported order, it is not possible to change quantity for a row to less than the already arrival reported quantity. When changing the quantity to a value which corresponds to the arrival reported quantity, a warning will be shown letting you know that the row will be marked as Final deliver made after you have saved.
If the part has partial quantities, you cannot enter a quantity in the field. You should instead use the Partial quantities button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) on the order row to enter a quantity.

#### Unit
For row type 1, you here see the part's default unit. If several units are registered for the part, you will see the unit selected for purchase order under the button Default units/usage in the Part register. You can change to another unit if the part has several units. If you change to another of the part’s units you will be asked if the quantity should be recalculated according to the entered conversion factor. The price each will also be affected if you change the unit. Unit is mandatory for row type 1.
For row type 2, no unit will be suggested, but you can select among all units in the system. By clicking the X button next to the Unit field, you can delete the unit on this row. It is optional to enter a unit for row type 2.
The unit is always displayed in the user's language. On printouts of purchase orders, the unit is displayed in the language of the mailing address.

#### Price each
Here you enter the price each of the part. It can be entered with a maximum of six decimals. The price is always displayed/entered excluding VAT.
For row type 1, the following applies regarding the price on the purchase order row:
- Primarily, the price is loaded from the supplier link, if any. If there is a staggered price in the supplier link, this will be used in cases where there is a staggered price matching the quantity on the order row. Staggered prices appear in italic font. If the quantity on the row is less than the lowest staggered price, the normal price on the supplier link will be used.
- A check will also be made against the valid through date of the price on the supplier link. If the valid through date has passed, you will get a warning. If you at this time has a future price entered, you will be asked if you wish to load the future price.
- If no supplier link exists or if no price has been registered in the supplier link, the suggested price will be zero. Regarding the supplier link, it refers to the supplier on the order, not the supplier in the Supplier number on invoice field.
- A warning will be displayed if the currency of the price does not match the currency on the order. The price will be converted to the currency on the order, and the warning shows that the order's exchange rate has been used when converting.
The number of decimals is determined by how many decimals have been entered in the system setting Number of decimals in price on inquiry, purchase order and supplier invoice.
For row type 2, zero is always suggested as price.
For return orders, the price each is always loaded from the original order.

#### Price each including VAT
By activating Price each including VAT it is possible to enter a price including VAT. By entering a price including VAT, the price will be changed to price each excluding VAT.
By using the calculator function in the Part register procedure you can calculate which appropriate price the part should have if you want a specific price including VAT.

#### Price alternative
Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can choose to use another price than the one current on the order row. Here you see standard price, supplier's supplier links with price, and supplier's part number. You can select among all of these prices. All properties from the selected supplier link will then be loaded to the row.

#### Partial quantity
The Partial quantity button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) is only displayed if the part has a partial quantity registered in the part register. By clicking this button you see partial quantities as described below.
If the part on the order row has the control method set to Stock driven, you see the partial quantities that are registered for the part. You can make changes to the rows, add rows with quantities, each partial quantity in the part’s unit, and you can link a packaging part to each partial quantity. You can delete the rows with existing partial quantities which should not be included on the order row.
If the part on the order row has the control method set to Order driven, you see the partial quantities that were saved on the linked the customer order row. In this case as well, you can make changes on the rows, add and delete rows. If you then change the partial quantity of the purchase order row, a dialog is shown where it is default to also update the linked the customer order row. If it is a linked manufacturing order you will see the partial quantities that are registered for the part. If you then change the partial quantity on the purchase order row, the linked manufacturing order will not be affected.
The quantity is multiplied by the partial quantity’s quantity, and is entered in the quantity field on the order row. It is not possible to make changes in the quantity field on the order row if there are partial quantities. The number of partial quantities you have entered under the button will only be saved on the order row, not for the part.

#### Price comment
If there is a price comment on the supplier link, this will be displayed when the part number is entered on the order row.

#### Discount
The discount that applies for the part on the row. For row type 1, the discount will be suggested based on the following rules: 1) discount in the supplier link, 2) discount from a discount category, 3) discount on the supplier. For row type 2, it is only possible to manually enter a discount on the row. For all row types it is possible to enter another discount on the order row. The discount is always entered in percent.
The discount is locked by default for return orders and purchase orders of the subcontract type.

#### Setup price
The setup price for the part on the row. For row type 1, the setup price entered for the supplier in the supplier link of the part will be suggested, otherwise the field is empty. For row type 2, the field is always empty, but it is possible for you to enter a setup price.
The number of decimals is determined by how many decimals have been entered in the system setting Number of decimals in price on inquiry, purchase order and supplier invoice.

#### Delivery date
Here you see/enter the order row's planned delivery date. This date can be entered on row type 1 or 2. The delivery date shown on the order row always refers to the date when the delivery should arrive at your warehouse. The date is shown in italics if the order has been changed which resulted in the current date not being the same as the initial date.
The subsequent order rows will by default get the same delivery date as the order row above. You only enter a delivery date on main rows, not on sub-rows.
On the first order row, today's date or today’s date plus lead time for the part/supplier link, will be suggested as delivery date. This is determined by the setting Default delivery date on order rows.
In the Delivery date field you always see the standard calendar entered in the Company information procedure.
If a different calendar has been selected for the supplier it means the supplier’s calendar will be used when calculating delivery dates for printouts when transport time is available data on the supplier, and also when calculating the suggested delivery date on order row. The reason behind this is that the purchaser should also be able to see its own company calendar to make sure he/she does not choose a date marked as holiday.
The suggested delivery date has also been checked against the supplier's delivery days and against the supplier's work days in the supplier's calendar. It has also been checked that the delivery date is not in a calendar exception for the supplier. You configure the supplier's delivery days (which days of the week) and calendar and calendar exceptions in the Supplier register procedure.
The supplier’s delivery days are also displayed at the bottom of the tab.
These settings configured on the supplier will therefore affect the suggested delivery date on the order row. The default delivery date will then perhaps not become today's date or today's date plus lead time. Instead, it will be the first date after today that has been entered as a delivery day, and it must also be a work day in the supplier's calendar.
If you manually select a delivery date on the order row, this date will be checked in the same way as above. A warning is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) together with an explanation if the date is not a suitable delivery date. A check is also made to make sure the selected delivery date has not already passed. If so, a warning will also be shown.
Changing the delivery date
If you change delivery date, a dialog opens where you will be asked if you also want to change the Initial delivery date and the Desired delivery date.
If you choose Yes (Change requested by us), it means both the initial and the desired delivery date will be changed to the same date as the delivery date. If the order row is Confirmed, it will be changed to Unconfirmed.
If you choose No (Change requested by supplier), it means no change will be made of the initial and desired delivery dates. If the order row is Confirmed, it will continue to be Confirmed.
If the order row is linked to a customer order row or a manufacturing order (material requirement), and you change the delivery date, it is also possible to update the linked order. See the section Update linked purchase order row above.

#### Delivery date from supplier
If the supplier has an entered transport time, this field will display the desired delivery date excluding the transport time. This field show the same delivery date as the delivery date on the Purchase order document.

#### Requirement date
If the purchase order row should supply a requirement, you here see the date when the requirement of the part on the order row occurs. The order row cannot be arrival reported later than this date. If the requirement date is later than the order row's planned delivery date, the date is displayed in red. If the requirement date is the same as or earlier than the order row's planned delivery date, the date is displayed in green.

#### Difference
Here you see the difference in work days between the order row's planned arrival date and requirement date. If the requirement date is later than the order row's planned delivery date, the difference is displayed in red. If the requirement date is the same as or earlier than the order row's planned delivery date, the difference is displayed in green.

#### CDT
The CDT ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypePurchase.png) button in this column shows the result of the check delivery times that was run by using the button Run the check of delivery times again ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delivery_time_check_again.png) on the function menu.
In the upper part of the window you see order information. Here you can, in the same way as directly on the order row, mark if the order row is confirmed as delayed, select a cause of delay, and enter a comment.
In the lower part of the window you see the entire chain of requirements, the consumers that the part on the order row should supply. You can expand one or all rows to see information from material requirement to underlying manufacturing and sales. The consumer's finish date/delivery date here is set as the requirement date on the order row.
On the function menu in the window, you can use the button Only show end-consumer ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_endconsumer.png) to only see the end-consumer, the material requirement, manufacturing order or customer order row, which started the chain of requirements.
On the function menu you also find the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png), which you can use to go to related procedures for detailed information about the marked row.
Read about [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using Monitor G5 in the online help function.

#### Amount
In this column you will see the order row's total amount according to the formula: Quantity x Price each - Discount + Setup price. The amount is shown in the currency of the order.

#### Revision
For row type 1, you will see the part's active revision. You can change among the existing revisions of the part. If the active revision is not selected, the revision will be displayed in italics. By placing the cursor on the revision field, you will see an explanation in a tooltip. The Modified order confirmation will be printed if the part's revision has been changed after the order confirmation was printed.

#### Receiving inspection
In this field you can determine if the order row should be subject to receiving inspection at arrival. If you have activated receiving inspection on the supplier in the supplier register, this is displayed in a tooltip over the icon ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_information.png) in the next field. Then this receiving inspection is applied regardless of what you do on the order row (if you select No, the receiving inspection selected in the supplier register will not be deactivated). If you select Yes, the buttons Instruction and Files will become activated. You can then enter a receiving inspection for this order row that will override the one selected in the supplier register.

#### Instruction
Here you can enter instructions regarding the receiving inspection. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
Here you can link files to the order row in question. Files that can be useful to link here are for example measuring forms and check lists etc. for receiving inspections.

#### Confirmed as delayed
Here you determine if the order row should be marked as confirmed as delayed. This means that the supplier cannot deliver the order row on the planned delivery date.
If you mark the row as confirmed as delayed, other affected users in the system can see that the delayed delivery date is fixed on this order row and there is no use sending reminders to the supplier. This means that we must try to catch up by reducing the affected throughput times and queue times on the manufacturing orders in question. This is made to mitigate the effects of the delay.
If you check the box, the field Cause of delay will become activated.

#### Cause of delay
Here you select a cause code for the delay. Cause codes for delays are handled in the Cause codes procedure. You might have configured that it is mandatory to enter a comment for cause codes.

#### Comment, cause of delay
Here you can see/enter a comment regarding the delay and the selected cause code. This comment can be optional or mandatory. This is determined by the cause code. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Message to goods receiving (M)
Here you can enter a message or instruction to the person who will receive the goods. The message is displayed in the Report arrival and the Receiving inspection procedures. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Included in payment plan
If you have selected a payment plan for the order, and the row should be included in a payment plan, then you should check this box. Payment plan is shown if the system setting called Handle payment plans on purchase orders is activated.

#### Customer order/Manufacturing order/Stock order
If the purchase order row is based on a customer order/manufacturing order/stock order, you will here see the order number in question. That is, the customer order, manufacturing order, or stock order that causes the requirement of this purchase order row. The position is shown after the linked order number.
When a purchase order is linked to a customer order row and you update the quantity or delivery date on the purchase order row and save, a dialog box appears where you can choose if the corresponding information on the linked customer order row also should be updated.
When a purchase order is linked to a customer order row or material row on a manufacturing order, you will see information about this on Transport label – Purchase, A4 and A5.

#### Blanket order
If there is a blanket order registered for supplier (the supplier in question or for one of the supplier’s parent companies) and part, the button Blanket order![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png) is activated. Under this button you can find information about the blanket order. Here you can see, among other things, the blanket order’s order number, supplier number and supplier name for the supplier registered on the blanket order, validity period, initial quantity, called quantity, quantity left, and blanket order status. By using the Link to blanket order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can link to/go to the row on the blanket order. By using the button Disconnect blanket order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) you can remove the link between blanket order and purchase order. If the link is removed, the price and any discount will be loaded from the supplier link.
Blanket orders that are used for calls are determined by the following priority:
1. The purchase order is registered for the same supplier that is registered on the blanket order or for a supplier whose parent company is registered on the blanket order.
2. Within the validity period (how the validity period is calculated is determined by if you have selected Order date or Delivery date­ date on the blanket order).
3. Priority.
4. Valid from (oldest first)
5. Valid to (oldest first)
6. Delivery date (oldest first)
7. Quantity left to call (smallest quantity first)
8. Order date (oldest first)

#### Link to order (L)
By using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can open the customer order or manufacturing order that has created and linked this purchase order row.

#### Link to blanket order (B)
By using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can open the linked blanket order.

#### Purchase account
Here you enter the account that the purchase should be posted on. With the system setting Mandatory posting on order row you determine if a purchase account must be selected on the row. For row type 1, the posting is determined by the posting matrix. For row type 2, the posting is determined by the system setting Default posting on additional order row.

#### Posting
The Posting button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) opens a posting window where you can distribute the posting in different posting dimensions on the purchase account on the row. The posting dimensions on the purchase account are also displayed in separate columns on the order row between the column Purchase account and the Posting button. The default posting is loaded to the row from the posting matrix (for row type 1), but when posting on dimensions you can also post based on the warehouse on the row in question. Provided the Warehouse option is used and you have activated settings for posting of CC, etc. based on warehouse.
In addition to the purchase account, there can also be separate posting rows for the Setup and Price difference posting types. The posting types handled on an order row are determined by the system setting for setup: Posting of setup price is set as posting of the part, and the system setting for price difference: Record price differences during invoice registration.
You can also enter a specification text for each posting row in the posting window. The text will be included in the accounting.

#### Confirmed
With this checkbox you indicate whether or not the supplier has confirmed the order row. If you have checked the Confirmed checkbox in the Miscellaneous box under the Header tab, this corresponding checkbox will automatically be marked for all the order rows. This is possible to modify per row unless the entire order is confirmed.
If you change price, quantity, discount, split row or revision for the part on the order row, this checkbox will be deactivated. This will also result in the document called Modified purchase order being available when reprinting the order.
The system setting called Change that will make purchase order row unconfirmed determines if a change of price, quantity, revision, split order row or delivery date on the order row should automatically uncheck this checkbox.

#### Confirmation date
The date when the order row was confirmed. The date is used for calculating order lead time. If you have checked the Confirmed checkbox in the Miscellaneous box under the Header tab, confirmation dates will be added to all order rows. This can be modified per row unless the entire order is confirmed.

#### Authorization list
The button Authorization list ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) is active if the order row should be approved. This occurs if the total amount on the order exceeds the user's authorization limit. By clicking this button you can view the authorization List. In this mode, the order is given status 0 (Awaiting manual approval) and the order row can be approved in the Approve purchase order procedure by the user's head signer.
If you register an order and an order row which result in that the total amount on the order exceeds your authorization limit, it is possible to change the quantity, price each, and discount so that the total amount falls below the authorization limit. If you then save, the order will automatically be approved by yourself (your name will be displayed under this button Authorization list and you can see that you have approved the order) and the order is given status 1 (Registered).
If you have sufficient user rights to modify the authorization list, the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_next.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_previous.png) are activated. These are used to add and delete available signers/signer groups from the left section to the authorization list in the right section. You can change the order of the selected signers/signer groups by using the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) in the right section. You can also check the box Parallel authorization if all signers/signer groups should be able to approve the order row at the same time and not necessarily according to the order in the authorization list.
The button Authorization list and the columns Send for authorization, Approved, Authorization status, Latest authorization action, and Approval comment are only shown if you have activated the system setting Approve purchase order.

#### Returned quantity
If the purchase order is a return order, this column is available. Here you see the quantity which has been returned to the supplier.

#### Return order
If the purchase order is a return order, this column is available. By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you find information about: return order number, link to the return order, supplier's order number, returned quantity, what is left to return, date of return (that is, the date when the order is expected to be delivered). When there is a return order, the button becomes orange ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png).

#### Drawings
If there are drawings linked to the part in the part register (at the time of the order registration), you will see information about those drawings here. By clicking the button you see the drawing number, active drawing revision, comment, and files linked to the drawing's revision. You can change revision on the row, and a warning will be displayed if the row’s revision does not match the current revision on the part. You can also synchronize the revision on the order row with the revision in the Part register, as long as the order/quote has status 1, Registered.

#### Extra fields
In the Extra fields procedure you can to add extra fields for order rows. If such fields already have been created, these will be available under the Extra fields button on order rows.
The More information button
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Amount (company currency)
If the currency on the order differs from the company currency, you can in this column see the amount of the order row displayed in the company currency.

#### Price each (company currency)
If the currency on the order differs from the company currency, you can in this column see the unit price displayed in the company currency.

#### Send for authorization
If you change something that affects the order row's amount (quantity, price each, or discount) you can check this box and save the order to send the order row for approval. The order is then available in the Approve purchase order procedure where your head signer can approve the order row.

#### Approved
This box is checked if the order row has been approved. However, you cannot check or uncheck this box.

#### Authorization status
Here you see the order row's authorization status.

#### Latest authorization action
Here you see the order row's latest authorization actions.

#### Approval comment
When you register the purchase order, you can enter a comment to your signer if you have checked the box Send for authorization.

#### Status
Here you see the current status of the order row.

#### Balance
In this field you can see the part’s current stock balance. The field is empty for parts of type Service and parts that are not stock updated.

#### Standard price
For row type 1, you will see the part's current standard price displayed in the company currency. The standard price on the row forms the basis for price differences in, for example, statistics and in the accounting.
For row type 2, you enter a standard price manually.

#### Desired delivery date
The row's desired delivery date is by default set as the same as the current delivery date on a new row. The desired delivery date is the date when we wish to get the delivery. This date can be changed until the point when the order is delivered in full.
The system setting Question when changing delivery date, applies to frozen initial/desired determines if the desired delivery day should be changed when the current delivery day is changed. The available options are:
- No, do not change initial/desired – This option does not provide a question. Initial and requested period are not changed when their respective frozen periods are reached.
- No, change always initial/desired – This option does not provide a question. The initial and requested periods are changed also after they have reached their respective frozen periods.
- Yes, default: do not change initial/desired – If the current period is changed after it is "frozen" you will receive a control question. The default answer to this question is No.
- Yes, default: change initial/desired - If the current period is changed after it is "frozen" you will receive a control question. The default answer to this question is Yes.
Printed purchase order = the "freezing" point for the desired delivery date. Confirmed purchase order = the "freezing" point for the initial delivery date.

#### Initial delivery date
The row's initial delivery date is by default the same as the current delivery date on a new row. The Initial delivery date is the date that first was configured when the row was registered. This date can be changed until the point when the order is delivered in full.
The system setting described above for Desired delivery date also affects the Initial delivery date in the same way.

#### Show prices
With this checkbox you determine if the price each and the amount should be displayed on the purchase order.

#### Remaining quantity
In this field you see how much is left to be delivered for the order row.

#### Delivered quantity
The total of the delivered quantity for the order row.

#### Dispatched quantity
Here you see quantity that is dispatched.

#### Quantity left to inspect
For rows where receiving inspection applies, you will here see the quantity left to perform receiving inspection on.

#### Net weight
If the row is of row type 1, the part's net weight registered in the part register will be displayed by default, but it can be changed on the row. The weight will be displayed in the unit of the order row. This means that a conversion will be made via a conversion factor if the unit on the row is not the standard unit of the part. If the row is a row type 2, you enter the net weight manually.

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

#### Supplier's part number
Here you see the supplier's part number on their corresponding customer order row. This is used on EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. purchase orders.

#### Supplier's order number
Here you see the supplier's order number on their corresponding customer order. This is used on EDI purchase orders.

#### Supplier's order row position
Here you see the supplier's position number on their corresponding customer order row. This is used on EDI purchase orders.

#### Supplier's reference for agreement
Here you see the supplier's reference entered on price agreement. This is used on EDI purchase orders.

#### Supplier's revision
Here you can see the supplier's revision of the part. This is used on EDI purchase orders.

#### Supplier's drawing number
Here you see the supplier's drawing number for the part. This is used on EDI purchase orders.

#### Supplier's action code
Here you see the supplier's action code on their corresponding customer order row. This is used on EDI purchase orders. The available options are:
- Empty – The order row has no action code.
- Registered – The order row has been received and registered by the supplier.
- New – A new order row has been added by the supplier which is not included in our initial purchase order.
- Accepted – The order row has been accepted as it is by the supplier.
- Accepted with changes – The order row has been accepted after it has been changed by the supplier.
- Deleted – The order row has been canceled by the supplier.

#### Blanket order, order number
The blanket order’s order number.

#### Blanket order, initial quantity
The blanket order’s initial quantity.

#### Blanket order, quantity left
The quantity left on the blanket order.

#### Original row quantity
This field is used when you have split a row using the Split row button. The field shows the original row’s quantity before splitting.

#### Split counter
The split counter is a counter value that counts the times a row has been split. Each new split of the original row increases the value by one. The split counter is per part number on the order.

#### Row's goods label
If you create a purchase order from a customer order, then the row's goods label will be included to this field on the purchase order. (If the customer order row's goods label is entered in Register customer order.)

#### CO2e
Here you see the CO2e value from the Part register. You can change the value, if needed. The CO2 e value is used in sustainability calculations.

#### Notes
This field makes it possible to add information for a specific purchase order row.
