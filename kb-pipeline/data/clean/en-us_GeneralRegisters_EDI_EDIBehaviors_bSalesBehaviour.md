### Sales – Behavior
Here you find all settings for the selected behavior.
Import and export

#### Search order, part identity
Click the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to decide in which order the search for part numbers should be performed in Monitor ERP. The available alternatives are Customer's part number, Other part identity, and Part number in Monitor. By using the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) you can move the alternatives to change the search order. You can also deactivate alternatives that you do not want to use.

#### Search term for customer identity
Determines on what the search for customer number/delivery address in Monitor ERPshould be based. The available options are:
- Alternative customer number – Alternative customer number is used in Monitor when searching for customers.
- Customer number in Monitor – The customer number in Monitor is used when searching for customers.
- Alternative customer number and Our supplier number – This option adds an additional validation step for searching customers in cases where customers use the same alternative customer number. If two or more customers have the same alternative customer number, the sales ID from the imported file will be used and matched to the Our supplier number field in the customer register in order to find out which customer should be used for the import.

#### "Our supplier number" is mandatory
This setting is available when the option called Alternative customer number and Our supplier number has been selected in the Search term for customer identity setting. When importing customer order it is verified that the matching customer has a value in the Our supplier number field. The following options are available:
- Yes – Means that when the field Our supplier number is empty, a validation will be made when importing customer order.
- No – Means that when the field Our supplier number is empty, no validation will be made when importing customer order.

#### Handling policy for delivery date
Here you determine how the delivery date on order rows in the import file with customer orders or delivery schedules should be handled when actual customer orders are created. The following options are available:
- States when we send the delivery – (Default) The delivery date when the supplier (we) should send the delivery. The system sets the date as delivery date, desired date, and initial date on the order row.
- States when the customer receives the delivery. – The delivery date when the customer should receive the delivery. The system calculates the supplier's (our) delivery date on the order row in Monitor ERP. This works in the same way as when you enter a value in the field At customer on the order row. The system considers any transport time, delivery days, and work days. The calculated date is set as delivery date, desired date, and initial date on the order row.

#### Use notifications
Here you determine if it should be possible to configure settings for notifications on this behavior. If you choose Yes, this button will be activated ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). By using this button you can configure which roles, groups, and users should receive a notification when an EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. transaction has occurred in the behavior. You configure for which transaction type and transaction status the system should create notifications. The affected users will be notified in the Notifications window, in the Message center on the title bar in Monitor ERP.
In the EDI configurations procedure, you can use notifications on channels in configurations. Then these notifications apply to all EDI transactions in a specific channel, regardless of behavior.

#### Use cross references
Here you determine if cross references should be used in the behavior. If you select Yes, you can use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to select one cross reference for each respective transaction type. One or several cross references must first be registered in the ED channels procedure.
Import

#### Import principle for business transactions
Here you determine if all or individual order rows in customer orders, or all or individual calls in delivery schedules must match before actual customer orders can be created in Monitor ERP. The available options are:
- Only complete business transactions – All rows on an order, or all calls in a delivery schedule in an import file must match with parts in Monitor ERP.
- Allow parts of business transactions – At least one row on an order, or one call in a delivery schedule in an import file must match with one part in Monitor ERP.

#### Order type
Determines which order type should be used for the actual customer orders that are created. You can select among the order types registered in the Order types procedure.

#### Order number
Determines the order number on actual customer orders created in Monitor ERP. The available options are:
- According to imported order – The customer order is assigned the order number included in the import file.
- According to Monitor – The customer order is assigned an order number from the number series in Monitor ERP.

#### Check customer's order number
Here you determine which check principle should apply to the customer's order number in the import file. The setting applies when the setting above called Order number has been set to According to Monitor. The available options are:
- Reject duplicates – The order will not be created if an order with the same customer's order number already exists in Monitor ERP for the same customer. In Manage EDI transactions, the business transaction will be shown with status error and an error message.
- Allow duplicates – The order will be created if an order with the same customer's order number already exists for the same customer. If a duplicate is matched this will create an item in the event log. This makes it possible to trace, if needed. The business transaction will not be shown with status error or an error message in Manage EDI transactions.

