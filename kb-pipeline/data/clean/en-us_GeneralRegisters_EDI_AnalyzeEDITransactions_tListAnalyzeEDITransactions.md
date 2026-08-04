### List – Analyze EDI transactions

#### Customer number, receiver
Here you see the customer number of the receiver.

#### Name, receiver
Here you see the name of the receiver.

#### Part number from file
This is the part number found in the import file.

#### Part name from file
This is the part name from the import file.

#### Customer's delivery schedule date
Here you see the customer's delivery schedule date from the import file.

#### Customer's delivery schedule no.
Here you see the customer's delivery schedule number from the import file.

#### Skipped
Here you see the reason to why the part has been skipped. The following causes/reasons exist:
- From skip list – The part has been skipped because it is found in a Skip list for parts. Read more about [skip list](../EDIChannels/bSkipLists.htm).
- Automatic – the part has automatically been skipped during the import since the EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. behavior has been set to Allow parts of business transactions. Read more about the [Import principle for business transactions](../EDIBehaviors/bSalesBehaviour.htm).
- Manually – The part has been skipped manually by the user (meaning the user has marked the Ignore part) under the Delivery schedules tab in the Handle EDI transactions procedure.

#### Aggregated quantity from calls
Here you see the total number of call-offs for the part in this delivery schedule.

#### Delivery schedule number
This is the delivery schedule number in Monitor ERP, if such has been entered.

#### Usage
How the delivery schedule is used, either Delivery schedule Silf (the Swedish association for purchase and logistics) explain the term "delivery plan" in the following way: A delivery schedule is a plan/schedule for deliveries from supplier to customer. The delivery schedule is created by customer and generally contains a planning horizon of 0,5–1 year. Normally the delivery schedule quantities are assigned different statuses depending on the type of demand. It is common that for example the entered quantities in the immediate future (closest in time) actually are fixed orders. In an interval of a few months ahead of the fixed orders, the entered quantities might be considered as preliminary orders for which the customer is obliged to take financial responsibility for any material purchased by the supplier. The subsequent quantities entered are considered to be forecast only. (Translated from source https://www.silf.se/tjanster/ordlista-for-inkop-och-logistik/l/ [2018-08-29]). A delivery schedule is a way to increase the transparency and thereby make it possible to mutually take charge of the financial situation across multiple steps in the supply chain. This is done by transferring information regarding the immediate demands/requirements as well as future forecast demands. or Call-off. This is loaded from the delivery schedule.

#### Created when
Here you see when the transaction was created.

#### Transaction
Here you see the number of the EDI transaction.

#### Port
This is loaded from the delivery schedule in the EDI transaction. This can be seen via More info.

#### Storage
This is loaded from the delivery schedule in the EDI transaction. This can be seen via More info.
