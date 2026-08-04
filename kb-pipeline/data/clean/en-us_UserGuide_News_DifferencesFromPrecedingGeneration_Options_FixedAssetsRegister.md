### Fixed assets register
In G5 the Fixed asset register is an option in the same way as it is a supplement in G4.

#### Register fixed assets object
Video: Register fixed assets object (Swedish)
- Register new and historical fixed assets object in the same procedure, not in separate procedures as in G4.
- You can see the status of the fixed assets object (registered, depreciation started, etc.).
- New field for initial acquisition value.
- New fields for Responsible and Used by.
- It is possible to update an existing fixed assets object from supplier invoices and vouchers. These automatically adjust the acquisition values of the object.
- New function for Investment in progress. Used fro fixed assets objects which refer to buildings, machines, etc. which are being constructed/built. During the time of the construction/build, all supplier invoices can be charged to the fixed assets object. An automatic reversal of entries will take place when the investment is activated. It is also possible to divide the fixed assets object in components (sub-objects) in connection with the activation.
- New field for Depreciation start where you decide when the depreciation should start. Which depreciation start that is suggested is determined by a system setting.
- It is possible to enter individual depreciation period/percent per fixed assets object.
- When registering sub-objects you can set the depreciation period automatically bases on the main object’s remaining depreciation period.
- New field for showing of remaining depreciation period in months or days.
- New fields regarding information about insurance and warranty.
- There is a new text box where you can enter a short description of the fixed assets object.
- A more detailed log which shows the type of depreciation done and changes made of acquisition values, etc.
- It shows which fixed assets account the fixed assets object is linked to.
- New tab for General ledger, where you can see general ledger transactions (from supplier invoices and depreciation, etc.) for the fixed assets object in question. This is made possible by saving the fixed assets object in a separate field in all general ledger transactions.
- For a main object, more information is now shown about its sub-objects.
- More information about sales/retirement of the fixed assets object.
- Handling of tax depreciation information for fixed assets referring to buildings (component depreciation).

#### Fixed assets list
Video: Fixed assets list (Swedish)
- This procedure mainly corresponds to the Fixed Asset List procedure in G4.
- More information can be shown in the lists, such as the status of the fixed asset, and how much of the asset which have been depreciated.
- It is possible to print more detailed depreciation information via the list type Depreciation log, also concerning calculated depreciation.

#### Depreciation
Video: Depreciation (Swedish)
- This procedure has been merged from the procedures Scheduled Depreciation, Calculated depreciation, and Budgetary depreciation in G4.
- Handling of journals for depreciation in the same way as in the accounts payable and accounts receivable.
- Depreciation can take place based on number of days (as in G4) or for entire months. Determined by the system setting called Depreciation is based on.
- New method for calculating depreciation, based on residual value and remaining depreciation time. Calculation of depreciation is based on residual value and remaining depreciation period, to make sure each object is depreciated according to the depreciation time entered for the object. If the acquisition value/residual value is changed for object where the depreciation started, this makes sure the correct depreciation time is kept.
- When calculating budgetary depreciation, you can also save the calculation to the accounting budget.

#### Tax depreciation
Video: Tax depreciation (Swedish)
- Improved bases for calculation of depreciation according to accounts.
- Bases for temporary differences of fixed assets objects which are real estate (component depreciation).

#### Print fixed assets journal
Video: Print fixed assets journal (Swedish)
- The procedure is new in G5 and it means that you can print journals for depreciation etc. and also reprint these.

#### Sales/Retirement of assets
Video: Sales/Retirement of assets (Swedish)
- Now it is possible to sell a fixed asset via the procedures Register customer order and Register invoice directly. When customer order/invoice is being registered, the user can enter which fixed asset is being sold. This is entered in a new column called Fixed assets object. In connection with approving the invoice, the sales will automatically become registered in the fixed assets register.
- Support for partial disposal/partial sales.
- New fields concerning customer and customer invoice.
- You can in advance see how sales/retirement will be posted.
- You do not have to perform scheduled depreciation to record the sales/retirement. It will take place directly when you save.
- It is possible to select if full depreciation should be performed in connection with sales/retirement. This is governed with a system setting.

#### Undo depreciation/sales
Video: Undo depreciation/sales (Swedish)
- New procedure where you can undo depreciation and sales/retirement.
- Sales/retirement can be undone even though you have entered the sales/retirement in the bookkeeping.

#### Fixed assets import
Video: Fixed assets import (Swedish)
- This is a new procedure where you can import a fixed assets list via a text file.

#### Basic data – Fixed assets register
Video: Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Fixed assets register (Swedish)
- You can enter depreciation time in number of years for fixed assets groups (except for %).
- Prefix for fixed assets group. This supports different prefixes on fixed assets depending on group affiliation.
- Fixed assets types can be linked to fixed assets groups.
- It is possible to activate the setting No depreciation for the group. This is for example used for short-term fixed assets.
- The settings for calculated depreciation have been moved from the system settings to each fixed assets group.
- Locations of fixed assets can be registered in a basic data table.
- You can enter tax depreciation method for fixed assets groups. There is support for depreciation according to accounts, component depreciation, and no tax depreciation.
