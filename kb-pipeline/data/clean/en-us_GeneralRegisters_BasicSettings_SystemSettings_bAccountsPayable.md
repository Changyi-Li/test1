### Accounts payable

#### Create invoice basis at arrival of
This system setting determines if a supplier invoice basis is to be created when reporting arrivals of purchase orders. The available alternatives are Purchase order and/or Purchase order (subcontract). If the alternatives have been activated then it is possible to link a purchase order when registering the supplier invoice.
The system setting also affects the purchase statistics. The purchase statistics can be loaded in the Supplier invoice log procedure both as detailed and total statistics per consecutive number, supplier, voucher date, or part.
If none of the alternatives has been activated in the system setting, you cannot load statistics at part level in the Supplier invoice log procedure. Then you must use the Arrival log procedure instead. However, you can always see purchase statistics, arrival log, and statistical prices at part level in the Part register procedure. This applies even if none of the alternatives has been activated.
The supplier invoice log for the part will be empty if you do not link purchase orders to supplier invoices. However, in the Part register procedure you will always find information under the buttons Purchase statistics and Arrival log as well as different statistical prices. These are based on the price on the purchase order.
If you link a purchase order to a supplier invoice, then the arrival log, purchase statistics, and statistical prices will also be updated in connection with the arrival reporting. The difference is that when you then link the invoice to the purchase order, the supplier invoice log will also be updated and the system will adjust the purchase statistics and statistical prices afterwards in case the price differs on the invoice.
If you have activated the alternative Purchase order you can, in the Supplier register procedure, create an exception per supplier by using the system setting called Do not create invoice basis. If you have activated the alternative Purchase order (subcontract) you can, in the Work center A work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register procedure, create an exception per work center (of type Subcontract) by using the same setting Do not create invoice basis.
If an exception is activated per supplier or subcontracting work center, no invoice basis will be created when the purchase order for the affected supplier is arrival reported. The purpose is to be able to except suppliers whose invoices are not specified per purchase order or in another way will not generate good invoice bases. Otherwise you will risk creating invoice bases that never will be linked to a supplier invoice. In turn, this results in incorrect information about "Arrived, not linked to invoice" being shown in the list in the Invoice basis – Purchase procedure and incorrect purchase statistics. In this case it might be better not to create invoice bases for these suppliers and instead update the purchase statistics at the time of the arrival.

#### Preliminary entry of supplier invoices
This system setting determines if preliminary entry of incoming supplier invoices should be used. This means that invoices registered in the Register supplier invoice procedure will be posted on Preliminary accounts payable and the offset account Preliminary account. Then this procedure will also show the field Prel. entry date: as well as a checkbox called Show preliminary entry, where you can view or modify the posting.

#### Post VAT during
If you apply preliminary entry of supplier invoices at registration, you can choose if the VAT should be reported during preliminary entry or final recording.
Final recording is selected by default.

#### Suggest same voucher date as invoice date
This system setting determines if the Voucher date always should be the same date as the Invoice date selected in the Register supplier invoice procedure. Otherwise the voucher date will be the same as the date selected in that field on the previous invoice.
If you use preliminary entry of supplier invoices (with the system setting mentioned above), then this system setting will also determine that the preliminary entry date will be set to the same date as the selected invoice date.

#### Suggested exchange rate during registration
This system setting determines if the exchange rate during supplier invoice registration should be the current rate or the exchange rate according to the invoice date. The following options are available:
- Current rate – If you select this alternative then the exchange rate that applies at the moment will be used. Current rate is selected by default.
- Rate according to invoice date – If you select this alternative then the exchange rate that applied at the invoice date entered on the invoice will be used.

#### Use exchange rate from XML file
With this setting you decide if exchange rate from XML file should be used. This setting will affect imported e-invoices, captured/interpreted invoices (CrossState) and M2M invoices. For example, if the supplier sends invoices in a different currency as e-invoices (XML file), this setting determines that the exchange rate in the XML file should be used. This system setting will override the system setting above called Suggested exchange rate during registration. If no exchange rate is included in the XML file, the exchange rate will instead be loaded according to the system setting above.

#### Allowed exchange rate difference on imported invoice
If the Use exchange rate from XML file system setting above has been set to Yes, you should in this setting enter the allowed difference in percent.

#### Use VAT amount from imported invoice
With this setting you decide if VAT from the invoice should be used or not during import of supplier invoice. This setting will affect imported e-invoices, captured/interpreted invoices (CrossState) and M2M invoices. If you select No, the VAT code from the supplier will be used instead. The recommended setting is Yes when you are using invoice interpretation via CrossState.
> Please note that if you choose No, the VAT will be calculated based on the default VAT code in the Supplier register. In this case, the VAT is calculated based on the invoice amount and any differences may therefore need to be adjusted manually.

