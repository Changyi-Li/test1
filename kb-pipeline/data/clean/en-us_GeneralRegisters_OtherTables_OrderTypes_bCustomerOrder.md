### Customer order
Under this tab you register order types for customer orders.

#### Order type
When you install the system, an order type called New sales and one called Agreement are included. If you have installed the option Warehouse you also find the order type Stock order. These order types cannot be deleted or inactivated, nor can you change the basic type.
* The Agreement order type is only used for the customer orders which are automatically created in connection with the release of an agreement basis in the Register customer agreement or Release customer agreement basis procedures. These customer order are separated from "regular" customer orders via the Agreement basic type. However, you cannot register new order types here for customer orders based on the Agreement basic type, and you cannot register customer order with the Agreement order type directly in the Register customer order procedure either. On the other hand you can register order types for agreements under the [Customer agreement](tCustomerAgreement.htm) tab and then use these for agreements you register in the Register customer agreement procedure.

#### Prefix
A prefix with up to 3 characters can be entered and the system will then automatically add the prefix at the start of the number loaded from the number series. For example when registering customer orders and the next number in the number series is 1001 and the prefix is S on the order type, the customer order number is set to S1001.

#### Name
The name of the order type. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Number series
Via the Number series button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see the next number in the number series for the order type in question. This is only shown if you have entered a separate number series for the order type in the Number series procedure.

#### Code
Here you enter the code for the order type using a maximum of 15 characters. Order type code is used for the option called Customer order transfer. This enables you to set the desired order type on new customer orders created in the production company when transferring customer orders from the sales company. The same code must be entered for the order type in both the sales company and in the production company. It must also be entered in the Order type code field in the setup number in the Settings for customer order transfer procedure in the sales company.

#### Basic type
The basic type indicates the function of the order type. The basic types called New sales and Stock order (option) are available when creating a new order type. Customer orders of the basic type Stock order do not create any invoice bases.

#### Price strategy
The price strategy determines how the price should be entered for the order type. The basic type "New sales" has by default the price strategy According to customer. This means that the price is primarily determined by the price linked to the customer and the price list in the customer register. The basic type Stock order has by default the price strategy Standard price. This means that the part's standard price will be used. When using the selection Price list, you select a specific price list that should apply to the order type.

#### Order type discount
Here you can add a discount in percent straight to the order type. When you create an order with this order type, this discount will be added to the order rows as Order type discount (code 5).

#### Rate type strategy
With this setting you decide which rate type should be used for the order type. According to customer is selected by default. This means the rate type entered for the customer will be used primarily. When choosing the According to order type alternative, you get to select a specific rate type. The different rate types in the system are the ones registered in the Currencies procedure, under the Rate types tab.

#### Posting group
Posting group for the order type (does not apply to the basic type Stock order). The available posting groups are of the type Sales in the Posting matrix procedure.

#### Document structure
By using the button Document structure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can define which documents should be printed by default together with customer orders with this order type. The documents can, for example, be front pages, and agreements. The documents that you select here will be automatically added to the Document structure tab in the Register agreement procedure. This applies to new order of this order type.
You can add or insert documents in the order you please, to the main document. Click on Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) to add the actual main document (quote, order). This document is displayed as a gray row (see the below image).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/DocumentStructure.png)
> If you do not use document structures, the main document will be printed even if you have not added the main document here (the gray row marked in the above image).
External document files can, for example, be PDF files that you select from a path, using the Browse button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_browse.png), and give a name in the table. Please note! It should preferably be a UNC path and not a path to a shared unit or a local unit. The reason for this is for the path to be accessible for other users if they should be able to print the documents. A UNC path is written as follows: \\ComputerName\SharedFolder, for example, \\file_server\documents.
One example of document structure is that you first have a front page, then a page with agreement text, then the actual main document, a finally an end/final page.
A document structure can be default. This is primarily decided by the order type and the language of the recipient's mailing address, but you can change the specific document files which should be included in this particular document structure together with the main document. You define default document structures per order type in the Order types procedure.
You add or insert an optional number of document files in the table, and place them in the order you want them. Changes you make will be saved for the record in question in the procedure.
> Please note! To add an external document file ahead of the main document, you must mark the Document row (putting it in focus) and then click the button called Insert new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) (Shift + F5) on the function menu.
The result is a compound document containing all document files including the main document in the order they were placed in the document structure. If you send this as an e-mail to the recipient, a single PDF file will be created of all the document files including the main document, and it will be attached in the e-mail. If you print the document structure, all the documents will be printed in the same order as in the table.

#### Variants
By clicking the Variants button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you access settings where you can configure a default document variant for order confirmation, invoice, comprehensive invoice, comprehensive delivery note, transport label, and delivery note, delivered.

#### Purchase order's address
Determines if the purchase order, created from the customer order with this order type, should have the company's delivery address (our supplier will then send the goods to us) or the customer order's delivery address (our supplier will then send the goods directly to our customer).

