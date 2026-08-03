## Manufacturing order suggestion
In this procedure you load a list of manufacturing order suggestions created for manufactured parts during net requirement calculation. You can also load lists with rescheduling suggestions of orders.
You can turn the suggestions in the list into actual manufacturing orders or replan existing orders timewise, for the suggestions where the Apply checkbox are checked. It is also possible to change the quantity and date. Conversion of suggestion to order is done using the button Generate/Replan manuf. order ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) (Ctrl + R) on the toolbar of the procedure.
Another function in the list is to load unnecessary orders (orders without requirement) and delete these as long as they are not started.
The net requirement calculation is based on the part’s stock balances, orders, and planning settings.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
What to consider when selecting
If you, for example, have added a selection row for manufacturing order number in this procedure, rows for other manufacturing orders will also be shown in the list, not only the selected order number. This is because the selection needs to consider all future events (orders) and not only the selected order number to be able to calculate rescheduling suggestions. The entire planning window must be loaded before the calculation can provide an accurate result. This applies even though you did not choose (in the settings) to display order suggestions for rescheduling.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
