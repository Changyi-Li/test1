### Settings
Here we have described the different settings you have to configure before you can use cash discount in Monitor ERP.

#### Conditions
Under the Payment terms tab in the Terms procedure you configure settings regarding cash discount on each of the affected payment terms. Enter an appropriate name on the payment term. This name should clearly show that it refers to cash discount (see example below). Click the button Cash discount to enter a number of days for cash discount and a percentage for cash discount. For each payment term it is possible to enter up to three cash discount limits.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/TermsConditions.png)](../../../../Resources/Images/TrainingMaterial/TermsConditions.png)
Under Basis for cash discount you can choose whether the cash discount should be based on the the invoice’s gross or net amount. When using the net amount it means that the VAT will not be affected by the cash discount when the payment is recorded.
A supplier invoice has a payment term with a 1% cash discount when making the payment within 7 days, and the basis for cash discount is set to net amount. The invoice amount is EUR 62,500 incl. 25% VAT (EUR 12,500). When the payment is made within 7 days, and since the cash discount is based on the net amount (EUR 50,000), the amount to pay is EUR 62,000. In the bookkeeping, EUR -500 will be recorded on the account for discounts.

If the same supplier invoice would instead use the gross amount as basis for the cash discount, the amount to pay would be EUR 61,875 since the cash discount (EUR 625) is based on the gross amount of EUR 62,500. In the bookkeeping, EUR -125 would be recorded on the VAT account and EUR -500 is recorded on the account for discounts.

#### System settings
In the System settings procedure, under the Sales tab and under the Incoming payments heading, there is a system settings for cash discounts: Grace period for cash discount for incoming payments. This system setting is set to 0 days by default. This means the procedures regarding incoming payments will suggest the discounted amount if the payment date is on the cash discount day or earlier. If you for example enter a 3-day grace period, the discounted amount will be suggested up to and including three days after the cash discount date.

#### Bank settings
Under the Write-off codes tab there is a write-off code which should be used for cash discount on outgoing and incoming payments. The system will automatically suggest the write-off code marked with Cash discount when a cash discount is received/given in the payment procedures. When a write-off code relating to a cash discount is used, the discount is posted using the entered account. If the cash discount is based on the gross amount, a VAT adjustment is also posted based on the discount.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/CashDiscount_BankSettings.png)](../../../../Resources/Images/TrainingMaterial/CashDiscount_BankSettings.png)
Please note! You might have to enter a different account for cash discount depending on the customer group/supplier group. You enter these by clicking the button E (Exception account).
