### Header row

#### Supplier
In this field you enter the supplier number. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature you can search the supplier register. You can register a new supplier by entering a supplier number that does not already exist.
If the supplier you enter is blocked, the supplier number will be displayed in red bold text, regardless of what action the block concerns. You will also see a red padlock ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png) after the field. If a message/notification has been entered for the supplier, you will see a speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png) after the field.

#### Name
In this field you can see the name of the selected supplier, and it is possible to modify it. If you modify the name, a question will appear asking if the new name should be copied to all the supplier’s addresses. You will also choose if the new name should be copied to the Supplier name when searching.

#### Supplier role
In this field you can select one or several roles for the supplier. These terms can then be used in several places in the system, e.g., when selecting suppliers in lists and when exporting registers to CrossState in order for the matching of supplier invoices to work. This field cannot be left empty. The following options are available:
- Material supplier – Check this role for suppliers from which you buy material. This alternative is selected by default.
- Subcontract – Check this role to label your subcontract suppliers.
- Shipping agent – Check this role to indicate that the supplier in question offers shipping services. If you check this alternative, additional fields will become available to the right.
- Miscellaneous – Check this role for suppliers that do not match any of the other alternatives.

#### Export plugin
(Shipping agent) Here you select which shipping service should be used when exporting shipments to the shipping agent. The supported services in Monitor ERP are Pacsoft Online, nShift Delivery, and nShift Web-TA. You select the alternative Other if you will not use any of these services for shipments with the shipping agent, for example if you manually export and manage the shipments via another program. When you use Export to file or Export to file, SFTP the file format will be JSON. The purpose of Export to file, Export to file, FTP, and Export to file, SFTP is to enable third party integrations to a TA system (Transport Administration system).

#### Shipping agent type
(Shipping agent) The shipping agent type determines how tracking links (URL) for goods tracking should be created. The shipping agent's tracking link is used for the alternatives DHL, Schenker, PostNord, and DSV. nShift Delivery/Web TA's tracking link is used for the alternative Other. This alternative requires that you use nShift Delivery Plus or Web-TA Track & Trace and that tracking has been activated on the account at nShift.
Goods tracking can then be performed in the following procedures: Shipment list, Customer order info, and Customer register.

#### Shipping agent code
(Shipping agent) Here you enter a code that is used to identify the shipping agent in the selected shipping service.

#### EDI connected
In this field you see a Yes if the supplier in question is connected to EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system., otherwise the word No is shown. When the supplier is connected to EDI, it is possible to use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to see which transaction types and directions that apply for the supplier in question.

#### Internal (stock order)
This setting is available if you have installed the option Warehouse. The setting determines if the supplier is an internal supplier used on stock orders for purchase, where the sending warehouse is the supplier. All settings that are not relevant for a warehouse will be deactivated on an internal supplier, for example payment terms, currency*, payment method, and VAT group.
The internal supplier can be linked to its warehouse in the Company information procedure. In the Register stock order – Purchase procedure you create stock orders for the warehouse that perform the purchase (arrival reports).
> * The currency on an internal supplier must be the same as the company currency.
> Bear in mind: If you uncheck the internal supplier checkbox, it will not be possible to arrival report registered stock orders. If you want to register an invoice to an internal supplier, it is better to register a new supplier and register the invoice for the new (not internal) supplier. If there are already registered orders for a supplier, it is not possible to mark the supplier as internal supplier.
