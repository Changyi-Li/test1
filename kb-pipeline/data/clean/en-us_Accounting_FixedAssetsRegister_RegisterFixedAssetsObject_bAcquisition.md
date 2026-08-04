### Acquisition

#### Acquisition date
Here you see the date when the fixed asset was acquired. When registering a new fixed asset, today's date will be suggested. This field is mandatory.
At a new registration of a fixed assets object you will be shown a warning if the acquisition date is outside the accounting year of the system. This warning is for example shown when you register a historical object and it works as a check to make sure you do not register a fixed assets object in the wrong year.
You can change the acquisition date on existing saved fixed assets objects regardless if the depreciation has been started.
However, a check is made when you save the acquisition date. The acquisition date must be the same or earlier than the depreciation start.
Example: If the acquisition date right now is 2017-01-01 and the depreciation start was 2017-01-31, then it is not possible to change the acquisition date to a date later than the object's depreciation start. The validation error will then show that the acquisition date is later than the depreciation start. Furthermore, a check is made of the event log of the object. If the fixed assets object has event logs for changed acquisition values, then the new acquisition date cannot come after the date of the oldest change of value.
If the fixed assets object is created from accounts payable or voucher registration, the acquisition date will be set based on the voucher date on the invoice/voucher.

#### Acquisition value
You enter the fixed assets object's acquisition value in the company currency. Both positive and negative values are allowed. The acquisition value is indirect the basis for the depreciation that will be made on the object. This is done by calculating the object's residual value from the acquisition value with deduction for made depreciation.
The acquisition value can be changed if more acquisitions are added to the same fixed assets object. This is normally done via supplier invoices or vouchers which are added to the fixed assets object. You can also adjust this manually. The field is possible to edit only when registering a new fixed assets object. If it is an existing object you must use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) which open a dialog.
In the dialog you will at the top see the current acquisition value. Under it you can enter the change you wish to make, either positive or negative. The new acquisition value is automatically calculated based on what you enter in the Change field. In the same way the field for the change is updated if you enter the new acquisition value directly. You can also enter a date as of when the new acquisition value will apply.
The date suggested here is based on the following:
- If it is an object for which depreciation has not yet started, the same date as is entered in the Acquisition date field will be suggested. It is possible to change into a later date, not an earlier date.
- If it is an object where depreciating has started, the last depreciation date is suggested as date for the change. However, it is possible to change into a later date, not an earlier date.
> The fixed assets object's acquisition value can be modified via a new voucher or a a new supplier invoice. Then the object's traceability is maintained in the General ledger.

#### Initial acquisition value
This field shows the initial acquisition value of the fixed assets object. If the acquisition value is changed over time, you will here see the value which was the initial value.

#### Quantity
The default quantity here is 1 (one), but it can be changed. When making a partial disposal/partial sales it is possible to change the quantity of the fixed assets object. The purpose of having a quantity is to enter a quantity of an object which the fixed asset concerns. For example if you register several pieces of equipment in a lump and regard these as a joint fixed asset.

#### Consecutive number
Here you see the consecutive number of the supplier invoice to which the acquisition refers. If acquisition has taken place via accounts payable, then the consecutive number of the object will be taken from there. If there are multiple supplier invoices which have created the value of the fixed assets object, then it is only the first supplier invoice which is shown here. An overview of all supplier invoices for the object is shown under the General ledger tab.
It is allowed to enter a consecutive number which is not registered in the system. This might be useful when registering historical acquisitions.

#### Voucher number
Here you see/enter the voucher number for the voucher to which the acquisition refers. If acquisition has taken place via the accounts payable or voucher registration, then the voucher number series and voucher number is taken from there.
It is possible to enter a voucher number which is not registered in the system. This might be useful when registering historical acquisitions.
When supplier invoices linked to fixed assets are entered in the journal, a link is created from the fixed asset to the voucher. This is created unless a link already exists on the fixed asset.

#### Supplier
In this field you see/enter the supplier from whom the fixed asset was acquired. It is possible to manually enter the supplier but the supplier can also be set based on the consecutive number of the invoice.

#### Investment in progress
With this checkbox you determine if the fixed asset is an investment in progress or not. This function can be used if you need to gather invoices to a fixed assets object during the time of it being constructed/created. For example, a larger or more complex fixed asset which is being constructed/created during a period of time and needs to be recorded on an account for construction in progress (In Sweden: account 1180). For a fixed assets object which is an investment in progress, no depreciation is made. These fixed assets are not shown in any of the depreciation procedures. In the Fixed assets list procedure you see fixed assets account for these fixed assets as Investment in progress instead of the regular fixed assets account.
A validation takes place to check that the selected fixed assets group has an account for investment in progress. Account for investment in progress is handled in the Posting box in the procedure Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Fixed assets register. If the fixed asset's depreciation has started, it is not possible to activate the checkbox investment in progress.
For main objects and sub-objects, the following applies:
- If a main object is an investment in progress, then all linked sub-objects must also be investments in progress.
- If a main object is active (not an investment in progress) then it is possible to have sub-objects that are investments in progress.

#### Activate investment
If you click the button Activate investment, a window will appear where you can enter when depreciation should start and also enter depreciation information and voucher text for the journal/voucher which will be updated when you save the fixed assets object. There is also functionality linked to sub-objects in the dialog box where the activation takes place. In connection with activation of the object, the status of it will change from Investment in progress to Registered.
When you click the button, a dialog opens.
The fields in Activate investment for depreciation start

#### Value to activate
Here you see the total value which will be activated. The value is the same as the current acquisitions value of the fixed assets object.

#### Acquisition value
Here you see the acquisition value which will apply for the object after activation. The value in the field is the same as Value to activate in cases where you have chosen not to divide the investment in different components (this is done in the box below). If you in connection with the activation divide the fixed assets object into different sub-objects, then the acquisition value of the sub-objects will be deducted from this field.

#### Depreciation start
The depreciation start is suggested based on the depreciation start of the fixed assets object, but this can be changed. It is not possible to select a depreciation start which is prior to the start of the object. If you in connection with the activation create new sub-objects, this depreciation start will also be set for the sub-objects.

#### Depreciation period and Depreciation percent
These are suggested based on what has been configured for the object, but this can be modified. If the setting Final depreciate sub-object concurrently with main object has been activated the sub-objects which are created will automatically get the same values.

#### Voucher text
The default text here is "Activation of investment". These texts are handled in the Voucher texts procedure.

#### Integration type
Here you can select the type of integration you want to apply.

#### Final depreciate sub-object concurrently with main object
If this setting is active it is not possible for you to edit the depreciation period and depreciation percent for the objects you have added in the box below.

#### Divide into sub-objects (components)
In this box you can add fixed assets objects. If the setting above is activated it is not possible for you to edit the depreciation period and depreciation percent.
