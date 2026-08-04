## Print customer order
In this procedure you can review and print customer orders for new sales, modified customer orders and stock orders* for sales. You print order confirmations for one or multiple customer orders at a time. You can also print delivery notes if you need to print them prior to the delivery of customer orders.
> * Stock orders are available if you have installed the option Warehouse.
You create customer orders in the procedures Register customer order and Register stock order – Sales. When registering orders you can also in those procedure review and print the order confirmation and delivery note for the customer order you have registered.
The selected list type determines whether you can print order confirmations or delivery notes in this procedure. The customer orders that you load after selection are displayed in the Result box. In the Result box you click on the row for the document that you want to preview and then you select which documents to print.
When you approve a printout of order confirmations, the status of the customer orders in question will be changed to 2 (Printed), if they had status 1 (Registered) before. When printing delivery notes the status of the customer orders in question, will not be changed.
> You can automate the running of this procedure with the Agent option. Read more about [The Agent](../../../UserGuide/Options/Agent.htm) can help make your processes more efficient.
> You can select by Status in order to print orders with different status. If you select status 2 (Printed), you can reprint the orders.
Reprint fully delivered customer order
When reprinting a delivery note for a delivered customer order you have to select by status 9 (Final delivery made), under the Selection tab. Only status 1 is selected by default. Under the Documents tab you see the remaining quantity 0 for the rows that have been delivered.
When reprinting an order confirmation for a delivered customer order you have to select by status 9 (Final delivery made), under the Selection tab. Only status 1 is selected by default. You must also select Ordered quantity to be able to show the rows on customer orders. There is not support to show remaining quantity.
List types

#### Order confirmation
This list type loads order confirmations for printout. When you have printed order confirmations, the status of the orders will be changed to 2 Printed.

#### Delivery note
This list type loads delivery notes for printout. When you printed delivery notes, the status of the orders will be changed to 4 Picking in progress. If the order has status 5 Partial delivery made or higher, the status of the order will not be changed.

#### Modified order confirmation
This list type loads changed order confirmations for printout. Here you can print order confirmations for the orders where a new order row has been added, or where quantity, price, discount, or delivery date, has been modified after the printout. A modified order confirmation is a separate document where the modifications are displayed in red text. The text MODIFIED ORDER is also shown as a watermark on the document, below the order rows. If this text should be shown or not is determined by a document setting found in the Document settings procedure. Rows that have been modified will also be marked with an asterisk (*).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
