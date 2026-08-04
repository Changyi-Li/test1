### Order
In this box you see the manufacturing orders. By using the buttons on the function menu in the box, you can add new orders, delete existing orders, and save an existing order as a new order (operations and material will then be included). It is possible to modify different data on an order, for example quantity, start date, finish date, priority, customer, project, and variant code.

#### Order number
You can enter the order number manually for a new order, or you can leave the field empty in order to load the next available number from the number series for manufacturing orders when saving the order. If the manufacturing order is created from a customer order (when the part has the lot sizing rule Lot-for-lot or Linked requirement), the order number is filled in by default according to the system setting M-order number is created. It can be either From number series or As customer order number + position number. An order number can have a maximum of 20 characters.

#### Overload (O)
If the setting Check overload is activated when you register a new order by clicking on Save, and a work center has or will have an overload, you will see this column and a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) in it. A tooltop on the symbol displays a text stating that overload exists for one or several work centers in the order.

#### Replan underlying structure (R)
This setting is activated by default for an order. It means that the quantity and times will be replanned also for included parts in structure orders. This is the recommended way of working in order to keep the relation between the parts in the order. If you uncheck this setting, only the part in the structure that is being loaded for replanning will be replanned.

#### Order type
Here you see/select the order type for the manufacturing order. The order type that you have set as default in your user account, will be suggested. If you have not configured a default order type there, then the order type you used on the most recent order will be suggested. It is possible to select another order type, when needed. It is possible to change order type for an existing order.
The order types Stock driven and Customer order oriented are included when you install the system. For a manufacturing order which you register manually in this procedure, it is only possible to select Stock driven. The order type Customer order oriented is only used for manufacturing order which are created from customer order row. Other order types that you need must first be registered in the Order types procedure. The order type determines the priority of the manufacturing order and is a good selection term, for example, for setting up statistics.

#### Status
A symbol is shown for the status of the order. In a tooltip on the symbol you will see the number and the name of the status (1 – Registered, 2 – Printed, 3 – Started, 4 – Finished, 5 – Post-calculated, 6 – Delivered, or 9 – Historical). It is not the main part that is shown, it is the status of the order. This status is based on the following set of rules:
- 1 – All parts in the order structure have status 1.
- 2 – There is one or several parts with status 2, but the other parts have status 1.
- 3 – There is one or several parts with status 3, but the other parts have status 1-2.
- 4-9 – The main part has status 4-9.

#### Entire structure (E)
When you replan an existing order, you can uncheck the checkbox Entire structure (E) on the row for an order. This can be done if you do not wish to replan the entire structure order, but only wish to replan a particular part in the structure. When the E is not checked, you can select the part to replan under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) (Structure) which is then shown next to the Part field. The parts you can then select among are structure parts in different nodes in the order structure.

#### Part
Here you can see the part number of the part that you are going to manufacture in the manufacturing order. In order to register a manufacturing order, you only have to select a part number and enter the quantity. If you are replanning an existing order, it is possible to replan an individual part in the structure order if the E is not checked. Otherwise, the part number is not possible to edit.
The Name of the part is shown in the next column.

#### B/N (Block/Notify)
In the Block/Notify column you see if the part is blocked or if there is a message regarding registration of manufacturing order. It is possible to edit a manufacturing order containing blocked parts if the manufacturing order was created prior to when the part was blocked. However, you cannot add new rows with the blocked part.

#### More than one main part exist on the order
If there are multiple nodes with main parts in an order, you will here find the More than one main part exists on the order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/several_parts_on_m-order.png). By hovering the cursor over the button, you will see a tooltip about this. By clicking this button you access replanning of Start date and Finish date for each part node, and you can choose whether or not the underlying structure should also be replanned for each part node.
Cases where there are multiple part nodes on an order occur if the quantity on the order is greater than the part's maximum quantity on manufacturing orders. Another case when this occurs is when coordinated processing is applied on parts (part A and B are manufactured on the same order).

