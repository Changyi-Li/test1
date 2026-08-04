### Header row
On the header row you select if an existing project should be loaded or if an new project should be registered. Here you also do basic settings for a project.

#### Project number
Here you can select a project number to load an existing project. If you enter a project number which do not exist or if you leave the field empty, a new project will be created. If you leave the field empty the next available project number will be loaded from the project number series once the project is saved. It is also possible to give the project a prefix in front of the project number based on the project type you create. This is configured in the Basic data With "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project procedure. You can enter a maximum of 15 characters.
A new record is highlighted by a green dot ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/green_dot.png) shown in the field. This dot will disappear when the record is saved for the first time.
If you delete a main project, the links to its sub-projects will be deleted, this means that the sub-projects will now become separate projects.

#### Name
Here you see/enter the name of the project. It is possible to edit this field also for existing projects. For a new project, it is mandatory to enter a name.

#### Project type
Here you see/select the type of project. The project type you have set as default in your user account, will here be suggested by default. If you do not have a default entered there, the first project type will be suggested. It is possible to select another project type, when needed. By using the Change project type button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) you can also change the project type for an existing project.
A few project types are included in new MONITOR systems to use as examples. Other project types that you need must first be registered in the Basic data – Project procedure. The project type governs many default settings in a project. Such as: prefix, priority, if the project should be inactive, project group, activity template, project manager, costs, internal and external comments, and linked files.

#### Project manager
Here you see/select the project manager/the person responsible for the project. You can select among the persons marked as project managers in the personnel records. The default option here is loaded from the selected project type.

#### Activity template
The activity template of the project determines which default phases and activities should exist in the project. The template is loaded from the selected project type by default.
Under the tab Phases/Activities you can in an individual project also insert or add additional activity templates, separate phases and activities. Under this tab you can edit or delete these from the project in question. If the project has activities where nothing has been reported, then it is possible to change template by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_record.png) next to the field. If these circumstances are not filled, then this button is not available.

#### Main project
Here you enter which main project the sub-project in question should be linked to. If a main project has been loaded in the procedure, the Main project field is not available.

#### Phase view
The arrow symbols show how far the project has come based on the status of the phases. Under the Phases/Activities tab you will see the phases and activities, and also their statuses in detail. A phase can have one of the following status options: Not started, Started, and Finished. The number of phases in a project varies. The phase view shows one arrow per phase in different colors for each status. That way, it is easy to see what the situation is like for the project.
You can see up to 10 phases (arrow symbols). If 11 phases or more are included in the project you will instead see a percent number since only 10 arrows can be displayed. For example, if 3 out of 11 phases are finished, the percentage shown will be 27%. Projects without phases are shown in a percentage based on the activities.
Color for each status:
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_1.png) – Not Started
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_2.png) – Started
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/phase_img_3.png) – Finished

#### Stage of completion
If you apply the Percentage of completion method, the stage of completion is shown according to the calculation basis you selected for the project. The header shows the stage of completion only in the interval 1-100%. If the calculated stage of completion exceeds 100% or falls below 0%, the percentage will be displayed in red italicized font. If you place the cursor over the percentage, you will see the actual stage of completion in a so-called tooltip.
