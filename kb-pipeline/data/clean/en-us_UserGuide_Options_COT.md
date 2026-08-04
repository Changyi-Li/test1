# Customer order transfer
Customer order transfer is an option in Monitor ERP which simplifies the handling of customer orders between the sales company and production company, when the sales company receives orders from end customers and the production company does the manufacturing for the sales company. You get an automatic transfer and update of customer orders between these companies.

#### Customer order transfer in Monitor ERP
In the customer order transfer option in Monitor ERP you’ll find procedures for connection between sales companies and production companies, setup of settings for customer order transfer, and transfer profiles between the companies.
In customer order transfer there is a procedure where you configure settings for transfer notifications in both the sales company and the production company, for different events such as a customer order being created, modified, or delivered.
There is also a procedure where you handle and monitor the transfers and events taking place between sales company and production company.
A connection determines to which other company (production company) in the Monitor system the customer order transfer should be made.
A setup of settings determine how price, payment terms, order number, delivery times, etc. should be handled on customer orders in the sales company and in the production company.
A transfer profile links a connection to a setup number and connects the production company to the sales company.

#### Synchronize parts
A procedure is also included where you can regularly synchronize a selection of parts between the sales company and the production company. During a synchronization, different part information will be updated. Structures will not be synchronized/updated.
By using transfer profiles, you can link multiple part selections to different production companies in the part synchronization.
The part synchronization is the basis for performing a customer order transfer between a sales company and a production company. It is also possible to identify parts in the production company by using the part number or another part identity.
The Synchronize parts procedure can also be purchased as a separate option used to only synchronize parts between companies, so you do not have to update the parts manually.

#### Customer order transfer and the Product configurator?
If you use both the Product configurator and Customer order transfer options, you can add the Remote configurator option in the sales company to use the configurations that are registered in the production company.

#### Principles
The illustration below shows automatic transfer of customer order using the Customer order transfer option.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/Options/COTFlow.png)
- Order (1) is placed by end customer with the sales company. The sales company registers a customer order (main order). The customer order is automatically transferred to the selected production companies. When the customer order is registered, a corresponding purchase order can automatically be created in the sales company.
- The production company receives the customer order and can make certain changes to it, for example regarding the delivery date on an order row. Such changes are transferred and the sales company's main order will automatically become updated, as well as the purchase order, if any.
- The production company can also add new order rows to the customer order. If a transfer profile is selected on a new order row, the main order of the sales company is automatically transferred and updated, as well as the purchase order, if any. If a transfer profile is not selected on a new order row, it will not be transferred to the sales company. However, new order rows will be added to the same invoice basis.
- The production company delivery report the customer order and print a delivery note. There are two methods:
- Delivery directly to the end customer (2). In this case, the sales company does not require a purchase order. The invoice basis (3) from the production company is automatically transferred to the sales company.
- Delivery to the sales company which then arrival report the purchase order and delivery report the main order to the end customer.
- The invoice (4) is sent from the production company to the sales company and is registered as a supplier invoice in the sales company.
- The sales company sends the invoice (5) to the end customer.
The production company can print a comprehensive invoice to the sales company (for example, once a week). We suggest you do this by exporting EDIEDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. invoice or via Monitor-to-Monitor. You register the supplier invoice in the sales company. We suggest you use import of EDI invoice or Monitor-to-Monitor.
> You can delete transferred orders in the sales company provided the order has not been commenced in any way. The order is also deleted in the production company.
Deleting a transferred customer order in a sales company will delete the customer order in the production company if the status of the customer order is 1 – Registered, 2 – Printed, or 3 – Delivery time cannot be confirmed.
Deleting a transfered customer order in the sales company will delete the linked purchase order if the purchase order’s status is 1 – Registered or 2 – Printed.
Read more [here](../../GeneralRegisters/CustomerOrderTransfer/SettingsForCustomerOrderTransfer/bHeader.htm) to see how invoicing plans are managed together with customer order transfer.
Management of alloy cost and customer order transfer
Alloy costs must be handled separately in the sales company and production company.
The alloy cost that is registered on the sales company’s customer order to the final customer is not transferred to the production company.
If the alloy cost is registered on the production company’s customer order, this is determined by the settings on the part and customer in the production company.
If the production company adds the alloy cost to its customer order, this alloy cost is only written to the sales company’s purchase order with the price and quantity from the production company’s customer order.
Please note that a separate part for alloy cost must be added to all companies. This part must have the same part number in all companies.
Interested in finding out more? Please contact our Sales department using this [form](https://www.monitorerp.com/sv/kontakt/). Want to find out more? Sign up to our upcoming [Monitor Demos](https://www.monitorerp.com/sv/kunskapsbank/effektivisera-med-monitor-erp/monitor-demos/) (Swedish).
