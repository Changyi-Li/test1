## Calculate annual budget
In this procedure you can create a list based on your selections made, the list is then used to calculate annual budget. The list can also be used to manually update the annual budget for selected parts. Under the Selection tab you choose which parts to load. In the list you can enter a new quantity and save the result for the selected rows.
If the option Invoicing log is selected for the setting Method of calculation, then the new quantity will be loaded from the invoicing log. The present month is not included in the calculation. If you select two months, the two previous months will be loaded (these will then be multiplied by 6 to simulate annual invoicing, please see the settings).
A record is created for the budget for the selected year, if such record does not already exist. Otherwise, the current year will be updated. When you save the budget, the following will be updated for the part: quantity, price alternative, price, and budget chart.
If you have activated the system setting called Show annual budget, annual volume, and order quantity with current pace and are saving the result to Annual budget, current pace, then data will not be saved month by month. If you save to regular annual budget, a monthly distribution will also be saved. You can either get the monthly distribution from the part or you can decide yourself which distribution to use.
If you have selected to use the part's budget chart, the data already registered for the selected year will primarily be used. Secondarily, the budget chart of the previous year will be used. Thirdly, even distribution will be used, which is budget chart 0 (zero).
List types

#### Calculate annual budget
This list type is used to calculate annual budget based on chosen selection. The list can also be used to manually update the annual budget for selected parts.

#### Reset annual budget
This list type is used to reset the annual budget for the parts where there is an annual budget registered. You can automate running of this list using Agent tasks.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
