## Posting of logs
In this procedure posting of the transactions that should be recorded via stock accounting and management accounting, is made. The posting can be made manually or according to a schedule. These transactions can for example be material reporting items and standard price changes. The procedure posts transactions from logs with the help of the posting methods registered in the Register posting method procedure. Transactions from the following logs can be posted via Stock accounting Stock accounting is a standard feature in Monitor ERP. It is used to continuously post all stock transactions in the system. This way the stock value in the Stock module matches the recorded value in the Accounting module. Changes in stock which are due to changed standard prices, direct stock reporting, arrivals and deliveries, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement.:
- Stock transaction log
- Price change log
These posting items automatically update the stock value in the general ledger. That is, the value in the Inventory value procedure is transferred to the general ledger.
If the option Management accounting Management accounting is an option in Monitor ERP. It is used as a complement to the standard function called Stock accounting. The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5. The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor. Calculation differences are posted and these can be followed up per product, per order, etc. This function also contains extended management of cost of goods sold. is used, then there is also support to post transactions from the following logs:
- Manufacturing order log
- Calculation differences
- Invoicing log
The Manufacturing order log and Calculation differences are used to update the WIP account (that is, manufacturing costs, subcontracting costs, and calculation differences).
The invoicing log is used to post COGS (Cost of goods sold), if COGS is not posted via customer invoice journals.
> When you start using Stock accounting or Management accounting, we recommend that you manually run the posting. This is done in the Log box. The first time you post, you need to enter a "Post from" date for each respective log.

#### Scheduling
The posting can be done manually or you can schedule it to run regular posting items. The posting is entered in the journals and can be printed in the procedure Print log journal. Approval of the journal (transfer to the accounting) can also be scheduled.
> Please note! To avoid overloading the server, we recommend that you do not run posting of logs more than necessary. This is especially important if the company has many transactions.
> You can have Posting of logs and Approve log journal in one sequence.

#### Invalid postings
In connection to the posting, some transactions might not be possible to post. When transactions cannot be posted, a message appears.
A list of these transactions can be printed in the Print log journal procedure, under the Warnings tab. Read more about these [warnings](../../../UserGuide/Using/ManagementAccounting/PrintLogJournal.htm#Fliken_Varningar).
