### Purchase – Behavior
Here you find all settings for the selected behavior.
Import and export

#### Search order, part identity
Click the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to decide in which order the search for part numbers should be performed in Monitor ERP. The available alternatives are Supplier's part number, Other part identity, and Part number in Monitor. By using the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) you can move the alternatives to change the search order. The top alternative is used first. You can also deactivate alternatives that you do not want to use.

#### Search term for supplier identity
Determines on what the search for supplier number in Monitor ERP should be based. The available alternatives are: Alternative supplier number or Supplier number in Monitor.

#### Handling policy for delivery date
Here you determine how the delivery date on order rows should be handled in the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. file when a purchase order is exported and an order confirmation is imported. The following options are available:
- States when the supplier sends the delivery – The delivery date when the supplier should send the delivery. The system considers any transport time, delivery days, and work days. The calculated date is set as delivery date, desired date, and initial date on the order row.
- States when we receive the delivery – (Default) The delivery date when we should receive the delivery. The system sets the date as delivery date, desired date, and initial date on the order row.

#### Use notifications
Here you determine if it should be possible to configure settings for notifications on this behavior. If you choose Yes, this button will be activated ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). By using this button you can configure which roles, groups, and users should receive a notification when an EDI transaction has occurred in the behavior. You configure for which transaction type and transaction status the system should create notifications. The affected users will be notified in the Notifications window, in the Message center on the title bar in Monitor ERP.
In the EDI configurations procedure, you can use notifications on channels in configurations. Then these notifications apply to all EDI transactions in a specific channel, regardless of behavior.

#### Use cross references
Here you determine if cross references should be used in the behavior. If you select Yes, you can use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to select one cross reference for each respective transaction type. One or several cross references must first be registered in the ED channels procedure.
Import

#### Import principle for business transactions
Here you decide if all order rows or if individual order rows in the order confirmation in the import file, must be matched before the business transaction is updated in Monitor ERP. The available options are:
- Only complete business transactions – All rows on an order confirmation in an import file must match with parts in Monitor ERP.
- Allow parts of business transactions – At least one row on an order confirmation in an import file must match with a part in Monitor ERP.

#### Matching principle for orders and rows
With this setting you decide how order rows in a purchase order in Monitor ERP should be matched with order rows in the order confirmation. The available options are:
- Match entered orders and rows – This is used in cases where there are references to purchase order and order row in the import file. The supplier's order row position on an order confirmation is matched with the supplier’s order row position of the order rows in Monitor ERP.
- Match and fit – This is used in cases where the import file does not have a reference to purchase order and order row. It will match the open purchase orders available for the supplier in question and the part, and the advised quantity will be distributed/fitted to these orders.

#### Limit "Match and fit" to specific order types
With this setting you decide if "match and fit" should be limited to specific order types when you match orders and rows. The setting is only available when the matching principle for orders and rows has been set to "Match and fit". The order types you can select are based on the Buy material basic type. Order types must be registered in the Order types procedure.

#### Limit "Match and fit" to specific warehouse
With this setting you decide is "match and fit" should be limited to specific warehouses when you match orders and rows. The setting is only available when the matching principle for orders and rows has been set to "Match and fit".

#### Matching principle for order rows
With this setting you decide how order rows in a purchase order in Monitor ERP should be matched with order rows in the order confirmation. You can configure to match with one or both alternatives. By using the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) you can move the alternatives to change the search order. The top alternative is used first. If no matching is successful with that alternative, another matching attempt will be made with the other alternative. The available options are:
- Supplier's order row position – The supplier's order row position on an order confirmation is matched with the supplier’s order row position of the order rows in Monitor ERP.
- Position in Monitor – The supplier's order row position on an order confirmation.

#### Order type
Here you determine which order type should be set on new purchase orders that are created when importing order confirmations. You can choose from the order types for purchase order that are registered in the Order types procedure.
A new purchase order is always created if the setting Always create new orders from purchase order confirmation below is set to Yes, or is set to Only if matching orders are missing and no match is made on the purchase order number in the order confirmation in the import file.

#### Received text rows
Here you determine how text rows should be handled in the import file. The following options are available:
- Add – All text rows are added as new text rows on purchase orders.
- Skip – (Default) No text rows are added to purchase orders.
- Add if the text doesn't exist – A text row is added if no matching text rows exist on the purchase order. If the text row is an underlying text row, it will be added to the order row's position if no matching underlying text rows exist.

