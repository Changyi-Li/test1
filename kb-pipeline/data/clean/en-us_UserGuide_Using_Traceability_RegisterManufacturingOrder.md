### Register manufacturing order

#### Traceability at serial number level
When a manufacturing order is created for parts with traceability level Serial numberA serial number is a number that is used for traceability for parts on entity level., the serial number will always be created and linked to the manufacturing order.
If a manufacturing order is created manually or via a manufacturing order suggestion (which is not linked to a customer order), this number will be loaded from a number series for serial numbers. This is found in the Number series procedure.
If the manufacturing order is created from a customer order, or from a customer order linked manufacturing order suggestion, where serial numbers have already been generated, these serial numbers are inherited from the customer order row for the manufacturing order. Otherwise, they are created from the number series.
If a structure order is created in which incorporated parts also have traceability with serial number, serial numbers are also created for these. Serial numbers are always linked to a part code (incorporated manufactured part) in the manufacturing order.
Under the Serial number tab in the Number series procedure, you can select how you want a serial number to be generated. In addition to regular number series, it is also possible to activate other prefixes or suffixes for serial numbers.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/SerialNumberManufacturingOrder.png)](../../../../Resources/Images/TrainingMaterial/SerialNumberManufacturingOrder.png)
On the manufacturing order document you can show the serial numbers. This is determined per document with the setting Show serial number in the procedure Document templates – Manufacturing order.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/SerialnumberManufacturingOrderDocument.png)](../../../../Resources/Images/TrainingMaterial/SerialnumberManufacturingOrderDocument.png)
