### Planning settings
Here you enter planning settings for the part. These settings control the net requirement calculation and the requirement calculation of the part. The settings are displayed in the unit selected in the header row.

#### Annual volume, current pace
This field is only displayed if you have activated the system setting Show annual budget, annual volume, and order quantity with current pace. Current pace is mostly applied when seasonal consumption exists and the planning is made according to stock refill. This field defines the annual volume according to the current month’s pace. Under Value you will see: annual volume, current pace × standard price.

#### Daily pace, current pace
This field is connected to the field above. The annual volume, current pace is also used to get a value for Daily paceDaily pace is the consumption per day of a specific part., current pace as: annual volume ∕ days worked per year. Under Value you will see: daily pace, current pace × standard price.

#### Safety stock
Safety stock defines when a shortage occurs of a part. Disposable balanceThe disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. less than the safety stock is equal to shortage. You can calculate safety stock in different ways in the Calculate stock levels procedure. The safety stock is not applied when the lot sizing rule has been set to Linked requirement. The safety stock can be calculated in the Calculate stock levels procedure.

#### Reorder point
The reorder point defines the balance at which it is time to place an order for the part and it is used together with the planning method called Stock refill. You can calculate reorder point in the Calculate stock levels procedure. If the planning method is set to Stock refill, you can enter an optional reorder point.

#### Safety time
The safety time (in number of work days) creates a "gap" between the time of shortage and the suggested delivery date/finish date. Safety time is available as variable in one of the methods for calculating safety stock in the Planning formulas procedure.

#### Order quantity
The order quantity describes the normal order quantity (size) and is used as suggested quantity if the part has the lot sizing rule Fixed order quantity. You can also calculate order quantity in the Calculate order quantity procedure.
If the option Warehouse is installed in the system, the order quantity is also used as default value for the part in pre-calculations. This will take place only if no Calculated quantity has been entered.
In systems without the Warehouse option, the system setting Keep order quantity and calculated quantity in sync determines if values for the order quantity and calculated quantity should be kept in sync. Calculated quantity is shown under the Manufacturing tab in the Part register.
Order quantity is not used if the lot sizing rule is Linked requirement.

#### Minimum quantity
Here you enter the minimum quantity to be suggested. E.g. if the lot sizing rule is Period requirement and the shortage is less than the minimum quantity, the suggested quantity will be increased to reach the minimum quantity. The minimum quantity is not applied if the lot sizing rule is Linked requirement.

#### Rounding quantity
The rounding quantity is often used to describe a package size or a bar length. All suggestions are rounded up to a multiple of the rounding quantity. For example, if the shortage is 17 pieces and the rounding quantity if 5, then the suggested quantity will be 20 pieces. Rounding quantity is not applied if the lot sizing rule has been set to Linked requirement.

#### Period length
The period length describes the planning horizon in work days which the requirement calculation will take into consideration. The period length column is available when the lot sizing rule is set to Period requirement.

#### Maximum quantity on manufacturing order
The field called Maximum qty on M-order describes the maximum quantity of the part on a manufacturing order, without dividing the order into several main part rows (nodes). The default value is zero, then maximum quantity is not applied.
If you create a manufacturing order and for example enter 12 as quantity of the part when the part has a maximum quantity of 5, then the manufacturing order will be divided into two main part rows, each with 5 as quantity, and one main part row with 2 as quantity. The order will then have three main part rows which are numbered from 1 to 3. These main part rows or nodes are displayed in the box Structure when the order is registered.
There will also be three copies of the manufacturing order document in the example above, one for each main part row. The node number will be shown next to the order number as 1/3, 2/3, and 3/3 on each copy of the manufacturing order document.
If the part has traceability, the batch number will be suggested as follows: Batch numberA batch number is a number that is used for traceability for a set of or a batch of parts. A purchased material can have a batch number that should be able to be traced back to a certain charge number from a supplier. = Order number + NodeA node is an included/incorporated manufactured part on a certain level in a part structure. A level in the structure part can contain multiple nodes. The node on the highest level is called the main part (order). number.

#### Maximum quantity on purchase order
The field called Maximum quantity on purchase order describes the maximum quantity of the part that can be on a purchase order, without dividing the order into several main part rows (nodes). The default value is zero, then maximum quantity is not applied.
If maximum quantity on purchase order is applied and you create a purchase order manually, a warning is displayed if the ordered quantity is higher than the maximum order quantity.
Example A:
For supplier A
Part A has a maximum order quantity on purchase order set to 10 pcs. There’s a requirement to purchase 15 pcs. A purchase order suggestion of 15 pcs will be created, but when this suggestion is confirmed it will result in two purchase orders: one for 10 pcs and one for 5 pcs.
Example B:
For supplier B
Part B has a maximum order quantity on purchase order set to 20 pcs. There’s a requirement to purchase 40 pcs.
Part C has no maxium order quantity. There is a requirement to purchase 15 st.
Two purchase order suggestions will be created for 40 and 15 pcs respectively, but when these suggestions are confirmed it will result in two purchase orders.
One purchase order for 20 pcs of Part B and 15 pcs of Part C, and one purchase order for 20 pcs of Part B.
> Please note that Distributed purchase cannot be used together with maximum purchase order quantity, regardless of whether it’s in the Planning tab or the Supplier link.

#### Order quantity current pace
This field is only displayed if you have activated the system setting Show annual budget, annual volume, and order quantity with current pace. Current pace is mostly applied when seasonal consumption exists and the planning is made according to stock refill. This field then defines the order quantity according to the current month's pace.
