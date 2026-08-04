### The Manual mode tab
Under this tab you can manually search for the parts for which you want to move a stock balance.

#### Search for parts
At the top of the tab you can search for parts using the following terms: Part number, BatchA batch is the set of components/products manufactured at the same time and made from the same original material., Serial numberA serial number is a number that is used for traceability for parts on entity level., and Location name. You can combine multiple terms. For example, you can enter a part name in the Part number field and a name for a location in the Location name field.
When you leave a filled-in field, the parts you searched for are displayed in the [Selected parts](bSelectedParts.htm) section, from where you then specify a number of the parts to move or choose to move the entire balance of parts.
These parts are then displayed in the [Quantity to move](bPartsToMove.htm) section, where you select location to move to and can make additional settings on those locations.

#### Grouping
Here you can choose if the list should be grouped by Location, Batch, Part, or None (meaning no grouping will be made).

#### Person
Select the person from the personnel register who will execute the move. This will then be saved in the column Signing employee number on the transaction in the stock transaction log. The field can be set as mandatory with the system setting Mandatory to enter person in Move stock balance.

#### WH – To
This field is only shown if you have installed the Warehouse option. Then you can here select a default warehouse to move balance to.

#### Default location – To
You can here select a default location to move balance to. If the Warehouse option is installed, you can select from the locations available in the warehouse selected in WH – To. When the transaction has been saved, the field is cleared.
By clicking the button called Apply to all selected rows ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can use the default location for all rows in the Parts to move box.
The Settings button

#### Show max no. of rows
In this field you can select a maximum number of rows to display in the list. The default option here is 100 rows. The available options are: 100, 500, 1000, and 2000 rows.

#### Selection
- Show locations without quantity – Tick this checkbox if you want to show locations with a balance of zero in the list. How this checkbox is configured is saved for the user.
- Exact match – Tick this checkbox if you wish the search result to only show exactly what has been entered in the search field. (This applies to the fields Part, Batch, Serial number, and Location name). How this checkbox is configured is saved for the user.

#### Use records from Clipboard
- Part – Determines if parts should be used from clipboard.
- Serial number/Batch numberA batch number is a number that is used for traceability for a set of or a batch of parts. A purchased material can have a batch number that should be able to be traced back to a certain charge number from a supplier. – Determines if serial number/batch number should be used from clipboard.
