### Settings – Documents

#### Document variant according to:
By using the setting called Document variant according to: you can change the document variant for all documents in the Result box. You can then make exceptions, if any, to each separate document (row) in the box. The document variants are handled in the Document templates procedure.
For quotes, you can use a document variant per quote type. This is registered under the Quote tab in the Order types procedure. For customer orders you can use document variants per order type for order confirmations, invoices, delivery notes, and transport labels. You register this in the Order types procedure under the Customer order tab. The document variant can be entered per customer in the Customer register.
When registering quotes, customer orders, and invoices, as well as at delivery, the document variant will be applied according to the following priority:
1. The document variant specified for the customer in the Customer register.
2. The document variant specified on the order type in the Order types procedure, under the Quote tab or the Customer order tab.
3. The default document variant in the Document templates procedure.

#### Linked files
With this checkbox you decide if files linked to part and quote will be included in the printout. These must in that case be set to be printed automatically in the file link in the Files window.
