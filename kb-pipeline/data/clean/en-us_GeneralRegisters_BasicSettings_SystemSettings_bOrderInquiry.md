### Order/Inquiry

#### Change that will make purchase order row unconfirmed
This system setting determines if a change of Price, Quantity, Revision, Split order row, Delivery date, or All on the order row will automatically uncheck Confirmed or not.

#### Activate the document tab after arrival reporting
This system setting determines if the Documents tab should open automatically. Under this tab you can print transport label after you have saved an arrival reporting in the Report arrival procedure.

#### Fictitious part with price on inquiry/purchase order
If the system setting has been set to Yes a fictitious part will be seen as row type 1 with price on order/inquiry rows. Included parts will be placed on underlying order/inquiry rows with the price set to zero. Additional name, purchase comment, and comment on supplier link are only displayed for the fictitious part.
If the system setting has been set to No a fictitious part will be seen as row type 4 with price set to zero on order/inquiry rows. The name of the part is displayed. Included parts will then instead get row type 1 with price on the order/inquiry rows. Additional name, purchase comment, and comment on supplier link are only displayed for the included part.

#### Merge same material from fictitious parts
If a material (with the same part number) exist on several order rows that belong to several included fictitious parts on a purchase order, these material will be merged into one row when activating this setting.

#### Default posting on additional order row
This system setting determines if and how the posting of additional order rows (row type 2) should be made. The system setting is used to assist when posting additional order rows. The alternative No posting is selected by default. You can also select posting according to standard account or that posting should be made according the order row above.

#### Account string will be copied from the part row above
The system setting is used to assist when posting part rows on inquiries and purchase orders. This system setting is deactivated by default. If you activate the system setting, then accounts and posting dimensions such as cost center will mainly be loaded from the posting matrix. If these are missing in the posting matrix they will instead be copied from the part row above. Posting dimensions are only copied from the row above if this is managed by the account.

#### Posting of setup price is set as posting of the part
This system setting determines if setup price on order row should be posted in the same way as part on order row. If the system setting has not been activated then you must manually configure posting for Setup cost per posting group, product group, and supplier group, under the Purchase account tab in the Posting matrix procedure.

#### Mandatory posting on order row
During purchase order registration, you can enter a purchase account for each order row. This account can be used to assist when posting supplier invoices. This system setting determines if the account field should be mandatory or not on the order row. No is selected by default for this system setting. However, linked purchase order rows are created in the Register manufacturing order or Register customer order procedures. Then a warning appears saying Account must be entered.
If you have selected Yes in the setting and create purchase order from inquiry, a message is shown letting you know an account must be entered in the purchase order.

#### Specification on order row
With this setting you decide if the part number and/or part name should be displayed automatically as a specification on inquiry rows, order rows, and invoice rows. This specification can then be seen in the general ledger after the supplier invoice has been recorded. The purpose is to provide additional information about which goods and services have been purchased, without having to register Part as a separate dimension for posting.
> For this system setting to take effect, it is required that the Specification checkbox has been marked for the purchase account in the Chart of accounts procedure.

#### Number of decimals in price on inquiry, purchase order and supplier invoice
You must at least select two decimals, but you cannot select more than six decimals for unit price. Here you determine how many decimals you want to use (and save in the database) when registering inquiries, purchase orders, and supplier invoices. This system setting also determines how many decimals that will be shown in the column Price each/Setup price on documents.
> If you change the number of decimals in this system setting, already registered order rows will not be affected. The number of decimals on existing order rows will be printed on documents.

#### Approve purchase order
This system setting determines if approve purchase order should be used.
When you have activated this system setting, the users who should be able to save new purchase orders must be added in the General approval settings procedure. For the users who have been added in that procedure, you can here choose if they should be allowed to approve purchase orders.
In the above mentioned procedure you enter authorization limits and select head signers for the users. The head signer has permission to approve the user's purchase orders. It might also be a signer group. If a new purchase order's total amount exceeds the user's authorization limit, the order will be given status 0 (Awaiting manual approval) when the user saves the order. Then you cannot print the order or send it via e-mail. No order rows can be arrival reported. Approval is made by each respective user's head signer in the Approve purchase order procedure. When all order rows on an order have been approved, the order is given status 1 (Registered) and can be handled as usual.
> Please note! If you apply approve purchase order and then configure this setting to No, you still have to approve existing purchase orders that have status 0.

