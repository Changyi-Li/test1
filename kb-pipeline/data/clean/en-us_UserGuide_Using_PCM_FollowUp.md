### Follow-up features
For the Percentage of completion method (PCM), there are lots of options for follow-up of the calculations performed in different procedures.

#### Project register – the PCM follow-up tab
Under this tab you find a summary of the performed revenue calculations (the journal has to be printed/reset) for the project in question. The summary shows the conditions on which the calculation was based at the time it was performed regarding forecast, result, stage of completion, mark-up, total recognized income, and if the stage of completion was edited manually. Here you see the voucher number where the recognized income was posted, as well as who approved the calculation and when.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PCM5.png)](../../../../Resources/Images/UserGuide/PCM5.png)

#### Revenue calculation – Previous calculations list type
In this list type you will only see already performed calculations where the revenue calculation journal for that period is reset. The list shows the conditions on which the calculation was based at the time it was performed regarding forecast, result, stage of completion, mark-up, and recognized income. There are multiple selections you can do in the list.
> Please note! If you select an interval spanning multiple periods, the amounts will be added together as they are. This means, for example, that the same forecast for the same project will be added together multiple times. If you select only one period you can use the list to compare to the balance account for the recognized income.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PCM6.png)](../../../../Resources/Images/UserGuide/PCM6.png)

#### Invoice basis – Sales and Purchase
You can add Project type as a selection row. This column is also available under Presentations in backstage to be shown in own presentations. Project on posting rows (as dimension) is available in these two procedures.

#### Stock value – Project list
This list is based on records reported for a project in the stock transaction log. You can check the stock transaction log records which have been reported for projects and which are the bases for the balance in the list in the stock transaction log.
Prerequisites:
- You purchase for project and consume/sell for the same project.
- You manufacture for project and sell for the same project.
The list requires an arrival on a project in order for the part to be shown in the list for the project in question. The list does not display an "actual balance" for the part in question, but only what is reported according to the stock transaction for project.
Example: If you purchase 10 pieces for project A, and you consume 10 pieces without a link to a project, this means that the balance is 0. But if you select the list by project A, the list will show a balance of 10 even though the total balance is 0. If you purchase 10 pieces for project B and stock count 5 pieces, it means that the total balance is 5. But if you select the list by project B, you will see a balance of 10 even though the total balance is 5.
If you only have consumption/sales on project, that is, no arrival reporting has been made, you can mark Show parts with negative balance on project to show these parts in the list.
There are procedures where you report items that will affect the balance but where there today is no support for projects, such as e.g. stock counts. If you discover incorrect reporting items, you can correct these in the Direct stock reporting procedure.

#### Manufacturing order log
You can add Project in own presentations of the lists.

#### WIP value
It is possible to select by Project type and Project.

#### Management accounting
For the Stock transaction log, Manufacturing order log, Calculation difference, and Invoicing log, you can add Project and Project type. This is done under Other terms in the Register posting method procedure.
