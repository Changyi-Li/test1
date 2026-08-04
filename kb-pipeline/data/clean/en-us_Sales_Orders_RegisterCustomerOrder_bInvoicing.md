### Invoicing

#### Customer number, invoice
Here you see/enter the customer that should be invoiced after delivery. By default this is the same customer number as on the header row of the order, unless the customer has a different Customer number, invoice in the customer register. The customer number you see here is the customer to whom the invoice should be sent for the order, for example a head office. The customer on the order (the customer number on the header row) is the customer where the order should be delivered.
> Please note! The accounts receivable is updated for the customer of the invoice and the sales statistics is updated for the customer on the order.

#### Invoice type
Here you decide which invoice type the invoice basis has by default when the order is invoiced. If an order has multiple invoice bases, it is possible to enter, if needed, different invoice types for each invoice basis. The default invoice type is determined by the order type and the payment terms registered in the Terms procedure. The available options are:
- Invoice – A normal customer invoice.
- Internal – This invoice type is for internal use to handle sales of internal customer orders. For example when withdrawing goods for an exhibition or a trade fair, and you want to create a stock withdrawal and a delivery note for this. But you only want to record the invoice as internal sales and not send it to the customer. In many cases you use an internal customer number on the order (referring to the own company or departments in the company). You might also use it when dealing with internal invoicing between group companies.
- Cash receipt – This invoice type is used when making sales where you receive payment directly in connection to when you approve and print the invoice, for example when selling in a store. It can also concern orders where the customer pays using credit cards. For this invoice type you must also select a payment method. If you select Cash receipt you must also select a payment method in the next field.

#### Payment method
If the invoicing should be done as cash receipt, select one of the active payment methods of the type Manual payment. Payment methods are registered in the Bank settings procedure.

#### Invoice address
On the order, the invoice address will be loaded according to what has been entered for the customer in the customer register. Clicking the button you can see the invoice address in question. If the Customer number, invoice is the same as the customer number on the order, you can also change the default invoice address for the customer order in question. This is done by checking the box above the invoice address. If the invoice address differs, you will see a symbol ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_broken_link.png) on the Invoice address button. It is also possible to reset the invoice address to the initial address by unchecking the box.

#### Comprehensive invoice
With this setting activated it means that invoice basis for all the delivered orders to the customer in question will be gathered in a comprehensive invoice. This setting is by default configured in the same way as it is configured on the customer. However, you can here change what should apply for the order in question.
In order for it to be possible to create a comprehensive invoice there is a number of criteria which has to be fulfilled. You can read more about this under the heading Comprehensive invoice in the [Invoicing](../../Customers/CustomerRegister/bInvoicing.htm) section of the Customer register procedure.

#### Use invoice number for pro forma
With this setting you decide if the pro forma’s invoice number should be loaded form the invoice basis. This means that the pro forma invoice will be assigned the same invoice number as the regular invoice. The invoice number becomes reserved when you approve the pro forma invoice and this is only possible when you create a pro forma from pick list and from invoice basis. If you approve a pro forma invoice that was created from/based on a customer order, the pro forma invoice will be assigned a number from the pro forma number series.
- No – No invoice number is reserved when you approve the pro forma invoice. The number will instead be loaded from the number series for pro forma invoices.
- Yes, from pick list – Here you determine if the pro forma should get the same number as the regular invoice. An invoice number from the invoice number series is reserved when you approve the pro forma in the Review/Approve pro forma invoice procedure, list type Pro forma Pro forma is a type of customs document which is used during export of goods. It is used to show information regarding the value of what is to be exported (customs cleared). Pro forma documents are also used in other contexts, for example much earlier than the time of delivery when contacting banks to arrange bank guarantees. from pick list.
- Yes, from invoice basis – Determines if the pro forma should get the same number as the regular invoice. An invoice number from the invoice number series is reserved when you approve the pro forma invoice in the Review/Approve Pro forma invoice procedure, list type Pro forma from invoice basis.

#### Invoices
By clicking this button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png), you access a table containing the invoices, invoice bases with status 1-3, credit invoices, if any, and pro forma invoices, created for the order. By clicking the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png) you can preview the document.
For invoices and credit invoices you see the Paid in full date.
If a pro forma invoice is approved or printed, you will see the text Approved or Printed as Status. The pro forma number is also shown.
You can cancel the pro forma invoice (and change the pro forma status back) by clicking the button Delete selected row ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete_row.png) (F6). This is possible to do as long as the order has not reached status 9 (Final delivery made). If you cancel the pro forma, you can register it again for the order in the Review/Approve pro forma invoice procedure. It then keeps the same pro forma invoice number as it had earlier. This is useful if there are new added/modified order rows that should be included on the pro forma.

#### Invoice is pending
This setting determines the status of the invoice basis after delivery. If the setting is activated, the invoice basis will get status 3 (Pending). If the setting is not activated, the invoice basis will get status 1 (For invoicing). The setting is activated by default, if it has been activated on the customer. Here you can change what should apply for the order in question.

#### Invoicing charge
The amount of the invoicing charge is entered by the system setting Amount of invoicing charge. With the system setting Only apply invoicing charge if invoice value is less than you determine that an invoicing charge only will be added when the amount is less than what is entered in the field. The setting is activated by default, if it has been activated on the customer. Here you can change what should apply for the order in question.

#### Factoring
With this setting you select if factoring should be used for this customer order. If factoring is activated for the customer in the Customer register, this checkbox will be activated by default on the Customer order.
