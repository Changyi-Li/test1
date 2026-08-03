## Calculate annual volume
In this procedure you can reset, calculate, and save annual volumes for selected parts.
Data can be loaded in different ways and the saving is made to either the annual volume or the annual volume, current pace. Each type of calculation in the procedure is divided in different list types.
In the Settings box you select from where the annual volume should be loaded, terms for the explosion, and the price types. You can automate running of the procedure via the Agent option.
List types

#### Update annual volume
This list type loads the calculated quantity for the annual volume for main parts. The list is used either to manually update the annual volume or to calculate a new quantity by selecting something in the table Load annual volume from in the Settings box.

#### Calculate annual volume – Detailed
This list type is a combination of the two lists called Update annual volume and Explosion. The list loads saved annual volume for main parts and in the next step you start a calculation with structure explosion in order to calculate the annual volumes also for the included/incorporated parts.
In this list you also see setup times and unit times in charts per work center or department.

#### Explosion
This list type loads saved annual volume and in the list you can run a calculation with structure explosion in order to calculate the annual volumes for the included/incorporated parts.

#### Loading
This list type loads saved annual volume and performs an analysis of how much manufacturing capacity which is required in order to manufacture this in the different work centers. This can then be saved as an annual volume for each work center.
> Please keep in mind that structure parts will be exploded, making the include/incorporated parts also have an annual volume. If you add the included/incorporated parts in the selection, this means the volume for the incorporated parts will be double.

#### Simulation
This list type is not possible to update. This list type is used to get an explosion and a calculation of the loading in the same run. This way you can, for example, simulate how much raw material will be consumed and how much loading is created for manufacturing x pieces of some complex/compound products. This simulation is not saved.

#### Calculate expenses
This list type is used to calculate and analyze purchase expenses and mark-ups based on a selected volume of purchased parts and price type. In the list you can run a calculation with structure explosion based on the selections you have made for the list and the quantity. During the structural explosion, expenses are calculated for each purchased part based on the quantity.
The total annual volume is used to calculate total expenses per type on each part. Furthermore, the number or orders is also calculated, as well as number of packages and number of kg for the calculated volume.

#### Reset annual volume
This list type is used to set the annual volume to zero for the selected parts.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
