### Result
In the Result box you see the invoice bases you selected under the Selection tab. You can check the invoice bases that you wish to review in the Invoice box to the right, before invoicing. Adjustments, if any, are then made in the Edit invoice window which you access by clicking the Edit invoice button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit.png). You can also choose not to include individual bases and you can change the status from 1 (For invoicing) to 3 (Pending), and vice versa.

#### Include
With this checkbox you determine if the invoice basis will be included in the invoicing. The checkbox is marked by default. If you uncheck the setting, the invoice basis will not be invoiced. Invoice bases with status 3 (Pending) are displayed in the result list if you have chosen to include them under the Selection tab, but you cannot include them in the invoicing. However, you can review invoices with status 3.

#### Customer
Here you see the customer number of the customer on the invoice basis.

#### Order number
Here you see your order number/partial delivery number on the invoice basis. Prefix, if any, is displayed before the order number. If it is a comprehensive invoice, you will see several order numbers after each other. The customer number is only stated for the topmost order.

#### Reserved invoice number
Here you see the reserved invoice number if the Use invoice number for pro forma setting under Other invoice settings in the Customer register procedure is set to Yes, from pick list or Yes, from invoice basis.

#### Invoice type
In this column you can see which type of invoice basis the row concerns: Invoice, Internal, Cash receipt, or Interest.

#### Status (St.)
Here you see the status of the invoice. It is displayed with a symbol on the button in this column. You can change the status from 1 (For invoicing) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusRegistered.png) to status 3 (Pending) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpStarted.png) by clicking the button.

#### Printing method
Here you choose printing method for the invoice in question. The available alternatives are E-invoice, Printer, or E-mail, that is, if the document should be sent to an operator of e-invoices, should be printed to a printer, or attached as a PDF file to an e-mail message. The printout can be executed when the invoice basis has been approved.

#### Document variant
Here it is possible to select a different document variant than the default, on which this invoice basis should be based. The default variant of the invoice document is configured in the procedure Document templates.

#### E-invoice
For customers who have e-invoice activated, the system will suggest for the invoice to be sent electronically. In the column E-invoice you will find the following options:
- No – Do not export e-invoice
- Yes – Export e-invoice
- Yes + Printout/E-mail – Export e-invoice and print it on paper in Monitor ERP/send via e-mail from Monitor ERP. If you have selected Yes + Printout/E-mail, you can also select printing method. The default printing method is configured on the customer.
- Save to file – If you have entered a Path for manual validation of e-invoice file in the Settings for export/import procedure, this option is available. This is used, for example, if you need to send the e-invoice to the Support Center for troubleshooting (by reprinting), or to send it to a customer for verification before going live. At this time an e-invoice is not sent to the operator/customer.

#### Conflicts
If there is a conflict on the invoice, you will here see the button Conflicts ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_information.png). By clicking it you can see what is causing the conflict. It might for example be that another user has the invoice open in the procedure Register invoice directly. When a conflict exists, you cannot include the invoice for approval.

#### Delivery note number
In this column you see the delivery note number of the delivery.
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

#### Factoring
With this setting you select if factoring should be used for this invoice. If factoring is activated for the customer in the Customer register, this checkbox will be activated by default on the invoice.
