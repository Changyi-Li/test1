### Quantity/Time
Under this heading you report the quantity of parts, rejections, goods location (not for final operation), and you report setup time. For the final operation you report the transfer to stock, that is, the part is now finished and can be placed in a location (transfer to stock). You can also add new locations to which you can then report the transfer to stock.

#### Quantity to report
(This field is not available for the final operation) Here you enter the number of finished/approved parts that have been processed in the operation and that should be reported. There is a validation that will warn you if the reported quantity you enter here is larger than the remaining quantity.
If you first have made a positive reporting, it is allowed to report a negative quantity provided that the remaining will not be greater than the planned quantity. However, this does not apply if the operation is the final operation and/or has serial numbers.
If the operation has a measuring plan, a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is shown if a control measurement must be performed for the entered quantity you are to report. You can then open the Report measuring data procedure via the button called Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) to report the performed control measurement for the operation in question.
If the operation contains a maintenance form you can via the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) go to the Report maintenance procedure to report maintenance.
For the final operation this field is instead called Transfer to stock, see below.
Read more about [Rules for prioritizing locations at withdrawal to manufacturing order](../RulesLocationsWithdrawMorder.htm).

#### Transfer to stock
(This field is only available for the final operation) For the last operation you report the transfer to stock (the number of parts that is reported and will be transferred to stock). If you enter a negative quantity, this will be shown with a minus symbol in the Reported quantity on Transport label, manufacturing, transfer to stock. Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see the locations registered for the part.
You can select a location and add new locations. The selected location will be printed on the transport label for transfer to stock.
If you are using the Stock location system option, you can use Open putaway dialog ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StockBalance.png) to receive suggestions about which location the parts should be stored in.
If the part has traceability at batch level you will in the field called Batch A batch is the set of components/products manufactured at the same time and made from the same original material. see a suggested batch number, but you can change this number. How the batch number should be designed is decided in the Number series procedure.
If the setting Apply best-before date is activated in the part register, you must enter such a date in the field Best-before date. In the part register you can also configure if the best-before date should be suggested based on two different criteria.
If the part has traceability level Serial number A serial number is a number that is used for traceability for parts on entity level., serial numbers will be loaded when the manufacturing order is created. You must then choose (one serial number for each entity of the part) from these serial numbers on the location when you transfer to stock.
You can also enter charge number for the location and you can link a certificate file.

#### Remaining quantity
Here you can see the remaining number of parts that are left to report.

#### Quantity to reject
Under the Rejection list ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button you can add rows where you can enter rejected quantity and select rejection code per row. You can also enter comments regarding the rejection and link external files. You can report rejection for serial numbers. Rejections made, comments, and linked files can be seen in the manufacturing order log.

#### Previously rejected quantity
Here you can see the quantity that has already been rejected.

#### Time to report
Here you enter the total unit time of the quantity that is being reported.

#### Setup time
In this field you report the setup time separated from the unit time. If the work center has an own defined cost for setup time, it can be crucial to report the setup time separately. The setup time is also governed by the setting that determines the suggested planned time. The setup time, however, is only suggested when the operation is reported for the first time. Regardless of which quantity that you report, the entire setup time will be suggested here.

#### Goods location
(This field is not available for the final operation) Here you enter the goods location for the number of parts you are reporting. This is not done for the last operation. The goods location is printed on the transport label for manufacturing in progress and can be entered as a reference to where you physically placed the reported quantity. This is done to make it easier for operators in the following operation.

#### Goods location previous operation
Here you can see the goods location entered for the previous operation.

#### Planned quantity and Reported quantity
In these fields you can see the operation's planned quantity and its reported quantity.

#### Planned time for reported quantity
Here you can see the operation's planned total time (unit time and setup time together).

#### Reported time
In this field you can see how much time that has already been reported for the operation (unit time and setup time together.)
