### The Parts tab
This tab is used to register multiple parts for the same case. It is also used to enter additional information for these parts.

#### Default
Here you enter which part is the main part in the case. The information entered on this row is reflected in the other tabs in the case.

#### Part
Here you enter the part number of the product which the claim concerns. You can either enter it or manually select it, or it is automatically entered/completed if you start by selecting a serial number in the Serial number A serial number is a number that is used for traceability for parts on entity level. field. If the part has an active revision, this is automatically entered/completed in the Revision field.

#### Name
Here you see the part name.

#### Serial number/Batch
In this field you select the serial number for the product which the claim concerns, if the customer/supplier can specify it. A validation takes place against the customer/supplier and a warning is shown if the serial number is not linked to the customer/supplier in the case.

#### Revision
Here you can enter the part's revision which the cases concerns. The revision is set to the part's active revision when the part number is entered. You can select a different revision here if the customer has a claim regarding an earlier revision.

#### Cause code
Here you enter the cause code provided by the customer in the claim. Rejection codes are handled in the Rejection codes/Error codes procedure. Please find more information about Cause code etc. in the [Basic information](bBasicInformation.htm) topic.

#### Number of rejections
Here you enter the number of rejections that the case refers to. When the case is saved with a number of rejections and part number entered, you can by using the button next to the field go to the Direct stock reporting procedure and have the part number and quantity filled in for withdrawal. The link is only available if the system setting Affect balance for case is set to Yes.

#### Rejection description
In this field you can enter a rejection description and a translation of it. If the case type is set to Customer nonconformity, you can enter the customer’s rejection description. By clicking the button Insert phrase ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_phrase.png) it is possible to insert different phrases which are registered in the Phrases procedure. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about language management for translatable texts.

#### Batch number
Here you enter the part's batch number, if such exist for the part. It is also possible to enter a batch number that is not registered.

#### Customer order number – Replacement delivery
If the customer should receive a new delivery, you can either create a new customer order in the Register customer order procedure or link an existing customer order. Here you can create a link between a replacement order and the case. If you enter an order, the correct invoice will be automatically displayed. The field is only active if the case type is Customer nonconformity.

#### Invoice number – Replacement delivery
Create a link between an invoice number and the case. If you enter an invoice number, the correct customer order will be displayed automatically. The field is only active if the case type is Customer nonconformity.

#### Purchase order number – Replacement delivery
If the supplier should send a new delivery, you can either create a new purchase order or link an existing one. A link is automatically created between the case and the order.

#### Consecutive number – Replacement delivery
Here you enter the consecutive number of the supplier invoice. The field is only active if the case type is Supplier nonconformity.

#### Order number (Initial delivery)
Here you enter the order number of the initial delivery to which the part belongs. The number you enter is validated against the customer in the customer nonconformity.

#### Delivered quantity (Initial delivery)
Here you enter the quantity the initial arrival/delivery consisted of.

#### Delivery date (Initial delivery)
Enter the date when the initial delivery was made.

#### Invoice number (Initial delivery)
Enter the invoice number that the delivery was invoiced with.

#### Purchase order numbers (Initial delivery)
The order number for the initial arrival to which the part belongs. The number you enter is validated against the supplier in the supplier nonconformity.

#### Arrival reported quantity (Initial delivery)
Here you enter the quantity the initial arrival/delivery consisted of.

#### Delivery date (Initial delivery)
Enter the date when the initial delivery was made.

#### Consecutive number (Initial delivery)
Enter the consecutive number that the arrival’s invoice received.

#### Project (Initial delivery)
Here you enter the project to which the initial delivery belongs.

#### Manufacturing order (Initial manufacturing)
If the part is manufactured by you, you can link the manufacturing order information to the case. If the part is delivered to you, you can enter the manufacturing order of the initial manufacturing of the nonconformity part.

#### Operation (Initial manufacturing)
Here you can enter the operation number, if the nonconformity can be traced to a certain operation. The field becomes active when a manufacturing order has been selected.

#### Work center (Initial manufacturing)
Here you can enter the work center, if the nonconformity can be traced to a certain operation.

#### Manufactured quantity (Initial manufacturing)
Here you can enter the manufactured quantity where the initial production of the claimed part took place. This is a numerical field with two decimals. If the part number has been entered you will see the part's standard unit in the field. By default, here is no value in the field. The field becomes automatically filled in with the finished quantity of manufacturing order if it is finished.

#### Manufacturing date (Initial manufacturing)
Here you can enter the finish date when the initial production of the claimed part took place. This is empty by default. If there is a finish date from the manufacturing order, this is filled in automatically.

#### Purchase order (Initial purchase)
The order number for the initial arrival to which the part belongs. The number you enter is validated against the supplier. The field is only active if the case type is Customer nonconformity.

#### Arrival reported quantity (Initial purchase)
Here you enter the quantity the initial arrival consisted of. The field is only active if the case type is Customer nonconformity.

#### Delivery date (Initial purchase)
Enter the date when the initial arrival was made. The field is only active if the case type is Customer nonconformity.

#### Goods location (Return)
Goods location is available for the case type Customer nonconformity. You can enter a goods location in order to indicate where the returned parts have been placed. This is to avoid defect parts being registered in the stock balance.

#### Confirmed rejection
If you realize during the handling of the case that the rejection code or the number of rejections initially entered were not correct, you can change the information in this box. It might for example be a customer who has provided you with information about a certain error or a certain number of rejections. At a later stage, it might be discovered that the error depends on another reason or that the number of rejections was not correct. You can then enter the new information in this box and it will override the information provided initially.
If the rejection code and the number of rejections were correctly entered initially, this box does not need to be used to verify the error.

#### Cause of nonconformity
Here you can choose a rejection code as the cause of the nonconformity in cases when the cause can be linked to such a code.
Here you can also choose a supplier as the cause of the nonconformity in cases when the nonconformity can be linked to a supplier. It can be e.g. a subcontract, a transport damage, or a delivery of incorrect material.
Enter the material's part number if the cause origins from a faulty incorporated material in a manufactured part.
For customer nonconformity or internal nonconformity you can enter a work center or department if the cause can be tied to any of these parties.
You can also enter a cause description and link files.
