### FAQ – Payments

#### Outgoing payments
How do I register outgoing payments?
You can register outgoing payments in the Outgoing payments procedure.
You can register outgoing payments in different ways in this procedure. One way is to order for payment directly via the Payment suggestion list, where the selected supplier invoices are directly transferred to a payment file that will be sent to the bank. Or you can transfer the selected invoices in the list to the transaction list to be approved/printed in the Print transaction list procedure. If you approve the invoices in the transaction list, they will be transferred to the payment file. Another way is to start by transferring all selected invoices from the Payment suggestion list to the Pay via bank (order) tab or adding them one by one to the tab, and then transferring them to a payment file. These methods mentioned apply for outgoing payments where electronic payment method is used. You can also register outgoing payments for supplier invoices where manual payment method is used in the Payment suggestion list. Then you start by selecting the invoices and transferring them to the Pay manually tab or you can add them one at a time to that tab.
You can read more about [Outgoing payments](../../../Purchase/AccountsPayable/OutgoingPayments/wOutgoingPayments.htm) here.
How do I cancel an outgoing payment?
You can cancel or undo outgoing payments that have been made. You may need to cancel payments, if you for example, by mistake ordered invoices to be paid. Such adjustments should only be made before the payment file is sent to the bank. It is possible to cancel individual payments as well as entire outgoing payment journals, transaction lists, etc. In order to cancel outgoing payments, select the list type Cancel outgoing payments.
You can read more about how to [Cancel outgoing payments](../../../Purchase/AccountsPayable/OutgoingPayments/tListCancelOutgoingPayments.htm) here.
I get an error message when I create a payment file (ISO), why?
With ISO payments this may be for a number of reasons:
-   
There is no recipient account for one or more invoices.
-   
A credit invoice doesn't have the same payment date as a debit invoice to the same supplier.
-   
A credit invoice and a debit invoice cancel each other out so the total amount becomes zero or negative.
-   
There are more than four invoices per supplier and payment date, and at least one of them is a credit invoice.
Here you can read more about what is good to bear in mind when using [ISO outgoing payments](../../Using/ISOSetup/AboutISOPayments.htm).
What happens to payments when a payment suggestion is canceled?
If a payment suggestion is canceled, the payments can be found in the Print a transaction list procedure.
New records are added to this procedure when electronic payments are executed in the Outgoing payments procedure. When the transaction list has been approved and a file has been created with a successful result, then the records will be removed from the procedure.
You can read more about [Print transaction list](../../../Purchase/AccountsPayable/PrintTransactionList/wPrintTransactionList.htm) here.
How do I get started with ISO payments?
The different settings required in order to begin using ISO payments in Monitor ERP are outlined here.
In the Bank settings procedure in General registers you active the bank/s used by your company.
Activate bank/banks
1. Open the Bank activation tab.
2. By default you will here see the country for which the system is intended (determined by the country package). However, you can select a different country.
3.   
Here you select which bank to use. This decides which active file formats will be displayed in the box to the right.
4.   
Under Active file formats you can see the payment formats that are activated in the system. The list shows the total of all formats that are active in the system, not only on the row where you are to the right (that is, every one you have checked as active). When you have activated a bank, you’ll find that bank's formats available to select among the electronic payment methods under the Payment method tab, and in the Settings for export/import procedure.
The settings for export and import of files are configured under Settings for export/import in General registers.
Settings for export
1. Open the Export tab.
2. Select Payment file under Export type.
3. Select a payment format.
4. Enter the path to the payment file under Path.
5. Under File name, the name of the file is pre-filled as a template with variables. The %T variable inserts the number of the transaction list into the file name. The %x variable inserts today's date into the file name. When you hover over the field, a tooltip appears with an explanation of the variables.
6. Enter a Signer ID. You can get this from your bank.
7. Enter an Agreement number. You can get this from your bank.
8. Merge payments is selected by default, except for Danske Bank (Sweden) and Nordea (Finland). This controls whether payments are merged. If multiple invoices are sent at the same time to the same supplier, they can be merged into one overall total in the payment file. For Danske Bank (Sweden) and Nordea (Finland), you can instead select Use batch payment.
9. Save.
You can configure the payment method in the Bank settings procedure under the Payment method tab.
Settings for import
1. Open the Import tab.
2. Select Confirmation outgoing payments under import type.
3. You can enter the path to the directory where the payment files are to be saved under Path.
4. Save.
Bank settings
1. Open the Payment method tab.
2. Add the code ISO in the table, and enter a name.
3. Select Electronic outgoing payment under Payment type.
4. Check the box under Active.
5. In the Bank information box, enter the Payment format and Confirmation format.
6. Select Transaction list ISO (standard) in the Transaction list box.
7. Save.
Depending on the bank you use, bank accounts are registered in slightly different ways in the Bank accounts procedure. Instructions for banks with more specific settings can be found below.
Bank settings – Swedbank
Enter the clearing and account number in succession, with no spaces or punctuation marks, in the Sender account BBAN field.
If the clearing number begins with 8, you must enter 15 digits.
If the clearing number plus account number consists of fewer than 15 characters, enter zeros between the clearing number and account number.
If the clearing number begins with 7, you must enter 11 digits.
All payments sent to Swedbank can be issued in a single file, although it is recommended to divide EUR and other currencies into separate files.
Bank settings – Nordea
Since Nordea uses currency pockets, you must enter links to bank accounts under the Payment method tab. This is done in the Link to bank account/bookkeeping account box.
Supplier register
Make sure the correct payment method has been entered for your suppliers in the Outgoing payments box in the Supplier register. If required, click the Export settings button to make exceptions for a specific supplier.
You can batch update the payment method for suppliers by selecting Outgoing payments under Presentations in the Supplier list procedure. Use Find & replace to update records quickly and easily.
Here you can read more about what is good to bear in mind when using [ISO payments](../../Using/ISOSetup/AboutISOPayments.htm).

