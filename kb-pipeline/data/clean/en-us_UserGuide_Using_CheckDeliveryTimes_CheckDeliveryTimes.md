## Check delivery times
> [Read more](NewCalcModelCDT.htm) about how the new and improved check of delivery times works. This is available as of version 25.6.
The check delivery times (CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.) is a function in Monitor ERP which is mainly used to control and calculate the delivery date of a customer order. The CDT takes existing requirements and reservations into consideration, as well as available capacity and material. The check is made in connection with the order being created.
The purpose of CDT is to offer better master plans with reasonable delivery dates on customer orders and reasonable finish dates on manufacturing orders. However, it is optional to use the delivery dates and finish dates calculated by the CDT.

#### Prerequisites to use CDT
A prerequisite to be able to use the CDT is that:
- Stock balances and order quantities on parts are up-to-date.
- The parts have correct lot sizing rules.
The CDT takes the supplier's days off from work into consideration. If you have not entered calendars and calendar exceptions, if any, for the suppliers it might cause the delivery date on purchase orders (including subcontracts) to fall on days when the supplier is closed for business.

#### CDT on quote
You can run CDT on quotes, which then reserves capacity and material for the intended customer order.

#### CDT in customer order transfer
If you use the Customer order transfer option, you can also run CDT in remote company.

#### CDT in Register manufacturing order
In the Register manufacturing order procedure you can run CDT to check when an intended manufacturing order can be finished. This check does not include the requirement calculation which is made on the highest level for quote and customer order. This requirement calculation is not needed since manufacturing should always take place. On the other hand, requirement calculation is performed on material included/incorporated in the part.

#### CDT on part
You can run CDT on parts in order to check when a certain part can be delivered if an intended customer order were to be created for the part. Since there is no customer order with a quantity to use as a basis, the CDT is instead based on the order quantity of the part.

#### Alternate BOM and routing and CDT
If you use alternative BOM and routing, CDT also takes the terms customer, variant code, revision, part status, and order type into account, since these may affect the result on the customer order and quote. When using CDT from the part register the analysis is performed using the active part revision and today's date, and when applying alternative BOM and routing, the current status is also used.

#### System settings for CDT
To apply CDT you activate a main system setting and then use the following settings to select what CDT should check by default. These system settings will be accessible when you activate the main system setting. Read more about this in the [System settings for check delivery times](SystemSettings.htm) section.
When you register a new work center, the setting regarding if it should be included in CDT is activated by default. The default mode of this setting is determined by a system setting. Normally you only need to include the work centers that are "bottle necks" (for example different machines) in the CDT.
The setting Automatically run analysis will make the CDT run automatically on manufacturing order, customer order row, or quote row, in each of those registration procedures. This takes place when part number, quantity, and planned delivery date/finish date, is entered or modified. The CDT will then also run when you save an order or a quote in each registration procedure. It might be the case, that a balance has been changed by another user during the time you have been working on the quote or order. In this case a warning will be displayed when you save, and it is then possible for you to accept the new delivery date in which the balance change resulted. You can also run CDT on multiple customer orders at a time in the Order list – Sales procedure. In the Part register procedure you can then run CDT on part. There you run the CDT manually by clicking the button Run CDT on the toolbar. Then the CDT is only run on the part's order quantity, since there is no quantity on order or delivery date to be used as basis.

#### Coordination and Net requirement calculation
To prevent two sales representatives from committing the same capacity or using the same incorporated/included materials, you should use net requirement calculation, which can be scheduled to run at regular intervals.
This is particularly important when manufacturing orders are not created immediately after you saved/created the customer order.

#### What the CDT checks and calculates
1. It checks if the planned date is reasonable. The result can either be positive or negative. The answer depends on the result of the calculation in item 2. For example: "Can we deliver 10 pieces of part A on May 14?" The answer can either be yes or no.
2. Make a calculation of the earliest possible time on which the part and quantity can be produced based on the standard BOM and routing. "10 pieces of part A can be delivered on May 5 at the earliest".
3. Make a calculation of the earliest possible time on which the part and quantity can be produced, but where some replanning is required to achieve that result. It might be that an operation should be run in a different machine which has less loading, or that an alternative supplier with shorter lead times is suggested. "10 pieces of part A can be delivered on May 3 at the earliest if operation 20 is run in work center 110 instead of in work center 230". The result of this calculation is only shown in the [result window](ResultFromCDT.htm) which can be opened when you register order/quote. The suggested replanning will not be applied until you accept it.

#### Result, critical point for the order, and follow-up
The calculation results in earliest delivery date/finish date "when we can deliver". This is not the same as when the customer can have the parts at their location (transport time should be added and fixed delivery days might make a difference).
In addition to receiving different dates as result, you can also in the result window see a more detailed view which the calculation has created. It shows availability of the different operations and the material, and the differences compared to the planned date. Each calculation finds a critical point for the order, that is, a maximum difference (between planned delivery date and earliest possible delivery date according to CDT) for either operation or for material, which determines what the earliest delivery date/finish date will be. This date can then be used as a planned delivery date on the customer order or quote, or the finish date on the manufacturing order.
If you cannot deliver within the planned time (that is, if the CDT results in a difference), then it is either an operation or a material which is most critical (has the maximum difference). This is called critical point for the order, and it is here you should first try to take action to, if possible, shorten the delivery time.
When you register a quote or a customer order, the CDT function checks if delivery of the quantity can take place on the planned delivery date you entered. A requirement calculation is made. If there is no shortage, then you can deliver on the date you have entered. If there is a shortage you must refill the stock. This always apply for parts with the lot sizing rules Fixed order quantity, Period requirement, and Lot-for-lot. For parts with the lot sizing rule Linked requirement the situation is instead that the stock never has to be checked since manufacturing will take place regardless of the stock balance.
If the CDT finds that there is a shortage, an action will start where the CDT function checks when the part can be manufactured with the quantity which the part's lot sizing rule determines. This is based on available capacity and available material. Read more about this in the [Check of capacity availability](CheckCapacityAvailability.htm) and [Check of material availability](CheckMaterialAvailability.htm) topics.
Other info regarding the calculations
When there is a shortage of manufactured or purchased parts, you’ll receive suggestions for placing an order. Should the start date become today or the order date be today for these order, then the system setting Time when order day changes to next day will be applied. That is, if the CDT is run after that time of day, the start date and the order date will be tomorrow instead of today.
