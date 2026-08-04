### Miscellaneous
In this box you enter miscellaneous information and configure different settings for the customer according to the following.

#### Credit limit
Here you can enter the amount that should apply as credit limit for this customer. Warnings can be displayed when registering orders and performing delivery reporting, saying that the limit is being exceeded. The default value is 0 (zero). This means that there is no limit. The credit limit is entered in the company currency. By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you will see information about the credit situation.
Bank accounts (in systems where the Customer order transfer option is used)
Clicking the Bank accounts ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button opens a window where you can register one or multiple bank accounts. To the left you can see the accounts you register, and there you can also select which one you wish to use by default. To the right you fill in information for the respective account according to the following. This is primarily used in systems where the Customer order transfer option is used, when you wish to be able to print delivery documents in the customer's name.

#### Bank account type
Here you select which type of account is being registered. You can choose between IBAN, BBAN, UPIC, and Other.

#### Account number/IBAN
Here you enter the bank account number or IBAN, using a maximum of 50 characters.

#### SWIFT/BIC
Here you enter the bank’s BIC or SWIFT code, using a maximum of 20 characters.

#### Clearing number
Here you enter the bank’s clearing number (not used with IBAN), using a maximum of 20 characters.

#### Clearing system
Here you enter the bank’s clearing system (not used with IBAN), using a maximum of 20 characters.

#### Currency
Here you link the bank account to a currency. The currency used by default is the same as the currency in the Export box, but this can be changed. The bank account is primarily suggested based on the currency of the invoice. If the there are several bank accounts in the same currency as the invoice, then the bank account that is set as default will be suggested.

#### Recipient’s country
The recipient’s country is by default the same country as is used in the mailing address, but this can be changed.

#### Country
In this field you enter the country where the bank is situated. By default you will here see the same country as in the mailing address, but this can be changed. The selected country affects the address format that will be applied. If you select a country that does not have a specific address format, a general address format will be applied. You link countries to address formats in the Countries procedure. If you change the country code, the address format will also be changed.
Settings for address
To the right of the Country field you find the Settings for address button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_settings.png) where you can see and add more information that is linked to the bank's country. By clicking the button, a window called Settings for address opens with the fields Language and Document group will appear. In the window you can also see the address format that applies for the selected country. At the bottom of the window you can preview the address according to the address format.

#### Language
The language you select here is the language that will be used in documents to the bank. The language is filled in automatically when you select the country. The field can be edited and you can select any language. This can e.g. be useful when dealing with countries where more than one language is commonly used. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. function, you can select among the languages registered as active in the Language procedure.

#### Document group
In this field you select a document group which determines the document group that will be used by default in documents to the bank. The document group is based on the selected language and is linked to the language in the Languages procedure.

#### Address format
This is an information field displaying the format applied for the selected country. This field is not possible to edit.

#### Preview
Here you can see a preview of the entered address in the address format of the selected country.
By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_in_google_maps.png) you can find and see the location of the entered address in Google Maps.

#### Name
Here you enter the name of the bank.

#### Address
Enter the street address or post office box number of the bank.

#### Zip code
Here you enter the zip code of the bank. If there are zip code tables registered for the country in question in the Zip code register procedure, you can select a zip code by using the Lookup feature.

#### City
Here you enter the city where the bank is situated. This field is automatically filled in if the corresponding information has been entered for the country’s zip codes in the Zip code register procedure.
The City field is available for the following address formats:
- Zip code + City
- City, Zip code (two rows)
- City + State/Region + Zip code.

#### State/Region
Here you enter the state or the region of the bank. This field is automatically filled in if you have entered the country’s zip codes in the Zip code register procedure.
The field State/Region is available in the address format City + State/Region + Zip code. This address format is used e.g. in the U.S.

#### City/Province
Here you enter the city or province for the bank. This field is automatically filled in if you have entered the country’s zip codes in the Zip code register procedure.
The field State/Province is available in the address format City/Province + Zip code. This address format is used e.g. in China.

#### Private person
With this setting you can determine if the customer is a private person (private customer). If you activate this setting you can not enter a VAT registration number or a corporate ID number. Instead you will be able to enter a Personal identity number for the customer.Prices on all documents and price lists sent to the customer will be shown including VAT.

