### Material
This box displays a material list with the material which is included in all operations for the selected part in the structure map of the manufacturing order. If you select an operation in the structure map, the Material box will only display the material to that specific operation, as long as the operation has incorporated material, otherwise, the box will be empty.
By clicking the button Add new row at the end (F5) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) you can add material at the bottom of the material list. You can select a part number, enter the operation for which the material will be used, and the quantity to report.
In the Material list you will also see information about the material's part number, name, part type, planned and reported quantity, for operation, disposable balance, and cleared quantity.

#### Quantity to report
Here you enter the quantity of consumed material that you want to report. A warning will be displayed if the entered quantity to report is greater than the remaining quantity. If it is traceable material then the withdrawal has to be reported under the Loc. button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).
Read more about [Rules for prioritizing locations at withdrawal to manufacturing order](../RulesLocationsWithdrawMorder.htm).

#### Location (Loc.)
Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see the locations registered for the part.
The location suggested for material withdrawal is primarily the one that has a cleared quantity for the order in question. If there is no cleared quantity, the system will suggest location for material withdrawal in the following order: pick location, priority, and according to age analysis (the oldest location). If there are several locations for the material, and clearance has been made, you will only see the locations that have a cleared quantity for the order in question. However, you can choose to show all locations by clicking the button Show all locations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png) on the function menu in the box. In the location window you can reject material when reporting. In order to do that, select the quantity to reject and a rejection code.
If the material has batch traceability you enter consumed quantity per location. For the location you can see batch number, best-before date (if applied for the material), and charge number from the supplier, if any (entered during arrival reporting). If the best-before date is today or in past time, the date will be displayed in red.

#### Unit
The part's standard unit is used by default when reporting, but you can select an alternative unit if such has been registered for the part.

#### Remaining quantity
Here you can enter the remaining quantity of the material that is being reported.

#### For operation
For added material rows you can change the operation for which the material is used.

#### Employee
In this column you can select an employee from the personnel records. This person will then be set as the executor or the person responsible for the reporting. This information will be saved in the manufacturing order log.

#### Actual reporting date
Here you can see the actual reporting date. It is set to today's date by default, but it can be changed.

#### Stock count request
Stock count request is mainly used if you find that the stock balance does seem to add up and you wish to signal this in Monitor ERP. When you activate this checkbox, today's date and the time will be set in the Request date field.
The parts for which there is a stock count request can be shown in the Create stock count basis list in the Stock count in list procedure. This is done by activating the Include requested stock counts setting. You can also select by Stock count request date. The list also displays the comment. When the stock count has been performed and saved for the part, the field and the comment will be cleared.

#### Request comment
If you have checked the Request comment checkbox, you can here add a comment regarding the cause of this request.
