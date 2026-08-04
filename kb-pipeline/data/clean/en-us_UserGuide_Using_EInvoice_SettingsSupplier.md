### Settings for supplier

#### Supplier register/Supplier list
E-invoice address (EIA)
You can also enter an E-invoice address (EIA) for your suppliers. This address is used to find the correct supplier when importing supplier invoices. The supplier’s Corporate ID number or VAT registration number can also be used to identify the supplier when importing invoices you receive.
Signer code
Enter a Signer code (authorized signer) for the suppliers in order for the invoices to automatically be sent for authorization.
CrossState Slogan
In the CrossState Slogan field, which is exported together with the supplier register to CrossState API, you can enter data which improves matching of suppliers during interpretation. For example, if you have two identical suppliers registered, where the only difference is that one has the currency EUR, and one has the currency SEK, you can enter EUR and SEK in the field for Slogan for each supplier (in order to separate them). You can enter a maximum of 50 characters. The field is only available if you have an account in CrossState.
Send e-invoice invitation to suppliers inviting them to start sending you e-invoices
E-invoice connected – Here you can see if your supplier is connected to e-invoice, which means that the supplier can send you e-invoices. If the supplier is not connected, you can send an invitation to your supplier. You send an invitation by clicking the button called Send e-invoice invitation![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png). A window will then open where you see information about your supplier loaded from Crediflow's e-invoice register. To be able to send an invitation, the system needs to find your supplier in the e-invoice registers. It is therefore important that you have correct information such as corporate ID number, VAT registration number, and country code, entered for your supplier. The supplier has the best chance of being found in the registers if a search can be made using the combination of corporate ID number and country code. It is therefore important that you have the correct corporate ID number and country code entered for your supplier. If everything looks correct, send your invitation by clicking the Send Invitation button. To check the status of an already sent invitation, click Check invitation status ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) again.
If you do not have an e-mail address to your supplier in the e-invoice registers, it is possible to manually add an e-mail address in the Communication box under the Contact information tab. In the Recipient of column, choose E-invoice invitation. An invitation will then be sent to this address.
> If the supplier is new or the details have been changed in the Supplier register procedure, remember that the register must first be uploaded to Crediflow prior to sending the invitation. The register is automatically uploaded once a day, however it is possible to upload manually in the Settings for export/import procedure. [You can read more here](SettingsEInvoiceImport.htm).
Supplier roles
This applies if you have the EIM Workflow option. For the system to be able to separate order invoices and expense invoices you need to configure settings for your suppliers. It is the supplier role on your suppliers which controls whether an invoice from the supplier will be imported as an order invoice, expense invoice, or a mix of these two. Open the Supplier register procedure or Supplier list procedure (choose the Standard list type and the Miscellaneous presentation).
How invoices are imported for different supplier roles:
-   
Material supplier and Subcontractor – invoices from suppliers with any of these roles are imported as order invoices.
-   
Shipping agent and Miscellaneous – invoices from suppliers with any of these roles are imported as expense invoices.
-   
Mix (e.g., Material supplier and Miscellaneous) – PDF invoices will be sent to CrossState for verification. E-invoices are imported as order invoices if there is an order number, and as expense invoices if there is no order number.
> This also applies to invoices which are imported via CrossState as M2M and other types of XML invoices.
