### Operations
This box displays the operations that are included in the selected part in the structure of the manufacturing order. Information about operations, that are loaded when a new order is saved, comes from the BOM and routing of the part in the order and from the work center.
You can add, insert, change and delete operations. It is only possible to add a new final operation if the existing final operation does not have a reported quantity. You cannot delete an operation that has reported time or reported quantity. All fields containing planned values can be edited.
A part in the structure must have at least one operation and/or one material.
If you add subcontracts, a purchase order will be created for each subcontract when you save the manufacturing order. You link the purchase order to the operation and you can, by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the row, open it in the Register purchase order procedure.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the function menu, you can go to related procedures for the marked operation row.

#### Status
In this column you see the status of each operation if the order has at least status 3 (Started).
The different status options for operations are:
| Symbol | Status | Description |
|---|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpStarted.png) | Started | Only time has been reported for the operation. |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPartiallyReported.png) | Partially reported | A quantity has been reported for the operation. |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) | Finished | The entire quantity has been reported for the operation. |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPartiallyShipped.png) | Partial delivery made | A partial delivery has been made on the purchase order for a subcontract. The status is shown on the order row in the procedure Report arrival. When a partial delivery has been made of the purchase order, the status of the subcontract will be shown as partially reported as described above. |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusDeliveredOpFullyShipped.png) | Final delivery made | Final delivery has been made on the purchase order for a subcontract. The status is shown on the order row in the procedure above. When a final delivery has been made of the purchase order, the status of the subcontract will be shown as finished as described above. |

#### Warehouse (WH)
Applies if you have installed the Warehouse option). If you change to another warehouse you will see the WH column. On the rows which belong to another warehouse than the selected warehouse you will see a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses_alt.png) in the column. A tooltip for the symbol informs you of which warehouse the row belongs to. Values and texts in all columns for these rows are displayed in italics.
In many of the procedures you can change the warehouse which you will be working in by using the Companies/Warehouses button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure. It is also possible to generally change in which warehouse to work. This is applied to all procedures.This is done in the desktop backstage.. In registration procedures for quotes, inquiries, different orders, and invoice bases, you can in a field select to which warehouse the record belongs.

#### Modification information (M)
If any of the information on the row has been manually modified, this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/modified_image.png) will be shown here. If anything on the row has been modified via Synchronize with BOM and routing, you will in this column see the following symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/sync_image.png).

#### Manufacturing order log
This Log column is displayed if the order has at least status 3 (Started). If reporting items exist on the operation, the button Manufacturing order log ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_log.png) will be shown . By clicking it you access information from the manufacturing order log.

#### Operation number
Here you see/enter the number of the operation. The operation numbers are by default set to 10, 20, 30, etc. However, these can be changed. You can also add new operation numbers. The rows will become sorted in numerical order when you save. It is not possible to insert an operation with a number higher than the existing final operation IF reporting items exist on that final operation. That is, you cannot add a new final operation, when transfer to stock has already taken place.

#### Work center
In this column you see/enter the number of the work center. You must enter one work center per row. By using the Change work center button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) on the function menu you can change the work center for an existing marked operation row.

#### Name
The name of the operation. The default name on a new order is loaded from the operation's name in the BOM and routing, but you can change the name for the order in question. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.
> If the operation's name differs from the name of the work center, the operation's name will not be changed if a user later on changes the work center for an operation in an order. The purpose of this is that it is possible to enter specific information for a certain operation via the name of the operation. That is why this information will not be removed if someone should change work center for the operation.

#### Planned start date and Planned finish date
For planned start date and planned finish date, the finish date of the previous operation is suggested. Planned start date of the final operation is calculated by using so-called "back planning", based on the Planned finish of the final operation. Planned finish for the final operation will be the finish date of the entire order.
The calculation for planned start date takes queue time, setup time, unit time, and overlap of the operations, into consideration. The parts' throughput times are also considered. If it is a subcontract, the system will also consider queue time and lead time for the subcontracting work center.
Planned start date is shown in red color if the date has already passed and the operation has not yet been started. Planned finish date is shown in red color if the date has already passed and there is a remaining quantity.

