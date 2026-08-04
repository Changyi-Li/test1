### Operations
In this box there is a table where you can create an operation list (routing) for the part selected in the structure map.
It is possible to add, insert, and delete operation rows by using the buttons Add ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5), Insert new row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_insert_row.png) (Shift + F5), and Delete ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6) on the function menu.
Using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) you can go to different procedures for the selected operation.
Using the button Expand all ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_expand_collapse.png) you can expand all instructions.
With the Summarize reported times button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_calculate.png) you can for the selected part in the structure show and update the operations' setup times and unit times with times from previously reported manufacturing orders. This button opens a window which is described below.
Summarize reported times
Under the Selection tab you select by finish date of operations and by part status, and you can configure different settings.
The Result tab becomes available after you have clicked the Select button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png). There you see a list with details about the manufacturing orders which the summary is based on.
You can select which setup and unit times should update the times of the BOM and routing. Operations on manufacturing orders are connected with the BOM and routing operation they should update by having the same work center and operation number. For a pool work center which always has different work centers in routing and on order, an operation ID is instead used as identifier.
You can choose to remove operations that differ too much from what is normal before saving and updating the BOM and routing.

#### The Selection tab
- Finish date of operation – Enter date interval for finish date of operation.
- Part status on order – This decides the part status on order.
- Minimum number of orders – Enter the minimum number of orders for the summary. The default value here is 1. If the number of orders are less than the entered minimum number, no summary will be made.
- Deduct planned setup time from reported time for operations without reported setup time – This setting is used if setup time is specified for the operation, but when you do not normally report it separately for the operation, but instead report int together with the unit time. The planned setup time will be deducted form the unit time and is presented as setup time. For operations where setup time have been separately reported, the reported times will always be left untouched.
- Update setup times by default – Determines if the Update setup column should be marked by default in the list.
- Update unit times by default – Determines if the Update unit column should be marked by default in the list.
- Only include finished manufacturing orders – Determines if only finished manufacturing orders (orders with status 4 or higher) should be included in the summary.
- Only include orders marked for mean price calculation – Determines if only orders which should get a mean price calculation will be included in the summary. In the Post-calculation procedure it is possible to uncheck this option for an order.
- Number of decimals – Determines the number of decimals. The default option here is 2 decimals.

#### The Results tab
By clicking the button with the plus sign ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_drill_down.png) you see order data with information about reported time and the order's quantity. You can choose not to include certain manufacturing orders in the calculation of average time for the operation.
- Setup time – Current setup time.
- Average setup time – Setup time calculated as an average value of reported setup times for the operation.
- Difference setup time – The difference is calculated as: Average setup time – Setup time.
- Update setup time – Check this box for the setup times which should be updated.
- Unit time – Current unit time.
- Average unit time – Unit time calculated as an average value of reported unit times for the operation.
- Difference unit time – The difference is calculated as: Average unit time - Unit time.
- Update unit time – Check this box for the unit times which should be updated.
- Close and update operation times – This button updates the operations with new setup times and unit times.

#### Expand row
By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_drill_down.png) to the far left on the row, you expand the row and can then see the instruction and the configured instruction which have been entered for the operation.

#### Warehouse (WH)
Applies if you have installed the Warehouse option). If you change to another warehouse you will see the WH column. On the rows which belong to another warehouse than the selected warehouse you will see a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses_alt.png) in the column. A tooltip for the symbol informs you of which warehouse the row belongs to. Values and texts in all columns for these rows are displayed in italics.
In many of the procedures you can change the warehouse which you will be working in by using the Companies/Warehouses button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_warehouses.png) in the toolbar of the procedure. It is also possible to generally change in which warehouse to work. This is applied to all procedures.This is done in the desktop backstage.. In registration procedures for quotes, inquiries, different orders, and invoice bases, you can in a field select to which warehouse the record belongs.

#### Row
Here you can see the row number of the operation. For each row added, one will be added to the number in this column. The row number cannot be edited.

#### Operation number
The operation number shows the sequence in which the operations will be run. The first operation that you register is given number 10, the next one is given number 20 etc. It is possible to edit the operation number. You can use the same operation number several times in an operation list (routing). This is useful e.g. in alternate BOM and routing. However, you cannot use the same operation number several times on the same manufacturing order. An operation number must be entered, otherwise you cannot save the BOM and routing. When you save, the operation list will become sorted by operation number.

