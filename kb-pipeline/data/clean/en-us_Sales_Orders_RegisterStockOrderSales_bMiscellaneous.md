### Miscellaneous
Here you find miscellaneous information about the stock order.

#### Status
The status of the stock order can be selected manually, but certain statuses are set automatically by the system at different events. An order that is delivered in full (final delivery made) can only be edited by first changing the status to 1-5.
- 1) Registered – This is the default status for new stock order for sales that you register.
- 2) Printed – This status is given when the stock order is printed and the printout has been approved. The order will also get a printout date, and a printout log will be created per document.
- 3) Delivery time cannot be confirmed – If the delivery period cannot be determined when registering the order, you can manually change to this status. If you can not decide the delivery period it might be that important information is missing in the planning window or when printing an order list.
- 4) Picking in progress – This status is given when the delivery note has been printed and approved, or when a pick list has been created for the order in the Delivery planning procedure.
- 5) Partial delivery made – This status is given when an order row has been fully or partially delivered (delivery reported).
- 9) Final delivery made – This status is given when all order rows have been delivery reported (that is, 0 in remaining quantity). You can also manually enter status 9. Then the remaining quantity on the order row will be deleted (set to 0). On the linked purchase order the remaining quantity will then also be set to zero on these order rows. If there is no delivered quantity on the customer order, then the remaining quantity will be set to 0 on th order rows, and the purchase order will be given status 9. If there is a delivered quantity, the remaining quantity will be set to the same quantity as the delivered quantity which has not been arrival reported on the purchase order (meaning the parts that are on their way).

#### Preliminary
If you check the Preliminary checkbox, it means that the order will be marked with the text "Preliminary" across the order confirmation. A preliminary order exists in the order register and can be listed in the Order list – Sales procedure. It can be displayed in the planning window if you choose to show preliminary orders, but it is not included in the net requirement calculation. Also, a preliminary order cannot be delivered. Preliminary orders can be useful if you e.g. aim to continue working with an order later on and cannot finish it completely at the time of registration. In the Order types procedure you can decide if Preliminary order should be default for the order type.

#### Currency
The currency on the stock order is always shown in the company currency.

#### Order date
The order date is set to today's date by default. You can modify the order date for the stock order in question. The date entered here is then set by default as order date on the order rows.

#### Warehouse
Here you see the order's warehouse which is the sending warehouse. The suggested warehouse is the warehouse you are working in. It is possible to choose another warehouse except for the receiving warehouse that is selected on the main row. When you have selected a part on the order row, you can change sending warehouse by using the button Change warehouse ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png). However, you can only change warehouse as long as you have not saved the order. When you save, the linked stock order for purchase will also be created. The order's warehouse must also be linked to a supplier. This is configured for the warehouse in the Company information procedure.