#### P-order (Create purchase order)
If the system setting Create purchase order when manufacturing order is created/edited has been set to Yes, optional or Yes, default, then you can in the P-order column choose to create a purchase order when you create the manufacturing order. If the system setting is set to Yes, default it means that this checkbox will be marked by default.
If the setting Create purchase order automatically is activated on the subcontract work center in the Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register procedure, a subcontract purchase order will be created automatically. One purchase order is created per operation.
The purpose of creating purchase order when you create the manufacturing order, is to quickly be able to create linked purchase order rows for material without waiting for net requirement calculation or performing a requirement calculation. When the manufacturing order is saved for the first time, a dialog box is shown containing the generated purchase order rows. If you then replan the manufacturing order's quantity, start date, or finish date, and this affects the linked purchase order row, then you can in a dialog box choose whether or not the linked purchase order row should be updated.
It is also possible to, at a later time, link or change an already created purchase order row for a material row on the manufacturing order. This is done by clicking the Change linked order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) on the material row.
More about purchase order from manufacturing order
Purchase order can be created for material on material on manufacturing order which have fulfilled the following criteria.
- The part is of the type Purchased.
- The part's lot sizing rule is Lot-for-lot or Linked requirement.
- The part has one or several Supplier links. Purchase order becomes created for the default supplier.
The purchase order will get the manufacturing order number as goods label if the system setting Update goods label on purchase order from manufacturing order is activated. If the purchase order rows have links to more than one manufacturing order, all of these manufacturing order numbers will be included in the goods label.
The quantity on the purchase order row will be the same as the quantity on the material row. Note, however, that if the part on the purchase order row has a partial quantity registered in the Part register, and that this partial quantity does not match the quantity of the material row, a validation error is shown and the purchase order is not created.
Price, discount and setup price, are loaded to the purchase order row in the regular way – from the supplier link and from discount matrix, if any. Delivery date on the purchase order row will be set to the material requirement date minus safety time on the part. Fixed delivery day for the supplier, and when the supplier is closed for business, are also taken into consideration. If the delivery date of the purchase falls in the supplier's day off (when the supplier is closed for business), the last day prior to the supplier's day off will be used as delivery date.
For example, if the requirement date is February 22, 2019, and the safety time is 1 day. Then the delivery date for the purchase order will be February 21, 2019 (a Thursday). If the fixed delivery date is set to Tuesday, the delivery date will be February 19, 2019. Revision number is set to the same as on the material row. The part number and the quantity field on the purchase order row are locked and cannot be edited. However, the part number can be replanned if you split the order row (see below under the heading "Replanning of linked purchase order"). The project number of the manufacturing order is saved to the purchase order row's project number (posting) in case the part has the setting Purchase on project activated. A link is created between the purchase order row and the material requirement on the manufacturing order, and the material's report number will be stated on the purchase order row. The manufacturing order number is also shown on the purchase order row and a link is created to the procedures Register manufacturing order and Manufacturing order info.
If the option Warehouse is used, the purchase order is created per manufacturing order, supplier, and warehouse. The purchase order is created in the warehouse in which the material requirement occurred on the manufacturing order. If the part on the material row is set to be acquired/refilled from another warehouse (regardless of supplier link), then a Stock order – Purchase will be created for the internal supplier which is tied to that warehouse. It is not possible to update quantity or delivery date when the stock order row has already been partially delivered or when final delivery has been made from the sending warehouse.
Replanning of manufacturing order
Regardless if the setting P-order has been activated or not on the manufacturing order, you can choose to replan the existing linked purchase order rows orders when you replan the manufacturing order.
If you replan the manufacturing order's quantity, start date, or finish date, and this affects the linked purchase order row and then you save, a dialog box is shown. In this dialog box you can choose whether or not the corresponding information on the linked purchase order row should be updated. You see the purchase order row's new quantity and new delivery date in the dialog box.
If the P-order setting is activated and you replan the quantity, start date or finish date of the manufacturing order, and the material on the linked purchase order has a partial quantity registered in the Part register, a dialog will open. In that dialog you can only update the corresponding information for the date for the linked purchase order row. To update the quantity on the purchase order row you use a link in the dialog to manually open the purchase order, and replan the quantity by clicking the Partial quantity button on the purchase order row.
If you replan a manufacturing order timewise (ahead or back in time) which gives a new requirement date to the material row with the linked purchase order, then a dialog box will open when you save. There you choose if you want the purchase order to also be replanned with a new delivery date. Please note! Replanning will not take place if the purchase order row has remaining quantity 0. When you replan the manufacturing order, the existing rules are used (same as for linked purchase order to customer order row) to get the right type of Purchase order/Modified purchase order, depending on the status of the purchase order at the time of the modification. If you replan a manufacturing order regarding quantity, it works in the same way as when you replan it in time.
It is not possible to delete a manufacturing order if there is a linked purchase order. In that case you first have to delete the purchase order to then be able to delete the manufacturing order. It is also not possible to delete a material row to which there is a linked purchase order row. In that case you first have to delete the purchase order row to then be able to delete the material row.
When you add a material row to the manufacturing order, a new purchase order will be created if the setting P-order is activated on the manufacturing order.
It is not possible to change revision on the material row if it has a linked purchase order row.
Replanning of linked purchase order row
If you replan the delivery date of the linked purchase order row (ahead or back in time), making the delivery date affect the material requirement date of the manufacturing order or operation, then you can choose if you also want to replan the manufacturing order. When you save the purchase order, a dialog box is shown where you can click the button Open manufacturing order to open this procedure and replan the manufacturing order.
Normally, it is not possible to change the quantity on a linked purchase order row. The quantity field is then blocked. But if the part on the linked purchase order row has a partial quantity registered in the Part register, you can replan the quantity by clicking the Partial quantity button on the purchase order rown. This replanning will not affect the quantity of the manufacturing order.
If the linked purchase order row is deleted, the link to the manufacturing order will also be deleted.
Automatic clearance of material row at arrival
The material row on the manufacturing order will automatically be cleared with the quantity that is arrival reported on the purchase order row, if they are linked. Clearance status on the operation (the one shown e.g. in the priority plan) is also set to Cleared, but not until all material for the operation has been cleared.

