### Chart of accounts
- The Account class field has been replaced by the field Account type. The account types are Assets, Payables and equity, Income, Costs, and Internal. The account type can be used as selection field/information field in lists and determine for which accounts transfer of CB should be made when changing year.
- It is possible to enter that specific accounts should be blocked for manual postings. Only the system can post for these accounts, for example accounts receivable, accounts payable.
- New field: VAT type. With this field you decide if the account should have a link to the VAT report.
- New field: VAT code. When the VAT report is configured to follow the chart of accounts setting, this field will decide on which row in the VAT declaration/VAT report the purchase/sales should be recorded. When the VAT report is configured to follow VAT code on transaction level, then the field only determine which default VAT code should be used for manual posting on the account in the accounting.
- VAT row is now only entered for accounts of VAT type VAT account.
- The checkbox Currency account is marked for accounts where the general ledger transactions should take place both in company currency and external currency. Normally entered in external currency for bank accounts. When this setting is activated, a currency becomes linked to the account. Only transactions in this currency will be permitted throughout the entire system.
- You can have up to eight dimensions (in addition to Account) for which you can make settings in the chart of accounts.
- There is only one field for SRUAll accounts in the chart of accounts are linked to an SRU code. (SRU is an abbreviation of the Swedish term for standardized accounting statement.) The code is used to transfer information from the accounting to the accounting schedule in the tax return. Information regarding the SRU coding is exported in the chart of accounts information in the SIE file. code. In G4 there were two fields. In Basic dataWith "basic data" we refer to the static records in a database, for example parts, customers, users, work centers, etc. – Chart of accounts you can administer a table containing SRU codes and enter if the SRU code should be redirected to another SRU code when the sign is reversed.
- When the account is created/modified in the change of year, you will receive a question if also the following accounting years should be affected.
-   
New field: Budget chart. If you select a default budget chart for the account, then you don't have to manually enter a budget chart when registering budgets or when importing budgets.
-   
New tab: Budget. Under this tab you can show and register budget for the account in question and its sub-dimensions.
- Via the setting Override VAT code (Register supplier invoice) you can enter a fixed VAT code on the account. This VAT code should then always be used when registering supplier invoices. This function is available when VAT processing takes place via VAT code on general ledger transactions.
-   
New field for Account category.
