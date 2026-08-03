### Stock count table
In this table you can report the parts you have stock counted. You can report several parts at a time on separate rows in the table.

#### Part
Here you select the part from the part register that will be stock counted.

#### Name
The part name is primarily shown in the language that is currently used in the system and secondarily in the company language.

#### Part type (T)
In this column you can see the part type illustrated with a symbol. When you hover over the symbol, a tooltip will display the part type in text form.

#### Current balance
Here you can see the balance on the location. This balance can be displayed with two to six decimals.

#### Stock counted balance
Here you enter the location's new counted stock balance that is being reported. This balance can be entered with two to six decimals.

#### Unit
In this column you will by default see the unit selected to apply during stock count of the part. It is possible to change unit if the part has more than one unit. The current stock balances are displayed in the selected unit.

#### Location
Here you can see the location that is being stock counted. You can also add more locations using the Add location button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_subrow.png) or by pressing Shift + F5. It is also possible to rename a location by entering a new location name.
> It is not possible to rename a location which already has a balance.

#### Suitability
Here you see how suitable this part is to be stock counted right now, depending on the transactions in the near future.
Explanation of suitability for stock count (1–4):
1. The part has no planned transactions.*
2. The part has planned transactions more than five calendar days ahead.
3. The part has planned transactions within five calendar days.**
4. The part has been cleared for order (regardless of date) or has planned picking (is included in a pick list).**
* By planned transactions is meant the part is either included on a registered order row (manufacturing, purchase, customer), on a pick list, or on a task to refill a pick location.
** For parts with suitability 3–4, the Detailed suitability info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) displays the cause of why the planned transactions are less suitable to be stock counted at the moment. This info is shown in the Info column.

#### Batch
Here you see the batch number of the part on the location. If there are more than one batch number on the same location, these will be shown on separate rows.

#### Current total balance
In this column you can see the current total balance for the part in question. It is a total of the balances on all locations. This balance can be displayed with two to six decimals.

#### Stock count date
Here you can see the part's stock count date. Today's date is entered by default, but it can be changed. If a stock count has been previously made on the location, you cannot select a stock count date that is earlier than the location's Last stock count date.

#### More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### Type
In this column you see which type of location is concerned, for example a pick location.

#### Actual date
Here you enter/see the date when the arrival is made or physically took place. By default, no date will be displayed.

#### Last stock count date
Here you see the location's last stock count date. You cannot select an earlier Stock count date than this date.

#### Last stock count quantity
Here you see the quantity reported at the most recent location stock count.

#### Revision
Here you see the part's revision. The revision can be edited.

#### Basic type (B)
Here you see the basic types of the tool. It is illustrated with a symbol. When you hover over the symbol, a tooltip will display the basic type in text form.

#### Serial number
Here you see the serial number of the part on the location. This serial number is a unique number, unlike the batch number which can be common for several entities. Each serial number is displayed on a separate row in the table.

#### Pick location
With the checkbox in this column you decide if the location should be a pick location. The system setting Apply pick location has to be activated in order for you to be able to check this setting. If pick location is activated for the location it is also possible to update the reorder point in the next field.

#### Pick location for work center
Here you determine if the location should be a pick location for work center.

#### Reorder point
Here you can enter a reorder point for the pick location.

#### Refill quantity
Here you enter a default refill quantity for the pick location.

#### Arrival location
Here you determine if the location should be an arrival location. The system setting Apply arrival location has to be activated in order for you to be able to check this setting. It is possible to activate both pick location and arrival location for a location.

#### Comment
Using this button you can add comments for the stock count in the last column of each row.