#### Quantity
Here you enter the quantity of the part that will be manufactured. If the part has an order quantity registered in the part register, that quantity will be suggested in this field. If you enter a quantity on the order that is greater than the part's maximum quantity, you will see a message saying that the order will be divided into several main part rows (nodes). If you enter a quantity smaller than the part's minimum quantity, a warning also appears.
Quantity is a term used for alternate BOM and routing. If quantity is entered as a term for operations and material in the part's BOM and routing, the entered quantity will affect which operation rows and material rows that by default are added, replaced, or deleted on the order.
If the manufacturing order is created from a linked customer order row, the field is not possible to edit. This means it is the quantity on the customer order row that will determine the quantity on the manufacturing order.
This field is also not possible to edit if there are partial quantities registered for the part. In that case, enter the quantity from the partial quantities on the manufacturing order via the Partial quantity button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) (see below).

#### Configuration
If the selected part on the order is linked to a configuration group you can configure the order by using the button in the Configuration column. If the button shows this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Available.png) it means the part is missing a default configuration template. By clicking this button you access a configuration window where you can configure the part. When you confirm the configuration using the button Confirm ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) in that window, the symbol on the button will change ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png), to illustrate that the part is configured.
When you save the order in the procedure, the configuration of the part also becomes saved. Then a pre-calculation is also saved for the configured part, based on the quantity entered on the order.
The part can have a default configuration determined in the part register, and in that case this configuration will automatically be loaded to the order.
If the manufacturing order is created from a customer order row, then it is not possible to modify the configuration. Any modifications must be made on the customer order row which in its turn will update the manufacturing order.

#### Unit
Here the standard unit of the part is shown.

