### Settings for match in Workflow
Under this tab, you configure general settings regarding allowed differences in days and amount that are used in EIM Workflow.
In the Supplier register procedure under the EIM Workflow tab, you are able to allow differences that only apply to a specific supplier and override these general settings. In that procedure you can also choose to not allow automatic final recording for invoices from the supplier.

#### Match identical order rows based on qty, price, and delivery date when pos. no. is not unique
If you activate this setting, EIM Workflow can match invoice rows to order rows even in cases where there are multiple identical rows.
When this setting is not activated, the EIM Workflow can only do the matching if the position number on the invoice row corresponds to the position number on the order row.

#### Allowed difference in days before due date
Here you enter the allowed difference before the due date, in relation to the payment term on the purchase order (order invoice) or on the supplier (expense invoice).
As long as the number of days between the due date of the invoice and the calculated due date (based on the invoice date and the payment term), is within the allowed difference, the invoice will not be sent for authorization for this reason.
The default value is zero (0) days. Then no difference is allowed. If you leave this field empty, this difference will not be taken into consideration.

#### Allowed difference in days after due date
Here you enter the allowed difference after the due date, in relation to the payment term on the purchase order (order invoice) or on the supplier (expense invoice).
As long as the number of days between the due date of the invoice and the calculated due date (based on the invoice date and the payment term), is within the allowed difference, the invoice will not be sent for authorization for this reason.
The default value is zero (0) days. Then no difference is allowed. If you leave this field empty, this difference will not be taken into consideration.

#### Allowed difference on price each (amount and percentage)
Here you enter the allowed difference in price each between invoice row and purchase order row. Invoices within this interval will not be placed in the inbox called Failed for precisely this reason. You can enter the difference in both company currency and percent. If the price each on the invoice row is in foreign currency, the price each in the company currency will be converted into the currency on the invoice row.
The default value is zero (0.00). Then no difference is allowed. If you leave this field empty, this difference will not be taken into consideration.

#### Automatic update of price each when matched within allowed diff.
This setting determines whether the Workflow service should automatically update price each on order rows that have been matched and linked. The setting takes into account the Allowed difference on price each (amount and percentage) which means that if the difference between the order row’s price each and the invoice row’s price each is within the allowed difference, the price on the order row will be automatically updated and the invoice will be automatically approved and final recorded. By default, No is selected for this setting, so the invoice is approved automatically however goes to the For final recording inbox and the price each needs to be manually adjusted for the invoice’s posting to balance.

#### Allowed difference on row total (amount and percentage)
Here you enter the allowed difference in row amount between invoice row and purchase order row. Invoices within this interval will not be placed in the inbox called Failed for precisely this reason. You can enter the difference in both company currency and percent. If the amount on the invoice row is in foreign currency, the amount in the company currency will be converted into the currency on the row.
The default value is zero (0.00). Then no difference is allowed. If you leave this field empty, this difference will not be taken into consideration.

#### Allowed difference on invoice total (amount and percentage)
Here you enter the allowed difference in total amount between invoice and purchase order. Invoices within this interval will not be placed in the inbox called Failed for precisely this reason. You can enter the difference in both company currency and percent. If the invoice total on the invoice is in foreign currency, the invoice total in the company currency will be converted into the currency on the invoice.
The default value is zero (0.00). Then no difference is allowed. If you leave this field empty, this difference will not be taken into consideration.
The system setting Allowed exchange rate difference on imported invoice determines the allowed exchange rate difference in percent on imported invoices in foreign currency. An invoice with a greater exchange rate difference than the entered percentage value, must be authorized in EIM Workflow.
