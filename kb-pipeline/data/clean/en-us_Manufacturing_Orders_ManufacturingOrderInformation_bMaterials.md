### Material
This box displays the material that is included in the selected part in each respective manufacturing order in the structure.
The box contains the same columns as the [Material](../RegisterManufacturingOrder/bMaterials.htm) box in the Register manufacturing order procedure. Read more about these columns in the online help function for that procedure.
The Supplied column is shown if New finish is activated in the settings for the Net requirement calculationYou use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts.. Then a supply date will be calculated for the material when performing the net requirement calculation. The supply date means the date when the material on the manufacturing order is supplied by a purchase order, stock order, or manufacturing order.
The Diff. (Days) column shows if New finish is activated in the settings for the Net requirement calculation. The column shows the difference between Reservation date and Supplied.
The column called Log can also be shown to the far left, but only if material has been reported for the operation. In that column you then see the button Manufacturing order log ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). By clicking the button you find information about the reporting of material for the operation.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the function menu, you can go to related procedures for the marked material row.
On the function menu you also find the Copy records to Clipboard button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy.png). This can be used to copy all material in the box to a part clipboard (part selection) for further processing in other procedures.
There are three settings in this box which determine how the material will be shown:

#### Show only material shortages
With this setting you can decide if the material list should be filtered by shortage. Using this filter it is easy to see if there are any material shortages. The definition of shortage is when the total stock balance minus the cleared balance for other orders does not cover the remaining material requirement. For example when the balance is 100 and the material requirement is 120. Cleared material rows are not checked against shortage since they, by definition, are not considered shortages.

#### Only show material for selected operation
With this setting you determine if material should only be shown for the selected operation.

#### Show location columns
This checkbox determines if the locations that are planned to be used for the material on the order should be shown, meaning the locations that have planned withdrawals for this order. If there are multiple locations, these are shown under the Location button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).
