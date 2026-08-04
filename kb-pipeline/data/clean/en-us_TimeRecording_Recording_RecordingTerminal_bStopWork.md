### Stop work
In this mode you stop direct work, indirect work, and project activity in progress. A direct work item is also possible to put on standby.

#### The Stop button
With the Stop button you stop/finish the work item or project activity for which the Include checkbox is checked.
If you have the work method Only change, the terminal will then change mode to where you can start a new work item, unless you first chose to start that work item.
If the work center has been configured to print transport label when you stop a work item and you have entered a reported quantity, the terminal will then go to the mode where you print transport labels. There you can preview and print transport labels. If you have entered a rejected quantity you can in this mode also preview and print the transport label for rejected goods.

#### The Cancel button
By clicking the button Cancel you cancel the mode where you stop work and the recording terminal reverts to the recording mode.
Work in progress
In the upper table you see the work in progress which you have started.
The Function menu
Using the buttons Add new row at the end ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5) and Delete selected row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6) you can add or delete material rows for the selected work item. This applies if you are allowed to make material addition. This is determined via a setting in the personnel records. You can NOT delete material rows which are already saved on the order. You can only delete rows which you yourself have just inserted, up to the point when you save.
With the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) (Shift + F8) you can expand all rows of work items, when there is one or multiple materials for the work. When material exists you will see an arrow button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to the far left on the row. This can also be used to expand the row for that specific work item and show the related material row. In their turn, material rows have the same arrow button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) which you can use to expand the material's locations and select location row from where material should be withdrawn in the Reported quantity field (Rep. qty).
Using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can via the link go to related procedures for the work item on the marked row.
You use the Update button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_update.png) to report a mandatory measuring item in order to close the validation to be able to report the actual operation.
The Find button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search.png) (Ctrl + B) will open a field for Find as You Type in texts among the work in progress.
The Edit traceability button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) is activated if there are serial numbers or batch numbers withdrawn for the work. By clicking the button you can then change these numbers. You may need to do this if, for example, a traceable material which has been withdrawn for the work item, must be replaced during the manufacturing.
Using the button Show all locations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png) you can choose to see all locations for the material. Then you also see the locations which the system has not suggested for material withdrawal. This means that you, when needed, can select a different location to withdraw material from.
The button Automatic withdrawal of material ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_no_structure_part.png) is shown if you are permitted to report material. This is determined via a setting in the personnel records. You can then activate/deactivate this button. If you activate it, the quantity of the material will automatically be reported. If you deactivate it, you get to enter the quantity manually when you report a work item of the recording type Unit time.
- If the button is activated, the material quantity will be automatically updated when you have entered a quantity in the field Reported qty and Rejected qty, if any. Then it will not be possible to expand material rows to see and select location. In that case, material is primarily withdrawn from the location which is pick location for the work center and secondarily from the location with the highest priority. In third hand, material will be withdrawn based on the age analysis. That is, material will be taken from the location which has the oldest "last arrival date".
- If the button is deactivated, then you can go to material row or location row and manually enter quantity to report and adjust the remaining quantity on the material row.
- If the system setting Suggest withdrawal of material at start of operation is set to Yes and the material was withdrawn at the start, this means no reporting of the material's quantity will be made in connection with reporting of the work item.
- If the material is traceable you must manually report the material withdrawal to be able to enter batch number/serial number.
The button Automatic withdrawal of tools ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_tools.png) is shown if you are permitted to report material according to above. This button is available if the Tools & Maintenance option is installed. You can then activate/deactivate this button. If you activate it, the quantity of the tool will automatically be reported. If you deactivate it, you get to enter the quantity manually when you report a work time.
- To be able to automatically report a tool (with traceability), the setting Allow automatic withdrawal in the part register must be activated. Tools that are withdrawn/lent are automatically returned only when no employee is clocked-in on the operation and the remaining quantity on the operation is 0.
- If the button is activated, the tool quantity will be automatically updated when you have entered a quantity in the Reported qty field. Then it will not be possible to expand tool rows to see and select location.
- If the button is deactivated, then you can go to the tool row or location row and manually enter quantity to report.
- If the system setting Suggest withdrawal of tools at start of operation is set to Yes and the tool was withdrawn at the start, this means no reporting of the tool quantity will be made in connection with reporting of the work item.
- If the system setting Return reusable tools when return operation is reported as finished is set to Yes, it means the tool will automatically be returned to its location when the work item is reported as finished (that is, the remaining quantity is zero). If that system setting is set to No, you will instead have to return the tool in the Withdrawal list procedure.
- With the Return tool when operation is interrupted setting in the Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register procedure you decide if the tools used in the operation should be returned if the operation is interrupted, even though the entire quantity has not been reported.

#### Include
With the checkbox Include you decide which of the work items in progress or project activity that should be stopped/finished. When you mark the checkbox, the following columns becomes available.

