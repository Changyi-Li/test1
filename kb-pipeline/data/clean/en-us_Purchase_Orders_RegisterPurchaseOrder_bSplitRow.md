### The Split row dialog
If you have selected the option Split, with dialog in the system setting Function of “Split row” button in Register purchase order, the Split row dialog will be shown and you will be given multiple options for how the splitting will be performed.

#### Base on order row
- Position – shows the original row’s position.
- Quantity – shows the quantity on the original row. If the setting Deduct quantity from original row is checked, you can see what the resulting quantity on the original row will be.
- Remaining quantity – shows the remaining quantity on the original row.
- Delivered quantity – shows the delivered quantity on the original row.
- Delivery Date – shows the delivery date on the original row.

#### New order row
- Quantity – Here you enter the quantity for the new row.
- Delivery Date – Here you enter the delivery date for the new row. The same date as on the original row is suggested by default.
- Position – If the order has the status Registered, the position cannot be edited. If the order status is Printed or higher, the position can be edited. The standard value suggested by default depends on the system setting Position on new row when splitting order row.
Position
Registered
Printed
Position on new row when splitting order row
- If the setting is configured to Same as on original row and the order has the status Printed or higher, the suggested position number will be the same as on the original row.
- If the setting is configured to Calculate new position, the suggested position number will be empty.
- If the position field is left empty, the system will calculate a new position when the new row is created.
- If you enter manually enter a position in the Position field, that position will be used on the new row that is created.
- Deduct quantity from original row – Not checked by default.
Deduct quantity from original row
- If the setting is not checked, the quantity on the original row will remain as it was initially.
- If the setting is checked, the quantity on the original row will be adjusted so that the quantity on the new row is deducted from the quantity on the original row. If the original row is partially delivered, it is not possible to enter a quantity for the new row which is larger than the remaining quantity on the original row. (In order to enter a larger quantity, you need to uncheck this checkbox.)
> If you delete a split row, the quantity on the original row will be restored.
