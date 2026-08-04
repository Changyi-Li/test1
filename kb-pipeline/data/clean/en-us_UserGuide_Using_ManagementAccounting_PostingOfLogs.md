### Posting of logs
In the Posting of logs procedure, you post transactions that should be recorded via Stock accountingStock accounting is a standard feature in Monitor ERP. It is used to continuously post all stock transactions in the system. This way the stock value in the Stock module matches the recorded value in the Accounting module. Changes in stock which are due to changed standard prices, direct stock reporting, arrivals and deliveries, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement. and Management accountingManagement accounting is an option in Monitor ERP. It is used as a complement to the standard function called Stock accounting. The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5. The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor. Calculation differences are posted and these can be followed up per product, per order, etc. This function also contains extended management of cost of goods sold.. It is also possible to automatically post and record the transactions in the accounting (using scheduling).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc48.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc48.png)
Manual posting
When you start using Stock accounting or Management accounting, we recommend that you manually run the posting. This is made in the top box of the procedure. The first time you post you need to enter a from date in the Post from column for each log.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc49.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc49.png)
Click the Run ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) button in order to execute the posting.
A message appears when the posting is made. The posting result can then be checked and printed in the Print log journal procedure. You can also see and check the postings in the Search management accounting procedure. This is made by selecting the alternative Not approved journals at the bottom of the Selection tab.
When you have approved and transferred the first journal to the accounting, the Post from field will be deactivated. The system automatically recognizes from when the posting has to take place in order to get all transactions – which are not yet recorded posted.
When you have run the logs from a date, you must check if records are added to you in journals from last month. Please note! These must be approved without integration.
Invalid postings
In connection to the posting, some transactions might not be possible to post. When transactions cannot be posted, a message appears.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc50.png)
A list of these transactions can be printed in the Print log journal procedure, under the Warnings tab. You might need to adjust/create new posting methods to be able to fix the error. This can be the case when, for example, basic data for parts has incorrect product groups, part codes, etc. You must then adjust the error and run a new posting of logs to see if the result is OK. Read more about [Warnings](PrintLogJournal.htm#Fliken_Varningar) in the section Print log journal.
Scheduling
Scheduling can be made for:
- Posting of logs
- Approve log journal (transfer to the accounting)
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc51.png)](../../../../Resources/Images/TrainingMaterial/ManagementAcc51.png)
Posting of logs
You can configure automatic posting of all logs in Stock accounting and Management accounting. This is made in the Scheduling box. Check the box Active on the row called Posting of logs. In the right box Posting of logs, you enter if the posting should be made at given times via Schedule or on certain Time intervals.
> Please note! To avoid overloading the server, we recommend that you do not run posting of logs more than necessary. This is especially important if the company has many transactions.
Approve log journal
When the logs are posted, the journals must be approved in order for the transactions to be recorded in the accounting. You can schedule approval of log journals in the same way as for posting of logs. This means that you do not have to use the Print log journal procedure. The transactions will be recorded in the accounting without printing a journal. Check the box Active on the row called Approve log journal. In the Approve log journal box to the right, you enter if the journal should be approved at given times via Schedule or on certain Time intervals.
> Tip! Please note! One voucher per log will be created in connection to each scheduled approval. If you do not want to have many voucher each day, the scheduling should not be set too frequently.
Automatic approval of log journals is not made for:
- Invalid postings (posting methods missing for the transaction)
- Transactions that belong to a closed/locked accounting period or voucher number series.
- Posting that contains incorrect/blocked accounts, dimensions
Notification and logging
You can activate logging for scheduling. This way you can, at a later time, view historical scheduling and also see statistics.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc52.png)
You can also activate notifications for scheduling.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc53.png)
The system can then send messages to selected users/roles/groups if, for example, transactions are found that cannot be posted.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc50.png)
These notifications can also be opened in the message center in Monitor ERP.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc54.png)
