### Registration of supplier invoices
E-invoices in Peppol BIS 3.0 format are registered in the Register supplier invoice procedure.
1. Open the Register supplier invoice procedure.
2. Select the inbox for e-invoices in the navigation panel.

![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/EInvoicePeppolInbasket.png)
3. Start the import by double-clicking on, or selecting the invoice, and click Import invoice![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png). By clicking Refresh ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png), you can update the information in the navigation panel. This can be useful if you want to see if any new invoices have arrived while the procedure has been open.
4. The Import supplier invoice window opens when the invoice is imported.
5. The system automatically looks for the right supplier by using the VAT number on the imported invoice. If the VAT number for a supplier can be found in the supplier register, this supplier is selected automatically. The right supplier can also be found using the EIA number. If the supplier cannot be found, you can enter it manually.
6. All invoice rows are shown in the upper box. If the order and order rows are in the system, they are linked in the next step when the invoice is created. If something goes wrong during the import, warnings are shown. See Warnings during import for suitable actions.
7. Click Create in order to create the invoice. The invoice is shown in a separate window on the right. The information from the invoice file is imported, and certain information from the invoice file is matched with data in the supplier register. Data which does not match is indicated by a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png).
8. Under the Order link tab, the quantity reported for arrival is matched with the invoiced quantity, price per unit, and discount. If the values in the e-invoice differ from those on the order row, warnings are displayed.
9. When the invoice is saved, it is removed (PDF and XML) from the inbox.
