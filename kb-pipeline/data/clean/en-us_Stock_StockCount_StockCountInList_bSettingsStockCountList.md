### Settings – Create stock count basis
Here you can configure settings regarding how to select and display the parts on the stock count basis you create.

#### Stock count due date
Here you can select a date interval using the fields From date and To date. It is within this date interval the stock count in the list should be performed. The dates are calculated as last stock count date plus the part's stock count interval.

#### Show
With this setting you decide which columns to show on the document: Balance, Revision, Standard price, Batch number A batch number is a number that is used for traceability for a set of or a batch of parts. A purchased material can have a batch number that should be able to be traced back to a certain charge number from a supplier., and Serial number A serial number is a number that is used for traceability for parts on entity level..

#### Part's unit
Here you select the unit in which the parts should be stock counted; the stock count unit or the standard unit. This unit will be shown on the document.

#### Parts with stock update
Here you decide which parts should be included in the list: all parts, only parts with stock update, or only parts without stock update.

#### Include requested stock counts
With this setting you decide if parts for which Stock count request has been marked, should be included in the stock count basis, even though these parts may not be included in the regular selection.

#### Analyze suitability
Here you decide if an analysis of the parts' stock count suitability should be performed. If you choose the Sorted by suitability presentation, this setting will be activated by default. When this setting is activated, the parts' suitability is displayed using a scale of 1–4.
Explanation of suitability for stock count (1–4):
1. The part has no planned transactions.*
2. The part has planned transactions more than five calendar days ahead.
3. The part has planned transactions within five calendar days.**
4. The part has been cleared for order (regardless of date) or has planned picking (is included in a pick list).**
* By planned transactions is meant the part is either included on a registered order row (manufacturing, purchase, customer), on a pick list, or on a task to refill a pick location.
** For parts with suitability 3–4, the Detailed suitability info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) displays the cause of why the planned transactions are less suitable to be stock counted at the moment. This info is shown in the Info column.

#### Suitability
If you activated Analyze suitability, you can choose to filter by suitability, according to the above scale.

#### Name stock count basis
Here you enter a name for the stock count basis. Here you enter a name for the the stock count basis. The number and the name is shown on heading rows of the actual Stock count basis document. The name can also be used when using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature.

#### Responsible
The logged-on user is entered here by default, but can be changed.

#### Stock count status
Here you select which stock count status the parts will be given when the stock count basis is created. The stock count status will also be shown when the user loads such parts in the Part register procedure. The stock count status of the parts will be reset to None once the stock count basis is reported or deleted. The status is saved in a separate stock count table. The available status options are:
- None – With this option, no stock count status will be registered for the parts.
- Under stock count – With this option, the stock count status Under stock count will be registered for the parts.
- Under stock count with saved balance – This option will give the stock count status Under stock count with saved balance to the parts in question. The stock balance existing for each location at the moment is saved. This stock balance will then be used during the reporting as a default value. The value is also used as a reconciliation against stock transactions that have taken place after you created the stock count basis and before the reporting was made.
Examples
The stock balance in the database for a specific part's location is 10 pcs, but you physically stock count the contents of the location to 9 pcs. A withdrawal of 2 pcs is then made by another user from that location, before you have reported the stock count. The location balance in the database is then 8 pcs when you report the 9 pcs you stock counted. When you save the reporting, 9 pcs will be saved as the stock counted balance and the location's balance is set to 7 pieces. In this case, the stock count difference is −1 piece.

#### Printed by (employee)
Here you can select which employee who has printed the document. This will be shown on the printout. If you do not choose an employee here, the employee linked to the logged in user will instead be shown.

#### Pre-select "Include"
This setting determines whether or not the “Include” box should be checked by default for all rows in the list/result.
