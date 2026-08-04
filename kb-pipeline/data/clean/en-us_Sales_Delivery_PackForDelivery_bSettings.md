### Settings

#### Document
Here you select the document that will be printed. In the settings below you can choose which document variant to print if there are multiple variants available of the document. The document you select is shown in the Preview box.
You can choose to print: Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. – By order, Pick list – Ready for delivery, Packing list A packing list describes in which packages and using which types of packaging, the parts/products have been packed for delivery. The packaging list often contains information about package number and gross as well as net weight., Transport label – Package structure, and Transport label, sales.
For Transport label – Package structure, the following two fields called Transport label and Use the part's default transport label are deactivated since this transport label is of a different format displaying package structures.

#### Transport label
Here you select the type of transport label you want to print. The types (the formats) which can be selected among are A4, A5, or Label (76 x 51 mm). This setting will also be used as a fallback value if no transport label is selected for the part in the part register. The default option is Transport label – A4.

#### Use the part's default transport label
With this setting you decide if the part's default transport label should be used for printout. If you uncheck the checkbox, the previous setting will be used as the transport label for all parts, regardless of the settings registered for each individual part in the Part register procedure.

#### Document variant
If you want to print another document variant than the default variant, you can select it here. The document variants are handled in the Document templates procedure.
In that procedure, you can for the selectable documents in the Document field above, add variants to use for this printout.
To be able to choose a document variant you must deactivate the setting below.

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

#### Sort trans. labels by
Determines what Transport label – Package structure will be sorted by. The following options are available:
- Package structure – The transport labels are sorted as per the package structure, meaning: the first handling unit, followed by its underlying level, followed by the next handling unit, followed by its underlying level, and so on.
- Order number – The transport labels are sorted by the customer order numbers in Monitor. This means that if a pick list contains multiple orders, the packages will be sorted so that the packages containing the lowest order number will be shown first in the list. If a package contains more than one order number, it will be sorted according to the lowest of these order numbers. An outer packaging that contains no payload in itself, but contains boxes with payload, will be sorted by the lowest order number from the boxes contained within the outer packaging.
- Part number – The transport labels are sorted by the payload’s part number. This means that if a pick list contains multiple parts, the packages will be sorted so that the packages containing the lowest payload part number will be shown first in the list. If a package contains more than one payload part number, it will be sorted according to the lowest of these part numbers. An outer packaging that contains no payload part in itself, but contains boxes with payload parts, will be sorted by the lowest payload part number from the boxes contained within the outer packaging.
- Order row position – The transport labels are sorted by the position number of the order row. This means that if a pick list contains multiple order row positions, the packages will be sorted so that the packages containing the lowest order row position will be shown first in the list. If a package contains more than one order row position, it will be sorted according to the lowest of these included position numbers. An outer packaging that contains no payload part in itself, but contains packages with payload parts, will be sorted by the lowest order position number from the boxes contained within the outer packaging.
- Handling units first – The transport labels will be printed “from top to bottom”, meaning all selected outer packagings first (sorted by ascending package numbers), followed by all selected packages on the underlying level (sorted by ascending package numbers), followed by all selected packages on the next underlying level, and so on.
- Handling units last – The transport labels will be printed “from bottom to top”, meaning all selected inner packagings first (sorted by ascending package numbers), followed by all selected packages on the higher level (sorted by ascending package numbers), followed by all selected packages on the next higher level, and so on.
- Package number – The transport labels are sorted by ascending package numbers.
In all the above cases, if there are multiple copies of a label, these copies will be printed in succession. If you, for example, have 5 copies of the transport label for a package, these 5 copies will be printed in immediate succession before printing the transport label for the next package number in the sequence.

#### Show all locations
Applies to the Picking plan list. With this setting you decide if all locations which have been registered for the part should be displayed in the pick list. When you use this setting for traceable parts, only the part’s disposable stock balance will be shown for the locations that you are not supposed to pick from.

#### Show packaging summary
Determines if a packaging summary (showing what the package consists of) should be shown at the bottom of the pick list.

#### Show grouping header
Determines if an additional sub-heading showing how the pick list has been sorted should be shown in the document. For example, if you have selected “part number” in the Sort pick list by setting, the sub-heading will show Part number.

#### Default customer linked document variants
In the Customer register procedure you can for each customer configure default customer linked document variants. This is done in the box [XML/Documents](../../Customers/CustomerRegister/bXMLDocuments.htm) (the button Customer-specific documents). If you uncheck this setting or if the customer on the row does not have a default document variant, then it is the document variant above that will apply.

#### Printed by (employee)
The employee who printed the document.

#### Linked files
This checkbox determines if linked files should also be printed when printing the document. The linked files which can be printed are the ones activated for Automatic printout in the file link. [Read more about linked files and where they can be printed automatically](../../Topics/UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles).

#### Include empty packages
For the document type Transport label – Package structure you can select whether empty packages will be included on the printout. This setting is not activated by default. If you mark the checkbox it means the empty packages will be included on the printout.
