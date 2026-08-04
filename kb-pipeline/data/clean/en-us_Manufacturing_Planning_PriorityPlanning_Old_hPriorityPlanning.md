### Header row – Former layout
On the header row you select the work center for which you wish to replan the operations. The operations that are shown all have a remaining quantity. It is also possible to show operations in manufacturing order suggestions.
You will see a total of the number of operations and their number of hours. There are also some filters that you can activate to only show the operations that fulfill the term(s). Under each filter term, there is also a total of the number of operations and their hours that fulfill the term in question. This way you get a quick overview of the situation in the work center and can focus on (filter) these critical operations for further actions. These totals can also be seen in the total [list](../PriorityPlanList/tListTotal.htm) in the Priority plan list procedure.
You can also activate and configure a time horizon in number of work days to not show orders that are unnecessary far ahead in time. You can also activate a simulation factor in percent for the work center and change it temporarily in order to see how it would affect the priority planning.
If you check or uncheck the checkboxes In progress, Prioritized, Ready to run ((P)), Ready to run ((M), or Simulation factor, a new calculation of New finish will be made for the operations.
All the filters and settings made on the main row apply to both the priority plan and the lead time chart. The procedure also remembers which filters which you activated the last time in the procedure, except for the settings Time horizon and Simulation factor.

#### Work center
Here you enter the work center in the selected warehouse for which you wish to replan the operations. The name of the work center is shown to the right. In the toolbar of the procedure you can choose the warehouses from which you want to be able to select the work center.

#### Show suggestions
With this setting you determine if operations from manufacturing order suggestions should be shown. The order suggestions are displayed with a pound sign (#) in front of the order number in the Order number column.

#### Total
Here you see the number of operations in the priority plan and how much accumulated time they contain combined.

#### In progress
Filter which only shows operations in progress.

#### Prioritized
Filter which only shows prioritized operations. That is, the operations that have a priority number entered in the Prioroity of operation column (P.op).

#### Ready to run (P)
Filter which only shows operations where the previous operation has zero (0) as remaining quantity. That is, the operations that have an F (finished) in the Previous operation column (P).

#### Ready to run (M)
Filter which only shows operations where the material is available or not required. Meaning where all material is cleared. That is, the operations that have a C (cleared) in the Material availability column (M) or where that column is empty.

#### Are late
Filter which only shows operations that are already late. That is, operations that have a date in past time in the column Planned finish.

#### Will be late
Filter which shows the operations that probably will be late. That is, the operations where New finish is later than the Planned finish. To make this easy to see, the date columns and the Difference column are shown in red.

#### Time horizon
Filter which shows the time horizon in number of work days for the priority plan/lead time chart. The system setting Time horizon filters by determines the date you filter by. You can enter a default number of days for the filter in the procedure Work centerA work center is a part of the factory. It can be a single machine or a group of machines, a single workstation or a group of workstations. register. This will give you the opportunity to filter out manufacturing orders far ahead in time that you do not wish to see in the priority plan at the moment.

#### Simulation factor
A filter which takes the simulation factor into consideration. The value of the simulation factor in percent is loaded from the work center, but you can change the simulation factor temporarily in this field in order to see how it affects the priority planning. By activating the simulation factor setting, the remaining time on each operation is divided by the simulation factor. If the operation for example has a remaining time of 10 hours and the work center has a simulation factor of 80%, the new remaining time will be 10 ∕ 0,8 = 12,5 hours. If you change the simulation factor and leave the field, a calculation of New finish is made for each operation. However, no update is made, since this is only a simulation.
