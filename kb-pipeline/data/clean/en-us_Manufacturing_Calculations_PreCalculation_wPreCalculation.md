## Pre-calculation
The main purpose of this procedure is to perform a financial calculation of manufacturing cost, cost price and sales price for product structures. Costs consisting of material, sub-contracted work, and own work are added together to a total manufacturing cost.
The calculation model is a so-called mark-up calculation. This means that you add mark-ups based on costs to calculate cost price and sales price. You can create pre-calculations after you have created BOM and routings for the parts.
In the section [Calculations](../../../GeneralRegisters/BasicSettings/SystemSettings/bCalculations.htm) under the Manufacturing tab in the System settings procedure, you find settings which affect pre-calculations.
Read more about how [precalculations](../../../UserGuide/Using/Calculation/Precalculation.htm) work under Using Monitor in the online help function.
Alloy cost
In this procedure you can also calculate and add alloy cost to calculations and look at already made calculations that have been saved. In the BOM and routing you decide which materials that are included in a part. These included materials might have alloy codes which are handled in the procedure Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part. Under the Purchase tab in the Part register procedure you can specify which alloy cost that should apply when purchasing the part (the material).
In this procedure you load the parts (for which you want to calculate the alloy cost) to the list. You select the rows you wish to include in the calculation run. Under the Summary tab you will see a summary of the alloy cost per part. This is possible to save.
List types

#### New calculation
This list type is selected by default. In this list type the procedure is set to perform new pre-calculations for the parts that you select to the list.

#### Existing calculation
This list type shows pre-calculations that are already saved for the parts. No calculation or update of calculations is made in this list.

#### Calculate alloy cost
This list type allows you to calculate an alloy cost based on the product structure. The alloy cost will be aggregated and saved for the main part.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
