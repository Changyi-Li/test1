### Signers/Approvers
Here you add the signers/approvers who should be allowed to approve stock counts that have been performed in the Stock count in list procedure. If you have not entered any signers/approvers, all stock count items will be approved. The order of signers/approvers are from top to bottom, if several users are approvers. The user authorized to approve the highest difference should be at the top. Please note! The stock count difference can be both positive and negative, that is, a stock count difference of -10 EUR in the example below would mean that user A must approve this difference.
| User | Stock count difference (Value from) | Stock count difference (Value to) |
|---|---|---|
| A | EUR 1000 |   |
| B | EUR 100 | EUR 999 |
| C | EUR 1 | EUR 99 |

#### Name
Here you can write a descriptive text as a name. You enter name texts in the company language and they are displayed in the user’s language.
By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Value from
Here you can enter a Value from for the difference interval which this signer/approver is allowed to approve/authorize. Differences that are smaller than this value do not have to be approved.

#### Value to
Here you can enter a Value to for the difference interval which this signer/approver is allowed to approve/authorize.

#### Percentage of balance
Here you can enter a percentage as the authorization limit when a stock count difference occur.

#### Notify
With this setting you decide if the signer/approver should receive a notification/message in Tasks when he/she has a stock count to approve.

#### Active
With this checkbox you determine if the signer/approver should be active.
> If the signer/approver is absent, a user with the ERP manager or System administrator role can approve the stock count.
> If you have entered both a value interval and a percentage of balance, an approval will be required when a stock count difference falls outside either of these limits.
Examples
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/StockCountApproval.png)
In the above example the stock count approval works the following way:
Is the value of the stock count 100,000 SEK or more?
- Yes – Approval is needed from ÅKE.
- No – Is the percentage of balance change 20% or more?
- Yes – Approval is needed from ÅKE
- No – See the next row
Is the value of the stock count between 10,000 SEK and 99,999 SEK?
- Yes – Approval is needed from ANNA.
- No – Is the percentage of balance change 5% or more?
- Yes – Approval is needed from ANNA
- No – See the next row
Is the value of the stock count between 100 SEK and 9,999 SEK?
- Yes – Approval is needed from BENGT.
- No – Is the percentage of balance change 2% or more?
- Yes – Approval is needed from BENGT
- No – See the next row
