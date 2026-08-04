### Material
This box displays the materials included in the selected part in the structure of the manufacturing order. The information about material, that is loaded when a new order is saved, comes from the BOM and routing of the part in the order and from the part register.
You can add, insert, change and delete material. You cannot delete material that has a reported quantity.
You cannot change to a fictitious or order orientated part on an existing material row.
If you add a manufactured part, it will be managed as a material row and will not be exploded.
All fields containing planned values can be edited.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the function menu, you can go to related procedures for the marked material row.
On the function menu you also find the Copy records to Clipboard button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy.png). This can be used to copy all material in the box to a part clipboard (part selection) for further processing in other procedures.
By clicking the button Disconnect purchase order row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) you can, when needed, delete the link to the purchase order row for the material if the purchase order has been generated from this manufacturing order. What happens when you disconnect the purchase order is that it becomes available for other requirements and that clearances for the purchase order row, if any, will be deleted. It is only possible to disconnect a purchase order row if the purchased part has the lot sizing rule Lot-for-lot.
If alternative materials are used, these are the only ones shown in the material row’s LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature.. Other materials are not displayed in the Lookup feature in this field. To change to an non-alternative part, you must instead use the Change material button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) on the function menu. You can enter alternative materials in the BOM and routing or Part register procedures. Alternative materials entered in the BOM and routing overrides any alternativ material entered in the Part register.
A part in the structure must have at least one material and/or one operation.

#### Modification information (M)
If any of the information on the row has been manually modified, a pen symbol will be shown in this column. If anything on the row has been modified via Synchronize with BOM and routing, you will in this column see a symbol of a rotating arrow.

#### Warehouse (WH)
Applies if you have installed the Warehouse option). If you change to another warehouse you will see the WH column. On the rows which belong to another warehouse than the selected warehouse you will see a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses_alt.png) in the column. A tooltip for the symbol informs you of which warehouse the row belongs to. Values and texts in all columns for these rows are displayed in italics.
In many of the procedures you can change the warehouse which you will be working in by using the Companies/Warehouses button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure. It is also possible to generally change in which warehouse to work. This is applied to all procedures.This is done in the desktop backstage.. In registration procedures for quotes, inquiries, different orders, and invoice bases, you can in a field select to which warehouse the record belongs.

#### Basic type (B)
In this column you can see a symbol representing the basic type of the material. The basic type is loaded from the part template which the material is linked to in the part register. A tooltip is shown when you hover over the symbol, displaying the basic type in text.

#### Manufacturing order log
This Log column is displayed if the order has at least status 3 (Started). If reporting items exist on the material, the button Manufacturing order log ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_log.png) will be shown. By clicking it you access information from the manufacturing order log.

#### Position
Here you see the position of the material in the operation.

#### Part
The part number of the material. You can delete a material row or change part on the row, as long as no reporting has taken place for the material row. When reporting has taken place the row becomes locked and it cannot be deleted and you cannot change the part. Next to the field you see the name of the part.

#### Part type
Here you see the type of the part.

#### Lot sizing rule
This field shows the material's lot sizing rule.

#### For operation
The operation in which the material is used. The operation number 10 is suggested in this field.

#### Setup quantity
The quantity of the material that is needed, e.g., for setup and wastage.
If it is a part possible to configure that an order is being registered for, and if there is a setup quantity formula for included material, then the setup quantity will be set by default, but it can be changed.
For tools, setup quantity is used instead of the regular quantity.

#### Extra %
Here you can enter a percentage for overflow of quantity. This can be used if it is more convenient to add a percentage rather than a fixed overflow.

#### Quantity per unit
The quantity that applies per unit.

#### Weight calculation (WC)
By clicking the Weight calculation button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) you can for this order see and edit the weight calculation which is loaded from the material row in the BOM and routing. You can also create a new weight calculation if such is missing on the material row. If there is a weight calculation registered for the part in the Part register, this will be shown by default if you add a material row with the part on the order. Read more about [weight calculation](../../Parts/BOMAndRouting/bMaterials.htm#Viktberäkning_(VB)) on material rows.

#### Planned quantity
The planned quantity is: the quantity on the order × quantity per unit + setup quantity + extra %.
If it is a part possible to configure that an order is being registered for, and if there is a quantity formula for included material, then the quantity will be set by default, but it can be changed.
If you modify the planned quantity the value is automatically calculated and changed in the Quantity per unit field.

#### Reported quantity
The quantity of the material which has been reported.

#### Remaining quantity
Here you can see the quantity that is left to report for the material.

#### Instruction
Here you can enter an instruction for the material in question. This instruction will be printed on the manufacturing order documents.

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
Here you can select if documents should be automatically printed together with the manufacturing order documents.

#### Material's revision
Here you can see the revision of the material.

#### Balance
Here you can see the current balance of the material on all locations.

#### Cleared quantity
Here you can see the material quantity that has been cleared in the Material clearance procedure. If the purchase order is linked to the manufacturing order, the material row will automatically be cleared with the quantity that is delivery reported

#### Rejected quantity
The quantity of the material which was rejected when reporting.

#### Reservation date
Shows the date when the material was reserved for the manufacturing order in question.

#### Report number
Here you can see the report number of the operation. It is created when you save a new order. You use the report number in the Report material procedure. The report number contains information about the order, the main part, and the material.

#### Traceability
This column is available if a material is traceable. In the column you see a symbol for the traceability level: Serial numberA serial number is a number that is used for traceability for parts on entity level. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/serialnumber_image.png) or BatchA batch is the set of components/products manufactured at the same time and made from the same original material. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/batch_image.png). A tooltip is shown when you hover over the symbol, displaying an explanation.

#### Purchase order
This column is shown if there is a linked purchase order row to the material of an existing manufacturing order. You will then see purchase order number and row position for the linked purchase order row here.

#### Change linked order
By using the Change linked order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can link a purchase order row to the material row at a later date as well. This is possible to do for order oriented parts as long long as the material on the row is not reported in full or as long as the order does not have status 9. You can, for example, link a purchase order row if the purchase order was created prior to the manufacturing order. You can also change an already linked order row for a different order row. In cases where quantity or date on the material row differs compared to the order row, a warning is displayed and you get the chance to replan the purchase order. When you link the order row or change a linked order row, the material will automatically be cleared. The clearance will also be deleted for material on an order row which you replace.

#### Link to "Register purchase order"
On an existing order, you can open the Register purchase order procedure with the purchase order loaded by using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) button.
