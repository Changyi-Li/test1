### Settings – Documents
Using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the toolbar, you can go to the Register invoice directly procedure. If the Customer order transfer option is installed, you can click the Go to procedure to go straight to the Handle transfers procedure to quickly be able to see if the delivery has been correctly transferred to the sales company.

#### Document
Here you see the documents available to print for the saved reporting of delivery. The standard documents included are: Delivery note, delivered, Transport label, sales, and Transport label – Package structure. The purpose is to pack the delivery note along with the shipment and label the pallets with the transport label. If you report delivery of a batch number or a serial number, then it is also possible to print Product description including certificate.
Product description incl. certificate can also show Measuring data – Manufacturing and Measuring data – Purchase if this has been selected in the Document settings.

#### Transport label
Here you select the type of transport label you want to print. The types (the formats) which can be selected among are A4, A5, or Label (76 x 51 mm). According to part is selected by default. By using this setting you can change transport label for all rows in the Result box. If the part does not have a default transport label (in the Part register, under the Sales tab), Transport label – A4 will be selected.

#### Document variant according to
If printing a delivery note, Customer will be selected by default in this setting.
You can also choose to print the document variant according to Order type or the default document variant according to Document templates.
If Customer is selected and the customer lacks a document variant, the document variant will be selected based on Order type or, if that too lacks one, the default document variant according to Document templates.
If the transport label will be printed, According to part is selected by default.
You can also choose to print the document variant according to Customer, Order type, or the default document variant according to Document templates.
If Customer is selected and the customer lacks a document variant, the document variant will be selected based on Order type or, if that too lacks one, the default document variant according to Document templates.

#### Automatic printout of transport labels.
Determines if the transport label will be automatically printed if the delivery note is printed. The system setting Automatic printout of transport labels in Report delivery procedure determines if this setting will be checked by default.

#### Use traceability document from customer link
This setting can be activated for the list type called Product description including certificate. You can activate this setting if the product description incl. certificate selected in the Certificate field in the customer links for parts, should be printed. In that case, the setting will override the document variant selected in the field above.

#### Linked files
This setting is available for the list types called Delivery note, delivered. With this setting you decide if linked files should also be printed in connection with printing of the document. The linked files which can be printed are the ones activated for Automatic printout in the file link. [Read more about linked files and where they can be printed automatically](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm).

#### Show included parts
With this setting you decide if included/incorporated parts should be shown on the printout. With the document setting called Show included parts in fictitious you decide if this setting should be marked by default.

#### Show info about origin
To make it easier to understand the content of the PDF file with "Product description incl. certificate", you can choose to mark the pages with a watermark text with information about its origin. The text shown is:
Used in serial no./batch: XXX
Main part "Main part" is the term used for the part in the top node (highest level) in a structure of parts. number: YYY
Part number: ZZZ

#### Printout date
The date that is shown on the document as the date of the printout. Today's date is shown by default. By using the available calendar, you can select another date.
Printout date is only printed on Delivery note, delivered.

#### Document variant
If you want to print another document variant than the default variant, you can select it here. The document variants are handled in the Document templates procedure.
In that procedure, you can for the selectable documents in the Document field above, add variants to use for this printout.
To be able to choose a document variant you must deactivate the setting below.

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

#### Default customer linked document variants
In the Customer register procedure you can for each customer configure default customer linked document variants. This is done in the box [XML/Documents](../../Customers/CustomerRegister/bXMLDocuments.htm) (the button Customer-specific documents). If you uncheck this setting or if the customer on the row does not have a default document variant, then it is the document variant above that will apply.

#### Include empty packages
For the document type Transport label – Package structure you can select whether empty packages will be included on the printout. This setting is not activated by default. If you mark the checkbox it means the empty packages will be included on the printout.

#### "Select all" will only include packages with package numbers
Only packages that have a package number will be included if you activate this checkbox.