#### Apply preliminary pick list
With this setting you decide if Preliminary pick list should be applied for the order type. If both the order type and customer have configured Apply preliminary pick list, the customer order will also apply delivery planning by default. Preliminary pick lists are useful if you also want to create pick lists for parts with shortages (not ready for delivery). You can also use preliminary pick lists when the picking will take long time or be made in several steps. When printing a preliminary pick list, the status on the customer order is set to 4 (Picking in progress). However, no check is made to make sure the balance is sufficient and the customer order rows will not cleared.

#### Exclude from EDI
This setting is available if the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. option with formats for customer order is installed in your system. With this setting you decide if customer orders with this order type by default should be excluded from EDI. This way you can handle orders outside the EDI flow in parallel with EDI orders, to customers connected to EDI. You should register an additional order type for the New sales basic type when you have this setting activated. That is, register it in addition to the regular order type for "New sales" for which this setting is not activated.

#### Apply delivery planning
Here you determine if customer orders of this type should apply delivery planning. If both the order type and customer have configured Apply delivery planning, the customer order will also apply delivery planning by default.
Delivery planning is made in the Delivery planning procedure and results in suggestions of orders ready for delivery.

#### Invoice type
This does note apply to the Stock order basic type. Here you decide which type of invoice should be set for the order type. The following options are available:
- According to customer's pmt terms (default) – the payment term on the order/invoice determines which invoice type will be set on the order/invoice.
- Cash receipt – will be set on the order when selecting order type. For cash receipt you must also select a payment method.
- Internal – will be set on the order when selecting order type. For internal invoice you must also select a payment method.
Read more about cash receipt and internal invoice under [Invoice type](../Terms/bTermsPayment.htm#Fakturatyp).

#### Payment terms
If the invoice type is set to cash receipt, you must select a payment term.

#### Linked to purchase order type
This applies to the basic type Stock order. Here you determine the link of this order type to a corresponding order type for purchase with the basic type Stock order. This order type must first be created under the Purchase order tab. However, this does not apply if you have selected an order type that is delivered with the system. This means that when you register a stock order for sales with this order type, a corresponding stock order for purchase will be automatically registered. A link is then created between these stock orders. You can say that the stock order for sales "owns" the stock order for purchase.

#### Automatic arrival reporting
This applies to the basic type Stock order. Here you determine if automatic arrival reporting should be made of stock orders for purchase with this order type. This means that after a stock order for sales has been delivery reported in the Report delivery procedure, theReport arrival procedure will open automatically with the linked stock order for purchase already loaded. You can then report the corresponding arrival.

#### Create invoice basis
Applies to the New sales basic type. Here you determine if invoice bases should be created from customer orders with this order type during delivery of orders. This settings is activated by default. Then invoice bases will be created during delivery reporting and the bases receive status 1 (For invoicing). You can deactivate the setting if you do not want to create invoice basis for certain deliveries. For example if you send goods samples. Then the status of the invoice basis is set to 0 (Canceled) during delivery reporting. The order types where Create invoice basis is not marked cannot be selected in the Register invoices directly procedure.

#### Create sales statistics
Here you determine if sales statistics should be created for orders with this order type. This can only be selected if Create invoice basis is checked as sales statistics are based on invoicing.

#### Priority
The priority is used to prioritize quotes, inquiries, orders, or projects. The default value here is 9. You can enter a digit between 1 and 9, where 1 is the highest priority. This field cannot be left empty.
This priority of the order type is always combined with the priority of the customer, when the priority of the customer order is set. The highest priority of the order type and customer will become the order's priority.

#### Activity template
The activity template you select here will by default become linked to new orders you create using this order type. Activity templates are predefined sets of activities for the order. They are managed under the Activity templates tab in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – CRM procedure. The activity template of the order is possible to change at a later time.

#### Preliminary
Here you determine if new customer orders with this order type should be preliminary. That is, if the setting Preliminary should be activated for the order.

#### Intrastat
For each order type you can configure different settings regarding transaction types and which value should be reported in the Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. report. Which fields can be entered and which options are available in each respective field depend on which basic type the order type has.

#### Document settings
Under the Document settings button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can for this order type decide from where the information in the page header and footer on the delivery documents Delivery note, delivered, Comprehensive delivery note, and Transport label, sales should be loaded. The following options are available:
- From company info – (default) If you select this alternative, the information will be loaded from the Company information procedure.
-     
From customer info – If you select this alternative, the information will be loaded from the Customer register procedure. In that case, the following applies:
The customer’s logo is shown in the header of the documents. In the footer of the documents you see the customer's Mailing address and Visiting address, Website, E-mail address (first row without "Recipient of" from the Communication box), Phone, Fax, Corporate ID number, VAT registration number, BIC, IBAN, and Bank name.
"From customer info" can be used in cases where you ship the deliveries directly to the end customer (the customer's customer). The purpose of this is to make it look like your deliveries have been shipped from your customer, and not from you.

#### Active
Here you determine if the order type is active. A deactivated order type will no longer be available for the users in the system.

#### Log
By using the Log button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you find a changelog for the order type. Here you see who modified the information as well as when. You also see what has been changed, with the value before and after the change.
