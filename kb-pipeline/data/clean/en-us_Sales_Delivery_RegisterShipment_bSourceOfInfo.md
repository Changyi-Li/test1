### Source of information
In the Source of information box you decide from where the shipment should load its information, for example, from a customer order. Addresses, terms, etc. are loaded from this source. You can include orders and pick lists for different customers in one and the same shipment, but you will receive a warning stating that customer, delivery method, etc., differs.

#### Type
The source of information type can be: Customer order/Delivery, Supplier, Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order., Customer, Pick list with package structure, Return order (Purchase), or Subcontract order (Purchase).

#### Source of information
Here you select and load the source of information to create a shipment for or to advice.
If the source of information type is Customer or Supplier, you will see its name in the Name column.
If the source of information type is Customer order/Delivery, Pick list or Subcontract order (Purchase), you will also see its Status.
If the source of information type is Customer order/Delivery and it has been partially delivered, you also get to enter a Partial delivery number in order to indicate the partial delivery in question.
If the source is of the type Subcontract order (Purchase), you will also see its Operation number from the manufacturing order.
You can add multiple rows with source of information, but only sources of the same type if you want them to be included in the same shipment.
If the source of information type is Pick list with package structure, a Yes will be displayed in the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. export column if the advice for the pick list can be exported via EDI. Otherwise you will here see No.
The column called B/N is included the table for all types of information sources and lets you know if there is a block or a notification regarding the source of information.
> * If is should be possible to EDI export a dispatch advice for a pick list with package structure, the customer on the pick list must be configured for EDI (that is, be included in an EDI behavior in the EDI behaviors procedure). Also, the pick list must not be excluded from EDI (which is configured by clicking the EDI button in the Pack for delivery procedure). It is also possible to add more rows with pick lists if you want dispatch advice for these to be included in the same EDI export. For this to be possible, there must be a Yes in the EDI export column on all of the rows.
