### Invoicing

#### Customer number, invoice
By default, "Customer number, invoice" has the same customer number as on the header row. If another customer number by default should be on invoices for orders to the customer, this can be changed here. For example when the customer has a head office which in normal cases should receive the invoices. The customer number in this field will by default be used in the corresponding field Customer number, invoice on new orders for he customer.
> Please note! The accounts receivable is updated for the customer of the invoice and the sales statistics is updated for the customer on the order.

#### Insurance cost
Here you enter a general insurance cost. It is entered in percent (100% to −100%). This cost is charged as a mark-up of the invoice value on all invoices to the customer.
Other invoice settings

#### Comprehensive invoice
Here you can choose if it should be possible to print/send a comprehensive invoice to the customer, containing several invoice bases. The following options are available:
- No – No comprehensive invoice.
- Per customer – One comprehensive invoice per customer.
- Per order – One comprehensive invoice per customer order.
- Per delivery note – One comprehensive invoice per delivery note.
Read about the criteria to fulfill to send comprehensive invoice
In order for it to be possible to create a comprehensive invoice there is a number of criteria which has to be fulfilled. All invoice bases must have the same:
- invoice status
- customer number, invoice
- invoice type
- currency
- exchange rate (if the orders have forward rate)
- setting regarding invoicing charge
- payment terms
- payment term text (when there is a manually entered payment term)
- credit period (when there is a manually entered payment term)
- printing method
- invoice address
- e-mail recipient (if invoice is sent by e-mail)
- order type (if different number series are used for different order types).
The following criteria must also be fulfilled in order to be able to create a comprehensive invoice:
- the customer cannot be a temporary customer (stray).
- the invoices cannot be credit invoices.
- the invoice basis cannot be linked to an invoicing plan, but a delivery invoice within the same order number can be used in a comprehensive invoice.
- if the system setting called Handle suspended VAT during payment of advance invoice is activated, you cannot use comprehensive invoice if the invoice basis is linked to an agreement that HAS accrual accounting.

#### Invoice is pending
If you check this option, the invoice basis will automatically become "pending" (status 3) when the delivery is made to the customer in question. A pending invoice cannot be approved or printed without first changing the status of the invoice basis to status 1 (For invoicing).
By using the system setting Status "Pending" as default status on invoice basis for new customers, you can decide that the checkbox Invoice is pending is activated by default for new customers.

#### Invoicing charge
Check the box if an invoicing charge should be added to the invoices to the customer. The amount of the invoicing charge is decided with the system setting Amount of invoicing charge.

#### Payment reminder
For new customers this setting is checked by default, meaning that payment reminders will be printed. You can modify this for the customer in question. You register payment reminder texts in the Document texts procedure.

#### Reminder fee
Check the box if the customer should be charged a reminder fee. With the system setting Amount of payment reminder fee you enter which amount which should apply for the reminder. A reminder fee is charged only on interest invoices to the customer.

#### Rounding
Determines if rounding should be applied on the amount. Decimal values 1–49 will be rounded down, and decimal values 50–99 will be rounded up.
By using the system setting Default rounding for new customer, you can decide that the checkbox Rounding is activated by default for new customers.

#### Factoring
With this setting you can determine if the customer should be invoiced via bank or via a factoring company. That is, when you e.g. sell your invoices (accounts receivable) to a bank or a company which will then take care of your claim. A plugin for factoring must be installed. You can configure that factoring is marked by default for new customers by using the system setting called Default factoring for new customer.

#### Use invoice number for pro forma
With this setting you decide if the pro forma’s invoice number should be loaded form the invoice basis. This means that the pro forma invoice will be assigned the same invoice number as the regular invoice. The invoice number becomes reserved when you approve the pro forma invoice and this is only possible when you create a pro forma from pick list and from invoice basis. If you approve a pro forma invoice that was created from/based on a customer order, the pro forma invoice will be assigned a number from the pro forma number series.
- No – No invoice number is reserved when you approve the pro forma invoice. The number will instead be loaded from the number series for pro forma invoices.
- Yes, from pick list – Here you determine if the pro forma should get the same number as the regular invoice. An invoice number from the invoice number series is reserved when you approve the pro forma in the Review/Approve pro forma invoice procedure, list type Pro forma Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees. from pick list.
- Yes, from invoice basis – Determines if the pro forma should get the same number as the regular invoice. An invoice number from the invoice number series is reserved when you approve the pro forma invoice in the Review/Approve Pro forma invoice procedure, list type Pro forma from invoice basis.

