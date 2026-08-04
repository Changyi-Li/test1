# Terms and definitions
Here you find a list of common terms and definitions used in Monitor ERP.
A
-    
ABC
ABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc.
-    
Absence code
Absence code is used in order to be able to link causes to recorded absence. Salary types can be linked to absence codes and thereby the system can link the different types of absences to the correct salary type. Examples of some of the most common reasons for absence are illness, parental leave, leave of absence, late arrival, etc. Furthermore, absence codes can be linked to time balances so that the absence recording automatically reduces the balance for flex time, comp or makeup time.
-    
Aggregation
Aggregation is data that is totaled or combined, creating new data.
-    
Available balance
Available balance is the current part balance on the locations minus the cleared quantity.
B
-    
Balance accuracy
Balance accuracy is a metric that indicates the extent to which the recorded stock balance matches the actual physical quantity in stock.
-    
Balance sheet total
The balance sheet total is the sum of assets, or the sum of liabilities and equity, in the balance sheet.
-    
Basic data
With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc.
-    
Batch
A batch is the set of components/products manufactured at the same time and made from the same original material.
-    
Batch number
A batch number is a number that is used for traceability for a set of or a batch of parts. A purchased material can have a batch number that should be able to be traced back to a certain charge number from a supplier.
-    
Batch recording
Batch recording of the operations in the recording terminal means that several different operations can be started and finished at the same time, and that the reported time will be distributed evenly among them. The time calculation will distribute the time according to the planned time and quantity taken from the pre-calculation, as well as the reported quantity. Batch recording can for example be made in cutting operations, when several operations have the same raw material and also have short lead times. This is then used to avoid unnecessary work with the reporting.
C
-    
CDT
CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.
-    
Charge number
A charge number is used to provide traceability. It is the supplier's batch number, or charge number, which is linked to our batch number for a location.
-    
CM
The contribution margin (CM) is the difference between the standard price and the sales price.
-    
Cost center (CC)
A cost center can be a department, a branch of operation, work centers, areas of responsibility or similar to which costs are assigned.
-    
Cost factor
You enter cost factors for work centers and they are used to calculate the processing costs in pre-calculations.
-    
Cost unit (CU)
A cost unit could be, for example, a product group to which you assign a cost.
-    
CR
The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage.
-    
Current balance
Current balance is the part balance at this moment on the locations.
-    
Cycle time
Cycle time is the productive time in the operation in which the unproductive time is not included. Cycle time plus Ineffective time adds up to the unit time for an operation.
D
-    
Daily pace
Daily pace is the consumption per day of a specific part.
-    
Daily working hours
Daily working hours is the agreed working hours per 24 hours according to a schedule.
-    
Day planning
Day planning is used when you are NOT applying hourly planning. It means that all operations are planned to a date and not to a specific time on a date.
-    
Days of grace
The term days of grace (or grace period) is used at requirements planning in order to calculate rescheduling of actual orders that cover the requirement but that are too late in time, instead of suggesting a new order.
-    
Delivery schedule
Silf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands.
-    
Dimensions
Dimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up.
-    
Disposable balance
The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity.
E
-    
EDI
EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system.
-    
Efficiency factor (E-factor)
This is a measure of the outcome (result) between planned and actual time. Calculated according to the following: E= (Planned total time x Reported quantity/ Planned quantity ) / Reported total time.
-    
Entity
An entity is an individual part which is manufactured or purchased with a unique serial number for each entity.
-    
Excess quantity
Excess quantity is an extra quantity, for example for wastage when setting up a machine, that should be possible to take into considered when creating BOM and routing for a particular part.
F
-    
FIFO
FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit.
G
-    
Goods type
Goods type describes what kind of part it is, for example machine parts, electronics, etc. Goods type is printed on shipping documents.
H
-    
Hourly planning
Hourly planning refers to when planning per work center is done per hour. Hourly planning is activated with a system setting. Period is then entered as date and time. You can view loading on hour basis.
-    
Hyperlink
A hyperlink is an HTML element which you can click. Using hyperlinks you can link to/go to websites, e-mail addresses, or files.
I
-    
Ineffective time
Ineffective time is time which is necessary in the operation, but not directly productive.
-    
Intrastat
Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states.
L
-    
Lag
The term "lag" refers to the total sum of the planned setup time and unit time that has not yet been reported as finished for a planned finish period.
-    
Lead time
Number of days between ordering date and delivery date. Normally used for purchased parts.
-    
Lead time calculation
When registering manufacturing orders, the lead time is calculated for the order, provided that you have selected the loading model using lead time calculation. The lead time for the order – using start and finish dates – determines when the preparation and material requirements occur.
-    
Loading meters
The unit "loading meter" is used for parts that are difficult to stow or pack (e.g. cannot be packed on pallets). You enter the longest measure (in meters) of the space which the packaged part takes up when you stow it.
-    
Lookup
The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard.
-    
Lot sizing rule
The lot sizing rule determines the suggested order quantity when a shortage occurs of a part. Lot sizing rules are used for parts for which requirement planing is performed.
M
-    
Main location
Earlier called "Current location". Main location means the stock location for a part that has the most recent arrival date for the part. If you apply priority for the locations, then the main location is the location which has the highest priority (that is, the lowest number).
-    
Main part
"Main part" is the term used for the part in the top node (highest level) in a structure of parts.
-    
Management accounting
Management accounting is an option in Monitor ERP. It is used as a complement to the standard function called Stock accounting. The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5. The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor. Calculation differences are posted and these can be followed up per product, per order, etc. This function also contains extended management of cost of goods sold.
-    
Monitor-to-Monitor (M2M)
Monitor-to-Monitor is designed to facilitate the communication between customers and suppliers using Monitor ERP and/or Monitor G4. The function facilitates registration of e.g. purchase orders, order confirmations, and invoices.
N
-    
Net requirement calculation
You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts.
-    
Node
A node is an included/incorporated manufactured part on a certain level in a part structure. A level in the structure part can contain multiple nodes. The node on the highest level is called the main part (order).
O
-    
On account
On account is a partial payment (advance payment) which you have made to a supplier or received from a customer.
-    
Operating time
The term "Operating time" signifies the loading time that an operation needs to produce a certain number of products. That is the time shown as "loading" in a loading plan or schedule. If the work center is automated, this time is needed to manufacture the product, but does not require as many man-hours. By using a staffing factor, you can recalculate the difference between mechanical and staffed loading.
-    
Order suggestion
Order suggestions are suggestions made for manufacturing or purchase orders generated by the system in order to cover stock shortages of manufactured parts as well as purchased parts.
-    
Overlap
Overlap is abbreviated to OL, and is entered as a percentage. This allows two operations to overlap in time when a manufacturing order is created. Overlap is entered as a value that indicates how much of the current operation should remain when the next operation can begin. Any queue time on the subsequent operation means that overlap is ignored.
P
-    
Package type
Package type describes what kind of package that is used, such as "pallet" for EU pallets, "box" for cardboard boxes etc.
-    
Packing list
A packing list describes in which packages and using which types of packaging, the parts/products have been packed for delivery. The packaging list often contains information about package number and gross as well as net weight.
-    
PD
The price difference (PD) is calculated as purchase price minus standard price for purchased parts. Regarding subcontracts, PD is calculated as actual cost for subcontract (the price on the supplier invoice) minus planned cost for subcontract.
-    
Pick list
A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order.
-    
Planning settings
A number of different settings in the part register, such as reorder point and safety time. These settings function as information about the part and are used during requirement calculations in the system.
-    
Posting methods
Posting method is used to register how different types of transactions are posted to the correct accounts in the Stock or Management accounting.
-    
Pro forma
Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees.
-    
Profit mark-up
The profit mark-up is a percentage mark-up on the cost price which will generate a suggested quote price.
Q
-    
Queue time
Queue time refers to time which is added to create a gap between two operations when the manufacturing order is created. It is normally stated in days, where 1 means the rest of the commenced day will be the "gap". 2 means the rest of the commenced day plus 1 full day will be the gap. For work centers with hourly planning, the queue time is instead entered in hours. The entered queue time will be added before the operation which has a value entered.
-    
Quick reporting
Quick reporting means that the entire manufacturing order becomes reported as finished in one single step, including deletion of remaining quantity, if any.
S
-    
Salary type
Salary types are used to create salary bases for worked time and absence. Different salary types are used, for example, for work during regular working hours, flex, overtime, shorter working hours, and sick leave. The salary bases are used to manage salaries in a payroll system. Salary types are linked to absence codes in addition to work schedules and overtime schedules.
-    
Sales overhead
Sales OH is a percentage mark-up of the manufacturing cost that describes the overhead expenses in addition to the manufacturing itself. These are administrative costs and selling expenses. Manufacturing cost + Sales OH = Cost price (the limit where the company starts making money).
-    
SC (Subcontracting cost)
The SC is a percentage mark-up of the subcontract cost in order to cover all of the costs for the subcontract. Subcontract cost + SC together describe costs for purchase, freight, customs, handling, and stock-keeping.
-    
Serial number
A serial number is a number that is used for traceability for parts on entity level.
-    
SO (Storage overhead)
The SO mark-up is a percentage mark-up of the material cost in order to cover all the costs for the material. Material cost + SO together describe costs for purchase, freight, customs, handling, and stock-keeping.
-    
SRU
All accounts in the chart of accounts are linked to an SRU code. (SRU is an abbreviation of the Swedish term for standardized accounting statement.) The code is used to transfer information from the accounting to the accounting schedule in the tax return. Information regarding the SRU coding is exported in the chart of accounts information in the SIE file.
-    
Staggered price
Staggered price means the part has one price for one sales volume/purchase volume (quantity) and another price for another sales volume/purchase volume, etc. Staggered prices can also be called a "price ladder".
-    
Stock accounting
Stock accounting is a standard feature in Monitor ERP. It is used to continuously post all stock transactions in the system. This way the stock value in the Stock module matches the recorded value in the Accounting module. Changes in stock which are due to changed standard prices, direct stock reporting, arrivals and deliveries, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement.
-    
Stray customer
A customer which only makes an occasional purchase. "Stray customer" is a customer number that is used for different customers for one-time sales (non-recurring). Therefor these customers do not have to be registered in the customer register.
-    
Stray supplier
A supplier from which you rarely make any purchases. A stray supplier is registered with a supplier number used for one-time purchases from different physical suppliers that you therefore do not want to register in the supplier register. For suppliers marked as stray suppliers, you fill in all the fields on the order instead.
-    
Structure order
A structure order means that there in a manufacturing order are multiple parts as one batch which should be manufactured in a certain structure.
T
-    
Throughput time
The throughput time is the time it takes to manufacture a part, from start of the first operation to finish of the last operation. In principle, it consists of production times, queuing times and setup times.
-    
Time bank
Time banks are used in order to save recorded time outside scheduled working hours. Different time banks are for example used for comp time, makeup time, flex time (positive/negative), and shorter working hours.
-    
Time unit
Time units are units used to indicate the setup and unit times at BOM and routing. Normally, minutes or hours are used.
-    
Traceability
Traceability in Monitor ERP is all about being able to trace a specific serial number or a batch in each step it is being processed, as of when a part or a material arrives with you from a supplier. Traceability is also about stating what is withdrawn from and what is added to stock, so it is then possible to trace from customer order, via manufacturing order to purchase order. But it is also about being able to trace the other way around; from purchase order via manufacturing order to customer order.
-    
Transport time
Transport time is the number of work days that it takes to send a shipment from sender to a receiver.
W
-    
WIP (Work in progress)
WIP is short for "Work in Progress". WIP signifies the value of all the parts, including the added work and material, that are tied up in the manufacturing.
-    
Work center
A work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations.
