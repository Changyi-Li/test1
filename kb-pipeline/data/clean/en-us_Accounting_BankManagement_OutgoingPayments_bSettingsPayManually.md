### Settings

#### Payment date
Here you see the date for the payment of the invoices. By default this is set to the same payment date as in the settings in the Selection tab for the list type Payment suggestion.

#### Payment method
Here you select the payment method that will be applied to the supplier invoices added in the Outgoing payment box. The available options are manual payment methods. If you have entered a default payment method for manual payments in the Bank settings procedure, this payment method will be suggested. The payment method determines how the payments will be posted, that is, on which bookkeeping account. The selected payment method overrides the payment method registered for the accounts payable entry (the invoice).

#### Voucher text
Here you select the text that will be used as voucher text for manual payments that you register. The default text is “Outgoing payments”. This text will be shown as voucher text when the voucher is recorded in the accounting via integration. In the Voucher texts procedure you can create texts which you then can select among here as pre-defined voucher texts.

#### Batch total
The batch total is an optional control function, that is, the field can be left empty. The purpose of the batch total is to enter the total amount that the bank has stated as paid into the account. When you then enter all the outgoing payments, the system will warn if the amount does not match the batch total. You can also select which currency to use for the batch total. By default the company currency is selected, unless you have selected a payment method linked to an account in another currency.

#### Remaining batch
Here you can see the difference between the batch total and the outgoing payments that you have entered. When all the payments have been registered, the remaining batch should be zero. If it is not zero, you get a warning when saving. However, it is possible to save even though you have a remaining batch amount. The remaining batch amount takes the currency you have selected for the batch total into consideration. The remaining batch only adds together invoices registered in the same currency as the batch total. If you change the currency, the batch total will be added together again for the invoices that are registered in that particular currency. That way you can control the batch total per currency, in case the invoices have mixed currencies in the outgoing payments that you enter.

#### Batch number
The batch number is a hidden, automatic function that assigns an internal number for an outgoing payment batch that corresponds to the payment summary you get from the bank. The batch number is loaded from a number series and does not exist until you have saved the outgoing payments. This number helps you to gather payments reported with the same payment date. Furthermore, you can search by batch number in both the ledgers and the accounting. If needed, you can turn off this feature by entering 0 as start code in the number series for batch number.
