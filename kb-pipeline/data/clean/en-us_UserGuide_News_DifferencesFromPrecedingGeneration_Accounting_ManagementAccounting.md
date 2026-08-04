### Stock accounting and Management accounting
Stock accountingStock accounting is a standard feature in Monitor ERP. It is used to continuously post all stock transactions in the system. This way the stock value in the Stock module matches the recorded value in the Accounting module. Changes in stock which are due to changed standard prices, direct stock reporting, arrivals and deliveries, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement. is a standard feature in Monitor G5. It is used to continuously post all stock transactions in the system. This way, the stock value in the Stock module matches the recorded value in the Accounting module. Changes in stock which are due to changed standard prices, direct stock reporting, arrivals and deliveries, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement.
Management accountingManagement accounting is an option in Monitor ERP. It is used as a complement to the standard function called Stock accounting. The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5. The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor. Calculation differences are posted and these can be followed up per product, per order, etc. This function also contains extended management of cost of goods sold. is an option in G5 used to complement the stock accounting. Here all transactions for manufacturing orders (WIP value) in the system are continuously posted. These postings concern processing, subcontracting, and calculation differences. Also the invoicing log can be posted via management accounting. If you have installed the option Management accounting, more functionality will be added for posting of additional transactions in the procedures Register posting method, Posting method list, Posting of logs, Print log journal, and Search management accounting.

#### Register posting method
- Posting methodsPosting method is used to register how different types of transactions are posted to the correct accounts in the Stock or Management accounting. can be created automatically via a guide.
- There is a control function to check that the posting methods are correctly registered for example if duplicates of posting methods are allowed.
- The posting is based on the transaction type instead of the procedure.
- Heading has been removed.
- It is possible to rename posting methods.
- You can copy posting methods to Clipboard.
- You can assign a number series for posting methods.
- Price alternatives for posting have been separated for purchased and manufactured part.
- Improved support to post calculation differences divided per calculation parts (concerns the option Management accounting).
- Support to post a planned cost before the supplier invoice is linked, when reported subcontracting cost is recorded (concerns the option Management accounting).
- When using "Other terms", you don't have to create posting methods to cover all intervals of the data you have configured terms for. Posting methods that don't have terms will take care of the transactions not covered by the entered terms.
- Posting on order number does not have to be entered, this is determined by chart of accounts settings.
- Posting on specification can be entered to get a more detailed information in the general ledger.
- The setting Code zero records is now called Post records without values and has been moved to a system setting.
- There are two new price alternatives for purchased parts for posting of stock transaction log and invoicing log. These price alternatives handles posting of standard price separated per calculation section for purchased parts.

#### Posting of logs
- Posting and approving transactions for the general ledger can take place automatically via the built-in scheduling function in the procedure. No separate Agent function is required. Posting and approving transactions for the general ledger can be scheduled on fixed times or on a certain interval.
- A notification can be sent automatically to selected users when the system finds transactions which cannot be posted.
- It is possible to post a selection of manufacturing orders. Used in connection with start up of Management accounting.

#### Print log journal
- Reprinting of journals is a built-in feature in the same procedure as the regular journal printing.
- It is possible to adjust certain information in the coding/posting prior to approval.
- You can go to log records, parts, and posting methods, by clicking links in the journal document.
- A check is made at an earlier stage than in G4, to see that all coding/posting items are OK before the journal can be approved.
- Makes sure that the period is open at an earlier stage than what was done in G4.
- The system automatically creates separate journals for the records belonging to different accounting periods.
- The system shows a suggestion of a posting method to post the record in connection with transactions which have not been possible to post.
- The heading has been removed and the records are instead shown in chronological order with information about transaction type. All posting items belonging to one and the same record are displayed together instead of scattered under the different headings.

#### Search stock accounting/Search management accounting
- It is possible to see posting items for approved and not approved journals in the same list.
- You can go to different procedures from the records in the list.
- Total lists also show a column regarding difference between debit and credit.

#### New system settings for Stock and Management accounting
- Post records without values.
- Calculation for stock transactions.
- Handle product groups as numeric fields during posting of logs.

#### Other differences (in Stock accounting and Management accounting)
- Transactions are now recorded on the actual date instead of on the log date.
- The posting method is saved to each voucher row in the accounting to supply information about the origin of the posting.
- In the Print accounting report procedure you can link from an amount in the general ledger view to the Search stock accounting/Search management accounting to see the transactions behind the recorded amount.
- It is possible to reconcile the stock value with the booked stock value by using the list type Reconciliation in the Stock value procedure.
- If the option Management accounting is installed, the list type Reconciliation is available in the WIP value procedure. This list is used to reconcile the WIP value with the accounting. In this list you see the opening and closing WIP value of the selected period, as well as its change. The list reconciles this with the corresponding recorded change. If there is a difference, you are able to see details about it.
-   
In the procedures Register vouchers, Voucher list, General ledger, and Balance information, you can from a posting use a link to go to Search stock accounting/Search management accounting to see the transactions behind the recorded amount.
