### Intrastat export/import
IntrastatIntrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. reporting is carried out in the Intrastat export and Intrastat import procedures.
Intrastat export is based on statistics loaded from the supplier invoice log (invoices), delivery log (stock order), manufacturing order log (shipment records for subcontract), and adjustment log for Intrastat.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Intrastat_export_overview.png)](../../../../Resources/Images/UserGuide/Intrastat_export_overview.png)
Intrastat export.
Intrastat import is based on statistics loaded from the supplier invoice log (invoices), arrival log (stock orders and purchases from suppliers for which a supplier invoice is not linked), and adjustment log for Intrastat. Please note that for orders not linked to invoices, the order price is used instead of the invoiced price.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Intrastat_import_overview.png)](../../../../Resources/Images/UserGuide/Intrastat_import_overview.png)
Intrastat import.
The workflow in the procedures is as follows:
1. Make a selection by date
2. Load the list
3. Check the result and any warnings issued
4. Adjust/add records
5. Save
6. Print or export the list by clicking Export ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_export.png) in the toolbar

#### The Selection tab
In the upper section, you do not have to make any selections to choose the records to be reported. The system detects this automatically. However, selections can be made in order to search for data in the Intrastat report (e.g., when troubleshooting).
In the date field, enter the period to be reported.
In the Include field, you can choose for a stock order to be included. For exports, you can also specify if subcontract shipments abroad are to be included.
Check that the correct shipment country is specified (in cases where the company has warehouses in multiple countries).

#### List
The Intrastat report itself is summarized in this tab.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Intrastat_export_list.png)](../../../../Resources/Images/UserGuide/Intrastat_export_list.png)
In the upper box, the total amount of the goods records is summarized per combination of Country, CN code, Country of origin, and Transaction type.
In the lower box, you see the detail records included in the row you selected in the upper box. The information in the upper box must be included in the report for Intrastat import.

#### Adjustments
The report can be adjusted in different ways. For example, you may wish to include records that are missing or incorrect.
1. In the upper box, you can correct the existinggoods records by editing either the Amount adjustment or Total amount columns.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Intrastat_adjust1.png)
2. In the upper box, you can click Add new row at the end (F5) in order to add new goods record rows in the Intrastat report. That is, rows in the Intrastat report that were not there before. Please note that the weight and quantity, if any, are entered in the lower box. If necessary, such adjustment records can be deleted in the upper box.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/Intrastat_adjust2.png)
The adjustments stated above are saved in a separate adjustment table in the system. They can be accessed the next time you generate the report. Remember to save the list, to ensure the adjustment records are saved.
3.   
As the Intrastat information is entered manually on order rows, it may be necessary to change the KN number, weight and/or transaction type directly in the invoicing log afterwards. This is done via a link to the Invoicing log procedure from the row.

#### Export to the authorities
The Intrastat report can also be exported to a file. When you have made a change to the report, save before exporting. Settings for the export are made in the Settings for export/import procedure.
The Warnings tab
Warnings relating to the Intrastat report are shown in this tab. Please note! You can print a list of warnings by using the Print/Send button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_mail_and_print.png) (Ctrl + P).
| Occurring warnings | When does this warning appear? | Action |
|---|---|---|
| CN code is missing | This warning appears if the country code in a delivery address or the country code for the warehouse is within the EU, but the CN code is missing (does not apply to services). Row type 2 and sub-parts for fictitious parts are excluded from this check. The check is made for all order types (including stock orders and subcontracts). | If these parts are to be included in the Intrastat report, you must enter a CN code for the parts in the Part register. |
| Weight is missing | This warning appears if the country code in a delivery address or the country code for the warehouse is a country within the EU, and a CN code exists, but no weight has been entered even though the CN code is configured to report weight. This check is also made for row type 2 and services. In this case the record will be shown in the Intrastat report, although the weight may be incorrect. | Enter weight for the parts in the Part register or Subcontract parts procedures. |
| The delivery is outside the EU (simple VAT handling) | This warning is shown if you report the delivery as trade in goods (EU) in the VAT report, but the delivery has not been sent to the EU. This check only applies to invoices (not stock orders or subcontracts). | If the record is to be included in the Intrastat report, the country must be changed on the delivery address. Use the link to go to the Update accounts receivable or Register supplier invoice procedures, and change the country on the invoice. If the record is not to be reported as EU trade, the invoice must be posted again so it will not be included in the VAT report as EU trade. |
| The delivery is outside the EU (advanced VAT handling) | This warning is shown if you report the delivery as trade in goods (EU) in the VAT report, but the delivery has not been sent to the EU. In this case, the record is included in the VAT report as trade in goods (EU), but is missing in the Intrastat report. This check only applies to invoices (not stock orders or subcontracts). | If the record is to be included in the Intrastat report, the country must be changed on the delivery address. Use the link to go to the Update accounts receivable or Register supplier invoice procedures, and change the country on the invoice. If the record is not to be reported as EU trade, the invoice must be posted again so it will not be included in the VAT report as EU trade. |
| Account does not concern trade in goods (EU) (check for simple VAT processing) | This warning appears if the country of delivery is in the EU, but the account used to record the transaction does not refer to goods traded in the EU. In that case, the record will be shown in the Intrastat report, but is not booked as trade in goods (EU) in the VAT report. This check only applies to invoices (not stock orders or subcontracts). | If the record is not to be reported in Intrastat, the country on the invoice must be amended. Use the link to go to the Update accounts receivable or Register supplier invoice procedures, and change the country on the invoice. If the record is to be reported as EU trade, the invoice must be posted again so it will be included in the VAT report as EU trade. |
| VAT code does not concern trade in goods EU (check for advanced VAT processing) | This warning is shown if the country of delivery is in the EU, but the VAT code that appears on the invoice row does not refer to goods traded in the EU (using the same logic as above). In this case, the record will be shown in the Intrastat report itself, but is not reported as trade in goods EU in the VAT report. This check only applies to invoices (not stock orders or subcontracts). This check is only made if the VAT report loads the VAT code from the general ledger transaction. | If the record is not to be reported in Intrastat, the country on the invoice must be amended. Use the link to go to the Update accounts receivable or Register supplier invoice procedures, and change the country on the invoice. If the record is to be reported as EU trade, the invoice must be posted again so it will be included in the VAT report as EU trade. |
| The part is missing reporting unit | A warning appears if the CN code is set to report another quantity, but the unit in question is not registered for the part in the part register. The check is made for all order types. In this case, the goods will not be included in the Intrastat report. | If the records are to be reported you must register a valid unit for the parts in the part register. (It is enough that it is registered as an alternate unit with the correct conversion factor.) |
| VAT registration number is missing | This warning appears if the VAT registration number is missing for the customer. | Enter VAT registration number for the customer in the Customer register. |
In certain cases, multiple warnings can be displayed for the same record (for example, if both weight and CN code are missing).
