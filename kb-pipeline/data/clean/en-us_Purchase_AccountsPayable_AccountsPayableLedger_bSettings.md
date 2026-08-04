### Settings

#### Ledger date
Here you select the ledger date. This makes it possible to create reports in past time. This is similar to the accounts receivable list. If you have activated the system setting Preliminary entry of supplier invoices, there is an additional factor to take into consideration in the accounts payable list: preliminary entry. In this case, each accounts payable record has two types of accounting dates: voucher date (which states the accounting date of the final recording) and preliminary entry date. Furthermore, two types of accounts payable accounts are handled: accounts payable (i.e. supplier debts) and preliminary supplier debts.
Example when applying preliminary entry of supplier invoices:
Invoice 1 (account 2442) for 1000 kronor (SEK) is preliminary recorded 2016-01-31.
Invoice 1 (account 2440) for 1000 kronor (SEK) is final recorded 2016-02-10.
If you do a search in the accounts payable list for account 2442 and date 2016-01-31, you find the invoice and it matches the general ledger. That invoice is found when doing a search for all dates up to 2016-02-10. As of that date, the final recording date is found.
If you do a search for account 2440 and date 2016-01-31, you do not find the invoice since it is not final recorded until 2016-02-10.
If you do a search for 2442 and date 2016-02-10 you will not find anything. This corresponds to the general ledger which now has 0 kronor (SEK) on the account 2442 for the date 2016-02-10.
If you have not selected by account in the Selection tab, the invoice is included regardless. The account that is displayed is the one that applied up to and including the accounts payable date you entered in the selection.
This setting is not available for the list types Payments and Bookkeeping.

#### Convert price each according to rate type
With this setting you determine if "price each" in foreign currency should be converted to the present exchange rate in the Currencies procedure. If the checkbox is not checked, the exchange rate saved on the record will be used instead. Which rate type to use is selected in the field below.

#### Rate type
The rate type you select here is used to convert "prices each" and price lists in foreign currency to the now applying exchange rate for the selected rate type. The default rate type is From supplier/order type. You register rate types in the Currencies procedure.
Columns and totals referring to remaining amounts in the company currency are recalculated according to the rate type you select in the field below. These two settings are only available for the accounts payable lists.

#### Base age interval on
(Age analysis) With this setting you determine if the time intervals should be based on the Due date or the Invoice date of the invoices.

#### Include
With this setting you decide which statuses the invoices must have to become loaded to the list. There are different alternatives to select among depending on which list type you have chosen.

#### Include fully paid
With this setting you decide if invoices that are fully paid also should be loaded to the list. The setting is only available for the accounts payable lists.

#### Show unpaid
(Applies to the Payments list) This setting determines if unpaid accounts payable records also should be included in the list.

#### Interval 1–3
Age analysis. Here you can create three different intervals. You enter the number of days back in time (that is, within which interval) in order to show when the remaining amounts on invoices became overdue. The remaining amounts are displayed in the company currency.
Examples
Interval 1 is set to 30 days: invoices that have become overdue between 1–30 days back in time.
Interval 2 is set to 30 days: invoices that have become overdue between 31–60 days back in time.
Interval 3 is set to 30 days: invoices that have become overdue between 61–90 days back in time.
Interval 4: invoices that have become overdue after 91 days and back in time.
