### Subcontract information

#### Supplier
A supplier for the work center is selected here.

#### Our reference
Your own reference for subcontract purchase orders for this work center.

#### Product group
This field is only available if the Posting of subcontract purchase according to product group on setting has been configured to Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations.. If so, you can select a product group for the work center.

#### Order lead time
The number of work days before the start of a subcontract that a purchase order should be sent to the supplier.

#### Queue time
The queue time for subcontracts creates the "interval" between the previous operation's finish time and the start day of the subcontract. Subcontracts can only be planned for a day (not hourly planned), that is, the queue time is always entered as full working days. The day planning of subcontracts work in the same way as when you day plan your own work center. See Queue timeQueue time refers to time which is added to create a gap between two operations when the manufacturing order is created. It is normally stated in days, where 1 means the rest of the commenced day will be the "gap". 2 means the rest of the commenced day plus 1 full day will be the gap. For work centers with hourly planning, the queue time is instead entered in hours. The entered queue time will be added before the operation which has a value entered. described above. A subcontract can have the same start date and finish date as the previous operation.

#### Lead time
Here you enter the lead time, in work days, for the subcontract. This determines the number of days required for the subcontract. That is, the number of days between the start date and finish date. This means the lead time is the time of the actual subcontract work and it is the number of days it takes from when we ship the subcontract to when it is completed. A subcontract can have the same start date and finish date as the previous operation.

#### Other emissions
Here you can enter values for other emissions in the unit kg CO2e/h for the subcontracting work center. These values are used in sustainability calculations if no emission value is entered on the subcontract part. You should also choose one of the following calculation bases:
- Net weight – If you choose net weight as calculation basis, you have to enter a net weight for the subcontract part in the Subcontract parts procedure. If net weight is missing for the subcontract part, the net weight entered in the Part register procedure will be used instead. The calculation will be performed as follows: Net weight x Other emissions. This calculation method is, for example, useful when dealing with surface treatments/coating.
- Operation price incl. setup – This is calculated according to: (Unit price + (Setup price/Calculated qty)) x Other emissions.
- Operation price excl. setup – This is calculated as follows: Unit price x Other emissions.
- Each – The value for Other emissions will be used per item (each).

#### Create purchase order automatically
With this setting you can determine whether purchase orders should be created automatically when registering manufacturing orders. One purchase order is created per operation.

#### Do not create invoice basis
(Subcontract work center) This setting is only available if you have activated the option Purchase order (subc.) for the system setting Create invoice basis at arrival of. If you check this setting, no invoice basis will be created for this specific work center when arrival reporting purchase order (subc.).
