## Price adjustment
In this procedure you can modify and adjust prices for parts. You can manage all prices that are possible to update, e.g. purchase and sales prices. The statistical prices, such as the last (most recent) purchase price and average purchase price, cannot be changed. The list you can update is based on the part register and its prices. In the selection and with the settings you configure, for the respective list type, which parts to make adjustments for and how. When you have configured the settings, you load the data and the parts are shown under the List tab. In the list, you can then adjust the prices for the selected parts.
> It is important to understand what the different prices on parts mean and for what they are used. Read more about this in the chapter called [Explanation of part prices](../PartPrices.htm).
List types

#### Change price
This list type is used to change a certain price for a part, supplier, or customer.

#### Change staggered price – Price list, Customer, Supplier
There are three lists for changing staggered prices. The lists are sorted by price list, customer, and supplier. In these lists you can create, change, and delete staggered prices.

#### Copy price
This list type is used to change a price for a part by using another of the part's prices as a basis.

#### Change price on stock increases – FIFO
This list type is used to change price on transactions which increase the stock value but which are missing a basis for valuation. Such transactions can be, for example, stock count, case/posterior rejection, material withdrawal for manufacturing order (negative reporting), direct stock reporting, and balance import. The arrivals in the list are loaded from transactions in the stock transaction log.
> Select by the requested transaction type to adjust one transaction type at a time.

#### Adjust existing FIFO price
This list type is used to change the price of existing FIFO FIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. prices.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
