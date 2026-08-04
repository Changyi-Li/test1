### Depreciation
This box shows information regarding the depreciating of the fixed assets object. The columns here show information about scheduled, calculated, and tax depreciation. If the fixed asset belongs to a group where calculated depreciation is not made, then the fields in that column will not be available. Read about how the scheduled depreciation is calculated in the [help topics for Depreciation](../Depreciation/wDepreciation.htm).
If the fixed asset belongs to a fixed assets group which in the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Fixed assets register have component depreciation selected on the row for tax depreciation, then the column Tax will be shown.

#### Depreciation start
Here you enter the date when the depreciating should start. The depreciation start for a new acquisition is set according to the system setting Depreciation start for new acquisition. This date can be changed manually if you want to start the depreciation at another date. It is also possible to select a future date. If the depreciating has been started it is no longer possible to edit the start date.
Example: When the system setting above is set to First day of acquisition month. You create a new fixed assets object with the acquisition date 2017-05-08. Then the depreciation start will automatically be set to 2017-05-01.

#### Depreciation period
Here you can enter how long the depreciation period should be for the fixed asset in question. The depreciation period of the selected fixed assets group will be used by default, but it can be changed per fixed asset.
The depreciation period is entered in number of years with a maximum of two decimals. This field is mandatory and it is not possible to enter zero (0.00) or a negative value. It is possible to enter a depreciation period shorter than one year.
This field affects – and is also affected by – the field Depreciation percent.
For example, if you enter 10.00 years, it means the depreciation percent will be set to 10.00%. If you enter 0.50 years, it means the depreciation percent will be set to 200.00%.
Change depreciation period
If the fixed asset is sold/retired or if the fixed asset's residual value is zero (0.00) meaning there is nothing left to depreciate on the asset, then it is not possible to modify the depreciation period. If the depreciating has started it is not possible to change the depreciation period directly in the field. You must then click the Change depreciation period button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) which opens a dialog where you can enter the new depreciation period.
A validation error is shown if the new acquisition period means that it is too short, that is, after the depreciation period there must at least be time to make an additional depreciation on the fixed asset in question. The values you have entered must lead to that the new depreciation end is after the date for the most recent depreciation.
Link to main object
If the fixed assets object in question is linked to a main object, then the checkbox Final depreciate sub-object concurrently with main object becomes activated in the dialog where you change depreciation period. It determines if the depreciation period should be adapted to the main object's remaining depreciation period (provided that the main object is not already fully depreciated or sold).
Thus, the new depreciation end is loaded from the main object at the same as a new depreciation period and depreciation percent is automatically calculated based on what is needed in order to have it fully depreciated at the same time as the main object. A check is made to make sure that the new depreciation end must have a date which is later than the date of the most recently made depreciation.
> A main object might already have been depreciated for a certain amount of time when a recently registered sub-object afterwards is linked to the main object. In that case it is desirable that the depreciation period of the sub-object reflects the remaining time of the main object.
Change depreciation period on main object
If the fixed asset for which you want to change depreciation period is a main object, then another dialog will open where the main object's current values and new values are shown at the top.
The linked sub-objects are shown in a table (unless they have been fully depreciated or sold). The table can be useful in the following examples:
> If you want to change the depreciation period for a main object and at the same time have linked sub-objects which also should be included in this change, that is, if the sub-objects should be fully depreciated at the same time as the main objects in connection with changing of the main object's depreciation period. Then you should use the checkboxes Change depreciation period on each row to mark that the sub-object's depreciation period should be adjusted.
These checkboxes are marked by default if the main object and the sub-object prior to the adjustment had the same depreciation end, then it is assumed that they should be fully depreciated at the same time.

#### Depreciation percent
Here you enter a percentage for annual balance depreciation, with a maximum of two decimals. This field is mandatory and it is not possible to enter zero (0.00) or a negative value. What you enter here affects – and is affected by – the field Depreciation period above. If the depreciating has started, this field is not possible to edit. Change of depreciation percent is then made via change of depreciation period, see above.

#### Depreciation percent (Declining balance)
Here you enter a percentage for annual declining balance depreciation, with a maximum of two decimals. This field is mandatory and it is not possible to enter zero (0.00) or a negative value. What you enter here affects – and is affected by – the field Depreciation period above. If the depreciating has started, this field is not possible to edit. Change of depreciation percent is then made via change of depreciation period, see above.

