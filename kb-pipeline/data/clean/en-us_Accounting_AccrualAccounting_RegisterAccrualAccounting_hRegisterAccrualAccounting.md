### Header row

#### Accrual number
This field is used for the accrual number for the accrual. If it is a new accrual you are creating, you can either enter a new number here or leave the field empty. If you leave this field empty, the next available number in a number series will be loaded when you save the accrual.
If the accrual is created from another procedure, e.g., Register supplier invoice, the accrual is created and numbered form the number series. This takes place in the background when the actual supplier invoice is created.

#### Voucher text
Here you select a voucher text for the accrual. If you create accruals, this is a text you can enter to describe the accrual in question. This text will be used as voucher text when the accrual is released.
If the accrual is created from accounts receivable/accounts payable and vouchers, then the voucher text will be added automatically. The text which is then added is created based on the type:
- Supplier invoice – The supplier invoice's consecutive number plus the supplier's name.
- Voucher – The voucher number plus voucher text from the voucher.
- Reversal voucher – The voucher number plus voucher text from the voucher which is reversed.

#### Type
The type of accrual is automatically entered if it is created from other procedures. For an already registered accrual it is possible to change the type before the accrual has started the release. The type also affects which fields will be available in the procedure. If you create the accrual in this procedure, the following type options are available:
- Supplier invoice – This option is selected when there is a posting on a supplier invoice which should be accrual accounted.
- Voucher – This option is selected when there is a posting on a voucher which should be accrual accounted.
- Reversal voucher – This option is selected when there is an entire voucher which should be reversed in a specific period. Most of the times it is a reversal in the next accounting period (can also be a future accounting year). This type can also be created via Save as in the Register vouchers procedure.
- Manual entry – This option is selected when there is not a specific entry which should be accrual accounted. For example, if you do not have the fixed assets register in the system and want to register a recording for depreciation which should be released each month. Then there is no link to any specific voucher or supplier invoice.