#### Divided time per date (Div.)
By clicking this button you can see the division of planned time per date. If you manually edit the number of days, a padlock ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png) is shown in the column and the lead time for the operations is locked. However, the block can be lifted if you edit the number of hours for the operation.

#### Actual finish date
The actual finish date is set when the operation is reported as finished. If the operation has been reported as finished (has 0 as remaining quantity), the field Actual finish date, will not be updated if more time or quantity is reported on the operation. If you replan the operation and a remaining quantity arises, then the field Actual finish date will become emptied. The date is then set again when the new remaining quantity is reported as finished.

#### Setup quantity
Here you enter the quantity of the part node in the operation which should be manufactured as, for example, "test run samples". Setup quantity can be used as an alternative to, or in combination with Extra % on the operation row.

#### Extra %
Here you see/enter a percentage for setup quantity or excess quantity.

#### Planned quantity
The planned quantity that is shown here consists of the quantity on the order + setup quantity + extra %.

#### Reported quantity
Here you can see the quantity that is reported for the operation.

#### Remaining quantity
Here you can see the quantity that is left to report for the operation.

#### Planned setup time
Here you can enter the planned setup time (in hours) for the quantity of the order. If you have entered a default setup time for the work center, it will be shown here but it can be changed.
If it is a part possible to configure that an order is being registered for, and if there is a quantity formula for setup time in the BOM and routing, then the result of the time formula will be used by default, but it can be changed.

#### Planned unit time
Here you will see the planned unit time (in hours) for the quantity of the order.
If it is a part possible to configure that an order is being registered for, and if there is a time formula for unit time, then the result of the time formula will be set by default, but it can be changed.

#### Total planned unit time
The total planned unit time is calculated as the quantity of the order multiplied by planned unit time.

#### Planned total time
This time consists of the total planned unit time + planned setup time.

#### Reported total time
Here you can see the total time that has been reported for the operation.

#### Instruction
By using this button you can enter an instruction for the operation. This instruction will be printed on the manufacturing order documents. The instruction can be edited in the Priority planning procedure.

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
If you activate the setting Automatic printout you get to select a printer to which the files should be printed together with the manufacturing order documents.

#### Measuring plan
By clicking Measuring plan button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can create a new measuring plan for the operation or modify an existing measuring plan. You create a measuring plan by adding one or multiple measuring templates with measuring forms containing measuring points and instructions. These must first be registered in the Measuring forms and Measuring templates procedures.
You can also, in the Measuring plan, link a work center to a row with a measuring template and measuring form. This means, reporting of measuring data on the operation for that row in the measuring plan can only be performed by the selected work center. If the field is empty, the row with measuring template and measuring form will always be used regardless of which work center that reports measuring data.
You report measuring data for the operation on the manufacturing in the Report measuring data procedure in connection with reporting quantity on the operation in any of the Report operation, Report manufacturing order, or Recording terminal procedures.
Already reported measuring data for the operation can be taken out subsequently in the Measuring data log procedure.

#### Report number
Here you can see the report number of the operation. It is created when you save a new order. You use the report number in the Report operations procedure. You can also use it in the Report manufacturing order and Undo reporting procedures. The report number contains information about the order, main part, and operation.

#### Supplier
If the row refers to a subcontracting work center, you will see the supplier number which was entered for the work center. It is also possible to change to another supplier in this field. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature, you can search for subcontract suppliers in the supplier register.

#### Delivery address
By clicking this button you will see which delivery address is used for this operation. If an alternative delivery address has been selected, this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info_have_data.png) is shown where you can see the alternative delivery address. For subcontracts the return address is loaded from the next/subsequent work center's warehouse. If the subcontract is the final operation, the following applies: If no other delivery address has been manually entered, the delivery address will be loaded from the warehouse where the manufacturing order was registered.

#### Purchase order
(Subcontract) Here you can see the purchase order number of the operation on an existing order. Purchase orders can be automatically created when registering manufacturing orders if the Create purchase order automatically setting is activated for the work center. One purchase order is created per operation.

