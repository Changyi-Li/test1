### The list Subcontract document
In the list you will see information about subcontracts which can be reported as shipped and for which you can print subcontract documents. Operations where purchase orders have not been created yet are also shown in the list. They are shown without data in the Purchase order number column. The operations in the same grouping on a supplier will end up on the same purchase order if Include is checked when the list is saved.
The list shows information about each subcontractor. For each subcontract the list displays all necessary information. You also see information about the previous operation P and the material availability M (same as in the priority plan). In systems where the Tools & Maintenance option is installed, you see the tool availability T. This means you see if the tool is cleared or not. You can update Quantity and Finish date for the subcontract.
The Function menu
By using the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) (Shift + F8), you can expand/minimize the grouping of the list by supplier.
By using the button Finish date as today + lead time ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_clock.png), you can set the finish date for all the operations in the list to today’s date plus lead time. This is useful if you shipped the goods late to the supplier. The finish date might even be in past time.
By using the Replan the entire order button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replan_order.png), you can, when changing the planned date on a subcontract, choose if only the subcontract or the entire manufacturing order should be replanned.
Using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can go to different related procedures for the selected operation. You can for example go to the Pick listA pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. procedure via the link, to create a pick list if the subcontract contains traceable material.

#### Include
Subcontracts where Include is checked in the list will receive a purchase order number, if they don’t already have one. All operations will be reported as shipped if that setting has been activated in the Selection tab.

#### Quantity
In this column the quantity to report is suggested based on the setting Suggested quantity under the Selection tab. This quantity is possible to change. If it is traceable material which should be reported, this is shown with a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png). To report traceable material you should use the link ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) to get to the Pick list procedure and perform the reporting there.

#### Finish date
In this column you can see the finish date of the subcontract. If you change the finish date, the Replan order checkbox becomes activated, see below.
> The finish date will also be saved in a separate date field for the operation which is only used in order to measure the delivery reliability for subcontracts. That field will not replan the operation or purchase order in any way. The field is in this context then called Requested delivery date.

#### Replan order
This checkbox becomes activated by default if the finish date is changed, but you can also make exceptions and uncheck it if the order should not be replanned. When the Replan order checkbox is marked it means the purchase order, the subcontract, and also the subsequent operations, will be replanned.
With the system settings Replan finished operations when replanning orders and Replan previous operations when replanning orders from an operation you decide if finished operations and previous operations should also be replanned.
