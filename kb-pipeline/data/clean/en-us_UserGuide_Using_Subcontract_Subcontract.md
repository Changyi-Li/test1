## Subcontract

#### The new subcontract work flow
In version 25.2 a new work flow for subcontracts was launched. This means several important changes. If you use subcontracting, we recommend that you review these changes to ensure a smooth transition and continued efficient work.
Watch the video on the new subcontract work flow.
| Swedish | English |
|---|---|
|   |   |

#### Important changes
- Purchase orders are created in the Subcontract documents/Shipped procedure. If the setting called Create purchase order automatically is activated for the work center, purchase orders can be created in the Register manufacturing order procedure.
- New settings in the Subcontract documents/Shipped procedure.
- Comprehensive purchase order is no longer available. Instead you can combine multiple operations to generate/create a single purchase order.

#### Important information if you are using adaptations
If you have adaptations that are linked to subcontract purchases and/or shipment of subcontracts, you should pay extra attention to the changes that the new process entails. For example, you may become affected by:
- Purchase orders not being created automatically when registering manufacturing orders.
- Document adaptations for comprehensive purchase order or comprehensive delivery note are not needed since these documents are no longer available.

#### Benefits of the new subcontract handling
- You can choose how purchase order rows should be grouped. You can group by operation, supplier, project, work center, or manufacturing order.
- More efficient communication with suppliers (when a supplier is carrying out multiple operations on your behalf).
- You can include XML-files in Monitor-to-Monitor, now also for orders containing multiple operations.
- You can send a "Modified purchase order" when you have made a change to a date or a price.
- Since there is only one purchase order, the order/invoicing process becomes easier for the supplier.
- Since there is only one purchase order and no comprehensive purchase order, it is also easier to link supplier invoices.
Additional improvements will be presented in future versions.

#### Questions and answers
- What will happen with my subcontract purchases on manufacturing orders already created?
- Purchase orders that are already shipped (status > 2) will not be affected. However, the purchase orders which have only been registered (status 0-1) will be deleted. This is done to make it possible to create comprehensive purchase- for already registered manufacturing order operations.
-    
How do I report arrival for comprehensive purchase orders which have already been shipped to my supplier/subcontractor?
- The collective/comprehensive number (available in earlier versions of Monitor ERP) can be searched for in the Goods label field for orders which were created in a previous version of Monitor ERP. In the Report arrival procedure you can add a goods label under the selection rows in backstage. Another way is to arrival report for the included purchase order numbers or manufacturing order numbers.
- Can I arrival report a subcontract purchase without first having to create the purchase order?
- No, you first have to create the purchase order via the Subcontract documents/Shipped procedure.
- Can I create subcontract purchase orders without reporting them as shipped? 
- Yes, in the Subcontract documents/Shipped procedure you will find the Report shipped setting which you can uncheck. By doing this you can create subcontract purchase orders for one or several manufacturing orders without reporting them as shipped.
- If I have activated approval on purchases, will I be affected by these changes?
- Yes, potentially. As subcontract purchases are created in connection with shipping, you may need to check that the user doing the shipping is registered in the General approval settings procedure, as well as checking the authorization limit for the user.
- Is the subcontract part used in the same way as before?
- No, the part number for the manufactured part will now always be the one used on the purchase order. The part number for the manufactured part will be an additional order row (row type 2).
- Is it possible to change supplier when I have a shipped quantity "At supplier"?
- No, you must first undo the shipment. Or, you can arrival report the quantity that is “At supplier”. After that, you can change the supplier.

#### Subcontract in Monitor ERP
A subcontract is an operation in a manufacturing order that is purchased by an external supplier. The work center linked to the operation must be classed as Subcontract. The supplier linked to the work center must be assigned the Subcontract supplier role. Material supplier is standard, although a supplier can be configured to be both a material supplier and subcontractor.
To create Subcontract­ purchase orders, the subcontract documents/Shipped is used. Here, you can select which operations should be grouped with order rows on a purchase order. For example, operations belonging to the same project with the same shipment date should be grouped on the same purchase order.
The order can be printed or e-mailed to the supplier.
When printing subcontract purchase orders and delivery notes, you can choose to print the shipped quantity in the document, rather than the planned quantity. This is controlled via a document variant. This document variant can also be set as default for the supplier (supplier-specific documents).
Orders relating to subcontract purchases are confirmed in the same way as regular material purchases. If the date is updated in connection with confirmation of the purchase order, the system asks whether the entire manufacturing order should be re-planned in accordance with the new delivery date for the operation to which the subcontract purchase refers.
When the goods are to be sent to the supplier, the shipment can be reported, in order to keep track of what has been sent, and not returned.
