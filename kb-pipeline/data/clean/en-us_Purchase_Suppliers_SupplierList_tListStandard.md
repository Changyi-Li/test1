### The Standard list
The Standard list displays different columns depending which presentation you have selected.
Terms/Prices

#### Payment terms
Here you see the payment term that should apply for the supplier on the row. For example 30 days net. You can select among the packaging terms that have been registered in the Terms procedure.

#### Delivery terms
Here you see the delivery term that should apply for the supplier on the row. For example Freight prepaid. You can select among the packaging terms that have been registered in the Terms procedure.

#### Delivery method
Here you see the delivery method that should apply for the supplier on the row. For example Schenker-BTL. You can select among the delivery methods that have been registered in the Terms procedure.

#### Response time
Here you see the response time that should apply for the supplier on the row. For example 3 days. You can select among the response times that have been registered in the Terms procedure.

#### Packaging terms
Here you see the packaging term that should apply for the supplier on the row. For example Pallet. You can select among the packaging terms that have been registered in the Terms procedure.

#### Payment plan
Here you see if a payment plan should be applied for purchase orders for this supplier. The payment plans you can select among must be registered in the Invoicing/Payment plans procedure.

#### Discount
In this column you enter the discount, in percent, that will apply for the supplier in question. This discount will be selected by default e.g. on new order rows.

#### Discount category
Here you see the discount category that will apply for the supplier on the row. You can select the category among the discount category that have been registered in the Terms procedure.
Import/Printouts

#### Language
By default you will here see the language that is linked to the mailing address, but you can select another language. The language selected here will be used e.g. in price lists. However, your selection of language here will not affect the language used on documents. That language is instead determined by the country entered for the order’s mailing address or delivery address. All languages you want to select among in this field must first be registered in the Languages procedure.

#### Currency
The currency entered here will be used by default All currencies you want to select among in this field must first be registered in the Currencies procedure. All amounts will be converted to the selected currency, for example on orders.

#### Date format
Here you select the date format that you wish to use when communicating with the company in question. For example YYYY-MM-DD.

#### Decimal separator
Here you select whether you wish to use period or comma as decimal symbol when communicating with the company in question.

#### Time zone
Here you select the time zone where the company in question is located. The default time zone in the field is the same as has been entered for the own company in the Company information procedure.

#### Print order/inquiry via
With this setting you determine if printout of purchase order and inquiry should be made using a printer or via e-mail. The method you select here will be the default option for purchase orders and inquiries to the supplier in question.

#### Print statement via
With this setting you determine if printout of the statement should be made using a printer or via e-mail. The method selected here will be the default for statements to the supplier in question.

#### Print delivery note/transport label via
With this setting you determine if printout of delivery note (for subcontract) and transport label should be made using a printer or via e-mail. The method you select here will be the default option for delivery notes and transport labels to the supplier in question.
Receiving inspection

#### Receiving inspection
In this field you select whether or not receiving inspection should be performed for purchase orders delivered from the supplier.
XML/Documents
Variants of different documents are created in the Document templates procedure. If you do not make any selections here, then the default document variants in the procedure in question will be used.

#### Order as XML
With this checkbox you decide if an XML file should also be attached when sending purchase orders via e-mail to the supplier.

#### Delivery schedule as XML
With this checkbox you decide if an XML file should also be attached when sending delivery schedules via e-mail to the supplier.

#### Case as XML
With this checkbox you decide if an XML file should also be attached when sending cases via e-mail to the supplier.

#### Inquiry
Here you decide which document variant should apply for inquiries to the supplier on the row.

#### Purchase order
Here you decide which document variant should apply for purchase orders to the supplier on the row.

#### Delivery schedule – Purchase
Here you decide which document variant should apply for delivery schedules to the supplier on the row.

#### Purchase order (subc.)
Here you decide which document variant should apply for purchase orders (subcontracts) to the supplier on the row.

#### Delivery note (subc.)
Here you decide which document variant should apply for delivery schedules (subcontracts) to the supplier on the row.

