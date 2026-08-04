### System settings that affect invoice interpretation
There are some system settings that affect the invoices that are imported from CrossState that can be good to be aware of.

#### Use exchange rate from XML file
With this setting you decide if exchange rate from XML file should be used. This setting will affect imported e-invoices, captured/interpreted invoices (CrossState) and M2M invoices. For example, if the supplier sends invoices in a different currency as e-invoices (XML file), this setting determines that the exchange rate in the XML file should be used. This system setting will override the system setting above called Suggested exchange rate during registration. If no exchange rate is included in the XML file, the exchange rate will instead be loaded according to the system setting above.

#### Allowed exchange rate difference on imported invoice
If the Use exchange rate from XML file system setting above has been set to Yes, you should in this setting enter the allowed difference in percent.

#### Use VAT amount from imported invoice
With this setting you decide if VAT from the invoice should be used or not during import of supplier invoice. This setting will affect imported e-invoices, captured/interpreted invoices (CrossState) and M2M invoices. If you select No, the VAT code from the supplier will be used instead. The recommended setting is Yes when you are using invoice interpretation via CrossState.
> Please note that if you choose No, the VAT will be calculated based on the default VAT code in the Supplier register. In this case, the VAT is calculated based on the invoice amount and any differences may therefore need to be adjusted manually.