#### Reported quantity
Here you enter the quantity you report. If you report the entire remaining quantity, the work will be set as completed. If there is a remaining quantity of traceable material, you cannot report the entire remaining quantity for the work item. Then you first have to report withdrawal of the traceable material and there enter batch number/serial number. Excess reporting of quantity and how great quantity you can excess report you determine using the system settings Reasonability check of excess reporting and Allowed excess reporting in % of planned qty.
If you first have made a positive reporting, it is allowed to report a negative quantity provided that the remaining will not be greater than the planned quantity. However, this does not apply if the operation is the final operation and/or has serial numbers.
If the button Automatic withdrawal of material ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_no_structure_part.png) is not activate, you can on the material row and/or the material's location rows manually enter reported quantity (withdrawal) of the material. If the button for Automatic withdrawal of material is activated, then the material withdrawal will be updated based on the quantity you report for the work item.
To show material rows and also to be able to manually report material, you must be allowed to do so. This is determined via settings in the personnel records.
If you have measuring points linked to the operation, you will be shown a validation message if the measuring points have not been reported according to the measuring template. This applies both to mandatory and non-mandatory measuring points.

#### Location (Loc.)
Instead of entering a reported quantity in the field Reported quantity you can use the button Loc. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) to select a location. This is then the location to which you arrival report the reported quantity when it results in transfer to stock (final operation). You can, if needed, also add new locations. If you have entered a quantity for a location, the preceding field for reported quantity will become gray.
If the part has traceability at batch level, you should enter a batch number for the location where you arrival report the reported quantity. By default the manufacturing order number is suggested as batch number. But you can enter any batch number you please. In case the setting Apply best-before date is activated in the part register, you also have to enter that date in the next column. This date can also be suggested by default if the part has the setting Suggest best-before date activated.
If the part has traceability at serial number level, you must enter a serial number for each entity of the part which is arrival reported during the reporting.

#### Goods location
Here you enter the goods location where the reported quantity should be placed. This field is used when the reported quantity does not result in transfer to stock, meaning when it is not the final operation.

#### Finished
This checkbox is available on project activities. If the project activity is finished and should be stopped, you check this box. You then execute by clicking the Stop button. The status of the activity will then be set to Finished.

#### Rejected quantity
Here you enter the rejected quantity to report in addition to the approved quantity. By clicking the button you open a window where you can add rows with different rejection codes, write comments, and link external files to rejections. You can report rejection for serial numbers.
If the system setting Create case/internal nonconformity at rejection for operation has been set to Yes, always or Yes, with question, a case will either automatically be created or created after a question. The case type which is created during the rejection, or which is suggested to be created, is determined by the related system setting Default case type. When the system setting is set to the option Yes, with question it is possible for the recording operator to select the case type.
Rejected quantity can also be reported in corresponding way for material per location.

#### Remaining quantity
Here you see the remaining quantity to report for the work item. The reported quantity is deducted from this value and the work item's Reporting status (S) will be set to Partially reported ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPartiallyReported.png). It is possible to manually enter a remaining quantity or enter (0.00) to delete the remaining quantity. If you enter zero, the Reporting status (S) on the work item will be set to Finished ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png).
If there is a remaining quantity of traceable material, it will not be possible to set the work item as finished here, by entering zero and deleting the remaining quantity. Then you have to replan the operation instead.
Deleting of remaining quantity and how much of the remaining quantity you can delete when work items are reported as finished, is determined with the system settings Reasonability check for deletion of remaining quantity and Max. deletion of remaining allowed in % of planned quantity.

#### Standby
For direct work and setup work you can check this box in order to put the work item/activitiy in question on Standby when you stop it. A work item or activity can be put on standby if you for example, intend to run another work item in between and then resume the work item. Standby work items are shown under Work in progress in the recording mode. From there it is possible to start it again. You can also release a work item which is on standby and thereby make it possible for other employees to start it. This is done in the same place using the button Release standby. A work item on standby is not visible in the priority plan for other employees.

#### Cause code
This field becomes available in cases where the Remaining quantity for the work is zero and the Reported total time differs (in percent) from the planned time for the reported quantity than what is allowed according to the system settings called Mandatory cause code if time used exceeds planned time (in %) and Mandatory cause code if time used is less than planned time (in %). In such cases you must select a cause code. It can also be mandatory to enter a comment.
You can select among the active cause codes for time loss and time gain that are registered under the Time used tab in the Cause codes procedure. In that procedure you also enter if a comment is mandatory for the cause code.

#### Comment
Here you can enter a comment regarding the work item you stop/finish. It can be mandatory to enter a comment for indirect work. This is determined via a setting per code for indirect work in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Work procedure. If the comment is mandatory it means the Stop button will not be available until you have entered the comment.

#### Files
Here you can link external files regarding the work item you stop/finish.

