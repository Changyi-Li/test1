### Work centers

#### Loading types
Here you can choose the type of loading that you want to display in the chart and the list. The alternatives Capacity and Actual orders are selected by default. It is possible to select more than one alternative in the list. The available alternatives are:
- Capacity – This option displays the total capacity of the selected work centers as a line in the chart.
- Actual orders – This option displays the loading created by registered manufacturing orders.
- Suggestions – This option displays the loading based on manufacturing order suggestions created in the net requirement calculation.

#### Only overloaded work centers
This setting is not activated by default. If you activate this setting, only overloaded work centers will be shown in the chart/list. Depending on which Time scale you have selected, you will therefore only see the work centers that are overloaded during a particular month, week, or day.

#### Include work centers without loading
This setting is not activated by default. By activating this setting, the work centers that do not have any loading will also be displayed in the chart/list. When the setting is not activated, you will only see the work centers with loading.

#### Only work centers included in CDT
This setting is not checked by default. By activating this setting, it will function as a filter which only will display the work centers that are included in the CDTCDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. (Check delivery times).
The purpose is to only include work centers that have the setting Included in CDT activated, that is, only the work centers that have a very strict capacity that cannot be changed. From a loading perspective, these are the work centers of special interest, since overloading in these work centers is particularly problematic.

#### Include blocked work centers
This setting is not checked by default. By activating this setting, it will work as a filter which only show blocked work centers.
