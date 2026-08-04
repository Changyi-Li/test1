### Delivery and invoicing of delivery invoice
Delivery planning, if any, and delivery will be made as usual.

#### Delivery planning
If delivery planning has been activated for the order, then it is possible to block it if the advance invoice has not been paid. In the [Delivery planning](../../../Sales/Delivery/DeliveryPlanning/wDeliveryPlanning.htm) procedure, the block is shown if Block delivery has been checked on the order's invoicing plan, at the same time as the advance has not been paid. In this mode, it is not possible to start picking the order. However, any order rows not included in the invoicing plan, are OK to start picking.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlanDeliveryPlanning.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanDeliveryPlanning.png)

#### Report delivery
In the [Report delivery](../../../Sales/Delivery/ReportDelivery/wReportDelivery.htm) procedure, a warning or a block will be shown if the advance invoice has not been paid, in the same way as when performing delivery planning.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlanReportDelivery.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanReportDelivery.png)
You delivery report the order as usual, but when the invoice basis is created (when saving), extra rows (services) are inserted. These will deduct the partial invoices according to the invoicing plan. The deduction is made in proportion to the delivered value.
Example:
Total order value: EUR 100,000
Invoicing plan:
Advance 30% – EUR 30,000
Delivery 60% – EUR 60,000
In arrears 10% – EUR 10,000
Order value that is being delivered: EUR 50.000
This results in an invoice with deduction of advance and in arrears as follows:
Delivered value: EUR 50,000
Deduction for advance: EUR -15,000
Deduction for in arrears: EUR -5,000
Total invoice value: EUR 30,000
Also remember the following:
- Deduction is only made for the order rows which have been marked with Included in invoicing plan.
- Rows added at the delivery reporting are not considered to be included in the invoicing plan, and therefore no deduction is made for these rows.
- The system will never deduct more than the value of the advance/in arrears, for example if you deliver a larger quantity that what was ordered.
- When deleting remaining quantity during delivery reporting, deduction will take place based on the delivered value. No deduction will be made for the deleted value.
An excess delivery or a delivery with a deleted remainder, will lead to a total invoiced value on the order which differs from the value you planned to invoice. Such a remaining record can be deleted via [Register customer order](../../../Sales/Orders/RegisterCustomerOrder/wRegisterCustomerOrder.htm).

#### Invoice delivery
In connection with the delivery, a basis is created for a delivery invoice. These invoices are invoiced in the regular way via the [Review/Approve invoice](../../../Sales/Invoicing/ReviewApproveInvoice/wReviewApproveInvoice.htm) procedure.
The delivery invoice contains the order row which have been delivery reported as well as deductions for advance invoices and invoices in arrears. It is also possible to create a comprehensive invoice, if there are multiple partial deliveries for the same customer order.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/InvoicingPlanInvoice.png)](../../../../Resources/Images/TrainingMaterial/InvoicingPlanInvoice.png)
On the invoice you see information about the invoicing plan in the same way as on the advance invoice. But here will also see which amounts have been invoiced, as well as the amounts left to invoice.
On the invoice you will also see information about the invoice number on advance invoice.
