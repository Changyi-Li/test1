### Voucher number series
Here you will see a table with voucher number series. There is one row per series. Data in the table is registered per accounting year.

#### Series
In this field the value of the series is entered/displayed. This is an alphanumerical field where you can use a maximum of 2 characters. The value must be unique.

#### Next voucher number
Here the next voucher number is entered/displayed. If the row is not linked to a journal, the field is mandatory. On new rows, the next voucher number is by default set to 1. The voucher number series and the following numbers are saved per accounting year. When switching year, the number series will automatically start over from 1.
If the row is linked to a journal, it is possible to enter next voucher number when using integration type:
- Via journal – Total
- Via journal – Total per payment day
- Direct per payment day.
When using the following integration types, this field is inactivated:
- Direct per invoice
- Via journal per invoice.
The system will recognize the value selected in the Integration column in the Journals/Integration box. Example. You register a new voucher number series with number 2 and next voucher number 1. Then you link the Customer invoice journal to voucher number series 2 with the integration setting Direct per invoice. The system will then inactivate the field Next voucher number for the Customer invoice journal and no value will be displayed there. This is made since the voucher number is set based on invoice number/consecutive number during this setting.

#### Greatest voucher number used
Here you can see the greatest number that has been used in the voucher number series. This is useful to see if you need to change the voucher number in the series to avoid a conflict.
