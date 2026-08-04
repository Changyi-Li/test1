### Locations
In this box there is a table where you can add and delete locations per part and warehouse. You can also configure different location settings. However, you can only delete a location if its balance is zero. If there is a negative balance on any of the part’s locations, then you cannot activate traceability.
In the Location settings list in the Part list procedure, you can update location settings for several parts at a time.
Parts with traceability
When a part has traceability and a batch number or serial number has been registered on a location, there are sub-rows on the locations that you can expand by using the arrow button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to the left in the location table. On the sub-rows you see which serial number/batch number and charge number have been registered on the location.
Rules that apply for sorting of locations during arrival
1. Locations which are arrival locations (provided that the system setting called Apply arrival location has been activated).
2. Priority.
3. Last arrival date.
Rules that apply for sorting of locations during withdrawal
In Monitor ERP, the following rules apply regarding how locations are suggested and displayed during withdrawal to customer order. The locations are sorted according to the following rules. No consideration is taken to the work centers on the manufacturing order.
1. Location which is a pick location (the Apply pick location system setting must be activated). Then comes locations which are not pick locations, and finally locations which are pick locations for work center.
2. Locations with cleared balance.
3. Best-before date (provided that it has been activated). Shortest best-before date will be consumed first.
4. The location's priority (ascending by priority).
5. Last arrival date. For locations with the same or no priority, the locations are sorted by age in ascending order. That is, the oldest Last arrival date at the top.
6. Location's ID (if the part has been arrival reported to several locations at the same time).

#### Type
In this column you see a symbol representing which type of location is concerned: Pick location![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Delivery.png), Pick location for work center![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridManufacturingGroupImage.png), or Arrival location![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Arrival.png). A location can be a combination of all three types.

#### Status (S)
If the part has traceability set to batch or serial number, this column is shown. Here you can see a symbol for the serial number's/batch number's status, according to the table on [this page](../../Traceability/SerialNumberBatch/bStatus.htm).

#### Configuration
If a configured part is concerned, you can see the details about the configuration by clicking this button.

#### Serial number/Batch status
If the status of the serial number/batch number means that it is blocked for usage or has a saved message for the status, this column is shown: S/B S. There you can read the message by clicking a button in the column.

#### Location
In this column you see the name of the location. For a new location, ******** will be entered by default as name, but you can change it as you please. However, you can only use 35 characters.
> It is not possible to rename a location which already has a balance.

#### Priority
The order of the locations are according to age analysis. That is, the oldest Last arrival date at the top. However, you can override the age analysis by using priority; a location with priority 1 will be placed above a location with priority 2 etc. If the location is a pick location, this will override the priority, that is, the pick locations will always be placed at the top of the table. Read more above about rules that apply for sorting of locations during withdrawal.

#### Current balance
In this column you see the current balance of the location.
On sub-rows with batch number or serial number, you see the balance of the batch or the serial number. If the batch number or serial number has a best-before date which has been passed, the balance is always displayed in red.
If the system setting called Validate best-before date is set to Block and the best-before date has passed, you see the balance in red and crossed out. This means that the balance is not available for withdrawal and an error message is displayed when withdrawing.
If that system setting is set to Warn and the best-before date has passed, the balance will not be crossed out. This means that the balance is available for withdrawal, but a warning will be shown.
The pick location’s current balance is always shown in red if the balance is below the reorder point.

#### Move stock balance
An icon shows whether a move between storage locations is possible. You can carry out the move by using a drag and drop function. It is not possible to move stock balance if there is cleared material in the location or if it is of the arrival location or pick location type. It is also not possible to move stock balance if the article has traceability activated. The Move stock balance user right is required to be able to move stock balance.

#### Cleared quantity:
Here you can see the cleared quantity in cases where there is cleared material.

#### Pick location
The system setting Apply pick location has to be activated in order for you to be able to check this setting. This setting determines if the location should be a pick location for withdrawal of a part to manufacturing order or customer order. Only one location can be pick location for the part.
If pick location is activated for the location, it is also possible to enter the reorder point in the next field and refill quantity in the following field.

#### Pick location for work center
The system setting Apply pick location has to be activated in order for you to be able to check this setting. This setting determines if the location should be a pick location for work center for withdrawal of a part to manufacturing order. Several locations can be pick location for work center for the part.
If pick location for work center is activated for the location, it is also possible to enter a reorder point and a suggested refill quantity in the following fields.
Pick location for work center is primarily intended to supply the manufacturing order/work center. Therefore, these will be placed last in the list over locations from which withdrawal should take place when needing quantity for e.g. customer order rows. Settings and search criteria for Default location in the work center register determine if the pick location for work center should be suggested when it fulfills your search criteria.

#### Reorder point
Here you can enter a reorder for the pick location.

#### Refill quantity
Here you can enter a default refill quantity for the pick location.

#### Arrival location
The system setting Apply arrival location has to be activated in order for you to be able to check this setting. This setting determines if the location should be an arrival location. Only one location can be arrival location for the part.

#### Last arrival date
This column shows the date when the most recent arrival was made.

#### Warehouse
Here you see/enter in which warehouse the location is registered. You select which warehouses you want to see by using the warehouse selector ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure. Only one warehouse is selected by default.

#### Count status
Here you see if the location is being stock counted with stock count status Under stock count (no.) or Under stock count with saved balance (no.). This is displayed in red color, where (no.) is the stock count list number. This is shown if the part has been included in a stock count list and you have updated the part status by using one of the above mentioned status alternatives. This is made in the Stock count in list procedure. If stock count is not in progress on the location, the field is empty.

#### Last stock count date
Here you see the most recent stock count date of the location.

#### Revision
Here you see the revision, if any, for the part in this location.

#### Exclude balance
Here you determine if the balance should be excluded during net requirement calculation, requirement calculation, and check delivery times. This is useful if for example the location contains overflow or wastage material that can be used but should not be considered as supply during requirements planning.
> Please note! Excluded balance does not apply to clearance, picking, stock count, and stock valuation. If, for example, a user registers a manufacturing order, the quantity on the order will be reserved against the balance even though this setting has been configured.

#### Best-before date
If traceability on BatchA batch is the set of components/products manufactured at the same time and made from the same original material. or Serial numberA serial number is a number that is used for traceability for parts on entity level. is activated as well as the Apply best-before date, the best-before date is shown for the batch's or serial number's balance.
For parts which use best-before date, the locations with the closest best-before date appear at the top in connection with stock withdrawals.
If the best-before date has passed, it is shown in red. If Block has been selected in the system settings for Check best-before date, the balance is both red and crossed out, and is also not included in the available balance.

#### More info
Under the button More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), charge number is displayed by default.
