### Header row

#### Order number
Here you can load an order number for an existing maintenance order. For a new maintenance order the order number is assigned when you save the order. This is loaded from the next available number in the number series for manufacturing orders. A maintenance order is a manufacturing order which is based on a separate order type of the basic type Maintenance.
> Please note! In the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature you also see regular manufacturing orders. If you load a regular manufacturing order in this procedure, it is not possible to make any changes to that order.

#### Serial number/Batch number
You create a new maintenance order for a serial number you first select here. When reporting maintenance orders, this serial number is suggested and then reported.

#### Maintenance
Here you select which maintenance should be performed by choosing a maintenance template. The maintenance templates you can choose among are those that have been linked to the part with the serial number in a maintenance plan. In the list in the field you also see in which maintenance plan the maintenance template is linked.

#### Part
Here you select the manufactured part which contains the BOM and routing that should be used in the maintenance. This is shown in the Operations box and the Material box, once you have saved the order. The default part here is the part configured to use the BOM and routing in the maintenance template. If no such part is entered in the maintenance template, the part with the serial number will be default.

#### Configuration
If the selected part is linked to a configuration group, a button for configuration of the order will be available. If the button shows this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Available.png) it means the configuration is incorrect or incomplete. By clicking this button you access a configuration window where you can configure the part. When you confirm the configuration using the button Confirm ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) in that window, the symbol on the button will change ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Button_Configuration_Done.png), to illustrate that the part is configured.
The part can have a default configuration determined in the part register, and in that case this configuration will automatically be loaded to the maintenance item.

#### Comment
Here you can enter a comment for the maintenance order.
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Variant code
Here you can enter a variant code in order to use variant codes for operation rows and material rows in the selected manufactured part.

#### Warehouse
This field is available if the Warehouse option is installed. Here you can select a warehouse for the maintenance order. The current warehouse is selected by default. If you choose a warehouse other than the warehouse to which the selected manufactured part belong, and then you save, the column called WH will be shown on all operation rows and material rows. In this column you find a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses_alt.png) with a tooltip. For operation rows it lets you know that the row belongs to a different warehouse, and for material rows it lets you know that the material will be withdrawn/deducted from a different warehouse.