#### Personal identity number
If the customer is a private customer, this field is available. You can then enter the customer’s personal identity number (approx. social security number). The personal identity number can be entered with 10 or 12 digits.

#### Corporate ID number
Here you enter the corporate ID number of the customer. If the customer has activated Factoring under the button Other invoice settings oand factoring is made via the Peppol BIS 3.0 plugin, then a corporate ID must be entered for the customer.

#### Our supplier number
Here you enter the supplier number that is registered for the company at the customer.

#### VAT registration number
Here you enter the customer’s VAT registration number. This number is printed on different documents to the customer. If the entered number is already used by another customer, a message appears.
Under the Alternative delivery addresses button, you can mark Exception VAT reg. no. and enter a VAT registration number for the alternative delivery address. This VAT registration number will then override the VAT registration number on the customer.
By using the VIES validation button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_validate.png) you can check the VAT registration number with VIES (VAT Information Exchange System). VIES is an electronic mean of validating VAT registration numbers of economic operators registered in the European Union for cross border transactions on goods or services. There you get the answer if the number is valid or not. Depending on the national rules on data protection, some countries will also provide the name and address linked to the given VAT number as they are recorded in the national databases. The system also keeps a log over the checks/validations made, and the returned results.
If a VAT number is shown as invalid, you should in the first instance check with the company in question to make sure the number is correct (correct number of characters, correct length and country prefix). If the number, even after checking, continues to be "invalid", you should ask that company to contact his/her tax administration to request that the data in the national VAT Information Exchange System (VIES) be updated (only national tax administrations can update VIES data).
If your own company information is incorrect or out of date, you should contact your tax administration and ask them to correct the information. Keep in mind that some member states/Northern Ireland, require that such requests of updates must be made in writing or via a web form.
Some member states/Northern Ireland require a separate VAT registration for intra-EU transactions (and Northern Ireland) regarding goods and services and only record such VAT numbers in their national databases. Therefore, it is possible that a VAT number, even if correct, will not be validated through VIES, because the owner of that VAT number is not involved in intra-EU transactions (and Northern Ireland) or did not register for such sales.
Read more at [https://ec.europa.eu/taxation_customs/vies/#/faq](https://ec.europa.eu/taxation_customs/vies/#/faq)

#### VIES check
If you have performed a check of the VAT registration number by using the VIES validation button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_validate.png) (see above), you will here see the result of that check. You will find information about the VAT registration number letting you know if it is valid or invalid, and you will also see the date when the most recent check was made.

#### EORI number
Here you enter the company’s EORI number (Economic Operator Registration and Identification). You use the EORI number for all customs related business within the EU. In the Document templates procedure you can add the EORI number in the document component Header – Sales.
It is possible to validate your entered EORI number in relation to the database available with the European Commission. This is done by clicking the EORI number not validated button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) and then the Validate EORI button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_validate.png). After you have validated the EORI number, the information about the company is loaded to the window and you can see if the EORI number is valid or not. The button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) will be changed to ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) if the EORI number is valid. Regardless if the EORI number is valid or not, you can in the tooltip belonging to the button see when the number was most recently validated and by whom.
> EORI-numbers that start with GB are checked against the database administered by HM Revenue & Customs (HMRC).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EORI_validation_valid.png)](../../../../Resources/Images/SubProjects/EORI_validation_valid.png) [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EORI_validation_invalid.png)](../../../../Resources/Images/SubProjects/EORI_validation_invalid.png)

#### Parent company (cust.)
A customer can have a Parent company (customer). This parent company can in its turn have a parent company. This way there can be many levels in the relationships between customers.
If you register a blanket order for a parent company, related customers (subsidiaries) will be able to register customer orders that make calls from the blanket order.
This field can be updated in Customer list, list type Standard, presentation Miscellaneous.

#### Included in
Under the Included in button, the customer’s parent company is shown.

#### Consists of
Under the Consists of button, the customers that this company consists of (the subsidiaries) are shown.

