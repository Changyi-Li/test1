### Settings – Documents (Transport label – Package structure)
These settings apply to the list type called Transport label – Package structure.

#### Transport label
Here you select the type of transport label you want to print. The types (the formats) which can be selected among are A4, A5, or Label (76 x 51 mm). This setting will also be used as a fallback value if no transport label is selected for the part in the part register. The default option is Transport label – A4.

#### Use the part's default transport label
With this setting you decide if the part's default transport label should be used for printout. If you uncheck the checkbox, the previous setting will be used as the transport label for all parts, regardless of the settings registered for each individual part in the Part register procedure.

#### Document variant
If you want to print another document variant than the default variant, you can select it here. The document variants are handled in the Document templates procedure.
In that procedure, you can for the selectable documents in the Document field above, add variants to use for this printout.
To be able to choose a document variant you should deactivate the setting further down.

#### Pick list printout order
With this setting you can decide in which order the transport labels should be printed. There are two options:
- Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. number (default)
- Customer number

#### Sort pick list by
Determines what the pick list will be sorted by. The following options are available:
- Main location Earlier called "Current location". Main location means the stock location for a part that has the most recent arrival date for the part. If you apply priority for the locations, then the main location is the location which has the highest priority (that is, the lowest number).
- Location's route sorting number
- Location
- Part number
- Customer order
- Customer's order row position
- Delivery date
- Position

#### Sort transport labels by
With this setting you decide what should be used to sort the transport label – package structure. The following options are available:
- Package structure – The transport labels are sorted according to the package structure, which means: first handling unit, followed by its underlying level, followed by the next handling unit, followed by its underlying level, and so on.
- Order number – The transport labels are sorted by customer order number in Monitor ERP. This means that if a pick list contains multiple orders, the packages will be sorted so that the package with the lowest order number will be shown at the top of the list. If a package contains more than one order number, it will be sorted according to the lowest of these order numbers. An outer packaging that contains no payload in itself, but contains inner packaging with payload, will be sorted by the lowest order number from the inner packaging contained within the outer packaging.
- Part number – The transport labels are sorted by the part number of the payload. This means that if a pick list contains multiple parts, the packages will be sorted so that the package with the lowest part number will be shown at the top of the list. If a package contains more than one part number, it will be sorted according to the lowest of these part numbers. An outer packaging that contains no payload in itself, but contains inner packages with payload, will be sorted by the lowest part number from the inner packaging contained within the outer packaging.
- Order row position – The transport labels will be sorted by the position number of the order row. This means that if a pick list contains multiple order row positions, the packages will be sorted so that the package with the lowest order row position will be shown at the top of the list. If a package contains more than one order row position, it will be sorted according to the lowest of these position numbers. An outer packaging that contains no payload in itself, but contains packages with payload, will be sorted by the lowest order position number from the inner packaging contained within the outer packaging.
- Handling units first – The transport labels will be printed “from top to bottom”. This means all selected outer packagings first (sorted by ascending package numbers), followed by all selected packages on the underlying level (sorted by ascending package numbers), followed by all selected packages on the next underlying level, and so on.
- Handling units last – The transport labels will be labels printed “from bottom to top”, meaning all selected inner packagings first (sorted by ascending package numbers), followed by all selected packages on the higher level (sorted by ascending package numbers), followed by all selected packages on the next higher level, and so on.
- Package number – The transport labels are sorted by ascending package numbers.
In all the above cases, if there are multiple copies of a label, these copies will be printed in succession. If you, for example, have 5 copies of the transport label for a package, these 5 copies will be printed directly after each other before printing the transport label for the next package number in the sequence.

#### Show all locations
With this setting you decide if all locations which have been registered for the part should be displayed in the pick list. When you use this setting for traceable parts, only the part’s disposable stock balance will be shown for the locations that you are not supposed to pick from.
> Rows with the delivery status called Shortage are marked with an asterisk (*) in the Pick list (standard) document variant.

#### Show packaging summary
Determines if a packaging summary (showing what the package consists of) should be shown at the bottom of the pick list.

#### Show grouping header
Determines if an additional sub-heading showing how the pick list has been sorted should be shown in the document. For example, if you have selected “part number” in the Sort pick list by setting, the sub-heading will show Part number.

#### Printed by (employee)
This setting determines which user name should be shown next to the heading Printed by on the document. The logged in user is selected by default. If you do not actively choose a different employee, the logged-in user will be used.

#### Default customer linked document variants
In the Customer register procedure you can for each customer configure default customer linked document variants. This is done in the box [XML/Documents](../../Customers/CustomerRegister/bXMLDocuments.htm) (the button Customer-specific documents). If you uncheck this setting or if the customer on the row does not have a default document variant, then it is the document variant above that will apply.

#### Linked files
This checkbox determines if linked files should also be printed when printing the document. The linked files which can be printed are the ones activated for Automatic printout in the file link. [Read more about linked files and where they can be printed automatically](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles).

#### Include empty packages
For the document type called Transport label – Package structure, you can select whether or not empty packages should be included in the printout. If you mark the checkbox, empty packages will be included on the printout.
