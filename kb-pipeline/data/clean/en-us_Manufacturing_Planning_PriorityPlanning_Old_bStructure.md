### Structure – Former layout
You can maximize this box with the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_maximize_section.png) and you can minimize it with ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_minimize_section.png). Here you see the structure of included/incorporated parts in the registered manufacturing order. The order number is shown on the top level.
You can here move between included/incorporated parts (called nodesA node is an included/incorporated manufactured part on a certain level in a part structure. A level in the structure part can contain multiple nodes. The node on the highest level is called the main part (order).) in the structure using the cursor or the arrow keys ↓ and ↑ on your keyboard.
If you mark a part node in the structure, you see information about operations and material included in the part. This is shown in the boxes Operations and Material.
By using the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) (Shift + F8) on the function menu, you can expand and minimize all nodes in all levels in the structure.
By using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png), you can go to related procedures and load the order/part is marked in the structure.
By using the button Find ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search.png) (Ctrl + B) you can show or hide a search field where you can search for parts in the structure.
With the button Show all parts ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_no_structure_part.png) you decide if all incorporated/included parts should be shown. By default, such parts are not shown.
With the button Show all tools ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_tools.png) you decide if all tools should be shown. By default, tools not shown. This button is available if the option Tools and Maintenance is installed.
The buttons Show all parts ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_no_structure_part.png) and Show all tools ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_tools.png) have a memory function. If you activate one or both of the buttons, the same buttons will become activated in other procedures where they are available.
The button Lead timeNumber of days between ordering date and delivery date. Normally used for purchased parts. chart ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_lead_time_chart.png) is available in the procedures Manufacturing order info and Priority planning. This is used to display a lead time chart for the manufacturing order. The procedure Priority planning also has a lead time chart for the work center's operations under a separate tab.

#### Status (S)
Here you see symbols representing the order’s status or the part's order status.
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

#### Order/Part
Here you see the part number of the main part and the included parts. On the top level in the procedures Manufacturing order info and Priority planning you will here see the order number.

#### Planned quantity
Here you see the planned quantity of the part on the order.

#### Unit
Here you see the part's standard unit.

#### Comment (C)
The part's manufacturing comment is shown when you click the button, if it has a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png). If there is no comment, the button will instead display an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png).

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.

#### Configuration
Applies when the option Product configurator is installed. If a part on the order is a configured part you will in this column see the button Configuration ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png). By clicking this button you open a window with information about the configuration.
If there are variables in the configuration, you can by using the button Show variables ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_hidden.png) in that window choose to also show variables or only the selected parts in the configuration.
The More information button
By clicking the button More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you find the following columns in the standard mode. These can when needed be dragged out as columns that you place in the table.

#### Start date
Here you see the order's start date for the part.

#### Finish date
Here you see the order's finish date for the part.

#### New finish
If the Check delivery times (CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered.) is applied, this column is available. It displays date for New finish for the part on the order. New finish is calculated by the net requirement calculation.

#### Name
Here you can see the name of the part.

#### Part status (P)
In this column you see the status of the part. In the procedure Register manufacturing order, you can in this field also change the status of the part.

#### Revision
In this field you see the active revision of the part, at the time of the order registration. In the procedure Register manufacturing order, you can in this field also change the revision of the part.

#### Revision comment
In this field you see the comment for the part's active revision, at the time of the order registration.

#### Files
Here you see the files linked to the active revision of the part.

#### Drawings
If there are drawings linked to the part in the part register (at the time of the order registration), you will here see information about those drawings. By clicking the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button you see the drawing number, active drawing revision, comment, and files linked to the drawing's revision. In the Register manufacturing order procedure, it is also possible to add/delete drawings, drawing revision, comment, and files linked to the drawing's revision.

#### Traceability level (Tr.)
If the part has traceability, you will here see a symbol indicating the traceability level: Serial numberA serial number is a number that is used for traceability for parts on entity level. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/serialnumber_image.png) or BatchA batch is the set of components/products manufactured at the same time and made from the same original material. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/batch_image.png).

#### Serial number
If the part has traceability at serial number level, you will here find the button Serial number ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) under which you see the part's serial number and the number of serial numbers. The following applies:
- If the setting called Create serial no. at customer order for the part has been configured to No, then you will here see the serial numbers which were created when registering the manufacturing order (the same number of serial numbers as the quantity on the order).
- If the setting Create serial no. at customer order for the part in the Part register has been configured to At registration of order, you will here see the serial numbers which became created when the customer order was registered. But this only applies if the part has the lot sizing rule Linked requirement.
