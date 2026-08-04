### The Project register
The Project register procedure is the central procedure in the project accounting. You can manually register a project in this procedure, but you can also automatically create the project from the Register customer order procedure.
You find a description of all information and functions available in the project register under the topic [Project register](../../../Accounting/Projects/ProjectRegister/wProjectRegister.htm).
> You can right-click in the procedure to see information regarding the project from other affected procedures in Monitor ERP, e.g. Invoicing log, Loading plan, etc.

#### The General tab
Under the tab you enter project number, name, and project type. Other info is optional to enter.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectRegisterHeader.png)](../../../../Resources/Images/TrainingMaterial/ProjectRegisterHeader.png)

#### The Costs/Income tab
Under this tab you get an outline of costs and income according to budget, planned, result, expected result, and forecast per different cost types and income types. This data is loaded from the different modules in Monitor ERP. You can also see CMThe contribution margin (CM) is the difference between the standard price and the sales price./CRThe contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage. % for each column.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectRegisterCostsIncome.png)](../../../../Resources/Images/TrainingMaterial/ProjectRegisterCostsIncome.png)

#### The Phases/Activities tab
The phases and activities are created based on default values of the project type. These can be changed for the project in question. You can insert activity templates, if needed. You can also report activities here.
A phase shows start and finish date based on first start date and last finish date of the activities included in the phase. The phase totals the activities' planned and reported hours, and costs. It is not possible report on a phase. The status of a phase is determined by the status of the activities. If no activity is started it means the phase is also not started. When an activity is started the phase becomes started as well. When all activities have been finished, the phase will also be finished.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectPhasesActivities.png)](../../../../Resources/Images/TrainingMaterial/ProjectPhasesActivities.png)

#### The Lead time chart tab
The lead time chart gives you a graphic display and planning of project activities. The lead time chart is based on the phases and activities in the projects. At the bottom of the chart you also see linked manufacturing orders, customer order, and purchase orders, if any. So-called tooltips show information about customer order, manufacturing order, and purchase order. The lead time chart is separately presented per project together with its sub-projects, if any. It is possible to decide that phases or activities must be performed in a specific order. This is done by linking the phases/activities to each other. By using different dependency types you can create dependencies between two or more activities and decide which type of dependency that should exist between them. Please note! There is a limitation which makes it possible for a project to either have dependencies between activities or dependencies between phases. Read more about [dependency types](RelationTypes.htm).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/LeadTimeChart.png)](../../../../Resources/Images/UserGuide/LeadTimeChart.png)

#### The Logging tab
Here you can log e-mail conversations regarding the project and you can also make notes for the project in question.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectLogging.png)](../../../../Resources/Images/TrainingMaterial/ProjectLogging.png)

#### The Purchase tab
Under this tab you see inquiries, purchase orders, invoice bases, and supplier invoices which are linked to the project.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectPurchase.png)](../../../../Resources/Images/TrainingMaterial/ProjectPurchase.png)

#### The Manufacturing/Stock tab
Under this tab you see manufacturing orders, cases, and parts which are linked to the project.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectManufacturingStock.png)](../../../../Resources/Images/TrainingMaterial/ProjectManufacturingStock.png)

#### The Sales tab
Under this tab you see quotes, invoice bases, and customer invoices which are linked to the project.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectSales.png)](../../../../Resources/Images/TrainingMaterial/ProjectSales.png)

#### The Time check tab
Here you can see the budgeted and actual time spent. Actual time spent can come from:
- reported time on the manufacturing order
- time reported in the Direct project reporting procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectTimeCheck.png)](../../../../Resources/Images/TrainingMaterial/ProjectTimeCheck.png)

#### The Budget/Forecast tab
Here you can create a budget and a forecast for costs, income, and time. The costs that exist as default values for the project type will be entered automatically. You can enter hours on all cost types except for subcontract and material. If you enter hours, the cost will be calculated based on the cost type in the basic data. CM and CR % are displayed. It is possible to can copy a budget to forecast by using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_to.png) on the function menu.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectBudgetForecast.png)](../../../../Resources/Images/TrainingMaterial/ProjectBudgetForecast.png)

#### The Documents tab
Here you can print a summary of the project as one document. You can select document: internal project report or external project report. You can also difference and difference in percent.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectDocuments.png)](../../../../Resources/Images/TrainingMaterial/ProjectDocuments.png)
