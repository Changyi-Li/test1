### Settings – Detailed/ Total
These settings are available for the list types Detailed and Total.

#### Show only main rows
This checkbox determines whether or not only main rows should be displayed. Associated sub-rows such as additional texts and included parts in fictitious part, will not be displayed.

#### Show alloy cost
With this setting you decide whether or not rows with alloy costs should be displayed in the list.

#### Price Alternative
Here you select the price that should be used in the list. The price alternatives that can be selected are:
- Purchase price (default) – With this alternative, the purchase price on the order row will be shown.
- Standard price – With this alternative, you will see the current standard price loaded from the part register.
- Historical standard price – With this alternative, the standard price that applied at the time of the arrival reporting will be used. For subcontract purchase orders, the purchase order price is used instead.
- According to price list – With this alternative, the field called Price list will become available. There you select which price list to use.
- Historical standard price excl. expenses – With this alternative, the standard price that applied at the time of arrival reporting, excluding expenses, will be used.

#### Include SO for P-parts
This setting is available for both standard price alternatives. It determines if SO mark-up (storage overhead) should be added to the price of purchased parts in the list.

#### Convert price each according to rate type
With this setting you determine if "price each" in foreign currency should be converted to the present exchange rate in the Currencies procedure. If the checkbox is not checked, the exchange rate saved on the record will be used instead. Which rate type to use is selected in the field below.

#### Rate type
The rate type you select here is used to convert "prices each" and price lists in foreign currency to the now applying exchange rate for the selected rate type. The default rate type is From supplier/order type. You register rate types in the Currencies procedure.

#### Show foreign currency
Purchase price. With this setting you determine if all values should be displayed in the foreign currency. A total per currency is shown at the bottom of the list.

#### Include
Here you select which types of invoices you want to include in the list. The available alternatives are based on the status of the invoices. If you mark Not linked and Linked, not final recorded, you can create reports to use when reconciling the stock. Specifically used to see the value of what has been arrival reported to stock but has not been recorded.

#### Valuation time
With this setting you decide if the current value should be shown in a report as for today, or if a historical value for a passed date should be shown. The historical value can be based on the log date or actual date. If you select one of the historical values, the date field will become available where you enter the historical date in question.
"Log date" means the date and time for when the arrival was reported in the system. "Actual date" refers to the date which was entered as actual arrival date at the time of the reporting. For example, if the arrival was reported some time after it took place, you can enter a date in passed time in order to get the arrival backdated.
- Current value – With this option, the valuation time will be today. This option is selected by default.
- Historical value (log date) – With this option, all arrivals (regardless of actual date) will be loaded to the list if they have a log date which corresponds to or is earlier than the entered date. The arrivals become loaded if they are not linked to an invoice. Orders will be loaded even if they are arrival reported (log date) on the selected date or earlier, but the invoices’ voucher dates are later than the selected date.
- Historical value (actual date) – With this option, all arrivals (regardless of log date) will be loaded to the list if they have an actual date which corresponds to or is earlier than the entered date. The arrivals become loaded if they are not linked to an invoice. Orders will be loaded even if they are arrival reported (actual date) on the selected date or earlier, but the invoices’ voucher dates are later than the selected date.
