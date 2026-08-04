### Settings

#### Days of grace
In this field you can enter how many days of grace to apply. The default value is loaded from the system setting Days of grace The term days of grace (or grace period) is used at requirements planning in order to calculate rescheduling of actual orders that cover the requirement but that are too late in time, instead of suggesting a new order. for interest. If days of grace is set to seven days, it means that the customer has seven extra days to pay the invoice without being charged interest (from the interest-free days).
Examples
An invoice date is set to June 1, 2017, with a payment term of 10 days. This means that the due date is June 11, 2017. In the system settings, the Interest-free days has been set to 20 days (from the invoice date), which means that interest will not be charged until 10 days after the due date of the invoice (June 21, 2017).
The days of grace is set to three days. This means that the customer has three more days (in addition to the interest-free days) to pay the invoice without being charged invoice, that is, June 24, 2017.
> [More information about interest-free days.](../../../GeneralRegisters/BasicSettings/SystemSettings/bInterestInvoice.htm)

#### Charge to include
With this setting you can filter which records to include in the list based on how interest charge should be made. The alternatives available are: Interest invoice, Next regular invoice, and No charge. The first two alternatives are selected by default.
When you load the list with the default values, only invoices with payments where interest charge have been activated, will be loaded. Other invoices can also be loaded if you check the option No charge. This can also be used with purpose to mark if interest should be charged for these. Records that are released but not invoiced, will not be loaded to the lists.

#### Minimum amount of interest charge
With this setting you decide the lowest interest amount required in order for a customer’s record to appear in the list. The interest amount must be the same or greater than the amount entered here. The default amount in this field is loaded from the system settings (for example EUR 10). If there are late incoming payments from a customer which have resulted in an interest amount of 5 EURO, this customer’s records will not be included in the list If you temporarily wish to send interest invoices with a lower amount, this can be changed under the Selection tab to included these records in the list and generate an interest invoice even though the minimum amount was not reached.
Please note! The amount limit only concerns records for which you have selected to charge invoice via interest invoice. Interest records marked to be charged on the next regular invoice do not have a minimum amount of interest charge. These will be included in the list regardless of the setting above, and the value of these will not take the minimum amount in the selection into consideration.

#### Order type, interest invoice
Detailed. In this field the customer order type 1 is selected by default. This customer order type is included in the system. You can administer order types in the Order types procedure. The order type selected here will apply as order type for the invoices released via this procedure.

#### Our reference, interest invoice
Detailed. This field is used when releasing interest invoices. The reference you select in this field will be registered as Our reference on the invoice bases that are released.

#### Waiting time for next invoice, warn after
Detailed. 60 days is entered by default, but it can be changed. The purpose of this setting is to in the list display a warning if the invoice has been waiting a long time for the next regular invoice. This is useful in order to see these invoices and possibly change them so the interest should be charged via interest invoices instead. If you enter 60 days for this setting, a warning will be shown for the records where this number of days have passed from the paid in full date. The warning is shown as red color on the paid in full date.

#### Pre-select "Include"
Detailed. With this setting you determine if all rows with Interest invoice selected in the column Interest charge should be selected to include.
