### List
In the upper box, the total amount of the goods records is summarized per combination of Country, CN code, and Transaction type. In the lower box, you can see the detail records included in the row that has been selected in the upper box. The information in the upper box must be included in the report for Intrastat Intrastat is the system which gathers statistics relating to trade in products within the European Union. Gathering of Intrastat statistics is handled in the same way by all EU member states. import.
The data in the upper box is loaded from:

#### Supplier invoices
Data is loaded from final recorded supplier invoice rows with links to parts, accounts payable, and other tables. The date selection under the Selection tab is made against the voucher date on the supplier invoice. Please note! The date in the supplier invoice journal is taken into consideration if the voucher date has been changed manually.

#### Stock order
Data is loaded form arrival rows in the database. The date selection under the Selection tab is made against the delivery date on the rows (the entered date, not the log date).

#### Purchase without active order link
Data is loaded from arrival rows, since you do not link supplier invoices to these. The date selection under the Selection tab is made against the delivery date on the rows (the entered date, not the log date).

#### Adjustment log
Data is loaded from the Instrastat adjustment log. In this log you find, for example, time, adjustment date, CN code, country, transaction type, amount.
