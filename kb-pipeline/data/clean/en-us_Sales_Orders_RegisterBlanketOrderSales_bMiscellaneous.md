### Miscellaneous

#### Status
Here you see the status of the blanket order. The status of the order can be selected manually, but certain statuses are set automatically by the system at different events. You cannot manually select status 9. An order with status 9 can only be edited by first changing the status to 1, 2, or 5.
- 1) Registered – This is the default status for new blanket orders that you register.
- 2) Printed – This status is given when the customer order is printed and the printout has been approved. The order will also get a printout date, and a printout log will be created per document.
- 7) Called off in part – This status is given when calls have been made on one or several order rows. You can edit and add rows on blanket orders with status 7. You can also edit the calls.
- 8) Called off in full – This status is given when the entire order is called off. You can edit and add rows on blanket orders with status 8. You can also edit the calls.
- 9) Historical – Status 9 can only be manually set here or in the list type called Blanket order in the Order list – Sales procedure.

#### Warehouse
This field is available if the Warehouse option is installed. The suggested warehouse is the warehouse you are working in. However, you can change warehouse for the order in question.
The warehouse you select here will also be entered for the blanket order rows, unless the part on a blanket order row has a different warehouse selected by default. This is configured for parts by using the setting called Default warehouse on customer order in the Part register.
The warehouse on the blanket order determines in which warehouse the purchase order suggestions and manufacturing order suggestions should be created (when the Include in net requirement calculation setting has been activated).

#### Order date
The order date is set to today's date by default. You can modify the order date for the order in question.

#### Currency
For new orders, the currency shown is by default the currency registered for the customer, but it is possible to select another currency in this field.
For an existing order, you change currency by using the Change currency button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png). When you have selected another currency in the dialog box that appears, you will get a suggestion to Convert prices on the order rows to the new currency, but you can choose not to convert. You can also choose to Convert according to rate type if you want to convert the prices according to the current exchange rate. Otherwise, the prices are converted according to the rate on the order.
If an order is registered in a foreign currency (a currency other than the company currency), the current exchange rate will be used unless the Use forward rate setting has been activated. Current exchange rate is loaded from the Currencies procedure for the rate type configured for the customer in the Customer register procedure. If rate type has been set to be loaded from the order type, that rate type will be used instead.

#### Mailing address
By clicking the button Mailing address ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you see the customer's mailing address. When needed, you can change the address information for the specific blanket order.
