### Automatic purchase order from manufacturing order

#### Create purchase order when manufacturing order is created/edited
This system setting determines if a purchase order should be created automatically when a manufacturing order is created/edited. The alternatives are: Yes, default; Yes, optional, and No.
- No – If you select this alternative, the function will not be available on manufacturing orders in the Register manufacturing order procedure. The system setting below is also inactive.
- Yes, optional – If you select this alternative, the function will not be activated on manufacturing orders. However, this can be activated manually in the Register manufacturing order procedure. A purchase order is created when you save the manufacturing order.
- Yes, default – If you select this option, the function will be activated by default on manufacturing orders in the Register manufacturing order procedure, and a purchase order is created when the manufacturing order is saved. If the function is deactivated on the manufacturing order, no purchase order will be created when the manufacturing order is saved. If the manufacturing order is created from a customer order, the purchase order will be created automatically when the manufacturing order is created.

#### Update goods label on purchase order from manufacturing order
This system setting determines if the manufacturing order number should be loaded to the Goods label field in the purchase order header. The purpose of this system setting is that the supplier should label the goods so that your goods receiving department easily can see to which manufacturing order the arrived material belong.
