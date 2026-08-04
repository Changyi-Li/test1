### Result
After having loaded the list you will here see the order confirmations or delivery notes that can be printed for the customer orders selected under the Selection tab. You select which rows to include in the printout.
When the printouts are made, you can by activating the check box Approve select the order printouts that you wish to approve with the button Approve ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png). You can cancel by using the button Cancel ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_cancel.png) and then you can make new printouts. If you approve the printout, that record will be removed from the regular selection. But it is still possible to reprint.
When you have printed order confirmations, the status of the orders will be changed to 2 Printed. When you have printed delivery notes, the status of the orders will be changed to 4 Picking in progress. If the order has status 5 Partial delivery made or higher, the status of the order will not be changed.

#### Include
In this column you determine if the order should be included in the printout.

#### Status
Here you can see the status of the order.

#### Preliminary
Here you can see if the order is preliminary.

#### Printing method
You can choose if the printout should be made to a printer or via e-mail.

#### Document variant – Customer order
Here you see the document variant for the customer order and it is possible to change variant for a specific customer order.

#### Document variant – Stock order
If you have the Warehouse option in your system, you can see the document variant for the stock order and it is also possible to change variant for a specific stock order.

#### EDI export
If the customer is connected to EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system., it is in this column set by default that the order confirmation should be exported and sent via EDI, but it is possible to change for orders in the list. There is also an option in this field to export the order confirmation via EDI plus print/e-mail (based on the printing method in the previous field).
An order can also be excluded from EDI via a setting on the order in the Register customer order procedure. In that case, the order confirmation will not be exported and you cannot choose anything in this field.

#### Files
A button is shown here if there are any linked files. In the window opened by the button, you can preview all files which will be included when printing.

#### Approve
This column is shown after you have printed/sent the order. Printed orders are marked by default for approval. The status will be changed from 1 to 2 on orders that you approve.
