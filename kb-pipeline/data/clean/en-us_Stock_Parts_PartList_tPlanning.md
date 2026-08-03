### The Planning list
This list type displays the parts' planning information and planning settings. It is possible to make the list updateable so that you can modify all information items and settings for the parts.
If you make your own presentations for a list type, you can choose to have more or less columns in that presentation based on a gross list of columns. In that presentation you can choose to also add the following updateable columns: Administrator, CN code, and Country of origin.

#### Planning method
The planning method for a part can be Net requirement, Stock refill, or Physical.
- Net requirement – This means that a net requirement will be made for the part and this creates order suggestions to cover shortages if the balance falls below the safety stock. This might be shortages created by reservations from customer orders, manufacturing orders, manufacturing order suggestions, forecasts, etc.
- Stock refill – This alternative means that the part is planned based on a fixed reorder point in stock.
- Physical – This alternative means that you physically/manually check if purchase or manufacturing is needed for the part. This option is normally used for purchased parts which are "bucket parts", consumables, etc. It can also be used for manufactured parts, for example in a small company with uncomplicated manufacturing where they manufacture when they sell parts from stock.

#### Control method
If you have selected Net requirement as planning method, you can here select Order oriented or Stock driven as control method. If you have selected Stock refill as planning method, Stock driven will be selected. Below you can see the differences between the control methods. If you have selected Physical as planning method, this field will be empty. The control method is set based on the selected lot sizing rule.
- Order oriented – With this rule, the quantity to be manufactured or purchased is determined by the quantity required for existing customer orders and manufacturing orders. If there are no orders that create requirements, no manufacturing/purchase will be made.
- Stock driven – With this rule, the quantity to be manufactured or purchased is determined by the availability in stock, and the requirements from existing customer orders and manufacturing orders, plus order quantity and safety stock entered for the part. If it is a stock driven part it is still possible to select that a specific manufacturing order or purchase order can be created from a customer order row, but then without a link (see below).

#### Allow to create order
This setting is only available for manufactured parts that are stock driven. If this setting is activated, a manufacturing order can be created from a customer order even though the part is stock driven. The manufacturing order which is created from the customer order row is possible to change. The purpose of this can for example be if you already have a quantity of the part in stock, which makes it unnecessary to manufacture as many as you are about to sell. If this setting is activated, you can create a manufacturing order directly and not have to go via the requirement calculation.

#### Lot sizing rule
The lot sizing rule determines the suggested order quantity when shortage occurs.
- Lot-for-lot – the control method is set to Order oriented and the setting Allow to create order is deactivated. This lot sizing rule means that one order suggestion per day is generated where the quantity matches the quantity of the requirements/shortages. Structure explosion will take place. The part's balance and other purchases might be a supply. If you from the customer order row select to create a manufacturing order or purchase order, then a link will be created in the same way as when using the lot sizing rule Linked requirement.
- Linked requirement – the control method is set to Order oriented and the setting Allow to create order is deactivated. This lot sizing rule means that linked order suggestions are generated where the quantity matches the quantity of each requirement/shortage. Structure explosion will take place. Only the linked order will form a supply, that is, a customer order can only be delivered after its generated order has been reported as finished or arrival reported. When using this lot sizing rule the user will receive a warning in case the part already has a balance or orders, such as manufacturing orders or purchase orders, in the planning window. These balances and orders will not be considered as a supply, which makes it not suitable to use with linked requirement.
- Fixed order quantity – the control method is set to Stock driven and the setting Allow to create order is activated. This lot sizing rule means that order suggestions are generated based on the part’s order quantity.
- Period requirement – the control method is set to Stock driven and the setting Allow to create order is activated. This lot sizing rule means that a common/mutual order suggestion is generated for all shortages within the period.
- No requirement calculation – the planning method is set to Physical and the setting Control method is deactivated. The setting Lot sizing rule The lot sizing rule determines the suggested order quantity when a shortage occurs of a part. Lot sizing rules are used for parts for which requirement planing is performed. will also be deactivated This means that no requirement calculation will be made for the part.