#### Partial quantity
If the part has partial quantities, these will be shown when you click the Partial quantity ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button as described below.
If the part on the order has the control method set to Stock driven, you see the partial quantities that are registered for the part. You can make changes to the rows, add rows with quantities, each partial quantity in the part’s unit, and you can link a packaging part to each partial quantity. You can delete the rows with existing partial quantities which should not be included on the order.
If the part on the order has the control method set to Order driven, you see the partial quantities that were saved on the linked customer order. In this case as well, you can make changes on the rows, add and delete rows. Note, however, the partial quantity on the linked customer order will not be updated.
Quantity x the partial quantity’s Quantity are added together and entered in the quantity field of the order. It is not possible to make changes in the quantity field on the order if there are partial quantities. The number of partial quantities you have entered under the button will only be saved on the order, not for the part.

#### Start date
The start date determines when the manufacturing of the part on the order will start. The start date field is empty by default for new manufacturing orders. It is calculated when the order is saved by using so-called "back planning" (in normal cases). However, it is possible to enter another start date even if the finish date is pre-filled. The manufacturing order will then be "compressed" or "extended" in time, in relation to the start date that would have been calculated. If you only enter the start date and delete the finish date, the system will apply so-called "planning ahead" and calculate the finish date instead. If the start date is in past time, the date will be displayed in red text.

#### Finish date
The finish date is the date when the manufacturing order should be finished. When you register the manufacturing order manually, the suggested finish date is: today's date + throughput time for the part in work days. The finish date of the order is the same as the last operation's Planned finish.
If the manufacturing order is created from a customer order, the suggested finish date is the Delivery date on the customer order row minus the Safety time for the part in work days.
If the finish date is in past time, the date will be displayed in red. A validation of the date will be made. A warning will appear if it is in past time or more than one year ahead in time. The finish date is shown in italics if the order has been changed and it resulted in the current date not being the same as the initial date.
Finish date is a term used for alternate BOM and routing. If Finish date is entered as a term for operations and material in the part's BOM and routing, the entered finish date will affect which operation rows and material rows that by default are added, replaced, or deleted on the order.
If you are using the check delivery times function (CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.), you can also use the earliest finish date suggested by the CDT calculation (see the following three columns). Read more about the check delivery times function under Using MONITOR on the start page of the online Help function.

#### Earliest finish date
In this column you can see the earliest possible finish date according to the CDT calculation. If it is possible to report the order as finished on the entered finish date or earlier, then the date is displayed in green color. If the earliest possible finish date is a date after the entered finish date, then the date is displayed in red color.
Using the button Use the dates suggested by the CDT ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) on the function menu, you can choose to apply the earliest finish date to the field Finish date. If you click the button, there are two alternatives. You can here choose to apply earliest finish date to the selected order row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) (Ctrl + D) or to apply the date to the orders on all rows ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace_all.png) (Ctrl + Shift + D).

#### Difference
Here you can see the difference between the suggested finish date and the earliest finish date. The difference is shown in number of work days, and in the same color as in the preceding field.

#### CDT
The button in this column always show a symbol of a factory ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeManufacturing.png) which means that manufacturing is required for the order. A tooltip over the button displays the same in text. The difference from running CDT on a customer order, is that no requirement calculation is made when running CDT on a manufacturing order. This is not needed since manufacturing should always take place.
If the CDT has selected an alternative supplier or work center for the order, you will will also see an asterisk (*) on the button. This information will also be included in the tooltip available on the button.
If you click on the button you will see a result window from the CDT. There you see the planning window of CDT, and also its manufacturing order suggestion and a loading chart. You can used the result window to investigate where there are critical operations/material, that is, the operation or material that determines which the earliest finish date can be.
In the Summary table at the top part of the result window, you can on the first row see the entered finish date on the order. On the next row you see what will be the earliest finish date if the standard work centers are used, and also the order's Contribution margin and Contribution ratio. On the third row you see which the earliest finish date will be if the alternative suppliers and work centers selected by CDT are used. You will also see what the order’s contribution margin and contribution ration will be in that case. If there are alternative suppliers or work centers selected by CDT, then you can check the Apply box on the third row if you wish to use that alternative, or you can keep the default setting to use standard work centers. By using the button Confirm![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) you confirm which row should be used. The result window will then close and the finish date of that row will be loaded to the Finish date field on the order.
Read about [Check delivery times](../../../UserGuide/Using/CheckDeliveryTimes/CheckDeliveryTimes.htm) under Using Monitor G5 in the online help function.
> Please note! An alternative supplier or work center selected by the CDT will not be included on the order when you save it, regardless if you have chosen to use the alternative supplier/work center in the CDT result window. The standard supplier or work center will be used. In that case you must manually change supplier or work center on the order to the alternative one selected by CDT.

