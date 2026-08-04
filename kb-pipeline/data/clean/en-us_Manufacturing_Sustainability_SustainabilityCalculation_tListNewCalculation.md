### The New emission calculation list
Under the List tab you see all selected manufactured parts for which you can perform the emission calculation if you chose the New emission calculation list type. You can check and adjust the quantity for distribution of setup times and also settings for terms in BOM and routing, as well as deselect parts that you do not want to include in the calculation. By clicking the Start calculation (Ctrl + R) button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) you start the calculation.
The Calculate CO2e value for configured parts system setting determines if CO2e values will be calculated for these parts.
> The times used in the calculation are the same times as are used for a manufacturing order or a pre-calculation. That is, it includes setup time, unit time, extra %, and setup quantity, for the operations.

#### Emissions
Here you see the part's calculated emissions in kg CO2e/unit.

#### Save
With this checkbox you decide if the calculated CO2e value should be saved to the Emissions field under the Sustainability tab in the Part register procedure.

#### Save calculation
With this checkbox you decide if the calculation should be saved under Emission calculations under the Sustainability tab in the Part register procedure. The most recent calculation is displayed and the older calculations can be seen under the Saved calculations button.
> We recommend that you always save the calculation if you have selected to saved the calculated emissions for the part.

#### Material
Here you see the material emissions in kg CO2e/unit.

#### Upstream transportation
Here you see emissions from transportation of purchased parts in the calculation. This is shown in kg CO2e/unit.

#### Production
Emissions from the own production. This is shown in kg CO2e/unit.

#### Subcontract
Here you see emissions from subcontracting in kg CO2e/unit. When calculating this value, the emission value entered for the subcontract part will primarily be used. If you have not entered a value for the subcontract part, the value entered under Other emissions for the work center will be used instead as a fallback.

#### Overhead
Overhead refers to the company's other emissions which have not been distributed to the other categories. This is based on values in the column called Distribute as OH in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Sustainability procedure.

#### Warnings (W)
If warnings exist after the calculation, you can click the Warnings button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) to view the warnings, if any. Go to each of the procedures and records in the warnings to enter the missing information. This way you rectify the problems causing the warnings and you will get a complete calculation.

#### Quantity
Here you see/enter the order quantity for the calculation. This is the entered order quantity for the part in the Part register procedure. Otherwise the quantity entered in the Quantity if order qty is missing setting, will be used.

#### Finish date
Used for conditioned BOM and routing. Finish date for the part.

#### Revision
Used for conditioned BOM and routing. Here you see the revision of the part.

#### Order number
Used for conditioned BOM and routing.

#### Customer
Used for conditioned BOM and routing.

#### Variant code
Used for conditioned BOM and routing.

#### Warehouse
Used for conditioned BOM and routing.
