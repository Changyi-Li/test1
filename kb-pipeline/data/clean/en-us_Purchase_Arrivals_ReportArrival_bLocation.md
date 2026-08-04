### Location
In this box you enter quantity to arrival report per location. This will then accumulate to a total quantity to delivery on the order row.
For order rows that should be subject to receiving inspection this Location box is not activated. Instead the corresponding Location box in the Report receiving inspection procedure is used. Then you enter a goods location instead for the order row that is being arrival reported.
By using the buttons on the function menu you can add ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) and delete ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) locations. With the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) Copy row button you can copy the above row. This makes it possible to report different batches to the same location. You also find two navigation buttons which can be used to move up ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_up_17x17.png) and down ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_down.png) between the order rows in the left section under the tab.
In the Type column you see a symbol that indicates which type of location it is. If you hover your cursor over the symbol a tooltip appears in which you can see the type.
If a return order is concerned, you here enter the quantity to return per location. In that cas you cannot add or delete rows for locations.

#### Location
Here you see/enter the location name. When you add a new location, you enter the name of the location here.

#### Arrival reported quantity
Here you enter the quantity that should be arrival reported on this location. In the Current balance Current balance is the part balance at this moment on the locations. column you see the location's current balance.

#### Quantity to return
If the order in question is a return order, you will see this column instead of the Arrival reported qty column. Here you enter the quantity that should be returned from this location.

#### Batch
If the part has traceability at batch level you will in the field called Batch A batch is the set of components/products manufactured at the same time and made from the same original material. see a suggested batch number, but you can change this number. How the batch number should be designed is decided in the Number series procedure.

#### Best-before date
If the setting Apply best-before date is activated in the part register, you must enter such a date in the field Best-before date. In the part register you can also configure if the best-before date should be suggested based on two different criteria.

#### Charge number
If a charge number is included in the goods that should be arrival reported, this is entered in the Charge number A charge number is used to provide traceability. It is the supplier's batch number, or charge number, which is linked to our batch number for a location. field. This can be the supplier's batch number.

#### Serial number
If the part has traceability at serial number level, you find a button called Serial number A serial number is a number that is used for traceability for parts on entity level. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). By using this button you can add rows ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) with serial number to each entity of the part. If you enter a serial number which already exists, a warning appears and the serial number will not be arrival reported. After you have entered a start number in the From column, you then enter in the Quantity column how many entities of the part to arrival report. Then the end number will be calculated and is automatically shown in the To field. Serial number can also be reported for arrival of subcontracts that result in transfer to stock.
By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png) on the function menu, you can import serial numbers from a text file.
In the serial number box, you can also enter charge number. By using the button Certificate ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png) you can link a certificate (as a PDF file) to each row with a serial number.

#### Batch number
Here you see the batch number if the part has traceability set to batch number.
If the traceability level of the part is set to batch number level, the button called Additional ID:s ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) is available. There you can enter Additional ID:s if the system setting called Use additional ID:s has been activated. The use of Additional ID:s enables traceability according to, for example, the EU Deforestation Regulation (EUDR).
> If you enter multiple rows with additional Id:s, all of the ID:s will be linked to the entire batch.

#### Country of origin
The country of origin from the batch number or serial number from the dispatch advice is displayed here. If no country of origin has been entered for the batch or serial number, the country of origin will be the country entered in the supplier’s delivery address at the time of arrival reporting.
