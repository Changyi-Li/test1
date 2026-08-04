### Data not converted from G4 to G5
Not all data is converted from G4 to G5. Below you find a list of data that is not included in the conversion from the G4 database to G5. This must be registered again in G5. This can be data which you need to re-register or data you need to update/complement. Please read this section with information about what is included in the conversion. Make sure the setup is correct together with your Monitor consultant.
General/MPC
| Procedures/Functions | To do |
|---|---|
| Backup | Support personnel from Technics/Installation are the ones who normally create backup tasks when they have installed the system. Make sure the setup is correct together with your Monitor ERP System AB consultant |
| Test company | Support personnel from Technics/Installation are the ones who normally create test companies when they have installed the system. Make sure the setup is correct together with your Monitor ERP System AB consultant |
| Logotype | The logotype must be added in G5. This is done in the Company information procedure. Keep in mind the scale of the logo must be 1:4. |
| Users | The user is included in the conversion to G5, but the user must then be assigned a license and user rights. ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/NotConvDataUser.png) Remember to assign EIM user rights and Warehouse user rights. This is assigned per user. |
| User rights groups | You must re-register user rights groups. In G5 there are pre-defined roles which can be used if you don't want to create user rights groups. |
| Default values | Default values in lists must be registered again. |
| Saved filters | Saved filters in lists must be registered again. |
| Own design of LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature | Lookups which have been created/designed by the user, have to be created again in G5. |
| AutoRuns (Agent tasks) | AutoRuns/Agent tasks must be registered again. |
| Background images on documents | This function is not yet implemented in G5, so data will not be converted. |
| Signatures | The signatures which in G4 was linked to the reference must again be linked in the Personnel records procedure. These can be used to show signatures on different documents. |
| Desktop/Desktop components | If you use desktops, you must create new desktops per role, user rights group and/or per user. |
| Extra fields | Extra fields need to be re-registered. The data in the fields can be imported from G4 to G5 by using the program Monitor Import. |
| Document phrases/Document texts | If you have made changes in document phrases in G4, then you have to make these changes again in G5 since these are not included in the conversion. Tip! Changed document phrases are shown in italics in G4. |
| Procedure instructions | Procedure instructions (own instructions when using procedures in the system) are not converted to G5. If the instructions should be used, they need to be copied over manually to the corresponding procedure in G5. |
| Planning formulas | If changes have been made in planning formulas, then you have to make these changes again in G5 since these are not included in the conversion. |
| Time zone | Remember to check the time zone in the Company Info procedure. If you are using the Warehouse option you need to check this per warehouse. |
| Production calendar | In case unique work center calendars were created in G4, then you have to create them again in G5 in Production calendar procedure. |
| Activate file paths | Check the boxes in File paths. |
| Templates for activities | Not converted for cases and projects, since there is a brand new term in G5 which is called phases. As such, an activity template contains both activities and phases. |
| ABCABC codes are used to classify the range of parts by the volumes you sell. The codes are used as a scale for the parts that turn over the most money. The turnover is calculated by multiplying the price of the part by the annual volume. Parts that turn over the most money are called "A-parts", and after that, "B-parts", etc. codes – Type | ABC codes are converted but the type will be set to "Unclassified". Read more about [ABC codes](../../Stock/Parts/BasicDataPart/tABCCodes.htm). |
| Supplier rating subcontract | Subcontract purchases from G4 cannot be analyzed in the G5 supplier rating. |
| Delivery planning (Sales) |   |
| ODBC links & SQL queries | In cases where you load data via one or multiple ODBC links or SQL queries, these must be remade. Since the database is designed in a different way, all reports (normally in Excel and Access) must also be remade. This also applies to loading of data to other programs which you have set up yourself. If you wish to get help with this, a cost will be charged. |
| Edited linked documents | In G4 it is possible to use the Info menu (accessed by right-clicking) and from there open a linked document and edit it. The modifications made will be added to the linked document but will not be saved on the PDF document. This means the changes will not be included in Monitor ERP |
| Changelogs | Changelogs (for parts, orders, etc.) are not included in conversion to G5. Except for the Preparation log which is converted from G4. |
| Message in Priority planning | Is not converted. |
Time recording
| Procedures/Functions | To do |
|---|---|
| Schedule calendars | The procedure called Schedule calendars is in G5 replaced with the Schedule cycles procedure. These schedule cycles must be created and linked to employees. |
| Export of salary basis | Create settings for export of salary basis. Alias on salary types are needed if you use KONTEK. Change the format in KONTEK to PaXML. |
| Work recording log | The work recording log is not converted to Monitor ERP However, the manufacturing order log is included in the conversion. |
| Attendance recording | Attendance recording items are converted for the current year and for one year back in time. That is, if a conversion takes place 2022-02-15 you will see recording items from 2021-01-01 onwards. |
| Adjust attendance recording | If the conversion is made while running, you need to adjust the recording items in G5 for the day in question, since the personnel is clocked out during the conversion. |
| SWH | Data regarding how SWH is calculated is NOT converted. The reason for this is that is saved in the ini-file in G4 and that it is a setting per user. The SWH is by default calculated per hour in G5. The hours from the parameter group and from the schedule are converted. These are saved to the respective place in G5. |
Shipping configuration
Shipping must be configured from scratch in Monitor ERP Remember to book a consultant with the specific knowledge or support services for this. This configuration can only be done after the actual conversion has been completed.
> Please remember that this also concerns already registered shipments - these are not included in the conversion to G5.
EDI
EDIEDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. must be configured from scratch in Monitor ERP Remember to book a consultant with the specific knowledge for this. This configuration can only be done after the actual conversion has been completed.
Finance
| Procedures/Functions | To do |
|---|---|
| Voucher number series | Make sure there are number series and link journals in the Voucher number series/Journals procedure. Applies to, for example, VAT report, accruals, and fixed assets register. |
| Own accounting reports | If you have created own financial reports in G4, these must be created again in G5. |
| Forecast (Accounting module) | Create forecasts in the Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Budget and Register budget procedures. |
| Days free of payment | Create bank calendar + system settings the system settings Calendar for calculation of payment date and Calendar for calculation of due date. |
| Automatic update of exchange rates | Schedule automatic update of exchange rates in the Currencies procedure. |
| Settings on bank account | Go over the Bank accounts tab in the Bank settings procedure. |
| Chart of accounts – Currency account | Mark accounts as currency accounts with the correct currency code. |
| Payment method ISO | Order the correct ISO formats from the Support Center (depends on which bank you use). Configure payment method ISO under the Payment method tab in the Bank settings procedure. Complement with correct information in the Settings for export/import procedure, for Payment files. When needed, register exceptions for bank settings per supplier under the Bank account button in the Supplier register procedure. |
| Path to export/import files (VAT report, IntrastatIntrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states., etc.) | Register the paths in the Settings for export/import procedure. |
| Check countries on delivery addresses for customers/suppliers | New field for country in G5, double-check that this is correct since this will affect the Intrastat reporting. |
| Interest charge | Service part is used to charge interest. Separate product group for the service is required to determine that the interest becomes exempt from VAT and to make the posting correct. You can read more [here](../News/DifferencesFromPrecedingGeneration/Sales/InterestChargeBasis.htm). |
| The system settings Price alternative for M-parts (COGS) and Price alternative for P-parts (COGS) | At present, the following is supported at conversion: -2 = Standard price at delivery, P-parts excl. SO -1 = Standard price at invoicing, P-parts excl. SO 0 = Material cost excluding SO >0 = According to price list Everything else will be: -4 = Material cost including SO |
| Invoice basis – Subcontract | This is converted but since handling of subcontract differs between G4 and G5, it is good to make sure that you have nothing or as little as possible as invoice bases, when it is time to do the conversion. In G4 main part numbers were used and in G5 subcontract part numbers are used. This will cause calculation differences in the accounting when you compare to standard price of the part. |
| Transaction list | The transaction list is not converted. Please note! The number series from the transaction list is not converted either, since in G5, there is only one number series for this. Remember to set this manually. |
