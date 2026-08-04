### The Reconciliation list
This list can be used to reconcile clearing accounts, also called “arrival, not linked to invoice”. This can be useful if you are working with stock accounting or management accounting. The list is based on invoice bases as well as the order number posting on clearing accounts that is created when posting arrivals (posting of stock transaction log) and final recording of supplier invoices.
> To be able to reconcile using the list, the setting Order number needs to be activated for your clearing accounts in the Chart of accounts procedure.
The list is divided into three different boxes. In the top box you can see amount/balance for invoice bases and general ledger, as well as a comparison between these in the Difference column. Using the button in the Warnings column, you can see potential causes for the difference on the selected row (order). The following warnings can be shown:
-   
Supplier invoice journal is not approved.
-   
Cancellation journal of supplier invoices is not approved.
-   
There are preliminary vouchers containing this order number.
-   
An order row of type 2 (Additional order row) exists on order.
-   
An invoice basis row has been deleted.
-   
A part without stock update exists in order.
-   
A part of the type "Service" or "Fictitious" is used in the order.
-   
A voucher row with this account and order number exists with a later voucher date.
In the boxes Invoice basis and General ledger you can see more detailed information about the record/order you have selected in the list. Here you see information about the invoice bases and the records that are in the general ledger.

#### Create voucher for settlement per order number (rounding)
If you have activated the setting Create voucher for settlement per order number (rounding), you can create a voucher to remove roundings that create differences. In the voucher, debit and credit are recorded to the same account but with the order number on one side, depending on whether the difference is negative or positive.
The order number is recorded on the side that will make it so that the value is equal to the one in credit.
Example:­­­ If debit =35.54 and credit = 35.55, the order number will be recorded on debit with 0.01, so that debit is equal to credit.
You can configure the maximum difference that a voucher can be created for using the setting Amount limit for difference.
A green check ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) will then be shown in the list for rows that will be included in the voucher. If a red warning symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/error.png) is shown, the row cannot be included in voucher. This may be caused by the order including multiple accounts. To create a voucher, you will then need to redo the selection so that you get a maximum of one account per order.
The voucher is saved by clicking Approve ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_approve_document.png) in the toolbar. You will then be given a control question where you see how many rows will be included in the voucher. When you have confirmed the control question a summary will be shown containing the voucher number and the voucher date. You can also open the voucher by clicking the link ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_link.png).
