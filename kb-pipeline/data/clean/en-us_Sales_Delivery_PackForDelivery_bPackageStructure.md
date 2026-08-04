### Package structure
In this box you see the pick list's package structure as package rows and the related part rows. The part rows corresponding to the row marked in the box To pack are displayed with a light yellow background.
You can make changes in the package structure by using buttons on the function menu in the box. In the package structure you can also update certain information on package rows and part rows.
> You can use the drag and drop function and add packaging parts in the package structure. You drag parts from the Packaging parts box and parts to pack you drag from the To pack box.
The Function menu
Use the button Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5) to add a package row at the bottom of the package structure. In the dialog which opens you select or search for a part or a packaging part to add. In this dialog window you can use the button Show unlinked packaging parts ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_hidden.png) to see all packaging parts you have in the part register. You can also enter a quantity of the packaging part to add in the package structure. If the packaging type is Cover packaging, the quantity will be added to a row in the package structure. For other packaging types, one row will be added per piece of the packaging part.
Using the button Insert new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) (Shift + F5) you insert a package row above the row in focus in the package structure. The same dialog as above will be shown.
Using the button Delete selected row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6) you delete the row (package row or part row) which is marked in the package structure.
Using the Add underlying level button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_subrow.png) (Ctrl + Shift + F5) you can insert a package row as a sub-row for the package row marked in the package structure. The same dialog as above will be shown.
Using the Move selected button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_streamline.png) you can choose to move part rows and package rows which you have marked with the Include checkbox in the package structure. If you click the button, there are two alternatives: Move selected to current packaging part and Move selected to new packaging part.
- To move selected to current packaging part, you first mark the Include checkbox for the parts and packages you want to move. Then you mark (put focus on) the package row to which you want to move it. As the final step, you click the button called Move selected to current packaging part.
- To move selected to new packaging part, you first mark the Include checkbox for the parts and packages you want to move. Then click the button called Move selected to new packaging part. After which you see the same dialog as when adding package row.
By clicking the Insert remaining quantity button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_package.png) you open a dialog where you can choose which remaining (not yet packed) parts you want to add in the To pack box for the package you have marked in the package structure. You cannot enter a quantity greater than what is actually left to pack.
By clicking the Print button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_print.png) you can choose to print a pack list or a transport label. These printouts can also be made from the Document tab.
Using the button Clear ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_release.png) you clear the parts on the marked part row, including sub-rows in the structure. The checkbox Cleared will then become checked. Preliminary quantity is moved to Cleared quantity on the part row. The Location button becomes activated and you can see and choose location where to clear the quantity. You execute the clearance by saving the pick list in the procedure.
Using the button Undo clearance ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_undo_release.png) you undo the clearance of parts on the marked part row, including sub-rows in the structure. The button has the reversed function of the Clear button. You execute the undoing of a clearance by saving the pick list in the procedure. If the pick list has been delivery reported, it is no longer possible to undo a clearance.
With the buttons Move up ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_up.png) and Move down ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_down.png) you can move the marked package and its related parts up or down the structure.
With the button Move in ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_in.png) you can move a package and its related parts in under a different package in the structure. For example, if you have added a pallet and you then want to move in boxes to it. With the button Move out ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_move_out.png) you can move a package out a step in the structure.
The button Calculate weight ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) resets the gross weigh on the rows based on the weight information on packaging parts and parts in the part register. If a manual change has been made of the gross weight on the rows, then this will be deleted if you click the button.
Using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can use the link to go to related procedures for the marked row, for example, to change information on the row.
By using the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) (Shift + F8), you can expand/minimize all levels on the rows in the package structure.
Information possible to update on the rows

#### Include
Rows for which the Include checkbox is marked, can be moved to sub-rows for the package row in focus in the package structure, or you can move them to sub-rows for a new package row. You move the rows by clicking the Move selected button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_streamline.png) on the function menu or on the context menu which you access by right-clicking.
> You can delete multiple package rows at a time by marking the rows in the Delete column and then click the Delete selected row button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) in the function menu and then Save. Please note! It is not possible to delete rows if any of the rows have been marked as Complete.

