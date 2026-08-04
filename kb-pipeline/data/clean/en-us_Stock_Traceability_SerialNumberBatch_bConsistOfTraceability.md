### Consists of
In this box you can in different levels in a traceability structure, see which serial number or batch number that has been used and where it comes from. The top level in the traceability structure in the box is based on the serial number/batch number loaded in the record selector in the procedure.
Example: Serial numberA serial number is a number that is used for traceability for parts on entity level. 1000 is loaded in the procedure header. In the manufacturing report for manufacturing order 2500 (the order by which the serial number was created or linked to), the serial number 1001 and 1002 were consumed. These serial numbers are displayed as rows on an underlying level (sub-level). This explosion is displayed for all traceable materials which have been consumed in the manufacturing, for the serial number or the batch number loaded in the procedure.
By using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) button on the function menu you can load the marked serial number/batch number to the record selector of the procedure.
By using the Add serial number/batch button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) you can add a serial number/batch numb to have it included in the number on the marked row in the traceability structure. With this button you then get to select which serial number that should be added and as of which date and time this should start applying. An added row is also created for the serial number/batch number in the section called Consists of serial numbers/batches under the Manual level list tab. Please note! No stock withdrawal will take place for the part linked to the new number you add. It is only the serial number/batch number which is added in the traceability structure. The stock withdrawal is done as usual when a customer order containing the part is delivery reported.
By using the Remove serial no./batch no. button![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) you can delete the serial number/batch number of the marked row.
By using the Replace serial number/batch number button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can replace the marked serial number/batch number with a different one. This is useful, for example, for serial numbers that have already been delivered for a customer order, in cases where the serial number needs to be replaced because the part linked to that serial number is being replaced/exchanged. With this button you then get to select which serial number that should replace the marked serial number and as of which date and time this replacement should start applying. A replacement row is also created for the serial number/batch number in the section called Consists of serial numbers/batches under the Manual level list tab. Please note! Information about the replacing number is always found one level up from the replaced traceable material. Please note! No stock withdrawal is made of the part which is linked to the new number you are replacing with. It is only the serial number/batch number which is replaced in the traceability structure. The stock withdrawal is done as usual when a customer order containing the replacement part is delivery reported.
With the Refresh traceability structure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) you can update the traceability structure without having to reload the serial number/batch number in the procedure.
You also find a few standard buttons on the function menu. These can be used to expand/collapse rows, go to related procedures for the parts on the selected row, preview rows (for printout), copy records to Clipboard, and export the structure.

#### Type
The traceability type of the row is indicated with a symbol. For serial number ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/serialnumber_image.png) is shown, and for batch this symbol is displayed ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/batch_image.png).

#### Serial number/Batch number
Here you see the serial number or batch number in the traceability structure.

#### Part number
Here you see the part number linked to the serial number or batch number.

#### Name
Here you see/enter the name of the part.

#### Type (T)
Here you see the type of the part.

#### Order
Here you see the order number to which the serial number or batch belongs. The order number is here shown in red if it is a manufacturing order and in yellow if it is a purchase order and in green if it is a customer order.

#### Balance change
Here you see the balance change in the transaction.

#### Customer/Supplier
Displays the name and number of the customer or supplier.

#### Charge number
Displays the charge number for the serial number/batch.
