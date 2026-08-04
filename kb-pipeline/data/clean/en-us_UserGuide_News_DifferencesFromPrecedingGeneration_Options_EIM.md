### Electronic Invoice Management (EIM)
In G5, EIM is an option in the same way as it is a supplement in G4.
General
- The floating license model with check of the number of simultaneous users in EIM has been removed from G5.
- All data concerning EIM, including images, is saved in the regular Monitor database.
- The recommended file type when scanning and handling invoices images is PDF. The file type TIFF is also handled but is automatically converted to PDF when scanning, which takes a bit longer.
- The function for annotations/stamps when viewing invoices, has been removed. Instead you write notes and messages regarding the invoice in a separate field next to the invoice in the viewing window. Predefined texts can be inserted. Function for chatting (send chart messages) with signers of the invoice in question.
- Adding/deleting/replacing invoice/attachment can be done in several places in the system. For example when registering and when authorizing invoice.
- When viewing an invoice in lists and reports, a document is always enclosed with the invoice. This document shows overall information about the invoice and its flow in a clear way (Invoice information).
- In the invoice viewing window it is possible to search for text in an invoice and to enter the page number of the invoice you wish to go directly to.
- By using a system setting you can activate authorization of invoices on row level. Via settings on accounts and dimensions you can determine who should authorize each posting row depending on the posting.
Authorization settings – EIM
Video: Authorization settings – EIM (Swedish)
- New procedure: Authorization settings – EIM where you configure settings for signers, authorization flows, scheduling (see below).
- Support for parallel authorization. This means that invoices which should be authorized by several persons does not have to be authorized in a specific order.
- It is possible to send the invoice to a signer group. A signer group consists of several signers where it is enough that one member of the group authorizes the invoice.
- More advanced settings for authorization limits, for example depending on supplier category.
- More advanced settings for user rights to show invoices in lists, etc. Can per user be determined dependent of supplier, supplier category, purchasing agent, supplier role, etc.
- "Absence from authorization of invoice" can be activated by the user (via the desktop backstage).
- Built-in function for scheduling of automatic forwarding of invoices in the flow. Also scheduling of sending e-mails regarding invoices to authorize.
- When using authorization limits you can activate the four eyes principle in order to ensure the invoice is always authorized by at least two people.
Scan supplier invoices
Video: Scan supplier invoices (Swedish)
- Here you register paths for inboxes for scanned invoices (PDF). These are used for Electronic invoice management (EIM).
- Here you also register paths for special XML inboxes with corresponding filing folders on the Monitor server. XML inboxes are used for e-invoices (that is, when the invoice arrives as an XML file). Please note that the filing folder must have a separate path, and it may not be located in a sub-folder of the regular XML path.
- Different types of attachments to the supplier invoices are also registered in the procedure. Attachment types are used to make it possible to link other documents to scanned invoices, such as delivery notes, purchase orders, travel claims, etc.
Register supplier invoice
- You do not have to select action when starting the procedure, this can be changed via a navigation panel in the procedure.
- It is possible to register an optional number of inboxes for scanning of paper invoices.
- An inbox for Monitor-to-Monitor is now built in to the procedure. No drag and drop technology is needed, neither for XML file nor for PDF file. Inbox for Monitor-to-Monitor can read both e-mail inbox and folders containing Monitor-to-Monitor files (XML and accompanying PDF files).
- When registering the invoice you can set it to status pending which means the invoice becomes registered without being sent for authorization. The function can for example be used when an order has not yet been arrival reported or when the invoice needs to be complemented with attachments and such, before it is sent for authorization.
- The action option Coding per user has been removed.
- Invoices which have been rejected during the authorization are found in a separate action folder in the Navigation panel.
- The ability to final record an invoice without it being sent for authorization can be determined via user rights.
- You can for example see which EIM status the invoice has in the flow, Sent for authorization, For final entry, etc.
- Now it is possible to add enclosures/attachments in connection with new registration of supplier invoices.
-   
If authorization at row level is applied, you can enter who should authorize expense invoices on each posting row. A central framework of rules and can also provide automation for such authorization depending on the posting.
Authorize supplier invoice
Video: Authorize supplier invoice (Swedish)
- You can link invoice to purchase order when it is sent for authorization (corresponds to preliminary linked in G4).
- Possible to access block for payment feature and enter comments (the general comment) on the invoice.
- Preceding signers' coding/posting items can be edited even though the row is already authorized. This feature is controlled via user rights.
- When you reject an invoice it is mandatory for you to enter a message regarding it.
- Automatic posting/Automatic allocation is generated when coding/posting when the invoice is sent for authorization (and when registering). This was previously not generated until the final coding of the invoice.
- Function to see the supplier's most recent invoices. This is shown in a new tab where you can both see the invoices as well as the coding/posting items. Coding/posting items can be copied to the invoice in question.
-   
If authorization at row level is applied, the system will automatically filter the rows that you should authorize.
Invoice overview – EIM
Video: Invoice overview – EIM (Swedish)
- In G4 this was called Search Supplier Invoice.
- This procedure contains a new report to load statistics of the authorization flow (handling times and number of invoices).