#### Part number
You can change the part number on a package row if you need to change the packaging part on the row. You can change to a packaging part of the same packaging type. If you change a packaging part, a recalculation will be made when you save. This will update the package’s gross weight, length, width, height, and volume.

#### Preliminary quantity
Here you see the preliminary quantity on the part row before clearance. It is possible to change the preliminary quantity to be cleared and packed. If the packed quantity differs from the quantity to pack in the To pack box, a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is shown there after the part row has marked here as completely packed. A tooltip over the warning symbol displays the same in text.
On a package row you see the quantity of the packaging part if it is of the packaging type Cover packaging. Here you can edit how many of the packaging part that is needed in the package structure.

#### Cleared
This checkbox determines if the quantity on the part row is cleared. When the box is checked, the Preliminary quantity is moved to Cleared quantity. For a part which is not stock updated, no clearance is made.

#### Location
The Location button becomes available when the part row is marked as cleared. By clicking the button you access a dialog window where you can see and choose location from which the Cleared quantity should be withdrawn. You can change the cleared quantity in the dialog. You can mark All to change the entire disposable balance for the location to cleared quantity. Changes made here to the cleared quantity will update the Cleared quantity column on the part row. If the Complete column on the part row is marked, you cannot change the cleared quantity in the dialog for location.
By checking the Swap checkbox you can change the pick list’s cleared quantity into a quantity which has been cleared on a different pick list. This can, for example, be used if the batch you should pick from is placed at the very back of the pallet rack and it is easier to pick from the batch in front.
Scanning field is activated for parts with traceability. It can be used to select batch or serial number from the list. When you enter the serial number or batch number in the scanning field and then press TAB or ENTER, the system will search for a matching serial or batch number and marking the All column for the matching serial or batch number.
Please note! If the same batch number exists in more than one place, the All column will be marked for all matching rows with that batch number.

#### Complete
This checkbox determines if the package row and the underlying package rows and their related part rows, are completely packed. It also determines that the packaging part on the package row should be cleared (quantity 1). If you mark an empty package (a package row not containing a part row) as completely packed, a dialog appears letting you know the package structure contains empty packages. You can then choose if you wish to keep the empty packages, delete the empty packages, or cancel. If you choose to remove an empty package, the corresponding package will be marked in the package structure.
When all rows have the Complete checkbox marked, all packages in the pick list are considered ready for delivery. You then select Yes for the setting Package structure ready for delivery on the header row.
You make the delivery reporting of the pick list in the Report delivery procedure, using the list type Via pick list.

#### Gross weight
The gross weight of parts is calculated as: the part's net weight x the part quantity. The gross weight of a package is calculated as: the packaging part's net weight + the part's net weight x part quantity per package. The gross weight can be changed manually. If you change the gross weight, it will be displayed in italics. A tooltip in the column informs you that the gross weight has been manually changed and what the initial value was.
At the bottom of the box you see the Gross weight total for the entire package structure.

#### External package ID
(Optional) On a package row you can here enter an external package ID, if needed.

#### Container number
(Optional) On a package row you can here enter a container number, if needed.

#### Seal number
(Optional) On a package row you can here enter a seal number, if needed.

#### Length, Width, Height, Volume
For a part row you only see the part's volume in total. The volume is calculated as: the part's volume x the part quantity.
For a package row you see the package's length, width, height, and volume. The volume is dependent of the setting Package volume consists of on the packaging parts in the part register. The following applies:
- If the packaging part's Package volume consists of is set to Packaging volume (enclosing), it is the packaging part's volume which is shown.
- If the packaging part's Package volume consists of is set to Packaging vol. + part vol., it is the packaging part's volume + all packages'/parts' volumes on underlying level which are shown.
You can change values for length, width, and volume. If you change a values, this will be shown in italics. A tooltip for the value in the column informs you that it has been manually changed and what the initial value was. (In order for this tooltip to be displayed, you must first have dragged the column from the More info button to the table.)

