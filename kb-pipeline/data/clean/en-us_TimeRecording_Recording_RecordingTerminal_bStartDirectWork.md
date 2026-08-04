### Direct work
This tab is available if the option Report number or Priority plan have been set as allowed methods to select work for you in the procedure Personnel records – Time recording.
Using the button Change work center ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_replace.png) on the function menu you can replan operations by changing work center for the operation in connection with starting work. You can select among the work centers which are your allowed work centers in the above mentioned procedure. A prerequisite for changing work center is that the setting Allow work center replanning for operation? has been activated.

#### Work center
In this field you can select a work center and you will see all operation in the priority plan for that work center. The field is available if you have Priority plan configured as an allowed method to select work.
You can only select among the work centers allowed to you in the procedure Personnel records – Time recording.
When you have selected a work center you can in the priority plan choose one or, in some cases, several operations to include in the work item. You can select to include more than one operation in the work item (which creates a batch) if the work center allows batch recording.
Read more about the priority plan below.

#### Report number
Here you can enter a report number and then you see the operation which has this report number. This field is available if you have Report number configured as an allowed method to select work in the procedure Personnel records – Time recording.
Using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search.png) next to the field you can instead select an operation via a manufacturing order number. First you select a manufacturing order, this will show you all operations belonging to that order and then you select one of these.
When you have entered or selected a report number, you can in the priority plan select to include the specific operation in the work item.
An operation will be displayed regardless of the time horizon applied for the work center.
You can only enter/select report number for operations in your allowed work centers, according to the setting in the above mentioned procedure. If you enter/select a report number for an operation in a work center which is not allowed, a message in red will inform you that you are not allowed to start this operation.
If you enter a report number for an operation which you have already started, a message in red will also be displayed saying you are already clocked in on the operation in question. This means that it is not possible to start the same operation twice.
Read more about the priority plan below.

#### Filter
In this field you can choose to filter which operation to show in the priority plan based on the options listed below. You can create a default filter in the procedure Personnel records – Time recording which you can use here. The default filter can also be locked in that procedure. In that case this field becomes inactive and you cannot make any changes to the filter. Please note! Delegated work and work on standby are never filtered out.
- Prioritized – This filter will show you the prioritized operations.
- Ready to run (P) – This filter will show operations where the previous operation is finished, that is, where the column P (Previous operation) displays an F for Finished.
- Ready to run (M) – This filter will show you operations that either have cleared material or do not have a material requirement, that is, where the M column (Material availability) shows a C for Cleared material or is empty.
- Time horizon (WC) – This filter will show you the time horizon of the work center, in number of days. You will see the operations which have a date within the time horizon. Which date is used for the filtering is determined by the system setting Time horizon filters by. If you select an operation via the report number, you will see this operation regardless of the time horizon which applies for the work center.

#### Shop packet
By clicking the Shop packet button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can in a dialog make temporary modifications to printout settings for the work item in question and choose to print shop packet, linked files, and transport label in advance before you start the work item. In the dialog you access with this button it is the Include checkbox which determines that the shop packet should be printed. You print by clicking the Direct printout button in the dialog.
You can configure default settings to apply for printouts at Start work in the recording terminal. This is configured per work center in the Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register procedure. Automatic printing of shop packet and transport label can be configured as well. You can also override these settings per person in the Personnel records – Time recording procedure.
Via the Print shop packet button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) in the dialog you can make a temporary choice of how many copies to print of the different order documents and if linked files, if any, should also be printed.
You can configure how and when order documents and linked files should be printed. On a general level this is decided with the system setting called Print linked files. The corresponding setting for printing of linked files can also be configured per user in the Users procedure.

#### Start
Using the button Start you start the direct work.
If the operation in the work item belongs to a pool group you now get to select the work center in the pool which should do perform the work.
If withdrawal of material at start of work has been configured, you will now come to the mode where you report material. If withdrawal of material should take place at start of work, is generally determined by the system setting Suggest withdrawal of material at start of operation. But you can override this with a setting on the work center. Read more about [Material reporting](bMaterialReporting.htm).
If you have the work method Only change the terminal will then change mode to where you can stop the previous work, unless you first chose to stop/finish that work item.
When printing of shop packet or transport label has been configured, for you or for the work center, to be done when starting the work item, you then get to approve the printout of the documents in question. If your user account have default printers set up for transport labels and shop packet documents, then the printing will take place without printer dialog.

#### Add to batch
This button is shown instead of the Start button if you have a batch recording work in progress and in the recording mode chose to add to batch. With this button you add the selected work to the batch. It is only work with time calculation set to Batch recordingBatch recording of the operations in the recording terminal means that several different operations can be started and finished at the same time, and that the reported time will be distributed evenly among them. The time calculation will distribute the time according to the planned time and quantity taken from the pre-calculation, as well as the reported quantity. Batch recording can for example be made in cutting operations, when several operations have the same raw material and also have short lead times. This is then used to avoid unnecessary work with the reporting. which can be added. The work item you add will get the same start time as the other work items in the batch. Consequently, there will be no difference regarding time if you add to batch or if all work items in the batch are started at the same time.

#### Start setup
By clicking the button Start setup you start setup work (setup time) for a direct work item.
If you have the work method Only change the terminal will then change mode to where you can stop the previous work, unless you first chose to stop/finish that work item.

#### Cancel
By clicking the button Cancel you cancel the mode where you start work and the recording terminal reverts to the recording mode.

#### The Priority plan
Using the Include checkbox in the priority plan you select which operation to include in the work.
A selected work item/operation gets a yellow background. Prioritized operations are positioned at the top of the priority plan and are shown with a green background. An operation which is delegated to you is always shown at the top of the priority plan with a dark yellow background, regardless if you have selected a work center or entered a report number. A delegated operation which is also prioritized, is also shown with the dark yellow background (delegation is ranked higher than priority). An operation which you have already started in a work item is not shown in the priority plan
Work items which have been replanned to reporting batches in the procedure Priority planning will get different background color making it possible for you to see which individual work items which belong together in each reporting batch. If you mark to include a work item in a reporting batch, then all work items with the same color will automatically be included.
In the W column a warning symbol is shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) if there is something that is not OK when starting the work item. A tooltip is shown when you hover over the symbol, displaying the cause of the warning in text form.
Other columns in the priority plan contains the same information as the [priority plan](../../../Manufacturing/Planning/PriorityPlanning/bPriorityPlan.htm) in the Priority in planning procedure.
The boxes called [Structure](../../../Manufacturing/Planning/PriorityPlanning/bStructure.htm), [Order information](../../../Manufacturing/Planning/PriorityPlanning/bOperations.htm), and [Material](../../../Manufacturing/Planning/PriorityPlanning/bMaterials.htm) contain the same information as in the Priority planning procedure.
