### Parameters

#### Balance brought forward
Here you enter the balance brought forward that should be the start value in the column Balance in the cash flow forecast. Please note that if the forecast is loaded for a selected currency (separate setting), the balance brought forward should be entered in that currency.

#### Bank credit
Here you enter a credit limit for the bank account. You can enter a value here if you have bank overdraft facility on the bank account. The credit limit is normally entered with a negative value. The purpose of entering bank overdraft facility is to make it easier to see how the credit limit situation at the bank looks like further on. This becomes particularly clear when viewing the report in chart form.

#### Consider holidays – Sales
With this setting you determine whether the forecast should add the value of sales records on the Next workday (default) or on the Previous workday, if the date of the record is a holiday. The forecast checks which days that are holidays in the calendar selected with the system setting Calendar for calculation of due date.

#### Consider holidays – Purchase
With this setting you determine whether the forecast should add the value of purchase records on the Previous workday (default) or on the Next workday, if the date of the record is a holiday. The forecast checks which days that are holidays in the calendar selected in the system setting called Calendar for calculation of payment date.

#### Consider cash discount
With this setting you determine if the forecast should take cash discount into consideration. With the use of this you can simulate that everything will be paid on the cash discount date for the records affected by this. If you for example have selected discount limit 1, you simulate that the invoices are paid according to the cash discount date and with that cash discount. The same applies for the other limits. Please note! If you select discount limit 2 and there are invoices which do not have that limit, then the order's regular due date will be used instead. If the regular due date already has passed, then the invoice is displayed as overdue.
When the parameter is set to any of the Yes alternatives, the amounts will be lowered and the cash flow is advanced.
This parameter affects all records except for other payments, that is, quotes, orders, invoice bases, ledgers.

#### Supplier invoice status
Here you determine which supplier invoices to include in the forecast, based on whether they are Blocked and if they are Unpaid, not ordered and Unpaid, ordered. By default, all options are selected.

#### Base customer order on
Customer order can either be based on the order rows' Delivery date (default) or on New finish. "New finish" is the delivery date which can be calculated by the Net requirement calculation You use the net requirement calculation to perform requirements planning based on the customer order backlog, as well as any existing sales forecasts. when Check delivery times is applied.
