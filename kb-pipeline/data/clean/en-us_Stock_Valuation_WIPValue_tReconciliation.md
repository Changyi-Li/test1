### The Reconciliation list
This list is available if you have installed the option Management accountingManagement accounting is an option in Monitor ERP. It is used as a complement to the standard function called Stock accounting. The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5. The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor. Calculation differences are posted and these can be followed up per product, per order, etc. This function also contains extended management of cost of goods sold.. In this list you reconcile the WIP value with booked balances on WIP accounts the accounting module.
If you have several WIP accounts, you should reconcile one WIP account at a time and make selections of orders, parts, product groups, part codes, etc. in order to make a correct reconciliation.
If you have installed the option Warehouse, you can choose to show WIP values for one or several warehouses. However, booked balances on WIP accounts in the accounting are not dependent on warehouse.
The information in the list is displayed for the time period you have selected (for example an accounting period) and is based on the reporting made on manufacturing orders (operations and material), price change log, and journals for management accounting. In the list you see (as total for each order) the WIP values at the beginning and at the end of the time period, as well as changes made during the time period (both in stock and on WIP accounts in the accounting). In the list you can also see differences regarding the WIP value changes in the Stock module and the Accounting module. By using this information you can take a closer look at order details and reconcile the transactions that have taken place per order as well as investigate why the differences occurred.
By marking an order in the Reconciliation box, you see all transactions for the selected order in the Log box. There you can see detailed information about different events on the order during the selected time period. There you also see waring if there are problems regarding journals for management accounting.
In the Summary box you see the WIP account's closing balance at the end of the selected time period. The balance is compared with the corresponding value in the WIP list. Any differences are shown in red font. Here you also see to which accounts the summary refer.
Read more about management accounting in the chapter [Stock accounting and Management accounting](../../../UserGuide/Using/ManagementAccounting/ManagementAccounting.htm) under Using MONITOR in the online help function.
Reconciliation
In this box, the WIP values are displayed in the company currency as total per order. By expanding a row using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_drill_down.png) next to the order number, you can see the WIP value distributed on material, subcontract, processing, and transfer to stock. Below you find a description of important columns in the list.

#### Status
In this column you can see a symbol representing the status of the manufacturing order.

#### Opening value
Here you see the part's WIP value on the date entered as From date in the settings section under the Selection tab. The WIP value corresponds to the loaded value in the Total by order list, if you set the valuation time to Historical value (actual date) and use the same date as valuation date.

#### WIP value change
Here you see the WIP value change between the dates entered in the settings section under the Selection tab.

#### Closing value
Here you see the order's WIP value on the date entered as From date in the settings section under the Selection tab. The WIP value corresponds to the loaded value in the Total by order list, if you set the valuation time to Historical value (actual date) and use the same date as valuation date.

#### Booked change
Here you see the WIP value change in the accounting between the dates entered in the settings section under the Selection tab. The change comes from postings (debit - credit) made on the WIP accounts that you have entered under the Selection tab. It is loaded from logs in all journals except for the invoicing log. Only postings that are transferred to the accounting are included in the value, unless you have activated the setting called Include not approved journals under the Selection tab.

#### Difference
Here you see the difference between the WIP value change and the booked change. Any differences are displayed in red font.
Log
In this box you see detailed information about the transactions from which the WIP value derives. This is shown for the order marked in the Reconciliation box. Recorded values on WIP accounts from postings are loaded from the logs: Stock transaction log, Manufacturing order log, and Price change log. By expanding a row using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_drill_down.png) next to the date, you can see all postings in detail on the transaction. Below you find a description of important columns in the list.

#### Date
Here you see the log date in the affected log.

#### Transaction type
For transactions from the stock transaction log, you see the transaction type from that log and not from the posting method. For transactions from the price change log, you see the transaction type "Standard price change", if you use standard price in the system or "Post-calculation" if you use FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. price. For transactions from the manufacturing order log, you see the transaction type from that log.

#### Quantity
For transactions from the stock transaction log, you see the balance change. For transactions from the price change log, you see the balance from that log as: WIP value's balance - "To stock" balance For transactions from the manufacturing order log, you see the reported quantity.

#### WIP value change
For transactions from the stock transaction log, you see the value of the log record as: Balance change x Standard price or Reported price if you use FIFO. These are the same values that can be loaded in the Stock transaction log procedure. For transactions from the price change log, you see the value of the log record as: (New price - Old price) x (WIP value's balance - "To stock" balance). These are the same values that can be loaded in the Price change log procedure. For transactions from the manufacturing order log, you see value of the log record. The value depends on the settings configured under the Selection tab for internal operations and subcontracts.

#### Booked change
Here you see any changes from the posting of the log record. The change comes from postings (debit - credit) made on the WIP account that you have entered under the Selection tab. Only postings that are transferred to the accounting are included, unless you have activated the setting called Include not approved journals under the Selection tab.

#### Difference
Here you see the difference between the stock value change and the booked change. Any differences are displayed in red font.

#### Information
If the difference is zero, "OK" is displayed in green text. If there is a difference, you see the cause of the difference.
Summary

#### WIP value
Here you see the closing WIP value on the To date.

#### Account balance
Here you see the closing balance on the WIP account on the To date.

#### Difference
Here you see the difference between the WIP value and Account balance. Any differences are displayed in red font.

#### From and To date
Here you see the date that was selected as reconciliation period under the Selection tab.

#### Accounts
Here you see the accounts that were selected under the Selection tab.
