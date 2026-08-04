## Shipment list
In this procedure you can create lists of registered shipments and sign receipt for picked-up shipments.
The lists are used to view:
- Status
- Shipment number
- Package
- Shipping agent
- Sources of information
- Other information
By using the button Goods tracking ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_url.png) on the function menu in the lists, you can also track goods for the marked shipment in the list via the shipping agent's shipment number. The goods tracking search takes place via nShift.
List types

#### Standard
With this list type, a standard list of shipments is loaded. In the presentation you can choose if the period interval for the shipments should be displayed by day, week, month, quarter, or year.
If the shipping agent in the shipment has Other selected as plugin for export (configured in the supplier register), then it is possible to change Status between Registered, Booked/Printed, and Shipped for a saved shipment. The purpose is to be able to manually change status when shipments are to be exported via a software other than nShift Delivery or nShift Web-TA. When using nShift Delivery or nShift Web-TA, the status in the shipments is assigned automatically.

#### Source of information
This list type loads a list of the sources of information.

#### Receipt list
This list type displays information about shipments to be picked up and you can use the list to print the shipment receipt document. You leave the shipment receipt document to the driver. The driver can sign the document. The list can be updated making it possible to mark the shipments as picked up in the system (and not only on the printed document).
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
