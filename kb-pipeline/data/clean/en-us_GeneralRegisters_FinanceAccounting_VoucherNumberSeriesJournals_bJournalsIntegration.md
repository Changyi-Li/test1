### Journals/Integration
In this box you see a fixed list of all journals that can be integrated from different ledgers, management accounting, project revenue calculation journals, and registers (e.g., the fixed assets register) to the general ledger. Data in the table is registered for all accounting years.

#### Type
Here you will see the type of series, for example customer invoices and incoming payments. This field cannot be modified.

#### Next journal number
Here the next journal number is entered/displayed. The number continues being counted up without taking the accounting years into consideration, as opposed to the voucher numbers. Also, this number should not be changed in connection to switching the year. This field cannot be left empty.

#### Integration
Here you select if and how integration to the accounting should be made. There are different selections depending on the journal type.
- No – Means that no accounting will be transferred to the accounting module when the journal is reset. If for example the journals are recorded manually or if the accounting module is not used.
- Direct per payment day – This can be selected for the system's payment journals. This setting means that the journals do not have to be printed/approved. Journals for payments will be transferred to the accounting automatically when the payments are saved. When using this alternative, a separate voucher number/journal number will be created per payment day where the voucher number is set based on the following/next number in the voucher number series.
- Direct per invoice – This can be selected for the system's invoice journals. This setting means that the journals do not have to be printed/approved. The invoices will be transferred to the accounting automatically when they are approved/preliminary recorded/final recorded. When using this alternative, a separate voucher number will be created per invoice where the voucher number is set based on the number on the ledger record, that is, the same as the invoice number or consecutive number.
- Via journal per invoice – This can be selected for the system's invoice journals. This setting means that you have to print/approve the journals in order for them to be transferred to the accounting. When using this alternative, a separate voucher number will be created per invoice where the voucher number is set based on the number on the ledger record, that is, the same as the invoice number or consecutive number.
- Via journal per reporting – This can be selected for direct stock reporting in the system. This setting means that you have to print/approve the journals in order for them to be transferred to the accounting. The posting of each reporting creates a separate voucher in the accounting. Next voucher number in the series will be set as voucher number. Information in the voucher will be saved in order to create traceability to the accounting.
- Via journal – Total – This can be selected for the system's invoice journals, journals for canceled invoices, and forjournals for direct stock reporting. This setting means that you have to print/approve the journals in order for them to be transferred to the accounting. When using this alternative, a common voucher number/journal number will be created for all records in the journal. A separate journal/voucher will be created per month where the voucher number is set based on the following/next number in the voucher number series.
-   
Via journal – Total per payment day – This can be selected for the system's payment journals. This setting means that you have to print the journals in order for them to be transferred to the accounting. When using this alternative, a separate voucher number/journal number will be created per payment day where the voucher number is set based on the following/next number in the voucher number series.
-   
Direct – Object number is saved on all accounts in the voucher – This can be selected for the fixed assets journal. This setting means that the journals do not have to be printed/approved. Recordings of depreciations/sales/retirements/activations are automatically transferred to the accounting when they are executed. On each row in the voucher, you will see to which object number the posting refers in the Fixed assets column. This enables full traceability in the general ledger for all transactions in the fixed assets register.
-   
Direct – Object number is saved on balance accounts in the voucher – This can be selected for the fixed assets journal. This setting means that the journals do not have to be printed/approved. Recordings of depreciations/sales/retirements/activations are automatically transferred to the accounting when they are executed. On each balance account in the voucher, you will see to which object number the posting refers in the Fixed assets column.
-   
Via journal – Object number is saved on all accounts in the voucher – This can be selected for the fixed assets journal. This setting means that you have to print/approve the journals in order for them to be transferred to the accounting. On each row in the voucher, you will see to which object number the posting refers in the Fixed assets column. This enables full traceability in the general ledger for all transactions in the fixed assets register.
-   
Via journal – Object number is saved on all balance accounts in the voucher – This can be selected for the fixed assets journal. This setting means that you have to print/approve the journals in order for them to be transferred to the accounting. On each row in the voucher, you will see to which object number the posting refers in the Fixed assets column.

#### Linked to voucher number series
In this field you link the journal type in question to a voucher number series.

#### Link
The function can only be activated if the system setting Register incoming and outgoing payments in the same procedure/journal is activated. Here you determine which voucher number series you want to use with different types of payments.

#### Detailed posting
Here you determine if detailed posting should be used. Detailed posting means that the invoice number on customer invoices and consecutive number on supplier invoices are saved for each posting row. The columns Invoice number and Consecutive number are found under More info ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) in the Register vouchers procedure. During incoming and outgoing payments, the invoice number and consecutive number are saved to each posting row. This is for example used to handle cash discount correctly in the EC sales list. Detailed posting is possible for the following journal types: Customer invoices, Incoming payments, Supplier invoices, Outgoing payments, Preliminary recorded supplier invoices, Canceled supplier invoices, Canceled customer invoices, and Canceled preliminary recorded invoices.
Detailed posting is always used for the integrations: Direct per invoice and Via journal per invoice. For the integrations Via journal – Total, Direct per payment day and Via journal – Total per payment day you can choose if you want to use detailed posting.

#### Preliminary vouchers
Here you determine it the vouchers should be preliminary saved to the accounting. The preliminary vouchers have a separate status. It is also possible to adjust these before they are locked. Preliminary recorded vouchers are not included in reports in the accounting (account balances). Preliminary vouchers can be modified. You can also set them as recorded in the list type Preliminary vouchers in the Voucher list procedure or in the Register vouchers procedure.

#### Voucher text
This determines which voucher text should be displayed on incoming and outgoing payments.
