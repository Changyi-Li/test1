### Printers
Different default printers for the user.
You can select among the printers that are installed in Windows on the computer where Monitor ERP is being used.
You can also enter a printer name for a printer driver that is not installed in Windows on the local computer, e.g. in order to register a printer for a user who has another printer installed than the one on the local computer. In that case, you enter the printer name exactly as it is entered on the user's computer. You see a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) if the entered printer is not installed on the local computer.

#### Standard printer
Here you select the general standard printer that should be set as default for different printouts. However, this does not apply to printouts to the printer selected in the fields External 1–3 and printouts per document and printer in the table Documents/Printers below.

#### External 1–3
Printers for automatic printout of linked (external) files. You can add special printers in order for the user to print, e.g., document files in A3 size to a printer that manages that document size. You can add three printers for linked files. This can be useful e.g. in order to manage different paper sizes.
When linking a file on a record (for example on an operation in a BOM and routing), you mark Automatic printout and select which of the printers Extern 1–3 should apply when printing this specific linked file. The selected printer will then be saved in the file link on the record.
> As standard you can have automatic printouts of linked files in PDF format. If you have other file formats that you want to link and print automatically (for example Word files, Excel files, image files, or CAD files) you must have the option called [Extended file viewer](../../../UserGuide/Options/ExtendedFileViewer.htm).

#### Printout format for Shipping – Label
Here you determine the printout size and format on transport labels printed in the Register shipment procedure. You choose the printout format based on which shipping service is used in the company. In the Documents/Printers table you also add the document Shipping – Label and connects the correct Local printer (driver). You choose printout format for the user as described below.
The company uses the nShift Web-TA service
- PDF (Web-TA) – Printout on label using label printer. The printer should have the driver for the current model.
- ZPL (Web-TA) – Printout on label using Zebra compatible label printer. The printer must have the driver Generic / Text Only.
> The printout format PDF (Web-TA) is recommended as the printout quality will be better and the PDF format is regularly maintained by nShift based on changes from the shipping agents.
The company uses the nShift Delivery and Pacsoft Online services
- Two STE labels (107 x 251 mm) on A4 – Printout of two labels in size A4 using laser printer (common alternative).
- STE label 107 x 251 mm – The same as above but one label using laser printer or label printer (common alternative).
> The printout format STE label 107 x 251 mm is recommended if you have a label printer. If you have a regular A4 laser printer, you are recommended to use the printout format Two STE labels (107 x 251 mm) on A4.
The alternatives below are intended for labels in A5 size or if you already have a label printer and labels in one of the specified sizes.
- A5 label – Printout of one label in size A5 on A4 sheet size using laser printer.
- Two A5 labels on A4 – The same as above but two labels.
- Label 107 x 190 mm – Printout of one label in existing label printer.
- Label 107 x 72 mm – As above.
- Label 107 x 165 mm – As above.
The company uses both nShift Web-TA and nShift Delivery or Pacsoft Online services
If the user has a printout format configured for one of the services, and prints transport labels for the other service – then the most suitable printout format for that service will be used.

#### Integrated printer queue (Logtrade)
This will override the printer queue entered in the Integrated printer queue setting in the Shipping services procedure, when this user exports the shipment to Logtrade from the Register shipment procedure.

#### Printing of linked files – Manufacturing
Here you decide the user's printing order regarding linked files (for order, part node, operation, and material) which are printed together with order documents (traveler, operation document, material document) for manufacturing orders and maintenance orders. This setting will override a general system setting with the same name. You can also override the setting per printout in the Register manufacturing order, Print manufacturing order, and Register maintenance order procedures. The available options are:
- Do not print – Linked files will not be printed.
- Print last – Linked files are grouped together and will be printed last after the order documents.
- Print by order number – Linked files are grouped together and are printed after each manufacturing order or maintenance order.
- Print by part – Linked files are grouped together and are printed per part node in the order.
- Print by operation – Linked files are grouped together and are printed per operation in the order.

#### Linked files
Mark the checkbox called Pre-select "Automatic printout/e-mail attachment" when linking files if you want linked files to be printed/sent via e-mail automatically for the user.

#### Documents/Printers
In this table you can link a Local printer and Server printer, if any, to different documents and customized reports.
The Variant column shows all document variants created in the Document templates procedure. This makes it possible to use different printers for different document variants.
Local printer is mandatory and means that when the user prints the document/customized report in question in the Windows client, the printer is default in the printer dialog.
Server printer is only used/linked if the user should be able to print documents from the mobile client. The server printer must first be registered in the Server printers procedure.
In the Type column you select Document if you want to connect printers to different documents. You can then select from the available documents in the Documents column. If you want to link/connect a local printer and a server printer, if any, to customized reports, you select Customized report in the column. You can then select from the created customized reports in the Documents column.
For the documents or customized reports to which you do not link a printer here, the Standard printer selected will apply.
For the Shipping – Label document it is important that you link the correct printer based on the Printout format for Shipping – Label selected.