#### Our reference on imported order/delivery schedule
Determines the name that will be shown in the Our reference field on the actual customer orders that are created. The available options are:
- Enter our reference – our reference who is selected in the field below.
- Seller – The person who is entered as seller for the customer in the customer register.
- According to imported order – the person who is our reference on the order in the import file. This option cannot be selected for delivery schedules.

#### Our reference
Here must select a person among our references. This person will then be used on actual orders provided that you have selected the alternative Enter our reference in the setting above.

#### Seller
Here you determine if the seller on the order should be set According to imported order or According to Monitor.

#### Delivery methods
Here you determine if delivery method on the order should be set According to imported order or According to Monitor.

#### Delivery terms
Here you determine if delivery terms on the order should be set According to imported order or According to Monitor.

#### Payment terms
Here you determine if payment terms on the order should be set According to imported order or According to Monitor.

#### Currency code
Determines which currency code should be used on actual customer orders that are created. The available options are:
- According to imported order – The currency code included in the import file will be used.
- According to Monitor – The currency code set on the customer in Monitor ERP will be used.

#### Goods receiver
Determines which goods receiver should be used on actual customer orders that are created. The available options are:
- Find other customer according to code in file – A search is made in the customer register in Monitor ERP for the goods receiver code in the import file. This customer's regular delivery address will be used as delivery address from Other customer.
- Use delivery address from imported order – The delivery address included the import file will be used.
- According to Monitor – The delivery address set on the customer in Monitor ERP will be used.
- Find other customer, but keep address from file – A search is made in the customer register in Monitor ERP for the goods receiver code in the import file. The delivery address included in the import file will be used.
- Find Alt. del. address according to code in file – Using this option, a search is carried out among the already matched customers’ alternative delivery addresses in Monitor ERP for the goods receiver code in the import file. The matching alternative delivery address will be used as the delivery address from the current customer.

#### Price strategy
Here you decide how the price each on the order row should be set. The available options are:
- According to imported order – The order row is given a price from the part row in the import file. This will override the price strategy that is selected on the order type. If the price is missing in the import file, the row will be shown with status error in the Manage EDI transactions procedure.
- According to Monitor – The order row is given a price according to the price strategy that is selected on the order type in Monitor ERP.

#### Discount strategy
Here you decide how the discount on the order row should be set. The available options are:
- According to imported order – The order row is given a discount from the part row in the import file.
- According to Monitor – The order row is given a discount according to the built-in discount management in Monitor ERP.

#### Check of unit on part row
Here you determine if and how a check of unit on part row should be made in the import file. You also determine how it should be handled, if the part's unit in the import file is not the found for the part in Monitor ERP or to linked ISO code for the unit in Monitor ERP. The following options are available:
- Check and mark as error – (default) the row will not be imported.
- Check and warn – the row will be imported.
- Do not check – No check is made of the row. The part's row is ignored and will not be used.

#### Approve manually at import
Here you select Yes if validated EDI transactions must be manually approved during import in the Manage EDI transactions procedure. After the approval, the business transactions will be created in Monitor ERP. The default alternative is No. Then the business transactions will be created automatically during import.

#### Check revision
Enables revision checks when importing customer orders. The following options are available:
- Check and mark as error – If the part in Monitor ERP has revisions, the order row will be marked as containing errors if the revision in the file does not match with an existing revision for the part. The order row will not be imported. If the revision match an existing, but not active, revision it will be indicated with a warning, and the order row will be created with the revision from the file.
- Check and warn – If the part in Monitor ERP has revisions, a warning message will appear notifying you that the revision in the file does not match with an active revision for the part. If the revision match an existing, but not active, revision the order row will be created with the revision from the file. If the revision does not match an existing revision the order row will be created with the part’s active revision.
- Do not check – The default option. The active revision from the part in the part register is used on the order row.

#### Delivery schedule type
Here you decide which delivery schedule type should be used. You register these in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Delivery schedules procedure.

#### Show delivery schedule transfer errors
Here you decide if errors which occurred during transfer of delivery schedule to customer order (in connection with EDI import), should be displayed with an error symbol on the business transaction in the Manage EDI transactions procedure. The setting is deactivated by default.

