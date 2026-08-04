### XML/Documents
In this box you configure settings for XML files and customer-specific documents.

#### Attach XML file
By clicking the ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) button you access settings where you select which XML files should be attached for the corresponding documents you send to the customer by e-mail. The documents that are available as XML files are Order confirmation, Shipment advice, Invoice, and Case.
It is possible to update which XML files should be attached for many customers at a time. This is done in the Customer list procedure by using the Standard list type and the Miscellaneous presentation.
If you have activated the system setting Attach XML file by default for new customers, all the options of XML files will be selected for a new customer.
> Attaching XML files is only relevant when using Monitor-to-Monitor (the customer also runs Monitor ERP), making it possible for the customer to import the XML files in their system. If the customer is using an ERP system other than MONITOR, it is better not to attach XML files due to performance reasons. This is especially the case for Invoice.

#### Select delivery address
Here you select which delivery address to the customer should be suggested at import of customer order from XML file via Monitor-to-Monitor. This setting can also be updated via the General list type, Miscellaneous presentation in the Customer list type. The available options are:
- According to Monitor – (default) The delivery address used on the customer in Monitor ERP will be suggested as the customer's delivery address on the imported customer order.
- According to XML file – The delivery address which is included in the imported XML file will be suggested as the customer's delivery address on the imported customer order.
The suggested delivery address for the customer can also be changed by using the corresponding setting in the import window when the customer order is imported from the XML file.

#### Customer-specific documents
By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) a window opens where you determine if a specific variant of different documents should be sent to the customer. Variants of different documents are created in the Document templates procedure. If you do not make any selections here, then the default document variants in the procedure in question will be used.
For quotes, you can use a document variant per quote type. This is registered under the Quote tab in the Order types procedure. For customer orders you can use document variants per order type for order confirmations, invoices, delivery notes, and transport labels. You register this in the Order types procedure under the Customer order tab. The document variant can be entered per customer in the Customer register.
When registering quotes, customer orders, and invoices, as well as at delivery, the document variant will be applied according to the following priority:
1. The document variant specified for the customer in the Customer register.
2. The document variant specified on the order type in the Order types procedure, under the Quote tab or the Customer order tab.
3. The default document variant in the Document templates procedure.

#### Document settings
By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), a window opens where you can configure if weight and CN code, as well country of origin should be displayed on the documents that you send to the customer. Which of these should be used is loaded from the Countries procedure. From the Country procedure, it is also loaded which type of Trade classification name should be used on the documents, such as, KN, HS or Taric. Other information (weight, country of origin, and codes) is loaded from the Part register. This information can be displayed as text rows on the documents quote, order confirmation, delivery note, invoice, and pro forma invoice. Which decimal separator that is used for weight is determined by the setting found via the Regional formats button in the Customer register. Changes that you make here, if any, which deviates from the default values in the Country procedure, will be marked.
> If you activate the checkboxes, the CN code, weight and country of origin, will also be exported if you send e-invoices. This information is exported to the Note tag for each row in the XML file.
You can also choose to show the Amounts excluding discounts on pro forma invoices. This is useful if discount rows should be hidden from the end customer, in cases where the goods go to the end customer but the invoice goes to a reseller. The end customer in this case does not obtain a discount from the reseller. In some cases you also need to hide discount rows when delivering to certain countries. If you activate this setting it means you will only see the gross amount on the pro forma invoice.
By using the Reset to original button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_cancel.png) you can reset all document settings to the default values from the Countries procedure.
