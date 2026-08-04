### Priority plan
In this box you see the priority plan for the work center. It shows all operations for the work center in all manufacturing orders. By default the operations are sorted by their planned start date. At the top of the priority plan you will find the operation that has the earliest planned start date. If you have entered a priority on operations, then the sorting is primarily made by priority and secondarily by start date.
For the marked operation you will see the same information as under the Priority plan tab in the Manufacturing order info procedure. The information which concerns the part is loaded from the part register.
> A corresponding priority plan is also available in the Recording terminal procedure in the Time recording module. That priority plan is intended for machine operators and is based on the work center or report number selected by the operator. An operator can there select which work items (operations) to start, report, and stop. These functions are available if the Work recording option is installed. In addition to work recording, the recording terminal also contains functions for attendance recording.
The buttons available on the function menu of the priority plan are:
- Go to procedure – Using this button you can link to different relevant procedures and there open the affected manufacturing orders for the selected operation. You can also select multiple operations by activating the checkbox Include.
- Copy records to Clipboard – Using this button you can copy all the affected parts or manufacturing orders in the priority plan to the Clipboard.
Print – Using this button you open a dialog for printing of shop packet (traveler, operation document, material document). Operations where Include is checked will be included in the Clipboard. You print by clicking the Direct printout button in the dialog.
The work center can have default settings for printing of the order documents in a shop packet, number of copies, and printing of linked files. But these can be changed temporarily in the dialog window by using the Print shop packet button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png).
You can configure how and when order documents and linked files should be printed. On a general level this is decided with the system setting called Print linked files. The corresponding setting for printing of linked files can also be configured per user in the Users procedure.
- Filter by material – With this button you can filter by material for the selected operation. Only operations with the same material as the selected operation will then be shown. It is the material in the column Mtl part no. in the priority plan. You can also filter by material by using text search for part number, name, part code, and part category. Here you can use special characters as wild cards:"_" and "%". This is applied if you wish to find all operations that, for example, have a material of a certain sheet metal thickness (often shown in the name) when the material does not necessarily have the same part number. It can also be used if you wish to filter by a material that is not the first in the material list. You can save filters and name it in order to reuse it later on. If you have filtered by material, you can also clear the filter in order to restore the priority plan.
- Change work center – With this button you open a dialog window where you can change the work center for the selected operation. You can also select multiple operations by activating the checkbox Include. If the checkbox Suggest most recent work center is activated in the dialog window, it means the most recently selected work center at an earlier change will be default when you want to change work center. If the operation has an alternative work center, you can by default change to that work center. The Show all work centers checkbox in the dialog is in that case not marked. If an operation does not have an alternative work center, that checkbox will be marked and then it is possible to select among all work centers.
- Rescheduling according to New finish – With this button you can reschedule the selected operations so that each operation's planned finish date will be changed to the same as the operation's New finish, if possible. First you mark the operations which you want to replan by using the Include checkbox.
You will be asked if you also wish to replan the entire manufacturing order. If you answer Yes, the entire order will be replanned. If you answer No, then only the operation will become replanned, and if the operation falls outside the part's lead time the entire order will be replanned.
- Clear material directly – Using this button you clear the material for the selected operation. You can also select multiple operations by activating the checkbox Include. In the column M you will see C (cleared) if all the material is available in stock (that is, all the material is cleared). If you use this function, the material clearance will be made. It is saved without any other window or other procedure is opered. This is a quicker way than to go to the Material clearance procedure. The advantage of going to the Material clearance procedure is that you can see the which materials where a shortage exist, if any.
- Return to regular sorting – With this button you reset the regular sorting of the priority plan after the planned start date, if you had resorted it by another column.
-    
Replan – With this button you can replan setup time and unit time for the selected operations in the priority plan. It is possible to change an individual operation or change the total/summary, this might then cause an adjustment of all the operations. On a total material row (bold row) you can change unit, adjust setup quantity and total planned quantity. You can also change part numbers on a material row if you want to change your orders so that another material is used. It is also possible to expand a total material row and adjust setup quantity and planned quantity for individual included materials. If a change is made of a total material row, the included sub-rows will also become changed. If it instead is a sub-row with included material that is changed, then that change will be locked, even if a change is then made of the total material row. If all sub-rows are changed and locked, then it is not possible to make changes to the quantity of the total material row.
It is also default to create a reporting batch of the operations. All work items in the reporting batch are then automatically selected in the recording terminal when one of the included operations is selected by an operator. Replanned operations get a background color in the Include column in the priority plan in the. This way the operator will see which operations belong together in the reporting batch. The same colors are also shown to the operator in the recording terminal.
Also in coordinated processing (configured in the part register), a reporting batch is created of the parts included in the coordinated processing in case those parts occur on the same operation number and work center.
> Please note! The function Replan is primarily intended to be used before the first reporting. After partial reporting there is great risk of unwanted effects if changed have been made to the planned time or planned material availability.
- Find – (Ctrl + B) This button will open a field for a Find as You Type feature which searches all columns in the priority plan. The search field is shown in the grouping section above the table in the priority plan.
- Change capacity – With this button you can change the capacity for the selected work center and week. For work centers with "Day planningDay planning is used when you are NOT applying hourly planning. It means that all operations are planned to a date and not to a specific time on a date." it is possible to edit basic time and number of machines/persons for each day. For work centers with "Hourly planningHourly planning refers to when planning per work center is done per hour. Hourly planning is activated with a system setting. Period is then entered as date and time. You can view loading on hour basis." or "Capacity via schedule" it is possible to change the capacity by changing the schedule and number of machines/persons.
- Show files – shows linked files such as, e.g, drawings, for the marked operation.
- Show documents – shows traveler, operation document, and material document for the marked operation in a separate document viewer window.
The document viewer window
On the toolbar menu you find the following buttons:
-   
Keep on top ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/KeepOnTop_15x15.png) – With this button you decide if this window should remain the top window.
-   
Remember size and position of window ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SaveWindowImage.png) – With this button you decide if you want the window size and position to be saved to next time you open the window.