#### Apply signer automatically based on reference in XML file
This system setting determines if invoices that are imported via Monitor-to-Monitor or from XML files should be assigned a signer code automatically based on the file’s reference. This system setting doesn’t apply to invoices imported from CrossState. These are managed via the Settings for export/import procedure.

#### Suggest previous supplier at registration
This system setting determines if the previous supplier should be suggested at registration. If you select Yes, then the previous supplier's information will remain after saving the invoice in the Register supplier invoice procedure. If you select No, then the Supplier field will be emptied after saving.

#### Check against recurring invoice numbers
This setting checks to find if there are any recurring invoice numbers in the Register supplier invoice procedure. You can choose if the invoice number that is already used for the same suppliers should be blocked (not be possible to enter) or if a warning should be displayed. Please note! If you choose the Block option, the block will only apply as of the registration up to and including the final recording. After the invoice has been final recorded, it will only cause a warning.

#### Default payment terms on credit invoices
This system setting determines which payment term should be selected by default on credit invoices. This payment term is also used when the invoice is automatically imported via CrossState or EIM Workflow. The payment term must be registered in the Terms procedure.

#### Load invoice information from purchase order
If some information on the purchase order differs from the information on the supplier, then this system setting determines that the information on the purchase order should be loaded to the supplier invoice at registration. This information is: Payment term, Currency, VAT group, and Supplier group.
Regarding the payment term, it works as described below. A check is made which compares the number of days according the imported invoice with the number of days according to the payment term on the linked purchase order. If the number of days differ, a warning is shown. The number of days according to the invoice is used when registering the supplier invoice.

#### Set invoice status to "Pending" if the order is not arrival reported
With this setting you decide if a supplier invoice (order invoice) by default should be given the status Pending at registration if the corresponding purchase order has not been arrival reported. This system setting is available if you have installed the option Electronic invoice management (EIM). The system setting is set to Yes by default and the material invoices will then be placed in the Pending inbox.
If the EIM Workflow option has been installed, this system setting is not shown. When Workflow is used, the arriving supplier invoices become placed in the Awaiting arrival reporting inbox.

#### Amount limit for rounding when linking an order
Here you enter an amount limit for rounding if a difference occurs when linking purchase orders to supplier invoices in the Register supplier invoice procedure. The default value here is 1.00. The entered value will also be shown to the right of the Diff field under the Order link tab in the Register supplier invoice procedure. The amount you enter is the difference in the company currency. If the invoice is in an external currency, the difference is calculated in the company currency in order to decide whether the rounded amount should be posted automatically or not.

#### Record price differences during invoice registration
This system setting determines if price differences and exchange rate differences should be recorded during the invoice registration. The following options are available:
- No – The price differences will not be recorded.
- Yes, only total price difference – If the invoice price differs from the price alternative on which price differences are measured, then the difference will be posted against the price difference account. If the invoice price is in foreign currency, then the price difference will be multiplied by the exchange rate according to the invoice and will be included in the recording of the total price difference.
- Yes, price difference and exchange rate difference – If an exchange rate difference occurs of the invoice price during the invoice registration, the difference will first be posted on the exchange rate difference account. The rest of the invoice price will then be posted on the price difference account in the same way as in the example above.
If the system setting is set to one of the Yes alternatives then fields for selecting price difference account to each product group and supplier group will open under the Purchase account tab in the Posting matrix procedure. Standard accounts for exchange rate profit and exchange rate loss are included in the chart of accounts. However, it is possible to make exceptions from the standard accounts for exchange rate profit and exchange rate loss during price differences.
When final recording the invoice in the Register supplier invoice procedure you post price differences per order row on the price difference account in cases when the invoice price differs from the price alternative (in the system setting below) with which price differences are compared. If orders/invoices are in foreign currency and an exchange rate difference occurs, then the invoice's rate at the time of arrival is compared with the rate type selected in the system setting Exchange rate difference will compare the invoice's rate with. The exchange rate difference is calculated according to the following formula:
(Exchange rate at the time of arrival - Exchange rate on the supplier invoice) x Price on the invoice in foreign currency

#### Price difference should compare the invoice's price with
If the system setting above is set to one of the Yes options, you configure to which price alternative the price differences should be compared. If you use FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. as stock valuation method, you should select Purchase order price.

#### Price list for price difference
Here you select a default price list if the price difference should be compared with Price list in the system setting above.

#### Exchange rate difference will compare the invoice's rate with
If the system setting Record price differences during invoice registration has been set to Yes, price diff. and exchange rate diff. you use this system setting to determine which rate type should be used in the comparison with the invoice's exchange rate.

