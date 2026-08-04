### Settings for export of e-invoice
The following settings must be configured before you can send e-invoices from Monitor ERP.
> Port 443 or 80 must be open for outgoing traffic in your firewall, so that your system can communicate with Crediflow.
Settings for exporting e-invoices
> Ensure you have entered the correct information (VAT registration number, addresses, etc.) in the Company information procedure before configuring the below settings. Contact our Support Center if you need help regarding how to enter the e-invoice information.
Before you can begin using the e-invoice services in the system, the following settings must be configured:
1. Open the Export tab in the Settings for export/import procedure.
2. Select E-invoice under export type.
3. Check E-invoice Crediflow.
4.       
Click the Create account button. This should be done regardless if you already have a "PartyID" with Creditflow since the procedure runs a check to see if a PartyID exist. If so, your PartyID will be loaded and no new account is created.
If you do not have a PartyID, a new account will be created. Once the account has been created, the Company ID will automatically be filled in. When you activate the function your company will also become activated in the e-invoice network to receive invoices.
Make sure the company information is correct and enter a contact person and that person's contact information.
Also enter a "Message in invitation". This message is used when you send an invitation to the customer asking if the customer wants to receive e-invoices from you.
If you have a GLN number (Global Location Number) registered, please contact the Monitor Support Center to get help to activate it on your account.
5. E-invoice address (EIA) is automatically entered. This information is required to fulfill the Peppol format validations in the system. E-invoice address can for example be the Corporate ID number or VAT registration number.
6. E-invoice address ID (EAID) is automatically entered. This information is required to fulfill the Peppol format validations in the system. In Finland, the EAID is usually "LY-tunnus".
7.   
Enclose embedded PDF in XML decides if an embedded PDF should be attached in the XML file with an e-invoice. The setting is deactivated by default and you manually have to activate it if you wish to attach the PDF file.
8.   
Activate test mode for sending invoices. If you activate test mode you can send invoices for testing of the data in the e-invoices. The test will take place towards Crediflow’s live endpoint, but with test data. The invoices that you send will be handled as live invoices when importing. However, the data will remain with Crediflow and not continue in the process flow. This means you can test status calls, etc.
9.   
The setting Path for manual verification of e-invoice file is used to test/validate e-invoices. If you enter a path, Save to file is shown under the E-invoice column in the Review/approve invoice and Print invoice procedures, where you can choose to save the e-invoice to file in the path you have entered here. At this time an e-invoice is not sent to the operator/customer. The purpose, for example, is to send the e-invoice to the Support Center for troubleshooting (by reprinting), or to send it to a customer for verification before going live. If you enter something in the path, this overrides the setting Activate test mode for sending invoices.
10. Use the Create account button to register an account with Crediflow if you do not already have an account with them. Make sure the company information is correct and enter a contact person and that person's contact information. Also enter a "Message in invitation". This message is used when you send an invitation to the customer asking if the customer wants to receive e-invoices from you. If you have a GLN number (Global Location Number) registered, please contact the Monitor Support Center to get help to activate it on your account.
11.   
Check the I have read and accepted the terms/conditions for this service box.
12. The account is created when you click the OK. This takes place via an API connection to Crediflow. If everything works correctly you will automatically receive your company ID. Now the account registration is completed. If the account registration should fail, you can read more about this below.
13. Save.

#### Deregister account
If you already have an account with Crediflow you can deregister that account in case you no longer will be sending e-invoices.

#### Failed registration of account
Most commonly a failed registration of account is due to the company information/organization information being "locked" by a different e-invoice operator. In that case you first have to contact your old operator and ask them to release your organization information. After that you can register an account.
