### Header row

#### Fixed assets objects
This is an alphanumerical field where you can select an existing fixed asset or enter and create a new. If you save a new fixed asset without having entered anything in this field, then the object will be named according to the number series for fixed assets objects. You enter the name in the next field. You can use a maximum of 40 characters.

#### Fixed assets group
Here you can enter the fixed assets group to which the fixed assets object belongs. Fixed assets groups are registered in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Fixed assets register procedure. These groups determine and suggest the objects' depreciation period, postings, etc. You can change fixed assets group as you please as long as no depreciation has been started on the object in question. In that case you must use the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) to open a dialog where you can change fixed assets group.
> If you change from one group which is depreciable to a group which is not depreciable, a validation error will be shown stating that it is not possible to have depreciation in that group. To get around this you can undo the depreciation and then change to the group which is not depreciable. This might be useful if you have started depreciating a fixed assets object and at a later stage found that it directly should be carried as an expense.
A warning will also be displayed if you change from one group with one fixed assets account to a group with another fixed assets account. The purpose of this warning is to call attention to that the change might cause a difference between the fixed assets list and the bookkeeping at the reconciliation.

#### Main object
Here you can enter the object number for the main object if the object in question is a sub-object to another fixed assets object. A sub-object can for example be incorporated components in a larger or more complex fixed asset. It is not possible to enter a main object which in its turn is a sub-object to main object. You can delete the link to the main object at any time, regardless if the depreciation has started or not.

#### Status
Here you see the status of the fixed assets object:
- Registered
- Depreciation started
- Fully depreciated
- Sold – if the entire fixed assets object is sold.
- Retired – if the entire fixed assets object is retired.
- Investment in progress.
