### The Rows tab
The Rows tab in the procedure shows the order rows reported as arrived in the Report arrival procedure. Here you find information about arrived quantity and quantity left to inspect, the delivery status of the order rows, inspection instructions/inspection documents, and already approved/rejected quantity of the parts. You also see if the parts are traceable, and the supplier's part number, and the revision of the part.
The order rows subject to receiving inspection (that is, order rows with quantity left to inspect) are the ones loaded to this list. You can enter unit, approved quantity, location, and rejected quantity. The part's locations on the order row are shown in the Location box under the tab.
By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the function menu, you can go to related procedures for the marked order row
> Parts with mandatory control measurement are blocked at receiving inspection. Saving is not possible until you have reported measuring data. For traceable parts, only a warning is shown.

#### Unit
Here you see the unit of the approved/rejected quantity. You can change to an alternate unit (provided that alternate units have been registered for the part in question) if you wish to enter the quantity in another unit.

#### Approved quantity
Here you enter the total quantity of parts (in the selected unit) on the order row that has been approved during the receiving inspection.
If there is a measuring plan for the part (entered in the Part register procedure for purchase parts and for the operation in the BOM and routing procedure for subcontracts), a planned measuring should be performed and reported before you report the receiving inspection for the approved quantity. For subcontract purchase order, a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is shown in the field, as long as the measuring is not performed and reported. If the measuring is mandatory (determined by the measuring plan), the reporting of receiving inspection is blocked ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) until the measuring is performed and reported. For purchase of parts, a warning ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) is shown in the field, as long as the measuring is not performed and reported. When a measuring is mandatory (determined by the measuring plan) a warning will still be shown ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) as long as the measuring is not performed and reported, and until the time it is reported the arrived balance will be blocked and cannot be used. By using the Go to procedure button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) on the order row or on the function menu, you can go to the Report measuring data – Purchase procedure for purchased parts and report measuring of the parts on the marked order row. For subcontracts you will instead be linked to the Report measuring data – Manufacturing to report measuring data.

#### Rejected quantity
Under the button Rejected quantity ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you enter the rejected number of parts (in the selected unit). This button is visible if the approved quantity is not as great as the arrived quantity. It is then possible to register a rejection. It is here mandatory to select a rejection cause if you enter a rejected quantity. You can also enter comments and link files to the rejection. A comment can be mandatory is it is configured for the rejection cause. These comments are printed on transport labels for the rejected parts.

#### Instruction
By clicking the Instruction button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) you can read instructions for the receiving inspection, if such instruction has been entered.

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png) you can see inspection documents linked to the receiving instructions, if such documents have been entered.

#### M
By using the Go to Report measuring data button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png), you can go to the Report measuring data – Purchase procedure for purchased parts and to Report measuring data – Manufacturing procedure for subcontracts, and there you report the measuring of the parts on the marked order row.

#### Delivery instruction
By clicking the Delivery instruction button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) you can read instructions for the delivery of the order row, if such instructions have been entered.

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png) you can see linked delivery instructions, if such documents have been entered.
