### Settings – Selection
Result

#### Pre-select "Include"
This setting determines whether or not the “Include” box should be checked by default for all rows in the list/result.

#### Show included parts
With this setting you determine if included/incorporated parts should be shown on the invoice.

#### Warn in case of zero invoice
With this setting you decide if a warning should be shown when printing "zero invoices".
Please note! The performance regarding loading of the list can be reduced if the Warn in case of zero invoice setting is activated.
Printout

#### Invoice date
The invoice date in this field will by default be today's date, but it can be changed. This date will then be printed on the invoice documents. The invoice date determines the date on which the invoices will be recorded and registered in the statistics. The number of days which the payment terms state on the invoice basis, will also be counted from the invoice date.

#### Number of copies
Here you select the number of copies that should be printed. The default value here is 1. If more than 1 copy is printed it will say "COPY" on all documents following the first printout. This feature can be turned off with the setting Mark as copy for each document in the Document settings procedure.
The default number of copies is determined in the document settings.

#### Print to printer when e-mailing
With this setting you determine if a copy of the invoice should also be printed when sending invoices by e-mail. In the system settings you can make this setting activated by default. The printouts will be marked with E-mail in the header. This is done in order for you to know that the invoices should not be sent by regular mail (by post). They are only printouts for own use. Whether or not the printouts should be marked with the text “E-mail” is determined by the document settings.

#### Number of copies
Here you select the number of copies that should be printed to printer when e-mailing. This setting is only available if you have activated the setting described above.

#### Enter fixed due date
If a fixed due date should be used on the invoices, you can activate this setting and then select a date in the Due date field. This date will then be printed on the invoice document.
If a fixed due date is used, regular payment terms will not apply to the invoice bases. A fixed due date is not saved on the invoice basis. It applies only to the specific invoicing occasion. However, due date is saved in the accounts receivable ledger.
Fixed due date can be used e.g. when you are late with your invoicing and need to backdate the invoice date. In order to avoid too short a credit time for the customer, you can set a later due date so that it will be e.g. 30 days from today's date instead of 30 days from the invoice date. Another way to use the fixed due date might be when you have agreed with a customer that they will temporarily have a longer credit time for a specific invoice. Then you can enter a fixed due date when invoicing.
By default, a fixed due date is not entered on an invoice. Instead the due date of the invoice is calculated as the invoice date plus the invoice terms of the invoice. The system setting Consider holidays when calculating due date makes the calculation of due date also take holidays from the selected calendar into consideration. You select calendar in the system setting Calendar for calculation of due date.

#### Factoring export
With this setting you decide if a factoring file should be created and exported when you approve and request printout of an invoice. If the customer has the Factoring setting activated in the customer register, then the Factoring export will be checked by default. A plugin for factoring must also be installed. Read more about [Factoring](../../../UserGuide/Using/Factoring/Factoring.htm).

#### Approve without Print/Send
This setting becomes available if you mark the Factoring export checkbox (see above). This means that you can approve invoices directly without first having printed the invoice or sent it via e-mail. This can be applied if the factoring company handles the distribution of invoices to the customer, in order to avoid the invoice also being sent to the customer by your own company.

#### Linked files
With this checkbox you determine if files linked to the invoice basis or to a part on an invoice row, also will be printed. This might be files that are linked to External order text in the Comment/Files box under the Header tab. It might also be files linked to the comment in the [Comment/Files](../../../Stock/Parts/PartRegister/bCommentSales.htm) box under the Sales tab in the Part register procedure.
EDI

#### "No" by default for EDI export
This is only available in systems with the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. option. When this setting is activated it means the column for EDI export in the Result box by default will be set to No. This setting can be of use in order to avoid unintentional EDI export when you list the results, for example when you want to reprint a document.
