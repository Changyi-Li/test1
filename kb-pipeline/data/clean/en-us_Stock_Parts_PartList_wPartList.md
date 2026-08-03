## Part list
In this procedure you can load different lists with the complete part register or parts of it in order to see and update different information for multiple parts at a time. You can also print part lists.
The different list types handle different data in the part register. The standard list contains the most data for the parts. You can also load lists containing parts based on, e.g., customer links, supplier links, planning settings, stock balances.
To update data on the parts you make the list Updateable ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_list.png) (Ctrl + U) before you load it on screen.
List types

#### Standard
This list type is a standard list of the parts. It is possible to make the list updateable and you can modify most information on the parts. The list can present data based on different areas in the Part register; General, Purchase, Sales, Manufacturing, and Shipping.

#### Block/Notify
This is a list containing blocks and messages for the parts.

#### Customer links
This is a list containing the parts' customer links. It is possible to make the list updateable and you can modify most information. It can be presented as grouped by part or by customer.

#### Supplier links
This is a list containing the parts' supplier links. It is possible to make the list updateable and you can modify most information. It can be presented as grouped by part or by supplier.

#### Planning
This list type displays the parts' planning information and planning settings. It is possible to make the list updateable and you can modify all of the information items and settings for the parts.

#### Default transfer profile
In the list you see the transfer profiles per part. For each part you can choose if transfer using profiles should be allowed. You can also enter a standard profile (per part) for transfer.
The list is available in systems where the Customer order transfer option is used.

#### Stock balance
This list shows the parts' stock balances. The list presents balances per location, balance per location with traceability, or balance per part.

#### Location settings
In this list you can update location settings for different parts.

#### Clearances
In this list you will only see parts for which clearances have been made. A clearance can e.g. be made for manufacturing order, customer order, pick list for manufacturing, or pick list for customer order. Incorrect clearances can be removed.

#### Translations
In this list you can handle translations made for part names and additional names.

#### Other part identities
In this list you can see different part identities entered for the parts. A part can have several registered part identities.

#### Expenses
In this list you can see different mark-ups such as purchase expenses for parts. It is possible to make the list updateable in order to modify these expenses. The expenses shown here are the expenses which have been set as active under the Expenses tab in the Calculation mark-up procedure.

#### Traceability settings
In this list you can configure traceability settings for parts.

#### Allow automatic withdrawal
Here you can allow automatic stock withdrawals during different reporting items. This is made per part.

#### Administer customer links
In this list you can delete multiple customer links.

#### Administer supplier links
This list can be used to update/modify information in the supplier links on multiple parts. This corresponds to what you can modify per part in the Supplier links box in the Part register procedure. You can also use the list to delete supplier links.

#### Replaced parts
In this list you see phased out parts and obsolete parts, and you can update these with replacement parts.

#### Receiving inspection
In this list you can update receiving inspection.

#### Distributed purchase by order
In this list you can update which suppliers in the distributed purchase that should be purchased from next.

#### Distributed purchase by percentage
In this list you can update the percentage of distribution between suppliers in distributed purchase.

#### Alternative part
In this list you can update alternative parts. The list contains parts which have been registered in the system as alternative parts, that is, they can replace the regular part when there is a balance shortage.

#### Stock and manufacturing – Packaging properties
This is only available in systems with the Advanced stock management option. In this list you can update packaging parts and packaging part dimensions linked to parts.

#### Part units
The Part units list type is used to display all parts along with their units. In this list it is possible to search, filter, and when needed, you can also update how the units are used for each part.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
