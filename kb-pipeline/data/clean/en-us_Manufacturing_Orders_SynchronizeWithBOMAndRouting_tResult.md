### Synchronize

#### Include
With this checkbox you decide if the manufacturing order on the row should be included in the synchronization check, the update of preliminary order, and finally saved. If there is a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) on the order you have to manually check the checkbox if you want to include the order. A tooltip is shown when you hover over the symbol, displaying the cause of the warning.

#### Revision
Here you can choose to change revision on the part in the manufacturing order.
A check is made to see if the part's status or revision differs from the manufacturing order. If you select a revision where it differs from the order, then the manufacturing order will become unchecked in the Include column and it will not be included in the synchronization. It is still possible for you to included these rows, but then these revisions will be displayed in blue.

#### Status
In this column you can change part status of the part in the manufacturing order.

#### P-order
Here you decide if a purchase order should be created.
> You can change Status, Revision, and you can create linked purchase orders, even though these modifications will not affect operations or material rows.

#### Nodes, Operations, Material, Tools
For the Nodes, Operations, Material, and Tools* columns, there are sub-columns where you can see quantity per row for:
- S – Selected
- N – New
- C – Changed (not available on nodes)
- D – Deleted
* The Tools column is available if the Tools & Maintenance option has been installed.
How different statuses on orders are handled
Depending on the status of the manufacturing order, changes and deleting are handled in different ways. The system settings Automatic withdrawal of material, Automatic reporting of tools plus the work center settings Exclude from automatic reporting of material and Exclude from automatic reporting of tools, affects the result of the synchronization.
Below it is described what applies for nodes, operations, material, and tools, when these should be added, deleted, or changed.
Nodes
Addition of new higher node
- Status on node: Registered, Printed, or Started.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- If there is material which is already reported, you can still add a node.
Deletion of higher node
- Status on node: Registered, Printed, or Started.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- Material and nodes on other material rows can be reported.
Deletion of node
- Status on node: Registered or Printed.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- Reported quantity on all materials = 0.
Deletion of underlying node
- Status on node: Registered or Printed.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- Reported quantity on all materials = 0.
> It is possible to turn a node into a material by deleting the node row but leaving the material row. It is not possible to delete the material row and leave the node row.
Changing of node
Changing of part type means that nodes, operations, and/or material/tools are deleted and added. There are rules for this.
In certain cases, existing operations' setup times and unit times will also be updated. Terms for when these times can be updated are found under Change of operation/subcontract.
| From | To | What happens in BOM and routing? | Synchronization | Note: |
|---|---|---|---|---|
| Manufactured | Purchased | The node disappears and becomes a material row. | Deletion of node.
The material row remains. | - |
| Manufactured | Fictitious | - | Deletion of node.
Addition of material.
Addition of operations.
Updating of operation times. | A |
| Purchased | Manufactured | The material row becomes node. | Addition of node.
The material row remains. | - |
| Purchased | Fictitious | The material row becomes fictitious node. | Deletion of material.
Addition of material.
Addition of operations.
Updating of operation times. | A |
| Fictitious | Manufactured | - | Addition of node.
Deletion of material.
Deletion of operations.
Updating of operation times. | B |
| Fictitious | Purchased | Fictitious node disappears. | Deletion of material.
Addition of material.
Deletion of operations.
Updating of operation times. | B |
Note:
1. The material rows of the fictitious part are added and/or existing material's quantity is updated. The operation rows of the fictitious part are added and/or existing operations' times are updated.
2. The material rows of the fictitious part are deleted and/or existing material's quantity is updated. The operation rows of the fictitious part are deleted and/or existing times are updated.
A node's comment, drawing, and files, can be changed as long as the status of the node is registered, printed, or started.
In the procedure you see if a part's revision or part status has been changed. If a node's revision or part status is updated, this will affect the BOM and routing only if there is alternate BOM and routing which takes revision into consideration. Then it is about adding or deleting operation rows or material rows.
Operations
Addition of operation/subcontract
- Status on node: Registered, Printed, or Started.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- If there is material which is already reported, you can still add an operation.
Deletion of operation
- Status on node: Registered, Printed, or Started.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- If the operation has material (reported or not) linked to it, then you cannot delete the operation.
- If there only is one operation, you cannot delete it.
Deletion of subcontract
- Status on node: Registered, Printed, or Started.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- If the operation has material (reported or not) linked to it, then you cannot delete the operation.
- If there only is one operation, you cannot delete it.
- Purchase order cannot have been sent.
- When deleting subcontract, the purchase order will also be deleted.
> If you have printed a purchase order for another subcontract in the node, but it has not been shipped/sent or been arrival reported then it is possible to delete the operation.
Change of operation/subcontract
- No rescheduling/replanning in time.
- Status on node: Registered, Printed, or Started.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- For subcontracts, purchase order cannot have been sent.
- The reported quantity of material linked to changed operation = 0.
It is possible to change:
- Operation number
- Operation name
- Supplier (subcontract)
- Delivery address (subcontract)
- Setup time
- Unit time
- Overlap Overlap is abbreviated to OL, and is entered as a percentage. This allows two operations to overlap in time when a manufacturing order is created. Overlap is entered as a value that indicates how much of the current operation should remain when the next operation can begin. Any queue time on the subsequent operation means that overlap is ignored.
- Queue time Queue time refers to time which is added to create a gap between two operations when the manufacturing order is created. It is normally stated in days, where 1 means the rest of the commenced day will be the "gap". 2 means the rest of the commenced day plus 1 full day will be the gap. For work centers with hourly planning, the queue time is instead entered in hours. The entered queue time will be added before the operation which has a value entered.
- Fixed lead time
- End customer on order
- Instruction
- Files
- Supplier's part number (subcontract)
- number of machines/persons per order
- Setup quantity
- Extra %
Material
Addition of material
- Status on node: Registered, Printed, or Started.
- Status on the operation of the material: not reported.
- Recording status on the operation: not in progress.
- If there is material which is already reported, you can still add new material.
Deletion of material
- Status on node: Registered, Printed, or Started.
- Status on the operation of the material: not reported or started.
- Recording status on the operation: not in progress or in progress.
- The material is deleted if reported quantity = 0.
- If other material rows (which are linked to the same operation) are reported, then a material row can still be deleted.
- If other material rows in the node are reported, a material row can still be deleted.
Change of material
- No rescheduling/replanning in time.
On a material row it is possible to change:
- Quantity
- For operation
- Instruction
- Files
- Position number
- Setup quantity
- Extra %
- Revision (is not included in the BOM and routing but is compared to the part's active revision).
For all of the items above, the following apply:
- Status on node: Registered, Printed, or Started.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- Reported quantity of changed material: 0.
When changing the quantity, a check is made to see if the material row is a node or not. If the row is not a node, you are allowed to change the quantity as long as the material is not reported.
If the material row is a node then you are allowed to change the quantity as long as the node and the underlying nodes are not in progress or reported. The quantity is also updated for the underlying nodes.
Tools
Adding of tools
- Status on node: Registered, Printed, or Started.
- Status on the operation of the material: not reported.
- Recording status on the operation: not in progress.
- If there are reported tools, you can still add new tools.
Deletion of tools
- Status on node: Registered, Printed, or Started.
- Status on the operation of the tool: not reported or started.
- Recording status on the operation: not in progress or in progress.
- The tool is deleted if reported quantity = 0.
- If other tool rows (which are linked to the same operation) are reported, a tool row can still be deleted.
- If other operations in the node are reported, a tool row can still be deleted.
Changing of tools
- No rescheduling/replanning in time.
-   
No replanning of Quantity per cycle
-   
No replanning of Cycle time Cycle time is the productive time in the operation in which the unproductive time is not included. Cycle time plus Ineffective time adds up to the unit time for an operation.
On a tool row it is possible to change:
- Quantity
- For operation
- Instruction
- Files
- Position number
- Setup quantity
- Extra %
- Revision (is not included in the BOM and routing but is compared to the part's active revision)
-   
Returning operation (for reusable tools).
For all of the items above, the following apply:
- Status on node: Registered, Printed, or Started.
- Status on all operations: not reported.
- Recording status on operations: not in progress.
- Reported quantity of changed tool = 0.
When changing the quantity, a check is made to see if the tool row is a node or not. If the row is not a node, you are allowed to change the quantity as long as the tool is not reported.
