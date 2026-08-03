### Material – Former layout
This box displays the material that are included in the selected part in the manufacturing order/manufacturing order suggestion, respectively, in the structure.
The box contains the same columns as the [Material](../../Orders/RegisterManufacturingOrder/bMaterials.htm) box in the Register manufacturing order procedure.
The column called Log can also be shown to the far left, but only if material has been reported for the operation. In that column you then see the button Manufacturing order log ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). Click this to see information about the reporting of the material for the operation.
On the function menu in this box you find the button Filter by material ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_filter.png). You can use this button to filter operations by the selected material. Then only the operations in which the material is included will be shown in the priority plan. Here you also find the button Copy records to Clipboard ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_to_clipboard.png). This can be used to copy all material in the box to a part clipboard (part selection) for further processing in other procedures.
There are three settings in this procedure that determine how the material will be shown:

#### Show only material shortages
With this setting you can decide if the material list should be filtered by shortage. Using this filter it is easy to see if there are any material shortages. The definition of shortage is when the total stock balance minus the cleared balance for other orders does not cover the remaining material requirement. For example when the balance is 100 and the material requirement is 120. Cleared material rows are not checked against shortage since they, by definition, are not considered shortages.

#### Only show material for selected operation
Default. With this setting you determine if material should only be shown for the selected operation.

#### Show location columns
Determines if location columns will be shown.