#### Goods type
Here you can enter a goods type for the package. The field can be edited for the top package levels (for other packaging parts than outer packaging) and for as long as the “Complete” checkbox is not marked. When a shipment is then created from the source of information called Pick list A pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. with package structure, this goods type will be entered for the package in the shipment. (In order for this tooltip to be displayed, you must first have dragged the column from the More info button to the table.)

#### Internal comment, External comment
By clicking these buttons you can enter an internal comment and an external comment for the row in question.
Other information you find on the rows
Type: Here you see the packaging type illustrated with a symbol. A tooltip is shown when you hover over the symbol, displaying the packaging type in text. The available packaging types are: EUR pallet, Outer packaging, Inner packaging, Cover packaging, and Unspecified.
Part number, Name: Shows the part number and name in the part register.
Cleared quantity: Shows the preliminary quantity that has been cleared. Preliminary quantity is moved to Cleared quantity when the Cleared checkbox is marked. For a part which is not stock updated, no clearance is made.
Packed quantity: Shows the cleared quantity which has been packed. Cleared quantity is moved to Packed quantity when the Complete checkbox is marked. For a part which is not stock updated, the Preliminary quantity is moved directly to Packed quantity when the Complete checkbox is marked.
Payload parts: Shows the part number of the parts which have been packed in the packaging part on the package row.
Package number: Shows a consecutive number assigned to the package row if the setting Assign package number has been activated for the packaging part in the part register. In the Number series procedure you can enter a starting number for the package number series.
Customer order number: Shows the pick list's customer order number on part rows.
Position: Shows the customer order row's position on part rows.
Template code­: Shows the template code for the handling unit level in the package structure, if a template code has been entered for the packaging template. The field is editable until the row has been marked as Complete. The template code will also be exported when exporting complex dispatch advice from version 11 of the format onwards.
Type of PU: Shows, on package rows, a label for the type of packaging unit which can be of the following three types: S (Simplified/Parts identification label), M (Homogenous), or G (Mixed). This is according to the Odette Transport Label (OTL).
Responsible: Shows the person who is selected to be responsible of packing the part. This information is shown on part rows.
Goods label printed when: Shows the goods label entered on the order row, as well as date and time when the order was printed. This information is shown on part rows.
Delivery note number: Shows the delivery note number, if it has been marked on the order that delivery note number should be created when delivery planning. This information is shown on part rows.
Pick instruction: Shows the pick instruction, if such has been entered for the part in the part register.
Other package number: Displays package number for SSCC, OSCAR, DUNS, or JIPDEC, if used for this type of package. Number series for these are first entered in the Number series procedure.
Other package number series: Shows if the number series is SSCC, OSCAR, DUNS, or JIPDEC. If no package number has been entered in Other package number, no package number series is shown in this column.
Total
At the bottom of the box a total section is show containing different information about the entire package structure.
No. of handling units: Shows the number of packages on the highest level in the structure.
No. of outer packaging: Shows the number of packages of the packaging type Outer packaging.
No. of inner packaging: Shows the number of packages of the packaging type Inner packaging.
No. of EUR pallets: Shows the number of packages of the packaging type EUR pallet.
No. of unspecified packaging: Shows the number of packages of the packaging type Unspecified.
No. of cover packaging: Shows the number of packages of the packaging type Cover packaging.
No. of levels: Shows how many levels of packages that exist in the structure.
Gross weight: Shows the gross weight as total for all packages on the highest level in the structure.
Tare weight: Shows the net weight of the packaging parts.
Payload net weight: Shows the net weight of the parts.
Packaging parts – Summary: By clicking the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button you access a list with all information of the packaging parts as well as how many are ready for delivery.
Loading meter: Shows loading meters for all packages.
Volume: Shows the volume for all the packages.
Earliest delivery date, Latest delivery date: Shows the earliest and the latest delivery date found among the order rows.
