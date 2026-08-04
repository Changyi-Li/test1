### Settings
The different settings required in order to begin using ISO payments in Monitor ERP are outlined here.
In the Bank settings procedure in the Accounting module, you can active the bank/s used by your company.
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
> In the System settings procedure, under the Purchase tab, you can select the Default payment method for new supplier.
