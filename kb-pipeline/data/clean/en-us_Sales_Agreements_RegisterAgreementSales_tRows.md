### The Rows tab
The agreement rows contain the same information as the customer order rows under the [Rows](../../Orders/RegisterCustomerOrder/tRows.htm) tab of a customer order. The information which is only available for agreement rows is described below.
At the bottom of the tab you will see a total of Total/Interval excluding VAT and including VAT shown in the currency of the agreement rows and in the company currency. You can also see a total of the standard price for all rows. This is calculated as standard price × quantity per row, and then the rows will be added together. You can also see the rows’ total CM The contribution margin (CM) is the difference between the standard price and the sales price. and CR The contribution ratio (CR) is the portion of the invoice amount (sales price) that the contribution margin represents. CR is entered as a percentage..
The Function menu
The function menu for agreement rows mainly consists of the same buttons as for customer order rows on a customer order. The buttons which are specific for agreement rows are:
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_row.png) – Split row (copy row) (Ctrl + Shift + C). With this button you split an agreement row to a new agreement row. This function is the same as on a customer order row. Please note! Rows for suggested upward adjustment will not be copied. Please note! Sub-rows for alloy cost will be copied only if the Alloy cost setting in the customer register is set to create alloy cost at order registration. Packaging is not added when you split row since these rows are created at the delivery reporting.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_finished_tasks.png) – Finish row. When you click this button today’s date will be inserted in the Valid to field if it is a regular agreement row. If accrual accounting is applied, the end date of the most recently released period will be inserted. This means that the marked agreement row will be finished.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusInvoice.png) – Show one-time costs. With this button you decide whether or not One-time costs should be shown under this tab.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add.png) – Create upward adjustment rows. If make changes to existing agreement rows (row type 1 and 2) which increase the row amount within a period that has been released, you can make adjustments for this. Only future agreement bases not yet released will be affected by the changes. Please note! You cannot make upward adjustments for agreement bases if the agreement is accrual based.
When you click the button, a new row is created on the next not yet released agreement basis. A tooltip displays the calculated adjustment amount and for which period the adjustment applies.
You can use suggested upward adjustment if you, for example, increase the quantity on the agreement row for an active agreement.
Suggested upward adjustment is not displayed on the agreement document.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_copy_to.png) – Recalculate order inflow. Using this button you can recalculate order inflow for a separate agreement row or for the entire agreement. The current order inflow records will be deleted and new records will be created taking the agreement rows’ current data such as prices, quantity, discount, and date of agreement, into consideration. Order inflow records gets a log date based on the Agreement date.

#### (P) Order's part status
When all bases containing a specific agreement row have been released, the agreement row will be marked as delivered. It is then only possible to edit Valid from and Valid to for that row.

#### Quantity
The quantity of the part. The field displays two decimals by default, but it is possible to enter up to six decimals.
For row type 1 and 2, the quantity must be greater than zero.

#### Unit
For row type 1, you here see the part's default unit. If there are more than one unit registered for the part, you will see the unit marked for customer order under the Usage button in the Part register. You can change to another unit if there are several units registered for the part. If you change to another of the part’s units you will be asked if the quantity, the future quantity, and previous quantity should be recalculated according to the entered conversion factor. The price/interval will also be affected if you change the unit. Unit is mandatory for row type 1.
For row type 2, no unit will be suggested, but you can select among all units in the system. By clicking the x button in the Unit field, you can delete the unit on the row in question. It is optional to enter a unit for row type 2.
The unit is always displayed in the user's language. On printouts of the agreement report it is displayed in the language of the mailing address. On printouts of pick lists it is displayed in the user's language. On printouts of delivery notes it is displayed in the language of the delivery address.
> Please note! If you change unit for an agreement that is active, this will only affect the agreement bases which have not yet been released.

#### One-time cost
Here you decide if the agreement row should be a one-time cost or if it should be invoiced according to what is agreed. A one-time cost can, for example, be used if the agreement requires a start cost. On the row which concerns the extra cost, you should add information regarding how the one-time cost should be handled. The one-time cost is added to an existing but not yet released invoice bases, or you can create a new invoice basis for the one-time cost.
- One-time cost – Here you decide if the one-time cost should be added to an existing agreement bases or if a new agreement basis should be created for the one-time cost.
- Planned invoice date – If you chose to "Add to existing agreement basis", you get to select a planned invoice date among the existing bases. If you chose "Create new agreement basis", you get to select a planned invoice date in the calendar.
- Use accrual accounting – With this checkbox you decide if the one-time cost should be accrued. This can only be activated if Accrual accounting was selected under the Header and you had selected Create new agreement basis above. For an accrued one-time cost, the planned invoice date will be set to today’s date.
- Period start – Here you see/select the beginning of the period.
- Period end – Here you see/select the end of the period.
Valid to and Valid from for a one-time cost row will be updated when you click "Yes" in the dialog which opens when Valid to or Valid from is changed in the order header.
> It can be good to use a special part called start fee, one-time cost, or something similar, which you can then load and turn into a one-time cost. This will look best on the agreement report.

#### Price/Interval
Price per invoicing interval.

#### Price/Interval (company currency)
Here you see the price per invoicing interval in the company currency when the currency selected for the customer/agreement differs from the company currency.

#### Revision
For row type 1, you will see the part's active revision. You can change among the existing revisions of the part. If the active revision is not selected, the revision will be displayed in italics. By placing the cursor in the revision field, you will see an explanation of this in a tooltip. The Modified order confirmation will be printed if the part's revision has been changed after the order confirmation was printed.

#### Future quantity
In this field you can enter a future quantity which will be included in the agreement basis (the invoice basis) as of the date entered in the Future valid from.

#### Future price
In this field you can enter a future price which will be included in the agreement basis (the invoice basis) as of the date entered in the Future valid from.

#### Future valid from
This field is mandatory if Future quantity and/or Future price have been entered. Here you see the date from which the Future price should apply. As of this date, the new quantity and/or price will be included on the agreement basis (the invoice basis). The date is loaded from the Valid through date in the customer link or from the Valid through date of sales prices in the part register. Please note! One day is added to dates loaded from the part register.
> Please note! Future price/future quantity will affect the invoice bases without any warning.

#### Valid from
This is by default loaded from the Header tab, but it can be edited. The valid from date of the row determines which agreement bases the row will be included in. Valid from is also possible to edit for rows that are accrued.

#### Valid to
This is by default loaded from the Header tab, but it can be edited. The valid to date of the row determines which agreement bases the row will be included in. This means you can have a "Valid to" date on row level but the "Valid to" in the Header tab is empty. The "Valid to" is also possible to modify for accrued rows.

#### Previous quantity
Here you see the previous quantity. This field can not be edited.

#### Previous price
Here you see the previous price. This field can not be edited.

#### Previous valid through
Here you see the date when the row got a new quantity or new price. This field can not be edited.