#### Warehouse strategy
This setting is available if the option Warehouse is installed in your system. The setting determines how a warehouse entered in order header and on order row should be handled if such exist in the import file when actual customer orders are created. The following options are available:
- According to imported order – Order header and order row in Monitor ERP are assigned warehouse from the import file. If the warehouse in the import file cannot be matched with a warehouse in Monitor ERP, an error message will occur during import.
- According to Monitor – Order header and order row in Monitor ERP are assigned warehouse according to the business logic in Monitor ERP.
- Enter warehouse – Order header and order row in Monitor ERP are assigned the warehouse entered in the setting below.

#### Warehouse
If you seleced the Enter warehouse option in the setting above, you must here select a warehouse for the EDI behavior.

#### Handling of delivery days
Determines how the customer's delivery days should be handled on actual customer orders that are created. The available options are:
- Do not take customer's delivery days into consideration – The delivery date included in the import file is set as delivery date on the order row.
- Adjust the delivery date according to the customer's delivery days – Before the delivery date included in the import file is entered as delivery date on the order row, it will be adjusted to fall on the customer's delivery day closest to the delivery date.

#### Matching principle for orders
This applies if Matching principle for orders and rows has been set to Match entered orders and rows. This setting determines the search order for customer order in the import file when matching with customer order in Monitor ERP. You can configure to match with one or both alternatives. By using the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) you can move the alternatives to change the search order. The top alternative is used first. If no matching is successful with that alternative, another matching attempt will be made with the other alternative. The available alternatives are: Customer's order number and Order number in Monitor.

#### Matching principle for order rows
This applies if Matching principle for orders and rows has been set to Match entered orders and rows. This setting determines the search order for order rows in the import file when matching with order rows order in Monitor ERP. You can configure to match with one or both alternatives. By using the buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up.png) and ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) you can move the alternatives to change the search order. The top alternative is used first. If no matching is successful with that alternative, another matching attempt will be made with the other alternative. The available alternatives are: Customer's order row position and Position in Monitor.
Import: Customer order change

#### Use frozen period for customer order change
With this setting you select if frozen period should be used for customer order change. If frozen period is applied it means that you cannot make changes to order rows that have a delivery date within the frozen period. The available options are:
- No – Frozen period is not applied.
- Yes – Frozen period is applied.

#### Frozen period for customer order change
This setting becomes available if the Use frozen period for customer order change setting has been set to Yes. Here you enter how long (in number of days) the frozen period should be.

#### Assign order status "Preliminary" after import of order change
With this setting you decide of the order should be assigned Preliminary status after import of order change. The available options are:
- Yes – The Preliminary status of the order remains unaltered after import of order change.
- No – The Preliminary status of the order will be assigned after import of order change.

#### Allowed actions (on order row)
Here you select which actions should be allowed to be performed related to the import of customer order change. You can choose one or several actions:
- Added – New rows are allowed to be added.
- Changed – It is allowed that changes to existing order rows are made.
- Canceled – Order rows are allowed to be canceled. Please note! To be able to cancel order rows, you must have option 247 installed in your system.
Import: Delivery schedule

#### Use skip list for parts
This setting determines whether Skip lists for parts should be used. Under the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button, you select the desired skip list. Skip lists for parts can be created in the EDI channels procedure.
Import: Delivery reporting
The settings in this section are available if the EDI import format called Sales – Customer order delivery reporting is installed. This format is used, for example, in cases where Company A has a subsidiary B or an external storage which delivers directly to the end customer, and Company A needs to import the reported deliveries to give the corresponding customer orders the status "Delivered".

#### Matching principle for orders and rows
Here you decide how reported deliveries of customer order in the import file are matched with the corresponding customer order in Monitor ERP. The available options are:
- Match entered orders and rows – This principle is used if order row and customer order are entered in the import file and thereby should be matched with the corresponding order row and customer order in Monitor ERP. Related to this principle you also configure Matching principle for orders and Matching principle for order rows.
- Match and fit – This principle is used if order row and customer order is not entered in the import file. Matching of orders and order rows will then only be made on customer and part in Monitor ERP. The delivered quantity will then be distributed to (make to fit) the available order rows for the matched customer and part. Related to this principle you also configure the following settings: Matching of dock and storage, Matching of customer's order number and Limit "Match and fit" to specific order types.

#### Matching of dock and storage
This applies if Matching principle for orders and rows has been set to Match and fit. Here you decide if dock or both dock and storage must match or not with the available order rows in Monitor ERP. The available alternatives are: Dock and storage must match, Port must match or Do not take dock and storage into consideration.