#### Comprehensive purchase order (subc.)
Here you decide which document variant should apply for comprehensive purchase orders (subcontracts) to the supplier on the row.

#### Comprehensive delivery note (subc.)
Here you decide which document variant should apply for comprehensive delivery notes (subcontracts) to the supplier on the row.

#### Claim report
Here you decide which document variant should apply for claim reports to the supplier on the row.

#### Waybill
Here you decide which document variant should apply for waybills to the supplier on the row.
Delivery/Shipping

#### Delivery days
Here you configure specific weekdays as delivery days. If no days are selected, all the days of the week will be delivery days. The effect is the same as if all the days are selected. If some days are selected as delivery days, this will affect the delivery date when registering orders.
For purchase orders, the delivery date suggested (finish date for subcontracts) will be the date closest back in time that is a delivery date for the supplier. For all purchase orders, the delivery date always refers to the day of the week when the delivery will arrive to the factory, regardless of transport time.
If you change the suggested delivery date on an order, a validation will be made against the entered delivery days. A warning will be displayed if the delivery date is not a day you have entered as a delivery day.

#### Transport time
Here you enter the transport time in number of work days (only whole numbers). The transport time refers to the time it takes to transport the goods from the sender to the receiver. The transport time also affects the delivery date printed on the documents and the text printed as an explanation to the delivery date, according to the following:
- If a transport time has been entered, the purchase order document will read “Del. date = shipped from your warehouse (transport time: X work days)”.
- If no transport time is entered, the purchase order document will have the text “Del. date = arrival our warehouse”.

#### Allowance too early/too late
Here you enter the allowance for deliveries made too early and too late in number of work days. The value is used when calculating the supplier’s delivery reliability towards you. That is, how many days the delivery can differ (in number of days) and still be considered to be “on time”.

#### Destination
You only need to enter a destination if it is not the same as the city entered in the delivery address.

#### Place of terms of delivery
You only need to enter the place of terms of delivery if it is not the city entered in the delivery address. The place of terms of delivery indicates the place or city where the financial responsibility for the shipped goods will pass to another party.

#### Cumulative quantity, start date
Determines from which date the arrival reported quantity of different parts from the supplier should be added together separately per part. The date and the cumulative quantity are shown in delivery schedules to the supplier. The cumulative quantity's start date can also be entered in supplier links for parts. In that case, the date in the supplier link will override the date you have entered here.

#### Indicate lagging orders
The setting in this column determine if lagging purchase orders should be indicated in delivery schedules to the supplier. Lagging purchase orders are orders that you have not yet had delivered from the supplier, but which should have been delivered. The available alternatives are:
- Indicate lagging purchase order rows
- Do not indicate lag
Outgoing payments

#### Payment method
Here you select the payment method that should be used when making payments to the supplier in question. You can select between the payment methods registered in the Bank settings procedure. There you can edit and/or add payment methods. This field is mandatory and cannot be left empty.

#### Pay via
Here you can enter another supplier number if the payment should be made via another supplier. By default this field will contain the same supplier number as in the main row, but it can be changed.
Exceptions

#### Account for outgoing payments
Here you select an account for the supplier that will be used for outgoing payments to the supplier. If no account for outgoing payments to the supplier has been selected here, the outgoing payments will instead be recorded against the account linked to the payment method selected at the time of the payment.

#### Purchase account
Here you enter an account for the supplier that will be used when registering expense invoices (without purchase order) from the supplier. This account will then be suggested for posting in the Register supplier invoice procedure.

#### Offset account for accruals
Here you select the offset account (expense account) that should be suggested by default when registering an accrual for the supplier.
SRM - Supplier Relationship Management

#### District
Here you can select a district for the supplier. District can be used e.g. as a selection term in different lists.

#### Purchasing agent
Here you can select a purchasing agent, that is, a person responsible for purchases made from the supplier. This can be selected among employees that have been registered as such.

