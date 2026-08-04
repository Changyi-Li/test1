### Delivery/Shipping
In this box you configure settings for delivery and shipping to the customer.
If you add one or multiple alternative delivery addresses for the customer, then you can for example select delivery days, transport time, place of terms of delivery, and customer number, shipping agents – per delivery address. On a new customer orders order, these settings will then be determined by the selected delivery address on the order.
If you have installed the option Warehouse you can also enter delivery days, transport time, and place of terms of delivery – per warehouse and the alternative delivery address default for the customer. The values entered in these settings will be saved on all warehouses for a new customer. If you change warehouse for the customer and select/enter other values in these settings, these values will only be saved for the warehouse in question and for the alternative delivery address which is default. You can enter another delivery address as default and select/enter other values in these settings – per warehouse for that address. On a customer order, these settings will then be determined by both the selected warehouse and the selected delivery address on the order.
The Delivery rules button
By clicking the button Delivery rules ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you access a window where you can choose to activate Apply delivery planning. Here you can also activate the setting Apply preliminary pick list. You can select which Partial delivery rule to use. Here you can also determine if the customer should have Additional split of pick list and delivery note and how this split should be made. Finally you can also choose if the customer should Apply comprehensive delivery note. Read more below about what these settings mean.
Apply delivery planning
If you activate Apply delivery planning on the customer, it means you can also use the following two settings. These settings will also be transferred to new customer orders you register for the customer.
If you have activated delivery planning on the customer, this will also be applied on new customer orders for the customer, if the order type also has Apply delivery planning activated in the Order types procedure.

#### Delivery horizon
In this field you see/enter a default Delivery horizon for the customer. This is entered in number of work days. The delivery horizon determines how far ahead in time the delivery planning should include, based on the delivery date on the customer order rows. If you enter e.g. 10, it means the delivery planning will include customer orders that are to be delivered during the next 10 work days. If you leave the field empty, then it is the general delivery horizon which have been entered using the system setting called Delivery horizon which will apply.

#### Create delivery note number when delivery planning
This means that a delivery note number becomes created when the pick list is created, via the list type Picking plan in the Delivery planning procedure.
In that procedure it is possible to analyze which order rows can be delivered within the delivery horizon. The delivery planning also considers how partial delivery is set on orders, see the explanation further down.
Apply preliminary pick list
With this setting you decide if Preliminary pick list should be applied for the customer. Preliminary pick lists are useful if you also want to create pick lists for parts with shortages (not ready for delivery). You can also use preliminary pick lists when the picking will take long time or be made in several steps. When printing a preliminary pick list, the status on the customer order is set to 4 (Picking is in progress). However, no check is made to make sure the balance is sufficient and the quantity on the order rows will not be cleared. Preliminary pick lists can be updated in the Customer list procedure, using the list type Standard and the presentation Delivery/Shipping.
If you have activated preliminary pick list for the customer, this will also be transferred to new customer orders you register for the customer, if the order type also has Apply delivery planning activated in the Order types procedure.
Partial delivery
You can always, regardless of whether the use of delivery planning procedure is activated or not, choose if partial deliveries should be allowed or not for customer orders to the customer. Partial delivery can be allowed for entire orders or per order row. The setting regarding Partial delivery will be transferred to new customer orders you register for the customer. Partial delivery can also be used when preliminary pick list is applied.
Explanation of the different alternatives in Partial delivery:
- Not allowed – With this alternative partial delivery is not allowed. That is, you must be able to deliver the entire order in full (i.e. the disposable balance covers the remaining quantity of all the rows) before delivery of the order is suggested. Order rows that can be delivered are given the status pending until the disposable balance will cover the remaining quantity of the last order row.
- Only allowed when deleting remaining – All order rows of the entire order must be possible to deliver in full. If the disposable balance does not cover the remaining quantity of all rows, the remaining quantity is allowed to be deleted to be able to deliver the order.
- Allowed on order – Partial delivery is allowed to do on order level, but not per row. This means that it not allowed to divide an order row in multiple deliveries. The disposable balance must cover the remaining quantity of an order row before delivery of the entire order row will be suggested. This alternative is selected by default when registering a new customer.
- Allowed on order per delivery date – partial delivery is allowed on order level, as long as the matching delivery dates on the rows are not split. Partial delivery per row is not allowed. This means that it not not allowed to split an order row or to split rows with the same delivery date into multiple deliveries. The disposable balance must cover the remaining quantity on an order row before delivery of the entire order row is suggested.
- Allowed on order row – Partial delivery is also allowed on order rows. It is possible to make partial deliveries per package. The disposable balance must cover a package size. The suggested quantity to deliver is always a multiple of the package size. If the disposable balance is less than a package size, the order row will be set to status pending.
Additional split of pick list and delivery note
This setting determines if and how pick list and delivery note to the customer should be split. Explanation of the different alternatives:
- No – No split is made.
- Yes, split per dock – (default) All parts on an order which should be sent to the same dock will be put on the same pick list and delivery note.
- Yes, split per dock and storage – (default) All parts on an order which should be sent to the same dock and storage will be put on the same pick list and delivery note.
Apply comprehensive delivery note
If comprehensive delivery notes are used, this means that several orders to the same customer can be delivered at the same time. All orders will then be assigned the same delivery note number.