#### Matching of customer's order number
This applies if Matching principle for orders and rows has been set to Match and fit. With this setting you determine if the customer's order number in the import file must match or not with the available order rows in Monitor ERP. The available alternative are: Do not match on customer's order number and Customer's order number must match.

#### Matching of other reference fields
This applies if Matching principle for orders and rows has been set to Match and fit. Matching of other reference fields makes it so that order rows can be matched with reference fields for Kanban number, Reference number for delivery­, and/or Reference number for manufacturing. None of these options are selected as standard.

#### Warehouse strategy – Delivery reporting
This setting is available if the option Warehouse is installed in your system. With this setting you decide how warehouse should be handled regarding matching of order and order row during import of reported deliveries on customer order. The available options are:
- According to imported order – The warehouse on the order and order rows in the import file will be used on matched orders and order rows in the same warehouse in Monitor ERP. If this warehouse does not exist in Monitor ERP or if warehouse is missing in the import file, an error message is displayed in the transaction.
- Enter warehouse – The selected warehouse in Monitor ERP in the field below will be used on matched orders and order rows, even though warehouse is missing in the import file or is an unknown warehouse.

#### Warehouse
If you have selected the Enter warehouse option in the setting above, you must here select the warehouse in Monitor ERP that should be used on matched orders and order rows in the import file.

#### Check external delivery note number
Here you decide if the check of external delivery note numbers in the import file should allow duplicates to be created or not, if the external delivery notes numbers already exist in Monitor ERP. The available alternatives are: Reject duplicates and Allow duplicates.

#### Limit "Match and fit" to specific order types
This applies if Matching principle for orders and rows has been set to Match and fit. With this setting you determine that only order rows of the selected order types, will be included when matching and fitting.
Export

#### Printout/e-mail during export of EDI
Here you determine if it should be possible to print to printer or send via e-mail during export of EDI messages. The default alternative is No.

#### Export principle for simplified dispatch advice
Here you determine if dispatch advice to receiver should be sent. The available alternatives are Export at delivery planning and Export at delivery reporting. The latter option is selected by default.

#### Export principle for complex dispatch advice
Here you decide if complex dispatch advice should be sent or not. The available alternatives are Export at delivery reporting and Do not export at delivery reporting. The first alternative is selected by default. This means the EDI export column will be set to Yes in the Report delivery procedure. If you select the latter alternative, complex EDI advicing will not take place by default in connection with delivery reporting.

#### Part types to export as invoice rows
This setting determines which part types should generate invoice rows in the export file.
The alternatives Freight, Alloy cost, and Unspecified are service types which applies to parts of type Service. The alternative Packaging applies to parts for which the setting The part is a packaging part has been activated. All alternatives are selected by default.
All purchased and manufactured parts always generate invoice rows in the export file.

#### Ignore search order for the following part types
By using this setting, it is possible to exclude service parts and packaging parts in EDI exports. These validation rules are entered under the setting called Search order, part identity.
You can choose more than one option:
- Service
- Packaging
This setting is deactivated if Part number in Monitor is configured in the setting Search order, part identity.

#### Fields used as basis for order confirmation return status
Here you can select which fields that should be included in the criteria for return status on order rows. The following fields are available:
- Price
- Delivery date
- Quantity
The fields Delivery date and Quantity are marked by default for migrated behaviors. All of these three values are marked for new behaviors.

#### Use order customer's ID as identity for the goods receiver
This setting determines if and how the identity for the goods receiver should be set in the export file. This applies to automatic order responses, order confirmations, simplified dispatch advice, and invoices. The available options are:
- No – (Default) Goods receiver's identity is only set if the delivery address on the customer order is linked to Other customer and this customer has an Alternative customer number in the customer register. Otherwise, this is left empty.
- Always – The alternative customer number on the customer for which the order is registered, is always used as identity for the goods receiver in the export file. This applies even if the delivery address on the order is linked to Other customer.
- Only if delivery address is not linked to "Other customer" – If the delivery address on the order is linked to Other customer, this customer's alternative customer number is used as goods receiver's identity in the export file. Otherwise, the alternative customer number from the customer for which the order is registered will be used.
