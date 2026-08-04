### Settings

#### Pre-select "Include"
This setting determines whether or not the “Include” box should be checked by default for all rows in the list/result.

#### Show blocked
With this setting you determine whether or not blocked invoices should be shown in the list. Even if you choose to show blocked invoices they cannot be paid.

#### Show credit invoices awaiting final recording
With this setting you can decide to show information about credit invoices that are awaiting final recording.
You cannot mark credit invoices to be included if they are not final recorded, but by showing them in the list you can provide useful information to the users letting them know there are credit invoices in the authorization flow. You must now have "coverage" for the entire credit invoice when you send the payment suggestion to the bank (ISO files), that is why it will facilitate your work if you get information early on about credit invoices.

#### Exclude suppliers with negative/zero remaining amount
With this setting you determine if invoices belonging to suppliers that have a total negative (or zero) remaining amount, should be excluded from the list. A negative remaining amount means that the value of the supplier’s credit invoices is greater than the value of the debit invoices. The suppliers who have a total negative or zero remaining amount will not get the Include checkbox marked if you activate this setting.

#### Consider cash discount date
The setting Consider cash discount date also includes invoices that have a cash discount date within the due date entered in the selection. The purpose of this is to be able to pay the invoices on their cash discount date, that is, prior to their regular due date.
> If you have selected Today in the system setting Payment date for overdue electronic payments, today’s date will also be taken into consideration.

#### Payment date when paying manually
Here you select the date for the payment of the invoices. This setting determines the default payment date that should be set on invoices in the list with a manual payment method. The date selected here also determines the payment date under the Pay manually tab.

#### Voucher text
Here you select the text that will be used as voucher text for outgoing payments that you register. The default text is “Outgoing payments”. In the Voucher texts procedure you can create texts to use as pre-defined voucher texts that can be selected in this procedure.
