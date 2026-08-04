## Emission type
Here you register emission types using codes, descriptions, and link to rows in the company's sustainability report according to the GHG protocol. These can then be used in the Company emission register procedure to create a more detailed specification specification of the different emission categories.

#### Code
Here you enter a code for the emission.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.

#### Translations
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Emission category
Here you select the emission category among the different rows/categories available in the emission report.

#### Scope category
Here you see the name of the scope category.

#### Scope
Here you see to which section (scope) of the report this code belongs.

#### Reporting method
Determines how the emission will be reported. The following methods are available:
- Invoices and vouchers – used to register carbon dioxide emissions related to the company’s purchases by linking the code to the posting on supplier invoices and vouchers. This takes place directly in the procedures Register supplier invoice, Authorize supplier invoice, Register vouchers, or it can be done after the fact in the Sustainability list procedure. CO2e will then be calculated automatically via Amount x Emission factor.
- Manual – used in the procedure Report emissions manually to perform manual reporting.
- This is used for emissions that cannot be directly related to the value on purchase.
- This could, for example, be emissions from the company’s official cars.
- The personnel’s trips to and from work.
- Emissions from the factory’s furnace

#### Emission factor
Here you enter the material's emissions in the unit kg CO2e/kg.

#### Unit
For the reporting method Manual, it is possible to select a unit that is appropriate for the reporting.
-  For example, km can be used for official cars.
-  The emission factor will then be presented in kg Co2e/km and it is sufficient to enter the amount of kilometers driven to report correctly.

#### Source
A text field where you enter where the emission factor has been loaded from. It can be, e.g., Ecoinvent.

#### Origin, date
Here you enter the date of when the data was loaded from its origin.

#### Reliability index
You determine the reliability index and how you want to use it yourself. The reliability index is there so you can evaluate how reliable you believe the information source where you have found your sustainability data to be. If you, for example, received data directly from the supplier, the data should be considered reliable. The number is entered with decimals within the interval 0-1.

#### Linked accounts/suppliers
If you enter account and supplier, the emission will be automatically registered when registering the supplier invoice.
