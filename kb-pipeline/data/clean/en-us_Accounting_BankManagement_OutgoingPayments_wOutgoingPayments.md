## Outgoing payments
In this procedure you can register outgoing payments in the accounts payable ledger and confirm payments. By registering outgoing payments, the invoices concerned get status paid or partially paid in the accounts payable ledger. Postings are also updated in the accounting. In the Bank settings procedure, you configure several settings regarding outgoing payments that are registered in this procedure, for example settings for different payment methods and write-off codes.
> This procedure is available in the Purchase module and the Accounting module, with the same contents.
Payment suggestion
You can register outgoing payments in different ways in this procedure. One way is to order for payment directly via the Payment suggestion list, where the selected supplier invoices are directly transferred to a payment file that will be sent to the bank. Or you can transfer the selected invoices in the list to the transaction list to be approved/printed in the Print transaction list procedure. If you approve the invoices in the transaction list, they will be transferred to the payment file. Another way is to start by transferring all selected invoices from the Payment suggestion list to the Pay via bank (order) tab or adding them one by one to the tab, and then transferring them to a payment file. These methods mentioned apply for outgoing payments where electronic payment method is used. You can also register outgoing payments for supplier invoices where manual payment method is used in the Payment suggestion list. Then you start by selecting the invoices and transferring them to the Pay manually tab or you can add them one at a time to that tab.
> If you are using the ISO payment method, you will in certain cases be required to use a special handling of invoices. [Read more about it here](../../../UserGuide/Using/ISOSetup/AboutISOPayments.htm).
Otgoing payments via Bank integration
As before, outgoing payments are made here in the Outgoing payments routine. Either directly via the Payment suggestion list type, or via the Pay via bank (order) tab. Use the payment method set for bank integration. Read more about outgoing payments with Open Banking and File pay (ISO) below.
Outgoing payment with the payment method linked to Open Banking

##### International payments
Via Open Banking you can make both domestic and international payments from your bank account in the local currency (SEK account in Sweden, NOK account in Norway, EUR account in Finland).
> Read more about Global Pay [here](../../../UserGuide/Using/BankIntegration/GlobalPay.htm).
In the payment suggestion you can see which payments are made via Global Pay under the Global Pay column.
Clicking the Load provided exchange rate and bank charge button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_download.png) in the function menu loads the current (live) exchange rate and bank charge per payment. The exchange rate and bank charge is shown under the Provided exchange rate and Provided bank charge columns for each payment.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/BankIntegration_OutgoingPayments_GlobalPay.png)](../../../../Resources/Images/SubProjects/BankIntegration_OutgoingPayments_GlobalPay.png)
You can also schedule a payment (within 30 days) via Global Pay in the following circumstances:
- The company account uses one of the following currencies: EUR, NOK, SEK, DKK (not available for currency accounts)
- The payment is in one of the following currencies: EUR, NOK, SEK, DKK, GBP, USD (more currencies are planned to be added)
- The payment must be approved within 12 hours or the same day (before 23:59). If this is not done, the payment will be canceled by the bank and you will be required to cancel the payment manually in Monitor ERP.
Please note! The sooner you add the payment, the cheaper it will be (lower exchange rate can be offered).
For payments in another currency that has not been mentioned above, you are only able to put the current date as the payment date.
> You will be charged if you cancel an approved payment. The charge depends on the size of the payment as well as the difference in the exchange rate since the payment was first approved.
> Sparebank1 (Norway) also supports outgoing payments from currency accounts via Open Banking. This bank does however have a limit for international payments. New international suppliers must be manually set up with the bank. A message is shown in Monitor ERP if this has not been done when making an international payment.

##### Signing payments
When you approve your payment suggestion, a question will appear asking if you wish to sign (approve) the selected payments. Signing is done through BankID. If your bank is DNB or you have the setting that payments are signed on the bank’s webpage, you will be redirected to the webpage so you can sign.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/BankIntegration_Sign_Payments.png)](../../../../Resources/Images/SubProjects/BankIntegration_Sign_Payments.png)
Please note that even if you have signed in Monitor ERP, another user may be required to countersign via online banking. This depends on the framework for signing your company has set up with the bank.
> When countersigning, the following person signs via online banking. The exception is SEB and Nordea that do not support countersigning via Open Banking. If countersigning is needed with this bank, we recommend making outgoing payments via File pay (ISO),
Once the signing has been approved, a payment confirmation is shown in Monitor ERP.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/BankIntegration_PaymentsToSign.png)](../../../../Resources/Images/SubProjects/BankIntegration_PaymentsToSign.png)
If the payment has a green tick under Status, it means that the payment has gone to the bank. If there is a yellow warning or a red cross in the Status column, it means that something has gone wrong and the payment has not gone to the bank. Under the Message button you can see what is stopping the payment from being sent to bank. For individual payments e.g. this can occur with OCR/reference number checks (read more in the section below). These payments need to be canceled and the issue must be resolved (e.g. enter OCR/Reference number on the supplier invoice) before sending the payment again.
> If you have Swedbank or Sparebank1 and use Open Banking, please note that all new payees must be signed the first time you make a payment to them. Swedbank requires an extended BankID to be able to sign new recipients of payment. You can extend your BankID via online banking or going to your local branch.
> The bank might have a limit on how many payments can be signed at a time. In this case, multiple signing rows are shown and each must be signed individually.
> There is a limit of 70 characters for payment references when making batch payments of debit invoices containing deductions for credit invoices. This applies to payments to the same supplier with the same payment date. The limit applies to the total number of characters in the payment reference for all supplier invoices in the same batch.

