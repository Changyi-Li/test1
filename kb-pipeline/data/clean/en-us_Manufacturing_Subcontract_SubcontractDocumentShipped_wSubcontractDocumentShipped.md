## Subcontract documents/Shipped
In this procedure:
- You create subcontract purchase orders and report subcontracts as shipped.
- You can print subcontract documents such as purchase orders, delivery notes, and transport labels for the shipping of subcontracts.
- You can attach a Monitor-to-Monitor XML file to make it easier for your suppliers to register orders.
When you create a purchase order, you can choose if 1 purchase order should be created per operation or if multiple operations should be grouped together on the same purchase order, and then you can also choose between different way to group them.
In addition to printing documents, you can also report shipped quantity in this procedure. The shipped quantity will then be reported for the operation on the manufacturing order. The shipped quantity will also be recorded in the manufacturing order log.
From the Result box found under the Documents tab, you can also create a shipment for the subcontracts which have been marked to include. A shipment draft with all of the information pre-filled is then created in the Register shipment procedure.
If you have material linked to the subcontract that is shipped, it is possible to report these if you have set the system setting called Report material at shipment of subcontract to Yes.
Read more about [Subcontract](../../../UserGuide/Using/Subcontract/Subcontract.htm) under Using Monitor in the online help function.
The system setting called Log outgoing e-mail determines whether or not e-mails sent from this procedure should create a log record under the Activities tab in the Register purchase order procedure.

#### How to handle traceable material
At present, there is no handling of traceability via subcontracts. Traceable material should therefore be handled by linking it to other operations, for example, a special operation for material reporting.
List types

#### Subcontract document
With this list type you load subcontracts for which you can then see information about, report, and print, in the form of purchase order, delivery note, and transport label for subcontract shipments.

#### Reprint – Subcontract document
Using this list type you handle printouts of already printed and approved subcontract documents.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