#### Depreciate to residual value
You can enter a lowest residual value here. This prevents the residual value according to plan from reaching zero. For a fixed asset intended to be sold after the end of the depreciation period, you can here enter the estimated value of the object at the end of the period of use. This results in a lower depreciation and at the same time in a lower capital gain at the disposal of an object. When depreciating, the basis for the depreciation will be reduced by this value.

#### Depreciated to
In this field you see most recent depreciation made. When registering historical fixed assets you can enter accumulated depreciation and date for the most recent depreciation made by using the button Historical object.

#### Remaining depreciation period
This is used and shown if the system setting Method for scheduled depreciation is set to Allocate residual value over the remaining depreciation period. Here you can see the remaining time in days or months depending on the system setting Depreciation is based on. 5 years depreciation can be shown as 60 months or 1825 days.

#### Depreciation end
This is used and shown if the system setting Method for scheduled depreciation is set to Allocate residual value over the remaining depreciation period. Here you see the date when the fixed asset is fully depreciated. For sub-objects you will in certain cases see the button Final depreciate sub-object concurrently with main object ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_time.png). With this button you open a window which shows that the depreciation end is set to the same as the linked main object's end. When you click OK it means that also the depreciation period and the depreciation percent will be changed. This is useful of you want to set a depreciation period/percent on a sub-object based on the main object's depreciation end date.
This button is not available if:
- Depreciating has started.
- The fixed assets object is not linked to a main object.
- The main object is sold or fully depreciated (residual value is zero).
- This would mean a new depreciation period which means that it is too short.

#### Alternative value
Here you enter an alternative value to base the calculated depreciation on.

#### Accumulated depreciation
(Scheduled) Shows the object's scheduled accumulated depreciation. When registering historical fixed assets you can enter accumulated depreciation and date for the most recent depreciation made by using the button Historical object.
(Tax) Next to the field you find the button Tax depreciation ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) which opens the dialog where you can add previous tax depreciation. You select accounting year and then enter the amount in the Depreciation field. The values for accumulated value and residual value are calculated continuously after what you enter. If you add previous years, values for later entered years will become updated.
It is only possible to select among the accounting years registered in the system. If you have tax depreciated the fixed asset several years prior to the accounting years registered in the system, you can enter the accumulated depreciation as a lump amount. This can for example be done in the first accounting year you can select among or the last accounting year prior to the current accounting year. This depends on if you want to be able to go back several years and see the correct accumulated depreciation. If you register a historical tax depreciation for the fixed asset, this depreciation will be shown until the end date of that year.
If you have registered an accumulated tax depreciation for the fixed asset for a year or saved to your calculation for the final accounting year, you will see the accumulated depreciation in italics (in the list in the Tax depreciation procedure). Then no additional depreciation made for that fixed asset will be saved. If you wish to redo the tax depreciation for that year you either have to edit or delete the fixed asset. If you delete the row with that year you can perform a recalculation and save.

#### Residual value
Here you see the residual value of the fixed asset. This is sometimes referred to as the book value or accounting value. The residual value is the difference between the acquisition value and the accumulated depreciation made for the fixed asset. During a new registration, the residual value will always display the same amount as the acquisition value.

#### Historical object
This button is available when you are registering a new fixed asset. It is also available for existing objects which have been added as historical objects, for which no additional depreciation has been made. The purpose of this button is to access the registration of information necessary when registering objects which are old fixed assets (for example during the start-up when coming from another system).
In the dialog which opens when you click the button it is possible to add depreciation information from depreciation already made.
The fields in the Historical object window.

#### Depreciation start, Depreciation period and Depreciation percent
These are information field which display what have been entered for the fixed asset in question.

#### Depreciated to
In this field you select the date of the most recent depreciation made.

#### Accumulated depreciation
Here you see the depreciation which have been accumulated. However, this value can be changed. The accumulated depreciation is based on acquisition value, depreciation start, and depreciation period, entered on the fixed asset.

#### Residual value
This is an information field where you see the residual value of the fixed asset (acquisition value reduced with the accumulated depreciation).
