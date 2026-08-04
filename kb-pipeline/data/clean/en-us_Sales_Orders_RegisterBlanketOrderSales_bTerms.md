### Terms

#### Validity period
You can choose between Order date and Delivery date. Order date is selected by default. If you select order date, the customer order date must be within the validity period of the blanket order. Otherwise it will not be possible to call off from the blanket order. If you select delivery date, call offs can be made even if the customer order is registered before Valid from or after Valid to as long as the delivery date is within the validity period.

#### Valid from
Today's date is set by default. However, this date can be changed. The date set here determines when the blanket order starts to apply.

#### Valid to
Valid to is set as today's date plus the validity period that is entered for the order type. The date set here determines when the blanket order stops to apply. If you change valid to in the order header, the valid to on the order rows that have the same initial valid to date will also be changed.

#### Include in net requirement calculation
With this checkbox you decide if the blanket order should be included in the net requirement calculation. If it is not checked, the order will be excluded form the net requirement calculation. This checkbox is not checked by default. If this is checked, the blanket order will be shown with a date in the part's Planning window, and the quantity on the blanket order will affect the disposable balance for the part.
If you want the setting Include in net requirement calculation to be checked by default, you can configure this via property management.

#### Requirement date
This date is used for the net requirement calculation. You can enter any date between Valid from and Valid to, depending on when you want the blanket order's requirement to be shown.
If you wish to override this date and spread the requirement over the validity time, you can change requirement date under the Rows tab.

#### Priority
Priority of the order can be 1 to 9, where 1 is the highest priority. By default, you will see the priority that is the highest, either the customer's priority or the order type's priority. The priority field cannot be left empty for orders.
