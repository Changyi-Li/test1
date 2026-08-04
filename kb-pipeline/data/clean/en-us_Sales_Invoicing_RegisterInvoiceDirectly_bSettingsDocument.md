### Settings
In the Settings box under the Document tab, there are different document settings as seen below which you can modify before printing the invoice, if needed. The invoice basis must also be approved for invoicing so that the invoice has received an invoice number. If you do not need to print or e-mail the invoice directly, you can instead print it in the Print invoice procedure.

#### Document
Here you can select which document you want to view and print. There are two different documents: Delivery note, delivered and Invoice.

#### Document variant
If you want to print another document variant than the default variant, you can select it here. The document variants are handled in the Document templates procedure.
In that procedure you can for the document templates Delivery note, delivered and Invoice in the Sales module, add variants to be able to use for this printout.

#### Linked files
With this checkbox you determine if files linked to the invoice basis or to a part on an invoice row, also will be printed. This might be files that are linked to External order text in the Comment/Files box under the Header tab. It might also be files linked to the comment in the [Comment/Files](../../../Stock/Parts/PartRegister/bCommentSales.htm) box under the Sales tab in the Part register procedure.
Please note! The Linked files setting is deactivated for the invoice document if the invoice status is less than 9.

#### Invoice date
Today's date is entered by default as invoice date, but it can be changed. The date is printed the invoices. The number of days which the payment terms state on the invoice basis, will be counted from the invoice date. For delivery notes you instead enter the printout date.

#### Printout date
The date that is shown on the document as the date of the printout. Today's date is shown by default. By using the available calendar, you can select another date.

#### Number of copies
Here you select the number of copies that should be printed. The default value here is 1. If more than 1 copy is printed it will say "COPY" on all documents following the first printout. This feature can be turned off with the setting Mark as copy for each document in the Document settings procedure.
The default number of copies can be configured in the Document settings procedure.

#### Print to printer when e-mailing
With this setting you decide if a copy should be printed to printer, at the same time as when you print the invoice to an e-mail. This setting can be checked by default by using the system setting Print to printer when e-mailing invoices. These printouts will be marked with "E-mail" in the invoice header. This is done in order for you to know that the invoices should not be sent by regular mail (by post). They are only printout copies for own use. Whether or not the printouts will be marked with "E-mail" is determined by the document setting Mark copy to printer with "E-mail".

#### Number of copies
Here you select the number of copies that should be printed when you send the invoice by e-mail. This number is possible to enter only if the setting described above has been activated. The default number of copies is configured is configured with the system setting Default no. of copies.

#### Enter fixed due date
If a fixed due date should be used on the invoice, you can activate this setting and then select a date in the Due date field. This date will then be printed on the invoice document. Since a fixed due date is used, regular payment terms will not apply to the invoice basis. A fixed due date is not saved on the invoice basis. It applies only to the specific invoicing occasion. However, due date is saved in the accounts receivable ledger.

#### Mark as reprint
With this setting you determine if invoices with status 9 (Printed) should be marked with the text "Reprint" diagonally across the document (as a watermark).
