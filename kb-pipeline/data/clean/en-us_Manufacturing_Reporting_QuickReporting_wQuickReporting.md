## Quick reporting
In this procedure you can report multiple manufacturing orders at order level after that the orders are started or completed.
The procedure is based on manufacturing orders and their structures, operations, and material. The reporting is made for operations, included material, and nodes, that is, underlying structure parts.
Three different lists are found in the procedure:
- A list for quick reporting of operations and material.
- A list for reporting remaining quantity.
- A list for deleting remaining quantity.
There are settings you can use to select if both quantity and time should be included in the reporting of operations. In the list for quick reporting you can also delete remaining quantity.
In the procedure you report the planned time of the operations for the quantity you enter at order level in the list. For the material, you report the planned included quantity multiplied by the quantity entered at order level in the list. In other words, no post-calculation difference can occur on time for operations and on quantity for material when quick reporting. However, if the prices for material or worked hours have changed since the order was registered, you will see a price difference in the post-calculation. The price at the time of reporting is shown as reported price in the post-calculation.
When you perform the reporting, the transfer to stock and withdrawal from stock become saved in the stock transaction log and in the manufacturing order log.
> Please note! Subcontracts in manufacturing orders cannot be reported in this procedure. Subcontracts are reported in the Report arrival procedure. Material with traceability on any part in the structure, cannot be reported in the procedure. These reporting items should be made in the procedure Report manufacturing order. You can delete remaining on a manufacturing order in the procedure. This is possible even though the incorporated/included material is traceable.
List types

#### Quick reporting
In this list you report manufacturing orders with the quantity you enter. One row per manufacturing order will be displayed in the list.

#### Report remaining
In this list you always report manufacturing orders with remaining quantity on all levels. One row per manufacturing order will be displayed in the list.

#### Delete remaining
In this list you can delete the remaining quantity on all levels of the manufacturing order. One row per manufacturing order will be displayed in the list.
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
