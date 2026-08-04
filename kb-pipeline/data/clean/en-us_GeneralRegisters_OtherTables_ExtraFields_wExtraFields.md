## Extra fields
In this procedure you can add an optional number of extra fields for different purposes. These fields can be used in basic data registers, in lists, and on documents. The following basic data registers support extra fields:
- Suppliers
- Customers
- Parts
- Cases
- Serial number A serial number is a number that is used for traceability for parts on entity level./batch number
- Work centers
- Personnel
- Projects
- Fixed assets objects
- Company information
- Operation rows (in BOM and routing and in manufacturing orders). Works in a limited capacity for fictitious parts, as if rows are merged the values of the extra fields will not be merged in the same way as is done with instructions. Instead, the original row's value or lack of value, will remain.
- Material rows (in BOM and routing and in manufacturing orders). Works in a limited capacity for fictitious parts, as if rows are merged the values of the extra fields will not be merged in the same way as is done with instructions. Instead, the original row's value or lack of value, will remain.
- Customer order
- Quote rows
- Customer order rows
- Invoice rows
- Inquiry rows
- Purchase order
- Purchase order rows
The procedure consists of separate tabs for each type of basic data. Under each tab you find two tables. In the left table called Fields you add the extra fields that you need to use. When you add a row by using the Add new row at the end button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_row.png) (F5), a main row and a sub-row will be created. The main row functions as a grouping (box) and heading for the underlying rows. The sub-rows are the actual fields. You can then add more sub-rows by using the Add underlying level button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_subrow.png) (Ctrl + Shift + F5). You can also add more main rows with sub-rows.
The main row's field name will be shown as the heading of the box in which you can see the fields. The box is shown under the Extra fields tab which will automatically become available in the affected basic data procedure.
In the table to the right you add register data to the selected field. This only applies to fields of the type Selection list and Multi selection list. The right table is not used for other types of fields.
Example of how extra fields can be used
The extra fields you created can then be added as selection rows in list procedures, as columns in own presentations of lists, and as own Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. presentations in the Lookup feature. This applies to list procedures which contain the above mentioned basic data.
The extra fields you have created can also be added to own variants of documents in the Document templates and Document templates – Manufacturing order procedures. Extra field for companies can, for example, be used in the Company information procedure and as extra information in the footer of different documents.
If you use the option called Product configurator, you can use extra fields on parts in order to give variables values in the configurator. You choose which fields should be used on the variables under the tab Variables in the Configuration groups procedure.
Extra fields must be used if you should export salary bases to the payroll programs V10 and Bluegarden. Then text fields should be added to the tabs Personnel and Company information. You must enter an identifier for the fields. The column Identifier must first be activated. This is made by using the system settings called Show identifier for external programs (Extra fields). Read more about adding text fields for these payroll programs in the section [Export settings](../../../TimeRecording/BasicData/BasicDataAttendance/tExportSettings.htm) in the online help function for the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Attendance.
