### Coordinated processing
Only applies to parts of the Manufactured type.
For manufactured parts, you can in this table add an unlimited number of other manufactured parts to be manufactured (coordinated) together with the part in question.
The purpose of coordinated processing is that parts that should/can be processed (manufactured) at the same time will also be ordered at the same time. If you for instance punch two different parts, part A and part B, at the same time from the same sheet-metal.
When using coordinated processing, the net requirement calculation will register orders for both part A and part B as soon as a shortage occur of one of them. If you register an order manually for part A, the system will automatically register an order for part B, too. Coordinated parts are kept together as several main parts on an order, and the same applies when replanning and deleting.
If you apply check of delivery times (CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.), that analysis will also take all coordinated processed parts into consideration, including material and loading for all parts. The delivery date/finish date which is the latest in the analysis of the parts, this date will be the date for the part in the order for which the CDT was run. [Read more about the check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) function under Using MONITOR on the start page of the online Help function.
If several parts that you have added to the table Coordinated processing appear on the same operation number and work center in the BOM and routing, a reporting batch will be created including the operations on a manufacturing order. All operations in the reporting batch are then automatically selected in the recording terminal when one of the included operations is selected by the operator. These operations have the same background color in the Include column in the priority plan in the recording terminal. This way the operator will see that these operations belong to the same reporting batch.

#### Part number
Here you enter the part number for the parts that should be coordinated. The name of the part will be displayed to the right. The first part added to the table will automatically become the part currently open in the procedure.

#### Quantity
The default quantity is 1,00 but you can enter any number with two decimals. The quantity shows the relation between part A and the other parts in the table, that is, the number of the respective part that will be processed at the same time as part A is being processed.
Example:
- If you want to process/manufacture 2 pieces of part B when you manufacture 1 piece of part A, then you should enter 2,00 for part B in the Quantity field (on the first row in the table).
- If you want to process/manufacture 15 pieces of part B when you manufacture 10 piece of part A, then you should enter 1,50 for part B in the Quantity field (on the second row in the table).
- If you enter 1,5 in Quantity and 3 should be manufactured of part A, an order of 4,5 pieces will be generated of part B (on the third row in the table). In this case you might get problems when registering orders. We recommended that you enter a relation that generates a whole number to avoid any problems.
| Quantity of part A | Quantity of part B | Manufactured quantity of part B |
|---|---|---|
| 1 | 2 | 2 |
| 10 | 1.5 | 15 |
| 3 | 1.5 | 4.5 |
