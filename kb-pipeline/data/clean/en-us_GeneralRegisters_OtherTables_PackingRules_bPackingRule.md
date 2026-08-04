### Packing rule
In this box you register packing rules and configure their settings.
By using the buttons in the function menu you add, insert, and delete packing rules row by row. You can also copy (clone) packing rules.
You name each packing rule.

#### Allow multiple delivery notes per pick list
In this column you decide if multiple delivery notes per pick list should be allowed or not. Yes is selected by default.
If you select No in this setting, you will receive a warning for customer orders on the linked customers for which the setting Apply comprehensive delivery note activated. This warning is shown in the Delivery planning procedure (list types Picking plan and Picking in progress), the Pack for delivery procedure, and the Report delivery procedure (list type Via pick list).

#### Check if package structure is missing
This setting you configure a check to see if packaging part rows are completely missing in pick lists when delivery reporting via pick list. The option Do not check is selected by default. No check will then be made.
The other options available are Check and warn or Check and mark as error. These options will activate a check in the Report delivery procedure (list type Via pick list. If it is set to warn, a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) will be shown on the order rows. If it is set to mark as error, a warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) will be shown on the order rows. This will make it impossible to save the delivery reporting in that procedure.

#### Add packaging part rows when reporting delivery
Here you decide if and how the packaging parts should be added to delivery rows in the Report delivery procedure, list type Via pick list.
If you select the option Add packaging parts from package structure, all packaging parts in the package structure will be added to separate delivery rows below the order rows.
The default option is Add packaging parts linked in part register. This option means a linked packaging part will be added as a sub-row to the part on the order row. It then works in the same way as If you do not have any packing rules in the procedure.
If you select the option Do not add packaging parts, no packaging parts will be added to delivery rows, regardless if they exist as linked to parts or in package structures.

#### Other package number series
Under the Other package number series button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can select which packaging type the package number will be applied to. The default there is no packaging type has a selected number series. The following packaging types are available:
- Unspecified
- Outer packaging
- Inner packaging
- EUR pallet
The following package number series can be selected depending on which package number series are activated in the Number series procedure.
- No value – this is the default option.
- SSCC package number
- OSCAR (Odette) Package number (OD)
- DUNS Package number (UN)
- JIPDEC Package number (LA)
