### Settings

#### Show only main rows
This setting determines if only main rows will be loaded to the list. If this setting is not used, order rows on underlying levels will also be included, such as underlying text rows, packaging parts, or sub-rows for fictitious parts.

#### Show alloy cost
With this setting you decide whether or not rows with alloy costs should be displayed in the list.

#### Price alternative
Here you select the price that should be used in the list. The price alternatives that can be selected are:
- Sales price (default) – With this alternative, the sales price on the invoice row will be used in the list.
- Standard price – With this alternative, manually entered standard price on the customer order row will primarily be loaded to the list. Secondarily, the current standard price will be loaded from the part register.
- Historical standard price – With this alternative, a manually entered standard price on the customer order row will primarily be used. Secondarily, the current standard price will be loaded from the time when the order was delivery reported.
- Material cost – With this alternative, a manually entered standard price on the customer order row will primarily be loaded to the list. Secondarily, the material cost will be loaded from the part register.
- Price list – This alternative will activate the next field where you can select a price list.
- Historical FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price – This alternative shows what the FIFO price was at the time of the delivery reporting. This means that even if the FIFO price is different today, you will still see the price which was in use at the time of the delivery. If the price is changed between delivery reporting and invoicing, this is also shown.

#### Price strategy
Only available for list type Check prices. The following options are available:
- According to order type (selected by default)
- According to customer price
- According to customer’s price list
- According to price list

#### Price list
If you have selected the alternative Price list in the setting above, you can here select which price list to use. If you choose to use a price list in foreign currency, you will also be able to select a rate type in the field below.

#### Price alternative for CM/CR
You can select what the CM The contribution margin (CM) is the difference between the standard price and the sales price./CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. should compare the sales price with. Can select among different types of prices:
- Standard price – With this alternative, manually entered standard price on the customer order row will primarily be loaded to the list. Secondarily, the current standard price will be loaded from the part register.
- Future standard price – With this alternative, the future standard price loaded from the part register will be used.
- Historical standard price – With this alternative, a manually entered standard price on the customer order row will primarily be used. Secondarily, the standard price from the delivery will be used.
- Comparative price – With this option, a manually entered comparative price from the customer order row or invoice basis, will primarily be loaded. Secondarily, the current comparative price of the part will be loaded. Which price is used as comparative price for the part is determined by the Comparative price system setting.
- Post-calculated mean price – With this alternative, the post-calculated mean price from the part register will be used.
- Price list – This alternative will activate the next field where you can select a price list.

#### Price list for CM/CR
If you have selected the alternative Price list in the setting above, you can here select which price list to use. If you choose to use a price list in foreign currency, you will also be able to select a rate type in the field below.

#### SO mark-up
This setting is available if any of the price alternatives called Standard price, Historical standard price, Material cost, or FIFO price at delivery has been selected. It determines if SO mark-up (storage overhead) should be added to the price of sold parts in the list.

#### Convert price each according to rate type
With this setting you determine if "price each" in foreign currency should be converted to the present exchange rate in the Currencies procedure. If the checkbox is not checked, the exchange rate saved on the record will be used instead. Which rate type to use is selected in the field below.

#### Rate type
The rate type you select here is used to convert "prices each" and price lists in foreign currency to the now applying exchange rate for the selected rate type. The default rate type is From customer/order type. You register rate types in the Currencies procedure.
This setting is only available if you have selected Sales price as Price alternative.

#### Show foreign currency
With this setting you determine if all values should be displayed in the foreign currency. If the setting is activated, you will see a total per currency at the bottom of the list (total value per currency code). For the total lists, CM and CR are not shown. Instead you will see Amount and Currency amount. The amount is displayed in the company currency and the currency amount is shown in the foreign currency.

#### Valuation time
With this setting you decide if the current value should be shown in a report as for today, or if a historical value for a passed date should be shown. The historical value can be based on the log date or actual date. If you select one of the historical values, the date field will become available where you enter the historical date in question. This way it is possible to see the value of what was not invoiced but has been taken away from the stock value, at a given point in time. This value can then be seen even though the invoice basis at the present time has been invoiced.
> Log date – The date when the delivery was reported. 
Actual date – The date the user entered that the reporting was made, for example when the user needed to make a posterior reporting of a delivery which physically took place the day before.
- Current value – With this option, the valuation time will be today. This is date (today) is selected by default and cannot be changed.
- Historical value (log date) – With this alternative, all deliveries (regardless of actual date) will be loaded to the list if they have a log date which corresponds to, or is earlier than, the entered date. The deliveries linked to invoices will not be loaded. Orders (status 8 and 9) that are delivered (log date) on the selected date or earlier, will be loaded if the invoices’ voucher date is later than the log date.
- Historical value (actual date) – With this alternative, all deliveries (regardless of log date) will be loaded to the list if they have an actual date which corresponds to or is earlier than the entered date. The deliveries linked to invoices will not be loaded. Orders (status 8 and 9) that are delivered (actual date) on the selected date or earlier, will be loaded if the invoices’ voucher date is later than the log date.

#### Default value when changing status
With this setting you can choose a default value when changing status of invoice basis, this alternative will then become the default one when you use the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) Change status button on the function menu. You can choose between the following alternatives Change status from For invoicing (1) to Pending (3), Change status from Pending (3) to For invoicing (1), or both. This setting makes it easier to update statuses for multiple invoice bases at the same time.
> To change the status on invoice basis, you first need to make the list Edit invoice header updateable using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_list.png) on the toolbar. You can then change the status either by using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) Change status button to update the status for all invoice bases in the list, or change the status manually on each individual invoice basis by clicking the buttons in the Status column.

#### Only show order rows with price differences
Only available for list type Check prices. If this setting is activated, only invoice basis rows where price each is different from the selected price for the part will be shown in the list.

#### Only show order rows with expired price
Only available for list type Check prices. Determines if the list will only show invoice basis rows for parts where the current price has expired. Meaning: Valid to date < Order date on the invoice basis row.
