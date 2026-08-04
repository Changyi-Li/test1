### Delivery/Shipping
In this box you configure settings for delivery and shipping from the supplier.
If you have installed the option Warehouse you can also enter delivery days, transport time, and place of terms of delivery – per warehouse for the supplier. The values entered in these settings will be saved on all warehouses for a new supplier. If you change warehouse for the supplier and select/enter other values in these settings, these values will only be saved for the warehouse in question. On a purchase order, these settings are determined by the selected warehouse on the order.

#### Delivery days
Here you configure specific weekdays as delivery days when the delivery should arrive to our factory. If no days are selected, all the days of the week will be delivery days. If some days are selected as delivery days, this will affect the delivery date when registering orders.
For purchase orders, the delivery date suggested will be the date closest ahead in time that is a delivery date for the supplier. For inquiries and purchase orders, the delivery date on the row always refers to the week day when the delivery will arrive to the factory, regardless of transport time.
If you change the suggested delivery date on an order, a validation will be made against the entered delivery days. A warning will be displayed if the delivery date is not a day you have entered as a delivery day.
If you have activated the system setting called Use fixed delivery day on subcontracts, you can also enter delivery days for subcontracts.

#### Transport time
Here you enter the transport time in number of work days (only whole numbers). The transport time refers to the time it takes to transport the goods from the sender to the receiver. The transport time also affects the delivery date printed on the documents and the text printed as an explanation to the delivery date, according to the following:
- If a transport time has been entered, the purchase order document will read “Del. date = shipped from your warehouse (transport time: X work days)”.
- If no transport time is entered, the purchase order document will have the text “Del. date = arrival our warehouse”.

#### Allowance too early/too late
Here you enter the allowance for deliveries made too early and too late in number of work days. The value is used when calculating the supplier’s delivery reliability towards you. That is, how many days the delivery can differ (in number of days) and still be considered to be “on time”.

#### Destination
You only need to enter a destination if it is not the same as the city entered in the delivery address.

#### Transport distance
Here you enter the transport distance (in kilometers) which is used for sustainability calculations.

#### Place of terms of delivery
You only need to enter the place of terms of delivery if it is not the city entered in the delivery address. The "place of terms of delivery" describes the place or city where the financial responsibility for the shipped goods will pass to another party. This information is printed on order documents when the setting Show place of terms of delivery has been activated in the Document settings procedure.

#### Delivery instructions
A delivery instruction can also be entered, if needed. If "Supplier" has been selected as source of information in the Register shipment procedure, the delivery instruction will be included in the shipment and on shipping documents.

#### Customer number, shipping agents
By clicking this button you access a table where you can enter the supplier's customer number with the shipping agent and the pallet registration number. In the table you will see all suppliers registered with the supplier role Shipping agent in the supplier register.
Customer number at the shipping agent is the goods address number (GAN) or customer number that is the freight payer at the shipping agent.
The customer’s customer number at shipping agent can be entered manually on customer order regardless of freight payer, and on purchase order if the freight payer is set to Other payer. You can by default include the Customer’s customer number at the shipping agent on order and invoice, if the following settings are configured in Monitor ERP:
- A supplier with the supplier role set to Shipping agent in the Supplier register procedure.
- The customer’s customer number at the shipping agent is entered for the shipping agent in question, when you click the Customer no., shipping agents button in the Customer register procedure
- The delivery method of the order is connected to the shipping agent in question. This is configured in the Terms procedure.
- The delivery term on the order has the correct freight payer. The default freight payer for a delivery term is configured in the Terms procedure.
- If the document setting called Show customer number at shipping agent has been activated for the documents in question – Order confirmation, Purchase order, Invoice, and Pro forma Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees., in the Document settings procedure – the customer number at shipping agent will also be printed on the these documents.

#### Indicate lagging orders
The setting in this column determine if lagging purchase orders should be indicated in delivery schedules to the supplier. Lagging purchase orders are orders that you have not yet had delivered from the supplier, but which should have been delivered. The available alternatives are:
- Indicate lagging purchase order rows
- Do not indicate lag

#### Cumulative quantity, start date
Determines from which date the arrival reported quantity of different parts from the supplier should be added together separately per part. The date and the cumulative quantity are shown in delivery schedules to the supplier. The cumulative quantity's start date can also be entered in supplier links for parts. In that case, the date in the supplier link will override the date you have entered here.

#### Miscellaneous
By clicking this button you access settings that concern suppliers that have the supplier role of shipping agents. These settings will remain if you change the shipping agent in the Register shipment procedure.
- Automatic booking – With this checkbox you determine if automatic booking should be applied.
- Return label – With this checkbox you decide if a return label should be included. (Only available if the export plugin is nShift Delivery or Pacsoft.)
- Default shipping document printouts – Select which shipping document printouts should be selected by default: Both, Only waybill, or Only label.
-   
Earliest pick-up time – If you entered an earliest pick-up time for the shipping agent here, the corresponding field on the shipment will get the same time by default.
-   
Latest pick-up time – If you entered a latest pick-up time for the shipping agent here, the corresponding field on the shipment will get the same time by default.
-   
Text for the booking – If you entered a text for the booking for the shipping agent here, the corresponding field on the shipment will get the same text by default.
-   
E-mail address to goods sender – If you have entered an e-mail address here, the corresponding field on the shipment will get the same address as entered here.
-   
Show printer dialog – Waybill – Here you decide if the printer dialog should always be displayed when printing a waybill for nShift Web-TA.
-   
Show printer dialog – Transport label – Here you decide if the printer dialog should always be displayed when printing a transport label for nShift Web-TA.
-     
Use customs info – This setting is only available on suppliers that have the supplier role of Shipping agent.
The following options are available:
-   
Yes – With this option, the Use customs info checkbox will be activated by default in the Register shipment procedure when you use this supplier.
-   
No – With this option, the Use customs info checkbox is not checked by default in the Register shipment procedure when you use this supplier. This box is checked by default.
- Available customs documents – Here you can add and delete customs documents for nShift Delivery, nShift Web-TA, or Logtrade, using name and code for the document. These codes are loaded via the external partner, that is, nShift Delivery or Logtrade when you create the shipment to determine which documents should be created via nShift or Logtrade.
