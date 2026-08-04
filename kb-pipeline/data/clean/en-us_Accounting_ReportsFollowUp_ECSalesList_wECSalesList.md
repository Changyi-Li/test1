## EC sales list
In this procedure you load bases for reporting of EU statistics.
It is possible to manually report this outside the system. For certain countries there is support in the system to electronically submit the reporting via a file. This reporting can either be made per month or per quarter. Which time period is used is determined by the date selection when the report is being printed.
Basics
The EC sales list concerns all trade with EU countries and this should be accounted for per VAT registration number (the buyer's). Per VAT registration number you see the following information:
- Value of goods delivery
- Value of three-party trading
- Value of services
Prerequisites for reporting of goods delivery:
- The buyer (recipient of invoice) is registered for VAT in another EU country.
- The goods are delivered to another EU country (country of the buyer or another EU country).
Prerequisites for reporting three-party trading:
- The buyer (recipient of invoice) is registered for VAT in another EU country.
- The goods are not delivered from the own company but is delivered directly from a seller in another EU country to the buyer. That is, three EU countries must be involved.
Prerequisites for reporting of services:
- The buyer (recipient of invoice) is registered for VAT in another EU country.
- The service must have been performed/executed in the country of the buyer.
How the EC sales list works in Monitor ERP
The EC sales list loads data from the Accounting module and the Sales module to compile this report. The system reads all vouchers which concern sales to customers, where the VAT registration number of the customer belongs to an EU country.
The following prerequisites are needed to get a correct reporting:
- The integration of customer invoices must be detailed per invoice, that is, the option Direct per invoice or Via journal per invoice must be selected for the integration setting in the procedure Voucher number series/Journals. Manually recorded vouchers will not affect the report (except for rectifying vouchers for customer invoices).
- VAT codes concerning EU sales should be linked to report for EC sales list. This link is created under the VAT codes tab in the VAT settings procedure.
- The VAT registration number including the country code must be registered for the customer in the customer register. The report will include the customers whose VAT registration number has a country code belonging to EU and is posted as EU sales.
Loading of data to the report
The data loading for the report basically follow the same logic as the regular VAT report, where values in the VAT report concerning trade with EU should show the same values as the EC sales list. The report loads data from voucher rows posted as EU sales, either via the account or via the VAT code (determined by a system setting described below).
In the same way as in the regular VAT report the system setting Basis for VAT report is loaded from affects how the values are loaded to the report. If the option VAT code in chart of accounts has been configured for the system setting, then the report will show all transactions on customer invoice vouchers which contain accounts linked to a VAT code marked for EC sales list. If the option VAT code in general ledger transactions has been configured for the system setting, then the report will show all transactions on customer invoice vouchers which contain VAT codes concerning EC sales list.
Customer number, invoice
In the system it is possible to use the function Customer number, invoice. This means that there are two different customer numbers involved in the sales flow. On one hand you have the customer number on which the order was registered and on the other hand you have the customer number that is used on the invoice, that is, the customer number that will receive the invoice. The EC sales list loads the VAT registration number on the order customer. This means that it is the order customer’s VAT registration number which is shown on the customer invoice document and which is recorded in the EC sales list. If you instead want the customer on the invoice to be governing for the EC sales list, there is a setting in the customer register to use on the Order customer. This setting is called Use VAT registration number from customer number, invoice. You find this setting under Miscellaneous in the Customer register procedure.
Alternative delivery address with exception VAT registration number
If you have Exception VAT registration number for alternative delivery address for the customer in the Customer register, the invoice will be sent to a central invoicing address, but arrival reporting is done in another place and the customer submits a separate VAT registration number for their purchase (often in another country). This allows the VAT registration number to be shown correctly on the customer invoice, intrastat, and EC sales list in these scenarios without needed to register them as separate customers.

#### Export of EC sales list
It is possible to export EC sales list to file. To do this you should load the list and then click the button Export ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_export.png) in the toolbar of the procedure. The default path for the export file is configured in the procedure Settings for export/import.
> Please note! The contact information has to be entered to be able to export the file.
List types

#### Total
This list type is shown as total by VAT registration number. The VAT registration numbers are loaded from the customer register. It is possible to expand the rows and see detailed information.

#### Detailed
This list type shows a detailed list grouped by customer. The list shows detailed information per invoice.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
