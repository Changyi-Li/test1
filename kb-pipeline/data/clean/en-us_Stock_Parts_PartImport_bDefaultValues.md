### Fallback values
The settings regarding fallback values apply for import of new parts. The fallback values are used in cases where there is no column for Part template in the import file and in the selected format template. If a part template is selected in the import file and in the format template, the values in that template will override the fallback values below.

#### Part type
Here you determine which part type should be assigned to new parts after the import.

#### Part status
There are seven different statuses for a part. These reflects a part’s life cycle (and an additional status for inactive parts) as seen in the status stages in the table below:
| Symbol | Code | Name |
|---|---|---|
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeFictitious.png) | 1 | Quote |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypePrototype.png) | 2 | Prototype |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) | 3 | New part |
|   | 4 | Normal |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeUpgrade.png) | 5 | New revision |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeDowngrade.png) | 6 | Phasing out |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/PartTypeDeleted.png) | 9 | Obsolete |
| ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/RedPadlock.png) | 99 | Inactive |
The different part statuses are fixed. It is not possible to add or delete a part status. The status of a part is shown, for example, on order rows. You can select by the part status in different lists.
The default part status is assigned to new imported parts. This will then override the part status which is entered in the system setting Default part status for new part.

#### Stock update
With this setting you decide if new parts should be stock updated.

#### Part template
You can select which part template you the parts to get during import. However, values from the template will not automatically be used for the part. Via the procedure Synchronize part template you can give the part values from the template after import.
