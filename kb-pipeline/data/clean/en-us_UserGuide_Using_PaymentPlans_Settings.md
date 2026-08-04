### Settings
Here we’ve described the different settings you need to configure before you can start using payment plans in Monitor ERP.

#### System settings
In the System settings procedure, in the Purchase tab and under the [Payment plans](../../../GeneralRegisters/BasicSettings/SystemSettings/bPaymentPlan.htm) heading, you’ll find the following important system settings for invoicing plans:
1. Handle payment plans on purchase orders
2. Handle suspended VAT during payment of advance invoice
Setting 1 is the main system setting used to activate all functionality related to payment plans in the system.
Setting 2 should be activated in order for the VAT to be recorded from suspended VAT to output VAT when the advance invoice is paid. This means that the VAT will not be included in the VAT report until the advance invoice is paid.
> Please note! Also enter suspended VAT on the advance part. Read more under VAT settings below.

#### Posting matrix/service parts
Create a product group for advances (and if needed, also create a product group for in arrears/final payment). Under the Purchase account tab in the [Posting matrix](../../../GeneralRegisters/FinanceAccounting/PostingMatrix/wPostingMatrix.htm) procedure, you then enter the account to be used for advance and in arrears for each supplier group.
In the [Part register](../../../Stock/Parts/PartRegister/wPartRegister.htm) procedure you then create service parts regarding advance and in arrears. Remember to enter the correct product group for the service parts.

#### VAT settings
The following applies if suspended VAT is to be handled. In [VAT settings](../../../GeneralRegisters/FinanceAccounting/VATSettings/wVATSettings.htm), you specify that the advance in the payment plan will have the VAT code for suspended VAT. You do this in the Exception per product group tab, by using a separate VAT code for these payment plan rows and invoices. For the product group Advances, you enter the VAT code for suspended VAT for suppliers within the country.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlanVatSettings.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanVatSettings.png)

#### Chart of accounts
Mark Order number for the balance accounts which concern advances and in arrears. When order number is activated for these accounts, the system will automatically do a posting on an order number in connection with invoicing and payment. The purpose of posting on order number is to make it possible to find and reconcile book value per purchase order for these balance accounts. In the Invoicing plan list procedure, you can make such a reconciliation.

#### Invoicing/Payment plans
In [Invoicing/Payment plans](../../../GeneralRegisters/FinanceAccounting/InvoicingPlans/wInvoicingPlans.htm) you register the different invoicing plans and payment plans, as well as related settings. These can then be selected for customers, quotes, customer orders and purchase orders.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlan1.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlan1.png)
In the upper box, you define the invoicing and payment plans which there should be. In the box below you enter, for each plan, which partial invoices should apply for the plan, and the percentage to be allocated to each invoice.
In the Partial invoice type field you enter the type of the invoice:
- Advance – This invoice is sent before the order is delivered. For each partial invoice number of the advance type, an invoice basis will be created. The service entered will apply as invoice row when the invoice basis is linked to the supplier invoice.
- Delivery – The invoice which is sent with the delivery when the order is delivered. This invoice is in fact a "regular" invoice basis which is created in connection with the arrival of the order. Partial invoices of the type Advance and In arrears, will automatically be deducted from this invoice. This partial invoice type might generate several invoices for the same partial invoice number. This can occur if multiple partial deliveries of a purchase order are made, and you choose to send an invoice for each partial delivery.
- In arrears – This invoice is sent separately in arrears, for example, when the delivery has been approved on final inspection. For each partial invoice number of the arrears type, an invoice basis will be created in connection with release. The service entered will apply as an invoice row when the invoice basis is recorded.
