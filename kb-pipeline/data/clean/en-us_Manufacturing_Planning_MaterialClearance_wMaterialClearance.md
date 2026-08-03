## Material clearance
In this procedure, you can make sure that all material that is needed for a manufacturing order, part, or operation, is available for clearance and you can also perform the clearance.
The material clearance is based on the material rows of manufacturing orders and on the locations, balances, and previous clearances of the parts. A check is made of the remaining material requirement on the order by comparing it to the disposable balance and previously cleared quantity. If the available quantity is greater than the requirement, the material can be cleared. This means that a certain quantity of the disposable stock balance on the locations is "earmarked" for the manufacturing order so that no other orders can make withdrawals from that balance. At a later stage when the material is reported, the system will automatically suggest withdrawal from the locations where the clearance was made.
If you have chosen that order oriented M-parts should be included in the clearance, their availability is checked via the reported quantity on the part node in the order structure. The clearance is then saved as usual on the locations which the specific manufacturing order is linked to.
Clearance and pick location
When a part has a pick location, the clearance affects the total balance and not the specific pick location's balance. This means you can save the clearance regardless of the pick location's balance. This is not applied on parts with serial number traceability.
Optimization of clearance
The same material is usually used for several manufacturing orders. Therefore, you can optimize a complete/full clearance using a setting in the procedure. This means that if a material that is needed for order X is cleared, but some other material for order X is not available, then the material in question will be released to other orders that would become completely cleared. If there are several other orders that need the same material, they are prioritized according to the following main principle:
1. Priority of operation.
2. Requirement date.
3. Priority of order.
4. Order ID.
If there are no other orders that would become completely cleared if the material for order X is released, the clearance remains and the order is placed in section 2) Some material available in the Clearance status box under the Clearance tab. The purpose of a clearance is that as many orders, parts or operations as possible can be placed in section 1) With all material available.
If there are parts in the clearance that belong to orders where "coordinated processing" is applied, then all material for all the parts that are coordinated has to be available for the clearance to be performed.
In the Clearance status box you see everything that can be cleared. Under the Shortage list tab, you see the material that have to be refilled in stock in order to cover a shortage.
You can perform material clearance by order, by part, or by operation. You can only perform material clearance in one warehouse at a time. Warehouse is selected in the toolbar of the procedure.
An alternative function to the Material clearance procedure is Clear material directly in the [priority plan](../PriorityPlanning/bPriorityPlan.htm) box in the Priority planning procedure. However, using this function you will not see material that has a shortage.
List types
Here you select list type. The list type determines if you perform material clearance at order level, part level, or operation level. The selected list type also partly affects the available selection terms.

#### Material clearance – By order
Using this list type, the clearance is performed at order level for all the material in the selected orders. One order per row is displayed in the Clearance status box under the Clearance tab.

#### Material clearance – By part
The clearance is performed at part level for all the material to each part node in the selected orders. One part per row is displayed in the Clearance status box under the Clearance tab.
The parts on the orders are divided in sections in the Clearance status box:
- Section 1 – With all standard material available
- Section 2 – With all mtl available, if alternative material is used
- Section 3 – With some material available
- Section 4 – No material available

#### Material clearance – By operation
Using this list type the clearance is performed at operation level for all material to the operations in the selected orders. One operation per row is displayed in the Clearance status box under the Clearance tab.
The order number is shown in bold font on the rows in the affected sections, if the operations of an order in the box Clearance status are divided in one of the sections (see above).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
