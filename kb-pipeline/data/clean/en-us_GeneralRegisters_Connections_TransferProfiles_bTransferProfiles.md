### The Transfer profiles table
In this table you add transfer profiles in the sales company. By using the buttons on the function menu you can add, delete, and copy profiles.
In the first column, you see this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinishedBox.png) if the transfer profile is validated and this symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/warning.png) if it is not validated. You can validate a new profile by using the button Reload ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_refresh.png) when all information has been entered. The transfer profile will then be set as validated if the communication between the sales company and the production company works.
The second column shows a row number for the transfer profile.

#### Active
Here you determine if the transfer profile should be active or not. Only active profiles will be selectable for parts in the part register and on customer order rows. Only validated profiles can be active.
> Please note! If a change has been made in the Settings for customer order transfer procedure of the setting number that is used by the transfer profile, it will be deactivated. You must then activate the profile again in this procedure.

#### Type
Here you decide which type of transfer profile is concerned. The different types can be combined and are described below.
- Customer order transfer – This type is used for customer order transfer between sales company and production company. The type is available if the Customer order transfer option is installed.
- Part synchronization – This type is used by the Synchronize parts procedure in order to synchronize data for parts from the company (the sending company) to a receiving company.
- Part information – This type is used to see stock balances for parts in other companies by clicking the Stock balances in remote company button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StockBalance.png) in the Part register procedure.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
The text can consist of a maximum of 35 characters. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Connection number
Here you select a connection number for the transfer profile in question. Connections must first be registered in the Connections procedure.

#### Warehouse
Applies to Customer order transfer and Part synchronization. If you have installed the Warehouse option, you here select for which warehouse in the production company or the receiving company the transfer profile applies.

#### Remote company's warehouse
Applies to Part information. Here you select for which warehouses in remote companies that part stock balances should be displayed in the Part register in this company. This applies if the Warehouse option is installed.

#### Setup number
Applies to Customer order transfer. Here you select a setup number for the transfer profile in question. Setups must first be registered in the Settings for customer order transfer procedure.

#### Supplier number
Applies to Customer order transfer. Here you select the production company's supplier number in the sales company.

#### Customer number (in production company)
Applies to Customer order transfer. Here you select the sales company's customer number in the production company.
