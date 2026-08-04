### Outgoing payments
In this box you enter information regarding outgoing payments in the accounts payable.

#### Payment method
Here you select the payment method that should be used when making payments to the supplier in question. You can select between the payment methods registered in the Bank settings procedure. There you can edit and/or add payment methods. This field is mandatory and cannot be left empty.

#### Pay via
Here you can enter another supplier number if the payment should be made via another supplier. By default this field will contain the same supplier number as in the main row, but it can be changed. This can be useful if the supplier who sent the invoices has handed over the invoices to a finance company (for example Nordea Finans, Klarna). This requires that you have registered the finance company as a separate supplier in the supplier register.

#### Reference number
Check this box if reference number should be entered when registering a supplier invoice in the Register supplier invoice procedure. For countries which have official handling of reference numbers, a validation is built in to the field to make a validation error appear if you enter an invalid number.

#### Copy inv. no. to ref. no.
Here you decide if the invoice number should automatically be copied to the Reference number field on supplier invoices.

#### Fixed reference number
Here you can enter a fixed reference number in cases where the supplier has the same reference number for all invoices. This setting becomes available if you have activated the Reference number checkbox.
Bank accounts
By using the Bank accounts button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can register one or multiple bank accounts. To the left you can see the accounts you register, and there you can also select which one you wish to use by default. To the right you fill in information for the respective account according to the following.

#### Bank account type
Here you select which type of account that is being registered. You can choose between IBAN, BBAN, UPIC, and Other.

#### Account number/IBAN
Here you enter the bank account number or IBAN, using a maximum of 50 characters.

#### SWIFT/BIC
Here you enter the bank’s BIC or SWIFT code, using a maximum of 20 characters.

#### Clearing system/Bank code
Here you enter the bank’s clearing system or bank code (not used with IBAN), using a maximum of 20 characters.

#### Currency
Here you link the bank account to a currency. The currency used by default is the same as the currency in the Export box, but this can be changed. The bank account is primarily suggested based on the currency of the invoice. If the there are several bank accounts in the same currency as the invoice, then the bank account that is set as default will be suggested.

#### Recipient’s country
The recipient’s country is by default the same country as is used in the mailing address, but this can be changed.

#### Central bank code
Here you enter the central bank code or payment code that should be used by default for payments to the account, a maximum of 20 characters. Central bank codes must first be registered in the Bank settings procedure.

#### Settings for address
To the right of the Country field you find the Settings for address button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_change_settings.png) where you can see and add more information that is linked to the bank's country. By clicking the button, a window called Settings for address opens with the fields Language and Document group will appear. In the window you can also see the address format that applies for the selected country. At the bottom of the window you can preview the address according to the address format.
Language
The language you select here is the language that will be used in documents to the bank. The language is filled in automatically when you select the country. The field can be edited and you can select any language. This can e.g. be useful when dealing with countries where more than one language is commonly used. By using the Lookup The Lookup feature is a powerful search tool which allows you to search and load information from large registers. You open the Lookup feature by clicking on the dropdown button or by using F4 on your keyboard. function, you can select among the languages registered as active in the Language procedure.

#### Document group
In this field you select a document group which determines the document group that will be used by default in documents to the bank. The document group is based on the selected language and is linked to the language in the Languages procedure.

#### Address format
This is an information field displaying the format applied for the selected country. This field is not possible to edit.

#### Preview
Here you can see a preview of the entered address in the address format of the selected country.

#### Name
Here you enter the name of the bank.
By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_show_in_google_maps.png) you can find and see the location of the entered address in Google Maps.

#### Address
Enter the street address or post office box number of the bank.

#### Zip code
Here you enter the zip code of the bank. If there are zip code tables registered for the country in question in the Zip code register procedure, you can select a zip code by using the Lookup feature.

#### City
Here you enter the city where the bank is situated. This field is automatically filled in if the corresponding information has been entered for the country’s zip codes in the Zip code register procedure.

#### The City field is available for the following address formats:
Zip code + City
City, Zip code (two rows)
- City + State/Region + Zip code.
- State/Region
- Here you enter the state or the region of the bank. This field is automatically filled in if you have entered the country’s zip codes in the Zip code register procedure.

#### The field State/Region is available in the address format City + State/Region + Zip code. This address format is used e.g. in the U.S.
City/Province
Here you enter the city or province for the bank. This field is automatically filled in if you have entered the country’s zip codes in the Zip code register procedure.

#### The field State/Province is available in the address format City/Province + Zip code. This address format is used e.g. in China.
Here you enter the city or province for the bank. This field is automatically filled in if you have entered the country’s zip codes in the Zip code register procedure.
The field State/Province is available in the address format City/Province + Zip code. This address format is used e.g. in China.
Export settings
Under the button Export settings![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you configure which export format and potential exceptions you want to use for the supplier.

#### Export format
Here you decide which export format that should be used. The formats you can choose from are the ones activated under the Bank activation tab in the Bank settings procedure. For the export type called Payment file you then configure settings in the Settings for export/import procedure.
If the selected Payment method to the supplier is linked to a Payment format in the Bank settings procedure, then this format will be set by default here.

#### Exceptions
Does not apply to the export formats Bank integration, Supplier payments LB, LB Nordea, and E-payment Netbox, Nordea, FI. With this setting you can make exceptions for this supplier from the default codes used for the selected export format. It might, for example, be that the supplier has a different payment format or payment method. You can also select a charge code.
For the Danske Bank (Sweden and Norway) and Nordea (Finland), you can make exceptions from batch payment by deactivating the Use batch payment setting.
Charge codes
The following charge codes can be selected:
-   
Automatically selected – Monitor ERP automatically adjusts the charge code based on the currency and the country code.
-   
CRED – The recipient pays the bank charges.
-   
DEBT – The sender pays the bank charges.
-   
SHAR – The sender and the recipient each pay for their own bank's charges.
-   
SLEV – The sender and the recipient each pay for their own bank's charges. Used for SEPA payments.
