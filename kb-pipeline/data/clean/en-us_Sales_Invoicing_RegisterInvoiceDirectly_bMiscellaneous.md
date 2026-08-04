### Miscellaneous
Here you see/enter miscellaneous information about the invoice basis. The information in this box corresponds to the information in the [Miscellaneous](../../Orders/RegisterCustomerOrder/bMiscellaneous.htm) box on a customer order, apart from the information or differences described below.

#### Status
Here you can select a status for the invoice basis:
- 1) For invoicing – This is the default status of a new invoice basis.
- 3) Pending – This status means that the invoice is pending and cannot be approved for invoicing. With the system setting Status "Pending" as default on invoice basis for new customers you can set this status as default on invoice bases created from customer orders for new customers.
- 8) Approved – This status is used when an invoice basis is approved to be sent to the customer. This status assigned in this procedure or in the Review/Approve invoice procedure.
- 9) Printed – This status is given when an invoice is printed and the printout is approved.
Invoices with status 8 or 9 cannot be edited. You cannot manually change the status of an invoice to 8 or 9.

#### Pro forma
Here you see the pro forma status. If a pro forma invoice is approved or printed, you will see the text Approved or Printed here. Otherwise, the field displays the text None.
You can cancel the pro forma invoice (and change the pro forma status back) by clicking the button Delete pro forma invoice ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_delete.png). This is possible to do as long as the invoice basis has not reached status 8 (Approved). If you cancel the pro forma, you can register it again for the invoice basis in the Review/Approve pro forma invoice procedure. It then keeps the same pro forma invoice number as it had earlier. This is useful if there are new added/modified invoice rows that should be included on the pro forma.

#### Currency
In this field you see the currency which is used when invoicing. When crediting an invoice in a different currency than the company currency, then the exchange rate used on the debit invoice which you are crediting, will be suggested. But it is possible to change the exchange rate.

#### Use forward rate
This setting is only available if you have are registering a new order in a currency other than the company currency. After you have checked the checkbox, you can then enter the forward rate in the field. The exchange rate must be greater than zero (0.00). The use of forward rate can be activated by default by activating the Forward rate setting for the customer in the Customer register procedure. If forward rate is not activated, the exchange rate that applied to the currency at the time of registration (of the order) will be saved instead. The left field displays the Exchange rate on invoice basis and the right field displays the Invoiced exchange rate.

#### Warehouse
It is not possible to change warehouse for an existing saved invoice basis.

#### Customer number, order
Here you see the customer number and customer name for the customer which is registered on the order that is the base of the invoice basis. The purpose is to show if it is a different customer which receive the delivery of the order than the customer who is set to pay the invoice. In the Register customer order procedure you can enter Customer number, invoice in cases where the invoice should be sent to a customer other than the customer on the order. For example, a subsidiary might have placed an order but it should be paid by the parent company.

#### Multiple invoices in e-mail
Determines whether invoices should be attached to a single e-mail or whether each invoice should be sent in a separate e-mail. The default value is loaded from the Customer register.
