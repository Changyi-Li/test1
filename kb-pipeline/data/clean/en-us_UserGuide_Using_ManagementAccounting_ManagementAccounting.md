## Stock accounting and Management accounting
Here it is described how stock accounting and management accounting works in Monitor ERP. Please note that Management accountingManagement accounting is an option in Monitor ERP. It is used as a complement to the standard function called Stock accounting. The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5. The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor. Calculation differences are posted and these can be followed up per product, per order, etc. This function also contains extended management of cost of goods sold. is an option in Monitor ERP.

### Stock accounting
Stock accountingStock accounting is a standard feature in Monitor ERP. It is used to continuously post all stock transactions in the system. This way the stock value in the Stock module matches the recorded value in the Accounting module. Changes in stock which are due to changed standard prices, direct stock reporting, arrivals and deliveries, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement. is a standard feature in Monitor ERP used to continuously post all stock transactions in the company. This way, the stock value in the Stock module matches the recorded value in the Accounting module. Changes in stock which are due to changed standard prices, direct stock reporting, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc1.png)
By using posting on cost center, cost unit, etc. the stock accounting also provides opportunity to give information about changes in stock on a more detailed level, for example per product group. This is possible since you can configure conditions for the posting (account and dimensions) via the stock accounting. These conditions can refer to a large number of terms for parts, customers, suppliers, and orders, such as product group, part code, order type, warehouse, etc.
In brief, the Stock accounting offers the following advantages:
- Stock values integrated with a stock account in the accounting, and does not have to be recorded manually.
- In-depth information about the cause of stock changes in the income statement. Without stock accounting, then the entire change in stock will manually be recorded "in a lump" once a month.
- By the use of dimension posting, it provides additional information about change in stock on product level.
> At present, the stock accounting does not support FIFOFIFO is calculated via the old stock log records existing in the system. All records have a price which is saved during the arrival reporting. However, for a purchase order the price will be updated when the supplier invoice becomes linked to the arrival reported items. This means that the FIFO value can change even though no stock transaction has taken place after the most recent inventory value list was created. Stock count and direct stock reporting will have the standard price as value. Other transactions such as negative reporting of material via manufacturing order, gets the standard price and also affect the FIFO. When FIFO is to be calculated, the part's balance is first checked. Then the program will find as many (positive) transactions as needed to be able to valuate these parts. The most recent transactions will then be used first. Example: If you have a balance of 100 units and the most recent transactions are: first a purchase of 80 units for EUR 10 each and then a purchase of 20 units for EUR 20 each, then the FIFO will be: 80 × EUR 10 + 20 × EUR 20 = EUR 1200, that is EUR 12 per unit. management of stock. It is instead based on posting of stock transactions at standard price (or calculation parts of standard prices).

### Tip! You should decide on work method together with your consultant from Monitor ERP System AB.
Management accounting
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc2.png)
Management accounting is an option in Monitor ERP, used to complement the stock accounting. Here all transactions for manufacturing orders (WIP value) in the system are continuously posted. These postings concern processing, subcontracting, and calculation differences.
With the management accounting it is also possible to record the invoicing log. This can be posted as standard in the regular invoice journal, but with Management accounting there is greater ability to determine the posting on multiple terms, while you can also record Cost of goods sold (COGS) distributed per calculation section.
- In brief, the Management accounting offers the following advantages:
- WIP value integrated with WIP account in the accounting, and does not have to be manually recorded.
- The worked hours on a manufacturing order will be recorded in the income statement and provides a good financial follow-up for example made per department and per cost factor.
- Calculation differences on manufacturing order are posted, and can be followed-up on, e.g. per product, or down to order level.

#### Cost of goods sold can be recorded divided per calculation section, and can be conditioned for more terms than customer group/product group.
Posted transactions
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc3.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc3.png)
Below you find a schematic illustration of the reporting flow and the transactions posted in stock accounting and management accounting. The transactions highlighted in green are posted in the stock accounting. The Stock accounting is included as standard in MONITOR. Transactions marked with red color require the option Management accounting. Gray arrows are posted in the regular invoice journals in the system. For the green and red transactions you have to register posting methods.

#### An example regarding how the above reporting flow might take place is found in the section [Example of posting of reporting flow](ExamplePosting.htm).
Procedures
- The Stock accounting and Management accounting means that the following procedure are added in the Accounting module:
- Register posting method
- Posting method list
- Posting of logs
- Search stock accounting/Search management accounting
Print log journal
