### Delivery

#### Mandatory to select person when printing pick list
This system setting determines if a person from the personnel records must be selected in the Delivery planning procedure before you can save loaded pick lists. The name of the selected person will also be printed on the pick list.

#### Handling of credit limit at delivery
This system setting determines if a check should be made of the credit limit at delivery. The check could either result in a warning or a block for delivery reporting when a certain credit amount has been reached. This amount is entered per customer in the Customer register procedure. If you enter zero (0) then no check will be made for the customer in question.
> Order rows that are included in an invoicing plan will be excluded from this check since invoicing plans have a separate setting regarding a check for unpaid advances at the time of delivery. However, when delivery reporting is taking place, a check regarding credit limit will still be performed for rows which have been excluded from being a part of the invoicing plan.

#### Credit limit compared to
If you have activated the system setting above, then here you select to what you want to compare the credit limit. The available alternatives are Order backlog, or Order backlog + accounts receivable, Accounts receivable, or Overdue accounts receivable. Order backlog is excluding VAT and forecast rows (row type 4) are also included in the order backlog. VAT is included in accounts receivable.

#### Delivery horizon
The general delivery horizon in work days determines how far ahead in time the delivery planning in the Delivery planning procedure should be made, based on the delivery date on the customer order rows. If you enter e.g. 10, it means the delivery planning will include orders that are to be delivered during the next 10 work days. If another delivery horizon has been entered on a specific customer/customer order, then that delivery horizon applies to the customer/customer order in question.

#### Reasonability check for excess reporting in the procedure Report delivery
This system setting determines if a reasonability check for excess reporting of quantity should be made at delivery. The available alternatives are Inactive, Warn, or Block.

#### Allowed excess reporting in % of planned quantity
If the system setting above has been set to Warn or Block then this system setting will also be activated. Here you enter how much excess reporting in percent of planned quantity is allowed on the order row that is being delivery reported. If the allowed excess reporting is exceeded, you can use the system setting above to receive a warning (the order row can still be delivered) or block the order row for delivery reporting.

#### Reasonability check for deletion of remain. in the procedure Report delivery
This system setting determines if a reasonability check for deletion of quantity should be made at delivery. The available alternatives are Inactive, Warn, or Block.

#### Max. deletion of remaining allowed in % of planned quantity
If the system setting above has been set to Warn or Block then this system setting will also be activated. Here you enter the maximum deletion in percent of planned quantity on the order row that is being delivery reported. If the allowed deletion is exceeded, you can use the system setting above to receive a warning (the quantity can still be deleted) or block the quantity for deletion.

#### Setup time for picking per order row
This system setting determines the planned setup time for picking. For each order row one setup time will be added to the planning.

#### Unit time for picking per package
This system setting determines the planned unit time for picking. For each order row one unit time will be added to the planning.
Setup time and unit time for picking per order row and package are used to create loading plans for deliveries in the Delivery planning procedure in the same way as you do in the manufacturing. When delivery planning you can create a loading plan based on the number of deliveries per day, measured in package quantity and pick time. Weight, volume, and number of order rows are also displayed in that loading plan.

#### Automatic printout of transport labels in Report delivery procedure
This determines whether the Automatic printout of transport labels setting is checked by default in the Report delivery­ procedure.

#### Warn/Block if multiple users try to report delivery at the same time
This setting determines if it should be possible or not for more than one user reporting delivery of the same pick list/order at the same time. The following options are available:
- Inactive – No warning or block is shown at delivery even though multiple users are reporting on the same order/pick list. (Default option.)
- Warn – A warning will be displayed to the next user if one user is already reporting on the order/pick list in question.
- Block – A block will be displayed to the next user if one user is already reporting on the order/pick list in question.
> This setting does not apply to Monitor Mobile.