#### Reference code/Reference number
When e-invoice should be applied, you can here enter the reference code or number with the customer, such as project number, agreement number, or other personal code. This code is included in the export file when e-invoice is sent. In the export file, the reference code/no. will be shown under the "BuyerReference” tag and the customer's reference (name) will be shown under the "Contact" section. If no code is entered, the customer's reference (name) will be placed under the "BuyerReference” tag as well as under the "Contact” section.
The reference code/reference number entered in this field will become default for all invoices to the customer, if no reference code/number has been entered for the selected reference person under the Contact information tab.

#### E-invoice connected
Here you see if the customer is connected to Crediflow. By using the Open Crediflow dialog button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) an online search takes place at Crediflow’s recipient register to see if the customer prefers or allows the suppliers to send e-invoices.
When you search for e-invoice recipients to connect via Crediflow, it is generally recommended that you only use the corporate ID number. This is to improve your chances of getting a match (the exception to this is when you are searching for german customers, see below.) The country code is loaded form the mailing address if you have not entered a separate invoicing address, in that case the country code is primarily loaded from the invoicing address.
For e-invoice recipients in Germany, searches for country code + VAT registration number is prioritized instead of country code + corporate ID number. When searching German e-invoice recipients using VAT registration numbers, it is important to make sure you have entered the number in the correct format, starting with the country code “DE”.
If you have the customer’s VAT registration number or GLN number, this can also be used when searching. Please note! You have to make sure the number is exact since it has to match what has been entered in the different e-registers. The country code is loaded form the mailing address if you have not entered a separate invoicing address, in that case the country code is primarily loaded from the invoicing address.
If the customer has approved Prefers e-invoice
If the customer prefers e-invoice, you can connect the customer directly by checking the Connect checkbox on the row and then clicking the Connect button at the bottom of the window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoice_Connection_PreferEinvoices.png)](../../../../Resources/Images/SubProjects/Einvoice_Connection_PreferEinvoices.png)
If the customer has approved Allows e-invoice
If the customer allows e-invoice, it means that the customer can receive e-invoices but that they want to approve the sender before you can send e-invoices to them. In this case, you send a message with a request to the customer, where the customer can then approve that your company will send e-invoices. To send a request, you check the checkbox under the column Connect and then you use the button Send request at the bottom of the window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EinvoiceConnection_AllowsEinvoice_Request.png)](../../../../Resources/Images/SubProjects/EinvoiceConnection_AllowsEinvoice_Request.png)
When a request has been sent, Request sent is shown next to E-invoice connected under Information at the bottom left of the window. You can also see the date when the request was sent.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EinvoiceConnected_Information.png)](../../../../Resources/Images/SubProjects/EinvoiceConnected_Information.png)
If you want to cancel your request, you use the information button next to Request sent, and then select the Delete request button in the Information about request window.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EinvoiceConnected_InformationAboutRequest.png)](../../../../Resources/Images/SubProjects/EinvoiceConnected_InformationAboutRequest.png)
When you close the Crediflow dialog, you will also see that the status in the field next to E-invoice connected under Invoicing has changed to Request sent.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/EinvoiceConnected_RequestSent.png)](../../../../Resources/Images/SubProjects/EinvoiceConnected_RequestSent.png)
Once the customer has approved your request, the status in the field will be changed to Yes.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoice_Connected_Invoicing.png)](../../../../Resources/Images/SubProjects/Einvoice_Connected_Invoicing.png)
If the customer is not shown in the search result
If you don’t find the customer at all in the recipient register, you can send an invitation to the customer or perform a manual connection (only applies to German customers, see more under Manual connection below.
Send invitation
Invitation, in this case, is distributed by Crediflow and is sent as an e-mail to the customer, asking if they can receive e-invoices. You will receive an answer from Crediflow to the e-mail you have entered when the customer has responded to your invitation. If the customer accepts your invitation, you can do a new search in the register to connect the customer. You send an invitation by using the Send invitation button at the top right of the window.
Manual connection
> Manual connection is needed for customers who want to receive invoices in ZUGFeRD format or who have a Leitweg ID. To be able to ,perform a manual connection the customer's mailing address needs to be registered with Germany as the country.
You can perform a manual connection if you know for certain that the customer wants to and can receive e-invoices, but the custom is not visible/available when you search for it in Crediflow’s recipient register. The purpose of the function is to be able to connect German customers who want to receive invoices in ZUGFeRD format or who have a Leitweg ID (B2G).
Connecting a customer using manual connection is like sending an invitation to a customer, with the only difference being that you, the sender, also accept the invitation on the customer's behalf. Please note! For this reason it is important that the customer’s information is correct and that the customer can receive e-invoices when you perform a manual connection.
> When performing a manual connection, it is important that the information that you enter for the customer is correct, since this is the information the customer will be added with in Crediflow’s recipient register. The register is visible for everyone who searches for the customer to connect e-invoice.
The connection is performed in two steps:
1.    
First, a manual connection is carried out. This is done using the button Open Crediflow dialog![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/G5_Sales_SV/Content/Resources/Images/button_more_info.png). Then click the Manual connection button. Select if the connection type should be Leitweg ID or ZUGFeRD. Depending on your choice of connection type, you need to enter either the customer’s Leitweg ID or the customer’s e-mail address. The correct operator will be selected automatically based on the connection type. Enter the customer’s information, make sure that all the information is correct, and then click the Connect button.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoices_Manual_Connection.png)](../../../../Resources/Images/SubProjects/Einvoices_Manual_Connection.png)
2.   
After a few minutes, when the customer has been registered and verified in Crediflow’s recipient register, you do an e-invoice search for the customer using the customer’s VAT registration number. The compliance for the customer should now be Prefers e-invoice and it should be possible to connect the customer. You connect to the customer by checking the Connect checkbox, and then clicking the Connect button.
> Please note that searching for German customers works better using VAT registration numbers instead of corporate ID number, which is usually the most commonly used search term.
You can also update the ZUGFeRD e-mail address for customers that are already connected by clicking the Update connection button in the Creditflow e-invoice dialog.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/Sales/Customers/Images/FAQ_Snippet_Images/ZUGFeRDuppdateconnection.png) ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Topics/Sales/Customers/Images/FAQ_Snippet_Images/ZUGFeRDManualConnection.png)
Delete e-invoice connection
To delete a customer e-invoice connection, follow the below steps:
1.    
Open the e-invoice connection with the help of the Open Crediflow dialog button.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoice_Connection2.png)](../../../../Resources/Images/SubProjects/Einvoice_Connection2.png)
2.    
Click the information button next to Party-id.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoice_PartID.png)](../../../../Resources/Images/SubProjects/Einvoice_PartID.png)
3.    
Under Party information you select Delete party connection.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/Einvoice_Party_Information.png)](../../../../Resources/Images/SubProjects/Einvoice_Party_Information.png)
4.   
Save the procedure.

