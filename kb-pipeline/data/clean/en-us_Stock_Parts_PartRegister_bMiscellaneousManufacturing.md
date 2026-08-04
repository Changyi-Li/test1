### Miscellaneous
In this box you configure other settings regarding manufacturing of the part.

#### Production engineer
Here you select a person from the personnel records who is responsible for the part's BOM and routing. By using the button More information ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can see more information about the selected production engineer and his/her contact information. The button is displayed to the right of the field after you have selected a person.

#### Quantity/package
Indicates the quantity of the part that fits in a package when the part is manufactured. This field is empty by default. This means that one transport label is printed for the entire order quantity. If you enter a quantity/package, a transport label will be printed for each package that has been reported as finished on the manufacturing order. The quantity is displayed in the unit selected on the main row, but it will be saved in the standard unit. A maximum of six decimals is allowed.

#### Calculated quantity
You can enter a quantity that should be selected by default for the part in pre-calculations. If the option Warehouse is installed in the system, it is mainly the value you enter here that will be used. If no calculated quantity is entered, the part's order quantity for the warehouse you are working in will be used instead.
In systems without the Warehouse option, the system setting Keep order quantity and calculated quantity in sync determines if values for the order quantity and calculated quantity should be kept in sync.

#### Packaging properties
If you are using the option Advanced stock management, you can enter packaging properties that will be used to determine the maximum size of packages/packaging that can fit in a location.
- Packaging part – Part number for the packaging.
- Length, Width, and Height – In these columns you can enter measures used to specify how large the packaging part is.
- Weight – Here you can enter a maximum weight for the packaging and its contents. This weight is used during putaway to make sure the location is not overloaded.
These measurements and this weight are used for the putaway during arrival to stock from the manufacturing.

#### Default transport label
This field determines the type of transport label selected by default to print for the part in the manufacturing. This setting applies for all part types, except for Fictitious. Yes, select at printout is selected by default. The options available as default transport label in the field are: None, Transport label – A4, Transport label – A5, Label, or Transport label – Grouped.
By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) next to the field you can select which type of transport label should be default for different events in the manufacturing. You can also select from you own transport label variants created in the Document templates procedure. The different events for which you can select transport labels: Transfer to stock, Prior to reporting, Operation in progress, Rejection, and Shipped subcontract. If you make one or multiple choices of transport label under this button, this will override the transport label selected, if any, in the Default transport label field.

#### Material enough for
By clicking this button you access a dialog where you see how many of the part in question (the part number selected in the procedure) that can be manufactured, based on the available stock balance of the included material (current balance minus cleared quantity).
In the Enough for column you see how many parts can be manufactured based on the materials’ available balance. Please note! If an included/incorporated material has 0.00 as the entered quantity in the BOM and routing, this will be shown as an infinity sign ∞ in that column. You also see the Lead timeNumber of days between ordering date and delivery date. Normally used for purchased parts. of the material and whether or not it is Ordered.
You can also show or hide included/incorporated parts of the Fictitious types. This is done using the Show/hide fictitious parts button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeFictitious.png) on the function menu in the dialog. This is done in order to see how many parts the material will suffice to when you include the incorporated materials used in the fictitious parts as well.

#### Included in
Here you see in which manufactured parts this part is included.

#### Consists of
Here you see which manufactured, purchased, and fictitious parts, this part consists of. If the Tools & Maintenance option is installed, you will also see the tools of which the part consists, that is, the tools used in the manufacturing of the part.

#### Alternative part
Here you can add alternative parts. These parts are displayed by default when changing part on a manufacturing order. These parts are also shown as an alternative (if there is an available balance) when there are material shortages in the material clearance. If an alternative material has been entered in the BOM and routing, that will override these materials and they are instead shown as alternatives.

#### Manufacturing order log
By clicking this button you access a log containing reported manufacturing orders for the part in question. If you have installed the option Warehouse, the statistics is shown for the selected warehouse.

#### Weight calculation
By clicking the Weight calculation button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) you access a calculator where you can create a weight calculation for the part. The weight calculation works as a template which has values already entered. It is used for material rows in BOM and routing and in manufacturing orders. For material rows in the BOM and routing and Register manufacturing order procedures, you find a corresponding function for weight calculation where you can display the part’s weight calculation template, make changes, if needed, and choose to apply it to the material row.
You select Type of profile in the calculator. You can select among: Area, Flat bar, Hexagon bar, L-profile, Round bar and Weight per unit.
Calculation formula for type of profile
- Area – Calculated as: Area x Length x Density.
- Flat bar – Calculated as: ((Length x Width x Height) - (Length x Inner width x Inner height)) x Density.
- Hexagon bar – Calculated as: (Length x 1.5 x Diameter2 / √3) x Density. Where the Diameter is measured between two sides according to this [illustration](../../../../Resources/Images/SubProjects/Hexagon.png).
- L-profile – Calculated as: Length x (Width + Height - Thickness) x Thickness x Density x Factor.
- Round bar – Calculated as: (((π x Diameter2 / 4) x Length) - ((π x Inner diameter2 / 4) x Length)) x Density.
-    
Weight per unit – Calculated as: Weight per unit x Length x Width. Weight per unit is used when you know the weight in kg for a piece of a material with the length and/or width 1000 mm, for example, length or width of a complicated aluminum profile.
Example: A certain aluminum profile weighs 2 kg per meter. You then enter 2.00 kg as Weight/unit. If the length of the material is 2 meter, you enter 2000 mm as Length and 0.00 mm as Width. The weight will then be 4.00 kg. If you enter 0.00 mm as Length or Width, that factor will be left out. If you enter both a Length and a Width > 0, the Weight/unit will be = kg/m².
You can select a Material registered in the Material and densities. You will then get a default Density shown in kg/dm3 according to the settings configured for the material in the procedure mentioned. But you can also enter a density of your own without first selecting a material.
You add a calculation row in the calculator and enter Position, Drawing number, Quantity, and the different measures from the drawing. The different measures for Length, Width, Height, and Thickness, should be entered in mm. The Area is entered in mm2. The measures which can be entered are based on the selected type of profile. If you have selected an L-profile, you can also enter a Factor in percent, with which the weight will be multiplied. The factor is used to adjust for material in radius for L-profiles. The default factor is 2.00 percent. The calculated Weight in kg, is shown on the row.
