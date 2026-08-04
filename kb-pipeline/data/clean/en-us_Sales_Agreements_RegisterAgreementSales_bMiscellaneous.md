### Miscellaneous

#### Currency
For a new agreement, the currency shown is by default the currency registered for the customer, but it is possible to select another currency in this field.
For an existing agreement with status 1 – Negotiation, you can change currency by using the button called Change currency ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png). When you have selected a different Currency in the dialog box that appears, you will be suggested to Convert prices on the agreement rows, that is, to recalculate the amount to the new currency. You can, if needed, choose no to convert the prices. You can also choose to Convert according to rate type if you want to convert the prices according to the current exchange rate, otherwise the prices will be recalculated according to the exchange rate of the agreement. You can also activate the Use forward rate checkbox, and then you enter which forward rate to apply. Read more about forward rate below.
If an order is registered in a foreign currency (a currency other than the company currency), the current exchange rate will be used unless the Use forward rate setting has been activated. Current exchange rate is loaded from the Currencies procedure for the rate type configured for the customer in the Customer register procedure. If rate type has been set to be loaded from the order type, that rate type will be used instead. The exchange rate used for the order is displayed under the Currency field.

#### Use forward rate
This setting is only available if you have are registering a new order in a currency other than the company currency. After you have checked the checkbox, you can then enter the forward rate in the field. The exchange rate must be greater than zero (0.00). The use of forward rate can be activated by default by activating the Forward rate setting for the customer in the Customer register procedure. If forward rate is not activated, the exchange rate that applied to the currency at the time of registration (of the order) will be saved instead.

#### Serial number
Here you can enter a serial number for the agreement. This can be used, for example, if you have a leasing agreement for a machine. It is not mandatory to enter a serial number.

#### Priority
The priority is used to prioritize quotes, inquiries, orders, or projects. The default value here is 9. You can enter a digit between 1 and 9, where 1 is the highest priority. This field cannot be left empty.