#### Payment terms
Here you determine if and how payment terms on purchase orders should be updated from payment terms in the import file. The following options are available:
- Update from file – The payment term is always updated from the payment term code in the file.
- Skip – (Default) The payment term is never updated.
- Update from file if the value is a match – The payment term is only updated if matching is made of the payment term code in the file.

#### Delivery terms
Here you determine if and how delivery terms on purchase orders should be updated from delivery terms in the import file. The following options are available:
- Update from file – The delivery term is always updated from the delivery term code in the file.
- Skip – (Default) The delivery term is never updated.
- Update from file if the value is a match – The delivery term is only updated if matching is made of the delivery term in the file.

#### Delivery methods
Here you determine if and how delivery method on purchase orders should be updated from delivery method in the import file. The following options are available:
- Update from file – The delivery method is always updated from the delivery method code in the file.
- Skip – (Default) The delivery method is never updated.
- Update from file if the value is a match – The delivery method is only updated if matching is made of the delivery method in the file.

#### Currency code
Here you determine if and how currency code on purchase orders should be updated from currency code in the import file. The following options are available:
- Update from file – The currency code is always updated from the currency code in the file.
- Skip – (Default) The currency code is never updated.
- Update from file if the value is a match – The currency code is only updated if matching is made of currency code in the file.

#### Project
Here you determine if and how project number on purchase orders should be updated from project number in the import file. The following options are available:
- Update from file – The project number is always updated from the project number in the file.
- Skip – (Default) The project number is never updated.
- Update from file if the value is a match – The project number is only updated if matching is made of project number in the file.

#### Supplier's reference on imported business transaction
Here you determine if and how the supplier's reference on purchase orders should be updated from the import file. The following options are available:
- Update from file – Supplier's reference is always updated from the reference in the file.
- Skip – (Default) Supplier’s reference is never updated.

#### Goods label
Here you determine if and how goods label in the header and on the rows on purchase orders should be updated from the import file. The following options are available:
- Update from file – Goods label is always updated from goods label in the file.
- Skip – (Default) Goods label is never updated.

#### Price strategy
Here you determine if and how price on purchase order rows should be updated from price in the import file. The following options are available:
- According to imported file – Price is updated from price in the file. A price must exist in the file.
- Skip – (Default) Price is never updated.
- Update, if the value exists in the file – Price is only updated if price exists in the file.

#### Setup price strategy
Here you determine if and how setup price on purchase order rows should be updated from setup price in the import file. The following options are available:
- According to imported file – Setup price is updated from setup price in the file. A setup price must exist in the file.
- Skip – (Default) Setup price is never updated.
- Update, if the value exists in the file – Setup price is only updated if setup price exists in the file.

#### Reference to price agreement
Here you determine if and how the supplier's reference to agreements on purchase order rows should be updated from the corresponding information in the import file. The following options are available:
- According to imported file – The supplier's reference to agreements are updated from the corresponding information in the file. This information must exist in the file.
- Skip – (Default) Supplier’s reference to the agreement is never updated.
- Update, if the value exists in the file – Supplier’s reference to agreement is only updated if the corresponding information exists in the file.

#### Discount strategy
Here you determine if and how discount on purchase order rows should be updated from discount in the import file. The following options are available:
- According to imported file – Discount is updated from discount in the file. Discount must exist in the file.
- Skip – (Default) Discount is never updated.
- Update, if the value exists in the file – Discount is only updated if discount exists in the file.

#### Check of unit on part row
Here you determine if and how a check of unit on part row should be made in the import file. You also determine how it should be handled, if the part's unit is not found for the part in Monitor ERP or for the linked ISO code for the unit in Monitor ERP. The following options are available:
- Check and mark as error – The row is marked as error and will not be imported.
- Check and warn – (Default) The row is marked with a warning but will be imported.
- Do not check – No check is made of the row. The part's row is ignored and will not be used.

#### Approve manually at import
Here you select Yes if validated EDI transactions must be manually approved during import in the Manage EDI transactions procedure. After the approval, the business transactions will be created in Monitor ERP. The default alternative is No. Then the business transactions will be created automatically during import.