#### Exclude stock driven parts from approval of purchase order
With this setting you decide if order rows with stock driven parts should be excluded from approval.

#### Include part's purchase comment as text row on order/inquiry
This setting determines if the part comment, entered under the Purchase tab in the Part register procedure, should be included on order/inquiry rows. The comments will be printed as additional text on row type 4 under each respective order row. If this system setting is set to Yes, then the system setting below called Show purchase comment on will be activated.

#### Show purchase comment on
This system setting determines if the purchase comment should be displayed as additional text rows (row type 4) on inquiry/purchase order rows. This system setting is linked to the system setting above.

#### Include part's additional name as text row on order
This setting determines if the part's additional names should be printed as additional text on row type 4 under each respective order row.
> Please note! The possibility to include the additional name as text row on order/inquiry rows can be activated via this system setting but also via a setting in the Document settings procedure. If this has been activated both here and in the Document settings, then there will be duplicates of the additional name on the printout.

#### Default quantity on new order row
This setting determines the default part quantity on new order/inquiry rows. This can be set to 0, 1, or the part's Order quantity (entered in the Part register procedure).

#### Check quantity on order against minimum qty for warehouse
If you configure this system setting, a check will be made of the entered quantity on an order row or inquiry row against the part's minimum quantity in the current warehouse. If the entered quantity is less than the part’s minimum quantity, you will see a warning in the Quantity field.

#### Check if the part exists on a valid inquiry
This system setting determines if a check should be made at the purchase order registration to see if the part on the order row already exists on a valid inquiry to the same supplier, that is, the inquiry has not been finished or converted into an order. If the part is included in an inquiry, a message appears and you can go to the inquiry in question.
The purpose of this setting is to observe existing inquiries. Perhaps you should turn the inquiry into a purchase order instead of registering a purchase order for the part.

#### Check quantity on order against quantity/package
This system setting determines if a check should be made to make sure that the order's quantity is a multiple of the part's quantity/package entered in the Qty/pkg field under the Purchase tab in the Part register procedure. If the entered quantity on the order is not a multiple of the part's quantity/package a warning appears in the Quantity field.

#### Default delivery date on order rows
This system setting determines if the default delivery date on order rows should be set to today or today + lead time.

#### Question when changing delivery date, applies to frozen initial/desired
This system setting determines whether the desired delivery date should be automatically changed if the current delivery date is changed after it is "frozen" for desired delivery date or initial delivery date. You can also choose to display a question whether or not these dates should be changed when the current delivery date is changed. You can choose to change the dates by default.
The "freezing" point for the desired delivery date is reached when the order receives status 2 (printed). The "freezing" point for the initial delivery date is reached when the order receives status 3 (Confirmed).

#### Posting of subcontract purchase according to product group on
This setting determines if posting on order rows for subcontract purchase should be made according to the product group on Subcontract part or Work center A work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations..

#### Quantity on purchase order row (subcontract)
This system setting determines if the quantity shown on the subcontract purchase should be Planned quantity (M-order) or Remaining + reported quantity (M-order). When choosing the first alternative – the default setting – the planned quantity on the purchase order row will be updated if the planned quantity on the manufacturing order's subcontracting row is updated. When choosing the second alternative, the planned quantity on the purchase order row is based on the operation row's remaining quantity – and updated during each reporting.

#### Type of document used when direct printing orders
This system setting determines which type of document should be printed when direct printing orders using the print button in the Register purchase order procedure. The available alternatives are Purchase order, Delivery note (subcontract), and Both.

#### Log outgoing e-mail
This system setting determines that an e-mail log will be created under the Activities tab in the Register inquiry, Register purchase order, or Subcontract documents/Shipped procedures, when someone sends an inquiry or purchase order via e-mail from one of these procedures.

#### Transfer info from causing requirement to purchase order
This system setting determines if causing requirements from customer orders and/or manufacturing orders should be transferred as a row type 4 to the purchase order. It only applies for linked requirement. This system setting also applies if purchase orders are created via purchase order suggestions.
- From manufacturing order – The instruction on the material row is transferred to purchase order suggestion and to the purchase order.
- From customer order – Row type 4 on the order row will be transferred to the purchase order (this only applies to row type 4 that is linked to a main row).

