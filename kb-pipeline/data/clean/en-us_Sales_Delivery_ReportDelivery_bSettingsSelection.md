### Settings

#### Actual delivery date
Today's date is entered by default in this field, but it can be changed. If you select a date which is more than two days ahead or back in time from today's date, a warning is displayed.

#### Show delivery planned orders
Only for the Free selection list type. The picking plan is the basis regarding which orders that should be considered ready for delivery. On the customer order there is a setting called Apply delivery planning. You find it under the Delivery rules button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). Delivery planning will only be made for the orders where this setting is activated. The corresponding settings can also be configured on the customer. If so, delivery planning will by default be made on orders to that customer.
With this setting you can decide how you want the above setting to be taken into consideration on order.
- Orders where delivery planning is not applied – This option means that orders without delivery planning will not be shown in the list.
- Orders where delivery planning is applied – (default) This option means that orders with delivery planning will be shown in the list. This setting makes it possible to deliver customer orders where delivery planning is applied and pick list has not been printed.

#### Person
Here you select the person that is performing the delivery reporting. This information is saved in the delivery log. If the field is empty, the user of the procedure will be registered as the person who is reporting.

#### Suggest quantity
With this setting you decide which quantity to suggest to delivery on customer order rows. Depending on the selected list type, the following alternatives are available:
- Remaining quantity – (list type Free selection) With this alternative, the quantity remaining after picking will be suggested.
- Disposable balance The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. – (list type Free selection) With this alternative, the disposable balance that is available will be suggested. However, it will never suggest more than the remaining quantity on the order row.
- Quantity in pick list – (list type Via pick list) With this alternative, the quantity that has been picked will be suggested.
- Zero (0) – With this alternative the suggested quantity will be set to zero (0).
If the system setting Check if balance is negative during reporting has been set to Warn or Block, then Disposable balance option will be suggested in this setting when using the list type Free selection. If that system setting is deactivated, Remaining quantity will be suggested instead.
If you have parts with traceability you want to delivery report and you have selected the list type Free selection, then no quantity will be suggested for delivery, regardless of the alternative selected for this setting.

#### Only include order rows with remaining quantity
If you activate this setting, only order rows which have a remaining quantity will be displayed. If you have not activated this setting, you will also see order rows with zero as remaining quantity.

#### Show only main rows
This checkbox determines whether or not only main rows should be displayed. Related sub-rows in form of additional texts, alloy costs, etc. are not shown. If you delivery report a main row, the related sub-rows that are hidden will also be delivery reported. The setting does not apply to sub-rows of fictitious parts. These are always displayed regardless of whether this setting is activated or not.

#### Sort by main location
Applies to he Via pick list list type. Here you decide if the rows should be sorted by the parts' main location instead of customer order number and position. This box is not checked by default. By activating this setting, the rows will be sorted in the same way as in list type Picking plan in the Delivery planning procedure. Rows of row type 2 will be sorted in after rows with row type 1. Unlinked rows of row type 4, will be sorted in last in the list, grouped per order number. They are then sorted within the group by the sequence of the order.

#### Show package related warnings
Applies to he Via pick list list type. With this setting you decide if warnings which occurred when packing pick lists, should be shown in the list. This setting is only relevant if you apply packing in Monitor ERP. This means you use the procedure Pack for delivery between delivery planning and delivery reporting.
