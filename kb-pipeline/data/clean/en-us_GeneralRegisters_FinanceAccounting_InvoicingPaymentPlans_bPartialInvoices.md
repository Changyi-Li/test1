### Partial invoices

#### Partial invoice type
In this box you can select one of the partial invoice types Advance, Delivery, and In arrears.
- Advance – This invoice is sent before the order is delivered. For each partial invoice number of the advance type, an invoice is created. You can create an optional number of partial invoice rows.
- Delivery – This invoice is sent when the order is delivered. This invoice is in fact a "regular" invoice basis which is created in connection with the delivery of the order. Please note! It is mandatory that the invoicing plan contains one delivery row. However, only one delivery row can exist. A validation is made and a warning appears if you try to enter more than one delivery row or if you have not added any delivery row.
- In arrears – This invoice is sent separately in arrears, for example when the delivery has been approved by the customer. For each partial invoice number of the in arrears type, an invoice is created. You can create an optional number of partial delivery rows.

#### Service
Here you select a service for advance invoices and in arrears invoices.

#### Name
Here you see the name of the service for advance invoices and in arrears invoices. For delivery invoices you see the name Delivery invoice.

#### Percent (%)
Here you enter how large a share of the invoice amount should be included in this partial invoice. The total cannot be greater than 100%. The percentage can be entered with two decimals. It is not possible to enter negative percentages.

#### Payment terms
Here you select payment term for advance invoices and in arrears invoices. This term overrides the term entered for the customer. For delivery invoices this field is deactivated. The order's payment term applies to delivery rows.

#### Check for unpaid advance invoices
For delivery invoices you can activate a check for unpaid advance invoices. The check is made during picking, reporting, and delivery planning.
> This setting only applies to invoicing plans.
The following options are available:
- No check – No check is made to see if the in advance invoice is paid during delivery.
- Warn – A check is made to make sure that the in advance invoice is paid during delivery. A waring appears if the advance invoice has not been paid. However, it is still possible to make the delivery, if so desired.
- Block delivery - If the in advance invoice has not been paid you cannot delivery report the customer order. This is set by default on new delivery schedules that are created.
