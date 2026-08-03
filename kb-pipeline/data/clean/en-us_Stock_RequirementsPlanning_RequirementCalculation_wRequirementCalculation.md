## Requirement calculation
In this procedure you can analyze the planning window for individual parts and get suggestions of actions; in this case order suggestions. This way you can avoid time shortage and shortage in quantity. You can also get suggestions on orders that are unnecessary early (rescheduling suggestion – out) and also orders that are unnecessary since the planned refill of stock does not correspond to any shortages.
The requirement calculation is based on the part’s stock balances, orders, and planning settings. The suggestions you get in the list can be turned into actual manufacturing and purchase orders. It is also possible to update existing orders concerning time. In addition to the suggestions you get, you can also manually add your own suggestions. You can also divide an order suggestion into several. For purchase order suggestions you can change supplier, quantity, and date.
First you select a range of parts. When you load the data, the parts become analyzed. Under the List tab you see the suggestions possible to modify. The suggestions marked here are the ones which will be turned into actual orders when you click the Apply suggestion button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png). Orders for manufacturing are opened in the Register manufacturing order procedure. There you can edit the order and save it. When you turn the suggestion into a purchase order by clicking the Apply suggestion button, a window will open where you can update the order. By using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can open the Register purchase order procedure with the order in question loaded.
> If you have installed the Tools & Maintenance option you can also include tools in the requirement calculation by adding the selection row Part template in the backstage of the procedure.
List types
Standard

#### This list is sorted by part number with one row per part. The values you see in the list are totals for the parts for the period, and also for the order types you selected.
Grouped by supplier

#### This list is grouped by supplier with the relevant parts in each section. Only parts of the type Purchased are grouped by supplier. Parts without supplier are placed under the heading Supplier is missing. Grouping is made on the default suppliers in the parts' supplier links.
Grouped by administrator

#### This list is grouped by administrator with the relevant parts in each section. Parts without administrator are placed under the heading Administrator is missing.
This list is grouped by administrator with the relevant parts in each section. Parts without administrator are placed under the heading Administrator is missing.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
