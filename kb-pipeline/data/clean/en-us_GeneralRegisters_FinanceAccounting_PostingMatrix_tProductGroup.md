### Product group
In the Product group table you register the product groups you need. When you start the system for the first time, there are some product groups included in the program.
You can register an optional number of product groups as well as delete product groups. If you delete a product group, a check is made to make sure it is not used for some part. Product groups are linked to parts in the Part register procedure.

#### Default
Here you determine if the row should be used by default when a new part is created.

#### Number
Here you can see the number for the position of the row. This field is numerical. A new row will by default be assigned the next available number. The table/list is sorted by this column. A number is unique and cannot occur on more than one row in the table.

#### Alias for BI
Here you can change the record's alias. This alias is used during data mining from records in the database in Monitor ERP to the database for Business Intelligence. The default value of alias is the same as the record's code/number, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on multiple records, for example customers, then data from these will be merged into a joint record in the database for business intelligence.
You activate alias for BI with the system setting Use alias when exporting to Business intelligence.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.

#### Translations
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.
