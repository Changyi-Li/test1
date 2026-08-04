### Result
After having loaded the list you will see here the invoices or pro forma invoices that you can print, based on the selections made under the Selection tab.
In this box you will, for example, see information about customer name, invoice number, order number, and printing method (printer or e-mail).
By checking the box Include, you decide which invoices will be included in the printout. Below the list you will see a total of the number of invoices. You can also see how many of them that will be printed and how many will be e-mailed.
After having executed the printout by using the button Print/Send (Ctrl + P) in the toolbar of the procedure, you can with the Approve checkbox decide which invoice printouts to approve. You approve by using the Approve button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png). The status of printed approved invoices will then be changed to 9 (Printed).
By using the button Cancel ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_cancel.png), you cancel the printout you just made. The procedure then will go back to where it was before you made the printout, and no status will be updated on any of the invoices.

#### Include
In this column you determine if the invoice should be included in the printout.

#### Customer
In this column you see the customer number and customer name.

#### Invoice number
In this column you see the invoice number.

#### Order number
Here you see the order number on which the invoice is based.

#### Printing method
You can choose if the invoice should be printed on a printer or should be sent with e-mail.

#### Document variant
Here it is possible to select a different document variant than the default, on which this invoice basis should be based.
For customer orders you can use document variants per order type for order confirmations, invoices, delivery notes, and transport labels. You register this in the Order types procedure under the Customer order tab. The document variant can be entered per customer in the Customer register.
When registering quotes, customer orders, and invoices, as well as at delivery, the document variant will be applied according to the following priority:
1. The document variant specified for the customer in the Customer register.
2. The document variant specified on the order type in the Order types procedure, under the Quote tab or the Customer order tab.
3. The default document variant in the Document templates procedure.

#### Document variant – Invoice
Here you can choose a document variant for the pro forma invoices.
When registering quotes, customer orders, and invoices, as well as at delivery, the document variant will be applied according to the following priority:
1. The document variant specified for the customer in the Customer register.
2. The document variant specified on the order type in the Order types procedure, under the Quote tab or the Customer order tab.
3. The default document variant in the Document templates procedure.

#### Document variant – Comprehensive invoice
Here you can choose a document variant for the pro forma comprehensive invoices.
When registering quotes, customer orders, and invoices, as well as at delivery, the document variant will be applied according to the following priority:
1. The document variant specified for the customer in the Customer register.
2. The document variant specified on the order type in the Order types procedure, under the Quote tab or the Customer order tab.
3. The default document variant in the Document templates procedure.

#### EDI export
If the customer on the invoice is connected to EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. in the customer register, this column is shown. If so, Yes is selected by default, meaning the invoice will be exported an sent using EDI. You can select No to not export and send the invoice via EDI. If you select the option Yes + Printout/E-mail, the invoice will be exported via EDI and you also get a printed invoice or send it via e-mail, depending on the selected Printing method. This option can also be configured to be default using the setting Printout/e-mail during export of EDI in the specific behavior the customer is linked to in the procedure EDI behavior.
An invoice can also be excluded from EDI via a setting on the invoice in the procedure Register invoice directly. In that case, the invoice will not be exported and you can also not choose anything in this field.

#### E-invoice
If the customer on the invoice has the setting Use e-invoice activated in the customer register, this column is shown. If so, Yes is selected by default. You can select No to not send an e-invoice, or Yes + Printout/E-mail if you both want to send an e-invoice and get a printed invoice or send it via e-mail, depending on the selected Printing method. The e-invoice will be sent when you approve the invoice with the Approve button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png).
If you have entered a Path for manual validation of e-invoice file in the Settings for export/import procedure, there is an option called Save to file. This alternative is used, for example, if you need to send the e-invoice to the Support Center for troubleshooting (by reprinting), or to send it to a customer for verification before going live. At this time an e-invoice is not sent to the operator/customer.

#### Approve
This column is shown after you have printed/sent the invoice. Printed invoices are marked by default for approval. Invoices which you then approve using the Approve button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) will get status 9.

#### Conflicts
In this column you see a button with a red padlock ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png) if one or multiple conflicts have occurred on the invoice. This can happen for example if another user has the same invoice open for printout. By clicking the button you see which user is concerned and the time when the user loaded the invoice. If a conflict exists, you cannot include the invoice for printing.
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Name of customer
Here you see the customer name.

#### Warehouse (WH)
Applies if you have installed the Warehouse option). If you change to another warehouse you will see the WH column. On the rows which belong to another warehouse than the selected warehouse you will see a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses_alt.png) in the column. A tooltip for the symbol informs you of which warehouse the row belongs to. Values and texts in all columns for these rows are displayed in italics.
In many of the procedures you can change the warehouse which you will be working in by using the Companies/Warehouses button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure. It is also possible to generally change in which warehouse to work. This is applied to all procedures.This is done in the desktop backstage.. In registration procedures for quotes, inquiries, different orders, and invoice bases, you can in a field select to which warehouse the record belongs.

#### Order type
Here you see the order type.

#### External delivery note number
Here you see the external delivery note number, if such exists.
