# Warehouse
The Warehouse option is useful if you have stock and manufacturing units located in different cities or if you have different stock types on separate premises. In this option, stock orders are used to move parts between different warehouses.

#### Warehouse
A warehouse is a physical storage facility which is administrated as a separate unit. It can be different units in separate buildings within the same premises, for example a raw material deposit, spare parts inventory, and finished stock. It can also be separate units located in different cities, for example regional and local distribution stock/warehouses.
If other operations also take place at the warehouse location (manufacturing etc.), then it is an operational unit. All warehouses belong to the same legal entity (the same company).
Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. is the same for all warehouses within a company, but certain basic data may belong to a specific warehouse, for example, planning settings and default supplier for a part.
Quotes, orders, and invoices can belong to one warehouse, while a customer order row can belong to a different warehouse. You can show data from multiple warehouses in lists.

#### Stock order
To be able to move parts between different warehouses, you can use stock orders for purchase and sales, respectively. These orders are always linked to each other. A stock order always has one sending and one receiving warehouse. Stock orders are then created for internal "customers" and "suppliers" linked to the warehouses.
Stock orders are created in separate procedures but they are handled in the same procedures as all other customer and purchase orders, for example, during delivery and arrival reporting, net requirement calculation, and when printing different lists.

#### Valuation
There is also a function used to valuate parts that are in transit (being transported) between warehouses. This can be used in cases with long transport times and great distances between the warehouses. During the transport, these parts are not registered on a location in any of the warehouses, and because of this the parts cannot be valuated in the regular procedure for stock valuation.

#### Automatic arrival reporting
If the transport times between the warehouses are very short, for example, when the warehouses are next door to each other on the same factory premises, it might be useful to apply the function Automatic arrival reporting. This means that as soon as a stock order (sales) is delivery reported in the sending warehouse, the procedure used to report arrival opens automatically. The same user can then arrival report the same quantity directly in the linked purchase order in the receiving warehouse. If you apply automatic arrival reporting, stock value between warehouses will not occur.

#### Example: Warehouse and one operational unit
This example shows one operational unit, with a warehouse at another location. The operational unit carries out purchasing, manufacturing, and sales. The warehouse only manages sales. The operational unit can deliver to the warehouse by using a stock order. A stock order is a separate order type in Monitor ERP used to move parts between different warehouses.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Warehouse1.png)](../../../Resources/Images/TrainingMaterial/Warehouse1.png)
For more examples, see the following [link](../Using/Warehouse/Warehouse.htm).
Interested in finding out more? Please contact our Sales department using this [form](https://www.monitorerp.com/sv/kontakt/). Want to find out more? Sign up to our upcoming [Monitor Demos](https://www.monitorerp.com/sv/kunskapsbank/effektivisera-med-monitor-erp/monitor-demos/) (Swedish).
