### Alternative customer information

#### Alternative customer number
By clicking the button Alternative customer number ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can add alternative customer numbers. It might for example be a GLN (Global Location Number) which is used to identify a place/location or a company. GS1 has created a global standard regarding how GLN should be put together. Alternative customer numbers can also be used as search terms for customer identity in EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. behaviors. You can export this number as a unique delivery recipient's E-invoice address (EIA) in the PEPPOL format, even though the invoice is sent to a different recipient (different EIA). Alternative customer number can be entered directly on the customer, order customer ("customer number, invoice"), and on "customer number, invoice". An alternative customer number is unique for each customer. You will receive a warning if the number you enter is already entered for another customer. The field is alphanumerical and can contain a maximum of 25 characters.

#### Identities in "Message header"
Additional sender identities and receiver identities for EDI messages for customers and suppliers using EDI. Values entered here will be exported in the section called MessageHeader in Monitor’s EDI format.
Receiver:
- Receiver ID – The ID of the receiver.
- Qualifier – The qualifier for receiver ID.
- Routing address – The routing address for receiver ID.
Sender:
- Sender ID – The ID of the sender.
- Qualifier – The qualifier for sender ID.
- Routing address – The routing address for sender ID.

#### Customer name when searching
Here you can enter an alternative name for the customers which can be used when searching. For a new customer, the customer name is entered in this field by default. If the customer changes its name, then the old name will remain in this field. This way, you can use the old name when searching and still find the customer. You can also enter a group name here on all belonging customers. This way it is possible to find all customer companies within the same company group in the same search.
If you do not enter a name in this field, the name of the customer is name entered on the header row will be used.

#### Alias for BI
Here you can change the record's alias. This alias is used during data mining from records in the database in Monitor ERP to the database for Business Intelligence. The default value of alias is the same as the record's code/number, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on multiple records, for example customers, then data from these will be merged into a joint record in the database for business intelligence.
You activate alias for BI with the system setting Use alias when exporting to Business intelligence.
