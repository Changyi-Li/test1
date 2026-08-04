### Rows
Here you configure settings for customer order rows on customer orders that are created in the production company when the customer order is transferred from the sales company.

#### Position number
This setting determines whether position numbers should be transferred from the sales company to the production company. Rows with status 9 Final delivery made in the production company are not affected. The following options are available:
- No (default)
- Yes, replace only unlocked
- Yes, replace unlocked and locked

#### Name
Here you determine which part name should be entered on order rows (row type 1) in the production company. This also controls the extra name and parts' sales comment between the companies. The following options are available:
- According to sales company's customer order row
- According to production company's part.
This applies if the system setting called Include part's additional name as text row on customer order/quote has been set to Yes:
- If the option According to sales company's customer order row is selected, the part's additional name in the sales company will be used on the text row (row type 4), both in the sales company and in the production company.
For additional order rows (row type 2), the name will always be loaded from the sales company's order row, regardless of this setting.

#### Unit
Here you determine which unit should be used on order rows (row type 1) in the production company. The following options are available:
- According to sales company's customer order row
- According to production company's part.
For additional order rows (row type 2), the unit will always be loaded from the sales company's order row, regardless of this setting.

#### Price each
Here you determine how the production company should price their order rows (row type 1). This setting overrides the price strategy configured for the order type set on the production company's customer order. The following options are available:
- According to customer in the production company
- According to customer's price list in the production company
- Standard price in the production company + % – Please note! This applies when orders are handled by the sales company. If changes and additions are made in the production company, price management is always used according to the order type’s price strategy.
- According to sales company customer orders - % – Please note! This applies when orders are handled by the sales company. If changes and additions are made in the production company, price management is always used according to the order type’s price strategy.
- Price strategy on order type in production company
For additional order rows (row type 2), the price each will always be loaded from the sales company's order row, regardless of this setting.
> In other words, there are some differences in how prices are handled for "regular" parts and for parts with a configuration. Configured parts will always be given a price according to the order type’s price strategy. "Regular" parts will be priced according to this setting.

#### Percentage
Here you enter the percentage that should apply when an alternative with percent has been selected in the setting above.

#### Discount
Here you determine which discount should be entered on order rows (row type 1) and additional order rows (row type 2) in the production company. The following options are available:
- None
- Customer in the production company
- Sales company's customer order – If multiple discounts have been added to the sales company’s customer order, the total discount is transferred to the production company’s customer order and Discount 1.
> For configured parts, the discount is loaded from the configurator according to the included parts’ customer link or the customer’s general discount even if the Customer in the production company option is selected.

#### Setup price
Here you determine which setup price should be used on order rows (row type 1) and additional order rows (row type 2) in the production company. The following options are available:
- None
- According to customer in the production company
- According to sales company's customer order.

#### Delivery date
Here you determine which delivery date should be calculated and entered on order rows in the production company. The following options are available:
- Empty
- According to sales company's customer order row
- According to sales company's customer order row - Production company's part's lead time.
The transport time entered for the customer in the production company can also affect the delivery date. This applies to the customer used for the sales company from which an order is loaded. The transport time affects the delivery date if the alternative According to sales company's customer order row is selected for the Delivery date, and if the Transport time Transport time is the number of work days that it takes to send a shipment from sender to a receiver. setting in the Header box has the Sales company's customer number in the production company selected. This way, the handling of delivery date at customer order transfer will be the same as when manually handling orders, for a corresponding order.
You cannot use the option called According to sales company's customer order row - Production company's part's lead time for additional order rows (row type 2). If you select this option, the delivery date will still be assigned according to the sales company's order row.

#### Standard price
Here you determine which standard price should be used on order rows (row type 1) and additional order rows (row type 2) in the production company. The following options are available:
- According to sales company's customer order row
- According to production company's part.
You cannot use the option called According to production company's part for additional order rows (row type 2). If select this alternative, the standard price will be zero on the production company's order rows.

#### Revision
Here you determine which revision should be entered on order rows (row type 2) in the production company. If the sales company's revision is not registered in the production company, an error message appears and nothing will be transferred. The following options are available:
- According to sales company's customer order row
- According to production company's part.
For additional order rows, this field will always be empty on order rows in the production company.