#### Link to "Register purchase order" (L)
(Subcontract) On an existing order, you can open the Register purchase order procedure with the purchase order loaded by using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) button.

#### Supplier's part number
If the row refers to a subcontracting work center, you here see the supplier’s part number. This part number is also shown on the manufacturing order, purchase order row (subcontract), and delivery note row (subcontract).

#### Shipped quantity
(Subcontract) Here you can see the shipped quantity, that is, the quantity reported as sent to the supplier in the Subcontract document/Shipped procedure.

#### Quantity at subcontractor
(Subcontract) The quantity that currently exists at the subcontractor. It is the shipped quantity minus the arrival reported quantity. (The latter is reported in the Report arrival procedure in the Purchase module.)

#### Receiving inspection
(Subcontract) Here you can see the quantity that has been arrival reported and is waiting for receiving inspection.

#### Overlap in %
In this column you can enter an overlap time (OL) as a percentage. The definition to enter overlap is: quantity (%) left on this operation when the next operation should start. For example, if operations 10 and 20 should overlap each other, set the desired overlap time as a percentage for operation 10.

#### Queue time
Here you can see/enter the queue time for the operation. The queue time for an operation will override the queue time entered for the work center, displayed in the next field. If you leave this field empty, it is the queue time for the work center that will apply. Depending on whether you apply day planning or hourly planning, the queue time is entered in work days or hours.

#### Fixed lead time
The operation can have a fixed lead time. This is entered in number of workdays. If there is a value here, it means that it is loaded from the BOM and routing, but this can be changed on the order.
If you leave the field empty, a dynamic lead time calculation will be performed, but that lead time will not be displayed for operations on orders. The dynamic lead time is calculated using the operation time (setup time + quantity x unit time) in relation to the work center's capacity per day.

#### Number of machines/persons per order
Here you see the number of machines or persons per order which has been entered for the work center. This is possible to modify temporarily for the work center for this operation.

#### Cost factor setup and Cost factor unit
Here you see/enter cost factors for the operation. For setup time and/or unit time you can choose the regular cost factor or one of the exceptions for cost factors. These exceptions must be first registered for the work center.

#### Staffing factor setup and Staffing factor unit
Here you see/enter the staffing factor for the operation. For setup time and/or unit time you can enter a staffing factor in percent that will override the staffing factor for setup time and unit time registered for the work center.
By using the system setting Staffing affected costs you can select the cost factors linked to the staffing. That way, the staffing factor will affect both the loading and the calculation.
Staffing factor is not entered for subcontract.

#### Goods location
Here you can see the goods location for the parts. This can be entered when you report an operation which is not a final operation, since transfer to stock will then take place.

#### Time calculation, Show in priority plan, and Multiple operators
The values for these settings are loaded from the work center, but they can be changed for the order or in the Priority planning procedure. These three columns are only shown if you have the Time recording option.

#### Delegate
This column is only available if the module Time recording is installed in your system. By clicking the D button a window opens where you can delegate the operation to one or multiple employees by adding them in the table. With the setting Locked you can decide that no other than the employees to whom you delegated the operation, will be able to start the work item. The purpose of this is to dedicate the operation to one or several employees.
When the operation is delegated to an employee, the employee number will be shown on the button. If the operation is delegated to more than one employee, then the text Multiple will be shown on the button. A tooltip for the button displays the employee numbers and names in text.
This column is also available for operations in the Manufacturing order info, but there you can only see to whom an operation has been delegated.
An operation which is delegated, is always shown for the employees at the top of the priority plan in the recording terminal with a dark yellow background, regardless if the employee has selected a work center or a report number.

#### Actual start date
By clicking the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you find the Actual start date column. This date is automatically used when time or quantity is reported the first time in a reporting procedure (when the operation gets status Started). This date is also automatically entered if the operation (the work item) is started in the Recording terminal in the Time recording module. The date will not be removed if the reporting item is undone. However, the date can be changed or removed here on the operation row.
In the Status column you can manually change the status of an operation, for example, if it has been reported by mistake. However, for orders with status 6 or 9 you cannot edit the status.
