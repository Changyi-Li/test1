### Settings – Selection

#### Actual arrival date
Today's date is entered by default, but it can be changed. If you select a date which is more than two days ahead or back in time from today's date, a warning is displayed.

#### Person
Here you enter the employee number of the person who performs the reporting. You can select among all persons in the personnel records. It is possible to enter which person is performing the arrival reporting.
It is common that several persons who work with arrival reporting share the same user in the system Here you enter the person who actually perform the arrival reporting.
The selected person is saved in the logs and is shown on the transport label. If you leave the field Person empty here, the Person field in the log will also be empty. However, in the User field you see the logged-in user.

#### Delivery note number
Here you enter the supplier’s delivery note number. This will then be displayed under the Rows tab and saved on the invoice basis. The system setting Mandatory delivery note number at arrival determines whether or not you must enter the supplier’s delivery note number.

#### Shipment number
Here you enter the number of the shipment. This will then be displayed in the list and saved on the invoice basis. The system setting Mandatory shipment number at arrival determines if you must enter the shipment number.

#### Suggest quantity for material row
Here you determine how quantity on order rows should be handled during arrival reporting. If it is a subcontract, the setting Suggested quantity for subcontract below will also be taken into consideration.
- Zero (0) – With this alternative, the suggested quantity will be zero (0,00).
- Remaining quantity – With this alternative the suggested quantity will be set to the remaining quantity on the row.

#### Suggest quantity for subcontract
When arrival reporting subcontracts with remaining quantity there are different quantities to suggest for arrival reporting, unlike regular purchase orders:
- Zero (0) – With this alternative, the suggested quantity will be zero (0,00).
- At supplier – With this alternative the suggested quantity will be set to the quantity at the subcontractor (that is, the shipped quantity minus the previously arrival reported quantity).
- Remaining quantity – With this alternative the suggested quantity will be set to the remaining quantity of the operation/purchase order (that are the same).

#### Suggest quantity for stock order
This setting is available if you have the option Warehouse. For stock orders purchase with remaining quantity there are different quantities to suggest for arrival reporting (to the receiving warehouse), unlike regular purchase orders.
- In transit – With this alternative the suggested quantity will be set to the quantity that has been delivered reported in the sending warehouse and that has not yet have been arrival reported (that is, parts being transported).
- Zero (0) – With this alternative, the suggested quantity will be zero (0,00).

#### Only include order rows with remaining quantity
With this setting you decide if only order rows which have a remaining quantity should be shown in the list.

#### Show only main rows
With this checkbox you determine whether or not only main rows should be displayed in the list. Related sub-rows in form of additional texts, alloy costs, etc. are not shown. If you arrival report a main row, the related sub-rows that are hidden will also be arrival reported. The setting does not apply to sub-rows of fictitious parts. These are always displayed regardless of whether this setting is activated or not.
