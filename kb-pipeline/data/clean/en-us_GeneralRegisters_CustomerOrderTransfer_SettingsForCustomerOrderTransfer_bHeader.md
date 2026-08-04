### Header
Here you configure settings for customer order headers on customer orders that are created in the production company when the customer order is transferred from the sales company.

#### Customer number
Here you determine which customer number should be used on customer orders created in production companies. The following options are available:
- Sales company
- End customer

#### Order type code
Here you enter the code of the order type using a maximum of 15 characters. This order type will be used on the customer orders created in the production company by the customer order transfer. The same code must also be entered in the Code field on the order type in the Order types procedure, both in the sales company and in the production company.
Another production company can use the same order type code for their order type, provided that that company uses the same setup number (as selected on the header row in the procedure).

#### Delivery
Here you determine if deliveries should be sent to the sales company or to the end customer. You also select which delivery address should apply. The delivery address in the customer register determines a number of delivery settings such as delivery term, delivery method, goods receiver's reference, customer number, shipping agent, transport time, and delivery instructions. The following options are available:
- To sales company, acc. to delivery address in the production company's customer register
- To end customer, acc. to delivery address in the production company's customer register
- To end customer, to delivery address registered on the sales company's customer order
If you have configured to send deliveries to the sales company (option number 1), the sales company must manually arrival report the purchase order and manually delivery report the customer order since the goods will arrive to the sales company. This is important in order to achieve correct stock balance.
If you have configured that deliveries should be sent to the end customer (option 2 or 3), the sales company's purchase order will be arrival reported and the customer order will be delivery reported automatically when the production company's customer order is delivery reported. On the document called Delivery note, delivered, the part number for delivered parts will be loaded from the field called Transferring comp.'s "Customer's part no." on the customer order row instead of from the production company's part.
It is the customer number and VAT registration number of the end customer that are printed on the delivery note.

#### Delivery address
Here you determine which delivery address should be set on customer orders created in production companies. The default option is loaded from the setting Delivery, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Delivery terms
Here you determine which delivery term should be set on customer orders created in production companies. The default option is loaded from the setting Delivery, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.
If the delivery terms on the order in the production company is loaded from the sales company's customer order, the Place of terms of delivery will also be loaded from the sales company's customer order.
> Under the Delivery terms tab, in the Terms procedure, you can enter a Code which will be used to match one delivery term in the sales company with another delivery term in the production company. Matching takes place if the same code is used in both companies.

#### Delivery methods
Here you determine which delivery method should be set on customer orders created in production companies. The default option is loaded from the setting Delivery, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.
> Under the Delivery method tab, in the Terms procedure, you can enter a Code which will be used to match one delivery method in the sales company with another delivery method term in the production company. Matching takes place if the same code is used in both companies.

#### Goods label
Here you determine which goods label should be used on customer orders created in production companies. The available alternative is:
- From the Header tab on the sales company's customer order.

#### Goods receiver's reference
Here you determine which goods receiver reference should be used on customer orders created in production companies. The available alternative is:
- From the Header tab on the sales company's customer order.

#### Delivery rules
Here you determine which delivery rules should be set on customer orders created in production companies. The default option is loaded from the setting Delivery, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Transport time
Here you determine which transport time should be set on customer orders created in production companies. The default option is loaded from the setting Delivery, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Delivery instructions
Here you determine which delivery instruction time should be set on customer orders created in production companies. The default option is loaded from the setting Delivery, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Pick instruction
Here you decide from where you want to load the pick instruction for customer orders created in the production company. The following options are available:
- End customer – The pick instruction is loaded from the Customer register in the sales company.
- Sales company's customer order – The pick instruction is loaded from the sales company's customer order.
It is possible to mark both of the options which means that the production company's customer order can have the general pick instruction for the end customer as well as the order-specific pick instruction added to the customer order in the sales company.

#### Document path, pick instruction
Here you can enter where files transferred from the sales company's pick instruction should be saved with the production company. Since you configure the setting in the sales company but it applies for where the file should be saved with the production company, you have to enter the path manually.
> If no document path has been entered, the pick instruction will be transferred without files.

