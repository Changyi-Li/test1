### Adjust work
Under the Adjust work tab you can adjust work recording and material for one day at a time.
The Work recording table
In the table you see work recording items and project activities for of the selected day. Here you can adjust these recording items.
Using the button Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5) in the function menu you can also add rows for work recording. Clicking the button lets you choose if you are adding Order-bound work. Indirect work. or Project activity. You get to enter times for start and stop, select a report number, and also select if it is setup time that is being added. You can only add order-bound work which the employee is allowed to run. This is determined via the setting Allowed work center for the employee/person in the Personnel records – Time recording procedure. The report number you enter here determines if the person is allowed to run the order-bound work or not (the report number is linked to the operation which in its turn is linked to a work center). If the employee/person is not allowed to run the order-bound work, then the OK button will not become activated. If a pool work center is linked to the operation for the entered report number you should also select which of the work centers in the pool group that will be used. If it is indirect work you are adding, you get to select a code for the indirect work instead of report number. You can also change the date for a work recording item you add, if it does not apply to the date of the selected day.
For projects it is possible to add project activities as well as edit times and project numbers.
Using the button Delete selected row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6) you can also delete a work recording item. But if that recording item has a reported quantity, a rejected quantity and reported quantity for material, you must first adjust these quantities to zero (0,00) before you can delete the recording item in question.
Using the button Calculate ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) you can calculate the time in the Time column on the rows.
Using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can go to related procedures for the selected recording item.

#### Recording type (T)
In this column you see a symbol representing which type of recording is concerned: setup time, unit time, indirect work, or project activity. A tooltip shows a text where you can see which part type the symbol refers to.

#### Modified
In this column you will see an exclamation mark (!) if anything on the row has been modified.

#### Status
If the manufacturing order the operation belongs to has status 9 (Historical) you will here see the symbol for status 9 ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusHistorical.png). Then it is not possible to make any adjustment of the recording item.

#### Start and Stop
In these columns you see the recorded start time and stop time. These times can be adjusted. In a batch recording it is only for the first row it is possible to adjust the times. If the work item is in progress, the stop time field is empty.

#### Distribution %
If the operation is part of a batch recording you will in this column see the distribution of the operation in percent in the batch.

#### Time
Here you see the time which have been recorded in hours. The time on the rows can be calculated directly by using the button Calculate. This calculation will also take place when you save in the in procedure.

#### Part Number
In this column you can see the main part number in an order-bound recording item. For indirect work you will see the name of the indirect work and you can change code. For projects you can instead see the project number here and it is possible to change.

#### Name
In this column you can see the main part's name in an order-bound recording. For project activities you will instead see the project name.

#### Comment for adjustment (A)
By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) you can enter a comment for the adjustment made. If there is a comment, the symbol has a black background color ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png) on the button.

#### Operator
For machine recording you will also see the Operator column. If the work item is order-bound then it is the employee number of the operator who started the machine and performed the recording that will be shown. If it is an indirect work item you will instead see the employee number of the machine. If you add an order-bound work item you must also select an operator.

#### Operation number, Order number, and Report number
For an order-bound work item you will see Operation number, Order number, and Report number. If you add an order-bound work item you can edit the report number until you save in the procedure.

#### Reported quantity
You can adjust the reported quantity in the used unit for an order-bound recording item of the type Unit time. You cannot enter a full quantity for the work recording item if there is a remaining quantity of traceable material.
If you first have made a positive reporting, it is allowed to report a negative quantity provided that the remaining will not be greater than the planned quantity. However, this does not apply if the operation is the final operation and/or has serial numbers.

#### Location (Loc.)
In this column the button Location ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) will be active if it is the final operation with transfer to stock that you are adjusting. By clicking this button you can see the selected location and the arrival reported quantity, and it is possible to adjust the information when needed. You can also add new locations. If you have entered a quantity for a location, the preceding field for reported quantity will become gray.
If the part has traceability at batch level, a batch number is entered for the location where you arrival report the reported quantity. If the setting Suggest best-before date is activated in the part register, then the part's best-before date is also shown in the next column. You can also adjust this date when needed.
If the part has traceability at serial number level, a serial number is entered for each entity of the part which is arrival reported during the reporting. Serial numberA serial number is a number that is used for traceability for parts on entity level. can be changed unless it is already taken.
Charge numberA charge number is used to provide traceability. It is the supplier's batch number, or charge number, which is linked to our batch number for a location. can also be entered for the location and it is possible to adjust. A link to a certificate file, if any, can also be adjusted.

#### Quantity to reject
Here you can adjust the rejected quantity by clicking the button in this column. The rejected quantity and its unit is then displayed on the button, otherwise 0.00 is shown.

#### Goods location
If the work item which you are adjusting has subsequent operations, you will here see the goods location where the reported quantity is placed.

#### Overtime
In this column you see the portion of the working hours that in the Time column is overtime.

#### Release work
You can choose to release an order-bound work item, if the person who started the work item in the recording terminal has clocked out and left the work in progress. You can then mark this checkbox. You might have to release a work item to be able to give the order status Historical, or to make the work item available to other employees.
If the work method Only change is selected for the person/employee, a new row will be added after the release. It will contain an indirect work item which is started on the code selected via the system setting Indirect work code to start when releasing order-bound work.

#### Date at stop
Here you will see the date when the work item was stopped. This date is possible to edit. A validation is made to make sure the stop date does not occur earlier than the start date.

#### Automatic withdrawal of material
When this setting is activated the Quantity to report will automatically be adjusted when you adjust quantity in a work recording item of the recording type Unit time. If the material is traceable you must manually report the material withdrawal to be able to enter batch number/serial number.
If the setting is not checked you manually have to enter quantity to report in the material table, and also select location and adjust remaining quantity.
A summary of total reported time, as well as the difference between reported attendance and reported hours on work items is shown.
The Material table
In this table you see the material which is included in the selected work recording item. Material is only included in order-bound work recording items. Here you can adjust quantity and remaining quantity.
Using the button Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5) you can also add rows for extra material to the selected work recording item. In a dialog box you can select part number and quantity to report. If you are not allowed to add material (determined with a setting in the personnel records), the setting is not available.
Using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can go to related procedures for the selected material.

#### Reported quantity
Here you see the reported quantity and it is also possible to adjust. The quantity is by default shown in the unit which applies for material withdrawal to manufacturing order.

#### Quantity to report
You can adjust the quantity to report if you for example add extra material.

#### Location (Loc.)
Under the Loc. button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can enter a location for the material withdrawal.

#### Unit
Here you by default see the unit which applies for material withdrawal to manufacturing order. If there are more than one unit registered for the part, you can change unit and it will affect the quantity fields.

#### Part
This field shows the material's part number. If you add an extra material you can edit the part number until you save in the procedure.

#### Name
Here you see the name of the material.

#### Part Type
This column displays a symbol representing the part type: Purchased or Manufactured. A tooltip shows a text where you can see which part type the symbol refers to.

#### Planned quantity
This column shows the planned quantity of the material in the operation.

#### Reported quantity
This column shows the reported quantity of the material.

#### Balance
Here you see the current balance of the material in total for all locations.

#### Cleared quantity
Here you see the quantity which has already been cleared for this order.
