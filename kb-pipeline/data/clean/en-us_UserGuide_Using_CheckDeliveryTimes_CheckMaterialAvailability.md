### Check of material availability

#### Purchased material
For purchased material, the CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. function checks if there will be a shortage within the lead time. Shortage is checked against definite shortage, not taking safety stock into consideration.
The CDT shows the earliest possible possible delivery date for the product without causing a problem with included material. If no shortage occurs during the lead time, it means the material is not critical for the delivery time.
If no shortage exists because there is already at least one purchase order that covers the requirement in time, the delivery date of that order is displayed in the results window. This applies regardless of whether the purchase order has been confirmed by the supplier or not.
An existing order is always awaited (even beyond the lead time) if doing so means that CDT does not have to place a new order.

#### Identifying critical material
The analysis of the material availability will result in one or several materials being critical regarding the delivery time if the difference between when the material is required and when you expect to have it available is greater than the difference on the operations (the analysis of [capacity availability](CheckCapacityAvailability.htm)).
If a material is critical for the delivery time, the CDT can suggest to change to an alternative supplier with a shorter lead time. If several alternative suppliers have the same lead time, the CDT will instead suggest the most inexpensive supplier.

#### Exception from the material analysis
Parts which are not stock updated or parts with the lot sizing rule No requirement calculation, are not included in the analysis of material availability.

#### Stock driven M-parts
Unlike purchased materials, the lead time specified for a part in the Part register cannot always be relied on for stock driven manufactured parts. CDT therefore checks if shortages occur within the lead time, or whether all shortages are far enough into the future that it is possible to draw from already registered orders, provided that refill/replenishment can be completed before the next requirement arises.
A requirement for a stock driven manufactured part can be covered by an existing manufacturing order. If you in the Net requirement calculationYou use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. have activated calculation of New finish, there is a date saved on each manufacturing order which shows when the order is expected to be finished, taking the remaining hours and available capacity as well as material requirement versus arrivals of purchased parts, into consideration.

#### Calculating throughput time for main part
When a stock driven manufactured part is the main part, the CDT will not use the part’s throughput time from the part register. A current throughput time will instead be calculated based on the actual capacity availability and material availability.
For example, a pre-calculated throughput time of three days will in reality be five days if the loading is high or if the material availability is limited.
The throughput time is calculated by CDT based on the greatest value of the order quantity and the requirement quantity, with today's date as initial date. The calculation is the same as the calculation you can make without an order, using only the part's order quantity as a basis (using the Run CDT button in the Part register procedure).

#### Requirement date for incorporated parts
The date the analysis in CDT is based on for included stock driven parts, is the requirement date based on the desired delivery date/finish date for the part one level up in the structure.

#### Coordinated processing
If coordinated processing is applied, the parts processed together will be included in the analysis together with all included/incorporated material and loading. This also applies even if there is only one of the these parts that you sell on a customer order.
The delivery date/finish date which is the latest in the analysis of the parts, will be the delivery date which applies for the part in the customer order.