#### Stock count request
Stock count request is mainly used if you find that the stock balance does seem to add up and you wish to signal this in Monitor ERP. When you activate this checkbox, today's date and the time will be set in the Request date field.
The parts for which there is a stock count request can be shown in the Create stock count basis list in the Stock count in list procedure. This is done by activating the Include requested stock counts setting. You can also select by Stock count request date. The list also displays the comment. When the stock count has been performed and saved for the part, the field and the comment will be cleared.

#### Request comment
If you have checked the Request comment checkbox, you can here add a comment regarding the cause of this request.
Other information for a work item in progress
The T column shows a symbol about which recording type is concerned: direct work (unit time) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridDirectImage.png), setup work (setup time) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpStarted_15x15.png), indirect work (indirect time) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/gridIndirectImage.png), or project activity ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_project.png). A tooltip is shown when you hover over the symbol, displaying an explanation.
The S column (Reporting status) shows a symbol representing which reporting status is concerned; partially reported or finished. A tooltip is shown when you hover over the symbol, displaying an explanation. If the work item in question has not yet been reported, the column is empty.
Part number refers to the part in the manufacturing order. If the row refers to an indirect work item, the code for the indirect work item will be show in red. On material rows you will here see the material's part number. On the material's location row you will see the location name.
Name is the name of the part. If the row refers to an indirect work item, the code for the indirect work item will be show in red.
Cleared quantity (Cleared qty) is the already cleared quantity of the material on this order.
Disposable balanceThe disposable balance is the current part balance on the locations at a given time minus reserved quantity plus ordered quantity. (Disp. balance) shows the material's disposable balance as total of all locations.
Order number is the manufacturing order number.
Op. no. is the number of the operation.
Op. name is the name of the operation.
WC is the work center for the operation when you started the work item. If someone changes the work center for the operation after you started it, you will still report on the work center where you started the work item.
Planned total time (Pl. total time) is the planned total time.
In the Reported total time (Rep. total time) column you see the already reported total time.
Report number is the report number of the operation/material.
Rejected qty is the quantity of work/material which has already been rejected.
In the Reported quantity column you see the already reported quantity.
Project number is the project number if the manufacturing order belongs to a project.
Project name is the name of the project.
Customer number is the customer number on the manufacturing order.
Rename serial number – If the part has a serial number it is possible to use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_rename.png) and then rename the serial number to a different serial number.
Best-before date is the latest recommended date for withdrawal and consumption of the material.
Charge numberA charge number is used to provide traceability. It is the supplier's batch number, or charge number, which is linked to our batch number for a location. is the charge number, if any, which you receive from the supplier and entered for the material during arrival reporting.
The More information button
The information below is available as standard under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) for a work item in progress:
The Time column refers to the time elapsed since you started the work. This the working time which will be reported. If the working time contains overtime this will be saved separately. When applying batch recording the time will be distributed among the operations, based on the operations' planned times and the reported quantity.
Balance shows the material balance as total of all locations.
Planned quantity (Pl. qty) is the planned quantity for the work item/material.
Started is the date and time when the work item was started.
A NodeA node is an included/incorporated manufactured part on a certain level in a part structure. A level in the structure part can contain multiple nodes. The node on the highest level is called the main part (order). is an included/incorporated manufactured part on a certain level in a part structure. A level in the structure part can contain multiple nodes. The node on the top level is called "main part".
Customer number is the customer number on the manufacturing order.
In the Customer name column you see the name of the customer.
Total material quantity
In the lower table in the window you also see the material rows for the work item in progress in the upper table which you have marked to Include. In this table you can report material withdrawal or you can do it directly on the work in progress in the upper table.
By using the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) (Shift + F8), you can expand all material rows to show the locations. You can also expand a material row by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_row.png) to show that material's loactions.

#### Quantity to report
Here you see the reported quantity (withdrawal) of the material. If you are permitted to report material and deactivate the button Automatic withdrawal of material ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_no_structure_part.png) on the function menu in the upper table in the window, you can also enter a quantity here to report. You enter the quantity per location.

#### Remaining quantity
This is the remaining quantity of the material which is left to report.
Other information shown in the material table
In the TT column you will see a symbol representing the traceability type: at batch level or serial number level. A tooltip is shown when you hover over the symbol, displaying an explanation.
The T column displays a symbol representing the part type: purchased, manufactured, fictitious, or service. A tooltip is shown when you hover over the symbol, displaying an explanation.
Part number is the part number of the material.
The Name is the name of the material.
Cleared quantity (Cleared qty) is the already cleared quantity on this order.
Balance shows the material balance as total of all locations.
In the Reported quantity (Rep. qty) column you see the already reported quantity of the material.
The More information button
The information below is available as standard under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) for the material belonging to a work item in progress.
Best-before date is the latest recommended date for withdrawal and consumption of the material.
Charge number is the charge number, if any, which you receive from the supplier and entered for the material during arrival reporting.
