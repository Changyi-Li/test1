### Import
In this box you configure settings for import from the supplier.

#### Languages
The language selected here will be used e.g. in price lists. However, your choice of language will not affect the language used on all documents. The language used on documents is determined by what is configured for the country you entered for the order’s mailing address or delivery address. All languages you want to select among in this field must first be registered in the Languages procedure.

#### Regional formats
Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you decide which date format, decimal separator, and time zone, to use.
- Date format – In this field you select the date format you wish to use when communicating with the company in question.
- Decimal separator – Here you decide whether to use stop/period or comma as decimal separator when communicating with the company in question.
- Time zone – Here you select the time zone where the company in question is located. The default time zone in the field is the same as has been entered for the own company in the Company information procedure.
- Local time – Here you can see the current date and the time on site at the registered company, based on the selected time zone.

#### Currency
The currency you select via the button Change currency ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) will be shown by default. All currencies you want to select among in this field must first be registered in the Currencies procedure.
With the checkbox Supplier prices, you decide if the supplier prices (supplier links on the part) should be updated. Price each, staggering prices, setup prices, and future prices will also be recalculated with the correct exchange rate. This also applies to subcontract parts.

#### Rate type
You can enter a rate type if the supplier uses a foreign currency (a currency other than the company currency in the company information). The default rate type is loaded from the Default rate type system setting under the Purchase tab. You register rate types in the Currencies procedure. With the use of different rate types you can handle parallel exchange rates for the same currency, for example, one variable USD rate and one fixed. But it can also be unique rate types to be used for individual suppliers. The rate type entered for the supplier will determine which rate will be used when registering orders, supplier invoices, etc. Please note! When changing rate type for a supplier, it will not have any effect on the orders and invoices which have already be registered for the supplier.
