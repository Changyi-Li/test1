### Invoicing plans

#### Handle invoicing plans on quote/customer order
Here you activate functionality for invoicing plans. A specific tab for invoicing plans will be activated in Register quote and Register customer order procedures. Other functionality for this will also be activated. This system setting is deactivated by default.

#### Handle suspended VAT during payment of advance invoice
Here you determine how suspended VAT should be handled during payments of advance invoices. This setting is activated by default. The setting used for posting suspended VAT when invoicing advances is determined via exception per product group. If you activate this system setting, the VAT amount will be moved from the account for suspended VAT to the correct account for output VAT based on the customer order's VAT group.

#### Use separate accounts for invoiced and paid advances
Here you determine if two accounts should be used for advances, one for invoiced advances and one for paid advances. Then the turnover will be shown in the VAT report in connection with the payment of the invoice. This applies when the advanced VAT handling is not used. The setting is activated by default.
The invoiced advances are determined by the product group matrix. When the system settings above have been activated, the VAT amount will be moved from the account for suspended VAT to the correct account for output VAT based on the customer order's VAT group. This is made when the advances are paid. The advance will be reversed to the account for paid advances which in turn is linked to the VAT report. During invoicing of supplier invoice, the advance will be deducted from the account for paid invoices. If you have not activated setting for suspended VAT, the advance will be deducted from the account that was used during invoicing.

#### Automatic activation of forward rate on customer orders with invoicing plan
With this setting you decide if variable exchange rate should be allowed on orders and invoices in foreign currencies which have invoicing plans. By selecting No for this system setting, the system will not set a forward rate for orders that have an invoicing plan. This means that the rate applied during invoicing will be used for each partial invoice. Please note! Exchange rate differences on the advance account, if any, must be adjusted manually in the accounting. This system setting is deactivated by default. However, you can override this setting per order.
