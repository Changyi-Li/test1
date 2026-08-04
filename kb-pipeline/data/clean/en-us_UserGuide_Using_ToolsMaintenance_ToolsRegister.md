### Tool register
In Monitor ERP, you handle tools in the Part register procedure by using basic types for tools. This means that practically all procedures that handle parts also handle tools.

#### Part template
In the Part template procedure, you find basic types for tools. To be able to handle tools, you must first create part templates for the types of tools and equipment that you want to use. You must create at least one template per basic type.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PartTemplate.png)](../../../../Resources/Images/TrainingMaterial/PartTemplate.png)
Basic types for tools
There are three different basic types for tools. Make sure that you choose the correct basic type for the tools since it determines the available functionality:
- Consumable – This type practically works in the same way as regular parts. This is used for tools that are consumed when they are reported. This is often used for consumable tools, supplies, and spare parts.
- Reusable – This is probably the most frequently used basic type. Tools of this type are handled via withdrawal from and return to stock. Reusable is always used if you want to perform maintenance and calibration. Then you must also use traceability on serial number, which is added in the part template. You can create several part templates for different types of tools, for example, measuring tools, fixtures, and machines.
- Tool list – This type is primarily used to create fictitious tool lists that can be reused in several BOM and routings. More functions will be developed for this basic type.
> Tip! It might be a good idea to create separate LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. presentations for tools and regular parts.

#### Part register
You register tools in the Part register procedure. Most of the settings that can be configured for regular parts can also be configured for tools. Many settings can be set by default via the part template, for example, traceability on serial number and planning settings.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ToolsInPartRegister.png)](../../../../Resources/Images/TrainingMaterial/ToolsInPartRegister.png)
> Tip! For consumable tools, it might be a good idea to use the planning method Stock refill. Entering reorder point, order quantity, supplier, and lead time provides easy purchase management in the Stock refill – Purchase procedure.
