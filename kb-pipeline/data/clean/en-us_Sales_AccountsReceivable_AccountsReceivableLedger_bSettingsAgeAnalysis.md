### Settings – Age analysis

#### Ledger date
Here you select the date for which the accounts receivable should be printed. Today's date is entered by default in this field, but it can be changed. You can e.g. enter a date in past time to reconcile the accounts receivable against the general ledger at a given time.

#### Include
With this setting you determine the types of invoices that will be included in the list: debit invoices, credit invoices, and zero invoices.

#### Convert price each according to rate type
With this setting you determine if "price each" in foreign currency should be converted to the present exchange rate in the Currencies procedure. If the checkbox is not checked, the exchange rate saved on the record will be used instead. Which rate type to use is selected in the field below.

#### Rate type
The rate type you select here is used to convert "prices each" and price lists in foreign currency to the now applying exchange rate for the selected rate type. The default rate type is From customer/order type. You register rate types in the Currencies procedure.

#### Base age interval on
With this setting you determine if the time intervals should be based on the Due date or the Invoice date of the invoices. An age analysis based on due date shows how the invoices will become overdue according to different time intervals. The remaining amounts are displayed in the company currency. An age analysis based on invoice dates shows when you have invoiced according to different time intervals.

#### Interval 1–3
Here you configure three different intervals. You enter the number of days back in time for the age analysis, counted from today's date. The default option here is 10 days in each interval. The invoice amounts within the intervals are shown in three columns in the list. Base age interval on With this setting you determine if the time intervals should be based on the Due date or the Invoice date of the invoices.
Examples
Interval 1 is set to 30 days: invoices that have become overdue between 1–30 days back in time.
Interval 2 is set to 30 days: invoices that have become overdue between 31–60 days back in time.
Interval 3 is set to 30 days: invoices that have become overdue between 61–90 days back in time.
Interval 4: invoices that have become overdue after 91 days and back in time.
There is also a column called Total A/R in the list. It shows the total outstanding amount. That is, it shows what is older than the three intervals you have configured. That column is dynamical and is always adapted in relation to your intervals.