#### Work center
Here you see/enter the work center that will perform the operation. Work centers must first be registered in the Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register procedure. The work center must be entered, otherwise you cannot save the BOM and routing.
If the selected work center is of the Subcontract type, a subcontract part will be created and linked to the operation when saving the BOM and routing. The subcontract part is the "data unit" in a subcontract, that is, you can update information for that part either from the subcontract or from the part register. The information updated for the subcontract part from the subcontract is supplier number (the part will get a supplier link to the supplier selected for the operation), supplier's part number, setup cost and unit cost, staggered subcontract prices and transport cost. The name of the subcontract part will by default be: "[part number of the BOM and routing] – [operation number]", for example, "895-21 – 20". You can link to the subcontract part in the Part register by using the button Go to procedure ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png) in the box when you have selected the subcontract in question. In the part register you can then enter additional information about the subcontract part.

#### Operation name
Here you see/enter the name of the operation in this BOM and routing. For a new operation the operation name is loaded from the selected work center, but you can change it if you do not want to use the default name. This field cannot be left empty.
> If the name of the operation is changed in the BOM and routing and you later on change the work center of the operation, then the operation name in the BOM and routing will not become updated. The purpose of this is that it is possible to enter specific information for a certain operation via the name of the operation. That is why this information will not be removed if someone should change work center for the operation. The same function exists for manufacturing orders. If the name of an operation is changed for a specific order, then that name will only apply on that order.

#### Translations
By using this button you can enter translations of the operation name. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Supplier
If the row refers to a subcontracting work center, you will see the supplier number which is entered for the work center. It is also possible to change to another supplier in this field. By using the LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature, you can search for suppliers of subcontractor type in the supplier register.

#### Delivery address
If the row concerns a subcontracting work center you can, by using this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), specify the address to which the subcontractor should send the goods after the work is performed. If you don't make a selection, then the Company alternative will be default, that is, the delivery address of the previous operation will be used. You can select another of the company's delivery addresses or another warehouse's delivery address. If the previous operation's warehouse is missing, then the delivery will be sent to the warehouse of the order. It is also possible to select a delivery address to Other customer or Other supplier.
If it is the final operation in the BOM and routing, you can select End customer on order instead. Then you shouldn't enter the address of a specific customer or supplier in the BOM and routing. The delivery address will instead be loaded from the linked customer order and be added on the manufacturing order. If no customer order is linked, the company's delivery address will be used instead. This dynamic solution can be applied if you deliver the same part to different customers.

#### Setup time
Here you can enter a setup time in the unit selected for the operation. The setup time is the operation time that is not dependent on the quantity. If you have entered a default setup time for the work center it will be shown here, but it can be changed.
You can also enter a setup cost, if any, for a subcontract if the row refers to a subcontracting work center. The setup cost is displayed in dark red.

#### Unit time
Here you can enter a unit time in the unit selected for the operation. It is the operation time that is dependent on the quantity.
If you in the column called Unit select any of the time units select quantity/hour, quantity/minute, or quantity/second, you can here enter the quantity of the part which is manufactured per selected time unit.
If the row refers to a subcontracting work center, you should instead enter the unit cost for the subcontract. The unit cost is displayed in dark red.

#### Cycle time
The cycle timeCycle time is the productive time in the operation in which the unproductive time is not included. Cycle time plus Ineffective time adds up to the unit time for an operation. column is shown if the system setting Use cycle time and ineffective time in BOM and routing is activated. The column Unit time is grayed out when this setting is activated.

#### Unit
Here you select the operation's time unit for setup and unit times. If you change time unit here, you will see setup time and unit time for the operation in the new unit instead. The default time unit is determined by the system setting Time unitTime units are units used to indicate the setup and unit times at BOM and routing. Normally, minutes or hours are used. for setup and unit time for operations.
If it is a subcontracting work center, you will here see the company currency or the supplier’s currency instead, but it can be changed. The default selection, company currency or supplier's currency, is determined by the system setting Default currency for subcontracts.

#### Ineffective time
The ineffective timeIneffective time is time which is necessary in the operation, but not directly productive. column is shown if the system setting Use cycle time and ineffective time in BOM and routing is activated.

#### Staggered subcontract prices
If the row refers to a subcontracting work center, you can enter staggered subcontracting costs under the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button. You can enter the current price and future price for unit costs, depending on the limit value for subcontract part quantity.

