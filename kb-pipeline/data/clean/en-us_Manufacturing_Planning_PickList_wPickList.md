## Pick list
In this procedure you can print a document to use when you pick material from stock to a manufacturing order.
The pick list is based on manufacturing orders where there are material rows with remaining quantity. You can also load picking in progress that have unreported material rows. This is done in order to reprint pick lists or delete a picking in progress.
If a material has more than one location, you will only see the locations needed to pick the material. If you have previously performed a material clearance, you will see these locations by default. Otherwise the locations are suggested according to priority. Secondarily, age analysis will be used. If a part appears several times in the same pick list, the deduction will be made according to the requirement date, so that the material row that is needed first, is withdrawn from the oldest location. When the disposable balance of that location is zero, the material row continues to make withdrawals from the second-oldest location, and so on. For example, if the balance is 100 pieces and there are two material rows that need 100 pcs each, the system will not suggest picking from the same location for both of the material rows. However, this check is only made within the same pick list. You have to apply material clearance as a preparation to the pick list to be sure that different pick lists will not suggest picking from the same balance.
You can only create and print pick lists or load picking in progress in one warehouse at a time. You select warehouse in the toolbar.
The actual reporting which create withdrawal from stock, are made in the Report pick list procedure. Entries will also be created in the manufacturing order log and the stock transaction log.
List types
Here you select if you wish to print a new pick list or load a picking in progress. The list type also affects the selection terms available.

#### Pick list
This list type loads the material rows that have a remaining quantity in the selected manufacturing orders. You can configure a number of different settings for the pick list under the Selection tab. Under the List tab you will see the result and you can select which material to be included in the pick list. When you save, the pick list is created and is given a pick list number.
If you have installed the Tools & Maintenance option, a separate pick list will be created for the tools linked to operations on manufacturing order.

#### Picking in progress
This list type loads all pick list numbers which contains not reported material rows. Under the List tab you then select if you wish to reprint pick lists or delete a picking in progress. When you save, the pick list is then reprinted or deleted, according to the choice you made.

#### Split pick list
This list type is used to split pick lists into Order, Manufactured part, Operation, or Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations.. Under Settings you decide how to split the pick list. When you have loaded the list you can choose to create pick lists with fully cleared material, with partially cleared material, or with not cleared material.
Presentations
Here you can see the presentations that are available for the list type Pick listA pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order.. You can with these presentations choose how to group the pick list. The grouping affects the appearance of the pick list.
There are also three different documents for the pick list, based on the grouping alternatives below. In the Document settings procedure you can determine whether position number, part revision, report number, and the material's additional name, should be displayed or not on those documents.

#### Grouped by order
Using this presentation, the material rows in the pick list will be grouped by manufacturing order and part node in the structure. The sorting within the groupings are made by order and, after that, it is sorted by the material's internal relation in the structure.

#### Grouped by material
The material rows in the pick list will be grouped by the material's part number and gather all the picking needed of that material as sub-rows.

#### No grouping
Using this presentation, no grouping will be made. The sorting will only determine how the material rows will be presented.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
