### Basic data
> Applies in versions up to and including 25.1.

#### Work center register
All subcontractors must be registered as work centers. If the same subcontractor performs several different jobs, for example, assembly and painting, this supplier should be registered as two different work centers for planning purposes. In other words, one work center for each type of job and supplier. In the supplier register, the Supplier role must be set to Subcontract before it can be linked to a work center.
The work center numbers should follow the same number series for subcontracts, for example, 900 and upwards.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Subcontract1.png)](../../../../Resources/Images/TrainingMaterial/Subcontract1.png)
Supplier
A supplier for the work center is selected here.
Our reference
Your own reference for subcontract purchase orders for this work center.
Product group
This field is only available if the Posting of subcontract purchase according to product group on setting has been configured to Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations.. If so, you can select a product group for the work center here.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Subcontract2.png)](../../../../Resources/Images/TrainingMaterial/Subcontract2.png)
Order lead time
The number of work days before the start of a subcontract that a purchase order should be sent to the supplier.
Queue timeQueue time refers to time which is added to create a gap between two operations when the manufacturing order is created. It is normally stated in days, where 1 means the rest of the commenced day will be the "gap". 2 means the rest of the commenced day plus 1 full day will be the gap. For work centers with hourly planning, the queue time is instead entered in hours. The entered queue time will be added before the operation which has a value entered.
The queue time for subcontracts creates the "interval" between the previous operation's finish time and the start day of the subcontract. Subcontracts can only be planned for a day (not hourly planned), that is, the queue time is always entered as full working days. The day planning of subcontracts works in the same way as when day planning your own work center.
Lead timeNumber of days between ordering date and delivery date. Normally used for purchased parts.
Here you enter the lead time, in work days, for the subcontract. This determines the number of days required for the subcontract. That is, the number of days between the start date and finish date.

#### BOM and routing
In the Operations box, in BOM and routing, there a number of fields worth noting.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Subcontract3.png)](../../../../Resources/Images/TrainingMaterial/Subcontract3.png)
Supplier
The supplier is loaded from the work center. This can be changed in the BOM and routing, or later, in the manufacturing order.
Delivery address (DA)
Here you enter the delivery address to which the supplier will send back the goods after work has been completed. The address is printed on the purchase order and delivery notes. The company’s own delivery address is shown by default. Under the button, you can uncheck Back to us and enter the customers’ or other suppliers’ addresses. It may be useful to enter the customers’ addresses when a subcontract is the final operation, and delivery is being made straight from the supplier to the customer. It can be useful to enter the addresses of other suppliers when there are several subcontracting jobs in a row, and the product can be shipped between these suppliers.
Setup cost (Setup time)
In the Setup time field, you enter a fixed setup cost for the subcontract.
Unit cost (Unit time)
In the Unit time field, enter the unit per quantity for the subcontract.
Transport cost
Here you enter the transport cost per order, for pre-calculation purposes.
Staggered prices (S)
Staggered prices can be entered if the unit price is dependent on quantity.
Queue time
If the queue time should differ from what is entered in the work center, you can change this here for the BOM and routing in question.
Instruction (I)
A text instruction can be entered under the button. This is printed on purchase orders and delivery notes.

#### Subcontract parts
The system always creates a subcontract part in the background when a subcontract is created in BOM and routing. The number of the subcontract part is created from a number series. The name is generated automatically. From BOM and routing, the main part is used as a prefix, and the operation number as the suffix. For example: "1500 - 10". You can choose whether this subcontract part number will be shown on the documents for purchase orders, delivery notes, comprehensive purchase orders, and/or comprehensive delivery notes. This is configured with the Show internal subcontract part number setting. The setting for these documents can be found in the Document settings procedure.
These subcontract parts can be managed in the Subcontract parts procedure, and you can configure different settings as well as obtain different information, such as the supplier's part number. Among other things, this procedure is used to assign a product group to the subcontract part other than that assigned to the main part. You can also assign a quantity/package to the subcontract part. Receiving inspection can be activated for subcontract parts.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Subcontract4.png)](../../../../Resources/Images/TrainingMaterial/Subcontract4.png)

#### System settings
System settings that affect subcontracts.
Default currency for subcontracts
Determines the default currency assigned to subcontracts in BOM and routing: Company currency or Supplier’s currency. However, the currency for the subcontract may be changed later.
Report material at shipment of subcontract
This system setting determines if reporting of material should be carried out at shipment of subcontract. By default, this system setting is Yes. The material will then be withdrawn on shipment. If the system setting is set to No, the material will instead be withdrawn when arrival is reported.
Use fixed delivery day on subcontracts
This system setting determines if a fixed delivery day should be used for subcontracts. The default is No. The fixed delivery day is entered for the supplier in the Supplier register procedure. The fixed delivery day is taken into account during, for example, order registration, net requirement calculation, and the calculation of new finish date.
Posting of subcontract purchase according to product group on
This setting determines if posting on order rows for subcontract purchase should be made according to the product group on Subcontract part or Work center.
Quantity on purchase order row (subcontract)
This system setting determines if the quantity shown on the subcontract purchase should be Planned quantity (M-order) or Remaining + reported quantity (M-order). When choosing the first alternative – the default setting – the planned quantity on the purchase order row will be updated if the planned quantity on the subcontract of the manufacturing order is updated. When choosing the second alternative, the planned quantity on the purchase order row is based on the subcontract's remaining quantity – and will be updated at each reporting.
Create invoice basis at arrival of
This system setting determines if a supplier invoice basis is to be created when reporting arrivals of purchase orders. In the case of a subcontract purchase, Purchase order (subc.) must be checked in the setting. You can read more about this system setting in the online help function.
