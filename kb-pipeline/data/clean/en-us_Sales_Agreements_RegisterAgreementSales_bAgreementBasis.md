### Agreement basis
In this box under the Agreement basis tab you find the agreement bases of the agreement. At the top you select for which Year.
If the agreement time does not have a Valid to date, bases will be created automatically for twelve months ahead. If the agreement has a Valid to date closer than 12 months, bases will be created up to the entered date. If the status or agreement time is changed on the agreement, the created bases that are not yet invoiced will be adjusted accordingly. When you create agreement bases, the same number of customer orders will be created at the same time. That is, a one-to-one ratio between customer order and agreement basis.
By using the Release agreement basis button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_release.png), you can release bases for invoicing and the Register invoice directly procedure is opened. In the Release customer agreement basis procedure you can release multiple agreements at a time in a list. When you release an agreement basis, a new basis is created for the final period to make sure there is always bases for the coming twelve months. That is, the agreement bases are created on a rolling 12-month basis (provided that no Valid to date has been entered for the agreement period). A check is made to see if the row has a valid to date that is more than 12 months ahead or if it is blank. It is then assumed by the system that additional agreement bases will be created and the row is not set to Delivered.
By using the Undo release button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_undo_release.png) you can undo the release of bases for invoicing. Please note! Bases which have been invoiced cannot be undone. Instead, these have to be credited before they can be undone. This will change the status of the customer order which was created in the background. It is changed from status 9 to status 1.
Under the Credit invoice ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_add_credit.png) button there are two options, Re-invoice after credit and Invoicing complete after credit. All information from the basis and customer order that are created in the background are loaded.
- Re-invoice after credit backtracks the status of the agreement basis to Registered, and the basis can once again be released after credit. This is used when the customer is to be invoiced once again after you have issued a credit.
- Invoicing complete after credit retains the status of Invoiced on the agreement basis after credit. This is used when the customer is not to be invoiced again after you have applied a credit.
When you credit an invoice, a new customer order row is created containing the corresponding negative record to achieve a correct order inflow.
Use the Suspend ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/StatusOpPaused.png) button to suspend an agreement basis, and it is no longer possible to release the agreement basis. This is useful if you don’t want the agreement basis to be invoiced. This means the agreement basis can no longer be released automatically if you have checked the Release basis automatically setting. When an agreement basis has been suspended, it cannot be released manually.
Use the Resume ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_run.png) button to once again release the agreement basis which is suspended. The Resume button is used to change the status of the agreement basis from Suspended to Registered.
When the agreement basis is released a customer order of the Agreement order type is created in the background. This is done because an invoice basis must be based on a customer order. This special type of customer order of the Agreement order type cannot be edited. Customer orders created from an agreement will get the planned invoicing date of the agreement basis as their delivery date. This makes the cash flow forecast reliable.
You find the Agreement order type in the following places in the system:
The Agreement order type is available for customer orders only for it to be possible to create invoice bases. This order type is only available in the following procedures:
- Register customer order
- Customer order info
- Order list – Sales
- Customer register – the Overview tab
The Agreement order type is not available in the following procedures:
- CRM view
- Print customer order
- Delivery planning
- Pack for delivery
- Report delivery
- Print delivery documents
- Undo delivery reporting
- Register shipment (Source of information)
> Please note! All customer orders connected to an agreement are automatically deleted when you delete an agreement and/or change the status from Active to either Signed/Valid or Negotiation. This is done so that automatically created orders will not remain in the system an cause an incorrect order inflow.
When an invoice has been reviewed/approved and been assigned status 8 Approved (for invoicing), an invoice number is created which is displayed in the Invoice number column.
By using the Show invoice button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_form_viewing.png) you can view the invoice.
By using the Show invoiced agreement basis button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_goto_critical_op.png) you can view the already invoiced agreement bases in the list.

#### Type
Here you see if the row is an Agreement basis, an Invoice, or a Credit.

#### Exchange rate
The following applies for the exchange rate column:
- Not released – The exchange rate shown is loaded from the Header tab.
- Released – The exchange rate shown is loaded from the customer order under the Agreement basis tab.
- Invoiced – The exchange rate shown is the exchange rate from the invoicing.

#### Accrual accounting
When applying accrual accounting to an advance invoice for an agreement, the accrual accounting number is displayed on the row of the agreement basis. It is also possible to go to the accrual record.
Before the agreement basis is released and approved for invoicing, a button is shown on the row where you can see what the accrual will be for the row in question.

#### Period allocation
The Accrual accounting button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) on the basis row displays details such as period, amount, and account for the accrual in cases where the agreement is accrual based.
