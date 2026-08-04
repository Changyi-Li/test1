### Import file

#### File
By using the Path button ![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/button_browse.png) you can enter a path to the file. You will then see the file path in the field.

#### Format template
Here you can select a format among the formats created in the backstage of the procedure. When the system is new, only a standard template is available. If you have made any temporary settings for the format, which have not been saved as a separate template, this will be shown as Current settings (not saved template).

#### Handle negative values in debit/credit
You should activate this setting if you want to be able to import negative values in the debit and credit columns. If the setting is deactivated, the system will show a validation error during the import if negative values exist in these columns. The setting is deactivated by default.

#### Automatic posting of VAT
With this setting you decide if posting of VAT should be generated in connection with the creation of vouchers via this procedure (when you save the import and the voucher is created). This can be useful if the file contains posting concerning sales or purchase which is liable to VAT and you want the system to post the VAT for these transactions. To be able to automatically post the VAT, the amounts in the file must be posted including VAT (gross). The system will in that case re-post these transactions, they will then be posted with the net amount on the intended account and the VAT is posted on the VAT account. In order for VAT to be generated, it is required that the sales account or the purchase account is set to the VAT type called Sales account or Purchase account If the VAT code column is missing in the file, the VAT code entered for the account in the Chart of accounts procedure, will be used instead.

#### Perform automatic postings
Here you decide if the system will generate automatic posting/allocation for the imported vouchers.
