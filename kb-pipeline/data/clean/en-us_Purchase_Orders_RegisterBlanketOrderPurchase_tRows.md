### Rows
Under the Rows tab you can add rows for the parts that are to be ordered in the blanket order in question and information regarding them.
There can be rows on different levels. For example, a part row on level 0 with additional text on level 1. Level 0 is called Main row and level 1 is called Sub-row/Underlying row/Underlying level.
At the bottom of the tab you see a total of the blanket order’s remaining excluding VAT as well as the order’s total excluding and including VAT. All totals are shown in both the blanket order's currency and in the company currency.

#### Position
The position of the first main row is 10 and the next main row added will get position 20 etc. If the order's status is 2 or 5 and you add new main rows between two positions, they will get numbers between the positions. In that way, you can add/insert several new main rows between the positions without them affecting the position numbering of the subsequent rows. However, if there are no available position numbers left and a new main row is added, all the positions will be renumbered. It is not possible to manually renumber the positions.
Only main rows have positions, not sub-rows. To the left of each position with sub-rows there is a button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) you can use to expand/minimize the sub-rows. There is also a button in the toolbar of the box that can be used to expand/minimize all existing sub-rows of the order.

#### Row type
Here you can see/enter the row type of the order row. Row type 1 is entered by default when registering a new order row. The following row types exist for blanket orders (purchase):
- 1) Part row – This row type can only contain parts that are registered in the part register (manufactured and purchased). When you have entered or selected a part number, data from the part will be loaded on the row. Part number is mandatory. If you have added an order row of row type 1, and then not entered or selected a part number, you will see an error symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) in the part number field, and in that mode you cannot save the order, until you fill in the part number.
- 4) Text row – This row type is intended for any additional text you want to enter on the row. A text row can be a sub-row and in that case it belongs to a main row of row type 1 or 2. If the text row does not belong to a main row, it belongs to the order itself. There is a text editor available on the row where you can type and edit texts, attach images and hyperlinks.
> Please note! You cannot register blanket orders with configured and fictitious parts.

#### Show on the following documents
For row type 4 you here find a text editor where you can write and format texts, insert images and hyperlinks. In the part register it is possible to enter a comment in the supplier link. For row type 4 you can click this button and select on which document types the additional text row should be shown. You can select among Inquiry, Purchase order, and Delivery schedule Silf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands.. All document types are marked by default. By using the checkbox at the top you can also select/deselect all documents at the same time.

#### Part
The part number on the row. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard.feature, you can search the part register for parts.

#### Name
For row type 1 the part’s name is automatically loaded from the part register after you have entered the part number. You can change the name on the order. In case the part name is not translated to the language of the mailing address and delivery address, the name will be displayed in the user's language. This also applies to order confirmations and delivery notes.

#### Part type (T)
This column shows a symbol for the type of part loaded on the row. Read more about [part types in the Part register](../../../Stock/Parts/PartRegister/hPartRegister.htm#Artikeltyp).

#### Order's part status (P)
In this column you can see the order’s part status in form of a symbol, except for the status Normal where the field is empty. A tooltip over the symbol displays the part status in text.

#### Quantity
The quantity of the part. The default value here is zero. The field displays two decimals, but it is possible to enter up to six decimals.

#### Called quantity
If calls have been made from the order, the called quantity is displayed in this column.

#### Quantity left
Here you see the quantity left for the order row.

#### Unit
For row type 1, you here see the part's default unit. If several units are registered for the part, you will see the unit selected for purchase order under the button Default units/usage in the Part register. You can change to another unit if the part has several units. If you change to another of the part’s units you will be asked if the quantity should be recalculated according to the entered conversion factor. The price each will also be affected if you change the unit. Unit is mandatory for row type 1.
For row type 2, no unit will be suggested, but you can select among all units in the system. By clicking the X button next to the Unit field, you can delete the unit on this row. It is optional to enter a unit for row type 2.
The unit is always displayed in the user's language. On printouts of purchase orders, the unit is displayed in the language of the mailing address.

#### Price each
Here you enter the price of the part. It can be entered with a maximum of six decimals. The price is always displayed/entered excluding VAT.
For row type 1, the following applies regarding the price on the purchase order row:
- Primarily, the price is loaded from the supplier link, if any. If there is a staggered price in the supplier link, this will be used in cases where there is a staggered price matching the quantity on the order row. Staggered prices appear in italic font. If the quantity on the row is less than the lowest staggered price, the normal price on the supplier link will be used.
- A check will also be made against the valid through date of the price on the supplier link. If the valid through date has passed, you will get a warning. If you at this time has a future price entered, you will be asked if you wish to load the future price.
- If no supplier link exists or if no price has been registered in the supplier link, the suggested price will be zero. Regarding the supplier link, it refers to the supplier on the order, not Supplier code on invoice.
- A warning will be displayed if the currency of the price does not match the currency on the order. The price will be converted to the currency on the order, and the warning shows that the order's exchange rate has been used when converting.
The number of decimals is determined by how many decimals have been entered in the system setting Number of decimals in price on inquiry, purchase order and supplier invoice.

#### Price alternative
Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can choose to use another price than the one current on the order row. Here you see standard price, supplier's supplier links with price, and supplier's part number. You can select among all of these prices. All properties from the selected supplier link will then be loaded to the row.

#### Price comment
If there is a price comment on the supplier link, this will be displayed when the part number is entered on the order row.

#### Discount
The discount that applies for the part on the row. For row type 1, the discount will be suggested based on the following rules: 1) discount in the supplier link, 2) discount from a discount category, 3) discount on the supplier. For row type 2, it is only possible to manually enter a discount on the row. For all row types it is possible to enter another discount on the order row. The discount is always entered in percent.

#### Setup price
The setup price for the part on the row. For row type 1, the setup price entered for the supplier in the supplier link of the part will be suggested, otherwise the field is empty. For row type 2, the field is always empty, but it is possible for you to enter a setup price.
The number of decimals is determined by how many decimals have been entered in the system setting Number of decimals in price on inquiry, purchase order and supplier invoice.

#### Amount
In this column you will see the order row's total amount according to the formula: Quantity × Price each − Discount + Setup price. The amount is shown in the currency of the order.

#### Revision
For row type 1, you will see the part's active revision. You can change among the existing revisions of the part. If the active revision is not selected, the revision will be displayed in italics. By placing the cursor on the revision field, you will see an explanation in a tooltip.

#### Arrival date
Here you see/enter the order row's arrival date. This is by default loaded from the Valid to in the order header.
> Please note! Please note! Rows with the same part must have different Arrival dates.
The More information button
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Supplier's part number
Here you see the supplier's part number on their corresponding customer order row. This is used on EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. purchase orders.