#### Overlap
In this column you can enter an overlap (OL) as a percentage. The definition to enter overlap is: "Quantity (%) left on this operation when the next operation should start". For example, if operations 10 and 20 should overlap each other, you set the desired overlap as a percentage for operation 10. In the example, 20% OL has been set on operation 10. Is possible to set the overlap from 0 to 100%.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/ol_percent.png)

#### Queue time
Here you can see/enter the queue time for the operation. The queue time that you enter on an operation row here will override the queue time entered for the work center. The work center’s queue time is shown in the next column. If you leave this field empty, it is the queue time for the work center that will apply. Depending on whether you apply day planning or hourly planning, the queue time is shown in work days or hours. If either capacity via schedule or hourly planning is used, then you can enter queue time in number of hours with two decimals. Read more about [Queue time in the Work center register](../../WorkCenters/WorkCenterRegister/bPlanningInformation.htm).

#### Queue time, work center
Here you will see the queue time entered for the work center.

#### Fixed lead time
You can here enter a fixed lead time in whole work days, if this should be used for the operation. 1 day as fixed lead time means that the start and finish date will be the same day. 2 days means that the start and finish date will be the two days following each other.
If this field is left empty, a dynamic lead time calculation is performed, but that lead time will not be displayed for operations in orders. The dynamic lead time is calculated using the operation time (setup time + quantity x unit time) in relation to the work center's capacity per day.

#### Only calculation
If you check this box, the operation will only be included in the calculation but not on the order. If you have material linked to an operation like that, the setting will also be activated for those materials.

#### Instruction (I)
Here you can see/enter an operation instruction. This instruction text will be printed on the manufacturing order documents.
By clicking this button you access a text editor where you can write and format text, insert images and signature, and hyperlinks, etc. When a comment/text exists, the symbol on the button will change from an empty speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_no_comment.png) to a filled speech bubble ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_comment.png).

#### Files (F)
By clicking the Files button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_link.png), it is possible to link different files related to a comment or an instruction for the record in question. When the setting Automatic printout is available for activation, you can choose to get the linked file automatically printed. Read more in the topic [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LinkFiles) about how to link files, automatic printout, and where linked files can be automatically printed. If there are linked files, you will see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_file_linked.png) on the button.
Here you can choose if you wish to print linked files automatically together with the manufacturing order documents. You can also choose if a unique file (copy) should be created of the linked file on the manufacturing order and if the unique file should be allowed to be opened in an external program in Windows. Read more about Link files in the section [General features](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm) in the online help function.

#### Measuring plan
By clicking the Measuring plan button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can enter a measuring plan for the operation. This applies to both internal operations and subcontracts. You create a measuring plan by adding one or multiple rows for measuring templates with measuring forms containing measuring points and instructions. These must first be registered in the Measuring forms and Measuring templates procedures.
You can also, in the Measuring plan, link a work center to a row with a measuring template and measuring form. This means, reporting of measuring data on the operation for that row in the measuring plan can only be performed by the selected work center. If the field is empty, the row with measuring template and measuring form will always be used regardless of which work center that reports measuring data.
The measuring plan can, when needed, be changed for the operation in a certain manufacturing order. You report measuring data for the operation on the manufacturing in the Report measuring data procedure in connection with reporting quantity on the operation in any of the Report operation, Report manufacturing order, or Recording terminal procedures.
Already reported measuring data for the operation can be taken out subsequently in the Measuring data log procedure.

#### Configured instruction (CI)
(This applies if you have the option Product configurator) Here you can enter a configured operation instruction. If there is also a regular operation instruction (I), this will be combined with the configured operation instruction on the manufacturing order documents.
By clicking the button CI you open a window where you can create a configured instruction per configuration group you add. You can enter variables by using the mouse pointer to drag and drop to the places in the instruction text where you want them. You can also manually enter a variable in the instruction text as [v:variable code]. You can create formulas from the available variables and add the formulas in the instruction text using drag and drop. It is also possible to manually enter a formula in the instruction text as [f:formula name]. Validations are made to make sure the entered variables and formulas are available.
You can test the outcome by using the button Preview instruction ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_preview.png) next to the instruction text.
Read more about configured instructions in the topic called [Basic data](../../../UserGuide/Using/Configurator/BasicData.htm) in the chapter about using the Product configurator.

#### Alternative work center
You can determine in which alternative work centers an operation in the routing can be run, according to a certain priority. By clicking this button you can enter work centers, with the first alternative on the first row, the second alternative on the second row, etc. On the rows you can enter unit time, setup time, queue time, and exception for staffing factor. You can enter subcontract work centers as alternative work centers.

