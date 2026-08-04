## Receiving inspection
In this procedure, you perform receiving inspections of arrived goods on order row level. You report approved and rejected quantity on these order rows. The approved parts will be transferred to stock to the location entered. The rejected parts will not be transferred to stock. In this procedure you can also value the parts on the order rows subjected to receiving inspection.
You can activate receiving inspection on suppliers, parts, individual order rows (in the Register purchase order or Arrival reporting procedure). All such order rows will be subjected to receiving inspection after they have been arrival reported. A receiving inspection can consist of different actions, for example quality controls, test runs, inspections, etc. The receiving inspection is used to determines whether an order row will be approved or rejected with a certain quantity.
Receiving inspection also applies to subcontracts. If you want to activate receiving inspection for a subcontract part, this should be done for the part in the Subcontract parts procedure or for the operation in the BOM and routing. You can also activate receiving inspection for a subcontractor and subcontract purchase order rows.
When you save the receiving inspection, the stock transaction log will become updated with the reported part and location when the approved quantity is reported. The purchase order will be updated on row level and a new status is set, depending on if a partial delivery or a complete delivery has been made from the supplier. An invoice basis and an arrival log are also created. If you have rejected a quantity, the arrival log will be updated with rejection information and the purchase order will also be updated. The remaining quantity on the order row displays the ordered quantity minus the approved quantity minus the rejected quantity. The invoice basis is also affected when items are rejected.
After having saved a receiving inspection, you can print transport labels for transfer to stock and rejection.

#### Handling of traceable parts with mandatory measuring
For traceable parts that have mandatory measuring, you will only see a warning in the receiving inspection. After this you must report receiving inspection to create batches or serial numbers. Once this is done, batches and serial numbers will be blocked for withdrawal if there are mandatory measurements to be made. When you have reported these measurements, the block will automatically be removed regardless if the measurement results in an "OK" or a "Not OK" on the rows.
Even though a serial number or batch is blocked for withdrawal, it is still regarded as a disposable balance (this way the Net requirement calculation You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. will not create "unnecessary" purchase order suggestions).
When needed, you can also manually change the status and for what the serial number/batch is blocked. This is done in the Serial number A serial number is a number that is used for traceability for parts on entity level./Batch A batch is the set of components/products manufactured at the same time and made from the same original material. procedure.
List types

#### Report receiving inspection
The list type is used to, on order row level, control and report arrived goods, and also to report measuring of the goods (if applied).

#### Valuation
After reporting, you can also print transport labels for transfer to stock and rejection. The list type is used to value arrived goods subject to receiving inspection.

#### Planned receiving inspection
In this list you see all purchase orders (including subcontract) that should undergo receiving inspection at arrival.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
