### Purchase order in sales company
Here you configure settings for the purchase orders that can be created in sales companies when customer orders are transferred to production companies.

#### Create purchase order
The default for a new setup number is to created a corresponding purchase order in the sales company when transferring a new customer order to the production company. This setting cannot be changed. When the production company delivery reports customer order rows back to the sales company, this purchase order can be used during the arrival reporting. A link on row level to the purchase order is created on the customer order in the sales company.

#### Default purchase order type
This setting determines which order type will be set on the purchase order that is created during the transfer. Purchase order types are registered in the Order types procedure.

#### Price each
Here you determine which price each will be set on purchase order rows. The following options are available:
- According to part in sales company
- Price each according to the production company's customer order + %
The second option means that a mark-up in percentage must be entered in the setting below.
> A purchase order that is created in the sales company always gets the same currency as the transferred customer order gets in the production company.

#### Percentage
Here you enter the mark-up in percent that the production company should have if you have selected Price each according to the production company's customer order + % in the setting above.

#### Purchase order status
This setting determines which status should be set by default on purchase orders. The available options are Registered and Printed.

#### Confirmed
Here you decide if the linked purchase order automatically should be confirmed at the time it is created when the customer order is transferred to the production company.