#### Delivery days
Here you configure specific weekdays as delivery days, that is, when the delivery should be sent from us. If no days are selected, all the days of the week will be delivery days. If some days are selected as delivery days, this will affect the delivery date when registering orders.
The delivery reporting of customer orders validates against the delivery days entered for the customer and warns if you try to deliver on another day than the delivery days. For a quote, customer order and invoice, the delivery date on the row always refers to the week day when the delivery is sent from us, regardless of transport time.
If you change the suggested delivery date on an order, a validation will be made against the entered delivery days. A warning will be displayed if the delivery date is not a day you have entered as a delivery day.

#### Transport time
Here you enter the transport time in number of work days (only whole numbers). The transport time refers to the time it takes to transport the goods from the sender to the receiver. The transport time also affects the delivery date printed on the documents and the text printed as an explanation to the delivery date, according to the following:
- If a transport time has been entered, the customer order document will read "Del. date = Arrival at your warehouse (Trans. time: X work days)".
- If no transport time is entered, the customer order document will have the text "Del. date = Shipped from our warehouse".

#### Transport calendar
Under the Transport calendar button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) next to the Transport time Transport time is the number of work days that it takes to send a shipment from sender to a receiver. field, you can select a separate transport calendar for the customer. The calendars that can be selected are loaded from the Calendars. By default, the calendar that has been entered for the location in the Company information procedure will be used.
A transport calendar is useful for example in connection to general industrial holidays and other extended periods when the company is closed for deliveries.
Please note that the transport calendar is only used to calculate the “Delivery date incl. transport time” date, that is, the date when the delivery is estimated to reach the customer.
You can update Transport calendar for multiple customers at the same time in Customer list using the Standard list type and the Delivery/Shipping presentation.

#### Allowance too early/too late
Here you enter the allowance for deliveries made too early and too late in number of work days. The value is used when calculating our delivery reliability towards the customer. That is, how many days the delivery can differ (in number of days) and still be considered to be “on time”.

#### Destination
You only need to enter a destination if it is not the same as the city entered in the delivery address.

#### Transport distance
Here you enter the transport distance (in kilometers) which is used for sustainability calculations.

#### Place of terms of delivery
You only need to enter the place of terms of delivery if it is not the city entered in the delivery address. The place of terms of delivery indicates the place or city where the financial responsibility for the shipped goods will pass to another party. This information is printed on order documents when the setting Show place of terms of delivery has been activated in the Document settings procedure.

#### Delivery instructions
Here you can enter a delivery instruction, if needed. It will be included on customer orders, and also in shipments and on shipping documents if the customer order is the source of information in the Register shipment procedure.

#### Customer number, shipping agents
By clicking this button you access a table where you can enter the customer's customer number with the shipping agent and pallet registration number. In the table you will see all suppliers registered with the supplier role Shipping agent in the supplier register.
Customer number at the shipping agent is the goods address number (GAN) or customer number that is the freight payer to the shipping agent.
The customer’s customer number at shipping agent can be entered manually on customer order regardless of freight payer, and on purchase order if the freight payer is set to Other payer. You can by default include the Customer’s customer number at the shipping agent on order and invoice, if the following settings are configured in Monitor ERP:
- A supplier with the supplier role set to Shipping agent in the Supplier register procedure.
- The customer’s customer number at the shipping agent is entered for the shipping agent in question, when you click the Customer no., shipping agents button in the Customer register procedure
- The delivery method of the order is connected to the shipping agent in question. This is configured in the Terms procedure.
- The delivery term on the order has the correct freight payer. The default freight payer for a delivery term is configured in the Terms procedure.
- If the document setting called Show customer number at shipping agent has been activated for the documents in question – Order confirmation, Purchase order, Invoice, and Pro forma Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees., in the Document settings procedure – the customer number at shipping agent will also be printed on the these documents.

#### Pick instruction
Here you can enter a pick instruction on the customer. This instruction will be printed on pick lists of orders to the customer. By using the button to the right, you can also link external files to the instruction. These will then be printed automatically when the pick list is printed.

#### Cumulative quantity, start date
If cumulative reconciliation should be applied for delivery schedules to the customer, you should here enter the start date for the cumulative quantity. Start date for cumulative quantity can also be entered for the customer in a customer link in the Part register procedure. Such date will in that case override the date entered here.

#### Deviation model
The deviation model is used to analyze delivery schedules. You create deviation models in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Delivery schedules procedure. [Read more](../../DeliverySchedules/BasicDataDeliverySchedules/bDeviationModel.htm) on how deviation models are prioritized.

#### Deviation model definition
Here you can see the deviation model that you've selected.
