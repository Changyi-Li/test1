### Export settings
This tab is available if you have installed the the option Export of salary basis. An export setting determines the format of the exported salary basis. The export is made to a file in a format intended for the company's payroll program. This export is made in the Export of salary basis procedure where you select an export setting which first has to be registered here.
In the Salary program box you add a path for export of salary basis from Monitor ERP to your salary program.
In the Settings box you add one or multiple file formats to the path, depending on how many files should be exported to the payroll program. For each file format you enter file name, select components (if any are available), and mark if alias from salary type should be used.
Salary program

#### Default
Here you decide if the export setting should be default in the Export of salary basis procedure.

#### Name
Here you see/enter the name of the export setting.

#### Path
Here you see/enter the path to a directory where the export file should be saved.
> It is important you enter a path which is always available to the users who perform export of salary bases.
Settings

#### File format
In this column you select the file format for your payroll program. At present there is support for: PAXml, Visma, SoftOne (only applies to Sweden), Agda, HogiaLön Plus, Hogia Lön, V10, Bluegarden, Visma Løn (Denmark), Huldt & Lillevik, UNI Economy, Comarch Optima, and Mepco.
PAXml is for example used for Kontek and Crona Lön. Go to [www.paxml.se](http://www.paxml.se/) for a complete list.
> The file formats included at delivery of the Export of salary basis option are available to select here.
Special settings for V10
1. If the company is to export salary basis to V10, a text field must be added under the Personnel tab in the Extra fields procedure.
2. The column Identifier for extra fields also has to be activated. This is done with the system setting Show identifier for external programs (Extra fields).
3. The text field under the Personnel tab should have the identifier "V10".
4. For each person you should in the extra field in the personnel records enter the person's code in the payroll program.
Special settings for Visma Løn (Denmark)
1. If the company should export salary basis to Visma Løn (Denmark), two text fields called Customer info and Employer number must be created as Extra fieldsunder the Company info tab in the Extra fields procedure. As well as the field called Employee number to export under the Personnel tab in the Extra fields.
2. The column Identifier for extra fields also has to be activated. This is done with the system setting Show identifier for external programs (Extra fields).
3. The text field called Customer info should have the identifier "KUNDEFORHOLD" and the text field Employer number should have the identifier "ARBEJDSGIVER".
4. The text field under the Personnel tab should have the identifier "EXPORT".
5. For each person you should in the extra field in the personnel records enter the person's code in the payroll program.
Special settings for Bluegarden
1. If the company should export salary basis to Bluegarden, two text fields must be added under the Personnel tab, and you also have to add a text field under the Company information tab in the Extra fields procedure.
2. The column Identifier for extra fields also has to be activated. This is done with the system setting Show identifier for external programs (Extra fields).
3. One of the text fields under the Personnel tab should have the identifier: "BLG_SALGR", which stands for Bluegarden Salary Group. The second text field should have the identifier "BLG_EMPNO", which stands for Bluegarden Employee Number. The text field under the Company information tab should have the identifier "BLG_COMPID", which stands for Bluegarden Company Id.
4. For each person in the Personnel records you should in the two extra text fields enter the person's salary group in Bluegarden and the person's employee number in Bluegarden. The latter field can be left empty. In that case the person's employee number in Monitor ERP will be used instead.
5. In the Company information for the company you should in the extra text field enter the company's ID used in Bluegarden.
Settings specific to Huldt & Lillevik
The format "4 standard fast lengde" applies for Huldt & Lillevik and the file name should be "ITxxxTRS.HLT (xxx = client number)".
Special settings for Mepco
The file name should be "siirto.txt".
Special settings for Visma Payroll
As of version 25.3, a 20th field is exported in the file.
This field is used for additional information relating to salary for employees living outside of Norway. This field will be empty if you don’t configure an extra field on employees.
In order to use this:
1. Activate the system setting Show identifier for external programs (Extra fields).
2. Create an extra field of the Text field type under the Personnel tab in the Extra fields tab and enter ADDITION as the identifier.
3. The following text should be entered in the extra field under the Extra fields in the Personnel records tab for all employees that require this additional information: ""2400"": ""loennOgAnnenGodtgjoerelseSomIkkeErSkattepliktig"", ""2100"": ""NO""
Please note that NO should be changed to the country code of the country that the employee resides in.

#### File name
Here you see/enter the name of the export file for the selected file format. The file must be given the correct file name extension in accordance with the table below.
| File extension | File format |
|---|---|
| .xml | PAXml, HogiaLön Plus (Attendance/Absence) |
| .tlu | Visma |
| .wli | Hogia Lön, HogiaLön Plus (Schedule) |
| .txt | Agda, V10, Bluegarden, Comarch Optima |
| .hlw | Huldt & Lillevik |
| .csv | Mepco, UNI Economy, Visma Payroll |
| .dat | SoftOne |

#### Components
For the format PAXml it is possible to mark which of the components to include in the export file: Working time schedule, Time transactions, and Salary transactions.
For the format Agda it is possible to select one of the components Attendance, Absence, or Schedule to include in the export file. You need to create one row for attendance, one row for absence, and one row for schedule. This will generate three different files with different names in the export setting for Agda.
For the format HogiaLön Plus it is possible to select one of the components Attendance/Absence, or Schedule to include in the export file. You need to create one row for attendance/absence and one row for schedule. This will generate two different files with different names and file extension in the export setting for HogiaLön Plus.
For Visma, Hogia Lön, V10, Bluegarden, and Huldt & Lillervik, there are no components to select.

#### Use alias from salary type
Check this checkbox if salary types have an Alias at export filled in If a salary type is missing an alias, the salary type's code will instead be used in the export file.
