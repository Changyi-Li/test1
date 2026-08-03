### Settings – Printout

#### Printed by (employee)
The employee that you select in this field will be shown on the pick list as the person who created/printed the pick list. If no employee is selected, the current user will be shown on the pick list.

#### Sort material rows by
Here you decide how to sort the material rows on the pick list. You can choose from: Location, Main location Earlier called "Current location". Main location means the stock location for a part that has the most recent arrival date for the part. If you apply priority for the locations, then the main location is the location which has the highest priority (that is, the lowest number)., Material's part number, Location's route sorting number*, or Main location's route sorting number*.
*These two options can be applied if you have created route sorting numbers for the location names. This is done using the Route sorting list in the Location list procedure.
The Grouped by material presentation always sort material by Location.
The order of priority of the locations is based on age analysis. That is, the oldest Last arrival date at the top. You can, however, disregard the age analysis by using priority; a location with priority 1 will be placed above a location with priority 2, and so on. If the location is a pick location, the priority will be disregarded, meaning the pick locations will always be placed highest in the table.

#### Show all locations
If you activate this checkbox, all locations will be shown if the material has more than one location. This setting is available if you choose to sort the material rows by Main location or Material's part number.

#### The material's unit
With this setting you determine which unit should be used for the material rows in the pick list. You either select the standard unit or the unit which was used on the material withdrawal on the manufacturing order.

#### Open the procedure Report pick list
With this setting you decide if the procedure Report pick list should automatically be opened for each pick list when the pick list is saved or reprinted.

#### Hide materials with pick location
With this setting you determine if parts on material rows which have a pick location and/or pick location for work center entered as location, should be hidden or not. If you activate this setting, these parts will be hidden on the document with the pick list, but they are shown under the List tab. This setting is available when the system setting Apply pick location is activated.
