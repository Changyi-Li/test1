### The Loading tab
After calculating in the Loading or Simulation lists, this tab is shown containing all affected work centers. The loading is calculated taking the order quantity into consideration. This way, the number of setup time will be correct.
For subcontracts, only costs will be displayed. Setup costs and Unit costs are calculated in a similar way as for other operations, taking the order quantity into consideration. If you have selected to include SC mark-up, it will be added according to each part's own mark-up. If you have chosen to include transport cost, there will be as many freights as there are setup costs.

#### Setup time
The setup time you see in this column is calculated based on the number of setups x the setup time of the BOM and routing.

#### Unit time
The unit time you see in this column is calculated based on the number of parts x the unit time of the BOM and routing.

#### Total time
The total time is setup time + unit time.

#### Cost
The cost is calculated as the total time x the cost factors you chose under the Selection tab. This shows the annual cost for the part.

#### Man-hours
Man-hours are calculated based on the separate fields for staffing factor for setup and unit. Values from the operation in the BOM and routing are primarily used, and secondarily from the work center. Each operation's unit time is multiplied by the staffing factor for unit time, and the total for setup time is multiplied by the man-hours factor for the setup time. This is then added together to a total man-hour time.

#### Include
Mark the Include checkbox for the work centers where times and costs should be saved when you save in the procedure. In the simulation list type, this column is not available and you cannot save.
