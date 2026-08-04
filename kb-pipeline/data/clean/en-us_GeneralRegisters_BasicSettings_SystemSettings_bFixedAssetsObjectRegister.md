### Fixed assets register

#### Method for scheduled depreciation
With this system setting you decide which method should be used to calculate scheduled depreciation. The following methods are available:
-   
Allocate residual value over the remaining depreciation period (default value)
-   
Percent of acquisition value

#### Depreciation is based on
This system setting determines if the depreciation should be based on days or months. This determines for example how the remaining depreciation time will be presented.

#### Depreciation start for new acquisition
This setting determines which date should be set by default at the depreciation start. The depreciation start on a new object can be set to:
- First day of acquisition month
- Month after acquisition date
- First day of acquisition year.
You can override this at fixed assets group level in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Fixed assets register procedure.
If the setting Depreciation is based on has been set to Days, you can also select Acquisition date.

#### Execute full depreciation in connection with sales/retirement
If you select Yes here, a check will be made in connection with sales/retirement. The system then checks how much has been depreciated previously and makes a new depreciation up until the sales date/sales month.
The system setting applies regardless of whether the depreciation is based on months or days.
