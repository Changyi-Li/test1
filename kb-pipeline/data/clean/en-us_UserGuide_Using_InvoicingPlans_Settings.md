### Settings
Here we have described the different settings required to configure before you can start using Invoicing plans in Monitor ERP.

#### System settings
In the System settings procedure, under the Sales tab and under the heading [Invoicing plans](../../../GeneralRegisters/BasicSettings/SystemSettings/bInvoicingPlan.htm), you find the following important system settings for invoicing plans:
1. Handle invoicing plans on quote/customer order
2. Handle suspended VAT during payment of advance invoice
3. Use separate accounts for invoiced and paid advances
4. Automatic activation of forward rate on customer orders with invoicing plan
Setting 1 is the main system setting used to activate all functionality related to invoicing plans in the system.
Setting 2 should be activated in order for the VAT to be recorded from suspended VAT to output VAT when the advance invoice is paid. This means that the VAT will not be included in the VAT report until the advance invoice is paid.
> Please note! Also enter suspended VAT on the advance part. Read more under VAT settings below.
Setting 3 should be activated to handle separate accounts for paid and unpaid advances. This way, it is possible to get the VAT report to show the turnover in connection with the payment of the invoice. This should be done for trade liable to VAT within the country. You should activate Setting 3 if you have activated Setting 2.
Setting 4 determines whether a variable exchange rate should be allowed on orders and invoices in foreign currencies which have invoicing plans. By selecting No for this system setting, the system will not set a forward rate for orders that have an invoicing plan. This means that the rate applied during invoicing will be used for each partial invoice. Please note! Exchange rate differences on the advance account, if any, must be adjusted manually in the accounting. This system setting is deactivated by default. However, you can override this setting per order.

#### Posting matrix/service parts
Create a product group for advances (and if needed, also create a product group for in arrears/final payment). Under the Sales account tab in the [Posting matrix](../../../GeneralRegisters/FinanceAccounting/PostingMatrix/wPostingMatrix.htm) procedure, you then enter which account should be used for advance and in arrears for each customer group. If you have separate accounts for unpaid and paid advances, then you should here enter the account for unpaid advances.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlanPostingMatrix.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanPostingMatrix.png)
In the [Part register](../../../Stock/Parts/PartRegister/wPartRegister.htm) procedure you then create service parts regarding advance and in arrears. Remember to enter the correct product group for the service parts.

#### Standard accounts
If you use separate accounts for invoices and paid advances you should enter the account for paid advances in the [Standard accounts](../../../GeneralRegisters/FinanceAccounting/StandardAccounts/wStandardAccounts.htm) procedure. This account should be entered on the row Paid advances from customer. Please note! You might need to enter separate accounts per customer group. You might have to do this to achieve correct VAT reporting in cases where the VAT report loads the VAT code from the chart of accounts. You create exceptions per customer group by using the plus sign on the row.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlanStandardAccounts.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanStandardAccounts.png)

#### VAT settings
In the [VAT settings](../../../GeneralRegisters/FinanceAccounting/VATSettings/wVATSettings.htm) procedure you configure that the system should post advance invoices on the account for suspended VAT. This is done by using a separate VAT code for such invoices. This is done under the Exception per product group tab. On the product group Advances, you enter VAT code for suspended VAT for customers within the country.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlanVatSettings.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanVatSettings.png)

#### Chart of accounts
Mark Order number for the balance accounts which concern advances and in arrears. When order number is activated for these accounts, the system will automatically do a posting on an order number in connection with invoicing and payment. The purpose of posting on order number is to make it possible to find and reconcile book value per customer order for these balance accounts. In the Invoicing plan list procedure you can make such a reconciliation.

#### Invoicing plans
In the [Invoicing plans](../../../GeneralRegisters/FinanceAccounting/InvoicingPlans/wInvoicingPlans.htm) procedure you register different "invoicing plan templates" and settings for these. These can then be selected for customers, quotes, and customer orders.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlan1.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlan1.png)
In the top box you define which invoicing plans that should exist. In the box below you enter, for each invoicing plan, which partial invoices should apply for the invoicing plan as well as what the percentage share should be for each invoice.
In the Partial invoice type field you enter the type of the invoice:
- Advance – This invoice is sent before the order is delivered. For each partial invoice number of the advance type, an invoice will be created. The service entered here will apply as invoice row when the invoice basis is being invoiced.
- Delivery – The invoice which is sent with the delivery when the order is delivered. This invoice is in fact a "regular" invoice basis which is created in connection with the delivery of the order. Partial invoices of the type Advance and In arrears, will automatically be deducted from this invoice. This partial invoice type might generate several invoices for the same partial invoice number. This can occur if several partial deliveries are made of a customer order and you select to send one invoice for each partial delivery.
- In arrears – This invoice is sent separately in arrears, for example when the delivery has been approved by the customer. For each partial invoice number of the in arrears type, an invoice will be created. The service entered here will apply as invoice row when the invoice basis is being invoiced.
Under Invoice text on advance invoice/invoice in arrears, you can enter if any additional text information should be displayed on advance/in arrears invoice.

#### Number series
You can have a separate invoice number series for advance invoices. You set this up in the Number series procedure.
