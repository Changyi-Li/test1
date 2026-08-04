### The Invoicing plan tab
Under the Invoicing plan tab you handle invoicing plans on customer order. This tab is shown in the procedure if the system setting Handle invoicing plans on quotes/customer orders is activated. This tab is gray (not available) if no invoicing plan is selected under the Header tab. Here you can get an overview of the total order value, what has been invoiced, and what is left to invoice. If a certain partial invoice has been released/delivered, partially delivered, partially invoices, or final invoiced, then it is not possible to change anything on the row. The amount is saved both in the currency of the order currency and in the company currency.
It is possible to change invoicing period and payment terms on the delivery row as long as the row's status is "Registered" or "Partial delivery made". On advance rows and in arrears rows, it is possible to change name, invoicing period, and payment terms, up to when the row is released.
It is possible to change amount and percent in the plan all the way up to the point when final delivery is made. However, you cannot change amount and percent for rows which are already released.
Read more about [nvoicing plan](../../../UserGuide/Using/InvoicingPlans/InvoicePlans.htm) under Using Monitor in the online help function.
At the bottom you see different totals regarding the invoicing plan. On the invoicing plan you can select how the Check for unpaid advance invoices at delivery should take place. The following alternatives are available: No check, Warn, or Block delivery.
When delivery reporting order rows included in an invoicing plan, deduction rows are automatically created for advance/in arrears payments. Please note! Rows added at the time of the delivery reporting, will never affect the invoicing plan.
Depending on the order row status, it is possible to release partial invoices of the type Advance and In arrears in this procedure. Those partial invoice types can also, depending on the status of the order row, be credited in the procedure. The partial invoice type Delivery is released when delivery reporting is performed. Partial invoice type is saved to the accounts payable/accounts receivable records and are shown in different lists.
The following buttons under this tab are special:
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_release.png) – Release for invoicing
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_undo_release.png) – Undo release
- ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_credit.png) – Create credit invoice
> It is not possible to create invoicing plans for warehouse.
Functionality in different row status
Step 1
In step 1, status Registered, only the button Release for invoicing is available for advance and in arrears rows. By releasing for invoicing, the Register invoice directly procedure will open with the correct basis loaded. The status of the row will be set to Released/Delivered.
Step 2
In step 2, status Released/Delivered, only the button Undo release is active. By using the button Undo release, the invoice basis will be deleted, a message saying that the invoice basis is deleted will be shown, and the row will get status Registered. If the invoice basis only has text rows left in addition to the advance/in arrears row, then the entire invoice basis will deleted.
Step 3
In step 3, status Invoiced, only the button Create credit invoice is active. By using that button, the procedure Register invoice directly will open and a basis for a credit invoice is created. The status of the row will be set to Registered, and it is possible for you to release the invoice basis again.
Step 4
In step 4, when the status is Paid and a payment is canceled, then the status will go back to Invoiced.
Step 5
If you want to delete a remaining value when the invoicing plan has been invoiced and there is a difference, the Delete remaining button will become available at the bottom of the tab. Then the amount in the plan is written-off, no accounting record is created so this should in that case be manually posted. A row for deleted is added in the total at the bottom of the tab, and thereby the difference disappears.

#### Comprehensive invoice
The following applies for comprehensive invoicing of invoicing plans. It is only for the partial invoice type Delivery which belongs to the same order that you can use comprehensive invoicing, for example if you have made partial deliveries on the order. For the partial invoice types Advance and In arrears, it is not possible to use comprehensive invoicing.

#### The Delete remaining button
When everything on the order is invoiced, then the amount of the invoicing plan's value should be the same as the total invoiced value. Otherwise, a difference is shown as below. Such a difference can for example occur if you delete remaining at delivery or if you delivery a larger quantity than the ordered quantity. By using the Delete remaining button you can delete this remaining record. The button becomes activated when all rows are invoiced and there is a difference. When you have clicked the button Delete remaining, the amount is moved from the column Left to invoice to the column Deleted amount, and Left to invoice becomes zero. Please note! You might need to create a manual accounting adjustment. No automatic adjustment of the accounting will be made regarding this.
> A control question appears when you delete the remaining. This is done to make sure you will not delete anything by mistake, since a deletion cannot be undone.
