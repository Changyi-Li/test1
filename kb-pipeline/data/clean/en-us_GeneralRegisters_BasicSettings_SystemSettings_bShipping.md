### Shipping

#### Load to our reference on shipment
This system setting determines which information should be printed as the our reference on shipping documents. The following options are available:
- Employee no. in Users – Contact details are loaded from the employee number linked to the user that creates the shipment. The employee’s forename and surname are written as Our reference and E-mail, Phone, and Mobile phone are loaded to the shipment.
- Description in Users – Contact details are loaded from the user that registers the shipment. The user’s Description is used as Our reference and the e-mail address entered for the user is loaded to the shipment.
- Our reference on customer order – Contact details are loaded from the reference that is selected as our reference on the customer order that is used as the information source. If the source of the information is not a customer order, the fields are left empty.
- None – The sender’s contact details are not loaded to the shipment.

#### Load to the sender's reference on shipment
This system setting determines which information should be printed as the sender’s reference on shipping documents. If multiple sources have the same value, each unique value will only be added once. The following options are available:
- Nothing
- Customer order number
- Customer's order number
- Goods labeling
- Delivery note number

#### Load to the recipient's reference on shipment
This system setting determines which information should be printed as the recipient's reference on shipping documents. You can also choose to not print any reference.

#### Update shipping information on quote/customer order/invoice
This system setting determines if shipping information should be updated on quote/customer order/invoice. The update can be made automatically or via a dialog box.

#### Load to pick-up address on shipment
Here you decide from where the pick-up address should be loaded. The following options are available:
- Address from source of information's warehouse (default)
- Address from the logged in user's warehouse

#### Use default consolidation key for shipment
With this setting you decide if consolidated shipments should be applied and in that case, which consolidation key to use. Consolidation key is an identifier uses when new consolidated shipments are created or when packages are added to open consolidated shipments. Consolidated shipments get the same Shipping agent's shipment no. when they have been exported in the Register shipment procedure. The following options are available:
- No – No default consolidation key is applied.
- Yes, use customer number – The default consolidation key is the customer number.
- Yes, use today's date – The default consolidation key is today's date.
- Yes, use delivery address (row 1) – The default consolidation key is the first address row in the delivery address.
- Yes, use delivery address (zip code) – The default consolidation key is the zip cope in the delivery address.
- Yes, use delivery address (row 1 and zip code) – The default consolidation key is the first address row and the zip code in the delivery address. The consolidation key is then changed into "address_zipcode".
> To be able to apply consolidated shipments in Monitor ERP, your shipping agent (freight company) must have support for it. Your subscription with the selected shipping service (nShift or LogTrade) must also have support for consolidated shipments.

#### Primary source of information for pick list
With this system setting you decide from where different information about the customer (reference, etc.) should be loaded by default to shipments. This applies to shipments where Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. or Pick list with package structure is used as source of information. The available options are:
- Customer – The information is always loaded from the Customer register.
- First customer order – The information is always loaded from the first customer order of the pick list. When this option has been selected you can also apply Shipping exceptions for a customer order in the Register customer order procedure.

#### Handling principle for package rows in shipment
With this system setting you decide if package rows in a shipment should be merged or split by default. The available options are:
- Leave as is – The package rows will not be merged or split by default.
- Merge packages – The package rows will be merged every time a new row for source of information is added.
- Split packages – The package rows will be split every time a new row for source of information is added.

#### Use 1 as default number of packages in Shipping info
With this setting you can decide it all parts should be added in one single package in the Shipping info, as long as the parts belong to the same Goods type Goods type describes what kind of part it is, for example machine parts, electronics, etc. Goods type is printed on shipping documents., Package type Package type describes what kind of package that is used, such as "pallet" for EU pallets, "box" for cardboard boxes etc., and Packaging part. This applies in the following procedures: Register quote, Register customer order, Report delivery, and Register invoice directly.
