### The Scanning mode tab
Under this tab you can scan parts to a list used to move a stock balance. The scan loads information from labels and transport labels, etc.

#### Source
At the top of the tab you configure which sources you will use for scanning of parts. The sources Part, Serial numberA serial number is a number that is used for traceability for parts on entity level., BatchA batch is the set of components/products manufactured at the same time and made from the same original material., and Location, are marked by default. You scan data to the field next to Source.
If your scan gets one (1) matching part, it will automatically be added in the list of parts to move.
If you get multiple parts that match, these parts are shown in the Multiple matches – select rows dialog. In the dialog window you can scan again to the Scanning field, for example, a serial number or batch number, and then the part's Include checkbox will be marked. It is also possible to manually mark the Include checkbox. When done, you click OK to close the dialog and add the marked parts to the list of parts to move.

#### Exact match
Mark this checkbox if you wish the search result to only show exactly what has been entered in the search field (applies to Part, Batch, Serial number, and Location name). How this checkbox is configured is saved for the user.

#### Warehouse
This field is only shown if you have installed the Warehouse option. Then you can here select a default warehouse in order to move a quantity to locations in that warehouse.

#### Default location
You can here select a default location to move the quantity to. If the Warehouse option is installed, you can select from the locations available in the selected warehouse.
By clicking the button called Apply to all selected rows ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can use the default location for all rows in the list.
The list of selected parts

#### All
This checkbox is marked by default in the list. This means the available balance on the location to move from is entered in the Qty to move column.

#### Qty to move
Here you can enter a quantity to move. This is entered in the standard unit of the part. The location's available balance is shown by default when the All checkbox is marked. You can modify the quantity but it cannot be greater than the available balance on the location which is to be moved from.
Other information
Other information in the list under the Scanning mode tab is the same as in the [Parts to move](bPartsToMove.htm) list under the Manual mode tab.
