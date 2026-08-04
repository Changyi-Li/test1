### Miscellaneous

#### Load account names/settings from file
With this setting you determine that certain information about the account is loaded in the import file and overwrites existing account information in the system. What is overwritten is account name, account type, and SRU All accounts in the chart of accounts are linked to an SRU code. (SRU is an abbreviation of the Swedish term for standardized accounting statement.) The code is used to transfer information from the accounting to the accounting schedule in the tax return. Information regarding the SRU coding is exported in the chart of accounts information in the SIE file. code. Other chart of account settings will be kept as they are.

#### Load dimension code names from file
With this setting you determine if the names of the dimension codes in the import file will be loaded and overwrite existing dimension names in the system.

#### Perform automatic postings
Here you decide if the system will generate automatic posting/allocation for the imported vouchers. This setting only applies if vouchers are imported.

#### Clear existing chart of accounts
With this setting you determine if the existing chart of accounts should be cleared when importing SIE file (4E or 4I). The chart of accounts clearing will in that case be performed for the accounting year you import to. Only accounts possible to delete will be removed, that is, not if that are included in balances, opening balances, transactions, standard accounts, posting matrix, bank settings, or VAT settings.
If you activate this setting, the Load account names/settings from file setting will become activated by default (mandatory).