#### Priority
Here you see the priority of the manufacturing order. The priority is used when selecting and sorting lists. If the order is registered manually, the suggested priority is loaded from the lowest priority value on order type and selected customer on the order. Please note! Lowest value = Highest priority. The priority can be changed. If the manufacturing order is created from a customer order, the priority will by default be the same as in the customer order header. The field will then not be possible to edit.

#### Serial number
If you have activated traceability at serial number level for a part, the serial number will be loaded when the manufacturing order is registered. The serial number is loaded from the number series and becomes saved when you save the manufacturing order. If you have not registered own serial numbers there is always a number series to fall back on.
If you increase the quantity of an existing manufacturing order, new serial numbers will be created for the new quantity. If you report more than the planned quantity, serial numbers will also be loaded for the reported quantity. If you report less than the planned quantity and delete the remaining quantity (or replan the order to a quantity smaller than the initial), then the final reporting will remove the serial number that have not been reported.
In cases where the customer order row has serial numbers and the manufacturing order is created based on the customer order, the serial numbers will be inherited to the manufacturing order.
On the manufacturing order documents and transport labels which you print, it is possible to show the serial numbers.
Operators must enter which serial numbers they are reporting on if there are more than one serial number on the manufacturing order. It is only possible to report on one (1). This way the serial number traceability remains intact, even though the quantity on the order is greater than one (1). This applies to operation reporting and material reporting.

#### Comment
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).
You can also enter a comment. This will be printed on the manufacturing order documents.

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
Here you can select if documents should be automatically printed together with the manufacturing order documents.

#### Revision
The revision of the manufacturing order is by default set to the part's active revision. You can select between the part's revisions.
Revision is a term used for alternate BOM and routing. If revision is entered as a term for operations and material in the part's BOM and routing, the entered revision will affect which operation rows and material rows that by default are added, replaced, or deleted on the order.
If the manufacturing order is created from a customer order, the revision will be the same as on the customer order row. It will also no longer be possible to edit the field.

#### Customer order
This column shows the customer order number if the manufacturing order is created from a customer order. By using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to the right, you can see information from the customer order header and the customer order rows.
Customer order number is a term used for alternate BOM and routing. If customer order number is entered as a term for operations and material in the part's BOM and routing, the entered customer order number will affect which operation rows and material rows that by default are added, replaced, or deleted on the manufacturing order.

#### Customer order row's goods label
If you create a manufacturing order from a customer order, then the row's goods label will be included to this field on the manufacturing order. (If the customer order row's goods label is entered in Register customer order.)

#### Customer
Here you can see the customer that the manufacturing order refers to.
Customer number is a term used for alternate BOM and routing. If Customer number is entered as a term for operations and material in the part's BOM and routing, the entered customer number will affect which operation rows and material rows that by default are added, replaced, or deleted on the order.
If the manufacturing order is linked to a customer order, you will see the customer number. This field is then not possible to edit. A tooptip for the field displays the customer name.

#### Project
The manufacturing order can be linked to a new or an existing project. If you have checked Manufacturing on project in the part register it is mandatory to enter a project. If you there also entered on which project the manufacturing should take place, then it is not possible to change project on the manufacturing order row.
If the manufacturing order is created from a customer order, the project number cannot be changed or deleted. However, you can modify the project name. The project number is then loaded from the customer order row and registered on the manufacturing order.
If a project has been entered and the part has a serial number, the project will be saved on the serial number in the Serial numberA serial number is a number that is used for traceability for parts on entity level./BatchA batch is the set of components/products manufactured at the same time and made from the same original material. procedure.

