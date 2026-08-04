### Report and follow-up on income, costs, and time

#### Income
The planned/ordered income on the project are the postings on customer order rows marked with the project number in question and where the account is inked to a cost type/income type referring to income.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectCustomerOrderRow.png)](../../../../Resources/Images/TrainingMaterial/ProjectCustomerOrderRow.png)
Result refers to income of sales (in the project) which have been recorded in the accounting. The actual result regarding income is loaded from postings in the general ledger, for accounts linked to the above mentioned cost type/income type.
Expected result for income is loaded from the remaining value left to deliver/invoice for linked customer orders plus the actual result of income.

#### Costs from manufacturing order
Costs from the manufacturing order are divided in three fixed cost types Material – Manufacturing order, Subcontract – Manufacturing order, and Work – Manufacturing order.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectCostsManufacturingOrder.png)](../../../../Resources/Images/TrainingMaterial/ProjectCostsManufacturingOrder.png)
All projects will by default make a reading of costs from here, but it is possible to create exceptions for this in the procedure Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Project. The exceptions are created per project type. This can for example be done if you wish to see the result for subcontracting costs from the subcontract account in the accounting instead of for manufacturing orders.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectCostsSubcontract.png)](../../../../Resources/Images/TrainingMaterial/ProjectCostsSubcontract.png)
Then it is important to register a separate cost type for subcontract which you link to the subcontract account in the chart of accounts. The checkbox Load subcontract cost above must then be unchecked, otherwise the cost will be doubled.
Manufacturing costs on the project are absorbed via manufacturing orders that are linked to the project number in question.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectManufacturingOrderRow.png)](../../../../Resources/Images/TrainingMaterial/ProjectManufacturingOrderRow.png)
The planned cost of the order for material, subcontracting, and work are recorded as Planned/Ordered in the project. Reported costs are recorded as Result in connection with when you report on the order. The total of what have been reported + what is remaining on the manufacturing order will be recorded as Expected result in the project.
For the cost type Material – Manufacturing order you can create exceptions on part level regarding whether the reading should be done from the manufacturing order or not. If there is material purchased directly for the project and you wish to absorb the cost for these via supplier invoices/accounting, you should in the Part register activate the setting Purchase on project.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PurchaseToProjectPart.png)](../../../../Resources/Images/TrainingMaterial/PurchaseToProjectPart.png)

#### Costs from customer order
To load material costs from customer orders might be useful when you need to absorb costs for material in the project which is neither on the manufacturing order nor has been purchased on the project. In order for this type of reading to take place, it is required that the part is not purchased on the project, that is, has the above setting deactivated Purchase on project, and that the project type has the setting Load material cost from customer order activated.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ProjectCostsMaterialCustomerOrder.png)](../../../../Resources/Images/TrainingMaterial/ProjectCostsMaterialCustomerOrder.png)
> If you are posting cost of goods sold (COGS) for the project you should not load material cost from customer order with the above mentioned setting, since that material cost can then be doubled.

#### Other cost types
Other cost types on the project refers to e.g. external work, traveling, direct material purchase, time reporting for personnel, etc. These are defined under the tab Costs/Income in the procedure Basic data – Project and are of the type Cost.
Result for other cost types are absorbed via:
- The cost is recorded on an account which in the chart of accounts is linked to any of the other "free" cost types.
- The cost is reported in the Direct project reporting procedure.
- You report time for activities where the activity has been linked to a cost type and the hourly cost has been entered for the cost type in the procedure Basic data – Project.
Planned/Ordered for other cost types is determined by how the cost type has been set in the column Planned is loaded from in the procedure Basic data – Project. For example you can absorb the following records:
- Purchase orders on the project where the account on the order row is linked to other cost type.
- Planned cost from activities. It is required that planned hours have been entered on project activities and that the activity in its turn is linked to a cost type.
Expected result for other cost types is determined by how it has been set in the column Expected result is loaded from in the procedure Basic data – Project.

#### Time used
Reported time can be added to the project from:
- Reported time on the manufacturing order.
- Reported time in the Direct project reporting procedure.
- Reported time via activity reporting on the project.
