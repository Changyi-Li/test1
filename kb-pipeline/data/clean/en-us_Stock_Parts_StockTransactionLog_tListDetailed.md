### The Detailed list
This list shows detailed information about stock transactions in the stock transaction log for the selected parts. The list can be grouped by log date, actual date, or part.

#### Log date
Here you see when transaction was made.

#### User
Here you see the user who created the transaction.

#### Actual date
Here you see when the operation was reported as finished. If it has not been reported as finished, the log date will be shown instead.

#### Order number
This column can display manufacturing order number, customer order number, purchase order number, or case number.

#### Return order number
In this column you see the return order number if the transaction is a return order for a purchase order.

#### Location
Here you see the location in which the transaction was made.

#### Type
In this column you see a symbol representing which type of location is concerned: Pick location![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Delivery.png), Pick location for work center![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridManufacturingGroupImage.png), or Arrival location![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Arrival.png). A location can be a combination of all three types.

#### Balance change
Here you see the balance change in the transaction.

#### Balance (after reporting)
Here you see the total balance for the warehouse in question after the transaction.
A move between locations will always create two transactions in the stock transaction log and it provides a temporary balance consisting of the current balance plus the moved quantity on the location to where the balance was moved. This is because Monitor ERP first has to move the balance to the new location before the balance is removed from the old location.

#### Location balance
Here you see the balance of the location.

#### Arrival reported price
Here you see the price from the purchase order. You only see arrival reported price for positive balance changes because the arrival reported price is used to calculate FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. value for the balance.
This means that a purchase can have a different arrival reported price compared to the stock value according to FIFO price.

#### Amount
The amount is calculated according to arrival reported price × quantity.

#### Selected price
Here you see the selected price for the part according to the setting called Load price from. If the part's Standard price is selected in the setting, the following applies: If the stock transaction is from an arrival reporting or receiving inspection of a configured purchase order row*, the purchase order row will have a calculated and a saved standard price from the configuration. In that case, the calculated and saved standard price from the purchase order row will be shown, not the price from the part register.
> * A configured purchase order row means a row which is linked to a configured part on a customer order row.

#### Value
In this column you see the value according to the selected price for both arrival and withdrawal in stock. The value is calculated as: Selected price x Balance change. Please note! A negative balance change results in a negative value.

#### Revision
Here you see the revision of the part.

#### Batch number
Here you see the batch number on the location (when using traceability for the part).

#### Serial number
Here you see the serial number on the location (when using traceability for the part).

#### Comment
Here you see any comments entered during the transaction in any of the following procedures: Stock count, Move stock balance, and Direct stock reporting.

#### Transaction type
Here you see what caused the transaction. For example, stock count or material withdrawal for manufacturing order.

#### Signing employee number
Here you see the operator who made the reporting. This is displayed if you use the Time recording module.

#### Cause code
Here you see the cause code from the direct stock reporting.

#### Cause code (name)
Here you see the cause code (name) from the direct stock reporting.

#### Customer order number
Here you see the customer order number for the transaction.

#### Customer number
Here you see the customer number for the transaction.

#### Customer name
Here you see the customer name for the transaction.

#### Supplier number
Here you see the supplier number for the transaction.

#### Supplier name
Here you see the supplier name for the transaction.
