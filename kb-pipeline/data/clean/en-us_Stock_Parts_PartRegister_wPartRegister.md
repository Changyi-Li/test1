## Part register
In the Part register procedure:
- You register new parts.
- Update existing parts.
- Delete or deactivate old parts and parts no longer in stock.
In the part number field on the main row you enter or select a part in order to load an existing part. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature you can search the part register. If you want to create a new part you can enter a unique part number or leave the part number field empty. Then the next available part number will be loaded from a number series when you save. The Name field is mandatory for a new part. The name is locked for an existing part, but it is possible to unlock it for editing by clicking the padlock button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Padlock.png) in the field.
The part register is the most important and fundamental register in Monitor ERP. A part can for example be: purchased, sold, manufactured, requirement planned, stock counted, stock valuated, product calculated, linked to price lists, used for statistic purposes.
In other words, many of the functions have to do with parts. The part register consists of a great deal of different types of information that supports all the different functions. The primary information for a part is its part number, part name, unit, part type, and standard price. In addition to this, there are different prices, planning settings, locations, grouping terms, order information etc. which can be entered for a part. However, it is not mandatory to enter all this information for a part. The basic principle is that it should be sufficient to only enter the primary information in order for it to be possible to use the most common functions in the system for example to manage orders. All other information that can be entered for a part is intended for more advanced functions, and to use the system at a more advanced level.

#### Environment and sustainability
To follow up on environmental standards and sustainability requirements, you can enter data about carbon dioxide equivalents and part contents (for example, chemical usage) under the Sustainability tab.
Copy part to new part using Save as
It is possible to create/register new parts by copying an existing part using the Save as button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save_as.png) (Ctrl + Shift + S) on the toolbar of the procedure. The information copied by default when using "Save as" is the information registered for the part in the part register. For manufactured parts, data about operations and incorporated material from the BOM and routing procedure is also copied. Therefore, it is recommended that you create a part that can be used as a template for new parts which you can then register by using Save as. The following data/information is copied to the new part:
- General and Stock – data from the General and Stock tabs is copied, except for Block/Notify info.
- Block/Notify info – information from Block/Notify including the message is copied.
- Planning – data from the Planning tab is copied.
- Manufacturing – data from the Manufacturing tab is copied.
- Purchase – data from the Purchase tab is copied (applies to purchased parts).
- Sales – data from the Sales tab is copied.
- Budget – data from the Budget tab is copied.
- Extra fields – data from the Extra fields tab is copied.
- Operations – data from the Operations box in the BOM and routing procedure is copied (applies to manufactured parts).
- Measuring plan – measuring plans entered under the Purchase tab are copied.
- Operations – data from the Operations box in the BOM and routing procedure is copied (applies to manufactured parts).
- Configuration information – data from Configuration under the General tab is copied (applies to configured parts).
Delete or deactivate parts
An old part that is no longer in stock can be deleted, or you can deactivate it if you wish to keep it in the database. By using the Delete button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png) (F6) on the toolbar of the procedure, a dialog opens where you can choose Delete or Deactivate. A deletion check is run in the background to check if it is possible to delete/deactivate the part.
If you choose Delete or Deactivate and it is not possible to execute, the Apply button in the dialog box becomes unavailable. By clicking the respective info buttons ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_information.png) in the dialog box, you see information about the dependencies preventing the deletion/deactivation of the part.
When it is possible to delete (or deactivate) the part, the Apply button is active.
If it should be possible to delete the part, there can not be any dependencies such as, the part being on an order, material rows in BOM and routing, has a stock balance, etc. To be able to deactivate the part, it cannot be in any active orders (status < 9) and the part also cannot have a stock balance.
When you deactivate a part it is given status 99 (Inactive) and is blocked regarding registration and reporting on new quotes, customer orders, inquires, purchase orders, manufacturing orders, BOM and routing, new serial number/batch number, options in configuration, and customer agreements. Deactivated parts do not show up in the Lookup feature (F4) in part number fields, but you can load deactivated parts if you enter the entire part number. If you load a deactivated part here, you can in a dialog save it as a new part (the same function as Save as) or reactivate it, or just load the part as it is. It is not possible to modify any information for an inactive part which you have loaded in the procedure. You can also reactive the inactive part using a button next to the status field.
In the Delete parts procedure you can delete or deactivate multiple parts at a time in a list.
With the list type Reactivate inactive parts in the Delete parts procedure you can reactivate multiple inactive parts at a time.
Extra fields
You can add extra fields for this procedure in the Extra fields procedure. If such fields already have been created, these will be available under the Extra fields tab.
Prices for parts
Much of the information entered on parts regards different prices. That is why it is important to understand what the different prices on parts mean and for what they are used. Read more about this in the chapter called [Explanation of part prices](../PartPrices.htm).
Warehouse
If you have installed the option Warehouse, it is possible to save certain information per warehouse. The information which is saved per warehouse is: stock transaction log, stock count log, consumption statistics, annual budget, administrator, all settings under the Planning tab, and the default supplier in supplier links. When you register a new part, the entered information will be set on all warehouses. However, if you change something on an existing part, the information will only be changed for the selected warehouse. If you want to change warehouse to work in, you use the Warehouse button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) (Ctrl + Q) on the toolbar of the procedure. Here you can also select from which warehouses you want to show data in the procedure. Administrator and all planning settings can only be shown from the selected warehouse. [Read more about the option Warehouse](../../../UserGuide/Using/Warehouse/Warehouse.htm).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_log.png)