#### Identify split rows in order confirmations
This setting determines whether split rows should be identified in the imported order confirmation. The following options are available:
- Yes – Split rows are identified and these rows are added to the purchase order as split rows. The splits are counted and the source row quantity remains the same.
- No – Split rows are not identified and are instead added to the purchase order as “normal” rows. The splits are not counted and the source row quantity remains the same. This is the default option.

#### Check revision
Here you determine how and if a check of revision for the part should be made in the import file. The following options are available:
- Check and mark as error – During import, an error message appears if the part's revision is not found in Monitor ERP.
- Check and warn – (default) During import, a warning message appears if the part's revision is not found in Monitor ERP.
- Do not check – No check is made during import. The part's revision is accepted even if it is not found in Monitor ERP.

#### Always create new orders from purchase order confirmation
Here you determine if new purchase orders always should be created from purchase order confirmation in the import file. The following options are available:
- No – (Default) No new purchase orders are created from order confirmations.
- Only if matching orders are missing – If purchase order number in the import file does not match with any purchase order number in Monitor ERP, a new purchase order will be created.
- Yes – New purchase orders are always created from order confirmations.

#### Order number
Here you determine the order number for a new purchase order you create in Monitor ERP. The available options are:
- According to imported order – The purchase order is assigned the order number included in the import file.
- According to Monitor – The purchase order will be assigned an order number from the number series in Monitor ERP.

#### Status on new purchase order
Here you determine which status should be set on new purchase orders that are created when importing order confirmations. The following alternatives are available Registered and Confirmed (default).

#### Allow to create new part row on purchase order
Here you determine if new order rows (row type 1 and 2) should be allowed to be created or not on the purchase order in Monitor ERP. This applies when no match is made of part on the same order row position in the order confirmation in the import file. A common case when no matching is made is when a new order row has been split into two rows. Then no matching will be made on the added order row. The following options are available:
- No – (Default) No orders rows are created. This mean that a purchase order row must be manually adjusted in the Manage EDI transactions procedure. This applies when the import file contains an order row position with a part number that is not matched against the same part number and order row position on the purchase order.
- Yes, if the part matches an existing part on the purchase order – If the part number on an order row in the import file matches an existing part number on a row on the purchase order, a new purchase order row is created.
- Yes – A new purchase order row is created for part number on an order row in the import file. This also applies even if no matching is made on an existing part number on a row on the purchase order.

#### Allow order confirmations only containing header information
Here you determine if order confirmations that only contain information in the order header should be allowed during import. That is, order confirmations without any information on the order rows. The following options are available:
- No – (Default) This means that when an order confirmation without any part rows is imported, an error will be reported for the transaction indicating that there are no part rows in the transaction.
- Yes – This means that when a referred purchase order in Monitor ERP is matched when importing the order confirmation, the entire purchase order including the order rows will be set to confirmed. If the referred purchase order is not matched, an error occurs indicating that a purchase order was not found. In order to confirm the order and order rows, you must manually adjust the transaction and select correct purchase order.

#### Warehouse strategy
If you are using the Warehouse option, this setting is available to determine how warehouse should be handled during import of order. The following options are available:
- According to imported order – The warehouse included in the import file will be used. If no warehouse is stated in the import file or if the warehouse in the import file does not match an existing warehouse, the warehouse entered in the system setting called Default warehouse for EDI will primarily be used, and secondarily the company's default warehouse will be used. The Warehouse setting found below is in this case deactivated.
- According to Monitor – Warehouse is set according to the system setting called Default warehouse for EDI. Secondarily, the company's default warehouse is selected. The company's default warehouse is the default option for this system setting. The Warehouse setting found below is in this case deactivated.
- Enter warehouse – With this option you have to enter a warehouse in the next setting called Warehouse.

#### Warehouse
If you selected the Enter warehouse option in the setting above, you must here select a warehouse.
Export

#### Printout/e-mail during export of EDI
Here you determine if it should be possible to print to printer or send via e-mail during export of EDI messages. The default alternative is No.

#### Use buyer's ID as identity for the goods receiver
Here you determine if and how the buyer's identity should be set as goods receiver in the export file for purchase order. The following options are available:
- No – The buyer's identity is never set as goods receiver.
- Always – The buyer's identity is always set as goods receiver.
- Only if delivery address is not linked to another party – The buyer's identity is set as goods receiver only when the delivery address is not loaded from another party. Thar is, when the field Select delivery address from is empty. This field is found by using the button Change delivery address in the order header.
