### Posting example
Below is an example of how posting can be done when using Monitor Factoring.
> The example is based on a Swedish chart of accounts.

#### Chart of accounts
| Account | Name |
|---|---|
| 1510 | Accounts receivable |
| 1517 | Accounts receivable factoring – Recourse |
| 2610 | Output VAT |
| 2640 | Input VAT |
| 3011 | Sales |
| 1930 | Bank |
| 2810 | Clearing account client funds |
| 6060 | Fees |
| 6350 | Factoring customer loss |

#### Events Invoice purchase (standard process)
(1) Invoice 1000 SEK including VAT recorded at invoicing.
(2) The invoice is purchased by Fedelta. Transaction type Invoice purchase when importing from Fedelta.
(3) Fee 10 SEK including VAT.
(4) Incoming payment of client funds 990 SEK from Fedelta to bank account. Takes place at regular incoming payment functions with the help of bank transaction rule.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Factoring_Posting1.jpg)

#### Events Invoice purchase with recourse
(1) Invoice 1000 SEK including VAT recorded at invoicing.
(2) The invoice is purchased by Fedelta. Transaction type Invoice purchase when importing from Fedelta.
(3) Fee 10 SEK including VAT.
(4) Incoming payment of client funds 990 SEK from Fedelta to bank account. Takes place at regular incoming payment functions with the help of bank transaction rule.
(5) Invoice recourse.
(6) Incoming payment after recourse.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Factoring_Posting2.jpg)

#### Events Invoice purchase followed by crediting of invoice
(1) Invoice 1000 SEK including VAT recorded at invoicing.
(2) The invoice is purchased by Fedelta. Transaction type Invoice purchase when importing from Fedelta.
(3) Fee 10 SEK including VAT.
(4) Incoming payment of client funds 990 SEK from Fedelta to bank account. Takes place at regular incoming payment functions with the help of bank transaction rule.
(5) Credit invoice 1000 SEK including VAT recorded at invoicing.
(6) The credit invoice is purchased by Fedelta. Transaction type Invoice purchasing credit invoice.
(7) Fee 10 SEK including VAT.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Factoring_Posting3.jpg)

#### Events Invoice purchase with recourse followed by crediting of invoice
(1) Invoice 1000 SEK including VAT recorded at invoicing.
(2) The invoice is purchased by Fedelta. Transaction type Invoice purchase when importing from Fedelta.
(3) Fee 10 SEK including VAT.
(4) Incoming payment of client funds 990 SEK from Fedelta to bank account. Takes place at regular incoming payment functions with the help of bank transaction rule.
(5) Invoice recourse.
(6) Credit invoice 1000 SEK including VAT recorded at invoicing.
(7) The credit invoice is purchased by Fedelta. Transaction type Invoice purchasing credit invoice.
(8) Fee 10 SEK including VAT.
(9) The recourse is credited at the same time.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Factoring_Posting4.jpg)

#### Events Invoice purchase with bad debt loss
(1) Invoice 1000 SEK including VAT recorded at invoicing.
(2) The invoice is purchased by Fedelta. Transaction type Invoice purchase when importing from Fedelta.
(3) Fee 10 SEK including VAT.
(4) Incoming payment of client funds 990 SEK from Fedelta to bank account. Takes place at regular incoming payment functions with the help of bank transaction rule.
(5) Invoice is written off (bad debt loss).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Factoring_Posting5.jpg)

#### Events Invoice purchase with bad debt loss after recourse
(1) Invoice 1000 SEK including VAT recorded at invoicing.
(2) The invoice is purchased by Fedelta. Transaction type Invoice purchase when importing from Fedelta.
(3) Fee 10 SEK including VAT.
(4) Incoming payment of client funds 990 SEK from Fedelta to bank account. Takes place at regular incoming payment functions with the help of bank transaction rule.
(5) Invoice recourse.
(6) Invoice is written off (bad debt loss).
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/Factoring_Posting6.jpg)
