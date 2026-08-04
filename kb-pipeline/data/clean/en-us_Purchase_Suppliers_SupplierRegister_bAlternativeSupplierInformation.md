### Alternative supplier information

#### Alternative supplier number
By clicking the button Alternative supplier number ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can add alternative supplier numbers. It might for example be a GLN (Global Location Number) which is used to identify a place/location or a company. GS1 has created a global standard regarding how GLN should be put together. Alternative supplier number is unique for each supplier. You receive a warning if the number you enter is already entered for another supplier.

#### Identities in "Message header"
Additional sender identities and receiver identities for EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system. messages for customers and suppliers using EDI. Values entered here will be exported in the section called MessageHeader in Monitor’s EDI format.
Receiver:
- Receiver ID – The ID of the receiver.
- Qualifier – The qualifier for receiver ID.
- Routing address – The routing address for receiver ID.
Sender:
- Sender ID – The ID of the sender.
- Qualifier – The qualifier for sender ID.
- Routing address – The routing address for sender ID.

#### Supplier name when searching
Here you can enter an alternative name for the supplier which can be used when searching. For a new supplier, the supplier name is entered in this field by default. If the supplier is renamed, then the old name will remain in this field. This way, you can use the old name when searching and still find the supplier. You can also enter a group name here on all belonging suppliers. This way it is possible to find all supplier companies within the same supplier group in the same search.
If you do not enter a supplier name here, the supplier name entered on the header row will be used.

#### Alias for BI
Here you can change the record's alias. This alias is used during data mining from records in the database in Monitor ERP to the database for Business Intelligence. The default value of alias is the same as the record's code/number, but this can be changed.
One of the purposes with alias is to be able to determine for which records data should be extracted to business intelligence. If the alias field is emptied for a record, then no data will be extracted from this record to the database in business intelligence.
Another purpose is to be able aggregate data. If the same alias is used on multiple records, for example customers, then data from these will be merged into a joint record in the database for business intelligence.
You activate alias for BI with the system setting Use alias when exporting to Business intelligence.

#### CrossState "Slogan"
This field is exported together with the supplier register to CrossState API. The field is only available if you have an account in CrossState. You use the field to enter data which will improve the match of supplier in the interpretation. For example, if you have two identical suppliers registered, where the only difference is that one has the currency EUR, and one has the currency SEK, you can enter EUR and SEK in the field for Slogan for each supplier (in order to separate them). You can enter a maximum of 50 characters.