#### Check supplier link for part during order registration
This system setting determines if a check should be made to see if parts on new purchase order rows have a supplier link.
- No – No check is made.
- Yes – A check is made. If the part has no supplier link, a warning appears on the order row.
- Block – A check is made. If the part has no supplier link, an error message appears on the order row and the order cannot be saved.

#### Pre-select "Include" on text rows for purchase order confirmation (M2M)
With this setting you decide if text rows should be marked by default to be included in the import.
- Yes – All text rows will be pre-selected to be included in the import.
- No – No text rows will be pre-selected to be included in the import.
- Only for new rows – Only the text rows that do not already exist on the purchase order will be pre-selected to be included in the import.

#### Update/Create supplier link when importing order confirmation (XML)
With this system setting you decide if you want to update/create a supplier link for the part when importing purchase order confirmation from an XML file via Monitor-to-Monitor. By default, this settings is set to Yes.

#### Use currency from supplier link
This setting determines whether the currency from the supplier link on the part added to a purchase order should be used.
If the first part added to the purchase order has a link to the supplier on the purchase order, this currency will be used for the purchase order.

#### Confirm order when entering supplier's order no.
This setting determines whether the purchase order should be confirmed when you enter the supplier’s order number in the Supplier's order number field in the purchase order header. If the order’s status is 1 (Registered) or 2 (Printed), the Confirmed box is automatically checked.

#### Copy order number to goods label
This system setting determines whether order numbers should be copied to the Goods label, (on the second row).

#### Manage delivery date in order header
With this setting you determine if the Delivery date field should be displayed under Terms under the Header tab. This system setting is deactivated by default. It makes it possible to change the delivery date for the entire order directly in the order header.

#### Default order type
With this setting you decide if the default order type should be According to user or None. If you leave the order type empty during registration, you cannot save until an order type has been selected. This applies to the following procedures: Register purchase order, Register blanket order - Purchase, Register stock order – Purchase, and Register inquiry.

#### Increment of positions
This setting determines how position numbers will increase on inquiries, purchase orders, blanket orders – purchase, and stock orders. The following options are available:
- Ones – 1, 2, 3...
- Tens – 10, 20, 30...
- Hundreds – 100, 200, 300...

#### Recalculate locked positions
When a position number is manually edited, it will be locked. This system setting determines whether locked position numbers will be recalculated when position numbers are recalculated. The following options are available:
- Yes
- No

#### Position numbers when using "Insert new row"
- Insert position number – Recalculate if no available position number – When a new order row is inserted between two existing order rows, this row will be given a new position number between position numbers that are already being used. That way, you can insert several new rows between the original order rows without them affecting the position numbering of the subsequent rows. If there are no available position numbers left and a new row is inserted, all position numbers will be recalculated.
- Insert position number – Manually add position if no available position number­ – When a new order row in inserted between two existing order rows, the new row will be given a position number between the position numbers that are already being used. That way, you can insert several new rows between the original order rows without them affecting the position numbering of the subsequent rows. If there are no available position numbers left and a new row is inserted, the user must manually enter a position number.
- Recalculate all positions – Each time a row is inserted, all position numbers will be recalculated.
This system setting is used if the status for:
- Invoice bases are the equal to or higher than 1 – Registered.
- Inquiries, purchase orders, stock orders – purchase, and blanket orders – purchase are equal to or higher than 2 – Printed.
Otherwise the position numbers are recalculated every time a new row is inserted.

#### Function of "Split row" button in Register purchase order
This setting determines whether a dialog should open when you click the Split row button. In the dialog you can select the quantity, delivery date, position number (depending on the above system settings) and whether the quantity should be taken from the original row. The following options are available:
- Split, no dialog – This is selected by default. If you choose the Split row button in Register purchase order, no dialog opens.
- Split, with dialog – If you choose the Split row button in Register purchase order, a dialog opens where you can select quantity, delivery date, and whether the quantity should be taken from the origin row.

#### Position on new row when splitting order row
This determines the position numbering on a new row when you use the Split row function. The following options are available:
- Calculate new position – This is the default option. The system will calculate a new position when the new row is created.
- Same as on original row – If the order has the status Printed or higher, the suggested number position will be the same as on the original row.

#### Enable temporarily unlocking "Price each" and "Discount"
This setting makes it possible to temporarily lock/unlock Price each and Discount for all rows on a purchase order. A button displaying a padlock is shown in the function menu in Register purchase order when the setting is set to Yes. By using this button you can unlock the Price each and Discount fields on all rows.
