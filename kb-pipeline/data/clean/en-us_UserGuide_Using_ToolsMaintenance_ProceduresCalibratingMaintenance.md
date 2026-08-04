### Procedures used for calibration and maintenance
After registration of basic data you can use the procedures as outlined below. Calibration and maintenance can be handled with or without maintenance orders*. For example, when calibrating measuring tools it is not necessary to create a maintenance order. This is only necessary if you buy the calibration service. Then you have to use maintenance orders since this takes place via subcontract purchase.
> * A maintenance order is a type of manufacturing order. Maintenance orders are used if you want to plan as well as report time and material for the maintenance.

#### Planned maintenance
In this procedure you monitor which tools require calibration and maintenance. You can, for example, select by Part template in order to see all maintenance items on a specific equipment. You can also select by Maintenance template in order to see all equipment that are included in this maintenance item.
Under Include, in the settings, you choose the trigger types to be checked (Calendar, Distance, Operation time and Number of cycles). You also choose which planned maintenance will be handled and affect the filtering.
Under the Show heading, in the settings, you choose the previously planned maintenance that is shown in the list, the reporting status, and if you want to see the next reservation of the tool.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PlannedMaintenance.png)](../../../../Resources/Images/TrainingMaterial/PlannedMaintenance.png)
Once you’ve loaded the list, the tools that are due for maintenance or calibration are shown, either because one of its counters has passed the limit for the selected maintenance, or because the number of days has passed. The list contains many columns with information. Among other things, these show where the tool is placed and if it is being used for an order right now.
There are many different ways to work in the list.
One way is to select that calibration or maintenance of a tool is in progress, in order for it to be shown in different procedures. You can then update the tool’s status to Maintenance in progress in the list. You can then enter a message in the M column. The status on the selected serial number will then be updated to Service/Calibration in progress in the Serial numberA serial number is a number that is used for traceability for parts on entity level./BatchA batch is the set of components/products manufactured at the same time and made from the same original material. procedure. The message will also be available there, and in other parts of the system. Thereafter, the maintenance or calibration can be carried out, and upon reporting, the status of the tools is reset.
You can create a maintenance order on one or more rows by checking Create maintenance order and selecting Run.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PlannedMaintenanceList.png)](../../../../Resources/Images/TrainingMaterial/PlannedMaintenanceList.png)
There several useful links in the procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PlannedMaintenanceLinks.png)
You can link directly to the Report maintenance procedure from the list in order to report maintenance of the selected tool.
You can also link directly to Register maintenance order from the list, in order to create a maintenance order. The procedure is then opened, and you can see the order right away and handle it accordingly.
It is optional to use maintenance orders. That is, you can also report maintenance without a maintenance order.
> Tip! By unchecking all alternatives under Trigger type, under Settings, you will see all maintenance items even if the limit has passed. This is useful if you want to see all your maintenance items.

#### Report maintenance
The Report maintenance procedure is used to report maintenance, but not maintenance orders, if you use it. A maintenance order is basically a manufacturing order, and is reported with regular procedures for this.
Each reporting of maintenance is assigned a “service number”, a consecutive number. This number is searchable, and if necessary the reporting can be updated by entering the consecutive number.
In the header of the procedure you can see instructions for the maintenance and any linked files.
In the Short comment field you can enter a shorter general comment relating to the reported maintenance. It is also possible to write a longer comment under the Comment button, and link files under the Files button.
The form that is linked to the maintenance will be used during the reporting. If the form contains rows, complete the reported values and the rows’ status will be updated accordingly. Rows that are checkboxes are best reported by setting the status on them, as the box is checked automatically. If you change the maintenance status for the whole form, a control question is shown asking if the rows that are not reported should also be reported. You can also enter a comment for the reporting of each row and see instructions per row.
If a tool (master) is linked to the form or if you link such a tool during the reporting, you must select a serial number for the tool in question.
There are two different statuses for the reporting:
- Reporting status – this status has the steps Not started, Started, and Finished. This status on the main row is updated automatically when you report the other rows.
- Maintenance status – this status has the steps OK, Not OK, and OK with action. This status is also automatically updated as the Status on the rows changes to OK or Not OK. However, you can manually change the status if necessary. The step OK with action has no function yet. However, it will later be possible to create an action that can be linked to the reporting.
On the header row in the reporting, you can manually select which status should be set on the serial number in the Serial number/Batch procedure after the maintenance has been reported. If something is wrong with the tool, that is, you can block it directly when reporting.
If there is a maintenance order linked to the maintenance, you can specify it to obtain the right form. It will also be completed automatically if you link from the maintenance order itself.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ReportMaintenance.png)](../../../../Resources/Images/TrainingMaterial/ReportMaintenance.png)

#### Maintenance log
In the Maintenance log procedure, you can view historical reporting items of maintenance and calibrations. There is a detailed and a total list with a few different presentations. In the list you can follow-up on performed maintenance items.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/MaintenanceLogTotal.png)
