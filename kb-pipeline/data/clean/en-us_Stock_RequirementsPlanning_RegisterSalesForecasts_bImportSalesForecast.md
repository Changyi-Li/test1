### Import sales forecast
By using the button Import sales forecast ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_import.png) in the toolbar of the procedure, a window opens in which you can import a sales forecast from a text file (.txt .csv).
The text file you use during the import must contain a column with our part number or the customer's part number. The text file can also contain one column for quantity and one column for delivery date. In that case, the text file must be tab-separated. The following applies for all three columns. They must be in the order stated below:
1. Part number – Our part number or the customer's part number. If the file contains the customer's part number, then the customer's part number must also be available in the customer link for the part to make it possible to match during the import.
2. Quantity – Period or comma as decimal separator.
3. Delivery date – The format is interpreted and saved according to the Date format system setting.
A validation is made during the import to make sure the entered part numbers in the file are registered in Monitor ERP and that the entered dates in the file are correct. Otherwise, the import cannot be performed.
> If the file is coded in UTF-8, then Å, Ä, and Ö also work (if it occurs in part numbers). This is not possible if the file is coded in ANSI. If you save the file from Excel, you should use the alternative Unicode text rather than the alternative Tab-separated text file.

#### Import to forecast
Here you can select an existing forecast or you can enter a forecast code for a new forecast.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.
You cannot edit the text on existing sales forecasts.

#### Existing forecast
If you have selected an existing forecast, you can select two alternatives:
- Only replace parts in the import file – If you for example have three parts A, B, and C in the existing forecast but only part B exists in the import file. Then existing forecast rows for part A and C will not be replaced, while the forecast rows for part B will be replaced with the rows imported in the file.
- Replace all rows in existing forecast – When using this alternative, all existing forecast rows will be removed and be replaced with the rows in the file. This means that only part B will have forecast rows when the import is completed.

#### Import file
Use the browse button to find the import file. The path is displayed in the box next to the button.

#### Import
When you have selected a forecast code and a file, you click the button Import which has been activated. When you have imported the file, the window is automatically closed. You then return to the forecast in question in the procedure window. The result is not saved until you click save in the procedure.
