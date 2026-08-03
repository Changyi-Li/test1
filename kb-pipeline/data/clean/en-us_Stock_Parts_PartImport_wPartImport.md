## Part import
In this procedure you can import parts, BOM and routing, annual budgets for purchase and sales, as well as measuring data, part contents, and alternative material, from text files. The procedure is mainly used to import new parts. But it is also possible to update parts that already exist in the part register.
If the part number that you import from the file already exist in the system, that part will be updated. For the parts you select which fallback values to use, their type and status, if they should be stock updated and load values from a selected part template. After the import it is also possible to synchronize new or both new and existing imported parts with a part template. This only applies to parts, not BOM and routing or annual budget.
> For existing parts and material you can only import the part's standard unit. You cannot change unit, but you are able to add new alternative units in connection with the import. For new parts, the unit you enter will become the part's standard unit. Existing parts are validated and updated only based on part numbers during imports. New parts must both have part number and name to be validated during import. For supplier links you can modify prices from existing suppliers. This is only possible if the supplier number and the supplier's part number matches the ones already in the system. If the numbers differ, a new supplier link will be created.
Create template
If external data processing needs to be done before it is imported back into Monitor ERP, you can create a template in CSV format to help fill the import file. Please note that you use the [format template](../../../UserGuide/GeneralFeatures/FormatTemplates.htm) when you create the import template.
If you have parts that you want to update, you can check Include parts from Clipboard, and once the template has been created, it will load the parts and the information from the selected columns.
Import file
In the Import file box you enter the path to the file from which you will import data. To start the import click the button Import ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) in the toolbar. All data will be loaded to the list in the Loaded records box. You can manually add and delete rows. You can also filter to decide which rows to see. To complete the import you must check the box Include for the rows you wish to save and then click Save ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png). When you save, the included rows will be removed from the list.
When importing a text field of rich text, you are able to create line breaks by using the <br> command.
> If the file is coded in UTF-8, then Å, Ä, and Ö also work (if it occurs in part numbers). This is not possible if the file is coded in ANSI. If you save the file from Excel, you should use the alternative Unicode text rather than the alternative Tab-separated text file.
Parts
For parts, you can also import extra fields of the types called Text field, Integer, and Decimal number, in case you are using such fields.
Material and operations
In addition to the parts you can also import BOM (bill of material) and routing (the order of the operations) for the parts.
For material and operations you have three options. You can either add operations and material to the operations and material already on parts, update existing rows, or delete everything and just add the imported records. This is determined with the settings Update existing rows, Delete existing rows.
For Update existing rows, the columns Material row number and Operation row number are found backstage. These columns can also be added and exported in the Operation list and Material list procedures. Please note that if these row numbers are not used when importing, all rows containing an imported part or operation will be updated.
> The part type must be entered using digits in the import file. The meaning of the digits are: 0 means Purchased, 1 means Manufactured, 2 means Fictitious, and 5 means Service.
When you import bills of material and operations you can also create the main part to which the operations/materials belong. This is possible if the part number does not exist in the system already. Both part number and name for this main part must then be included in the file.
> When importing operations, the default time unit in the system setting Time unit Time units are units used to indicate the setup and unit times at BOM and routing. Normally, minutes or hours are used. for setup and unit time for operations will be used. The unit is shown at the bottom of the box Default values when you select the type Operations. Queue time Queue time refers to time which is added to create a gap between two operations when the manufacturing order is created. It is normally stated in days, where 1 means the rest of the commenced day will be the "gap". 2 means the rest of the commenced day plus 1 full day will be the gap. For work centers with hourly planning, the queue time is instead entered in hours. The entered queue time will be added before the operation which has a value entered. is displayed in days or hours depending the settings of the work center.
Importing terms for material and operations
If you are using alternate BOM and routing and you are importing terms for the alternate BOM and routing to operations and materials, you need to enter the terms with digits in the import file. In the table below you can see what each respective digit means.
| Digit | Meaning |
|---|---|
| 0 | None |
| 1 | + Finish date (add this extra row) |
| 2 | + (add this extra row) |
| 3 | + Customer code (add this extra row) |
| 4 | + Order (add this extra row) |
| 5 | + Revision (add this extra row) |
| 6 | + Variant code (add this extra row) |
| 9 | + Part status (add this extra row) |
| 10 | + Warehouse (add this extra row) |
| 51 | ± Finish date (replace previous row) |
| 52 | ± Quantity (replace previous row) |
| 53 | ± Customer code (replace previous row) |
| 54 | ± Order (replace previous row) |
| 55 | ± Revision (replace previous row) |
| 56 | ± Variant code (replace previous row) |
| 59 | ± Part status (replace previous row) |
| 60 | ± Warehouse (replace previous row) |
| 101 | - Finish date (delete this row) |
| 102 | - Quantity (delete this row) |
| 103 | - Customer code (delete this row) |
| 104 | - Order (delete this row) |
| 105 | - Revision (delete this row) |
| 106 | - Variant code (delete this row) |
| 109 | - Part status (delete this row) |
| 110 | - Warehouse (delete this row) |
Annual budget – sales and purchase
When you import the type Annual budget – sales or Annual budget – purchase, the row number, part number, old annual budget, and new annual budget are shown. You also find a column called Difference %. Then all columns that you have selected to include in the current format template are shown.
Import of annual volume
If your customer sends a file containing Annual volume, you can import the file here. Select the import type Part, and create a template for this purpose with the columns Part number and Annual volume.
Import of measuring data
At the time of the import you can add measuring data to the part's operations. During the import you can select if existing measuring data should be deleted or not from the operation.
If a part has the same operation number on multiple operations you can use the Operation row index column to determine which operation should be affected by the import. This column can be added in a format template which you base on the Measuring data import type. Read more about format templates below.
Import of part contents
If your supplier includes a file containing Part contents, you can import the file here. Use the import type called Part contents.
Import of alternative material
At the time of the import you can add alternative material to the part's material rows. During the import you can select if you want existing alternative materials to be deleted or not from the material.
If there are multiple materials with the same part number, it is possible to choose which material row that should be affected by the import. You can determine which material row to affect with the use of the Material row number column. This column can be added in a format template which you base on the Alternative material import type. Read more about format templates below.
Format templates
You can configure the format of the file at the time of the import. You can create a temporary format or a format template which can be used again.The function Format templates is found in the backstage of the procedure. There you can select for which columns data should be loaded/imported. For the content of the file you can also configure which limiters should be used as column limiter and decimal limiter. Furthermore you can enter a specific number of initial rows which should be skipped during the import.
Read more about [format templates](../../../UserGuide/GeneralFeatures/FormatTemplates.htm).