#### Row
Here you see the row number. If you use drag and drop to prioritize the operations, you must place the mouse pointer in the Row column for the drag and drop function to work. Read more about drag and drop under Priority of operation (P. op.) further down on this page.

#### Include
With this checkbox you enter if the operation should be included in actions performed via the function buttons (for example "Rescheduling according to New finish" or "Clear material directly").
You can mark this checkbox for several rows in an interval by using Shift + mouse click.

#### Recording status (Rec. s.)
This column is only shown if you have installed the Time recording option and there is at least one operation with a recording status. A button will then be available here showing a symbol for the recording status in question. The different recording statuses are In progress, Clocked out, and Standby. A tooltip is shown when you hover over the symbol, displaying the status in text. If you click the button you can see which employee has recorded, as well as date and time for the recording, and the status of the recording.

#### Priority of operation (P. op.)
Here you can enter the priority of the operation (up to 2,147,483,647 which is an integer of 32). The lower the number, the higher the priority. Operations with a priority are shown with a green background. In the recording terminal you will see operations that have a priority displayed with the same green background and at the top of that priority plan.
It is also possible to prioritize by dragging and dropping an operation. This is done by clicking a row number and drag it up or down (the row will be highlighted with a blue frame). If multiple rows have been marked with the Include checkbox, all of the marked rows will be prioritized when dragging and dropping.

#### Prioritize the entire operation list (E)
If a priority has been entered for the operation, you will see the button Prioritize the entire operation list ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) in the column E. Using this button you can select if other operations, in the same node in the order structure, also should get this priority.

#### Previous operation (P)
In this column you can see if the operation is ready to run, based on the status of the previous operation.
If the column is empty it means that the previous operation has not been started. Therefore, the operation in question is not ready to run.
An "I" means that the previous/preceding operation is in progress, that is, someone is recorded on that operation at the moment, or that there is a shipped quantity (when the previous operation is a subcontract).
An "S" means that the previous operation has been started and has reported time, but it has no reported quantity or its quantity is the same as on this operation. This means that the operation is not yet ready to run, but that it might soon be ready to run.
A "P" means that the previous operation has a partially reported quantity that is greater than the quantity reported on the operation in the priority plan. That is, you have a quantity that can be processed in this operation even though the previous operation is not entirely finished.
A "F" in green, means that the previous operation is finished (has zero as remaining quantity), and the new operation is thereby ready to run.

