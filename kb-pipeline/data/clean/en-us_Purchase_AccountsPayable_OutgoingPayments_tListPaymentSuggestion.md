### The Payment suggestion list
This list contains information from the accounts payable about all unpaid supplier invoices, including credit invoices, that have been registered in the system and should be paid.
> If you are using the ISO payment method, you will in certain cases be required to use a special handling a credit invoices. [Read more about it here](../../../UserGuide/Using/ISOSetup/AboutISOPayments.htm).
The following information is displayed, but cannot be updated: supplier name, supplier number, consecutive number, block (cause), supplier’s invoice number, invoice type, and the invoice amount (the remaining amount converted to the company currency with the exchange rate of the accounts payable entry taken into consideration). Amounts for credit invoices and on account payments are displayed in red.
The information that can be updated in the list is described below.

#### Include
In this column you select which invoices should be included in the outgoing payment. By using the function button Move selected invoices ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) you can transfer the invoices to the tab Pay manually or Pay via bank (order). Which of these two tabs the invoices are transferred to depends on the payment method registered for the selected invoices; electronic or manual. Furthermore, all selected invoices must have the same payment method, otherwise, the function button will not be activated.

#### Payment method
Here you select the payment method that should be used for the outgoing payment of the supplier invoice in question. The payment methods available here are the ones registered in the Bank settings procedure. They also have to be set as Active in that procedure.
Please note! All invoices in the list that you select to include must have the same payment method. Otherwise you cannot execute the payment.

#### Due date
Here you can see the invoice’s due date which is saved in the accounts payable entry. The due date is displayed in red if it is a non-working day or if it has already passed (the payment date has been adjusted).
If the invoice has an electronic payment method registered, the due date will also be displayed in red if it is today or in past time.
You decide if today's date or next payment date should be suggested for overdue electronic payments with the Payment date for overdue electronic payments system setting.

#### Payment date
Here you see the date for the outgoing payment, by default the same date as the due date. But depending on whether the payment method of the invoice is electronic or manual, the payment date is managed differently:
- Electronic payment method – The payment date is normally set to the same as the due date of the invoice, but this can be changed on each row. You can have different payment dates on different rows. When suggesting payment date, the system considers the system setting Method for calculating payment date. A check is also made in order to make sure that the payment date is not today's date or in past time. If the due date is today’s date or in past time for an invoice, the system will automatically move the payment date forward in time to the first work day after today's date.
- Manual payment method – The payment date is based on the payment date for manual payments selected under the Selection tab. This date can be changed for each row.

#### Amount to pay
Here you see/enter the amount to pay. It is entered in the invoice's currency. It is the remaining amount on the invoice by default, but the amount can be changed. If you enter an amount that is lower than the remaining amount, the outgoing payment will automatically be managed as a partial payment. You cannot enter a greater amount than the remaining amount (overpayment) in the list. If you wish to make an overpayment, you must do that under the tabs Pay manually or Pay via file (order).
More info
Under the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you can generally find additional columns. Below you find the online help topics for the columns.

#### New remaining amount
Here you see the invoice's new remaining amount after payment (in the invoice's currency). You will only get a new remaining amount if a partial payment has been made.

#### Comment
You can here enter a comment for the invoice.

#### Pay via
Here you can enter the supplier number for the supplier via which the payment will be made. This will affect the account information etc. which is applied during the payment. When manual payment method is applied, this column cannot be modified.

#### Recipient account
Here you can see the default bank account number for the supplier. You can select among the bank accounts that are registered on the supplier. When manual payment method is applied, this column cannot be modified.

#### Sender account
Here you see our bank account that will be charged. When manual payment method is applied, this column cannot be modified. When electronic payment method is applied, it is possible to change account here. The default account is then selected based on the invoice's currency, primarily via the currency’s link to bank account and bookkeeping account in the Bank settings procedure, for the payment method of the invoice.
> Please note! Warnings might exist in the field Pay via which are not shown as standard. This field is found under More info. If you for example in the Bank settings procedure have chosen to block if giro number is missing, a validation error might appear when you move selected invoices and continue. In order to see these warnings you can drag the Pay via column to the list and save the layout for future use.
