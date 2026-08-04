### Header row
On the header row you will find the basic settings for a work center, e.g. type, and the department and warehouse it belongs to.

#### Work center
The work center is the most important information in this register. In this field you will see the most recent work center that has been loaded. By using the LookupThe Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. feature, you can select another work center. You can enter a new work center code (alphanumerical, with a maximum of 8 characters) and leave the field using Tab in order to create a new work center. You can also click the Create new button or press (Ctrl + N) in order to create a new work center.
A new record is highlighted by a green dot ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) shown in the field. This dot will disappear when the record is saved for the first time.

#### Name
Here you see/enter the name of the work center. It should be entered in the company language. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Type
Here you select the type of the work center. A work center can be any of the following types: Machine (default), Manual work, Pool, or Subcontract. The type selected affects the functionality and some of the fields. Thereby it determines the information that can be entered for a work center. It can also be used as a selection term.
- Machine – This work center is a machine which is manned by one or several persons, for example punch, lathe, welding equipment.
- Manual work – This work center only consists of one or multiple persons, for example assembly.
- Pool – This work center is a pool work center consisting of multiple work centers used for pool planning. Read more in the online help function for the procedure Pool planning.
- Subcontract – This work center is a subcontractor which is hired to do subcontract work.
- Picking – a work centersimilar to manual work, but with the addition that the mobile pick list starts and ends the operation. No automatic material reporting is performed when reporting the operation, since the material is instead reported via the pick list.

#### Operation name
Here you see/enter the operation name. By default, it is the same as the work center's name, but it can be changed. The operation name will then be default as the operation name of new operations when the work center is selected in BOM and routing.
The work center's name can be the same as machine's name and model, for example "Okuma MB-4000H", while the operation's name for example can be entered as "Okuma NC". By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.
> If the operation's name differs from the name of the work center, the operation's name will not be changed if a user later on changes the work center for an operation in a BOM and routing. The purpose of this is that it is possible to enter specific information for a certain operation via the name of the operation. That is why this information will not be removed if someone should change work center for the operation. The same applies for manufacturing orders. If the name of an operation is changed for a specific order, then that name will only apply for that order.

#### Department
Here you select to which department the work center belongs. Departments must first be registered in the Departments procedure.

#### Warehouse
This field is available if you have the option Warehouse. Here you select the warehouse to which the work center should belong. A work center of the Pool type and its related/included work centers must belong to the same warehouse. It is optional to enter a warehouse, if the work center is of the type Subcontract.
