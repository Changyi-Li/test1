### Payment terms
In this table you register payment terms. Payment terms indicate the credit time within which payments of invoices should be made.
For customers and suppliers you select a payment term that determines the credit time that will be registered by default on quotes, inquiries, customer and purchase orders.
You find settings that determine which default payment term should be set on credit invoices and interest invoices.

#### Default
Here you can select the default payment term for new customers or suppliers.

#### Number
Here you can see the number for the position of the row. This field is numerical. A new row will by default be assigned the next available number. The table/list is sorted by this column. A number is unique and cannot occur on more than one row in the table.

#### Name
Here you enter a name of the payment terms in question. By using the button Translations ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_translate.png) you can translate the text to the different active languages registered in the system. Read more about [language management](../../../UserGuide/GeneralFeatures/GeneralFeatures.htm#LanguageManagement) for translatable texts.

#### Code
Here you enter the code for the payment term using a maximum of 15 characters. The code is used by the option Customer order transfer in order to match this payment term with a payment term in the other company when customer orders are transferred from the sales company to the production company. If the same code is used for a payment term in both companies, the payment terms will match.

#### Number of days
Here you enter the credit time in number of days for the payment term. If you enter more than zero (0) days, the invoice type will always be Invoice. However, if you enter zero days you can select another invoice type (see below).

#### Cash discount
By using the button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_more_info.png) you can register up to three different cash discount limits in percent. The number of days for the discount limit must be fewer or the same as the number of days on the payment term. The limits cannot have the same number of days.

#### Basis for cash discount
With this setting you determine if the cash discount should be based on the gross amount or the net amount. When using the net amount it means that the VAT will not be affected by the cash discount when the payment is recorded.
A supplier invoice has a payment term with a 1% cash discount when making the payment within 7 days, and the basis for cash discount is set to net amount. The invoice amount is EUR 62,500 incl. 25% VAT (EUR 12,500). When the payment is made within 7 days, and since the cash discount is based on the net amount (EUR 50,000), the amount to pay is EUR 62,000. In the bookkeeping, EUR -500 will be recorded on the account for discounts.

If the same supplier invoice would instead use the gross amount as basis for the cash discount, the amount to pay would be EUR 61,875 since the cash discount (EUR 625) is based on the gross amount of EUR 62,500. In the bookkeeping, EUR -125 would be recorded on the VAT account and EUR -500 is recorded on the account for discounts.

#### Method
Here you select terms of payment:
- Days – Enter the number of days for the term in question under Number of days.
- Free delivery month – "Free del. month" means that the credit time starts to apply at the coming turn of the month, calculated from the invoice date.
- End of month – This method resembles the Free delivery month method, but the difference is that the credit time (for example, 45 days) is counted directly from the invoice date, and then the remaining time of the month will be added to when the due date occurs. An example of EOM: The due date is firstly calculated 30 days ahead – for example, June 10 for an invoice sent on May 11. It is then extended to the end of the month (in this example, June 30).
The illustration below shows the differences between the different payment terms.
![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/SubProjects/end_of_month.png)

#### Add days to EOM
If you selected the EOM method, you can also enter a number of extra days after EOM when the due dates should occur (for example, 4 days after End Of Month).

#### Cash discount date from
With this setting you determine how the due date for the cash discount should be calculated for payment terms that have a cash discount and free delivery month. You can choose from Next month or from Invoice date.

#### Invoice type
Here you decide which invoice type should be used when the order is invoiced. It is only possible to link invoice type to a term with zero (0) entered in the Number of days field.
- Invoice – This type is selected by default for new payment terms.
- Internal – This invoice type is for internal use to handle sales of internal customer orders. For example when withdrawing goods for an exhibition or a trade fair, and you want to create a stock withdrawal and a delivery note for this. But you only want to record the invoice as internal sales and not send it to the customer. In many cases you use an internal customer number on the order (referring to the own company or departments in the company). You might also use it when dealing with internal invoicing between group companies.
- Cash receipt – This invoice type is used when making sales where you receive payment directly in connection to when you approve and print the invoice, for example when selling in a store. It can also concern orders where the customer pays using credit cards. For this invoice type you must also select a payment method.
Both cash receipts and internal invoices are automatically set as paid in the accounts receivable when they are invoiced. They have separate document templates and invoice number series (optional). On these invoices you will not see any payment terms.
Posting of these invoice types is recorded in the customer invoice journal. No incoming payment journal will be printed for these invoice types (even though they are automatically paid).
Since the invoicing of cash receipt and internal invoice automatically is set as paid, you can select a default payment method for the payment (only manual payment methods). The payment method affects which cash account the invoice will be recorded on when cash receipts are concerned. For internal invoices the posting is determined by the standard account called Accounts receivable for internal invoices.
You do not have to enter a payment method on internal invoices. The payment method is not important, since the posting is loaded from a standard account and not from the account of the payment method.

#### Payment method
If the invoice type for the payment term is set to Cash receipt or Internal invoice, this field will become activated. Here you must select one of the active payment methods of the type Manual payment registered in the Bank settings procedure.

#### Number of days (factoring)
With this field you determine how cash and cash equivalents should be calculated in the Cash flow forecast procedure for the orders/invoices which have this as payment term. Here you enter (in number of days) when the cash and cash equivalents are expected to be received from the factoring company after invoicing. If cash and cash equivalents, for example, are expected to be received 1 dat after invoicing, you enter 1 in the Number of days (factoring) field. This calculation is also based on the Factoring % field and Fixed factoring fee (see below).

#### Factoring %
With this field you determine how cash and cash equivalents should be calculated in the Cash flow forecast procedure for the orders/invoices which have this as payment term. Here you enter (in percent) how large portion of the invoice amount that is expected to be received from the factoring company after invoicing. This calculation is also based on the Number of days (Factoring) field (see above).
Example: If cash and cash equivalents are expected to be received 1 day after invoicing with 90% of the invoice amount, you should enter 1 in the field called Number of days (factoring) and 90 in the field called Factoring % for the payment term.

#### Fixed factoring fee
This system setting determines if a fixed factoring fee should be applied. The setting is available if the option Number of days (factoring) was selected for the payment term. You can enter a fixed factoring fee per currency.
This setting determines how cash and cash equivalents are calculated in the Cash flow forecast procedure. Enter a fee per currency to handle forecasts shown in foreign currency.
