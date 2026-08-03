### The Material tab
Under this tab you see the material rows of the pick list you have selected.
For each material you can see order number, the manufactured part's part number (in which the material is included), part type, traceability level, quantity to report, the material's part number and name, remaining quantity, cleared quantity, the disposable balance, and the planned quantity. The fields for reported quantity and remaining quantity are possible to edit.
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you find the operation number, operation name, and work center.
Using the button Copy records to Clipboard ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy.png) you can copy either manufacturing order number or part number on the pick list to Clipboard.
Using the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) (Shift + F8) you can expand/minimize all material rows on the pick list, to see the locations registered on the parts. Locations with a zero balance are not shown.
An alternative is to only expand a single material row using the arrow button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to the left on the material row, to see the locations registered for that part.
If the material has got traceability, then you will for each location see the registered serial numbers/batch numbers, the suggested quantity to report, cleared quantity, and disposable balance. If there are multiple serial numbers/batch numbers, you will see one location row per number. For each location row you can also see best-before date (if applied for the material), and charge number from the supplier, if any (entered during arrival reporting). If the best-before date is today or in past time, the date will be displayed in red.

#### Reported quantity
Here you enter the quantity that you want to report. The value entered here is deducted from the remaining quantity. If you delete the value, it will be transferred back to the remaining quantity.
Reported quantity per location
If you expand the material row you will see the part's locations. The location for material withdrawal is suggested using the following rules: It is primarily the location that has a cleared quantity for the order/pick list in question. If there is no cleared quantity, the system will suggest location for material withdrawal in the following order: pick location, priority, and according to age analysis (the location with oldest Last arrival date).
Locations with a zero balance are not shown.
You can choose to show all locations by clicking the button Show all locations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png). Then you also see the locations which the system has not suggested for material withdrawal. This means that you, when needed, can select a different location to withdraw material from.

#### Remaining quantity
The remaining quantity of the material on the pick list.
