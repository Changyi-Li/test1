### Settings – Selection (Picking plan)

#### Show delivery planned orders
The picking plan is the basis regarding which orders that should be considered ready for delivery. On the customer order there is a setting called Apply delivery planning. You find it under the Delivery rules button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). Delivery planning will only be made for the orders where this setting is activated. The corresponding settings can also be configured on the customer. If so, delivery planning will by default be made on orders to that customer.
With this setting for the list Picking plan, you can decide how you want the above setting to be taken into consideration on order.
- Orders where delivery planning is not applied – This option means that orders without delivery planning will not be shown in the list.
- Orders where delivery planning is applied – (default) This option means that orders with delivery planning will be shown in the list.

#### Show sections
With this setting you determine which sections with delivery status that you wish to show in the box Delivery status, under the Rows tab.
The following options are available:
- Ready for delivery
- Ready for delivery – Credit limit exceeded
- Ready for delivery – Unpaid advance invoice
- Waiting list
- Shortage list
- Unconfirmed
- Preliminary

#### Show orders with preliminary pick list
- Orders where preliminary pick list is not used – (default) This option means that orders where Apply preliminary pick list is not checked, will be included in the list. The balance is checked and material clearance is also made.
- Orders where preliminary pick list is used – This option means that orders where Apply preliminary pick list is checked, will be included in the list. Neither balance check or clearance is made.

#### Show text rows on the pick list
With this setting you decide if linked and/or not linked text rows (row type 4) should be shown on the pick list. Linked text rows are sub-rows to a main row of row type 1 or 2 on an order. The "not linked" text rows are separate main rows on an order. A linked text row is shown directly under the part row on the pick list. "Not linked" text rows are shown under the part rows on the pick list together with the order number to which they belong.

#### Pick list's delivery date
The pick list's delivery date is used as a planned date when all order rows on the pick list should be delivery reported. For example, if you have a truck coming certain days to collect goods, and those are the days you plan for deliveries to be made. This way, the date here overrides the planned delivery date on each order row.

#### Suggest picking of orders ready for delivery
Here you determine if orders ready for delivery will have the Pick checkbox activated by default. This checkbox is found in the Delivery status box under the Rows tab, and when it is marked it means that a pick list will be created for these orders. By default, this setting is not activated.

#### Impose a time limit on delivery horizon
With this checkbox you determine if an exception from the Delivery horizon entered for the order will be taken into consideration in the delivery planning. This setting is activated by default. It applies to orders with delivery planning and it takes the system setting Delivery horizon into consideration.
> If you have opened this procedure with the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) in Register customer order, you need to uncheck this setting and reload the list in order to get the expected result.

#### Print by order
With this setting you decide if a pick list should be printed by order. This setting is not activated by default, meaning the pick list will be printed by customer and delivery address.

#### Consider qty/pkg
Here you decide if the quantity per package should be considered when deciding if an order is ready for delivery. The following rules applies:
- When a preliminary pick list is used, a warning is displayed if the Delivered quantity is not evenly divisible by Quantity/package.
- When a "standard" pick list is used, a warning is displayed if there is a partial shortage, but a warning is also displayed if the Delivered quantity is not evenly divisible by Quantity/package.
- This warning is not displayed if the part is a fictitious part, nor for a part that is included in a fictitious part.
- The entered quantity/package in the customer link is the primary information used, and secondly it is the quantity/package entered in the Shipping section for the part.

#### Person
Here you select the person whose name will be printed below "Printout date" and "Pick date" on the document. If this field is left empty, the name of the logged in user will instead be printed on the pick list.
If you have activated the system setting Mandatory to select person when printing pick list, then you must here select a person to be able to save a new pick list.

#### Name
In this field you can name the pick list. You can use a maximum of 50 characters. If multiple pick lists are printed at the same time, then all pick lists will get the same name.

#### Assign number
With this setting you determine in which order the pick lists should be assigned pick list numbers when multiple pick lists are created. They will also be sorted in that order under the Rows tab. The options available for this setting are:
- Date and priority (This is the default option.)
- Customer and delivery address
