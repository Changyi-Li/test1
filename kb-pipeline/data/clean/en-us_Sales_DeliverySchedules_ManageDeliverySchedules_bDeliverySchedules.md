### Delivery schedules
In this box you see your selected delivery schedules in a list.
You can expand each delivery schedule and see the parts that are included in the delivery schedule. The list contains all necessary information about each delivery schedule and part.
The information is partly loaded from the delivery schedule in [Register delivery schedule](../RegisterDeliverySchedule/wRegisterDeliverySchedule.htm) and partly from [settings](../BasicDataDeliverySchedules/bSettings.htm) on the delivery schedule type. There is also additional information which is only displayed here on the delivery schedule. This information is described below.
The function menu
On the function menu you also find a button you can use to expand/minimize rows. There is also a button you can use to go to the related procedures for the marked delivery schedule. Here you also find buttons used to handle entire delivery schedules or specific parts included in these.
The Activate button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) – With this button you activate a selected/marked delivery schedule or a marked incorporated/included part. Status is set to Activated.
The Reconcile button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_edit_list.png) – With this button you reconcile a marked delivery schedule or a marked incorporated/included part. Status will be set to Reconciled.
Transfer ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_release.png) – With this button you transfer a marked delivery schedule or a marked incorporated/included part to customer order. For each call, a customer order row is created on the order. Status is set to Transferred.
Cancel all requirements ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_undo_release.png) – With this button, the status will go back to Reconciled and at the same time all requirements will be canceled by turning the remaining quantity to zero (0). The cancellation of the customer order rows will then be executed by transferring the delivery schedule using the button Transfer ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_release.png).
Set status to Replaced ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_cancel.png) – With this button you manually replace a marked included/incorporated part in a delivery schedule. The status is set to Replaced for the part and for all calls regarding it. This function can be used in cases where there are parts left in the delivery schedule which have not been replaced.
> Please note! You must save in the procedure when you have performed any of the following actions: Activate, Reconcile, Transfer, and Cancel all requirements. Otherwise it will not be saved on the delivery schedule and customer order in Monitor ERP.
Calculate deviations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) – With this button you start a calculation of deviations based on the deviations model entered for the delivery schedule. The button is activated if the delivery schedule has status Activated or higher and a deviation model is linked to the delivery schedule.

#### Deviations (D)
Available via More info. Deviations are checked and saved on part level for the delivery schedule. The button itself shows if there are deviations (warnings and/or alerts). If you click the button, a table is shown with details about the deviations:
- Type – Here you see if it is a deviation alert or a deviation warning.
- Deviation percent – the deviation in requirements between this delivery schedule and the previous one.
- Period start date – the start date of the period (based on the period definition in the deviation model).
- Period end date – the end date of the period (based on the period definition in the deviation model).
- Period multiple – (from the period definition in the deviation model).
- Period type – (from the period definition in the deviation model).
- Alert threshold – upper – (from the deviation model).
- Alert threshold – lower – (from the deviation model).
- Warning threshold – upper – (from the deviation model).
- Warning threshold – lower – (from the deviation model).
- Current period quantity – the total of the requirements for this period in the current delivery schedule.
- Previous period quantity – the total of the requirements for this period in the previous delivery schedule.

#### Calculated start date
Here you see the calculated start date of the delivery schedule. This date is based on the call which has the earliest date among the parts included in the delivery schedule.

#### Calculated end date
Here you see the calculated end date of the delivery schedule. This date is based on the call which has the most recent date among the parts included in the delivery schedule.

#### Cumulative quantity, start date, Monitor
Here you see the start date for cumulative quantity for the part in Monitor ERP. This date is loaded from the customer link of the part in the Part register primarily, and secondarily from the customer in the Customer register.

#### Cumulative quantity, start date, Delivery schedule
Here you see the start date for cumulative quantity for the part in the delivery schedule. This date is from the customer in the delivery schedule.

#### Cumulative quantity – Delivered
If cumulative adjustment is used, the adjusted cumulated quantity will be included in this field.

#### Cumulative quantity – Received
Shows the cumulated received amount.

#### Cumulative quantity, offset

#### Transfer to
Shows if the delivery schedule is transferred to customer order or sales forecast.
