### Miscellaneous
In this box you enter miscellaneous information and configure different settings for the supplier according to the following.

#### Private person
With this setting you can determine if the suppliers is a private person (private supplier). If you activate this setting you can not enter a VAT registration number or a corporate ID number. Instead you will be able to enter a Personal identity number for the supplier.

#### Personal identity number
If the suppliers is a private person, this field is available. You can then enter the supplier’s personal identity number (corresponding to social security number). The personal identity number can be entered with 10 or 12 digits.

#### Minimum order value
In this field you can enter the order value that should apply as Minimum order value for this supplier. The minimum order value should be entered in the company currency.
The default value is 0 which means there is no minimum order value to take into consideration when registering a purchase order. If you have entered a minimum order value you will be shown a warning when registering purchase orders in cases where the order's total value is less than the minimum order value you have entered here.

#### Corporate ID number
Here you enter the supplier’s corporate ID number. If the entered number is already used by another supplier, a message appears.

#### Our customer number
Here you enter our own customer number registered at the supplier. This is shown on the documents that are sent to the supplier.

#### VAT registration number
Here you can enter the supplier’s VAT registration number.
If the entered number is already used by another supplier, a message appears.
By using the VIES validation button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_validate.png) you can check the VAT registration number with VIES (VAT Information Exchange System). VIES is an electronic mean of validating VAT registration numbers of economic operators registered in the European Union for cross border transactions on goods or services. There you get the answer if the number is valid or not. Depending on the national rules on data protection, some countries will also provide the name and address linked to the given VAT number as they are recorded in the national databases. The system also keeps a log over the checks/validations made, and the returned results.
If a VAT number is shown as invalid, you should in the first instance check with the company in question to make sure the number is correct (correct number of characters, correct length and country prefix). If the number, even after checking, continues to be "invalid", you should ask that company to contact his/her tax administration to request that the data in the national VAT Information Exchange System (VIES) be updated (only national tax administrations can update VIES data).
If your own company information is incorrect or out of date, you should contact your tax administration and ask them to correct the information. Keep in mind that some member states/Northern Ireland, require that such requests of updates must be made in writing or via a web form.
Some member states/Northern Ireland require a separate VAT registration for intra-EU transactions (and Northern Ireland) regarding goods and services and only record such VAT numbers in their national databases. Therefore, it is possible that a VAT number, even if correct, will not be validated through VIES, because the owner of that VAT number is not involved in intra-EU transactions (and Northern Ireland) or did not register for such sales.
Read more at [https://ec.europa.eu/taxation_customs/vies/#/faq](https://ec.europa.eu/taxation_customs/vies/#/faq)

#### VIES check
If you have performed a check of the VAT registration number by using the VIES validation button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_validate.png) (see above), you will here see the result of that check. You will find information about the VAT registration number letting you know if it is valid or invalid, and you will also see the date when the most recent check was made.

#### Parent company (supplier)
A supplier can have a Parent company (supplier). This parent company can in its turn have a parent company. This way there can be many levels in the relationships between suppliers.
If you register a blanket order for a parent company, related suppliers (subsidiaries) will be able to register purchase orders that make calls from the blanket order.
This field can be updated in Supplier list, list type Standard, presentation Miscellaneous.

#### Included in
Under the Included in button, the supplier’s parent company is shown.

#### Consists of
Under the Consists of button, the suppliers that this company consists of (the subsidiaries) are shown.

#### EORI number
Here you enter the company’s EORI number (Economic Operator Registration and Identification). You use the EORI number for all customs related business within the EU. It is possible to validate your entered EORI number in relation to the database available with the European Commission. This is done by clicking the EORI number not validated button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) and then the Validate EORI button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_validate.png). After you have validated the EORI number, the information about the company is loaded to the window and you can see if the EORI number is valid or not. The button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) will be changed to ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusFinished.png) if the EORI number is valid. Regardless if the EORI number is valid or not, you can in the tooltip belonging to the button see when the number was most recently validated and by whom.
> EORI-numbers that start with GB are checked against the database administered by HM Revenue & Customs (HMRC).
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EORI_validation_valid.png)](../../../../Resources/Images/SubProjects/EORI_validation_valid.png) [![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EORI_validation_invalid.png)](../../../../Resources/Images/SubProjects/EORI_validation_invalid.png)

#### Supplier number on invoice
If you want another supplier number to be printed on invoice bases after arrival reporting, you should enter it in this field. The supplier number on invoice is used e.g. when the purchase order has been sent to one company but it is invoiced from another company, for example from a central storage etc.

#### Days of grace for order confirmation
Here you enter the number of days that should pass before a reminder should be sent to the supplier saying that you have not received an order confirmation. This setting applies to all orders that have a printout date which has been passed by the entered number of work days, or more.

