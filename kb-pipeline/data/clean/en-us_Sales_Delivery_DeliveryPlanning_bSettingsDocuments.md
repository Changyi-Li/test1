### Settings – Documents

#### Document
Here you select the document that will be printed. In the settings below you can choose which document variant to print if there are multiple variants available of the document. The document you select is shown in the Preview box.
Depending on which list type you have selected, you can choose to print: Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. – By order, Pick list – Ready for delivery, Packing list A packing list describes in which packages and using which types of packaging, the parts/products have been packed for delivery. The packaging list often contains information about package number and gross as well as net weight., Transport label – Package structure, and Transport label, sales. For the Pick list – Ready for delivery there is a document variant called Pick list (packaging) which can be selected in the Document templates.
For Transport label – Package structure, the following two fields called Transport label and Use the part's default transport label are deactivated since this transport label is of a different format displaying package structures.
Depending on the selected list type you can go to the Pack for delivery and Report delivery procedures.

#### Transport label
Here you select the type of transport label you want to print. The types (the formats) which can be selected among are A4, A5, or Label (76 x 51 mm). This setting will also be used as a fallback value if no transport label is selected for the part in the part register. The default option is Transport label – A4.

#### Use the part's default transport label
With this setting you decide if the part's default transport label should be used for printout. If you uncheck the checkbox, the previous setting will be used as the transport label for all parts, regardless of the settings registered for each individual part in the Part register procedure.

#### Document variant
If you want to print another document variant than the default variant, you can select it here. The document variants are handled in the Document templates procedure.
In that procedure, you can for the selectable documents in the Document field above, add variants to use for this printout.
To be able to choose a document variant you should deactivate the setting further down.

#### Pick list printout order
With this setting you can decide in which order the pick lists should be printed. There are two options:
- Pick list number (default)
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

#### Show all locations
Applies to the Picking plan list. With this setting you decide if all locations which have been registered for the part should be displayed in the pick list. When you use this setting for traceable parts, only the part’s disposable stock balance will be shown for the locations that you are not supposed to pick from.
> Rows with the delivery status called Shortage are marked with an asterisk (*) in the Pick list (standard) document variant.

#### Show packaging summary
Determines if a packaging summary (showing what the package consists of) should be shown at the bottom of the pick list.

#### Show grouping header
Determines if an additional sub-heading showing how the pick list has been sorted should be shown in the document. For example, if you have selected “part number” in the Sort pick list by setting, the sub-heading will show Part number.

#### Printed by
This setting determines which user name should be shown next to the heading Printed by on the document. The logged in user is selected by default. If you do not actively choose a different employee, the logged-in user will be used.

#### Default customer linked document variants
In the Customer register procedure you can for each customer configure default customer linked document variants. This is done in the box [XML/Documents](../../Customers/CustomerRegister/bXMLDocuments.htm) (the button Customer-specific documents). If you uncheck this setting or if the customer on the row does not have a default document variant, then it is the document variant above that will apply.

#### Linked files
This checkbox determines if linked files should also be printed when printing the document. The linked files which can be printed are the ones activated for Automatic printout in the file link. [Read more about linked files and where they can be printed automatically](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles).