#### Drawings
Here you determine which drawing/s should be entered on order rows in the production company. The following options are available:
- According to sales company's customer order row
- According to production company's part.

#### Desired delivery date
Here you determine which desired delivery date should be entered on order rows in the production company. The following options are available:
- Empty
- According to sales company's customer order row
- According to sales company's customer order row - production company's part's lead time.
You cannot use the option called According to sales company's customer order row - Production company's part's lead time for additional order rows (row type 2). If you select this option, the desired delivery date will be entered according to the sales company's order row.

#### Initial delivery date
Here you determine which initial delivery date should be entered on order rows in the production company. The following options are available:
- Empty
- According to sales company's customer order row
- According to sales company's customer order row - production company's part's lead time.
You cannot use the option called According to sales company's customer order row - Production company's part's lead time for additional order rows (row type 2). If you select this option, the initial delivery date will be entered according to the sales company's order row.

#### Net weight
Here you determine which net weight should be used on order rows (row type 2) in the production company. The following options are available:
- According to sales company's customer order row
- According to production company's part.
You cannot use the option called According to production company's part for additional order rows (row type 2). If you select this option, the net weight will be entered according to the sales company's order row.

#### Dock – Row
This setting determines whether Dock – Row should be transferred when a customer order is transferred from the sales company to the production company’s customer order. No is selected by default in this setting.
If this is set to Yes and if the customer order in the sales company has a value, it is this value that transferred to the production company’s customer order.
If set to No, nothing will be transferred to this field on the production company’s customer order.

#### Dock description
This setting determines whether Dock description should be transferred when a customer order is transferred from the sales company to the production company’s customer order. No is selected by default in this setting.
If this is set to Yes and if the customer order in the sales company has a value, it is this value that transferred to the production company’s customer order.
If set to No, nothing will be transferred to this field on the production company’s customer order.

#### Storage
This setting determines whether Storage should be transferred when a customer order is transferred from the sales company to the production company’s customer order. No is selected by default in this setting.
If this is set to Yes and if the customer order in the sales company has a value, it is this value that transferred to the production company’s customer order.
If set to No, nothing will be transferred to this field on the production company’s customer order.

#### Kanban number
This setting determines whether the Kanban number should be transferred when a customer order is transferred from the sales company to the production company’s customer order. No is selected by default in this setting.
If this is set to Yes and if the customer order in the sales company has a value, it is this value that transferred to the production company’s customer order.
If set to No, nothing will be transferred to this field on the production company’s customer order.

#### Reference number for manufacturing
This setting determines whether the Reference number for manufacturing should be transferred when a customer order is transferred from the sales company to the production company’s customer order. No is selected by default in this setting.
If this is set to Yes and if the customer order in the sales company has a value, it is this value that transferred to the production company’s customer order.
If set to No, nothing will be transferred to this field on the production company’s customer order.

#### Reference number for delivery
This setting determines whether the Reference number for delivery should be transferred when a customer order is transferred from the sales company to the production company’s customer order. No is selected by default in this setting.
If this is set to Yes and if the customer order in the sales company has a value, it is this value that transferred to the production company’s customer order.
If set to No, nothing will be transferred to this field on the production company’s customer order.

#### Show unlinked text rows on document
With this setting you decide if rows of row type 4 should be transferred from the Sales company to the Production company. The button called Show on the following documents on the row of row type 4 on the customer order in the Sales company, will determine on which documents the text rows are displayed.
- Show on all documents – This option means that the text rows will be displayed on all documents.
- Show on selected documents – This option means that the text rows are only displayed on the document types marked in the Sales company.

#### Block changes of manufacturing orders at following status or higher
With this setting you decide if manufacturing orders can be automatically replanned in the production company when the sames company modifies quantity or delivery date on a transferred customer order row. You can select one the following status options:
- Registered
- Printed
- Started
- Finished
Please note! Changes made in configurations on order rows in the sales company will NOT automatically update created manufacturing orders.
It is therefore important to always Synchronize with BOM and routing for the affected manufacturing orders when making changes to a configuration on rows where manufacturing order has been created.
