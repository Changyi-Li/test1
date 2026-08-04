### Basic data for projects
In the procedure Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project you register data which will then be used as default values when a new project is registered. Basic data also consists of setting which affect how costs are calculated. You find the description of this information under the help topic [Basic data – Project](../../../Accounting/Projects/BasicDataProject/wBasicDataProject.htm).

#### The Project types tab
The project type determines for example activities, default values for project manager, mark-ups, priority, etc. for the project. These project types can later be used to have different default values. They can also be used as selection terms in lists.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectTypes.png)](../../../../Resources/Images/TrainingMaterial/ProjectTypes.png)
In the Costs column you can determine per project type if and how loading of costs takes place from manufacturing or customer orders. Read more about these costs under the heading The Costs/Income tab below.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectTypesCosts.png)](../../../../Resources/Images/TrainingMaterial/ProjectTypesCosts.png)

#### The Phases tab
Here you register different phases that can occur in projects. Phases are used in activity templates, see below.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectPhases.png)](../../../../Resources/Images/TrainingMaterial/ProjectPhases.png)

#### The Activities tab
Here you register the activities that can occur in different projects. Activities can then be added to the projects you register. Activities can also be linked to cost types, which means that the reported time will also be regarded as a cost on that cost type.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectActivities.png)](../../../../Resources/Images/TrainingMaterial/ProjectActivities.png)

#### The Activity templates tab
Here you register different activity templates that can be used in different projects. An activity template can consist of different phases which in their turn consist of different activities. An activity template can also only be a set of activities.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectActivityTemplates.png)](../../../../Resources/Images/TrainingMaterial/ProjectActivityTemplates.png)

#### The Costs/Income tab
In this table you register different cost types/income types used to report costs, income, and hours, on the project. The top four cost types are fixed cost types which are included in the system. These cannot be deleted. The three top cost types are connected to costs loaded from manufacturing orders. The fourth cost type is connected to costs loaded from customer orders.
For other cost types/income types you can select from where Result, Planned, and Expected result should be loaded.
The hourly cost which you can enter will be the default price per unit in the Direct project reportingprocedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectBasicsCostsIncome.png)](../../../../Resources/Images/TrainingMaterial/ProjectBasicsCostsIncome.png)
To be able to know which costs and income that are ordered and recorded in the project, you should for the affected accounts in the Chart of accounts procedure select which cost type or income type should apply for the posting dimension linked to the project register.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ChartOfAccountDimensionProject.png)](../../../../Resources/Images/TrainingMaterial/ChartOfAccountDimensionProject.png)
The link of the posting dimension to the project register should first be done in the DimensionsDimensions are used by large companies in their accounting in order to divide up activities and make it easier to track internal results. An account is a dimension, although large companies usually use the dimensions cost center (CC), cost unit (CU) and project. In addition to these you can create other dimensions in Monitor ERP based on your own operational follow-up. procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CodingDimensionProject.png)](../../../../Resources/Images/TrainingMaterial/CodingDimensionProject.png)

#### The Project groups tab
You can also register project groups. These project groups can later be selected for the project type and be used as selection terms in lists. However, it is not mandatory to use project groups.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectGroups.png)](../../../../Resources/Images/TrainingMaterial/ProjectGroups.png)
