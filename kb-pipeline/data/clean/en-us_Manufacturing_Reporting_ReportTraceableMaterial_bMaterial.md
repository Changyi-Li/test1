### Material
In this box you add one row for each batch/serial number from which you want to report a withdrawal.

#### Serial number/Batch
Here you can manually enter the serial number/batch number for the material which should be withdrawn from stock for the reporting or you can load it via a bar code scanner. This field is mandatory. Only serial numbers/batches which at present have material in stock, can be reported. If the part has been set to create serial numbers at withdrawal, then you do not use this procedure for reporting.
The serial numbers/batch numbers you see in the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature, are the ones which at the moment have material in stock.

#### Location
Here you see the location from which the batch number/serial number is taken. Material which belong to a serial number only exists in one location. That is why this field cannot be edited for rows with serial numbers. It only shows on which location the serial number exists.
For batch number it is possible to have material in multiple locations. If a batch number only exists in one location, then it works in the same way as for serial numbers. However, if the batch exists in multiple locations you must choose from which of the locations the stock withdrawal should be made. It is not possible to enter the reported quantity until the location has been selected. Then you can save the reporting.

#### Reported quantity
Here you can enter the quantity to report of the stock withdrawal from the batch. What is suggested here is the lowest of these two values: remaining quantity or batch's balance. A warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) will be displayed if the entered quantity to report is greater than the remaining quantity.
Example: remaining quantity is 13 and the balance of the entered batch is 100. In this case, 13 will be suggested to be reported as stock withdrawal. If the balance on the other hand is 10 in the example, then 10 will be suggested to be reported as stock withdrawal. Then it is expected of you to enter at least one batch for the remaining 3. This is done on the next row, where the suggested quantity follows the same logic.
You cannot enter a quantity greater than the available balance. You can report a negative quantity for parts with traceability set to batch, but only as much as what has previously been reported as withdrawn.
> This field is unavailable for serial numbers since it is always just 1 (one) you can report per row and serial number, but only until the remaining quantity is finished. After that it will be 0 as quantity for remaining rows you add with serial numbers.

#### Best-before date
If best-before date is applied for the material in the part register, this date will be shown here. If the date is today or in past time, the date will be displayed in red. The material is sorted according to the best-before date.

#### Disposable balance
Here you see the disposable balance per serial number/batch on the location.

#### Charge number
Here you see the charge number from supplier, if any, which was entered when arrival reporting the batch.
