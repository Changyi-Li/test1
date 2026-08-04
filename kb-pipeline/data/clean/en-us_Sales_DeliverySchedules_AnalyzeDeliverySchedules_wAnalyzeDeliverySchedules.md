## Analyze delivery schedules – Sales
In this procedure you can analyze the "snapshot" which shows differences between the delivery schedules and the order backlog. That is, from when the delivery schedules were imported and transferred to customer orders or sales forecasts. You can also compare delivery schedules and see how the requirements differ between different schedules. The list type Delivery schedule Silf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands. parts lets you identify significant deviations when it comes to requirements.
With the list type Requirements – Summarized you can see how the requirements in the delivery schedules have looked and varied over time as well as between different delivery schedules, and with the help of the list Requirements – Detailed you can find reasons for the result of the transfers.
Using the list type called Delivery schedule parts, you can analyze warnings and errors which have occurred during the transfer of delivery schedules.

#### Logic for handling frozen periods when reconciling delivery schedules
The following order of priority is used when a frozen period is applied during delivery schedule reconciliation:
1. Customer link – the system first checks if a frozen period has been specified on the customer link. If a frozen period is specified, it will be used.
2. Part – if no frozen period is specified on the customer link, the system checks the setting on the part. If a frozen period is specified, it will be used.
3. Delivery schedule type – if neither the customer link nor the part has a value specified, the frozen period defined on the delivery schedule type, will be used.
List types

#### Requirements – Detailed
The list type Requirements – Detailed has three presentations:
- Standard – this presentation is by default grouped by Transferred when, Customer, and Part.
- Grouped by customer/part – this presentation is by default grouped by Customer and Part.
- Grouped by delivery schedule/customer/part – this presentation is by default grouped by Delivery schedule, Customer, and Part.
For the grouped presentations you can select to group by day, week, month, quarter, or year. That is, how long period of time the grouping should comprise.

#### Requirements – Summarized
The list type Requirements – Summarized is used to compare and see how delivery schedules vary. In the list you can choose how you want to group the requirements in the delivery schedule, as well as whether you want to see the actual requirement or the difference in requirements compared to the previous schedule. You can compare quantity and amount.
The list type has two presentations:
- Grouped by customer/part – the requirements for the delivery schedules are summarized and grouped by customer and part.
- Grouped by customer – the requirements for the delivery schedules are summarized and grouped by customer.

#### Delivery schedule parts
The list type Delivery schedule parts with the Deviations presentation gives you a heads-up regarding deviation alarm signals or warnings. The presentation called Transfer warnings and errors shows warnings and errors, if any, if you selected by Errors and Warnings.

#### Deviations – Detailed
You use the Deviations – Detailed list to show details about the deviations discovered during the deviation check. To be able to find and get an overview of the deviations, you must first have linked a deviation model to the delivery schedule and performed the deviation check.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
