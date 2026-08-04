### The Payment plan tab
Under the Payment plan tab you handle payment plans for purchase orders.
This tab is shown in the procedure if the system setting called Handle payment plans on purchase orders is activated.
This tab is activated if a payment plan is selected under the Header tab. If not, it is inactive.
Here you can get an overview of the total order value, what has been invoiced, and what is left to invoice. If a certain partial invoice has been released/delivered, partially delivered, partially invoices, or final invoiced, then it is not possible to change anything on the row. The amount is saved both in the currency of the order currency and in the company currency.
It is possible to change invoicing period on the delivery row as long as the row's status is Registered or Partial delivery made. On advance rows and in arrears rows, it is possible to change name and invoicing period up to when the row is released.
It is possible to change amount and percent in the plan all the way up to the point when final delivery is made. However, you cannot change amount and percent for rows which are already released.
At the bottom of the tab you see different totals regarding the payment plan.
When arrival reporting order rows included in a payment plan, deduction rows are automatically created for advance/in arrears. Please note! Rows added during the delivery reporting, will never affect the payment plan.
Depending on the order row status, it is possible to release partial invoices of the type Advance and In arrears in this procedure. The partial invoice type called Delivery is released when arrival reporting is performed. Partial invoice type is saved to the accounts payable/accounts receivable records and are shown in different lists.
Read more about the [Payment plans](../../../UserGuide/Using/PaymentPlans/PaymentPlans.htm) application.
Functions
The Release supplier invoice basis button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_release.png) – With this button found on the function menu, you release invoice bases.
The Undo release button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_undo_release.png) – With this button you can undo the release of an invoice basis.
The Delete remaining button – You find this button at the bottom of the tab and you can use it to delete records that has a remainder. When everything on the order has been invoiced, the total value of the payment plan should be the same as the total invoiced value. Otherwise, a difference is shown. Such difference can, for example, occur if the supplier delivers/invoices something else than what was planned. By using the Delete remaining button you can delete this remaining record. The button becomes activated when all rows are invoiced and there is a difference. When you have clicked the Delete remaining button, the amount is moved from the column called Left to invoice to the column called Deleted. The Left to invoice column will then be zero. Please note! You might need to create a manual accounting adjustment. No automatic adjustment of the accounting will be made regarding this.
Functionality at different row status
Step 1
In step 1, status Registered, only the button Release supplier invoice basis is available for the advance and in arrears rows. When releasing, an invoice basis is automatically created which can be linked to invoices in the Register supplier invoice procedure. The row will be assigned the status called Released/Arrival reported.
Step 2
In step 2, status Released/Arrival reported, only the Undo release button is available for the advance and in arrears rows. By using the Undo release button, the invoice basis will be deleted. The row gets the status called Registered.
Step 3
In step 3, status Linked, not final recorded, the partial invoice has been linked to the order but the invoice has not yet been final recorded. The consecutive number of the supplier invoice is shown on the row.
Step 4
In step 4, status Final recorded, the partial invoice has been linked to the order and the invoice is final recorded. The consecutive number of the supplier invoice is shown on the row. If you credit the invoice or if you cancel it, the status will go back to Registered.
Step 5
In step 5, status Partially paid, the supplier invoice is partially paid.
Step 6
In step 6, status Paid, the supplier invoice is paid in full.
