### Parts to move
In this list you see the parts for which Move all has been activated, or where a Qty to move has been entered in the table containing the selected parts.
On the function menu you find the following buttons:
- Create new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) – If you distribute a quantity of the part you are moving to multiple locations, you use this button to copy the marked row to a new row. On the new row you should then enter a quantity to move and select or enter a location. The total of the quantity to move for all rows must correspond to the quantity to move of the part in the upper table. This value can be adjusted in both tables.
- Delete row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) – With this button you can delete the marked row. If you have created (copied) new rows by using the button described above, all those rows which have the same part will be deleted.
- Clear processed rows ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_reject.png) – With this button you deleted the rows with parts that have had their quantity moved when you saved in the procedure.
- Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) – Use this button to open the part on the row in the Part register procedure.
- Print transport labels for saved rows ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_print.png) – With this button you open the Print transport label – Part procedure where you can print transport labels for the part rows where the quantity has been moved prior to when this procedure was saved.
- Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) – (Shift + F8) With this button you can expand or collapse the part all rows in the table.

#### Revision
Here you see the part's revision.

#### Last arrival date on "From location"
Here you see the part's most recent arrival date on the location from which you are moving a quantity.

#### Cleared (C)
If there is a cleared quantity of the part, this column appears and a C is displayed in the column on an extra row for the cleared quantity. If you place the cursor over the column on the row, a tooltip will show where the quantity is cleared, for example, for a manufacturing order and the order number.

#### Available balance
Here you see the part's available balance. (The available balance is calculated as the current balance minus the cleared balance.) On the extra row for cleared balance you see the cleared balance in this column.

#### Total qty to move
Here you see the total quantity to move of the part.

#### Qty to move
Here you see the quantity of the part (in the selected unit) to move to a location. You can modify the value but it cannot be greater than the part's total quantity to move in the list of selected parts.

#### To warehouse
In this column you see in which warehouse you find the location that the quantity is moved to. This column is displayed if the Warehouse option is installed.

#### To type
Here you see a symbol illustrating which type of location you are moving the quantity to. There is also a tooltip for the procedure letting you know the type.

#### To location
If a Default location has been entered at the top of the tab, it will be suggested the quantity is moved to that location. If not, a warehouse location is suggested according to the sections of the rules that apply for sorting of locations during withdrawal. Read more about those rules [here](../../Parts/PartRegister/bStock.htm) (cleared balance and best-before date not included). You can also manually select a location. If you want to create a new location, you enter a new name.
If you have copied multiple location rows for the same part by using the Create new row button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png), in order to distribute the number to move of the part to several locations, it is possible to enter different or the same location name on all location rows. If you enter the same location name, the Group balance on locations with the same name system setting directs the quantity to either be moved to the specified location or to move the quantity/balance to as many locations as there are location rows, with the quantity distributed as you have specified it on each location row. In the latter case, the same number of locations as copied location rows are created.

#### From location
Here you see the location from which you are moving the quantity.

#### Batch
If the part on the location that you are moving the quantity from has a batch number, this is shown here.

#### Serial number
If the part on the location that you are moving the quantity from has a serial number, this is shown here.

#### Best-before date
If the part on the location that you are moving the quantity from has a best-before date, this is shown here.

#### Cleared for
If the part is cleared, you will see for which order the part is cleared. The order number is shown in the column to the right.

#### Pick location
Here you determine if the location should be a pick location. This setting and the next setting called Pick location for work center are available if the Apply pick location system setting is activated. It is possible to activate both pick location, pick location for work center, and arrival location, for a location (see below).

#### Pick location for work center
Here you determine if the location should be a pick location for work center.

#### Reorder point
Here you enter/see the reorder point for the pick location. This setting is activated if any of the above two settings called Pick location or Pick location for work center is marked.

#### Refill quantity
Here you enter/see the refill quantity for the pick location. This setting is activated if any of the above two settings called Pick location or Pick location for work center is marked.

#### Arrival location
Here you determine if the location should be an arrival location. This setting is available if the system setting Apply arrival location is activated. It is possible to activate both arrival location, pick location, and pick location for work center, for a location.

#### Priority
Here you can change the priority of the location.

#### Last arrival date on "To location"
Here you see the part's most recent arrival date on the location to which you are moving the balance.

#### Exclude balance
Here you determine if the balance should be excluded during net requirement calculation, requirement calculation, and check delivery times. Read more about this in the section [Locations](../../Parts/PartRegister/bStock.htm) in the online help function for the Part register procedure.

#### Comment
Here you can enter a cause regarding the move of the stock balance.
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Charge number
If the part on the location has a charge number, this is shown here.
