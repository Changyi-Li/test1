### Basic information
In this box you enter basic information about the company.

#### Company name
Here you enter the name of the company.

#### Corporate ID number
Here you enter the corporate ID number of the company.

#### Domicile
Here you enter the domicile of the company.

#### Language
Here you select which language should be used as company language.
When translatable texts (names, etc.) have no translation in the user's language in Monitor ERP, the company language will be used instead. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Currency
Here you select the company currency used in the company’s accounting as well as during standard pricing of parts. This currency applies to all warehouses if the option Warehouse is used. The name of the currency is shown in the user’s language. By using the Change currency button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png), you can change the company currency.
> Please note! You should only change company currency in an empty database. Existing data will not be converted into the new company currency.

#### GS1 company prefix
Here you enter a unique company prefix that has been assigned to the company by a GS1 standards organization for its region or line of business. The company prefix is a combination of six to nine digits. GS1 company prefix is used to create unique GTIN numbers for parts that the company sell. The company prefix is found in the beginning of the GTIN number for parts.
Next to the GS1 code field, under the Sales tab in the Part register procedure, you find a feature used to generate unique GTIN numbers for parts. If this feature is used and the company consists of a seven- to nine-digit company prefix, then the first six digits in the company prefix should be entered in this field. The digits seven to nine are entered in the number series GS1 code, under the Stock tab in the Number series procedure. The number series must start with the remaining digits in the company prefix plus a number of zeros for consecutive number. The number series should in total consist of six digits (hundreds of thousands).
When a GTIN13 number is generated in the part register, then the six digits in the company prefix are put together with the six-digit number loaded from the number series. A control digit is then added. All in all, the GTIN13 number consists of 13 digits. You can also calculate check digits in the field GTIN-13 on page [https://gs1.se/en/standards-and-services/check-digit-calculator/](https://www.gs1.se/Support/Berakna-kontrollsiffra/).
If GS1 company prefix should not be used, you leave the field empty.

#### Bank account
Here you select the default bank account of the company. You can select among bank accounts registered in the Bank settings procedure.

#### Time zone (UTC)
If you do not select a time zone here it means that the time zone used in Windows on the Monitor sever will be applied instead. The time zone is applied for all warehouses.

#### Our partner code
The "our partner code" is used to identify the company in EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. export files for purchase orders and delivery schedules. You can also enter "our partner code" in the company's alternative delivery addresses.

#### EORI number
Here you enter the company’s EORI number (Economic Operator Registration and Identification). You use the EORI number for all customs related business within the EU. In the Document templates procedure you can add the EORI number in the document component Footer.
It is possible to validate your entered EORI number in relation to the database available with the European Commission. This is done by clicking the EORI number not validated button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) and then the Validate EORI button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_validate.png). After you have validated the EORI number, the information about the company is loaded to the window and you can see if the EORI number is valid or not. The button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) will be changed to ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) if the EORI number is valid. Regardless if the EORI number is valid or not, you can in the tooltip belonging to the button see when the number was most recently validated and by whom.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EORI_validation_valid.png)](../../../../Resources/Images/SubProjects/EORI_validation_valid.png) [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EORI_validation_invalid.png)](../../../../Resources/Images/SubProjects/EORI_validation_invalid.png)