#### Name
Here you enter the Name of the project if you in the project field entered a new project number. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Variant code
You can enter a variant code for operations and materials in the BOM and routing. This makes it possible to add and delete operations and materials dependent of the variant code.
Variant code is a term used for alternate BOM and routing. If variant code is entered as a term for operations and material in the part's BOM and routing, the entered variant code will affect which operation rows and material rows that by default are added, replaced, or deleted on the order.

#### Initial finish
Here you can see the initial finish date of the order. You can edit this date on the order.

#### Confirmed as delayed
You can check this box for an existing manufacturing order if it is confirmed that the order is delayed and that it cannot be rescheduled.

#### Cause of delay
You can in this field select a cause code for the delay if you have checked the Confirmed as delayed box. Otherwise, this field is inactive. The cause codes must be registered in the Cause codes procedure. This way you can create statistics for the different causes of delay.

#### Comment on delay (C)
You can in this field enter a comment regarding the delay. This is possible if you have checked the Confirmed as delayed box. The cause code might have mandatory comment. The comment is not mandatory if the order is not confirmed as delayed. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Warehouse
If you use the option Warehouse you will also see this column. A manufacturing order belongs to a warehouse (WH).
Default warehouse on a new manufacturing order which you register manually, will be the warehouse you are currently working in. If the manufacturing order is created from a customer order, the warehouse will instead be loaded from the customer order row.
When needed, you can register several manufacturing orders belonging to different warehouses. You can register orders and replan operations belonging to another warehouse even though you do not have user rights in that warehouse. This can be done as long as you have sufficient user rights to replan in the order's warehouse.
Structure explosion/order registration is made of each operation according to which warehouse the work center belongs to, and saves the warehouse on each operation. For subcontracting work centers, WH is not mandatory. For those subcontracting work centers that are missing a warehouse, the same warehouse will be used as for the previous operation. If previous operation is missing (if the subcontract is the first operation in the level), then the same warehouse as the one on the node, will be used. The purchase order you create for the subcontract when the manufacturing order is created, will inherit the warehouse from the subcontract.
For each material row the warehouse for the operation, in which the material is included, will be saved. The top node (the main part) gets its WH from the manufacturing order.
If the work center is changed for an operation, the warehouse from the work center will be used for the operation and its material. If you change work center from own to subcontract, then the same rules will apply as described for when registering new order (see above).
If you change warehouse for a work center, the new warehouse will be used on all manufacturing orders' operations which have that work center and which have a remaining quantity.
If you change warehouse for an already registered manufacturing order, then it will only be changed on order and main part, and in some cases on subcontracts. In theory, the new warehouse can have a different lot sizing rule for included manufactured part, which affects the structure explosion. But this is something you must decide on via an option in the Explosion field. Selecting warehouse during new registration of order compared to changing it on an already registered order, can therefore result in different structure explosions.

#### Manufacturing order category
Here you can enter a manufacturing order category. By clicking the Category selection button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select a category if categories have been registered in the Categories procedure. If no categories are registered, you can type as you please in this field. Categories can be used as a selection term in different lists. Read more about how categories can be created/constructed in the online help function for the [Categories](../../../GeneralRegisters/Categories/Categories/wCategories.htm) procedure.

#### Category selection
Under this button you can select category according to the categories registered in the Categories procedure.

#### Change status
By clicking the button in this column you access a window where you can change the status of the part nodes in the order. If the order only has one manufactured part, the order will be give the same status when you save. If the order has multiple part nodes, you can change status of each part node. The order will then be assigned a status according to the criteria below:
When all part nodes have status 1-3, the order will be assigned the same status as the part node with the highest status. When all part nodes has been given status 4 (Finished), the order will also be assigned status 4. The order is assigned status 5 (Post-calculated) if all part nodes have been set to status 5.
As long as the status of the order is lower than 5, you can change status within the interval 1-5. If the status of the order is 6 (Delivered), you can change the status within the interval 1-6. If the status of the order is 9 (Historical), then you can change status within the interval 1-6 and 9.
The purpose of changing status on part nodes can, for example, be to change from status 2 to 1 in case someone printed the order by mistake, or to change from status 4 to 3 if you need to plan an excess quantity for an already finished order.
