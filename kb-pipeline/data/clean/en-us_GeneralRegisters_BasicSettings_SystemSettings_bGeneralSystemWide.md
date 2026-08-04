### General (System overall)

#### Date format
This system setting determines if the date format should be displayed as the date in Windows or as YYWWD. For example, this applies to date on parts in the planning window or date on order rows and operations. This means that only period fields are affected, that is, finish dates, planned finish dated, etc. on orders. Not dates in general.
It is almost only in connection with order planning the YYWWD format is used. This makes it easy to see, for example, "how much are we supposed to delivery day 5 (Friday) in week 17".

#### Use alias when exporting to Business Intelligence
This system setting determines if it should be possible to modify the record's alias for BI in a separate field called Alias for BI. When the setting is activated, the field is available in the procedures Customer register, Supplier register, and Part register. The field is also available in the table for product groups in the Posting matrix procedure, the table for part codes in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Part procedure, and in the tables for project types, phases, activities, costs/income, costs/income groups, and project groups in the Basic data – Project procedure.
Alias for BI is used during data mining from records in the database in Monitor ERP to the database for BI. The default value of alias is the same as the record's number/code, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on several records of the same type (for example customers), then data from these records will be merged into a joint record in the database for business intelligence. The name of the record will then be loaded from the record that ends up last in the ascending alphabetical order. That is, if there are two customer with customer names A and B, they will be displayed as customer B in the database. This can be used in cases where it is the same physical record that has different numbers/codes in two or more companies in Monitor ERP. Alias can also be used for this purpose when only one company is used.
It is also possible to use alias for the opposite purpose. To split records with the same number/code in several companies in Monitor ERP to different records in the database for business intelligence.

#### Manage staggered discount rates in the procedure Discount categories
To each discount category in the Discount categories procedure you can enter a discount rate for each product group, part code, or part category (this is determined by the system setting below). If you activate this system setting you can manage staggered discount rates in that procedure. This means that you can add discount rates for 1–10 limits, based on quantity or value.

#### Part grouping term for discount categories
This system setting determines if the part grouping term in the Discount categories procedure should be product group, part code, or part category.

#### Time when order day/start day changes to next day
Here you enter the time when the order day changes to next day For purchase order suggestions and manufacturing order suggestions created during net requirement calculation prior to this time, today will be suggested as earliest order date. For order suggestions created during net requirement calculation after this time, next day will be suggested as earliest order date.

#### Show identifier for external programs (Extra fields)
This system setting determines if a column for identifier should be available in the Extra fields procedure. The identifier is used to find the specific extra field in external programs during different data exports, part synchronization, or in adaptations.

#### Search indexing (Monitor search)
With this system setting you decide if the Monitor search function (Ctrl + F), which you find on the title bar in Monitor ERP, should be activated or not. Yes is the default option here and this activates a continuous indexing of the database. In test companies, this function is deactivated by default for performance purposes. This is shown with a No in this setting.

#### Warn if part name does not have a translation
This setting determines whether a warning is shown if a part name lacks a translation to another language used in an address (mailing address or delivery address) in any of the following procedures:
- Register inquiry
- Register purchase order
- Register stock order - Purchase
- Register blanket order – Purchase
- Register quote
- Register customer order
- Register invoice directly
- Register stock order – Sales
- Register blanket order – Sales
- Register customer agreement
Deactivate the setting if you do not want a warning to be displayed when a part name is missing translations.

#### Send usage statistics to Monitor
Here you decide if statistics about the use of Monitor ERP and hardware should be sent to Monitor ERP System AB. The statistics will be used by Monitor ERP System AB solely for the purposes of product improvement. The data collection includes which procedures that are opened, closed, what parts of the procedures are used and updated, and how long different updates take. The statistics gathered will include information about the hardware used, such as processors, memory, and disks.
> Please note! The statistics is completely anonymous. No information about data and values which are updated in the program will be sent. Also, no user information or company information will be sent.

#### Send basic usage statistics to Monitor
Here you decide if basic statistics about the use of Monitor ERP and hardware should be sent to Monitor ERP System AB. The statistics will be used by Monitor ERP System AB solely for the purposes of product improvement. The data includes information on which file types are used, opened, or viewed when the Extended file viewer option is activated.
> Please note! The statistics is completely anonymous. No information about data and values which are updated in the program will be sent. Also, no user information or company information will be sent.