#### Ready to run. Sufficient quantity reported from previous op.
Show number of operations ready to run based on the previous operation. This is calculated as “Reported quantity on previous operation” minus “Reported quantity on my operation”. (Except for on the first operation of the order, there you will instead see the operation’s remaining quantity as ready to run).

#### Material availability (M)
In this column you can see whether or not the operation is ready to run, based on if material is available.
- If the column is empty, it means the operation does not have any material requirements. The operation is ready to run (as long as the previous operation is finished or has a partial reported quantity).
- An "R" means that there is a material requirement. That is, material is needed for the operation according to the BOM and routing or the manufacturing order, but the material is not cleared. Therefore the operation is not ready to run.
- A "C" means that the material for the operation is cleared.

#### Tool availability (T)
In this column you can see whether or not the operation is ready to run, based on if the tools are available. If the column is empty, the operation has no linked tools, and the operation is ready to run (as long as the previous operation is finished or has a partial reported quantity).
An "R" means that there is a tool requirement, that is, there is linked tools for the operation but that tool is not cleared. Therefore the operation is not ready to run.
A "C" means that the tool for the operation is cleared.

#### Manual operation status
Here you can assign the operation a manual status. These should first be registered in the procedure called Manual operation status. The purpose of such a status may be, for example, to describe other events taking place for operation before they are started. When the Tools & Maintenance option is used you can also use the manual operation status as a tool status for the operations. Then you can describe if the tools for the operations are ready so the operations can be started.

#### Order number
Here you can see the order number that the operation belongs to.

#### Order type
Here you can see the type of manufacturing order: Stock driven or Order oriented.

#### Part number
Here you can see the part number to which the operation belongs.

#### Active case
Here you can see cases with statuses 1–3. If there are no cases on any of the parts in the loaded work center, then this column will not appear. If the part only has one case, the case number will be shown in the column. If there is more than one case, Several will be shown in the column. The case number and name is shown in the tool tip.
On the toolbar and in the information menu (right-click), you can go directly to the Register case with the cases in question already loaded.

#### Operation
In this column you can see the operation number. The operation number of the starting operation is displayed in bold font.

#### Planned start
Here you can see the planned start date of the operation. If this date has already passed, it will be displayed in red.

#### Planned finish
Here you can see the planned finish date of the operation. If this date has already passed, it will be displayed in red.

#### New finish
The date you can see here is a date calculated in the priority plan, based on the current order of the operations. New finish is shown with date and time (hours) when hourly planning is applied. The date reflects an expected finish date/time considering capacity and remaining time on the operations and their priority in the priority plan. The New finish date is always in the future.
The New finish is based on the current date and time. Then the remaining time for the planned operations in the priority plan is added. Based on the capacity, a new theoretical finish date is then calculated for each operation.
> Please note that the “New finish calculation” takes the number of machines in the operation into account. This may mean that the new finish date is not always in the same order as the rows.

#### Difference (Diff.)
In this column you see the difference in work days or hours (depending on whether daily or hourly planning is applied) between the planned finish and the new finish. If the new finish is later than the planned finish, a negative value will be displayed in red.

#### Remaining time
Here you can see the remaining time for the operation, in hours.
Calculation of remaining time
Calculation of remaining time on operation when no quantity is reported
Remaining time = Planned total time – Total reported time
> Remaining time cannot be less than 0.
Calculation of remaining time on operation when quantity is reported
Remaining time = Remaining quantity x (Planned total time / Planned quantity)

#### Accumulated time
This column shows the remaining time of the operation as an accumulated value in hours.

#### Remaining quantity
This column shows the operation's remaining quantity in the part's standard unit. If the operation has a reported quantity, the remaining quantity is displayed in bold font.

#### Status
In this column you can see a symbol representing the order status of the part. The order status of the part is also shown on the node in the Structure box.
The different status options for manufacturing orders are:
| Symbol | Status |
|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusRegistered.png) | 1 – Registered |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_print.png) | 2 – Printed |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) | 3 – Started |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) | 4 – Finished |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusPostCalculated.png) | 5 – Post-calculated |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusDeliveredOpFullyShipped.png) | 6 – Delivered |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusHistorical.png) | 9 – Historical |

