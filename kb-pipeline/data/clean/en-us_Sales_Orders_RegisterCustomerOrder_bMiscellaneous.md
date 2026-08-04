### Miscellaneous
Here you find miscellaneous information about the customer order.

#### Credit limit
Here you can see the credit limit entered for the customer. The credit limit is displayed in the company currency. If the credit limit for the customer is already exceeded, you will see a warning when the customer is loaded on a new order. By using the button More information ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can see information about the quote backlog, order backlog, and credit situation of the customer.
With the system setting Handling of credit limit during order registration you can warn or block if the amount is exceeded when saving an order.

#### Status
The status of the order can be selected manually, but is it also set automatically by the system at different events/actions. It is possible to manually set status 9 on customer order. The remaining quantity on all rows will then be cancelled. Also, you cannot edit an order with status 9 (final delivery made). If you change status for a customer order, it also becomes possible to change the status of the order rows.
If the Customer order transfer option is used, the customer order's status will be transferred from the production company to the sales company's purchase order (if the sales company has a purchase order), and displays it on the order in the Supplier's order status field.
- 1) Registered – This is the default status for new orders that you register.
- 2) Printed – This status is given when the order confirmation is printed and the printout has been approved. The order will then also get a printout date, and a printout log will be created per document (confirmation and delivery note).
- 3) Delivery time cannot be confirmed – If the delivery period cannot be determined when registering the order, you can manually change to this status. If you can not decide the delivery period it might be that important information is missing in the planning window or when printing an order list.
- 4) Picking in progress – This status is given when the delivery note has been printed and approved, or when a pick list has been created for the order in the Delivery planning procedure. Price each, Discount, and Setup price can be edited on orders with this status.
- 5) Partial delivery made – This status is given when an order row has been fully or partially delivered (delivery reported).
- 9) Final delivery made – This status is given when all order rows have been delivery reported (that is, 0 in remaining quantity).

#### Preliminary
If you check the Preliminary checkbox, it means that the order will be marked with the text "Preliminary" across the order confirmation. A preliminary order exists in the order register and can be listed in the Order list – Sales procedure. It can be displayed in the planning window if you choose to show preliminary orders, but it is by default not included in the net requirement calculation. Also, a preliminary order cannot be delivered. Preliminary orders can be useful if you e.g. aim to continue working with an order later on and cannot finish it completely at the time of registration. In the procedure Order types you can decide if Preliminary customer order should be default for the order type.

#### Currency
For new orders, the currency shown is by default the currency registered for the customer, but it is possible to select another currency in this field.
For an existing order, you can change the currency by using the button Change currency ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png). When you have selected another currency in the dialog box that appears, you will get a suggestion to Convert prices on the order rows to the new currency, but you can choose not to convert. You can also choose to Convert according to rate type if you want to convert the prices according to the current exchange rate, otherwise the prices will be recalculated according to the exchange rate of the order. You can also activate the Use forward rate checkbox, and then you enter which forward rate to apply. Read more about forward rate below.
If an order is registered in a foreign currency (a currency other than the company currency), the current exchange rate will be used unless the Use forward rate setting has been activated. Current exchange rate is loaded from the Currencies procedure for the rate type configured for the customer in the Customer register procedure. If rate type has been set to be loaded from the order type, that rate type will be used instead. The exchange rate used for the order is displayed under the Currency field.

#### Use forward rate
This setting is only available if you have are registering a new order in a currency other than the company currency. After you have checked the checkbox, you can then enter the forward rate in the field. The exchange rate must be greater than zero (0.00). The use of forward rate can be activated by default by activating the Forward rate setting for the customer in the Customer register procedure. If forward rate is not activated, the exchange rate that applied to the currency at the time of registration (of the order) will be saved instead.

#### Order date
The order date is by default today's date, but it can be changed for the order in question. The date is configured by default as order date on the order rows. It is mandatory to enter a date.

#### Warehouse
This field is available if the Warehouse option is installed. The suggested warehouse is the warehouse you are working in. You can also change warehouse for the current order.
The warehouse you select here will also be entered for the customer order rows, unless the part on a customer order row has another warehouse selected by default. This is configured for parts by using the setting Default warehouse on customer order in the part register.
Some customer information is saved per warehouse and will be changed on the customer order if you change warehouse in this field. The information that is saved per warehouse is:
- Delivery terms
- Delivery method
- Delivery days
- Transport time Transport time is the number of work days that it takes to send a shipment from sender to a receiver.
- Place of terms of delivery

#### Transfer status
This field is available if the option Customer order transfer is installed. Here you can see the transfer status of the order. The different statuses are Not transferred, Partly transferred, and Fully transferred.
- Not transferred – This status means that no customer order row with a transfer profile has been transferred.
- Partly transferred – This status means than one or multiple – but not all – customer order rows with a transfer profile have been transferred.
- Fully transferred – This status means all customer order rows with a transfer profile has been transferred.

#### Multiple orders via e-mail
Determines whether multiple order confirmations should be attached to a single e-mail or whether each order confirmation should be sent in a separate e-mail. The default value is loaded from the Customer register.
