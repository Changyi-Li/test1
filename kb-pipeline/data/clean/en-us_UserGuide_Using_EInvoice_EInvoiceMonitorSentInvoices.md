### Monitoring of sent invoices
To monitor your e-invoices we recommend you to use the desktop component called Crediflow invoice status.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/TrainingMaterial/EInvoiceDesktopComp.png)
The component can be configured to show invoices with different statuses. You can also configure for how many days back in time you want to show invoices.

#### Explanation of status with Crediflow
- In queue – Means that the document is sent to Crediflow's API. It has been placed in a queue to be processed by Crediflow.
- Imported – Means that Crediflow has matched the correct issuer and mapped the document and loaded it in the system (Crediflow).
- Exported – Means the document is exported from Crediflow to the receiver.
- Printed – Means exported from Crediflow to the print partner.
- Sent to post – Means sent from the print partner to the post distributor.
- Rejected – Means that either Crediflow has rejected the invoice due to a validation error, or the receiver's operator/system for some reason has rejected the invoice.
- Acknowledged – Means that the invoice has been acknowledged by the receiver.