#### Priority
Here you see the priority of the manufacturing order.

#### Goods location
The goods location of the parts are shown here if this was entered in the previous operation.
Goods location can be entered when you report an operation which is not a final operation. The purpose is to let the operators in the next operation know the location of the parts.

#### Manufacturing order category
Here you can enter a manufacturing order category. By clicking the Category selection button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can select a category if categories have been registered in the Categories procedure. If no categories are registered, you can type as you please in this field. Categories can be used as a selection term in different lists. Read more about how categories can be created/constructed in the online help function for the [Categories](../../../GeneralRegisters/Categories/Categories/wCategories.htm) procedure.

#### Project number
Here you see the project number, if such exists on the manufacturing order. The name of the project is shown in the next column.

#### Variant code
Here you see the variant code, if such exists on the manufacturing order.

#### First material
The material’s part number is the first material row’s part number that is linked to the operation.

#### Material's name
The material’s name is the first material row’s name that is linked to the operation.

#### First tool
The part number of the first tool row that is linked to the operation.

#### Tool's part name
The name of the first tool row that is linked to the operation.

#### Report number
Here you see the report number of the operation.

#### Delegate
This column is only available if the option Work recording is installed in your system. By clicking the D button in the column, a window opens where you can delegate the operation to one or multiple employees by adding them in the table. With the setting Locked you can decide that no other than the employees to whom you delegated the operation, will be able to start the work item. The purpose of this is to dedicate the operation to one or several employees.
When the operation is delegated to an employee, the employee number will be shown on the button. If the operation is delegated to more than one employee, then the text Multiple will be shown on the button. A tooltip for the button displays the employee numbers and names in text.
An operation which is delegated, is always shown for the employees at the top of the priority plan in the recording terminal with a dark yellow background, regardless if the employee has selected a work center or a report number. A delegated operation which is also prioritized, is also shown with the dark yellow background (delegation is ranked higher than priority).

#### Customer
Here you see the customer number, if such exists on the manufacturing order. The name of the customer is shown in the next column.

#### Customer order
This column shows the customer order number if the manufacturing order is created from a customer order. By using the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button to the right, you can see information from the customer order header and the customer order rows.

#### Delivery date
This column shows the customer order row's delivery date in cases where the manufacturing order is created from a linked customer order and the part is order oriented.

#### Operation status
In this column you can see a symbol representing the status of the operation.
The different status options for operations are:
| Symbol | Status | Description |
|---|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpStarted.png) | Started | Only time has been reported for the operation. |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPartiallyReported.png) | Partially reported | A quantity has been reported for the operation. |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) | Finished | The entire quantity has been reported for the operation. |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPartiallyShipped.png) | Partial delivery made | A partial delivery has been made on the purchase order for a subcontract. The status is shown on the order row in the procedure Report arrival. When a partial delivery has been made of the purchase order, the status of the subcontract will be shown as partially reported as described above. |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusDeliveredOpFullyShipped.png) | Final delivery made | Final delivery has been made on the purchase order for a subcontract. The status is shown on the order row in the procedure above. When a final delivery has been made of the purchase order, the status of the subcontract will be shown as finished as described above. |

#### Part status (P)
In this column you can see a symbol representing the status of the part.

#### Instruction
The instruction for the operation. By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files (F)
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.

#### Alternative work center
You can determine in which alternative work centers an operation in the routing can be run, according to a certain priority. By clicking this button you can enter alternative work centers, the first alternative on the first row, the second alternative on the second row, etc. On the rows you see unit time, setup time, queue time, and exception for staffing factor.

#### Confirmed as delayed
In this column you can see if the operation is confirmed as delayed or not.

#### Cause
And if it is delayed, you can here see the cause of the delay.

#### Comment to delay
This button shows a comment to the delay, if any.

#### Time calculation, Show in priority plan, and Multiple operators
The options for the settings are loaded from the work center, but can be changed in the priority plan. These three columns are only available if the option Time Recording is installed in your system.

#### Node
If the main part has a maximum quantity entered in the part register and if the manufacturing order has a quantity greater than the main part's maximum quantity, then the quantity will become divided in different nodes with each nod containing the part's maximum quantity. For such orders, this column is also displayed and a node number is shown for each row of the main part.
