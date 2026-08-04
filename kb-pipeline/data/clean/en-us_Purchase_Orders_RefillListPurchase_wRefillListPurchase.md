## Stock refill – Purchase
The procedure Stock refill – Purchase is used to calculate which parts should be purchased based on the part's reorder point. By default only parts with the planning method Stock refill will be shown.
Normally, you check if the current balance plus registered orders, is less than the part's reorder point. In this procedure you then create purchase orders when you choose to generate purchase orders based on the suggestions created in the calculation. Stock orders are also created in this list regardless if the part is manufactured or purchased.
The procedure uses different calculation formulas which are included as standard. You find these in the Planning formulas procedure. In that procedure you can also create your own formulas and then select them here prior to the calculation.
In the list you can see information from the linked supplier as well as information from the part register and registered orders. Prior to generation of purchase orders you can:
- Change supplier.
- Change price.
- Edit posting.
- Change quantity to order.
- Change delivery date.
Distribute purchases between suppliers
If distributed purchase per order is applied for the part, the suggestions for the suppliers are strictly created according to the settings in the part’s distribution and will go from top to bottom among the suppliers. Click the Distribute purchase button under the Purchase tab in the Part register procedure, to access where you configure distributed purchase for a part.
If the part has distributed purchase between different suppliers, this distribution will be used when the suggestions are created.
> Select by the part template called Consumable tool if you want to calculate stock refill for consumable parts.
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
