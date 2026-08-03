### Import file

#### Type
Here you select the type of records you wish to load: Parts, Material, Operations, Annual budget – Purchase, Annual budget – Sales, Measuring data (for operations in the BOM and routing), Part contents, or Alternative material.

#### Update existing rows
Here you determine whether existing material in material lists (BOM) and operations in operation lists should be updated when importing material or operations. If you update existing operations, it is the operation number that updates and the part number for material rows.
If you have multiple rows with the same operation number (e.g. for alternate BOM and routing) or multiple rows with the same part number, the file should also contain the existing operation/material’s row number in order for the operation/material that you wish to update to be updated. If the row number is missing, all rows with the same operation/part number will be updated.
Existing row numbers can be viewed/exported in Operation list and Material list.

#### Delete existing material
With this setting you determine if existing material in material lists (bills of material = BOM) should be deleted when you import Material. Material in the file will replace the ones already existing for the part. Otherwise the imported information will be added to the existing rows.

#### Delete existing operations
With this setting you determine if existing operations in operation lists should be deleted when you import Operations. The operations in the file will replace the ones already existing for the part. Otherwise the imported information will be added to the existing rows.

#### File
By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_browse.png) you can enter a path to the file. You will then see the file path in the field.

#### Year
If you want to import Annual budget – Sales or Annual budget – Purchase, you must select for which year the loaded value applies.

#### Format template
Here you can select a format among the formats created in the backstage of the procedure. The following standard templates are available: Standard, Annual volume, standard, CO2e data, and CO2e data in supplier link. If you have made any temporary settings for the format, which have not been saved as a separate template, this will be shown as Current settings (not saved template).
