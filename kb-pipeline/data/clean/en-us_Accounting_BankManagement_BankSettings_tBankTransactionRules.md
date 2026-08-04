### Bank transaction rules
This table defines how different types of bank transactions should be posted when bank statements are imported. Bank transaction rules are used in the Manage bank transactions and Bank account reconciliation procedures. In the Bank account reconciliation procedure, a check is first made if the record has been posted in the general ledger. If it is not, the transaction will become posted. Primarily, the payments are matched by Reference, if such has been registered. Secondarily, the match is made by Code.
The table is based on codes used by banks in Finland, but there are automatic converters which also transform those codes used in the CAMT053 and MT940 file formats.

#### Code
The codes available by default in the system consists of 3 characters, and the maximum is 6 characters.

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.

#### Translations
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Reference
Payment information/reference according to the account statement that you wish to match with. You can use wildcards such as % (percent).

#### Account
Here you see/enter the account for the transaction.

#### Dimensions
Here you will find dimension columns that can be linked to the write-off code. The dimensions apply to both incoming and outgoing payments.

#### Post automatically
Here you determine if transactions marked with Post automatically should be posted when the automatic matching in the Register payments and Bank account reconciliation procedures have been completed. A validation error is shown if the posting, for some reason, is not OK.

#### Automatic posting of VAT
With this setting you decide if VAT should be posted automatically. The system will re-allocate the posted amount so that the net amount is retained on the posting row, and the VAT amount is posted on a separate row.

#### VAT code
Select the VAT code that should be used for the automatic posting of VAT.

#### Active
Here you decide if the bank transaction rule should be active or not.
