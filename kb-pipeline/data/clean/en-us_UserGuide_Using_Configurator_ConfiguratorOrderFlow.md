### Order flow using the configurator

#### Quote and customer order
When you register a quote or a customer order for a part which is linked to a configuration group, you will see a button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png) in the Configuration column on the row. The configuration window where you do the actual configuration will automatically open, unless you have deactivated this function on the part. In that case you should use the above mentioned button to open the window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfiguratingWindowGuide.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratingWindowGuide.png)
If there is a default template on the part it means that options and variables now have been entered under the Guide tab according to the template. It is possible to select a different template or load settings from an earlier quote, customer order, or manufacturing order, before you go ahead and select options and enter variable values in the sections. It is always possible to save the current configuration as a template to reuse.
To the left you can expand a navigation tree. This is useful if the configuration is extensive. To the right you can see the descriptions which have been added for the field which is active.
The result of the configuration is shown under the Result tab. There you can select which information to display. You can also enter comments for each option and variable and select where to show them. It is possible to adjust prices and discounts.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfiguratingWindowResult.png)](../../../../Resources/Images/TrainingMaterial/ConfiguratingWindowResult.png)
You can run the CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. and calculation when the configuration is valid by clicking the button Confirm, but do not close the window ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinishedBox.png). The result of CDT and the standard price is shown on the order row in the main window behind the configuration window.
When you are done you confirm the configuration with the button Confirm ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png). This closes the configuration window and updates the price on the order row. A sub-row is automatically created which displays information about the configuration.
On documents there is as special document section where you can see the configuration according to your settings.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfigurationDocumentComponent.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationDocumentComponent.png)
If you have configured that the part should have serial numbers, this will be handled in the same way as for parts without configuration.

#### Manufacturing order
You create manufacturing orders in the same way as for regular parts. The most common way to create manufacturing order for configured parts, is to create it directly from customer order. The Net requirement calculationYou use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. and Requirement calculation procedures handle the creating of a correct manufacturing order suggestion based on the configuration.
The manufacturing order you create functions as a normal manufacturing order. Information about the order being configured is shown with the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png) in the Manufacturing order info. Information about the configuration is shown when you click the button.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfigurationMOrderInfo.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationMOrderInfo.png)
The configuration is shown on order documents according to the settings you made on option lists and variables and in the document settings. Configured instructions are also shown.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfigurationMOrderDocument.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationMOrderDocument.png)

#### Purchase
Purchased parts can be configured on a customer order. When you create a purchase order for these rows the information will be transferred to the purchase order and be shown on the documents.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfigurationPOrderDocument.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationPOrderDocument.png)

#### Changes
If you want to change the configuration on a registered manufacturing order, these changes are made from where the configuration was made, which in most cases is on the customer order. When you save the change, for example in the Register customer order procedure, the following takes place to make the modification affect the manufacturing order:
The procedure Synchronize with BOM and routing is automatically opened and there you have to check and confirm the changes on the manufacturing order. This is done by using the button Run the synchronization check ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) (Ctrl + R).

#### Version management
To handle changes in the configuration group which is already used in the order system, the system will automatically create a new version of the configuration group, a so-called snapshot.
This new version is not created when you make a change in the configuration group. It is created the first time you use the configuration group in the order system after the change was made.
If you open the configuration on an order after such a change, then you will see the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_information.png) below the Warnings button in the top right corner in the configuration window. You can now either keep the order as it is with the old configuration group, or you can update the order with the new version of the configuration group. This can then be done by using the button Synchronize with configuration group ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) to the top left of the window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfigurationGroupChanges1.png)](../../../../Resources/Images/TrainingMaterial/ConfigurationGroupChanges1.png)
> After a synchronization you should check that the configuration on the order is correct.
After making major changes to a configuration group you might need to create new configuration groups and link to the parts. On existing orders you will then see a different warning in the configuration window.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ConfigurationGroupChanges2.png)

#### Aftermarket
In the product register (the procedure called Serial numberA serial number is a number that is used for traceability for parts on entity level./BatchA batch is the set of components/products manufactured at the same time and made from the same original material.) you can enter additional information on each delivered unit via a serial number. Serail numbers can be created in connection with registering customer order. The product register supports follow-up and handling of e.g. warranty commitment, claims, supply of spare parts, repairs, etc.
The product register is especially useful when using the product configuration and when variations in the execution/design might vary from unit to unit.