##### OCR/reference number checks
When making an outgoing payment via Open Banking, a check is carried out whether the recipient of the payment requires an OCR/reference number. If this number is missing, the payment of the invoice is stopped and is excluded from the payment order that is forwarded to the bank. You then need to cancel the invoice payment in the Outgoing payment procedure, or change the status to resend in the Print transaction list. You then enter the invoice’s OCR/reference number in the Register supplier invoice procedure and pay the invoice again.

##### Credit invoices
Credit invoices are managed differently when paying via Open Banking. Since sending credit invoices is not supported via PSD2, the system automatically makes an automatic set-off between the debit and credit invoice, so the payment order that is sent to the bank is the net amount between the two. As reference information for the payment, the system sends both the debit and the credit invoice's reference to the recipient of the payment.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/BankIntegration_CreditInvoices.png)
If the debit invoice contains an OCR number, only the debit invoice’s OCR number is sent as reference to the recipient of the payment (with a deduction for the credit invoice). When confirming the system will automatically match both the debit and the credit invoice.
Outgoing payment with a payment method linked to File pay (ISO)

##### International payments
With File pay (ISO) you can make international payments via your currency account or use Global Pay.
Via Open Banking you can make both payments in another currency from your bank account in the local currency (company currency), meaning that you can make both domestic and international payments from your account in your local currency (SEK account in Sweden, NOK account in Norway, EUR account in Finland).
> In payment method in Bank settings you can choose whether Global Pay should be used by default for international payments.
In the payment suggestion you can see/select which payments should be made via Global Pay under the Global Pay column. You select payments by ticking/unticking the checkbox.
Clicking the Load provided exchange rate and bank charge button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_download.png) in the function menu loads the current (live) exchange rate and bank charge per payment. The exchange rate and bank charge is shown under the Provided exchange rate and Provided bank charge columns for each payment.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/BankIntegration_OutgoingPayments_GlobalPay_FilePay.png)](../../../../Resources/Images/SubProjects/BankIntegration_OutgoingPayments_GlobalPay_FilePay.png)
You can also schedule a payment (within 30 days) via Global Pay in the following circumstances:
- The company account uses one of the following currencies: EUR, NOK, SEK, DKK (not available for currency accounts)
- The payment is in one of the following currencies: EUR, NOK, SEK, DKK, GBP, USD (more currencies are planned to be added)
- The payment must be approved within 12 hours or the same day (before 23:59). If this is not done, the payment will be canceled by the bank and you will be required to cancel the payment manually in Monitor ERP.
Please note! The sooner you add the payment, the cheaper it will be (lower exchange rate can be offered).
For payments in another currency that has not been mentioned above, you are only able to put the current date as the payment date.
> You will be charged if you cancel an approved payment. The charge depends on the size of the payment as well as the difference in the exchange rate since the payment was first approved.
> Read more about Global Pay [here](../../../UserGuide/Using/BankIntegration/GlobalPay.htm).

