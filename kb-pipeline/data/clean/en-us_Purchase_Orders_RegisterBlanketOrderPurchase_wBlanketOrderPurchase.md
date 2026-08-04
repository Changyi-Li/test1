## Register Blanket order - Purchase
In this procedure you register blanket orders to suppliers.
A blanket order is an order where you have an agreed quantity and price for a part for a certain period of time. Based on this blanket order you then call off quantities from the order. When a blanket order has been registered, you can register purchase orders for this blanket order. The quantity is deducted (called-off) when orders are placed and the current called quantity is shown on the blanket order. Price and discount can be copied to the call order (the purchase order). On the call order you can see to which blanket order each call is linked. When purchase order suggestions are created in the Purchase order suggestion and Stock refill – Purchase procedures, any blanket orders will be considered.
The access to the procedure is determined by user rights in the Users procedure.
You can add extra fields for this procedure in the Extra fields procedure. If such fields already have been created, these will be available under the Extra fields tab.
In the Extra fields procedure you can to add extra fields for order rows. If such fields already have been created, these will be available under the Extra fields button on order rows.
Rules for call offs from blanket order
The following rules apply to find blanket orders to make call offs from:
1. Within the validity period which is based on Order date or Delivery date, depending the selected option in the blanket order header.
2. Priority, where 1 is top priority.
3. Valid from (oldest first).
4. Valid to (oldest first).
5. Delivery date (oldest first).
6. Remaining quantity to call off (lowest quantity first).
7. Order date (oldest first).
> You cannot delete a blanket order for which calls have been made. It is also not possible to delete a row from which calls have been made.
