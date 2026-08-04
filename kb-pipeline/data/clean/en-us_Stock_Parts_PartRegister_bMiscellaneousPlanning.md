### Miscellaneous
Here you enter miscellaneous information about the part.

#### ABC code
Here you select which classification for the volume value to use. The ABCABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc. codes are handled in the procedure Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part.

#### Forecast deduction
You can configure if forecast deduction should be made, and in that case when it should take place. The following options are available:
- None – With this option, the sales forecasts will not be deducted when customer order is registered. Also the forecasts will not be removed from the planning when the date of the forecast has passed.
- Present time – This option is suggested for parts with the lot sizing rule Period requirement and Fixed order quantity.
- Lead timeNumber of days between ordering date and delivery date. Normally used for purchased parts. – This option is suggested for parts with the lot sizing rule Lot-for-lot.
When Present time or Lead time is applied, forecasts will no longer be included in the planning after the time in question has passed. If any of these alternatives has been selected, the field Deduction method will become available.
Sales forecasts are then registered in the Register sales forecasts procedure.

#### Deduction method
By selecting one of the following methods, you determine how sales forecasts should be deducted for the part:
- Percentage – With this option the deduction of the customer order's quantity will be distributed evenly as a percentage from the sales forecasts that are earlier than the customer order (that is, the forecasts' forecast dates are earlier than the delivery date of the customer order row).
- Chronological order – With this option the deduction of the customer order's quantity will be made from the oldest sales forecast. If the forecasts that have an earlier date than the customer order are not sufficient, the deduction will continue with the forecasts that have a later date than the customer order.
- Nearest – With this option the deduction of the customer order's quantity will be made from the sales forecast with the date nearest the customer order date (both before and after).
- Nearest before – With this option the deduction of the customer order's quantity will be made from the sales forecast with the date nearest before the customer order date, and then from the forecast with the second nearest date, etc.
- Periodic intervals – With this option the deduction of the customer order's quantity will be made from the sales forecast which is within the selected period interval. If this option has been selected, the fields Interval setting and Deduct from other part becomes available. In order for this deduction to be calculated you must activate Deduct forecast in the net requirement calculation in the Net requirement calculationYou use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. procedure. You configure how long the periodic intervals should be in the Basic data – Part procedure.
When there are multiple order rows on a customer order, deduction is made for each order row according to the same pattern for each deduction method. It is always the order row's delivery date and the forecast's forecast date which are referred to.

#### Interval setting
Here you select an interval setting for the deduction method called Periodic intervals. Interval settings should first be added under the Forecast deduction tab in the Basic data – Part procedure.

#### Deduct from other part
Here you can choose if deduction from the sales forecast should be made for the customer order's quantity from a different part. This is used if the sales forecast applies to multiple parts (e.g. different variants of a part) and not a specific separate part.

#### Refill from warehouse
This field is available if you have installed the option Warehouse. If the part primarily should be refilled from another warehouse and not be manufactured (if it is a manufactured part) or purchased from a material supplier (if it is a purchased part). Warehouses are registered in the Company information procedure.
If it is a manufactured part and you select to acquire/refill from a warehouse, the field Throughput timeThe throughput time is the time it takes to manufacture a part, from start of the first operation to finish of the last operation. In principle, it consists of production times, queuing times and setup times. will be renamed to Lead time (in the same way as for purchased parts). This is made since the manufactured part will generate stock order for purchase and be refilled from the warehouse and not from the manufacturing order.
If you leave this field empty, it means that you refill the part by manufacturing it or purchasing it from a material supplier.
If you apply linked requirement and supply planning and the part is refilled from warehouse, then no linked purchase order will be created from customer order row on the part.
If the part is requirement planned and refilled from another warehouse, a stock order suggestion will be created during shortage of the part. The suggestions are then released into actual stock orders for purchase. This applies to both manufactured parts and purchased parts.
The setting regarding refill from another warehouse applies to the part in the warehouse that has been selected on the toolbar of the procedure. This means that you cannot choose to refill from the same warehouse you are working in, that is, you cannot refill from yourself.
Example: In warehouse A you have configured that the part should be refilled from warehouse B. Then you cannot choose to refill from warehouse A (i.e. from itself). The field is empty in warehouse B which means that the part is manufactured or purchased in that warehouse.

#### Default transfer profile
This button is available if you use the Customer order transfer option. Here you can choose a default transfer profile for the part. This will be used for transfers between the sales company and the production company. This transfer profile will then be selected by default on new customer order rows containing the part. You can also decide, per transfer profile, whether a part can be transferred or not transferred.
If the Product configurator option is also used and the part is linked to a configuration group (is configured), a warning is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png), letting you know the configured part cannot be transferred (to the production company).
But the part can be configured in the production company. The part is then configured on the customer order row in the sales company by using the Remote configuration button which connects to the part's configuration in the production company. For this to be possible, the part must have Configuration activated in the supplier link in the sales company. This shows that the part has a configuration with the supplier in the production company.
