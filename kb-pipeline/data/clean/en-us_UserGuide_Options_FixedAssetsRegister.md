# Fixed assets register
This option in the Accounting module provides system support for managing the company’s fixed assets.

#### Fixed assets objects
Fixed assets objects refer to machinery and equipment, buildings, etc. These should be registered as assets in the fixed assets register. It is possible to depreciate the fixed assets objects in the register based on the settings configured for the objects. You can also register objects which should not be depreciated. You can also create and update fixed assets objects from the accounts payable and from the registration of vouchers.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Options/FixedAssetsRegister2.png)](../../../Resources/Images/Options/FixedAssetsRegister2.png)
Different lists can be printed from the fixed assets register. These lists are used for several purposes, for example to reconcile the residual values of the fixed assets to the balance sheet or see information about depreciation and sales. They can also be used to show and update information about the fixed assets.

#### Depreciation
There is support for scheduled, calculated, depreciation for the fixed asset objects in the fixed assets register. Data for depreciation is based on information about the fixed assets as well as settings for fixed assets groups.
When scheduled depreciation is done, the residual values and accumulated depreciation will be updated. At the same time a basis for recording/booking of the depreciation is created. For scheduled depreciation there are methods called Straight-line, Declining balance, and Declining balance + Straight-line
During calculated depreciation, a calculation of depreciation based on the settings for the fixed assets groups is made. As opposed to scheduled depreciation, the calculated depreciation is not regulated by law. It takes place based on internal purposes. These normally concern basis for price calculations and profitability calculations based on the asset's replacement cost instead of acquisition value.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Options/FixedAssetsRegister3.png)](../../../Resources/Images/Options/FixedAssetsRegister3.png)

#### Fixed assets journal
You can print journals regarding depreciation and the postings. The journals can be reviewed and then approved. They are then transferred to the accounting. In many cases companies also make a printout of the journal/accounting order and put it in the voucher binder. You only need to use fixed assets journals if you apply integration to the accounting via printout of journals.

#### Sales/Retirement
In connection with sales/retirement of fixed assets, the fixed asset will be given status "Sold/Retired" at the same time as the system removes the fixed asset's value from the balance sheet. Any profit or loss will also be posted. If the sale is made after the most recently made depreciation, a recording of depreciation can also be made up to the date of the sale.
If the sale concerns a main object you can choose if the linked sub-objects should be included in the sale/retirement. The sub-objects that are not included in the disposal/sale become disconnected from the main object. A sub-object can for example be an associated component that is part of a larger machine (main object).
It is possible to sell/retire part of a fixed asset. The fixed asset will then remain as active in the register but with a reduced acquisition value and accumulated depreciation/residual value.
It is possible to undo depreciation, sales, and retirement. You can for example undo the depreciating you just performed, which means the depreciation will be reversed for many fixed assets at the same time. Another purpose might be to undo depreciation for a specific fixed asset, for example if depreciating has been done for a period of time for a fixed asset, but needs to be undone or has been incorrectly performed due to new circumstances.

#### Fixed assets import
It is possible to import fixed assets from a text file. This is mainly used to load entirely new records, but it can also be used to update existing records.
Interested in finding out more? Please contact our Sales department using this [form](https://www.monitorerp.com/sv/kontakt/). Want to find out more? Sign up to our upcoming [Monitor Demos](https://www.monitorerp.com/sv/kunskapsbank/effektivisera-med-monitor-erp/monitor-demos/) (Swedish).
