## Send dispatch advice
The Send dispatch advice procedure helps make the workflow more efficient and provides an easy handling of dispatch advice via EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system..
Regardless if the customer has been configured for simplified or complex dispatch advice, you can load a list and start EDI export of dispatch advice.
> Please note! Since the system identifies if an advice has been sent or not based on the EDI records in the print log, you should always enter a from-date in the selection field called Actual delivery date. If you do not enter a From date in this field, all existing records which have not yet been sent as EDI advice, will be included in the list.

#### What to keep in mind when using warehouses
The records included in the list depend on the warehouse or warehouses selected on the toolbar of the procedure.
- For records that have a pick list, the selection is based on the warehouse entered on the pick list.
- For records which do not have a pick list, the selection is based on the warehouse entered on the invoice basis.
> Please note! Records without a pick list can contain orders where the order rows have different warehouses, depending on how the customer order was registered and reported as delivered. The list result in this procedure does not take the warehouse on row level into consideration, only at invoice basis level.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
