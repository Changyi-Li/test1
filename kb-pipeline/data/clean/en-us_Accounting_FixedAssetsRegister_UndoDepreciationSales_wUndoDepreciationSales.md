## Undo depreciation/sales
This procedure is used in connection with when you need to undo depreciation or sales/retirements. The procedure is for example useful if you want to undo depreciating you just performed, which means the depreciation will be reversed for many fixed assets at the same time. Another purpose might be to undo depreciation for a specific fixed asset, for example if depreciating has been done for a period of time for a fixed asset, but needs to be undone or has been incorrectly performed due to new circumstances. It is also possible to undo sale of a part of the fixed asset.
If yo need to undo more than one depreciation item, then it is necessary to undo these in the correct order: from the most recently made and continue back in time. This can be done under the tab called Undo per object.
Depending on if depreciation/sale has been transferred to the general ledger or not, different things will happen:
The depreciation/sale is not recorded
When you undo a depreciation item which is not recorded, then the depreciation of the fixed asset will be undone and the event log regarding the depreciation will be deleted on the asset.
Depreciation/sale is recorded
When you undo a recorded depreciation, it means the fixed asset's depreciation will be undone at the same time as a posting is created which reverses the initial depreciation. A log record of the type Undo depreciation is also created under the Event log button.
When using direct integration a contra entry will directly be recorded when you undo, without needing a journal printout.
List types

#### Undo scheduled depreciation
By using this list type you can undo scheduled depreciation, either via a list to undo depreciation for many fixed assets at the same time or via a tab when you undo for a single specific fixed asset.

#### Undo sales/retirement
Via this list type you can undo sales/retirements of fixed assets.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
