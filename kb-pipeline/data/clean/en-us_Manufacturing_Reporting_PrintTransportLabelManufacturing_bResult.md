### Result
In this box you can see the reporting records that have been selected and loaded.

#### Include
The rows that are checked in this column will be printed.

#### Order number and Part number
In these columns you will see the manufacturing order number and the part number that will be printed on the transport labels.

#### Reported/Shipped/Rejected quantity
In this column you will see the reported quantity for the list types Transfer to stock and In progress. The reported quantity can be edited, if needed. For the list type Shipped subcontract you will see the quantity that has been shipped and for the list type Rejected you see the quantity that has been rejected.

#### Quantity/package
Here you see the quantity per package that should be printed on the label. This value is loaded from the part, but it can be edited. It affects the number of copies to be printed. If the arrival reported quantity is 20 and you enter 10 as Quantity/package, it means two transport labels will be printed. The package number will be updated and shows that the package is divided.
For the document Transport label, manufacturing, transfer to stock the following applies; if the part has serial number as traceability, then one transport label per serial number will always be created regardless of what you have written in the field Quantity/package.
For the documents Transport label, manufacturing, transfer to stock and Transport label, purchase the following apply; if the part has serial number as traceability, then the serial number will be shown if you enter 1 in the field Quantity/package. But if you write any other value, the batch number will be shown instead.
You can configure the field for batch number/serial number on the documents to always show the batch number regardless of the value in the field Quantity/package. This can be configured by clicking the button Edit ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_xtrareport_designer.png) on a variant of the above mentioned documents in the procedure Document templates.

#### Number of copies
Here you select the number of copies that should be printed. The default value here is 1. If you want a different default quantity, this is configured in the Document settings procedure.
