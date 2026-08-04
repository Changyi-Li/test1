### Result
Here you select for which delivered orders you want to print delivery note or transport label, depending of the document you selected in the settings. All rows that have orders are marked by default. If you selected the Via pick list list type, the rows will be grouped by pick list number.
In the Preview box you can see the document for the marked row before you print it.
You can also print the documents separately in the Print delivery documents procedure.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can go straight to procedures such as Register customer order, Review/Approve invoice and Review/Approve pro forma invoice.
By using the Create shipment button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_shipping.png) you can create a shipment for the orders or pick lists where Include is marked. A shipment draft with all of the information pre-filled is then created in the Register shipment procedure.
If the Customer order transfer option is used, you can click the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the toolbar to load orders here to the Handle transfers procedure. This applies to orders containing order rows that have a transfer profile.
Result for Transport label – Package structure
In this box you see the package structure. If the Transport label – Package structure document has been selected, there is a checkbox for each package which you should mark if you wish the document to be printed. For the Transport label – Package structure document, the checkbox for all packages are marked by default.
There is also a checkbox in the column heading. You can use this if you quickly want to check or uncheck all the checkboxes for all of the packages. This is useful if you are working with large package structures.
If you have sorted the transport labels by Package structure, the list will be shown as a tree structure/structure map.
If you have sorted the transport labels by Order number, Part number, Order row position, Handling units first, Handling units last, or Package number, no structure will be displayed in the list.
You print by using the button Print ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_print.png) on the toolbar of the procedure.

#### Include
Here you decide which documents should be printed or for which a shipment should be created.

#### Quantity/package
(Transport label, sales) Here you determine how large quantity it is per package and thereby how many transport labels will be printed. The suggested quantity/package is loaded from the reporting or from the part register, but it is possible to edit here. This is useful if the package size of the part might vary and the default value does not suit the delivery.

#### Transport label
Here you see which transport label is selected according to the Transport label setting above. This can be changed per row.

#### Document variant
Here you see which document variant is selected in the setting called Document variant according to above. This can be changed per row.

#### EDI export
(Delivery note, delivered) This column is shown if Export principle for dispatch advice has been set to Export at delivery reporting in the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. behavior to which the customer on the order is linked. Here you can then choose if the dispatch advice should be exported via EDI in connection with printing of the delivery note.

#### Files
(Delivery note, delivered) A button is shown here if there are any documents linked. In the window opened by the button, you can see all documents which will be included when printing.
