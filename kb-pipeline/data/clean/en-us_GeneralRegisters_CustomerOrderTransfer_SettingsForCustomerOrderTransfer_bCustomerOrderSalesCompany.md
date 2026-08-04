### Customer order in sales company
Here you find settings for customer orders that are transferred for the first time from the sales company to the production company.

#### Transfer preliminary order
This setting determines if preliminary orders should be transferred from the sales company. If you select No you can add/delete rows, modify and save the order without transferring it to the production company. This applies as long as the order is preliminary. When you deselect Preliminary on the order, it will be transferred the next time you save the order.
> If you want to work with preliminary customer orders, this can be determined by an order type. In the Order types procedure, you check the box Preliminary if the order type should be preliminary by default. This can also be configured via Property management in the Register customer order procedure. There you can set that the Preliminary box should always be checked on new customer orders.
Please note! Order rows on a customer order can have different transfer profiles. The setting retarding transferring preliminary order can only be activated for some transfer profiles. You can configure transfer profile on order rows manually on an order row or automatically via the part's default transfer profile. Such order rows will be transferred even though the customer order is preliminary.

#### Transfer order rows with the following requirement types
With this setting you decide which order rows should be transferred to the production company referring to the contents of the Type of requirement column. The following alternatives are available:
- Fixed order
- Manufactured
- Buy material
- Forecast
When you transfer order rows with type of requirement set to Forecast, a purchase order row will NOT be created in the sales company for the order row in question When Type of requirement is later changed to Fixed order, the purchase order will be created.

#### Update remaining qty from production company
With this setting you decide if a deleted remaining quantity on the customer order row in the production company should be transferred to the customer order row in the sales company. In cases where the production company delivers directly to the end customer, and the sales company's customer order and purchase order is automatically reported, then it is necessary to have this setting set to Yes.

#### Block changes from production company at following status or higher
With this setting you decide at which order status the customer order rows in the sales company will no longer be possible to change if changes are transferred from the production company. The most common case is that the customer order rows will be blocked for editing after the order confirmation has been printed, that is, when the order has been given status 2 in the sales company.

#### Standard price for remotely configured parts
Here you decide which standard price should be saved to customer order rows for remote configured parts. Prices for both alternatives are loaded from the production company. The following options are available:
- Calculated standard price in production company – This option means that a pre-calculation is made for the configuration in the production company and its manufacturing cost is loaded to the sales company’s customer order row.
- Price each from production company's customer order – This means that the production company’s standard prices of the included/incorporated options in the configuration are added together and are loaded to the sales company’s customer order row.

#### Percentage
Here you enter a mark-up (in percent) for the option you selected for the standard price in the setting above.

#### Replace internal comment
This system setting determines whether the sales company’s customer order’s internal comment will be replaced with the production company’s customer order’s internal comment.
If this setting and the corresponding setting in the Production company tab are both set to Yes, the internal comment can be used to send information between the companies.

#### Document path, internal comment
Here you can select where files transferred from the production company's customer order’s internal comment should be saved.

#### Show text for remote configured parts on documents
This setting determines which documents remote configured parts’ text rows will be shown on. The following options are available:
- Quote
- Order confirmation
- Delivery note
- Invoice
- Pro forma Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees. invoice
