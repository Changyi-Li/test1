### The Stock value change/Reconciliation list
In this list you reconcile the stock value with booked balances on stock accounts in the accounting module.
If you have several stock accounts, you should reconcile one stock account at a time and make selections of orders, parts, product groups, part codes, etc. in order to make a correct reconciliation.
If you have installed the option Warehouse, you can choose to show stock values for one or several warehouses. However, booked balances on stock accounts in the accounting are not dependent on warehouse.
The information in the list is displayed for the time period you have selected (for example an accounting period) and is based on part balances, reported prices (standard prices or FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price), price change log, and journals for management accounting. In the list you see (as total for each part) the stock values at the beginning and at the end of the time period, as well as changes made during the time period (both in stock and on stock accounts in the accounting). In the list you can also see differences regarding the stock value changes in the Stock module and the Accounting module. By using this information you can take a closer look at part details and reconcile the transactions that have taken place as well as investigate why the differences occurred.
By marking an order in the Reconciliation box, you see all transactions for the selected part in the Log box. There you can see detailed information about different events for the part during the selected time period. There you also see waring if there are problems regarding journals for management accounting.
In the Summary box you see the stock account's closing balance at the end of the selected time period. The balance is compared with the corresponding value in the stock value list. Any differences are shown in red font. Here you also see to which accounts the summary refer.
Read more about stock accounting in the chapter [Stock accounting and Management accounting](../../../UserGuide/Using/ManagementAccounting/ManagementAccounting.htm) under Using MONITOR in the online help function.
Reconciliation
In this box, the stock values are displayed in the company currency as total per part. Below you find a description of important columns in the list.

#### Opening value
Here you see the part's stock value on the date entered as From date in the settings section under the Selection tab. The stock value corresponds to the loaded value in the Total list if you select the balance alternative Historical balance (actual date), and use the same date as well as activate Historical price for purchased and manufactured parts.

#### Stock value change
Here you see the stock value change between the dates entered in the settings section under the Selection tab.

#### Closing value
Here you see the part's stock value on the date entered as To date in the settings section under the Selection tab. The stock value corresponds to the loaded value in the Total list if you select the balance alternative Historical balance (actual date), and use the same date as well as activate Historical price for purchased and manufactured parts.

#### Booked change
Here you see the stock value change in the accounting between the dates entered in the settings section under the Selection tab. The change comes from postings (debit - credit) made on the stock accounts that you have entered under the Selection tab. It is loaded from journals in the stock transaction log and price change log. Only postings that are transferred to the accounting are included in the value, unless you have activated the setting called Include not approved journals under the Selection tab.
This column is shown when the Reconciliation of general ledger setting is activated.

#### Difference
Here you see the difference between the stock value change and the booked change. Any differences are displayed in red font.
This column is shown when the Reconciliation of general ledger setting is activated.
Log
In this box you see detailed information about the transactions from which the stock value derives. This is shown for the part marked in the Reconciliation box. Recorded values on stock accounts from postings are loaded from the logs: Stock transaction log and Price change log. By expanding a row using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_drill_down.png) next to the date, you can see all booked postings in detail on the transaction. These log records are the basis for the booked change on the selected part. You cannot expand the row if there are no booked changes. Below you find a description of important columns in the list.

#### Date
Here you see the log date in the affected log.

#### Order number
Here you see the order number from the stock transaction log.

#### Transaction type
For transactions from the stock transaction log, you see the transaction type from that log and not from the posting method. For transactions from the price change log, you see the transaction type "Standard price change".

#### Quantity
For transactions from the stock transaction log, you see the balance change. For transactions from the price change log, you see the balance from that log.

#### Stock value change
For transactions from the stock transaction log, you see the value of the log record as: Balance change x Reported price. These are the same values that can be loaded in the Stock transaction log procedure. For transactions from the price change log, you see the value of the log record as: (New price - Old price) x Balance. These are the same values that can be loaded in the Price change log procedure.

#### Booked change
Here you see any changes from the posting of the log record. The change comes from postings (debit - credit) made on the stock accounts that you have entered under the Selection tab. Only postings that are transferred to the accounting are included, unless you have activated the setting called Include not approved journals under the Selection tab.

#### Difference
Here you see the difference between the stock value change and the booked change. Any differences are displayed in red font.

#### Information
If the difference is zero, "OK" is displayed in green text. If there is a difference, you see the cause of the difference.
Summary

#### Stock value
Here you see the closing stock value on the To date.

#### Account balance
Here you see the closing balance on the stock account on the To date.

#### Difference
Here you see the difference between the Stock value and Account balance. Any differences are displayed in red font.

#### From and To date
Here you see the date that was selected as reconciliation period under the Selection tab.

#### Accounts
Here you see the accounts that were selected under the Selection tab.
