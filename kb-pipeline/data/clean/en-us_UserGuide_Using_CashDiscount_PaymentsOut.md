### Outgoing payments

#### Payment suggestion
If you use cash discounts on supplier invoices, you should choose the presentation Cash discount for the list type Payment suggestion in the Outgoing payments procedure. A tip is to make this presentation the default one. This is done via Default values in backstage.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PresentatonCashDiscount.png)](../../../../Resources/Images/TrainingMaterial/PresentatonCashDiscount.png)
When you are working with cash discounts, it is important to activate the setting Consider cash discount date. You should also configure a default value for that setting. When the settings is activated, the list is adjusted to have the payment date and paid amount take the cash discounts into consideration.
When you load a payment suggestion it is common to select invoices which are due up to and including a specific date, as seen in the image below. When the setting Consider cash discount date is activated, invoices with a cash discount date before this due date will also be included. The purpose of this is to be able to pay the invoices on their cash discount date, that is, prior to their regular due date.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/SettingsPaymentsIn.png)](../../../../Resources/Images/TrainingMaterial/SettingsPaymentsIn.png)
In the presentation Cash discount you see several columns concerning cash discount. Payment date on the invoices will be suggested according to the invoice's regular due date or according to cash discount limit 1, 2, or 3. If a discount is activated, you will see cash discount date and cash discount in percent in bold font. Amount to pay will take possible discounts on each invoice into consideration, that is, it will be reduced with the cash discount amount. The discounted amount is shown in a separate column to the right.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/PaymentsOutList.png)](../../../../Resources/Images/TrainingMaterial/PaymentsOutList.png)

#### Pay manually
During manual payment the system will take cash discount, if any, into consideration in the same way sas when registering incoming payments. Read more in the topic [Manual registration of incoming payments](PaymentsIn.htm).

#### Pay via bank (order)
When you order outgoing payments via file, cash discount will be taken into consideration in the same way as in the payment suggestion. That is, the system suggests a payment date and amount to pay based on the cash discount which can be obtained. However, if it is too late to use the cash discount, then the system will suggest to pay the remaining amount in full on the regular due date.

#### Confirmation
When confirming outgoing payments, the system will consider that invoices have been sent for payment with deduction for cash discount. When the confirmation is made, the system suggests the write-off code Cash discount. Posting of discount and VAT takes place in the same way as during incoming payments. When making a partial payment of invoices with cash discount, the cash discount is posted when the final payment is confirmed.
