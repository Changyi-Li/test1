### Posting
In this box you see hoe the sale/retirement will be posted for the main object. If you activate Total accounting order you will also see the posting for the sub-objects if there are linked sub-object which will be included in the sale/retirement. The posting of separate sub-objects are shown under the Sub-object tab if you have a sub-object loaded in the procedure.
When selling fixed assets it does not generate a regular income. Instead a calculation should first take place to see if the sale means a profit or loss compared to the recorded value (residual value). You can do this by comparing the sales price with the residual/recorded value (that is, the acquisition value minus the accumulated depreciation).
If the sales price is higher than the book value it is a profit which should be booked/recorded (in Sweden) on account 3979 Capital gains on sale of machinery and equipment. The sold fixed assets should be removed from the balance sheet. This is done by crediting for example 1210 Plant and machinery with the acquisition cost of the fixed assets, and debiting account 1219 Accumulated depreciation on machinery and equipment with the fixed assets' accumulated depreciation.
Posting example
Chart of accounts
- 1210 Machinery and equipment
- 1219 Accumulated depreciation
- 7830 Depreciation on machinery and equipment
- 3973 Capital gains on sale of machinery and equipment
- 7973 Losses on sale of machinery and equipment
- 3990 Other remuneration and revenue (this account will be used as transition account for sales, and you find it in the procedure Standard accounts.
Requirements
- Depreciation based on days
- Acquisition value: 100,000 (10 years depreciation period)
- Accumulated depreciation 1849.32
- Depreciated to 2017-01-31
- Sales date 2017-02-15
- Sales price: 60,000.
| Posting | Debit | Credit | Explanation |
|---|---|---|---|
| 7830 | 410.96 |   | Depreciation up to sales date |
| 1219 |   | 410.96 | Depreciation up to sales date |
| 1210 |   | 100,000 | Offset posting of acquisition value |
| 1219 | 2260.28 |   | Offset posting of value depreciation |
| 3990 | 60,000 |   | Sales price |
| 7973 | 37,739.72 |   | Loss |
Customer invoice is posted according (takes place via customer order journal during invoicing):
| Posting | Debit | Credit | Explanation |
|---|---|---|---|
| 1510 | 75,000 |   | Accounts receivable |
| 2610 |   | 15,000 | VAT 25% |
| 3011 |   | 60,000 | Sales |
Please note that the sale (60,000) is recorded with two records. A regular income, subject to VAT, 60,000. At the same time the same amount is booked in the debit account. For this booking the sales account which is VAT exempt is used. This way the sales accounts will cancel out each other's results in the accounting. However, this will be recorded correctly for the VAT report since the first account is linked to the VAT report but the second account is not. In the example above, a loss of 37,739.72 is posted.
If the sales price is higher than the residual value of the fixed asset, then then profit will instead be recorded on the standard account for profit (capital gains) on sale of fixed assets. When retiring without a sales price and the residual value is 0 (zero), then booking will only take place in the balance sheets without any affect of the result caused by the event.
Also you should note that if a sale takes place later than the most recent depreciation of the fixed asset, then an automatic depreciation will also take place for the fixed asset up to the date of the sale (according to the example in the tables). However, this final depreciation can be prevented if you deactivate the system setting Execute full depreciation in connection with sales/retirement.
The standard account for sales of fixed assets (Transition account for fixed asset sales) is last under the Accounting tab in the Standard accounts procedure. The posting recorded as sales price (3990 in the example above) is entered there.
Example of posting when selling/retiring part of a fixed asset
The following applies when a certain part of a fixed asset is sold/retired. This means the acquisition value and previously made depreciation for the disposal, will be proportionally distributed in relation to the current total acquisition value.
Requirements
- Acquisition value: 60,000
- Accumulated depreciation at date of sale: 3,000
- Sales date and the most recent depreciation date is the same
- Part of acquisition value to dispose of: 15,000 (that is, 25%)
- Sales price: 0.
| Posting | Debit | Credit | Explanation |
|---|---|---|---|
| 1210 |   | 15,000 | Offset posting of part of acquisition value |
| 1219 | 750 |   | Offset posting of part of value depreciation (25% of 3,000) |
| 7973 | 14,250 |   | Loss |
