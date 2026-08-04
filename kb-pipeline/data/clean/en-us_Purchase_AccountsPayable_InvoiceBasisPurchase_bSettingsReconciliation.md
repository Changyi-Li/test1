### Settings – Reconciliation
These settings apply to the list type Reconciliation.

#### Show only main rows
This checkbox determines whether or not only main rows should be displayed. Associated sub-rows such as additional texts and included parts in fictitious part, will not be displayed.

#### Only show orders with a difference
With this setting you determine if only orders with differences between invoice basis and general ledger should be shown.

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
This setting is available for the price alternatives Standard price and Historical standard price. It determines if SO mark-up (storage overhead) should be added to the price of purchased parts in the list.

#### Valuation time
The historical value which can be based on the log date or actual date. In the date field, you can enter the historical date.
"Log date" means the date and time for when the arrival was reported in the system. "Actual date" refers to the date which was entered as actual arrival date at the time of the reporting. For example, if the arrival was reported some time after it took place, you can enter a date in passed time in order to get the arrival backdated.
- Historical value (log date) – With this option, all arrivals (regardless of actual date) will be loaded to the list if they have a log date which corresponds to or is earlier than the entered date. The arrivals become loaded if they are not linked to an invoice. Orders will be loaded even if they are arrival reported (log date) on the selected date or earlier, but the invoices’ voucher dates are later than the selected date.
- Historical value (actual date) (default) – With this option, all arrivals (regardless of log date) will be loaded to the list if they have an actual date which corresponds to or is earlier than the entered date. The arrivals become loaded if they are not linked to an invoice. Orders will be loaded even if they are arrival reported (actual date) on the selected date or earlier, but the invoices’ voucher dates are later than the selected date.

#### Create voucher for settlement per order number (rounding)
Here you decide if a voucher should be a created for the rounding. In the list you can see which rows/orders will be included in the voucher. The voucher is saved by clicking the Approve ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_approve_document.png) in the toolbar. The purpose of the voucher is to get rid of roundings that create differences. In the voucher, debit and credit are recorded to the same account but with the order number on one side, depending on whether the difference is negative or positive.

#### Amount limit for difference
Here you can enter an amount limit, meaning the maximum amount the difference can be for it to be possible to create a voucher. There is a default amount limit entered, but it can be changed.

#### Voucher number series
The voucher number series that will be used for the voucher being created.

#### Voucher text
In this box you can enter a voucher text for the voucher that is created. There is a default voucher text entered, but it can be changed.

#### Voucher date
Here you can enter the voucher date. The date used by default is the one that has been entered in the date field for Valuation time.
