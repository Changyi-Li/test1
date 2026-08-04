### Miscellaneous

#### Confirmed
With this checkbox you can indicate that the supplier has confirmed the purchase order. This checkbox is checked automatically if you enter a registered or printed order as the supplier’s order number on the header row for a registered or a printed order, provided that the Confirm order when entering supplier's order number system setting has been set to "Yes".

#### Status
The status of the purchase orders can be selected manually, but different events will also cause the system to automatically assign a status. You cannot manually select status 0 or 9. You cannot change status on orders with status 0. An order with status 9 can only be edited by first changing the status to 1, 2, or 5.
- 0) Awaiting manual approval – This status is only used if you use approve purchase orders. This is determined by the system setting Approve purchase order. Status 0 is set on new orders whose total amount exceeds the user's authorization limit. Then you cannot print the order or send it via e-mail. No order rows can be arrival reported. When the order has been approved, it is given status 1.
- 1) Registered – This is the default status for new orders that you register.
- 2) Printed – This status is given when the order is printed and the printout has been approved. The order will also get a printout date, and a printout log will be created per document. The purchase order rows which are included in a delivery schedule will get status "Printed" in connection to the delivery schedule being printed, e-mailed, or sent via EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system..
- 5) Partial delivery made – This status is given when an order row has been fully or partially delivered (arrival reported).
- 8) Denied – This status is assigned when a purchase order has been sent for authorization/approval and the signer denied it. That is, did not approve the order. This status prevents the printing of a purchase order.
- 9) Final delivery made – This status is given when all order rows have been arrival reported (that is, 0 in remaining quantity).

#### Supplier's order status
This field is available if you have installed the Customer order transfer option. The field displays the status of the customer order in the production company. That is, the status of the customer order to which this purchase order in the sales company belongs.

#### Warehouse
If you have installed the option Warehouse, this field appears. The suggested warehouse is the warehouse you are working in. You can also change warehouse for the current order.
Some supplier information is saved per warehouse and can therefore be changed on the purchase order if you change warehouse in this field. The information that is saved per warehouse is: Delivery terms, Delivery method, Delivery days, Transport time Transport time is the number of work days that it takes to send a shipment from sender to a receiver., and Place of terms of delivery.

#### Quote number
The supplier’s quote number. This information is displayed on the purchase order document.

#### Order date
The order date is set to today's date by default. You can modify the order date for the order in question. The date entered here is then set by default as order date on the order rows.

#### Currency
For new orders, the currency shown is by default the currency registered for the suppliers, but it is possible to select another currency in this field.
If an order is registered in a foreign currency (a currency other than the company currency), the Current exchange rate will be used. Current exchange rate is loaded from the Currencies procedure for the rate type configured for the supplier in the Supplier register procedure. If rate type has been set to be loaded from the order type, that rate type will be used instead.
For an existing order, you can change the currency by using the button Change currency ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png). When you have selected another currency in the dialog box that appears, you will get a suggestion to Convert prices on the order rows to the new currency, but you can choose not to convert. You can also choose to Convert according to rate type if you want to convert the prices according to the current exchange rate. Otherwise, the prices are converted according to the rate on the order.

#### Multiple orders via e-mail
Determines whether multiple purchase orders should be attached to a single e-mail or whether each purchase order should be sent in a separate e-mail. The default value is loaded from the Supplier register.
