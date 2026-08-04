### Startup settings
Before you can start using the Stock accountingStock accounting is a standard feature in Monitor ERP. It is used to continuously post all stock transactions in the system. This way the stock value in the Stock module matches the recorded value in the Accounting module. Changes in stock which are due to changed standard prices, direct stock reporting, arrivals and deliveries, stock count differences, nonconformities (cases), etc. will automatically be posted and give a better understanding of changes in stock and the company's gross profit margin in the income statement. and/or Management accountingManagement accounting is an option in Monitor ERP. It is used as a complement to the standard function called Stock accounting. The function means that all transactions on manufacturing orders (WIP value) are posted and transferred to the general ledger in the Accounting module in Monitor G5. The hours worked are recorded in the income statement, and provide a financial follow-up, for example, made per department and cost factor. Calculation differences are posted and these can be followed up per product, per order, etc. This function also contains extended management of cost of goods sold., you must configure some settings in the system.
> Please note! All startup settings and posting methods should be configured together with a consultant.

#### Voucher number series/Journals
In this procedure you register voucher number series for the journals which concern the Stock accounting, that is, voucher number series for Stock transaction journals and Price change journals.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc14.png)
If the option Management accounting is used, you also have to register voucher number series for Manufacturing order journal, Calculation difference journal, and possibly also for Invoicing journal (if COGS is recorded using posting method and not in the regular customer invoice journal).
> Please note! In the lower box you link each voucher number series and enter Yes as setting under Integration.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc15.png)
In the above example Management accounting is used, but COGS is recorded in the regular customer invoice journal in the Sales module.
> Please note! The journal for Direct stock reporting should not be used if you post stock transactions using the Stock accounting. It should be set to No in the Integration column.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc16.png)

#### System settings
There is also a number of system settings for the Stock accounting and Management accounting. You find these settings collected under the heading Management accounting, under the Accounting tab in the System settings procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc17.png)
Read more about each system setting in the topic [Management accounting](../../../GeneralRegisters/BasicSettings/SystemSettings/bManagementAccounting.htm) in the online help function for the System settings.
Under the Purchase tab you find a few of system settings concerning posting of price differences when final recording supplier invoice linked to purchase order:
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc18.png)
Activate posting of price difference and enter price alternative for this. The recommended option is Standard price at arrival.
Read more about the these system settings in the topic [Accounts payables](../../../GeneralRegisters/BasicSettings/SystemSettings/bAccountsPayable.htm) in the online help function for the System settings procedure.
Under the Stock tab you need to review the following system settings:
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc19.png)
The above system setting is applicable when the option Management accounting is used. Normally, this should be set to Started.
Read more about the above system setting in the topic [Part](../../../GeneralRegisters/BasicSettings/SystemSettings/bPart.htm) in the online help function for the System settings procedure.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc20.png)
The above system setting should be set to Cause and posting if it should be possible to enter a posting in connection with reporting of direct stock reporting.
Do not use the journal for direct stock reporting if you have configured this system setting to Cause and posting.
Read more about the above system setting in the topic [Direct stock reporting](../../../GeneralRegisters/BasicSettings/SystemSettings/bDirectStockReporting.htm) in the online help function for the System settings procedure.
Under the Sales tab you need to review the following system settings:
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc21.png)
The top system setting should normally be set to Yes. However, if you are using the option Management accounting and are recording COGS via this, then this system setting should be set to No, otherwise the COGS will be recorded twice. You can select the price alternative to be used in the calculation of COGS for P-parts as well as M-parts. The recommended price alternative is Standard price at delivery.
Read more about the above system settings in the topic [Invoicing](../../../GeneralRegisters/BasicSettings/SystemSettings/bInvoicing.htm) in the online help function for the System settings procedure.

#### Posting matrix
In the Posting matrix procedure you enter accounts which concern posting of COGS when invoicing. This is entered under the Sales account tab. The system setting Record material cost of goods sold at invoicing must be activated. As account for Material, the cost account for COGS is normally used. As account for Stock, the clearing account for delivery is normally entered (this account is debited at delivery and credited when invoicing). These accounts should be entered for product groups which concern goods that is stock updated and is delivered to customers. If the option Management accounting is used and COGS is recorded there, then the accounts below do not have to be entered here, but is entered in the procedure Register posting method instead.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc22.png)
In this procedure you also enter accounts concerning posting of price differences when linking supplier invoices. This is entered under the Purchase account tab. The system setting Record price differences during invoice registration must be activated. As account for Purchase, the clearing account for arrival is normally entered (this account is credited at arrival and debited at invoice registration). As account for Price difference, the cost account for price differences is normally entered. These accounts should be entered for product groups concerning material that is stock updated and is purchased from suppliers.
Price difference account should be configured for product groups concerning subcontract in cases you record planned subcontracting cost in WIP. When posting reported subcontracting cost, the price difference should only be recorded for product groups concerning purchase of goods.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc23.png)
Here you can also enter accounts concerning posting of direct stock reporting. The system setting Use cause/posting in the procedure Direct stock reporting must be set to Cause and posting.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/ManagementAcc24.png)

#### Chart of accounts
In the Chart of account procedure, you should mark Order number for the accounts where the system should post on the order number in the general ledger as well, for example on balance accounts which should be reconciled. Specification should be activated for the accounts where you wish the system to post additional details in the voucher rows in the general ledger, for example part number.