#### Forward rate
The setting Forward rate only applies if the customer has a currency other than the company currency. If that is the case, you can check this setting if new customer orders for the customer by default should have the corresponding setting Forward rate activated. Then you get to enter the forward rate that should apply, on each new order. The forward rate entered for an order also applies during invoicing.

#### Stray customer
"Stray customer A customer which only makes an occasional purchase. "Stray customer" is a customer number that is used for different customers for one-time sales (non-recurring). Therefor these customers do not have to be registered in the customer register." is a customer number that is used for different customers for one-time sales (non-recurring). Therefore, these customers do not have to be registered in the customer register. If the setting Stray customer has been checked it means that printouts of reminders, if any, for that customer number will be divided per invoice and will not be gathered to a single reminder. That way, you can separate the reminder printouts for the different physical customers.
For stray customers (occasional customers), the e-mail address entered in the invoice header will always be used when sending invoices via e-mail. The e-mail address from the Customer register is never used, regardless of how the setting Recipient of invoice via e-mail is loaded from is configured.

#### Use VAT registration number from customer number, invoice
In the system it is possible to use the function Customer number, invoice. This means that you have two different customer numbers involved in the sales flow. On one hand, you have the customer number on which the order was registered and on the other hand you have the customer number that is used on the invoice, that is, the customer number that will receive the invoice. This setting will be marked by default when you have entered a customer number, invoice. EC sales list and Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. export will then load the VAT registration number from the customer entered under Customer number, invoice. This also means that it is the invoice customer’s VAT registration number which is shown on the customer invoice document and which is recorded in the EC sales list and the Intrastat report.

#### Customer no., VAT agent
This field can be applied when using EDI EDI is the acronym of Electronic Data Interchange. EDI is about exchanging electronic business documents with your business partners, e.g. customers and suppliers. The EDI concept can be wide and a bit unclear, and can many times be used about all types of documents which are sent electronically, even if it might be PDF files sent via e-mail or publishing business documents on a website. What we refer to as EDI – and what is traditionally meant by EDI – is structured business documents following given standards, electronically sent or received and which are compiled and interpreted automatically and that is integrated with the customer's/supplier's ERP system.. Here you can select if another customer will act as VAT agent. The VAT agent is included in the EDI export format for customer invoice.
Printouts
Under the Printouts button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you configure different settings for printing orders and invoices for the customer.

#### Print order/quote via
With this setting you determine if the printout of the orders should be made using a printer or via e-mail. The method selected here will then be the default method on customer order to the customer in question.

#### Print invoice via
With this setting you determine if the printout of the invoices should be made using a printer or via e-mail. The method selected here will then be the default method on invoice to the customer in question.

#### Print pro forma invoice via
With this setting you determine if the printout of the pro forma invoice should be made using a printer or via e-mail. The method selected here will then be the default method on pro forma invoices to the customer in question.

#### Print payment reminder/statement via
With this setting you determine if printout of payment reminder/statement should be made using a printer or via e-mail. The method selected here will be the default method on payment reminders/statements to the customer in question.

#### Print agreement report via
With this setting you determine if printout of the agreement report should be made using a printer or via e-mail. The method selected here will then be the default method for agreement reports to the customer in question.

#### Multiple orders via e-mail
Determines whether multiple order confirmations should be attached to a single e-mail or whether each order confirmation should be sent in a separate e-mail.
You use the system setting called Maximum size for files in e-mail to determine the allowed size of these attachments. If the attached files in one e-mail message are bigger than the entered size in MB in the system setting, the e-mail message and the attached files will be split into two or more e-mails. The default size is 10 MB.

#### Multiple invoices in e-mail
Determines whether invoices should be attached to a single e-mail or whether each invoice should be sent in a separate e-mail.
You use the system setting called Maximum size for files in e-mail to determine the allowed size of these attachments. If the attached files in one e-mail message are bigger than the entered size in MB in the system setting, the e-mail message and the attached files will be split into two or more e-mails. The default size is 10 MB.

#### Merge recipients to the same e-mail
Here you decide whether a single e-mail with multiple recipients should be created instead of sending separate messages to each of the recipients. The same setting is available in all order procedures if you want to make an exception for a specific quotation, customer order, etc.
- Yes – All recipients are added to a single e-mail.
- No – Each recipient will get a separate e-mail.
