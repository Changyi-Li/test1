### Depreciation settings
In this box you configure depreciation settings for Scheduled and Calculated depreciation. These settings apply to the marked fixed assets group.

#### Depreciation type
The following depreciation types can be selected:
- Scheduled
- Calculated

#### Depreciation period
Here you can enter the depreciation period in number of years. The depreciation period can be entered using two decimals.
This field can be available or disabled depending on what you have selected as Depreciation method.

#### Depreciation percent
Depreciation percent per year for scheduled depreciation is automatically calculated. You can also enter the annual depreciation in percent and then the depreciation period will be calculated. The percentage can be entered using two decimals.
For calculated depreciation you enter depreciation percent for the depreciation according to plan (the annual).

#### Depreciation method
In this column you select if depreciating should be done or not for the fixed assets linked to the fixed assets group.
Straight-line depreciation is set to scheduled depreciation by default, and can be chosen for calculated depreciation.
The option No depreciation is default for calculated depreciation. This setting will make the other settings for depreciation percent/basis and posting, unavailable.
Straight-line depreciation means the depreciation is based on the asset's residual value at the start of each calendar year. However, the residual value will never be zero.
Declining balance + Straight-line depreciation means declining balance depreciation is applied at the start of the asset’s lifetime. In the year in which the object may have a higher straight-line depreciation, the straight-line method is automatically applied to the object.
You can read more about these methods and see examples of calculations [here](../Depreciation/wDepreciation.htm).
If you change from No depreciation to a depreciation method for an existing group, then the fixed assets which are linked to the group and have zero (0.00) as depreciation period will be updated and get the depreciation percent (and depreciation period for scheduled) you entered for the group when you save.
Read more about the different [depreciation methods](../Depreciation/wDepreciation.htm).

#### Depreciation percent (Declining balance)
For the declining balance depreciation method and the declining balance + straight-line method, enter the depreciation percent here.

#### Depreciation start
Here you can override the default date for when depreciation will start. In the system setting Depreciation start for new acquisition you can choose the default depreciation start. The depreciation start on a new object can be set to:
- First day of acquisition month
- Month after acquisition date
- First day of acquisition year.

#### Depreciation basis
By clicking the button Depreciation basis ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you access additional settings for calculated depreciation.
For calculated depreciation you can select a depreciation basis among the following:
- Acquisition value – The cost of acquiring the fixed assets (it is the purchase cost incl. handling costs for example freight/transport and customs duty).
- Replacement cost – The cost to replace or again acquire the fixed asset on the accounting date.
- Alternative value – This is any optional alternative value on the fixed asset. You can use alternative value if you use a work flow where you use another value than the acquisition value or the replacement cost as basis for calculating the calculated depreciation.
For calculated depreciation it is possible to enter the Depreciation share in percent. The percentage can be entered using two decimals. The depreciation share refers to how large a share of the depreciation basis which can be depreciated, normally and default this is 100.00 percent.
Depreciation basis and depreciation share apply for fixed assets where depreciating is in progress and for assets fully depreciated.