#### Prefix
Here you determine which prefix should be set in front of the customer order number on customer orders created in production companies. The following options are available:
- From the sales company's customer order type
- From the production company's customer order type.

#### Customer order number
Here you determine from where you want to load customer order number to customer orders created in the production company. The following options are available:
- From the sales company's customer order
- From the production company's order number series.
If you have configure to load customer order numbers from the sales company's customer order and that customer order consists of several customer order rows to different production companies, then the customer order number will be the same in all production companies.
If the suggested customer order number already exists in the production company, a suffix will be added to the customer order number. For example, the customer order number suffix will be 50515-1, 50515-2, and so on.

#### Customer's order number
Here you determine from where you want to load customer's order number to customer orders created in the production company. The following options are available:
- Sales company's customer order number
- Customer's order number on sales company's customer order
- Sales company's purchase order number.
If you choose multiple alternatives, these will be separated by a space.

#### Customer's reference
Here you determine which reference should be set on customer orders created in production companies. The following options are available:
- Customer in the production company
- Sales company's customer order.

#### Invoicing plan
Here you decide if the production company is allowed to delivery orders (straight to end customer) before the advance invoice in the sales company has been paid. The following options are available:
- No
- Yes, always
- Yes, warn/block delivery if unpaid advance invoice exists – If the Check for unpaid advance invoices at delivery setting in the Register customer order procedure in the sales company has been set to Warn or Block delivery, it means an invoicing plan will be applied to the customer order in the production company. This invoicing plan is loaded from the production company’s customer register (the setting called Invoicing plan COT) for the customer on the order.
Work method to handle invoicing plans
In order to make invoicing plans function smoothly when working with customer order transfer, we have a suggested way of working when the production company should retain the order (directly to end customer) until the advance invoice in the sales company has been paid.
1. The production company should have an invoicing plan with 100% advance on the advance invoice. This invoicing plan should also have the setting called Check for unpaid advance invoices set to Block delivery in the Invoicing/Payment plans procedure.
2. In the production company, this invoicing plan (100% advance) should be entered on the customer (in the setting called Invoicing plan COT) that the customer order is being registered for. For example, for the customer number which represents the sales company.
3. In the sales company, the Invoicing plan setting in the Settings for customer order transfer procedure should be set to Yes, warn/block delivery if unpaid unpaid advance invoice exists.
4. The sales company will thereby be able to transfer customer orders with invoicing plans where the advances must be paid before delivery is made.
5. The invoicing plan will be added to the customer order in the production company. The production company can start the manufacturing, but they cannot delivery the order until the advance has been paid.
6. The sales company receives the advance payment and notifies the production company of this.
7. The production company removes the Invoicing plan from the terms of the customer order and they can now deliver the order. Please note! It is important that the invoicing plan is only removed once the customer has paid the advance to the sales company. Otherwise, the purchase order and the customer order cannot be reported automatically when the production company delivers the order to the end customer.

#### Mailing address
Here you determine which mailing address should be set on customer orders created in production companies. The following options are available:
- Customer in the production company
- Sales company's customer order.

#### Seller
Here you determine which seller (from the personnel records) should be set on customer orders created in production companies. The following options are available:
- None
- Customer in the production company
- Sales company's customer order – This option is only useful if the sales company and the production company have synchronized their personnel information. That is, that both companies have matching sellers (based on the employee number).

#### Order date
Here you determine which order date should be set on customer orders created in production companies. The following options are available:
- Transfer date
- Sales company's customer order.

#### Communication
By clicking the Communication button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you decide from where communication information for different Recipient of should be loaded to customer order created in the production company. The following options are available and can be combined:
- From the sales company's customer order
- From customer in the production company.

#### Status
Here you determine which status should be set on customer orders created in production companies. The following options are available:
- Preliminary
- Registered (status 1)
- Printed (status 2).

