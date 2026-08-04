### Bank-specific settings
In the procedure called Settings for export/import you have to configure settings for factoring companies for the export type Factoring. At present there is support for the formats for "Handelsbanken Finance" (applies to Sweden), "Swedbank Payex" (applies to Sweden), "Nordea Finance" (applies to Norway), "DNB" (applies to Norway), "Nordea Finance" (applies to Finland), and "Peppol BIS 3.0".

#### Directory
Here you enter the path to the directory where the export file should be created.

#### File name
Here you enter the name of the export file. The file name is pre-filled as a template and contains a variable that inserts today's date in the file name.
The variable is {datetime}. Example of file name: "CUSIN_{client_number}_{datetime}_*.xml" for Swedbank Payex. The variable "*" stands for consecutive number. The consecutive number is an uninterrupted number series where the company's first file should have number 0001, the next 0002, etc. The system will automatically name the file this way, but if needed, it is possible to adjust the consecutive number, for example, if the system should start from number other than 1 Next consecutive number for file export is entered in the Consecutive number field.
When you hover over the field, a tooltip will display an explanation of the variable.

#### Handelsbanken Finans
In the Factoring service field you can select between Invoice credit and FakturaLink.
Handelsbanken's format is called Falk and only handles one client number. This means that you only need to enter Client no. factoring, on the row for the company currency under the Document information tab in the Bank settings procedure.

#### Swedbank Payex
In the Factoring service field you can select between Ledger service and Invoice service. Swedbank’s format is called CUSIN.
