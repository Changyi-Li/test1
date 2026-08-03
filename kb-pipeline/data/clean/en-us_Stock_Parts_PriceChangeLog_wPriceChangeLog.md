## Price change log
In this procedure you can load lists in order to see price changes for parts. Using this list you can:
- Study price changes over a certain period of time.
- Study price change for certain parts.
- See parts’ future prices (Future price).
This information displayed here is the same as the information found under the buttons Standard price log, Supplier price log, Customer price log, and Sales price log in the part register.

#### What to keep in mind when using FIFO price
All price changes due to, for example, supplier invoice price, supplier invoice expenses (freight, customs duty, etc.) or calculation of manufacturing cost (post-calculation on manufacturing order) are handled as a price adjustment and are logged. This adjustment affects reports such as stock value, WIP, invoicing log, post-calculation, etc. As a result, price according to supplier invoice will be used as of the date when the invoice was linked, when an arrival gets a new price, for example, due to supplier invoice link.
The stock and management accounting supports these price changes and updates the general ledger.
> Please note! Only the list type Standard price supports the option Warehouse.
List types

#### Standard price
In this list you see standard price changes grouped by part or date.

#### Supplier price
In this list you see supplier price changes grouped by part or date.

#### Customer price
In this list you see customer price changes grouped by part or date.

#### Sales price
In this list you see sales price changes grouped by part or date.

#### FIFO price
In this list you see the price changes which affect the FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price.
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