#### Period length
The period length describes the planning horizon in work days which the requirement calculation will take into consideration. The period length column is available when the lot sizing rule is set to Period requirement.

#### Order quantity
The order quantity describes the normal order quantity (size) and is used as suggested quantity when the lot sizing rule is Fixed order quantity. The order quantity can be entered when the lot sizing rule is Linked requirement, but the requirement calculation will not take the order quantity into consideration. You can also calculate the order quantity in the Calculate order quantity procedure.
If the option Warehouse is installed in the system, the order quantity is also used as default value for the part in pre-calculations. This will take place only if no Calculated quantity has been entered.
If you have not installed the option Warehouse, the values for order quantity and calculated quantity are synchronized.

#### Minimum quantity
Here you enter the minimum quantity to be suggested. E.g. if the lot sizing rule is Period requirement and the shortage is less than the minimum quantity, the suggested quantity will be increased to reach the minimum quantity. The minimum quantity is not applied if the lot sizing rule is Linked requirement.

#### Rounding quantity
The rounding quantity is often used to describe a package size or a bar length. All suggestions are rounded up to a multiple of the rounding quantity. For example, if the shortage is 17 pieces and the rounding quantity if 5, then the suggested quantity will be 20 pieces. Rounding quantity is not applied if the lot sizing rule has been set to Linked requirement.

#### Reorder point
For parts with the planning method Stock refill, you can enter a reorder point for the part in question. The reorder point defines the balance at which it is time to place an order. The reorder point is not applied if the lot sizing rule has been set to Linked requirement.

#### Safety stock
What is entered here will be the definition of when a shortage occurs. Available balance Available balance is the current part balance on the locations minus the cleared quantity. less than the safety stock = shortage. The safety stock is not applied when the lot sizing rule has been set to Linked requirement.

#### Safety time
The safety time creates a gap (in number of work days) between the time of shortage and the suggested delivery date/finish date.

#### Maximum quantity
This column describes the maximum quantity of the part on a manufacturing order. If you create a manufacturing order and for example enter 12 as quantity of the part when the part has a maximum quantity of 5, then the manufacturing order will divide the quantity into two main part rows (nodes), each with 5 as quantity, and one main part row with 2 as quantity. The node number will also be displayed on the main part rows as well as on the manufacturing order documents. In the example mentioned above, these documents will be printed and called node 1/3, 2/3 and 3/3.

#### Lead time
You can enter a general Lead time Number of days between ordering date and delivery date. Normally used for purchased parts.. However, the lead time in the supplier links of the part will override it.

#### Forecast deduction
You can configure if forecast deduction should be made, and in that case when it should take place. The following options are available:
- None – With this option, the sales forecasts will not be deducted when customer order is registered. Also the forecasts will not be removed from the planning when the date of the forecast has passed.
- Present time – This option is suggested for parts with the lot sizing rule Period requirement and Fixed order quantity.
- Lead time – This option is suggested for parts with the lot sizing rule Lot-for-lot.

#### Deduction method
By selecting one of the following methods, you determine how sales forecasts should be deducted for the part:
- Percentage – This option configures that the deduction for the quantity on the customer order will be distributed evenly as a percentage from the sales forecasts that have an earlier date than the customer order.
- Chronological order – This option configures that the deduction for the quantity on the customer order will be made from the sales forecast with the oldest date, out of the forecasts that have an earlier date than the customer order
- Nearest – This option configures that the deduction for the quantity on the customer order will be made from the sales forecast with the date nearest after the customer order date.
- Nearest before – This option configures that the deduction for the quantity on the customer order will be made from the sales forecast with the nearest date before the customer order date.

#### Annual volume
The annual volume is the expected annual consumption registered for the part.

#### ABC code
Here you select which classification for the volume value to use. The ABC ABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc. codes are handled in the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part.

#### Refill from warehouse
Here you select if the part should be refilled internally from another warehouse. An empty field indicates that you manufacture the part yourself or buy it from a supplier.

#### Default transfer profile
This column is available if the option Customer order transfer is installed in your system. Here you can see if parts have a default transfer profile. This can be changed for the parts in the list. Transfer profiles are registered in the Transfer profiles procedure.
