# Electronic Invoice Management (EIM)
Electronic Invoice Management (EIM) enables you to electronically manage invoices received from suppliers and link them to supplier invoices in Monitor ERP. EIM also provides support for electronic authorization. This enables signers to receive reminders and messages regarding authorization and final recording.

#### How does EIM work?
Supplier invoices can be placed in Monitor ERP in different ways:
- Invoices (paper) that are scanned to PDF files and become placed in a specific directory (inbox).
- Invoices (PDF) sent by e-mail can be dragged straight from the e-mail client and dropped into an invoice viewing window.
- Monitor-to-Monitor e-invoices (XML + PDF) will be shown in a specific directory (inbox).
- Invoices (paper) that are scanned, interpreted, and are then automatically imported.
- E-invoices automatically imported.
- Invoices (PDF) received via e-mail, that are automatically interpreted and should be verified in Monitor ERP before they are registered.
When supplier invoices are registered in Monitor ERP, the invoices are imported from the specified inboxes. Alternatively, an invoice file can be manually dragged with the cursor from an e-mail client and dropped into the invoice viewing window.
The PDF file is used to provide an image of the paper invoice. The XML file is used to import data from the supplier invoice for registration. The data in the XML file is matched in an import window with the correct purchase order and invoice basis in Monitor ERP.
An invoice can also be preliminary recorded, rather than being registered. You can also final record invoices directly upon registration and preliminary entry, provided that the signer has the user rights to do so. An alternative is to final record the invoice after it has been authorized by one or more signers.
EIM also provides support for authorization lists and signer groups.

#### Interpretation
You can activate a function to interpret and import invoices. This function is linked to CrossState (OptoSweden) via an API in Monitor ERP. CrossState is a cloud solution for scanning and data capture/interpretation of supplier invoices.
The data capture/interpretation function facilitates registration of the invoices since no manual registration of information from the invoice is necessary to perform.
Particularly effective in combination with the EIM Workflow option, EIM Invoice Capture automates the entire invoice flow in Monitor ERP, from interpretation and import of supplier invoices to authorization and final recording. Read more about [Capture/Interpretation](EIMInvoiceCapture.htm).

#### E-invoice
You can activate a function to import e-invoices in EIM. This makes it possible for your suppliers to send you e-invoices which will automatically be imported in Monitor ERP.
You can also activate a function to export e-invoices. With this function you can send e-invoices to those of your customers who are able to receive e-invoices. Read more about [E-invoice](EInvoice.htm).

#### EIM Workflow
EIM Workflow is an option which automates the invoice flow in Monitor ERP, from registration, linking to purchase order, authorization, to the final recording of the invoices.
By using EIM and the EIM Workflow option, you can achieve a fully digitalized and automated invoice flow in Monitor ERP. This is unique in the industry. Read more about [EIM Workflow](EIMWorkflow.htm).
Functionality overview
| Function | EIM | Interpretation | E-invoice | EIM Workflow** |
|---|---|---|---|---|
| Manual invoice registration | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |   |   |
| Manual import MONITOR-to-MONITOR* | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished_15x15.png) |   |   |   |
| Automatic import MONITOR-to-MONITOR* |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |
| Automatic import of captured invoice |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |   |
| Automatic import of e-invoice |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |
| Send e-invoice |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |
| Electronic authorization circulation | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |   |   |
| Authorization via app/web | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |   |   |
| Authorization limits | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |   |   |
| Reminder management | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |   |   |
| Manual final recording | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |   |   |
| Automatic final recording |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |
| Automatic purchase order matching |   |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |
| Authorization/authorization control at row level | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |   |   | ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) |
* Monitor-to-Monitor
**Additional option for EIM
Interested in finding out more? Please contact our Sales department using this [form](https://www.monitorerp.com/sv/kontakt/). Want to find out more? Sign up to our upcoming [Monitor Demos](https://www.monitorerp.com/sv/kunskapsbank/effektivisera-med-monitor-erp/monitor-demos/) (Swedish).