#### Extra
If extra fields have been created for operation rows in the Extra fields procedure, this column is displayed. By clicking the button you can then use the extra fields for the operation rows in BOM and routing.

#### Time formula f(x)
(This applies if you have the option Product configurator) In the f(x) column you find the button Time formula ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_formula.png). This button opens a window where you can add formulas for unit time and setup time for the operation row. When a formula already exists, the symbol on the button will be different ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_formula_info.png). You can select one of three different functions for a time formula which will be taken into consideration when an order is registered for the part. It is possible to multiply, add, or replace the regular value with the result of the formula. Time formula also works for subcontracts. Read more in the section [Formulas](../../../UserGuide/Using/Configurator/Formulas.htm) in Using Monitor about the product configurator.

#### Supplier's part number
If the row refers to a subcontracting work center, you can enter the supplier’s part number here. This will then be displayed on subcontract purchase orders and subcontract delivery notes.

#### Number of machines/persons per order
Here you can enter an exception from the number of machines or persons per order which is entered for the work center.

#### Setup quantity
Here you can enter a fixed excess quantity for the operation. The setup quantity (the excess quantity) can be applied, for example, when a number of "test run samples" have to be run in order to setup a machine for production. Setup quantity can be used as an alternative to, or in combination with Extra % on the operation row.

#### Extra %
Here you see/enter a percentage for setup quantity or excess quantity.

#### Cost factor setup exception and Cost factor unit exception
Here you can enter cost factor exceptions for the operation in question. For setup time and/or unit time you can choose the regular cost factor or one of the exceptions for cost factors. These must be first registered for the work center.

#### Transport cost
If you have selected a subcontracting work center, you can here enter the transport cost for the subcontract, if any. The cost is entered in the company currency.

#### Staffing factor setup and Staffing factor unit
Here you can enter staffing factor exceptions for the operation. For setup time and/or unit time you can enter a staffing factor as a percentage that will override the staffing factor for setup time and unit time entered for the work center. This will be displayed in the Staffing factor, setup (WC) and Staffing factor, unit (WC) columns.
By using the system setting Staffing affected costs you can select the cost factors linked to the staffing. That way, the staffing factor will affect both the loading and the calculation.
Exceptions for staffing factors are not entered for subcontracts.

#### Staffing factor setup (work center) and Staffing factor unit (work center)
Here you can see the staffing factor entered for setup time and unit time for the work center.

#### Terms
By using different terms on operation rows (and material rows), you can apply alternate BOM and routing. The terms available are: Finish date, Quantity, Customer number, Order, Revision, Variant code, Part status, and Warehouse. You choose to apply a row with a term in one of the following ways in the BOM and routing:
- add this extra row (+)
- replace previous row (±)
- delete this row (-)
Finish date
If you use the Finish date term and choose to use start date when registering manufacturing order and you leave the finish date empty, the start date will be used for the term instead.
Variant code
Variant code differs somewhat from the other terms. You can use the following wildcards when you enter a variant code on rows in the BOM and routing: "_" (or a space) and "%". This can be used to define a property for each position in the Variant code, for example, to configure a product. In that case you only use the From field.
For example, if we use a car as an example of the configuration, the first position stands for the "motor option", the second position refers to the "fabric option", and the third position is the "sunroof option". For the different rows in the material list for motor options, you enter, e.g., "1%", "2%", etc. in the variant code field. For the different fabric options, you enter, e.g., "_1%", "_2%", etc. If you enter the variant code "111" at order registration it means motor option 1, fabric option 1, and sunroof option 1.

#### From
Here you can enter a "from value" of the selected term.

#### To
Here you enter the "to value" for the selected term. By entering a value in From and To you decide within which interval the operation row with the terms will be met.

#### Lead time
This field shows the lead time in number of work days for a subcontract. This determines the number of days required for the subcontract. That is, the number of days between the start date and finish date. This field is empty if the row does not refer to a subcontract.

#### Net weight
Here you enter a net weight for subcontracts before they are sent to the subcontractor. The weight is also automatically saved in the Subcontract parts procedure. The net weight is used to obtain correct weight information for the subcontracts which are sent to a country within the EU, and should thereby be included in the IntrastatIntrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. report.
It is also used to calculated weight when when a shipment is created based on a subcontract purchase order.