#### Part number for [freight charge | packaging cost | alloy cost] when loading XML invoice
In these three fields you select the parts that should be used for freight charge, packaging cost, and alloy cost when loading XML invoices from suppliers. XML invoice is a function e.g. in the Monitor-to-Monitor feature.
Freight charge
Selectable parts for freight charge are parts of the type Service and service type Freight.
If a supplier that also use Monitor ERP, adds a freight charge to the invoice, an invoice row will automatically be created for that cost under the Order link tab. This applies only if the supplier has entered Freight as service type for the service in his part register.
Packaging cost
Selectable parts for packaging cost are parts for which the system setting The part is a packaging part has been activated, under Shipping under the Sales tab in the Part register procedure.
If a supplier that also use Monitor ERP adds a packaging cost to the invoice, an invoice row will automatically be created for that cost under the Order link tab. This applies only if the supplier has checked the box The part is a packaging part for the part in his part register.
Alloy cost
Selectable parts for alloy cost are parts of the type Service and service type Alloy cost.
If a supplier that also use Monitor ERP adds an alloy cost to the invoice, an invoice row will automatically be created for that cost under the Order link tab. This applies only if the supplier has entered Alloy cost as service type for the service in his part register.

#### Number of days before due date when warning should appear
Here you determine how many days before an invoice's due date a warning should appear. The default value is 7 days. When the invoice's due date is within the entered number of days, the date will be displayed in red in the lists in the Invoice overview – EIM procedure as well as in the navigation panel in the Register supplier invoice and Authorize supplier invoice procedures. These are available when the option Electronic invoice management (EIM) is installed.

#### Allowed exchange rate difference on imported invoice
Here you determine the allowed exchange rate difference in percent on imported e-invoices (XML file) in foreign currency. The default value is 0.00 percent. Then no exchange rate difference is allowed. The system setting is ignored if you leave this field empty. An invoice with a greater exchange rate difference than the entered percentage will not be registered during the import. It will instead be placed in an inbox called Failed. The purpose of this system setting is to avoid importing e-invoices with incorrectly interpreted exchange rates to the invoice flow and to the accounts payable.
This system setting depends on that the system setting called Use exchange rate from XML file is set to Yes.

#### Use extended authorization on posting rows
With this system setting you decide if it should be possible to enter who should review/authorize the invoice on posting row level for expense invoices. This setting also determines the head signer for both expense invoices and material invoices (order invoices). Via settings on accounts and dimensions you can determine who should authorize each posting row depending on the posting. This applies to systems with EIM and EIM Workflow.

#### Activate EIM Workflow
This is where you activate EIM Workflow in systems where the EIM Workflow option is installed. When you purchase EFH Workflow, the system setting is deactivated by default.

#### "Order number" after "Supplier" in tab order
Here you decide if you want the Order number field to be the next field to go to after the Supplier field when you press the Tab key in the Register supplier invoice procedure. The default option here is No. This means the Suppl. Invoice no. field will be what the cursor moves to after the Supplier field in the tab order.

#### Add pre-posting on imported expense invoice
This system setting determines if expense invoices imported from CrossState should go to the For registration/verification inbox so you can pre-post the invoice before it is sent for authorization.
If you have the EIM option, it is mainly the e-invoices that will be affected by this setting since these invoices would otherwise be sent for authorization directly (if there is a signer code). Please note! If the e-invoice contains an order number, the e-invoice will be considered an order invoice and will thereby not be affected by the setting.
If you are using the EIM Workflow option, the invoices sent for invoice interpretation to the address for expense invoices, will be handled by the setting. If you only have one address for both expense and order invoices, it is the supplier role that determines if the invoice is considered an expense invoice or not. For e-invoices, the same principle as for EIM is partly applied. That is, e-invoices that contain an order number will be considered to be order invoices. The only exception applies to e-invoices from suppliers that are assigned the roles called Miscellaneous or Shipping agent. Such e-invoices are considered to be expense invoices even if they contain an order number.

#### Use/apply withholding tax
With this setting you decide if withholding tax (WHT) should be activated. With the following system setting called Post withholding tax during you choose when WHT should be posted.

#### Post withholding tax during
With this setting you decide when withholding tax (WHT) should be posted. This setting becomes available when you have activated the use of withholding tax.
The following options are available:
-   
Invoice registration – WHT will be posted at final recording of supplier invoice. When using this option, you need to configure certain settings for WHT for the VAT codes in the VAT settings procedure.
-   
Outgoing payments (default) – WHT will be recorded in connection with outgoing payments. When using this option, WHT will be registered when registering the invoice but is not recorded until you register the outgoing payment in the Outgoing payments procedure. There you can use a write-off code to write off the WHT amount. You enter the write-off code and account in the Bank settings procedure.
