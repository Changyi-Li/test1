### Using tools in BOM & routing and in manufacturing orders
Tools can be linked to operations in BOM and routings, and then be handled in manufacturing orders.

#### BOM and routing
When creating BOM and routing for parts, tools can be linked to operations in the same way as material rows. In most cases, the field Setup quantity is used to enter how many tools that are needed for the operation. On rows with reusable tools, you find a field where you enter if the tool should be returned in an operation other than the one in which the withdrawal is made. You also find two fields where you enter the number of details that are manufactured per cycle as well as the tool's cycle time. These values are required in order for the counters on the tools to be updated in the serial number register when the operation is reported. The value on these counters in the serial number register can in turn be used to trigger different maintenance items of the tools.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsInBOM.png)](../../../../Resources/Images/TrainingMaterial/ToolsInBOM.png)
> Tip! In the Level list procedure, you can see in which BOM and routings the tools are included. In the Material list procedure, you can edit data on the tool rows in the same way as for included material. There you can also exchange one tool for another in the BOM and routings in which it is included.

#### Manufacturing order
In a manufacturing order, you can add and delete tools in the same way as material. A reusable tool is displayed on two rows in the material list in the order. One row for withdrawal and one for return. The reservation date on the withdrawal row is loaded from the start date on the operation. The reservation date on the return row is loaded from the finish date. The tool's Quantity per cycle and Cycle timeCycle time is the productive time in the operation in which the unproductive time is not included. Cycle time plus Ineffective time adds up to the unit time for an operation. can be adjusted on the order if you need to make a temporary change.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsInMOrder.png)](../../../../Resources/Images/TrainingMaterial/ToolsInMOrder.png)
> Tip! You might need to configure settings regarding Allow automatic withdrawal for the tools when they have serial numbers. This will facilitate the reporting of withdrawals and returns. This can be configured in the part template in the Part template procedure. In the structure map in order procedures, you find a button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_tools.png) that is used to show or hide tools. There you also find the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_search.png) that is used to search for tools in the structure map.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsInStructure.png)

#### Manufacturing order document
In the Document templates – Manufacturing order procedure, you find settings that determine how tools should be shown on order documents. You can use a separate tool list by creating a variant of an existing document where you configure to only show tools.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsMOrderDoc.png)](../../../../Resources/Images/TrainingMaterial/ToolsMOrderDoc.png)

#### Priority planning, priority plan list, pool planning
On the operation rows in the priority plan, you find new columns with information about tools. In the T column, you see if the operation has tools and if they are cleared. You also find columns that show part number and tool name of the first tool that is linked to the operation.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsInPriorityPlanning.png)](../../../../Resources/Images/TrainingMaterial/ToolsInPriorityPlanning.png)
If you want to filter the operations, to be able to coordinate processing based on tools, this is made in the same way as for material.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsFilterMaterial.png)

#### Managing preparation of tools
The Manual operation status function can be used to create a flow to order the preparation of tools, and a confirmation that the tools are available.

#### Reporting tools on manufacturing orders
There are several possible combinations of settings that can be used when reporting tools on manufacturing orders – for example, if the tools should be manually or automatically reported when the operations are started and reported. Some of these settings work better or worse together. The settings below affect the reporting of tools.
> Please note! It is important that you carefully consider how you want to report tools.
System settings for manufacturing:
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsSettings1.png)](../../../../Resources/Images/TrainingMaterial/ToolsSettings1.png)
System settings for time recording:
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsSettings2.png)](../../../../Resources/Images/TrainingMaterial/ToolsSettings2.png)
Settings for work center:
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsSettings3.png)](../../../../Resources/Images/TrainingMaterial/ToolsSettings3.png)
Settings for part (can also be configured via part template):
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsSettings4.png)](../../../../Resources/Images/TrainingMaterial/ToolsSettings4.png)
Suggestions of how to handle and configure settings for tool reporting
Handling and settings depend on if you want to report tools manually or automatically.

#### Manual reporting of tools
If your company has a tool department that handles withdrawal and return of tools, then manual reporting can be good to use:
-   
Turn off automatic withdrawal and return in the system settings.
-   
Make withdrawals in the Pick listA pick list is a list of parts/products which should be picked from stock for a manufacturing order or a customer order. and Report pick list procedures.
-   
Make returns in the Withdrawal list procedure.

#### Automatic reporting of tools when recording
If you record operations in the Recording terminal procedure, in the Time recording module, and want to automate withdrawal and return:
-   
Activate the setting Allow automatic withdrawal in the part register for tools with serial number where you find it convenient.
-   
Activate the system setting Return reusable tools when operation is reported as finished. (The logic behind this is that the return will be made automatically when the remaining quantity reaches zero on the returning operation. The logic has one condition – no employee can be clocked-in on the operation.)
There are two alternatives to choose from when it comes to withdrawals:
Alternative 1:
-   
Activate the system setting Automatic reporting of tools.
-   
Configure the Suggest total setup qty at first automatic material reporting system setting to For tools. With this setting, the withdrawal does not take place when clocking in, rather, when first reporting the quantity for the operation. (This is done to avoid problems if you perform partial reporting of quantity in manufacturing orders.)
Alternative 2:
-   
Activate the setting Suggest withdrawal of tools at start of operation. The operator will then see a reporting window when clocking-in on the order. He/she can then sign for the tool withdrawal. The manufacturing order is recorded as usual.

#### Automatic reporting of tools without recording
If you use the reporting procedures in the Manufacturing module to report operations:
-   
Activate the system setting Automatic reporting of tools.
-   
Activate the system setting Return reusable tools when operation is reported as finished. (The logic behind this is that the return will be made automatically when the remaining quantity reaches zero on the returning operation. The logic has one condition – no employee can be clocked-in on the operation.)
-   
Configure the Suggest total setup qty at first automatic material reporting system setting to For tools. The withdrawal then takes place at the first reporting of quantity on the operation, and not during clock-in. (This is done to avoid problems if you perform partial reporting of quantity in manufacturing orders.)
-   
Deactivate the setting Suggest withdrawal of tools at start of operation.

#### Batch record orders using the same tools
The same tool will be withdrawn to all operations in a batch which are using the tool. The withdrawal takes place via automatic reporting upon the first partial reporting, or via the Material reporting window, depending on the system settings as stated above. Please note! The tools are always returned automatically upon stopping work when recording a batch. If there is a remaining quantity on the operation at the time of the return, the remaining quantity on the tool will be reset to make it possible to withdraw it again when the order is started again.
Please note! The add to batch function cannot be used yet. Manual withdrawal and return in other procedures is not supported if operations will be batch recorded.

#### Logging of number of cycles and cycle time
For tools with serial numbers that are withdrawn to an operation, the Number of cycles is automatically logged on the serial number. You can see the log in the Serial numberA serial number is a number that is used for traceability for parts on entity level./BatchA batch is the set of components/products manufactured at the same time and made from the same original material. procedure. The logging takes place automatically when quantity is reported on the operation. Cycle time is also logged on the serial number if a cycle time has been entered in the BOM and routing or in the order.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsLoggingTimeCycles.png)](../../../../Resources/Images/TrainingMaterial/ToolsLoggingTimeCycles.png)
