### Print revenue calculation journal
After you have saved the revenue calculation you have to print the journal to transfer the journal's values to the accounting. This can be done in the Print revenue calculation journal procedure.
You can select the list by Project and Project type. The voucher date suggested under Settings is always the last day in the current period. The date displayed on the row of each project is the last day in the period where you saved the actual revenue calculation. Since the revenue calculation is made per period, there is only one calculation per project. If you have performed multiple calculations (before the journal has been reset) for the same period, it will be the calculation most recently saved that is loaded to the journal.
If you discover errors in the revenue calculation once the journal has been reset, you have to make the correction/adjustment, if any, on a manual voucher.
There are two list types in the procedure: Revenue calculation journal and Reprint – Revenue calculation journal.

#### Reversal voucher
When printing the revenue calculation journal, it is also possible to automatically create a reversal voucher. This setting is checked by default under Settings in the Print revenue calculation journal procedure.
[![](https://help.monitorerp.cn/CN-MONITOR_G5/en-us/Content/Resources/Images/UserGuide/PCM7.png)](../../../../Resources/Images/UserGuide/PCM7.png)
The date of the the reversal voucher voucher is suggested as the final day of the month after the date you selected in the Date field. When printing and resetting the revenue calculation journal, an accrual for the reversal voucher will be created automatically. You can see this accrual accounting record in the accrual accounting procedures.
If you do not want a reversal voucher to be created automatically you should uncheck this setting. You can manually reverse the voucher in the Register vouchers procedure.
To record the reversal voucher (an accrual accounting record of the reversal voucher type) you should use the Release accrual accounting procedure.
Here you can select by, for example, the type of reversal voucher used for the accrual created via printing of the revenue calculation journal.
> We recommend you to always reverse the recognized income from the previous period before you perform the revenue calculation for the current period.

#### Undo the journal
It is possible to cancel the revenue calculation journal. This will create a reversal voucher, and any accrual record will be removed. If you have released the accrual record, you cannot cancel the journal. Please note that the period/voucher number series must also be open.
