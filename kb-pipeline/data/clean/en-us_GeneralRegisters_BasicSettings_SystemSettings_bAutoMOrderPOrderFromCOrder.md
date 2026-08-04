### Automatic manufacturing order/purchase order from customer order

#### Create manufacturing order when creating/editing customer order
This system setting determines if the box M-order should be checked by default on the customer order row. The part must be Order oriented.
If the part is Stock driven, a manufacturing order can still be created when a customer order row is saved. In that case, the setting Allow to create manufacturing order from customer order (no link will be created) must also be activated for the part. The user can then manually check the box M-order on the customer order row. Please note! No link will then be created between the manufacturing order and customer order.
If a part should be Order oriented or Stock driven is selected in the planning setting Control method in the part register.

#### Manufacturing order number is created
This system setting determines how the manufacturing order number should be created. The available alternatives are From number series and As customer order number + position number.

#### Create purchase order when creating/editing customer order
This system setting determines if the box P-order should be checked by default on the customer order row. The part must be Order oriented and have one or more Supplier links. If the part is Stock driven, a purchase order can still be created. But then the user must manually check the box P-order on the customer order row. Please note that no link will then be created between the purchase order and customer order.

#### Include posting to purchase order
Here you determine if it should be possible to copy the customer order row's posting to the purchase order row when a purchase order is linked to a customer order row. You select for which dimensions this should apply. The posting will then be copied if the selected dimensions are set to Yes or Mandatory for the affected accounts in the chart of accounts. If there is no posting on the customer order row, the posting will be loaded from the posting matrix to the purchase order row. You can use this setting even though the setting above was not activated.