#### Days of grace for delivery
Here you enter the number of days that should pass before a reminder should be sent to the supplier saying that you have not received a delivery. The days of grace are always entered in work days.

#### Authorized signer
Here you enter who is the authorized signer. This person is then automatically used as authorized signer of supplier invoices from the supplier in question.

#### Signer code
If you have activated the EIM option, you will see this field instead of the field mentioned above. You here enter a code for the person or for the list of persons that are authorized signers. This will be used by default on supplier invoices from the supplier in question.

#### Other invoice settings
E-invoice address (EIA)
You can enter an E-invoice address (EIA) for suppliers that sends e-invoices. This address can be used to find the correct supplier when importing supplier invoices. You can also use the supplier’s corporate ID number or VAT registration number to find the correct supplier during import.
E-invoice connected
(Applies to those who have an account for E-invoice CrossState and import e-invoices via Crediflow). Here you can see if your supplier is connected to e-invoice, which means that the supplier can send you e-invoices. If the supplier is not connected, you can send an invitation to your supplier. You send an invitation by clicking the button called Send e-invoice invitation![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). A window will then open where you see information about your supplier loaded from Crediflow's register. If everything looks correct, send your invitation by clicking the Send Invitation button. To check the status of an already sent invitation, click the Check invitation status button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) again.
> To be able to send an invitation, the system needs to find your supplier in the e-invoice registers. It is therefore important that you have correct information such as corporate ID number, VAT registration number, and country code, entered for your supplier. The supplier has the best chance of being found in the registers if a search can be made using the combination of corporate ID number and country code.
Do not create invoice basis
This setting is only visible if you have checked any of the alternatives for the system setting Create invoice basis at arrival of. If the checkbox is activated, it is not possible to link orders to supplier invoices from the supplier.
Use VAT amount from imported invoice
Here you decide which VAT amount should be used for imported invoices for the supplier in question. You can choose if the VAT from the invoice should be used or if the VAT code from the supplier register should be applied. Another option here is According to setting which is the default option.

#### Stray supplier
A stray supplier is a supplier number used for one-time purchases from different actual suppliers. These suppliers do not have to be registered in the supplier register. For suppliers marked as stray suppliers, you fill in all the fields on the order instead. Reminders, if any, for that supplier number will be divided per order, and they will not be gathered in one reminder, as otherwise, when this setting is not selected. That way, you can separate the reminder printouts for the different actual suppliers.

#### Calendar
Here you can link a calendar to the supplier. The default calendar is the one selected in the Company information procedure. You register calendars in the Calendars procedure. A calendar determines which days are days off from work and holidays.
If a delivery date selected on inquiry row, purchase order row, and purchase order suggestion, is a holiday or a day off from work in the calendar in question, you will see a warning in the affected procedure. Please note! CDT CDT is short for check delivery times and it is a function on order rows which calculates when the order row in question can be delivered, taking lead times and throughput times into consideration. CDT also checks if existing orders and suggestions can cover material shortages, if any, and affects when the order row can be delivered. takes the supplier's days off from work into consideration.
If the Default delivery date on order rows system setting is set to Today + lead time it means a delivery date calculated for purchase order rows will never be set to one of the calendar's holidays or days off from work. For example, calculations for check delivery times, net requirement calculations, and purchase order created from manufacturing orders.

#### Calendar exceptions
Here you can add date intervals that are exceptions or additions to the selected calendar, and these will apply specifically to the supplier in question. These are dates when the supplier is closed for business, such as during holiday periods.
> For subcontractors, you enter calendar exceptions in the Production calendar procedure.
Printouts
Under the Printouts button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you configure different settings for printing orders and other documents for the supplier.

#### Print order/inquiry via
With this setting you determine if printout of purchase order and inquiry should be made using a printer or via e-mail. The method you select here will be the default option for purchase orders and inquiries to the supplier in question.

#### Print statement via
With this setting you determine if printout of the statement should be made using a printer or via e-mail. The method selected here will be the default for statements to the supplier in question.

#### Print delivery note/transport label via
With this setting you determine if printout of delivery note (for subcontract) and transport label should be made using a printer or via e-mail. The method you select here will be the default option for delivery notes and transport labels to the supplier in question.

#### Multiple orders via e-mail
Determines whether multiple purchase orders should be attached to a single e-mail or whether each purchase order should be sent in a separate e-mail.
You use the system setting called Maximum size for files in e-mail to determine the allowed size of these attachments. If the attached files in one e-mail message are bigger than the entered size in MB in the system setting, the e-mail message and the attached files will be split into two or more e-mails. The default size is 10 MB.

#### 2D code template
Here you can select a 2D code template which will be used to interpret the QR code when scanning a QR code during arrival reporting of an entire order. This means you only need to scan one code to perform arrival reporting on the entire order. 2D code templates are created in the 2D code settings procedure.
