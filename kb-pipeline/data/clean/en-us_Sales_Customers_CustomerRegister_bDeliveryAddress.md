### Delivery address
In this box you enter the delivery address for the customer. When registering a new customer, information from the Mailing address box will be used as default, but it can be changed.
Settings for address
By clicking the Settings for address button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_settings.png) you can change language and document group. This can be used if there should be a different language than the one determined by the Country field in the delivery address address or if a different document group should be used, that is, not the group determined by the language. You also see which address format is used. This is also determined by the selected country. You can also preview the delivery address in the current address format.

#### Languages
The information entered here will affect which language is used on different documents such as inquiries, purchase orders, quotes, and order confirmations. The selected language determine names and extra names of parts and services which are added for example on an order. The language is filled in automatically when you select the country. The field can be edited and you can select any language. This can be useful e.g. for countries with several languages or if the customer/supplier wishes to have all the documents in a certain language, regardless of the country they are sent to. You can select among the languages registered as active in the Languages procedure.

#### Document group
Here you see a default document group for the entered address. The document group determines which texts (phrases) will be shown as headings on documents. The document group is determined by the language selected in the above field, but it is possible to select a different document group. You can select among the document groups registered in the Document texts procedure.

#### Address format
This is an information field displaying the address format for the selected country. The address format is configured for each country in the Countries procedure.
To the right of this button there are buttons you can use to preview the address and to show the address on Google Maps.

#### Name
The company name used in the address. This field is mandatory.

#### Address
The P.O. box address or street address. These rows can consist of a maximum of 50 characters each.

#### Zip code
The zip code of the delivery address. If there are zip code tables registered for the country in question in the Zip code register procedure, you can select a zip code.

#### City
The city of the delivery address. This is loaded automatically from the Zip code register procedure if it has been entered for the Zip code in the country.
The City field is available for the following address formats:
- Zip code + City
- City, Zip code (two rows)
- City + State/Region + Zip code.

#### State/Region
The state or region of the delivery address. This is loaded automatically from the Zip code register procedure if it has been entered for the Zip code in the country.
The field State/Region is available in the address format City + State/Region + Zip code. This address format is used e.g. in the U.S.

#### City/Province
The city or province of the delivery address. This is loaded automatically from the Zip code register procedure if it has been entered for the Zip code in the country.
The field State/Province is available in the address format City/Province + Zip code. This address format is used e.g. in China.

#### Country
Country is mandatory to enter and it determines which language and address format that will be used by default in the delivery address. The language and address format is configured per country in the Countries procedure. If the selected country does not have a specific address format, the general address format will be applied. The country is displayed on the final row of the delivery address on documents.

#### Alternative delivery addresses
Under the Alternative del. addresses you can add additional alternative delivery addresses for the customer. If you add an alternative delivery address you can enter specific information for delivery terms, delivery method, transport distance, goods receiver reference, transport time, delivery days, destination, place of terms of delivery, customer number at shipping agent, customer group, VAT group, and communication information.
Checking the Exception VAT registration number checkbox lets you enter a VAT registration number for the alternative delivery address in the field below. This is used if the invoice will be sent to a central invoicing address, but arrival reporting is done in another place and the customer submits a separate VAT registration number for their purchase (often in another country). This allows the VAT registration number to be shown correctly on the customer invoice, intrastat, and EC sales list in these scenarios without needed to register them as separate customers.
When delivering to a delivery address with a separate VAT registration number, this number is displayed as the buyer’s VAT registration number on sales documents (invoices etc.). This is also the case when exporting orders and invoices to file, as well as other types of export, for example SAF-T, JPK, etc.
When using comprehensive invoicing, the invoice bases that have deviating VAT registration numbers are separated.
Alternative customer number is used for EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system..
You can select which delivery address should be used by default. The default delivery address and its information is loaded by default on for example a new customer order, but then it is also possible to change delivery address on that order. If you change delivery address for a customer order, the related information will also be changed on the order.