##### Signing payments
When you approve your payment suggestion, a question will appear asking if you wish to sign (approve) the selected payments. Signing of payments is done via online banking. If any payment files need countersigning, this is also done via online banking.
> Tip! As payments are signed through the bank, you can make things easier by adding a link to your bank’s website in the Payment method tab in the Bank settings procedure. The website will then automatically open when you create an outgoing payment.
Confirmation
In this procedure you can also confirm paid supplier invoices (that have already been sent in a payment file to the bank and that the bank has confirmed as paid). The confirmation must be performed in order to update the status of the invoices as paid in the system. The confirmation is made in a list for the invoices that have been paid. In order to confirm outgoing payments, select the Confirmation list type.
You can perform confirmation via file. The purpose of this function is to use a file to confirm the payments that have been carried out by the bank. To load payments via file is a much faster and easier way to confirm payments than to manually confirm payments that you have registered with the bank.
> Outgoing payments via Bank integration are confirmed via the Manage transactions via bank integration tab in the Manage bank transactions procedure.
Cancellation
You can cancel or undo outgoing payments that have been made. You may need to cancel payments, if you for example, by mistake ordered invoices to be paid. Such adjustments should only be made before the payment file is sent to the bank. It is possible to cancel individual payments as well as entire outgoing payment journals, transaction lists, etc. In order to cancel outgoing payments, select the list type Cancel outgoing payments.
If you need to cancel an outgoing payment that has been sent to the bank but has still not been withdrawn from the bank account (future payment, the handling will be different depending on the bank you have. For most banks, it's the same as before, i.e. The payment order needs to be canceled via online banking and then canceled in Monitor ERP via the Cancel outgoing payment list type in the Outgoing payments procedure.
> The exception is if you have made an outgoing payment via Open Banking (Bank integration option) and use the banks Nordea, SEB, or Swedbank. If this is the case, you are not able to cancel via online banking, but must cancel via Monitor ERP. When you save the cancellation in Monitor ERP, an automatic message is sent to the bank saying that the payment order has been canceled. Please note that it may take about a minute before the payment order has been removed in the internet bank.
Outgoing payments as on account
You can also register outgoing payments as on account payments in the procedure. They can be outgoing payments of e.g. advance payments or excess payments (overpayment) for which there are no invoices in the accounts payable ledger. An outgoing payment like that creates a new accounts payable entry of type "On account On account is a partial payment (advance payment) which you have made to a supplier or received from a customer." and will then exist as a balance in your favor in the accounts payable ledger. You add on account payments under the Pay manually tab by leaving the field Consecutive number empty.
On account outgoing payment via file
If you want to send an on account outgoing payment via file, you should first register on account under the Pay manually tab. Then you can select an electronic payment method in the Payment method column. In the standard mode you will find this by clicking the More info button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). The on account payment will in this step create a record in the ledger which is not recorded. The record is shown as a debt to the supplier and thereby you see it as a positive amount in the Accounts payable list. After registration you can create payment via file in the same way as when you do other file payments. When the on account payment is confirmed/reported as paid in full, a new on account is automatically created. This on account record is recorded and displayed as a balance in favor against the supplier and thereby as a negative amount in the Accounts payable list procedure. The new on account record created is assigned the consecutive number from the original on account payment as Supplier invoice number. This is done to be able to see the connection between these two. For on account payments that have an electronic payment method, you will see On account (electronic) as Invoice type.
> The following system settings affect incoming payments: Default exchange rate for outgoing payments, Default exchange rate for outgoing payments (via file), and Method for calculating payment date.
Read more about [Setting up ISO payments](../../../UserGuide/Using/ISOSetup/ISOSetup.htm) under Using Monitor in the online help function.
List types

#### Payment suggestion
This list type is used to order for payment from a list of payment suggestions for invoices, and transfer them to a transaction list and a payment file or pay them manually.
The purpose of the list is to load payment suggestions for invoices selected by payment method. That is, that you load a list containing invoices that have the same payment method. In the list you will see all invoices that should be included when going ahead from payment suggestion to payment. If the payment method of the suggestions is manual payment, you transfer the invoices to the Pay manually tab where you can save and record the payments. If the payment method of the suggestions is electronic payment, you either transfer the invoices to the Pay via file (order) tab or skip that step and save instead. When you save, you can choose between transferring the invoices directly to a payment file or opening the transaction list and approving the invoices there instead and then transferring them to the payment file. Then you can also print the transaction list, if needed.

#### Confirmation
This list type is used to confirm paid supplier invoices (which has previously been sent to the bank in a payment file), for which you have received payment confirmation for the bank.
The purpose of the list is to load invoices for confirmation selected by payment method up to and including a certain payment date. All the invoices that are to be confirmed as paid will be displayed in the list. You can adjust the payment date if the payment was withdrawn on another day. You do not have to execute the confirmation in order to adjust the payment date, you only need to save it. This can be necessary if you for example have sent an adjustment task to the bank regarding changed payment date.

#### Cancel outgoing payments
This list type is used if you wish to cancel or undo outgoing payments.
The purpose of the list is to load already made outgoing payments of invoices for cancellation, e.g., if you by mistake ordered invoices for payment. Already paid and recorded outgoing payments can also be canceled. When canceling, reversal vouchers will be created for these outgoing payments.
Presentations
The presentations determine how the selected list should be displayed/presented. For example if it should be presented as grouped or as total. There are some standard presentations included in the program.
In most procedures where you can load lists, you are also able to create your own presentations.This is done under Presentations in the backstage of the procedure in question. If you create your own presentation you can for example choose if it should have a drilldown function and a drilldown filterering.
You can select which columns the list should consist of, and for each of the columns you can configure grouping, sorting, aggregation, and if the column should be shown in chart form and if it should be printed. Additionally you can also make printout settings, chart settings, and settings regarding extra aggregation.
Read more about this in [Presentations](../../../UserGuide/GeneralFeatures/Presentations.htm).
Selection rows
In a list procedure there is always a tab called Selection where you can select data records in different intervals from the database. The data records are then loaded by using the Load button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_display_list.png) in the toolbar of the procedure.
Under Selection rows in the backstage of the procedure, you can choose which selection rows that each list type should have, under the Selection tab in the procedure. In the List type field you select for which list type you want to customize the selection rows.
One table shows selection rows possible to select and one one table shows the selected selection rows. You can add, delete, or move selection rows by dragging and dropping the selection rows with your mouse pointer.
Using the Save button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_save.png) you save the selected selection rows.
Read more about this in the [Selection](../../../UserGuide/GeneralFeatures/Selection.htm) topic.
