## Price list – Sales
In this procedure you can load price lists for parts. You can for example print the lists in order to send them to a customer. The lists are based on part data, price lists, customer links, discount categories, and customer data. You cannot updates any information in this procedure.
If the system setting Manage future sales prices is set to Yes, then it is possible for you to see future price, future setup price, and future valid through date under the More info button (in the standard mode) in the list types Price list and Customer price. For the presentation Price list – Staggered prices, you can also see Future price (staggering) if the system setting mentioned above is activated.
List types

#### Price list
In this list you find information about the parts' price lists. The list is grouped by part number and can be presented based on price list or price list for staggered prices.

#### Customer price
In this list you find information about the parts' customer links. The list can be grouped by customer prices on part (with or without staggered prices) or grouped by customer prices on customer (with or without staggered prices).

#### Compare prices
In this list you can compare two prices with each other. You select the prices in the settings. When comparing, the difference between the prices is calculated in the company currency. Difference in percent is also shown.

#### Order simulated price
In this list you calculate the price corresponding to the price created at registration of customer order. The price can be loaded from price list or from customer link. The discount can be loaded from customer link for, customer's general discount, or customer's discount category. The list is printed for one customer at a time.

#### Order simulated price – External
This list is the same as the list described above, but it is adapted to be sent by e-mail to customer. That is why it is possible to select Customer's reference, E-mail (of the reference) and Our reference in the Settings section. The list is printed for one customer at a time. A text file (CSV file) is attached in e-mail sent from the procedure. This text file can be imported to the customer's system in the Price import procedure.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
