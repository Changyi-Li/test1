### Variable explanations
Here you find explanations to all variables available for planning formulas in Monitor ERP.
| Code | Name | Explanation |
|---|---|---|
| ADU | Daily pace Daily pace is the consumption per day of a specific part. | Calculated as AV / WDY and is saved under the Planning tab in the Part register procedure. |
| ADUD | Daily pace, current pace | Calculated as AVD / WDY and is saved under the Planning tab in the Part register procedure. |
| AV | Annual volume | Can be calculated in the Calculate annual volume procedure and be saved under the Planning tab in the Part register procedure. |
| AVAILQ | Available quantity within lead time | Calculated as BAL + ORQLT - MAX(RESLT, ADU x LT). |
| AVD | Annual volume, current pace | Can be calculated in the Calculate annual volume procedure and be saved under the Planning tab in the Part register procedure. |
| BAL | Balance | Current balance Current balance is the part balance at this moment on the locations. in total for all locations in the selected warehouse. |
| BS | Basic safety time | Safety time, entered under the Planning tab in the Part register procedure. |
| CLT | Calculated throughput time | Can be calculated in the Pre-calculation procedure and be saved under the Planning tab in the Part register procedure. |
| CLTM | Calculated throughput time incl. material | Can be calculated in the Pre-calculation procedure and be saved under the Planning tab in the Part register procedure. |
| CQ | Calculated order quantity | Calculated quantity, entered under the Manufacturing tab in the Part register procedure. |
| HC | Interest | Holding cost, can be entered when making calculations in the Calculate order quantity procedure. This is not saved anywhere. |
| LSR | Lot sizing rule The lot sizing rule determines the suggested order quantity when a shortage occurs of a part. Lot sizing rules are used for parts for which requirement planing is performed. | Entered under the Planning tab in the Part register procedure. |
| LT | Lead time Number of days between ordering date and delivery date. Normally used for purchased parts. | Lead time for purchased part and Throughput time The throughput time is the time it takes to manufacture a part, from start of the first operation to finish of the last operation. In principle, it consists of production times, queuing times and setup times. for manufactured part. Entered under the Planning tab in the Part register procedure. |
| MAXOQ | Maximum order quantity | Maximum quantity on manufacturing order, entered under the Planning tab in the Part register procedure. |
| MINOQ | Minimum order quantity | Minimum quantity, entered under the Planning tab in the Part register procedure. |
| MPQ | Rounding quantity | Entered under the Planning tab in the Part register procedure. |
| OC | Ordering cost | Ordering cost, manufacturing, Ordering cost, purchase, and Ordering cost, subcontract, can be entered when calculating in the Calculate order quantity procedure. This is not saved anywhere. |
| OQ | Order quantity | Calculated in the Calculate order quantity procedure and is saved under the Planning tab in the Part register procedure. |
| OQD | Order quantity current pace | Calculated in the Calculate order quantity procedure and is saved under the Planning tab in the Part register procedure. |
| ORQ | Quantity, actual orders | Added together under the Planning window tab in the Part register procedure. |
| ORQDE | Quantity, actual orders in past time | Added together under the Planning window tab in the Part register procedure. Applies to the orders where delivery date or finish date is in past time. |
| ORQLT | Quantity, actual orders within lead time | Added together under the Planning window tab in the Part register procedure. Applies to the orders where delivery date or finish date is in past time or within the part's lead time. |
| PF | Forecast error (uncertainties in consumption) | A constant which you update in the Planning formulas procedure. The default value of 0.60 is a value based on experience and it works well in most situations. |
| PIG | Control method | Entered under the Planning tab in the Part register procedure. |
| PM | Planning method | Entered under the Planning tab in the Part register procedure. |
| PQM | Quantity/package – Manufacturing | Entered under the Manufacturing tab in the Part register procedure. |
| PQP | Quantity/package – Purchase | Entered under the Purchase tab in the Part register procedure. |
| PS | Part status | Entered under the General tab in the Part register procedure. |
| QI | Receiving inspection | Entered under the Purchase tab in the Part register procedure. |
| RES | Reservations | Added together under the Planning window tab in the Part register procedure. |
| RESDE | Reservations in past time | Added together under the Planning window tab in the Part register procedure. Applies to the orders where delivery date or finish date is in past time. |
| RESLT | Reservations within lead time | Added together under the Planning window tab in the Part register procedure. Applies to the orders where delivery date or finish date is in past time or within the part's lead time. |
| ROP | Reorder point | Calculated in the Calculate stock levels procedure and is saved under the Planning tab in the Part register procedure. |
| SS | Safety stock | Calculated in the Calculate stock levels procedure and is saved under the Planning tab in the Part register procedure. |
| ST | Safety time | Entered under the Planning tab in the Part register procedure. |
| STD | Standard price | Calculated in the Pre-calculation or Post-calculation procedures and is saved under the General tab in the Part register procedure. |
| TRT | Transport time Transport time is the number of work days that it takes to send a shipment from sender to a receiver., supplier | Entered in the Supplier register procedure and is loaded via a supplier link for the part. |
| WDY | Number of work days per year | Entered under the Stock tab in the System settings procedure. |
| Z | Factor standard deviation (service level) | A constant which you update in the Planning formulas procedure. The default value of 2.33 is a value based on experience and it works well in most situations. |
