## Stock value
In this procedure you can create lists showing the value of the parts in stock.
You can select which balance you want to use in the valuation of parts in stock. The following balances are available:
- Current balance Current balance is the part balance at this moment on the locations..
- Last stock count date
- Optional stock count date
- Different types of historical balances (these are based on actual date or log date).
You can also decide if parts without balance should be included. You can enter a minimum value per unit for the parts you want to include in the list. Different price alternatives for purchased and manufactured parts are then selected for the valuation, e.g. current standard price or a historical price.
> FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. always links withdrawals to arrivals based on log date and not the actual date. This means that the correct stock value cannot be guaranteed based on historical actual date when the price alternative is FIFO.
There are no update options in the procedure.
List types

#### Standard
This list shows detailed information about the stock value for the selected parts. The list can be grouped by part code or product group.

#### Detailed with location
This list shows detailed information about the stock value for the selected parts per location. The list is grouped by location.

#### Detailed with traceability
This list shows the same information as Detailed with location, but also shows information about traceability.

#### Total
This list shows total information about the stock value for the selected parts. The balances and values in the list are also displayed as a bar chart. It can be presented as total by part, by part code, or by product group.

#### Total by date
This list shows total information about the stock value for the selected parts. The purpose is to see how the stock value has changed over time. The balances and values in the list are also displayed as a bar chart. This list is shown as total by date, based on the grouping of dates you select in the next field.

#### Configured parts
This list type is available if the option Product configurator is installed in your system. This list is grouped by part number and displays stock value based on current balances of the selected and configured parts.

#### Stock value change/Reconciliation
In this list type you reconcile the stock value with the booked balance on stock accounts in the accounting.

#### Withdrawn reusable tools
This list type is available if you have installed the Tools & Maintenance option. This list is grouped by part code and displays information about the stock value of the selected tools which are currently withdrawn.

#### Project
This list is based on records reported for a project in the stock transaction log. You can check the stock transaction log records which have been reported for projects and which are the bases for the balance in the list in the stock transaction log.

#### Rejected in receiving inspection
The list shows the parts that have been rejected in the receiving inspection and have not yet been returned to the supplier.
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
