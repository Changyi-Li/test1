### Planning window
In this box you find a planning window for the part marked in the list.
You can unpin the box and use it as a floating window. This is done using the pin ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_float_window.png) at the top right corner of the box.

#### Action
This column shows a symbol representing the action that is needed on the row. If you place the mouse pointer over the symbol you will see a tooltip regarding the action.

#### Date
In this column you see the finish date or the delivery date for a new order suggestion, rescheduling suggestion, or order.

#### Type
Depending on the order type and the planned transaction type, you will see here "Manufacturing", "Material requirement", "Purchase", "Sales", etc. in the corresponding module color. If it is a balance row, you will see the word "Balance" in black color.

#### Status
In this column you see the status of the order/order row. If you place the mouse pointer over the status number, a tooltip will show the status in text.

#### Order number
In this column you see the order number of the order/order row. It is a separate number series for suggestions.

#### Information
Here you see information regarding the suggestion. You can also see/change supplier. If you change supplier this might result in other order dates and delivery dates depending on the supplier's fixed delivery day and lead time.

#### Ordered
In this column you see the ordered quantity on the order and order suggestion. For suggestions, it is possible to edit this field.

#### Reserved
Here you can see the reserved quantity on the existing orders.

#### Cleared (C)
In this column you will see a C if the record on the row is already fully cleared. If the record is partially cleared, you will see a P here.

#### Disposable balance
In this column you see the disposable balance for each row. When you check the Apply checkbox, the order suggestion's quantity will be included in this balance. If you make changes to the Ordered column, the Disposable balance The disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. field will also be affected.

#### Start date
Here you can see the manufacturing start date for a manufacturing order suggestion or the order date for a purchase order suggestion. On a manufacturing order it is possible to change the start date. The suggested date is a calculated value dependent of the finish date and the quantity.

#### Finish date
Here you can see the finish date for a manufacturing order suggestion, or the delivery date for a purchase order suggestion/stock order suggestion. This date is possible to modify on all types of suggestions.

#### Apply
Check Apply for the suggestions that you want and click the Apply suggestion button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar of the procedure to execute the action in the marked suggestion. For example, if a purchase order suggestion is concerned, the action will be to create an actual purchase order from the suggestion.
If the part has distributed purchase by order, and there are multiple purchase order suggestions, the purchase order will be generated according to the order of the suppliers stated in the distribution. If you mark only one of the suggestions (and it is not the first suggestion according to date), a warning will be displayed ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) letting you know that purchase order will not be generated according to the part's distribution.
In the settings under the Selection tab you can enter activate that Apply should be suggested.

#### Requirement date
This date is only shown when a requirement actually occurs. The date is calculated at requirement calculation and is used on manufacturing and purchase orders.

#### Warehouse (WH)
Here you will see the warehouse to which the balance belongs.

#### Confirmed delay
An orange clock is shown in this column if the order has been confirmed as delayed.
