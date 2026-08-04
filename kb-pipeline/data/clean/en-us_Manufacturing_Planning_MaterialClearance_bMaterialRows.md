### Material rows
In this box you see a table with the material that belongs to the order selected in the Clearance status box.
The Function menu
With the Find button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search.png) (Ctrl + B) you can search in all columns in the table for the phrase you enter.
With the button Copy records to Clipboard ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy.png) you can copy records to Clipboard, for part node, part, material, or manufacturing order.
With the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can create a monitoring task for Balance – Part.
With the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) (Shift + F8) you can expand all material rows to see the batch number/serial number of each material, and to see in which locations the materials are, and you can enter quantity to clear. You can also expand individual material rows by using the arrow button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to the far left in the table.
With the button Show all parts ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_part_structure.png) you can decide if all parts should be shown.
With the button Show all tools ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_tools.png) you can decide if all tools should be shown.

#### Show
At the very top of the box you can with this setting decide if All material or if Only material with shortage should be shown in the box.

#### Cleared material (C)
If the material is cleared, you will see a C in this column.

#### Type
For traceable material, you will here see a symbol indicating the type of traceability of the material; batch ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/batch_image.png) or serial number ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/serialnumber_image.png). For locations you here see a symbol representing which type of location is concerned: pick location, pick location for work center, or arrival location.

#### Order number
In this column you can see the number of the manufacturing order the material belongs to. If there is a shortage of the material, the order number is displayed in red.

#### Project
If batch number is linked to a project, you will in this column see the project number.

#### Part node
Here you can see the part node in the order structure to which the material belongs.

#### For operation
Here you see the operation for which the material will be used.

#### B (Basic type)
Here you see the part's basic type. A tool is shown with a symbol and a tooltip.

#### Material's part number
This field shows the material's part number.

#### Name
Here you see the name of the material.

#### Cleared
In this column you see the quantity suggested to be cleared for the material. If you expand the row, you can per location change the suggested quantity to clear. The system suggests clearance according to age analysis of available locations. A validation is then made to make sure that the quantity entered is not greater than the dispsable balance per location. The total quantity must be the same as the material requirement. That is, you cannot clear parts of the material requirement or clear more material than what is disposable.

#### Reserved quantity
The top row shows the quantity which has already been cleared. On the following rows, the quantity is increased by the requirement stated on each row in order to take what is about to be cleared into consideration. This is used to see for how long the balance of the part will suffice.
Expired quantity of the material is also shown here.

#### Current balance
Here you see the current balanceCurrent balance is the part balance at this moment on the locations. of the material in the selected warehouse. You select warehouse in the toolbar of the procedure.

#### Available balance
In this column you see the available balanceAvailable balance is the current part balance on the locations minus the cleared quantity. of the material.

#### Material requirement
Here you see the material requirement for the order in question. It is the remaining material quantity of the order.

#### Disposable balance
Shows the disposable balance of the material, meaning the current stock balance in the warehouses that are allowed for the consuming work center, minus reservations. If there is a shortage of the material, the shortage is displayed as a negative value in red.

#### Alternative material
(This button is available when material shortage occur and there is a disposable balance for the alternative material.)
There is a checkbox you can use to mark the material you wish to change to. The following information is displayed about the alternative material:
- Part number
- Part name
- Current balanceCurrent balance is the part balance at this moment on the locations.
- Available balanceAvailable balance is the current part balance on the locations minus the cleared quantity.
- Material requirement
- Disposable balanceThe disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. after change of material
- Reserved
- Available balance within lead time
- Disposable balance within lead time – Check this balance to see if you can use the alternative material.
- Requirement date – Here you can see the date when the material requirement occurs.
> If you change to an alternative material, you need to redo the clearance and then save for the material to be updated on the manufacturing order.

#### Best-before date
If best-before date is applied for the material in the part register, this date will be shown here. If the date is today or in past time, the date will be displayed in red. The material is sorted according to the best-before date.

#### Charge number
Here you see the charge number from supplier, if any, which was entered when arrival reporting the material.