#### Payment
Here you determine who should pay the production company's invoice. That is, which customer number should be set in the field Customer number, invoice on customer orders created in the production company. The selected alternative also determines a number of payments settings such as, payment term, invoice address, invoice is pending, invoicing charge, customer group, VAT code, currency. The following options are available:
- Sales company, acc. to payment settings in the production company's customer register
- End customer, acc. to payment settings in the production company's customer register
- End customer, acc. to payment settings on the sales company's customer order.

#### Payment terms
Here you determine which payment term should be set on customer orders created in production companies. The default option is loaded from the setting Payment, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.
> Under the Payment terms tab, in the Terms procedure, you can enter a Code which will be used to match one payment term in the sales company with another payment term in the production company. Matching takes place if the same code is used in both companies.

#### Invoice address
Here you determine which invoice address should be set on customer orders created in production companies. The default option is loaded from the setting Payment, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Invoice is pending
Here you determine if the setting Invoice is pending should be activated on customer orders created in production companies. The default option is loaded from the setting Payment, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Comprehensive invoice
Here you determine if the setting Comprehensive invoice should be activated on customer orders created in production companies. The default option is loaded from the setting Payment, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Invoicing charge
Here you determine if the setting Invoicing charge should be activated on customer orders created in production companies. The default option is loaded from the setting Payment, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Customer order category
Here you decide whether the customer order category from the sales company’s customer order should be copied over to the production company’s customer order. If set to Yes, the Customer order category on the sales company’s customer order will be copied to the production company’s customer order.
If the production company has another setting for the customer order category (another number of characters or obligatory fields) that do not match the category from the sales company, the Customer order category of the production company’s customer order will be empty.
If set to No, the Customer order category on the sales company’s customer order will NOT be copied to the production company’s customer order.

#### Customer group
Here you determine which customer group should be set on customer orders created in production companies. The default option is loaded from the setting Payment, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### VAT group
Here you determine which VAT group should be set on customer orders created in production companies. The default option is loaded from the setting Payment, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.

#### Project
Here you decide whether the project from the sales company’s customer order should be copied over to the production company’s customer order. If set to Yes, the Project on the sales company’s customer order will be copied to the production company’s customer order. This can only be done if the project exists in the production company. If the project does not exist in the production company, the Project field will be empty on the production company’s customer order.
If set to No, the Project on the sales company’s customer order will NOT be copied to the production company’s customer order.

#### Currency
Here you determine which currency should be set on customer orders created in production companies. The default option is loaded from the setting Payment, but this can be changed. The following options are available:
- Sales company's customer order in the production company
- End customer's customer number in the production company
- Sales company's customer order.
> When a price is converted into another currency, the exchange rate in the production company will be used.

#### Aftermarket – Serial number
With this setting you decide if the serial number entered on the sales company's customer order (Header tab, under Aftermarket) should be transferred to the production company.
The following options are available:
- No – Serial number A serial number is a number that is used for traceability for parts on entity level. will not be transferred to the production company.
- Yes, when existing in production company – serial number will only be transferred if the serial number is already registered in the production company’s serial number register.
- Yes, add to production company – If the serial number is not registered in the production company, the serial number on the customer order in the sales company will be transferred to the production company’s customer order and will also be registered in the production company’s serial number register.

#### Replace internal comment
This system setting determines whether the production company’s customer order’s internal comment will be replaced with the sales company’s customer order’s internal comment.
If this setting and the corresponding setting in the Sales company tab are both set to Yes, the internal comment will be used to send information between the companies.

#### Document path, internal comment
Here you can enter where files transferred from the sales company's customer order’s internal comment should be saved with the production company. Since you configure the setting in the sales company but it applies for where the file should be saved with the production company, you have to enter the path manually.

#### Replace external comment
This system setting determines whether the production company’s customer order’s external comment will be replaced with the sales company’s customer order’s external comment.

#### Document path, external comment
Here you can enter where files transferred from the sales company's customer order’s external comment should be saved with the production company. Since you configure the setting in the sales company but it applies for where the file should be saved with the production company, you have to enter the path manually.