#### Use e-invoice
Use e-invoice will activate the following settings to configure. The settings for e-invoice are available on the customer if the option E-invoice has been installed, or if the plugin for Peppol BIS 3.0 is installed. With the setting "Use e-invoice" you decide if the customer by default should receive invoices as e-invoices. In the Print invoice procedure you will also see the E-invoice column in the list. There you see a default Yes when printing invoices to the customer.

#### Distribution method
Here you decide which distribution method should be used when e-invoices are sent via Crediflow. The following options are available:
-   
E- Invoice –(default)
Crediflow distributes the e-invoice to the recipient.
-   
E-mail – (extra service that incurs an additional cost. For more information, please see terms and prices [here](https://www.monitorerp.com/sv/villkor-och-priser-foer-e-fakturering/).)
Crediflow receives the e-invoice and then forwards the embedded/generated PDF invoice to the recipient by e-mail.
-   
Paper (printed) – (extra service that incurs an additional cost. For more information, please see terms and prices [here](https://www.monitorerp.com/sv/villkor-och-priser-foer-e-fakturering/).)
Crediflow receives the e-invoice, prints the embedded/generated PDF invoice on paper and then posts it to the recipient.
> If you wish to send attachments (linked files) together with your invoices, you need to activate the setting called [Enclose embedded PDF in XML](../../../GeneralRegisters/ExportImport/SettingsForExportImport/tExport.htm#E-faktura) in your settings for export of e-invoice. Such linked files/attachments will be distributed in the same way as you selected for invoices.

#### E-invoice address (EIA)
Here you enter the customer's e-invoice address, based on which e-invoice address ID you select in the next field. E-invoice address can for example be the customer's Corporate ID number, GLN number, or the VAT number. E-invoice address (EIA) is automatically loaded when the customer is connected to Crediflow.

#### E-invoice address ID (EAID)
Here you select an option for the customer's e-invoice address ID. The following options are available: Corporate ID number, GLN number, or VAT number. If you choose Swedish VAT number and the customer’s VAT registration number has been entered in the Miscellaneous box, that number will automatically be entered in the E-invoice address (EIA) field above. Please note! The E-invoice address ID (EAID) is automatically loaded when the customer is connected to Crediflow.