#### Incoming payments
How do I register incoming payments manually?
1. Start by entering Payment date and Payment method in the Settings box.
2. Continue by filling in all other information in the box or skip the following fields by using the Tab key. Tab until the cursor is placed on the top row in the table where payments are registered in the Incoming payments box.
3. Add a new row by using the shortcut key F5 or + (the plus sign) on the numerical keyboard and select/enter an invoice number. If the incoming payment is an on account payment, leave the invoice number field empty and instead you enter the customer number for the customer who made the payment.
4. Check the row and adjust, if needed, the suggested values for the payment.
5. Add rows for the incoming payments that have been made.
6. When you have entered all the incoming payments you wish to register, click the Save button or the Save and print journal button. In the latter case, the Print incoming payment journal procedure is automatically opened, with the correct journal loaded. At the same time, the procedure is prepared for the next batch of incoming payments to register by emptying all the fields and moving the focus back to the Payment date field in the Settings box.
For each incoming payment, you can see how the posting is created in real time in the Posting box. The Total field at the bottom is updated continuously.
How do I cancel an incoming payment?
You cancel incoming payments in the Cancel incoming payments list in the Incoming payments procedure.
In this column you check the invoices for which you wish to cancel incoming payments. The cancellation is executed for the checked invoices when you save. A box will then appear asking you to confirm that you wish to save the cancellation. When canceling payments, the remaining amount of the invoices will be reset. Furthermore, a posting will be created that reverses the posting of the payment. The canceled payment records remain in the system but with status Canceled. You can print canceled payments in the Accounts receivable list procedure, in the list type Payments.
You can read more about [canceling an incoming payment](../../../Sales/AccountsReceivable/IncomingPayments/wIncomingPayments.htm) here.
How do I offset incoming payments against another?
It is also possible to pay invoices by offsetting one invoice against another. An invoice with a large amount can e.g. be set-off against a number of debit invoices to the same customer. When you make such a set-off, all the affected invoices will become registered as paid.
You can offset debit invoices against credit invoices manually under the Set-off tab in the Incoming payments procedure.
You can read more about [how to set-off](../../../Sales/AccountsReceivable/IncomingPayments/vSetOff.htm) here.
How do I cancel set-offs?
To cancel set-offs, select the list type Cancel set-offs in the Incoming payments procedure.
The set-offs you have selected are shown in the upper table. In the table below, you see the payment records against which the selected invoice has been set-off. For these payment records, the Cancel checkbox will automatically be checked when you have marked the invoice for cancellation. When you save, the entire set-off is canceled.
When the checkbox Cancel is checked, the voucher date becomes active and the same date as the payment date of the invoice is suggested, but it is possible to change to a different voucher date.
How do I register on account payments?
In the Incoming payments procedure you are able to manually register on account payments.
That is, when the customer makes an incoming payment that refers to payment of something that does not exist in the accounts receivable ledger, e.g. an advance payment or an overpayment. An incoming payment like that creates a new accounts receivable entry of type "On accountOn account is a partial payment (advance payment) which you have made to a supplier or received from a customer." and will then exist as a balance in that particular customer's favor in the the accounts receivable ledger. You add on account payments under the Pay manually tab by leaving the field Invoice number empty.

#### Miscellaneous
What is a Cash book in Monitor ERP?
Cash book function is mainly intended for countries in Eastern Europe where there are certain rules regarding the handling of liquid funds and cash in the accounting. In the cash book you register cash withdrawals and deposits. These could include transactions relating to customers, suppliers, employees or banks, etc.
The following is a short summary of the functions included in the cash book management:
-   
The system setting Use cash book functionality must be activated. To activate the function you must first configure the system setting Register incoming and outgoing payments in the same procedure/journal.
-   
You create a payment method for the cash book in the Bank settings procedure under the Payment method tab. There you also enter in which voucher number series the transactions should be recorded.
-   
In the Manage bank transactions procedure you find the Cash reports tab where you register cash reports with start and end date for the report. Here you can also print cash reports which summarizes the transactions become registered in the cash book.
-   
You register transactions in the cash book in the Manage bank transactions procedure, using the payment method linked to the cash book.
-   
The Cash receipt document, which you can print for each transaction you register in the cash book.
-   
In cases where supplier invoices have been paid in cash, you can register the payment of the invoice at the same time as the invoice is final recorded in the Register supplier invoice procedure. This payment will be automatically registered in the cash book.
Before you start using Cash book in Monitor ERP, you are required to configure some settings in the system.
You can read more about [settings for the cash book](../../Using/CashBook/CashBook.htm) here.
How do Cash discounts work?
[Here you can read more about cash discounts](../../Training.htm#Kassarabatt__).
