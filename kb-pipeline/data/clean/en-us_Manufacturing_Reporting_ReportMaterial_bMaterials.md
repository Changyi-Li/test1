### Material

#### Quantity to report
Here you enter the quantity of consumed material that you want to report. A warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) will be displayed if the entered quantity to report is greater than the remaining quantity. If it is traceable material then the withdrawal has to be reported under the Location button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).
Read more about [Rules for prioritizing locations at withdrawal to manufacturing order](../RulesLocationsWithdrawMorder.htm).

#### Location
Under the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see the locations registered for the part.
The location suggested for material withdrawal is primarily the one that has a cleared quantity for the order in question. If there is no cleared quantity, the system will suggest location for material withdrawal in the following order: pick location, priority, and according to age analysis (the location with oldest Last arrival date). If there are several locations for the material, and clearance has been made, you will only see the locations that have a cleared quantity for the order in question. However, you can choose to show all the locations by activating a check box. In the location window you can also reject material when reporting. You then select quantity to reject and a rejection code.
If the material has batch traceability you enter consumed quantity per location. For the location you can see batch number, best-before date (if applied for the material), and charge number from the supplier, if any (entered during arrival reporting). If the best-before date is today or in past time, the date will be displayed in red.

#### Unit
Reporting is by default made in the unit entered for the part as default unit for material withdrawals for manufacturing orders, but you can select an alternative unit if there is such a unit registered for the part.

#### Remaining quantity
Here you can enter the remaining quantity of the material that is being reported.

#### Rejected quantity
Here you can see a total of the rejected quantity that has been entered in the location window.

#### Employee
In this field you can select an employee from the personnel. This person will then be set as the executor or the person responsible for the reporting. This information will be saved in the manufacturing order log.

#### Actual reporting date
The actual reporting date will be today's date by default, but it can be changed if the material was actually withdrawn another day.

#### Stock count request
Stock count request is mainly used if you find that the stock balance does seem to add up and you wish to signal this in Monitor ERP. When you activate this checkbox, today's date and the time will be set in the Request date field.
The parts for which there is a stock count request can be shown in the Create stock count basis list in the Stock count in list procedure. This is done by activating the Include requested stock counts setting. You can also select by Stock count request date. The list also displays the comment. When the stock count has been performed and saved for the part, the field and the comment will be cleared.

#### Request comment
If you have checked the Request comment checkbox, you can here add a comment regarding the cause of this request.

#### Other information in the Material box
Information about planned and reported quantity, previously rejected quantity, and the current total balance in the warehouse to which the material is linked.
