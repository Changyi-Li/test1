## Review/Approve pro forma invoice
In this procedure you review, approve and print pro forma invoices Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees.. These functions are the same as in the Review/Approve invoice procedure. Please read the online help for the chapter concerning [Review/Approve invoice](../ReviewApproveInvoice/wReviewApproveInvoice.htm).
However, there is a difference in this procedure and that is that the pro forma invoices becomes created in connection with the approval. Pro forma Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees. can be created from:
- Pro forma – Customer order printed before delivery reporting will include the rows from the customer order, based on the remaining quantity on the rows.
- Pro forma – Invoice basis printed after delivery is based on the invoice basis created in connection with delivery reporting.
- Delivered stock orders (if the Warehouse option is installed).
When you approve pro forma invoices, each pro forma invoice will get a pro forma number. In the procedures Register customer order and Register invoice directly, you can see which pro forma number has been set, for the customer order and the invoice. For regular invoices the accounts receivable, journals, statistics, etc. then becomes updated. But for pro forma invoices which you approve in this procedure, only the pro forma invoice number will be saved. No update of, for example, statistics and journals will then be made.
Reprint pro forma invoice
When the pro forma is approved and printed, then it will be possible to reprint the pro forma via the Print invoice procedure.
Texts on the pro forma invoice
In the Customer register procedure you can configure if the pro forma invoice should display the amount excluding discounts. This is done under the Document settings button in that procedure.
To show weight and shipping information on the pro forma invoice, it is required that the setting Show shipping information is activated for that document in the Document settings procedure. The parts' shipping information and weight information is registered in the Part register. The part's shipping information can also be edited under the Shipping information button on order rows and invoice rows.
Cancel pro forma invoice
In the procedures Register customer order and Register invoice directly it is possible to cancel an existing pro forma invoice, for example when a new pro forma needs to be created because changes have been made on the order rows/invoice rows. The pro forma number on a canceled pro forma is kept on the new pro forma which you create here. A pro forma for a customer order can be canceled as long as the order does not have status 9 (Final delivery made). A pro forma for an invoice can be canceled as long as the invoice does not have status 8 (Approved).
List types

#### Pro forma from invoice basis
This information is based on the invoice basis. Invoice bases with the pro forma status Printed and bases from credit invoices will not be included in the list. If the pro forma from invoice basis is based on an invoicing plan, then the advance and in arrears rows are hidden.

#### Pro forma from customer order
This information is based on the order backlog. Orders with status 1–5 will be included in the list. For rows with status 5 it is the remaining quantity that will be displayed when printing the pro forma, since the remaining quantity belongs to the customer order.

#### Pro forma based on delivery (stock order)
This information is based on the delivery reporting of stock order for sales. Orders that have partial deliveries registered or where final delivery is made, will be included. The delivered quantity is shown on the printout.
This list type is available if you have the option Warehouse.
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