#### Type
The supplier type describes e.g. in which line of business the supplier is active, or what kind or service the supplier is providing. The supplier type can e.g. be used as a selection term in different lists.

#### Supplier status
The supplier status describes the status/relationship that you currently have with the supplier in question. The status of the supplier might be an actual supplier (which you can register orders to), or it might be a potential supplier, etc.
Miscellaneous

#### Supplier role
In this field you can select one or several roles for the supplier. These terms can then be used in several places in the system, e.g. when selecting suppliers in lists. The following alternatives are available:
- Material supplier – Check this role for suppliers from which you buy material. This alternative is selected by default.
- Subcontract – Check this role to label your subcontract suppliers.
- Shipping agent – Check this role to indicate that the supplier in question offers shipping services. If you check this alternative, additional fields will become available to the right.
- Miscellaneous – Check this role for suppliers that do not match any of the other alternatives.

#### Priority
Here you can see a priority for the supplier. The priority can be 1-9. This priority is always combined with the order type's priority when the priority of a new order is decided. The highest priority (lowest number) of either the order type's priority or the supplier's priority, is then the priority that will be set for the order. For a new supplier the default priority is 9.

#### Supplier group
Here you see the supplier group for the supplier. You can select among the supplier groups that have already been registered in the Posting matrix procedure. The supplier group you select determines the posting of orders and invoices, and also the VAT code on order rows.

#### VAT group
Here you see the VAT group for the supplier. VAT groups must first be registered in the VAT settings procedure. The VAT group determines which VAT code should be used by default on orders.

#### VAT registration number
Here you can enter the supplier’s VAT registration number. If the entered number is already used by another supplier, a message appears.

#### Corporate ID number
Here you enter the supplier’s corporate ID number. If the entered number is already used by another supplier, a message appears.

#### Category
In this field you can enter categories for the suppliers. By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select categories. These must first be registered in the Categories procedure.

#### Our customer number
Here you enter our own customer number registered at the supplier. This is shown on the documents that are sent to the supplier.

#### Supplier number on invoice
If you want another supplier number to be printed on invoice bases after arrival reporting, you should enter it in this field. The supplier number on invoice is used e.g. when the purchase order has been sent to one company but it is invoiced from another company, for example from a central storage etc.

#### Authorized signer
Here you enter who is the authorized signer. This person is then automatically used as authorized signer of supplier invoices from the supplier in question.

#### Calendar
Here you see the calender number of the calendar linked to the supplier. It is possible to change calendar in the updateable mode.

#### Signer code (with EIM)
If you have installed the option EIM, this column is displayed instead of the column mentioned above. You here enter a code for the person or for the list of persons that are authorized signers. This will be used by default on supplier invoices from the supplier in question.

#### Do not create invoice basis
This setting is only visible if you have checked any of the alternatives for the system setting called Create invoice basis at arrival of. If the checkbox is activated, it is not possible to link orders to supplier invoices from the supplier.

#### Stray supplier
Here you see if the supplier is marked as stray supplier. A stray supplier is a supplier number used for one-time purchases from different physical suppliers that you therefore do not want to register in the supplier register. For suppliers marked as stray suppliers, you fill in all the fields on the order instead. Reminders, if any, for that supplier number will be divided per order, and they will not be gathered in one reminder, as otherwise, when this setting is not selected. That way, you can separate the reminder printouts for the different physical suppliers.

#### Internal (stock order)
Here you see if the supplier is an internal supplier used on stock orders for purchase. This columns is available if you have installed the option Warehouse.

#### Website
Here you can enter the address (URL) to the supplier's website.

#### Order as XML
With this checkbox you decide if an XML file should also be attached when sending purchase orders via e-mail to the supplier.

#### Delivery schedule as XML
With this checkbox you decide if an XML file should also be attached when sending delivery schedules via e-mail to the supplier.

#### Case as XML
With this checkbox you decide if an XML file should also be attached when sending cases via e-mail to the supplier.
