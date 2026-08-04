### Invoicing

#### Invoice type
Here you see/enter the invoice type of the invoice basis. It is possible to enter different invoice types for different invoice bases for the same order. The available options are describe below. The default invoice type is determined by the order type and the payment terms registered in the Terms procedure.
- Invoice – A normal customer invoice.
- Internal – This invoice type is for internal use to handle sales of internal customer orders. For example when withdrawing goods for an exhibition or a trade fair, and you want to create a stock withdrawal and a delivery note for this. But you only want to record the invoice as internal sales and not send it to the customer. In many cases you use an internal customer number on the order (referring to the own company or departments in the company). You might also use it when dealing with internal invoicing between group companies.
- Cash receipt – This invoice type is used when making sales where you receive payment directly in connection to when you approve and print the invoice, for example when selling in a store. It can also concern orders where the customer pays using credit cards. For this invoice type you must also select a payment method. If you select Cash receipt you must also select a payment method in the next field.
- Collective discount invoice – This can be used when you want to grant a collective discount retroactively based on the sales made to the customer during a specific period of time. You choose a date interval for invoices as basis for the calculation of discount.For the invoices included in the calculation, the total sales amount of the selected invoices is added together. Based on this total, you can specify an overall discount, either as a percentage or as an amount, which will be credited to the customer in the form of a credit invoice. The discount is invoices using a service part with one invoice row per VAT code. To use the invoice type you have to activate the system setting Service part for collective discount invoice.
- Interest – This invoice type is used to charge interest. Read more about charging interest in the topic [Interest invoicing](../../../UserGuide/Using/InvoicingAccountsReceivable/InterestInvoicing.htm).

#### Payment method
If the invoicing should be done as cash receipt, select one of the payment methods of the Manual payment type. This field is mandatory.

#### Credit
Here you determine if the invoice should be a credit invoice. If you check this box, the field Crediting of invoice number will become activated, and you can select the invoice to be credited.

#### Discount period
Here you enter a date interval when using the invoice type called Collective discount invoice. When you have entered a discount period, the Selected invoices window opens where you can choose which invoices to include as basis for the discount. Under Rows you see the invoice rows that will be created, one row per VAT code. Here you can enter the discount in percent or as an amount per invoice row.Under Settings it is possible to adjust the discount period and to include other customers’ invoices.

#### Partial invoice type
If the invoice is included in an invoicing plan, you will here see the type of the partial invoice. The following partial invoice types are available: Advance, Delivery, and In arrears.

#### Credited by invoice number
If the above mentioned invoice number is credited, you will here see the invoice number of the credit invoice.

#### Crediting of invoice number
If the Credit setting is activated, you can here select the invoice which will be credited. A window will then open where you can select the invoice rows to be credited and enter a new price if the price is to be credited. Rows selected in the window will be copied to the credit invoice and you can then adjust most of the main information and invoice rows, e.g. if the quantity on a row should be credited. If you try to credit an invoice which has already been credited, a warning will appear in the validation window.

#### Comprehensive invoice
With this setting activated it means that invoice basis for all the delivered orders to the customer in question will be gathered in a comprehensive invoice. This setting is by default configured in the same way as it is configured on the customer. However, you can here change what should apply for the order in question.
In order for it to be possible to create a comprehensive invoice there is a number of criteria which has to be fulfilled. You can read more about this under the heading [Comprehensive invoice](../../Customers/CustomerRegister/bInvoicing.htm#Samlingsfaktura) in the [Invoicing](../../Customers/CustomerRegister/bInvoicing.htm) section of the Customer register procedure.

#### Invoicing charge
With this checkbox you determine is an invoicing charge should be added on the invoice. This setting is activated by default if it is activated for the customer in the customer register. However, you can change this for the invoice you are registering. The amount of the invoicing charge is entered by the system setting Amount of invoicing charge. With the system setting Only apply invoicing charge if invoice value is less than you determine that an invoicing charge only will be added to invoices where the invoice amount is less than what is entered in the field.

#### Factoring
With this setting you select if factoring should be used for this invoice. If factoring is activated for the customer in the Customer register, this checkbox will be activated by default on the invoice.
