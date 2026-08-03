### Part codes
Under this tab you create part codes and names for these. Part codes are then used to group parts in the part register, e.g. in order to divide parts into different qualities, types, variants, etc. Part codes can also be used as a selection term in different lists. You can also delete part codes. A check will then be made to make sure the code is not used, e.g., on any parts, discount categories.

#### Part code
In this column you enter the code for the part. It can consist of a maximum of 10 characters. A code must be entered for each part.

#### Alias for BI
Here you can change the record's alias. This alias is used during data mining from records in the database in Monitor ERP to the database for Business Intelligence. The default value of alias is the same as the record's code/number, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on multiple records, for example customers, then data from these will be merged into a joint record in the database for business intelligence.
You activate alias for BI with the system setting Use alias when exporting to Business intelligence.
