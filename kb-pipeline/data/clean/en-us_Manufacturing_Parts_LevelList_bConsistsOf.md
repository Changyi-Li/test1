### Consists of (structure map)
This list shows the parts that have been selected. Under the parts you see their structures.
The top part node is marked by default. For the selected part you will see which other structure parts it is included in. That is shown in the [Included in](bIncludedIn.htm) list.
If you have selected parts that do not consist of any material or operations, they will be shown without a structure. This is done in order to be able to perform an "included in" analysis of purchased parts. If you have also selected operations to be shown, they are included in the structure along with information about the operation number and operation name.
Function buttons
There are function buttons to preview the list before printout and to print it. In the preview window it is possible to select whether or not you wish to include the selection view in the printout. There are buttons you can use to search among the records (Ctrl + B) and to copy them to Clipboard. There is a button you can use to expand and minimize (Shift + F8) all the nodes in the structures. There is also a button to open the marked record in a related procedure.

#### Part type/Operation
In the first column you see the part type/operation indicated by a symbol.

#### Basic type
Here you see the part's basic type. It is loaded from the part template which the part is linked to. Basic type is mainly used for tools and is available when the Tools & Maintenance option is installed.

#### Part/Operation
This column shows the part number or operation number.

#### Name
Here you can see the part name or operation name.

#### Quantity
This column shows the material quantity for the main part in the default unit (standard unit).

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
New parts will get a default part status which is determined using the system setting Default part status for new part.
The More information button
By clicking the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) at the far left of the list, you find additional columns with information from the BOM and routing and the part register.
