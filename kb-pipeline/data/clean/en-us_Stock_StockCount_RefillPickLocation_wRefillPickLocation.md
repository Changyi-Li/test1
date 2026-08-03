## Refill pick location
This procedure is used when pick locations are applied in the system. The purpose of this procedure is to efficiently create a refill basis for pick locations. This is based on the reorder point and refill quantity of the pick locations. Thereafter the pick locations will be refilled from buffer locations when balance reaches the reorder points.
Pick locations are locations where one or both of the alternative Pick location and Pick location for work center have been activated. Other stock locations are considered buffer locations.
List types

#### Reorder point list for pick locations
Here you find parts that have a pick location and/or a pick location for work center. Only parts where the current/disposable balance on each pick location falls below the reorder point on the pick location are shown in this list. This is determined by a setting. In the list, you check the box in the Apply column for the pick locations you want to refill. The reorder point list is created by clicking the button Generate ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar.

#### Print refill tasks
Here you load and print a refill task where you see the parts which need to be refilled in their pick location. In the list, you check the box in the Apply column for parts that should be included in the document Refill pick location. The document is created by using the button Generate ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) on the toolbar.

#### Report refill of pick locations
Here you report the quantity that has been moved from buffer location to pick location. The list consists of two boxes. In the box called Pick location to refill, you check the box in the Apply column for the pick locations which should be refilled. In the box called Buffer location to move from, the quantity will then automatically be filled in. If the quantity on one buffer location is not sufficient, the quantity will be taken from more than one of the available buffer locations in the box. The distribution between buffer locations is made using the same rules as for withdrawal from stock locations, That is, primarily from the location with the highest priority, and secondarily based on age analysis. The above mentioned document Refill pick location is used as basis for reporting.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
