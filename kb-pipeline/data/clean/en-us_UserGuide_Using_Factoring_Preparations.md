### Preparations
Here you can read about what needs to be configured before you can start using factoring export.

#### Settings for export/import
You find settings for factoring export under the Export tab and under the export type Factoring. The settings to configure depend on the format used by the bank. Settings which might differ between the formats are that the customer register should be exported as a separate file or that you must select which service you have signed up for at the factoring company. One thing that applies to all bank formats is that you have to select path to a directory and a file name for the export.
At present there is support for the formats for "Handelsbanken Finance" (applies to Sweden), "Swedbank Payex" (applies to Sweden), "Nordea Finance" (applies to Norway), "DNB" (applies to Norway), "Sparebank1" (applies to Norway), "Nordea Finance" (applies to Finland), and "Peppol BIS 3.0".
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Factoring1.png)](../../../../Resources/Images/TrainingMaterial/Factoring1.png)
Read more about the settings in the section[Bank-specific settings](BankSpecificDetails.htm).

#### Bank settings
In this procedure you need to register information about the factoring company's bank accounts and enter your (the company's) client number used at the factoring company. Here you also configure settings to make the bank information in the footer of different documents (invoices etc.) be based on the intended currency and if factoring is used for the customer in question.
The Bank accounts tab
Under this tab you register the factoring company's account and its information regarding account number etc. For certain factoring companies you might need to register more than one account.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/factoring2.png)](../../../../Resources/Images/TrainingMaterial/factoring2.png)
The Document information tab
Under this tab you configure settings to make the bank information in the footer of different documents (invoices etc.) be based on the intended currency. If factoring is applied for the customer in question, you also enter account information to be displayed in the footer of the document.
Client number
If it mandatory to have a client number in the export file, you must as a minimum always enter one row for the company currency, with a link to your own bank account and the factoring company's bank account, and the client number at the bank.
If you have multiple currencies registered as factoring information then it is sufficient to enter the client number on the row referring to the company currency.
For certain exports the bank requires you to have different client numbers per currency. In these cases you have to register one row for each currency and you have to enter a client number for that currency in the column to the far right.
In the example below the company has several different currency account at the bank, that is why a separate bank account and factoring account is entered for each currency. However, the bank in the example does not demand different client numbers depending on the currency, therefore you only enter that information on the row for the company currency.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/factoring3.png)](../../../../Resources/Images/TrainingMaterial/factoring3.png)

#### Customer list
For it to be possible to export factoring, it is required that you for each customer activate the setting Factoring. This is done in the Standard list with the presentation Miscellaneous. Update this info by using the checkbox in the Factoring column for each row.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/factoring4.png)](../../../../Resources/Images/TrainingMaterial/factoring4.png)
> Use Find & replace to update the column for many customers at the same time.
