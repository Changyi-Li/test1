### The Per supplier list
This list shows the payment history per supplier and it is possible to use the drilldown function. The list can be updated and you can change the payment history for separate invoices. You have to expand the row to be able to update the Payment history field for a specific invoice. That is, you can overwrite the calculated payment history with a value you enter as payment history. This can be useful if, for example, there is a late payment that you do not want to affect the payment history negatively, then you can enter a 0 as payment history for that specific invoice.

#### Payment terms
The payment terms describe the credit time, that is, within which time frame the payment should be made. This is loaded from the accounts payable.

#### Number of employees
Here you see the supplier’s number of employees. This information is loaded from the Supplier register, is such data has been entered.

#### Agreed payment time
Agreed payment time (as an average) is calculated by the system. An agreed payment time is available for each invoice. It is the number of days between the invoice date and the due date. To create this value for a supplier, the system will add together the number of days between the invoice date and the due date for all invoices which have been paid within the selected period of time. Then the total number of days between the invoice date and the due date, are divided by the number of invoices. For example, if two invoices have been paid, one of them was paid after 30 days and the other invoice was paid after 40 days, the agreed payment time for that supplier is 35. No decimals are used. The value is rounded to whole days. This column also displays an average for all suppliers at the bottom of the list.

#### Actual payment time
Actual payment time (as an average) is calculated by the system. The actual payment time is available for each invoice. It is the number of days between the invoice date and the fully paid date. To create this value for a supplier, the system will add together the number of days for all invoices which have been paid within the period of time. Then the total number of days is divided by the total number of invoices. For example, if two invoices have been paid, one of them was paid after 30 days and the other invoice was paid after 40 days, the agreed payment time for that supplier is 35.
Please note! If a separate invoice has a manually entered payment history, the actual payment time for that invoice will be taken into consideration. For example, if payment is made 60 days after the invoice date and the due date was 45 days after the invoice date. (The payment history will then be +15 for that invoice). But if you manually entered 10 as payment history for this invoice, it means that the actual payment time is 55 days instead of 60. No decimals, rounded to whole days. The value is displayed in red if the payment history is 5 or higher. This column also displays an average for all suppliers at the bottom of the list.

#### Payment history
The payment history is a number which describes your company's ability to pay on time. It is the difference between the actual payment time and the agreed payment time. Or, in other words, the number of days between the due date and the paid in full date. 0 is exactly on time and a value greater than 0 means delayed. A negative value is shown when payments are made sooner than planned. The payment history can be edited on invoice level (in drilldown). If you change it, it will be saved as a disregarded payment history for that invoice. No decimals. The value is shown in red if the payment history is 5 or higher. This column also displays an average for all suppliers at the bottom of the list.

#### Invoices late pmt (%)
Here you see how large the share is in percent, out of all invoices, where the payment is late. The number of all invoices with late payment divided by all invoices. This value is displayed without decimals. This column also displays an average for all suppliers at the bottom of the list.

#### Invoiced amount
Here you see the total invoice amount for all paid invoices displayed in the company currency. A total for all suppliers is displayed at the bottom of the list.
