### Pick lists (Picking in progress)
In this list you see the selection of pick lists where picking is in progress. You can delete as well as reprint the pick lists.
Preliminary pick lists can also be displayed. You can reprint or delete such pick lists. Preliminary pick lists are shown in italic font.
By using the Delete selected row button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6) on the function menu, you delete the pick list for which the Include button is marked in the list.
By using the Create shipment button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_shipping.png) you can choose to Create shipment from pick list or Create shipment from pick list with package structure, for the pick list where Include is marked in the list.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png), you can go to related procedures for the pick list of the marked row.
For each pick list you see the pick list number, customer number, customer name, pick time, date and time when the pick list was printed and by whom, date and time when the pick list was created an by whom, if the package structure is ready for delivery, how large portion (in percent) of the pick list has been packed, and the number of the handling units. Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you find additional information. Please see an explanation of the columns on rows below.
In the Order rows bow to the right you find the same information on the order rows as in the Picking plan list. Read more about this information in [Order rows](bOrderRows.htm).
Under the Reprint tab you can choose to reprint pick lists, packing lists, and transport labels. This tab works in the same way as the Documents tab, in cases where you choose to load any of the list types Picking plan, Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. by order, or Release preliminary pick lists.

#### Include
With this checkbox you decide if the pick list should be included to be deleted or to create shipment from the pick list.

#### Pick time
The pick time is the time it is calculated it will take to physically pick the parts on the pick list from stock. This time is calculated based on entered general values in the system settings Setup time for picking per order row and Unit time for picking per package.

#### Package ready
In this column you see a "Yes" if the setting Package structure ready for delivery has been set to Yes on the pick list in the procedure Pack for delivery. Otherwise you will here see "No".

#### Percentage packed
Here you see a bar and the value in percent of how much of the quantity on the pick list which has been packed. On new pick lists you see 0 percent. When a regular pick list has been saved (picking in progress) and is loaded via the list type Picking in progress, you will here see 100%. When the pick list is set to picking is in progress, the parts that should be picked are also considered packed. On a preliminary pick list on the other hand, you will see 0 percent even when it is saved and you load it via the list type Picking in progress.
Percentage packed is only relevant when packing is applied in Monitor ERP. In the procedure Pack for delivery you will in the pick list see which packages in the packaging structure that are completely packed. Here on the pick list you will then see a percentage value based on how many of the packages that are marked as completely packed. This applies to both regular and preliminary pick lists.

#### No. of HU
Here you see how many handling units there are in the pick list.
The More information button
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you see the earliest and latest delivery date among the order rows, gross weight, payload net weight, loading meters, volume, internal and external comments, reference number on shipment, the customer's part number, and status of shipment registered for the pick list on the row.
