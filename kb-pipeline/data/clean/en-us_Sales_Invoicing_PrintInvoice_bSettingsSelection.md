### Settings – Selection
Result

#### Reprint
With this checkbox you determine if only invoices which have already been printed should be loaded. If you do not check the box, only invoices that are approved but not printed, will be loaded. When reprinting an invoice, the invoice address can be loaded from the current invoice address in the customer register instead of from the invoice. This can be useful if the customer requests an new invoice and if their invoice address is changed. To do this you need to do the reprint by using the Document template. You also have to configure the document setting called "Reprint via document template – Load invoice address from" to the Customer register option in the Document settings procedure.

#### Mark as reprint
This setting is only available if you have activated the setting described above. It determines if the documents you reprint should be marked with that text.

#### Pre-select "Include"
This setting determines whether or not the “Include” box should be checked by default for all rows in the list/result.
Printout

#### Number of copies
Here you select the number of copies that should be printed. The default value here is 1. If more than 1 copy is printed it will say "COPY" on all documents following the first printout. This feature can be turned off with the setting Mark as copy in the Document settings procedure.

#### Print to printer when e-mailing
With this setting you determine if a copy of the invoice should also be printed when sending invoices by e-mail. In the system settings you can make this setting activated by default. The printouts will be marked with E-mail in the invoice header. This is done in order for you to know that the invoices should not be sent by regular mail (by post). They are only printouts for own use. Whether or not the printouts should be marked with the text “E-mail” is determined by the document settings.

#### Number of copies
Here you select the number of copies that should be printed to printer when e-mailing. This setting is only available if you have activated the setting described above. The number 1 is entered by default, but this can be changed in the system settings.

#### Factoring export
With this setting you decide if a factoring file should be created and exported when you approve and request printout of an invoice. If the customer has the Factoring setting activated in the customer register, then the Factoring export will be checked by default. Read more about [Factoring](../../../UserGuide/Using/Factoring/Factoring.htm).

#### Approve without Print/Send
This setting becomes available if you mark the Factoring export checkbox (see above). This means that you can approve invoices directly without first having printed the invoice or sent it via e-mail. This can be applied if the factoring company handles the distribution of invoices to the customer, in order to avoid the invoice also being sent to the customer by your own company.

#### Linked files
With this checkbox you determine if files linked to the invoice basis or to a part on an invoice row, also will be printed. This might be files that are linked to External order text in the Comment/Files box under the Header tab. It might also be files linked to the comment in the [Comment/Files](../../../Stock/Parts/PartRegister/bCommentSales.htm) box under the Sales tab in the Part register procedure.

#### Printing method
Here you decide which printing method should be used for the invoice. Select among the following options: According to invoice, E-mail, and Printer. That is, of the document should be printed on a printer, attached as a PDF in an e-mail message, or print according to the invoice’s default method.

#### Document template
Here you can choose which document variant and which language should be used when reprinting an invoice. This is useful if you, for example, want to print a copy of the invoice in a different language or with a different layout of the reprint than the original. You create document variants in the Document templates procedure.
EDI

#### "No" by default for EDI export
This is only available in systems with the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. option. When this setting is activated it means the column for EDI export in the Result box by default will be set to No. This setting can be of use in order to avoid unintentional EDI export when you list the results, for example when you want to reprint a document.
