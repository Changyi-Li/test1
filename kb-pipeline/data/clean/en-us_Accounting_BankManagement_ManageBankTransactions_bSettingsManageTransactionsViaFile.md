### Settings – Manage transactions via file

#### Payment method
In this field you select with which payment method you wish to confirm. The payment method is linked to the format/import plugin that is used in the confirmation file. Only payment methods of the type Electronic incoming payment can be selected, although the file may contain both incoming and outgoing payment transactions. Settings for the payment method are made in the Bank settings procedure.

#### Path
Here you can see the path to the confirmation file. This path is entered in the Settings for export/import procedure.

#### Load file
With this button you load data from the selected file. If no file has been selected, the button instead opens a path dialog where you can select which file to load. When a file has been loaded, data will be displayed in the tab’s boxes.
Monitor ERP can load confirmation files in the format CAMT053 regardless of the file's version number.

#### File date
Here you see the date when the bank created the file.

#### Voucher number series
Here you see the voucher number series for the voucher. Voucher number series must first be created in the procedure Voucher number series/Journals.

#### Voucher text
Here you select the text that will be used as voucher text for incoming payments that you register, Payments is the default text. In the Voucher texts procedure you can create texts to use as pre-defined voucher texts.

#### Automatic posting of VAT
With this setting you decide if automatic posting of VAT should take place when you register other payments. Please note! The VAT posting will currently only take place in cases where posting takes place on one offset account for the bank account.
The following options are available:
- No – No automatic posting of VAT takes place.
- Yes, post gross amount – The system will re-allocate the posted amount so that the net amount is retained on the posting row, and the VAT amount is posted on a separate row.
> Via the system setting called Automatic posting of VAT on other payments, you can enter which option should be used as default.
