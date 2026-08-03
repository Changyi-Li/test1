## Work center list
In this procedure you can load lists to see and update data in existing work centers.
For the list types that are possible to update, you can activate this function by using the button Updateable ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_list.png) on the toolbar.
It is not possible to add new rows in the form of schedule cycles or cost factors.
The validation from the Work center A work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register is also included in the list. It makes sure for example that the number of machines per order cannot exceed the number of machines in the work center.
List types

#### Standard
This list type shows information that only exists in one set for work centers. This list type does not show information about work centers of the type Pool and Subcontract.

#### Costs
This list type shows information about the work center's costs. This list type does not show information about work centers of the type Pool and Subcontract.

#### Production schedule cycles
The list shows information about the work centers’ schedule cycles. This list type is only available if you have activated the system setting called Enable hourly planning for work center.

#### Subcontract
This list type shows information about work centers of the type Subcontract. You can e.g. enter suppliers, lead times, and references.

#### Exceptions
This list type shows exceptions made per work center. If there are saved exceptions from basic time or from number of machines for a work center, it will be shown in the list. This list type does not show information about work centers of the type Pool and Subcontract.

#### Annual volume
In this list type you can enter planned annual volume for the work center. In the list you can for regular work centers manually update setup time, unit time, total time, and man-hours. For subcontract work centers, it is possible to edit the costs.

#### Default location/pick location
In this list type you can update default locations/pick location for the work center. A work center can have more than one default locations/pick locations.
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
