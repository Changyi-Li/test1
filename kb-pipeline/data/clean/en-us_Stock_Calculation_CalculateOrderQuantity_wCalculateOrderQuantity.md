## Calculate order quantity
This procedure is used to calculate the part's order quantity. The purpose is to calculate a quantity that will minimize the cost of stock-keeping and purchasing. This quantity is later used for requirements planning and calculations. The calculated order quantity can derive from the following:
1. Wilson formula
2. Number of orders per year
3. Part's minimum quantity
4. Minimum consumption
5. Maximum consumption
Depending on how you configure different settings, the calculations are made according to the following principles: The greatest value of alternative 1, 2, and 3 is compared with alternative 4 or 5. If the greatest value of 1, 2, and 3 is less than alternative 4, the calculation is made according to alternative 4. If the greatest value of 1, 2, and 3 is greater than alternative 5, the calculation is made according to alternative 5.
The Order quantity and Order quantity, current pace can be updated. The calculations are automatically made when the list is loaded. Then you save the rows that you have selected.
The list is based on part data (planning settings).
Calculation basis
Here you can see a description of the calculation bases that are used to calculate the order quantity in the procedure.
AV=Annual volume
HC=Interest
OC=Ordering cost
Part value=Read more about part value in the [List](tList.htm) section.

#### Wilson formula
OKW=√((2*OC*AV)/(HC*part value))

#### Number of orders per year
OKA=AV/Number of orders per year
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
