### Cost factors
This box is found under the Costs tab. This tab is not active for subcontract work centers. You can add an unlimited number of cost factors. These factors will become available to select for operations of the work center in the BOM and routing. From the start there is a cost factor for unit cost and setup cost. This default cost factor can be modified in the list.
A cost factor consists of three components that you can name using the three system settings Heading for cost factor 1, 2, 3. For example, you can name them "Machine", "Salary + Soc", "Fixed MO", or something else. By using the system setting Staffing affected cost factors, you can select the cost factor(s) that are costs for staffing. By using the system setting Default cost factors, you can select which types that will be selected by default in pre-calculations.
In the Pre-calculation procedure the cost is calculated for the operation according to the following formula:
(Setup time in hours × hourly cost for cost factors that are not staffing affected + setup time in hours × staffing factor × hourly cost for staffing affected cost factor) + (unit time in hours × hourly cost for cost factors that are not staffing affected × quantity + unit time in hours × staffing factor × hourly cost for staffing affected cost factor × quantity).
Quantity = quantity on operation + extra % + setup quantity.
Please note that you can enter a staffing factor for setup and a staffing factor for unit for an operation in the BOM and routing. This staffing factor will then override the staffing factor registered for the work center.
For the cost factor determined by staffing you enter a man-cost for staffing factor as 100%, regardless of the staffing factor entered for the work center or operation in the BOM and routing.
Sustainability
For sustainability calculations, you can enter current and future power and other emissions for your own work centers. These values are used in sustainability calculations and simulations of modifications in material in BOM and routing.

#### Setup and Unit
With these checkboxes you determine if the setup cost and/or unit cost should apply for the cost factor. These alternatives become available for operations in the BOM and routing. On the rows you can configure if these should be checked by default.

#### Cost factor 1-3
For each component in the cost factor you can enter a current and a future price per hour. You should enter this price in the company currency.

#### Power (Current)
Here you enter the machine's (work center's) current power in kW. The power is then multiplied by the operation's time to get an energy consumption.
Only include the work centers that are connected to the power grid with a three‑phase connection or more (direct‑connected machinery).
Find the machine’s maximum effect/power rating, which should be available on the machine’s nameplate or in the instruction manual. (This value will be higher than the machine’s actual effect/power usage, since the machine normally operates at a lower level during regular operation. You can therefore enter a value of 70% of the maximum rating to obtain a value that is closer to real operating conditions.)
The actual effect/power consumption can be measured by an electrician or by a company specializing in measuring machine power usage.

#### Other emissions (Current)
Here you enter the machine's (work center's) current emissions in kg CO2e/h. All work centers that emit green house gases to the atmosphere must be added here. Find out how many kilograms of CO2e per hour the work center emits on average and enter that value here. Examples of types of production equipment referred to are: welding equipment, laser cutters, or ovens that use gas.

#### Power (Future)
Here you enter the machine's (work center's) future power in kW.

#### Other emissions (Future)
Here you enter the machine's (work center's) future emissions in kg CO2e/h.

#### Comment
Here you can enter a comment that e.g. describes how you have calculated the prices entered in the cost factors.
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
The files can, e.g., contain bases and calculations for cost factors.
